# Pokedex- The CRUD App

## Contents
1. Brief
2. Software Design
3. Project Planning
4. Risk Assessment
5. Testing
6. Front End
7. Evaluation
8. Appendix

## 1. Brief

The objective of the project is as follows:

_"To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training."_

**CRUD being an acronym for Create, Read, Update and Delete.**

The project also had requirements summarised in the bullet points below:

* A Trello board to track tasks

* A database with at least 2 tables containing some form of relationship.

* Documentation describing the architecture used and Risk Assessment.

* A functional CRUD app created in Python

* Unit testing and automated validation tests for the app.

* A front-end website and integrated API's, using Flask.

* Code integrated into a Version Control System (GitHub) to be built through a CI
server and deployed to a cloud-based virtual machine (Google Cloud Platform).

## 2. Software Design

A range of software has been used through the design process, for the convenience of the reader I will highlight software names in Bold when first mentioned below throughout.

Before writing any code it was important to establish an idea for the project. I decided to create an app that mimicked some of the functionality of a Pokedex. A fictional tool used in the cartoon and game series Pokemon. It allowed users to keep a record of pokemon they had seen for the first time. As an optional extra I thought it would be fun to let the user keep track the pokemon they had caught as well as seen.

### ERD (Entity Relationship Diagrams)

These help model how data will be stored in the **MySQL** database used in the project. These MySQL databases are stored on a virtual machine. For my project I have used **Google 
Cloud Platform (GCP)** 

My initial ERD looked like this:

![First ERD](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60201f383e7e0b63dc1e4078/5a6e737f5e45070edcd82d4557bc80b5/ERD_diagram.JPG)

My final ERD looked like this:

![Final ERD](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60201f383e7e0b63dc1e4078/146c4fffbe89cf3ea67394572339d6cd/final_erd.JPG)
 
I initially thought of using three tables. One with all pokemon ever seen, another for caught pokemon and the final one for the users current inventory of 6 pokemon. This is how the structure worked in the famous Pokemon game on GameBoy Colour.

However time constraints of the course and project deadline looming I thought it best to simplify the ERD to only contain 2 tables. PokeDatabase and Caught Pokemon. With Caught pokemon having a foreign key relationship to the ID of the pokemon database. I will draw on how I used this relationship later on in the project.
The Pokedatabase has a one to many relationship with Caught Pokemon. Hence you can catch the same pokemon more than once.

### CI Pipeline

Below is a CI (Continuous Integration) pipeline diagram showing all the different software ackages I used and how they relate in relation to one another

![CI Pipeline](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60201fcc8fba3318caac5360/28360f75ae8231e52ddb9fb9742df195/cicd_pipeline.jpg)

As you can see I used **GitHub** as a version control system. Trello (Kanban Board) to manage my project planning. **Pycharm** IDE to write my code in **Python**. Pytest to test my coverage. **Jenkins** allows for automation to take place in that it has a web hook to my GitHub repository and has a script to test the code before running it on **Gunicorn**.
All the data for my app is held on a virtual machine instance in GCP. The shell being run on GCP is a **Linux/Unix** language through **Ubuntu**.

## 3. Project Planning
I used Trello to manage my planning for the project. It contains a very simple user interface which allows for Todo, Doing and Done coloumns.
This style of planning is taken from the japanese method of Kanban.

To see the actual Trello Board:

[Link to Trello Board](https://trello.com/b/yTAUXvO3/qa-week-6-project)

This is my initial Trello board:
![Trello First](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60201fdec7de598cda7e0859/89410659280049a87b6849550a940d1c/Beginning_Trello.JPG)

This is my Trello board at the end of the project:
![Trello End](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60201fdec7de598cda7e0859/dfa5c756b763199e430e15b0495d436b/End_Trello.JPG)

## 4. Risk Assessment
This is the risk assessment I have conducted for the project
![Risk Assessment](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/6020355e91dfc2794a87e432/197c575103b08e6b80da596bf160311a/Risk_Assessment.JPG)

## 5. Testing
We only had time to conduct unit testing for the project and not the integration testing as this had not been taught before the deadline for the project.
I used **Pytest** to conduct the tests for my project. Unfortunately due to the complexity of my code it was not possible to replicate the environment in testing that was creating the tables for input into the database. I have included in my code a random functionality that allows a user to catch a random pokemon from the first table and input this pokemon into the second table Caught pokemon.  And due to this recreating the initial test database and table relationship was not possible due to my lack of knowledge of replicating it within the test environment parameters. This resulted in failures in loading HTML pages that contained information from my databases. The pages that did not contain information from my database did however pass testing.

The project brief wanted us to have a test coverage of approximately 70-80% of our code. This is what my test coverage report gave:
![Testing](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/6020395e9eb1b76f22fa55de/18e955cd6015ee07fa40a2acfaf54601/Test_coverage.JPG)

If we had been taught the content for integration testing before the project deadline I believe this would have been the better testing method for my app, as this would not require the tester to manually enter data to create the tables.

## 6. Front End
Time constraints meant that I was unable to add any CSS to my HTML pages to make them look good. However this wasn't a required part of the project brief anyway.

Here are screenshots of my app when running, contained is every HTML page apart from the delete functionality which redirects to the Catch pokemon page:

##### HomePage

![Home Page](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/491395aeb12ec01b9f4b94856495ca62/Homepage.JPG)

##### Pokemon Database

![pokedatabse](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/5a3478817095c875ffd29b0484adbd3a/Pokedatabase.JPG) 

##### Add Pokemon

![add](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/a9238def6d8bd5915083b298318ad16a/Add_pokemon.JPG)

##### All fields required validator  

![validator](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/98e278469a1fe74b1a7bb5f17cbeab44/Validator_Required.JPG) 

##### Pokemon Added

![added](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/a68855b6a395decb001a87085b957115/added_pokemon.JPG)

##### Catch Pokemon

![catch](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/57a9e03ca8285db368473d392d56d138/catchpoke.JPG) 

##### Throw a Pokeball

![throw](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/b94524528afd55ef769e862f680bae53/throwball.JPG) 

##### Caught Pokemon

![caught](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/2e41d63ae5ae5568cfe9fa6c0f7e1163/caught.JPG) 

##### Update Nickname

![update](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/60203d7cc725443afc9db901/164565fcf5873ded7d799a04ec4b2548/update.JPG) 

## 7. Evaluation   
   Overall I think the project was very successful. I managed to create a CRUD app in the form of a Pokedex using Python. Whilst hosting ti inside a virtual machine, in this case Google Cloud Platform and storing data in a cloud environment through MySQL.
   
   It is a shame the testing did not go as planned. I do believe if I had more time and a little help from the instructors I would have managed to create a testing environment which could handle the random functionality I had inside my app.
   
   If I could do it again and had more time I would love to get the testing finished and improve the front end graphics with my existing HTML/CSS web development skills. I would also have liked to add a user login functionality. I have learnt a lot through the experience about application development through Flask, hosting on a Virtual Cloud Platform and managing databases on SQL

## 8. Appendix  

Author: Kishan Vekaria

All the content in this repository has been created by me and is being stored on Github. Hence it's open source. If you have any questions or contribrutions you would like to make please contact me and I would be happy to hear from you!
