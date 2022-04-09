from application import app, db
from flask import render_template, url_for, redirect, request
from flask_testing import TestCase
from application.model import Game, Review, AddGame, AddReview

class TestApp(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATEBASE_URI='sqlite:///:test.db',
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Game(game_name='test_game', category='test_category', publisher='test_publisher'))
        db.session.add(Game(game_name='test_game2', category='test_category2', publisher='test_publisher2'))
        db.session.add(Review(rating=5, game_id=1,  comments="test_comments"))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestList(TestApp):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test_game', response.data)
        self.assertIn(b'test_game2', response.data)
        self.assertIn(b'test_category', response.data)
        self.assertIn(b'test_category2', response.data)
        self.assertIn(b'test_publisher', response.data)
        self.assertIn(b'test_publisher2', response.data)

    def test_navbar(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)
        self.assertIn(b'Add Game infomation', response.data)
        self.assertIn(b'Review lists', response.data)
        self.assertIn(b'Add Game Review', response.data)
        self.assertIn(b'About', response.data)
    
    def test_about_page(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)
    
    def test_list_game_info(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test_game', response.data)
        self.assertIn(b'test_game2', response.data)
    
    def test_list_game_review(self):
        response = self.client.get(url_for('reviewlist'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test_comments', response.data)

    def test_add_game_page(self):
        response = self.client.get(url_for('add_game_info'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add', response.data)

    def test_add_review_page(self):
        response = self.client.get(url_for('add_game_review'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add', response.data)

class TestAdd(TestApp):
    def test_add_game(self):
        response = self.client.post(
            url_for('add_game_info'),
            data = {'game_name': 'test_game', 'category': 'test_category', 'publisher': 'test_publisher'},
        )
        self.assertEqual(response.status_code, 200)
        assert "Add" in response.data.decode()

    def test_add_review(self):
        response = self.client.post(
            url_for('add_game_review'),
            data = {'rating': 1, 'comments': 'test_review'},
        )
        self.assertEqual(response.status_code, 200)
        assert "Add" in response.data.decode()

class TestDelete(TestApp):
    def test_delete_game(self):
        response = self.client.get(
            url_for('delete_game_info', game_name = "test_game2"))
        self.assertEqual(response.status_code, 200)
        assert "test_game_name" not in response.data.decode()
    
    def test_delete_review(self):
        response = self.client.get(
            url_for('delete_game_review', game_id = 1))
        self.assertEqual(response.status_code, 200)
        assert "test_review" not in response.data.decode()


class TestUpdate(TestApp):
    def test_update_game_info(self):
        response = self.client.post(
            url_for('update_game_info', game_name = "test_game"),
            data = {'game_name': 'update_game', 'category': 'update_category', 'publisher': 'update_publisher'},
        )
        self.assertEqual(response.status_code, 200)
        assert "update_game" in response.data.decode()


    



