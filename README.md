Project details :
The Aim of the project was to execute the following

1.Make a Django application

2.Migrate it to FastAPI

3.Use config based development  , follow good coding practices , write comments and documentations and put logs

4.Package it (Using poetry module packaging)

5.Host on Windows services and/or IIS


How to execute this File:

Method 1:
1. Navigate to FastAPI_Main\dist\fastapi_main-0.1.0.tar.gz and download the tar.gz file
2. Open terminal with path of the folder in which tar.gz file is saved
3. Execute the following in the terminal 
           tar -xzf fastapi_main-0.1.0.tar.gz
           cd fastapi_main-0.1.0
4. Run the following python command(Install Python if already not installed) to create and activate virtual environment.
           python -m venv venv
           venv\Scripts\activate
5. Run the following 
           pip install poetry
           poetry install
           cd fastapi_main
           poetry run uvicorn app.main:app  --host 127.0.0.1 --port 8080  --reload

This will launch the FastAPI server, you can view the source code in the fastapi_main folder

Method 2:
1. Navigate to FastAPI_Main\dist\fastapi_main-0.1.0-py3-none-any.whl and download the .whl file
2. Open terminal with path of the folder in which tar.gz file is saved
3. Execute the following in the terminal 
Run the following python command(Install Python if already not installed) to create and activate virtual environment.
           python -m venv venv
           venv\Scripts\activate
4. Run the following 
           pip install fastapi_main-0.1.0-py3-none-any.whl
           cd "venv\Lib\site-packages\fastapi_main"
           uvicorn app.main:app  --host 127.0.0.1 --port 8080  --reload

This will launch the FastAPI server, you can view the source code in the venv\Lib\site-packages\fastapi_main folder

Application details:
This is a basic CRUD Application migrated from Django Application, keeping in mind all the details of Aim of the project




