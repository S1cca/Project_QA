# QAProject_01 

#### Game Review

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

#### Home Page

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In my home page, I have managed to list all games that stored in the data base to user, as well as navbar for users to use, this page will be shown to all users once they have navigated to the URL.

Users will not be allowed to delete a game that have saved review to it, since the Game table contains a foreign key acting as a Primary key in the Review table
![image](https://user-images.githubusercontent.com/76656869/162629253-3a3e9cea-444d-4fef-90d5-08dd4a05e1ae.png)

#### Add Game Infomation Page 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To add a Game to the database, users would only to  click the Add Game Infomation Button, then users will be redirected into the Add Game Infomation Page, There will be 3 empty boxes to allow users to input relative infomation about the game they wanted to add to the database, Game Name, Game Category, Publisher of the game.

![image](https://user-images.githubusercontent.com/76656869/162637172-f74ec1a2-ae66-407e-9130-ad5e06808253.png)


#### Add Game Review Page
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By clicking the Add Game Review button, users will be allowed to post their review to a game

![image](https://user-images.githubusercontent.com/76656869/162637181-e3c0db75-ce37-4b5e-a344-73d7fd55858a.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users will be able to choose a game from the database (where they previously stored) to post relative review to it
![image](https://user-images.githubusercontent.com/76656869/162637195-791a5658-c7ab-46bf-997a-1d843ac3e55a.png)


#### Review List

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After user have added their reviews, they can browse all their reviews in this Review list, I have managed to show all previously saved review to the user, users could manage their saved reviews by clicking relative button: update, delete.


![image](https://user-images.githubusercontent.com/76656869/162630439-3a95e0fc-6e09-4399-b227-1bc4b09b01fe.png)


#### About Page

The About Page will show some basic detail about this appplication and where to locate the repository code
![image](https://user-images.githubusercontent.com/76656869/162631118-197c1d06-7c2c-49b1-9919-903e81e2d176.png)



## CI/CD Pipeline

The pipeline image represents how will the entire project work breaking down into different stages, and tools/platform have been chosen to use for each stage of development. For my project, I have used flask to build my application including the database schema which was connected to an external SQL instance created from Google Cloud Platform, since it was ideally reliable and secure to use 
![image](https://user-images.githubusercontent.com/76656869/162626126-8a2ac243-fa28-49c1-9fa5-c1ef7036ef78.png)

## Testing
**pytest** is the best way to test python programs. Here are my code for pytest

![image](https://user-images.githubusercontent.com/76656869/162637586-eea9c533-2363-41b4-82e7-d7db2aca0708.png)
![image](https://user-images.githubusercontent.com/76656869/162637590-88386e89-1151-445b-b90b-aaff844a02ff.png)
![image](https://user-images.githubusercontent.com/76656869/162637598-1c635ec0-e804-47f8-8365-48e9eba354fb.png)

and the pytest coverage report

![image](https://user-images.githubusercontent.com/76656869/162639829-009f06c6-40f1-43fb-bb79-ccff16831171.png)

## Build Automation

I have used Jenkins as the CI server, a list of commands could to be excuted in order to install the various modules and dependencies of the project, a virtual environment would be created and then the database connection string will then be exported before the app launches

In Jenkins, the GitHub repository will be cloned and a scipt with build (list of commands), and eventually test stage will run. See below as the console output from Jenkins

![image](https://user-images.githubusercontent.com/76656869/162640307-95e860dc-769d-49f6-8bad-dc1fbaf90077.png)
![image](https://user-images.githubusercontent.com/76656869/162640377-edf981c4-16f4-4001-afe6-dd56f0c0ca87.png)

Jenkins is currently set to run this automation from any branch of the GitHub repo on the click of a button, however for future development Jenkins would most likely be set to run tests automatically on pushing to the repos 'Main' branch.

## Future Work

This application is not completely finished 
