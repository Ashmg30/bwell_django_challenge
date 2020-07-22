#### Requested tasks: Status
- For the dataset above, download the data in an appropriate dataset file and evaluate the contents
Done
- Create a Django app to serve information about the facilities
Done
- Create models in a SQLite database to hold the data with the following conditions:
  - Description information should be in its own table with a FK relationship
    Done
  - Address/location information should be stored in its own table with FK relationships
    Done
- Write a management command or migration to load the data from the dataset file into the database using the models
    Done
- Create REST-ful endpoints via Django REST Framework which provide the following:
  - Detail page for a facility with all data
    Done
    - Ability to CRUD facilities using the above endpoints
    Done
  - An end-point which accepts a “description” or “short description” and returns only facilities that match 
  Done
- Please try to write all API end-points to be as performant as possible while still using the Django ORM
Done

#### Stretch goals: Status
- Paged listing of facilities with subset of data with 50 results per page
Done
- Write unit tests for all above end-points and CRUD operations




#### How to run 


- Your Django project in its own directory
extract the zip
- A copy of your SQLite database with all data loaded
db.sqlite3 is already present in the folder
adminusername = health , password = 123
- A requirements.txt file
- Instructions on how to load the data, and a brief explanation of how to use the API endpoints
If you want to load data from scratch 
    delete the db.sqlite3 
    run

    python manage.py makemigrations

    #### facilities/migrations/0002_initial.py is having the script to load csv in data
- Any docker file or other manifest file that would help us run the application
    None
- A document in which you describe the following:
  - What assumptions you made, and how those assumptions might affect the project.
  - Any trade offs you made based on the assumptions above.
  - Approximately how long you spent working on this project.
    2.5 hours
  - The most difficult aspect of the project.
    To create the correct models and relationships and writing migration
  - The easiest aspect of the project.
    creating CURD api