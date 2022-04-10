# QAProject_01 - Game Review

# By Wei Yao

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
 
* All code, configuration files, and any related code to be contained in a Github repository with a write up of the project in a README.md file
* Save all code on Github Repository 

## The implicit CRUD functionality of this app will include:

 __CREATE:__
 - __Add Game Detail__
 - __Add Game Review__

__UPDATE:__
- __Update Game Detail__
- __Update Game Review__

__DELETE:__
- __Delete Game Detail__
- __Delete Game Review__

__View:__
- __View Game Detail__
- __View Review Detail__

## Planning, Design and Project Tracking

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I have used a basic entity relationship diagram 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The application was designed to fulfil the must have features as given by the brief:

* A relationship between two tables via a foreign key
  * Game table and Review table
* Interaction between the front end and the database using SQLAlchemy
  * Front end comprises of the home page and list all saved game detail from the database to the user, user could update and delete the game they want by clicking the Update or Delete button
* Jenkins is the CI/CD server which automates testing and deploying

### ERD

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I have made a basic relationship diagram at the begining of my project, with expected entities 

#### Initial Plan:

![image](https://user-images.githubusercontent.com/76656869/162614545-9b8cfd3c-7f2b-4ba7-83c8-834142631312.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After further work and researching, I have realised that asking user for date was not necessary and formating users' input would require an extra table, here is something I could improve in the further if more time were given and made a many-to-many relationship. 

#### Final Plan: 

![image](https://user-images.githubusercontent.com/76656869/162623836-12f619cd-f001-4595-b215-02f6a059be1f.png)

## Trello Board
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I have used Treloo Board to manage and organise my workflow, so I would be able to follow up all requirements of this project and avoid and missing tasks, and what to do next once a task was completed, as well as tracking my overall progress.

![image](https://user-images.githubusercontent.com/76656869/162623690-8a206800-6372-4321-9ff0-c62674ec82ad.png)

## User Case
* As a user I want to be able to add a game or game review with its details: **Game Name**, **Category**, **Publisher**, so that I can record my favourite game with the review I posted
* As a user I want to be able to retrieve lists of games and game reviews that was previously stored in the database, so that I know what game have I recorded and avoid duplicated game
* As a user I want to be able to delete previously stored games or game reviews, so that I can alter my choices to my changing favorite game review accordingly
## Risk Assessment
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;My risk assessment, while simple, aimed to identify potential project concerns. The entries with proposed Control Measures rather than realised Control Measures were considered and documented later in the project.
![image](https://user-images.githubusercontent.com/76656869/162620003-34bb606c-668b-482e-82f5-000f946a9ca2.png)
## HTML Page functionality 

### CI/CD Pipeline

![image](https://user-images.githubusercontent.com/76656869/162626126-8a2ac243-fa28-49c1-9fa5-c1ef7036ef78.png)

## Unit Tests

# Instructions to run Application on local machine.
