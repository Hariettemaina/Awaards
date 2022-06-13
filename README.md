# Awwwards
- By: Hariette Maina

## Description
- This web-app allows a user to create a Profile,Category,Country,Technology,Color and Projects that are all under his username allowing other users to vote for them and visit the particular projects site.
<!-- 
Known Bugs
Elements re-arrange themselves unequally on different screen sizes.
Cards disarrange themselves when they're not four in a row.
Submit button moves to the side when a user with a long username logs in. -->
## Behaviour Driven Development
- The program should return all projects on the directories page
Given:All projects
When: Url is changed to directory page
Then: All projects are displayed

- Admin site should be displayed when "admin/" url is chosen
Given: An admin url
When: User enters admin url in browser
Then: Admin Login is displayed

- User authentication occurs when Admin tries to Login
Given:Admin page is accessed
When: User tries to login
Then: User details are authenticated to confirm if user is an admin

- User session should end when logout url is chosen
Given:Logout option is given
When: User chooses logout option
Then: User session is ended

## Description
A web application where developers can be a able to post their projects and other developers can be able to vote and gauge their views on the application.

# Technologies used
- The project is created with:

- HTML:5 for giving the structure of the webpage.
- CSS:3 for styling the webpage.
-Bootstrap for more styling of the webpage.
- Python Django for the functionality.
## Installation
- Clone the repository directly to your pc using this command https://github.com/Hariettemaina/Awaards.git
- To be able to run this project on your PC you need to have python already installed Python version 3.8 and above. Incase you dont have it use this commands to install $ sudo add-apt-repository ppa:jonathonf/python-3.8 $ sudo apt-get update $ sudo apt-get install python3.8

- Install Python command tool called PIP which comes preinstalled in linux and mac. For linux use this to install pip $ sudo apt-get install python3-pip

- For mac 0S use this command to install pip sudo easy_install pip Open your editor and run the cloned repository and install the modules below to run effectivey.

- To install all requirements and extentions needed to run the app install requirements using

- pip install -r requirements.txt

- To run the class test use the following commands in the terminal python3.8 manage.py test

- Now your ready to run the modules type the fillowing commands to run the app locally. python3.8 manage.py server

## Setup
-To run this project, use the live link in the GitHub repo: The live link to the project is als provided 
below.

# Contact
- hariettemaina@gmail.com


# License
Copyright (c)2022 Hariette Maina