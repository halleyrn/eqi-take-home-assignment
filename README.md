# EIQ Take Home Assignment
This application was made to address the following prompt:

> A simple Flask-Kubernetes-Docker web application that allows the user to upload a .CSV file. On successful file upload, the application should perform the following validations:
>
> * Checks whether the uploaded is a .CSV and not any other format.
> * Check whether the .CSV file has exactly 10 rows and 3 columns.
> * Checks whether the data is present in each cell (.CSV file is "complete"). A "complete" sample test.csv is available in this repository for testing purposes.
> 
> Build, push, and deploy a docker container on Kubernetes Engine that performs the above validations for an uploaded .csv file.

## Build Instructions
The following commands will build this application on a Mac:
```bash
python3 -m venv venv  # create a virtual environment called venv
source venv/bin/activate  # activate the created virtual environment
python3 -m pip install -r application/requirements.txt  # install project dependencies
python3 application/app.py  # run development server locally
```

To run the developemnt server locall, alternatively, from inside `/application` you could run 
```bash
python3 -m flask run
```

Once the service is up and running, open a web browser of your choice and navigate to `http://127.0.0.1:8080/` 
to view the running application. 


## Test Instructions
Activate the virtual environment created in the build instructions. Then use the following 
command to run the tests.
```bash
python3 -m pip install -r requirements-dev.txt  # install project dependencies
python3 -m pytest test/tests.py
```


## Build in Docker Instructions
First install Docker for your operating system.  
From the root directory, run the following
```bash
docker build --tag eiq-take-home .
docker run --publish 5000:5000 eiq-take-home
```
Once the service is up and running, open a web browser of your choice and navigate to `http://localhost:5000/` 
to view the running application. 


## Push and Deploy to Google Cloud Platform Instructions
1. Make sure the `PROJECT_ID` environmental variable has been set  
2. Make sure that the project has the correct permissions and API enabled.  
3. Push your files to the cloud and build your image: `gcloud builds submit`  


## Set up Build on Google App Engine Instructions
*This set of instructions does not successfully deploy the application. Upon opening the 
service in your browser, you will see a '502 Gateway error'.*  
1. Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install). 
2. Create new project on Google Cloud Platform. Note the project ID.
2. Authenticate your Google App Engine account from your local computer with `gcloud auth login`
3. Set `PROJECT_ID` environmental variable `gcloud config set project <project-ID>`
3. Run the command in command prompt: `gcloud app deploy`
4. Select a region when prompted.
5. Confirm the deployment, when prompted.
6. Run `gcloud app browser` to open the deployed service in your browser.


## Usage
1. Click `Choose File` to select a file. The chosen filename will preview on the screen.
2. Once you have verified the file name is correct, click `Submit` 

The page will navigate to another page upon clicking submit, and the status
of the uploaded file will be displayed. To return to the main page with the input form, use
the back arrow of your browser.  

If the file **does not** meet the criteria of the prompt, then the conflict will be explained. If 
the file **does** meet the criteria of the prompt, then the page will read "Success!".


## Author
Halley Nathwani 

