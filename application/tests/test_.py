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
        test_game = Game(game_name='test_game', category='test_category', publisher='test_publisher')
        db.session.add(test_game)
        test_review = Review(rating=1, game_id=1, comments='test_comments')
        db.session.add(test_review)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRead(TestApp):
    def test_list_game_info(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_list_game_review(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_game_info(self):
        response = self.client.post(url_for('add_game_info'), data=dict(game_name='test_game', category='test_category', publisher='test_publisher'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_add_review(self):
        response = self.client.post(url_for('add_game_review', id = 1, follow_redirects=True))
        self.assertEqual(response.status_code, 200)

    def test_update_game_info(self):
        response = self.client.post(url_for('update_game_info', id = 1, follow_redirects=True))
        self.assertEqual(response.status_code, 200)
    
    def test_update_review(self):
        response = self.client.post(url_for('update_game_review', id = 1, follow_redirects=True))
        self.assertEqual(response.status_code, 200)

    



