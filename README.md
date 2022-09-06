# ML-1st-Project
This is first ML project

###Software and account Reruirments.

1. Github account
2. Heroku account
3. VS Code IDE
4. GIT cli

# Create conda environment # -p means the venv file will get created in this project itself
'''

conda create -p venv python==3.9    

'''

'''
conda activate venv/ OR conda activate venv
'''

'''
pip install requirements.txt
'''

'''
git add .
'''

'''
git add <file_name>
'''

Note :- To ignore file and folder from git we can write the name of file and folder in .gitignore file

To check git status
'''
git status
'''

To check all the versions maintained of git
'''
git log
'''

To create version/commit all the changes by git
'''
git commit -m "message"
'''
To send versions/chnages to github
'''
git push origin main
'''

To check remote url
'''
git remote -v
'''

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = ankurshrivastava020@gmail.com
2. HEROKU_API_KEY = 7b71208b-5959-48b1-98e9-c6d91ecf3b15
3. HEROKU_APP_NAME = pehla-ml-project


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

>Note :- image name for docker should be in lowercase

TO LIST DOCKER IMAGES
\\\ docker image \\\

RUN DOCKER IMAGE
\\\ docker run -p 5000:5000 -e PORT=5000

TO CHECK RUNNING CONTAINER IN DOCKER
\\\ docker ps \\\

 TO STOP DOCKER CONTAINER
 \\\  docker stop <container_id> \\\
 

 ```
 python setup.py install
 ```

Install ipynbkernal

\\\

pip install ipykernal

\\\
