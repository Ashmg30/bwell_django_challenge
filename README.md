# b.well Django challenge

#### Summary:
Load a public dataset from into a SQLite database and build a RESTful API interface using Django REST Framework in Django version 2.2 and Python3.

#### Dataset:
- State of New York - Health Facility General Information (1.6 MB)
  - Included in /data folder or downloadable from [healthdata.gov](https://healthdata.gov/dataset/health-facility-general-information)

#### Requested tasks:
- For the dataset above, download the data in an appropriate dataset file and evaluate the contents
- Create a Django app to serve information about the facilities
- Create models in a SQLite database to hold the data with the following conditions:
  - Description information should be in its own table with a FK relationship
  - Address/location information should be stored in its own table with FK relationships
- Write a management command or migration to load the data from the dataset file into the database using the models
- Create REST-ful endpoints via Django REST Framework which provide the following:
  - Detail page for a facility with all data
    - Ability to CRUD facilities using the above endpoints
  - An end-point which accepts a “description” or “short description” and returns only facilities that match 
- Please try to write all API end-points to be as performant as possible while still using the Django ORM

#### Stretch goals:
- Paged listing of facilities with subset of data with 50 results per page
- Write unit tests for all above end-points and CRUD operations

#### Please deliver a zip file containing:
- Your Django project in its own directory
- A copy of your SQLite database with all data loaded
- A requirements.txt file
- Instructions on how to load the data, and a brief explanation of how to use the API endpoints
- Any docker file or other manifest file that would help us run the application
- A document in which you describe the following:
  - What assumptions you made, and how those assumptions might affect the project.
  - Any trade offs you made based on the assumptions above.
  - Approximately how long you spent working on this project.
  - The most difficult aspect of the project.
  - The easiest aspect of the project.

Please reach out to the b.well interviewer, if you have any questions.

This assignment may not be shared with anyone or posted on any blog or website.


All Rights Reserved.  
b.well Connected Health  
http://www.icanbwell.com
