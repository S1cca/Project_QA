# QAProject_01 - Game Review

## Brief 
 > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This a web application that integrates with a database and demonstrate CRUD functionality, users will be able to track various game detail stored in the database, and the review for each game, users will be able to input and delete game details for each game,including game name, publisher, and category of the game; on the other hand, users will also be able to post and remove game review to the game that was previously stored in the database, including post comments and rating to the game user has selected. However, users will also be able to update details to any stored game and game review if users have ever changed their mind. Users would be able to review all games and game review they have saved in the database

## Objectives:

* To be a monolithic Flask application that serves both front and back end of this application

* Front end to use HTML templates to serve webpages that allow the user to perform CRUD functionality with data from the database

* Frontend of application to use SQLAlchemy to model an integrate with database

* This appplication must interface with a separate database service, in this case, MySQL container from GCP

* The database must contain two related table, either one-to-many or many-to-many relationship

* pytest to be used to write unit tests with the aim of achieving high coverage

* Create a continuous integration CI/CD using Jenkins:
  * To run the unit test
  * To Build the application
  * To be continuously deployed
 
* All code, configuration files, and any related code to be contained in a Github repository with a write up of the project in a README.md file.

## The implicit CRUD functionality of this app will include:
  
 __CREATE:__
 - __Add Game Detail__
 - __Add Game Review__

__UPDATE:__
- __Update Game__
- __Update Game Review__

__DELETE:__
- __Delete Game Detai__
- __Delete Game Review__


## Planning, Design and Project Tracking

### ERD

I have used a basic entity relationship diagram 

The application was designed to fulfil the must have features as given by the brief:

* A relationship between two tables via a foreign key
  * Game table and Review table
* Interaction between the front end and the database using SQLAlchemy
  * Front end comprises of the home page and list all saved game detail from the database to the user, user could update and delete the game they want by clicking the Update or Delete button
* Jenkins is the CI/CD server which automates testing and deploying

## Database design 

## HTML Page functionality 

### CI/CD Pipeline

## Unit Tests

# Instructions to run Application on local machine.
