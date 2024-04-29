# finalproject

AutoSellPro is a web application therefore it cannot be run and distributed like a desktop application. This document is for explaining how to run this project. I have used a virtual environment to develope this app. Miniconda is the virtual environment distribution I have on my computer. On this document there is guide for running this app. There are numerous tutorials on the web for miniconda installations. Throughout the guide, we will be assume that miniconda is installed on your computer. 

1. First you need to create a virtual environment. For this open up terminal and type "conda create --name finalproject python"
2. Now type "conda activate finalproject" (from now on virtual environment "finalproject" must be activated all the time!)
3. After that virtual environment will be activated. You can check your python version by typing "python --version"
4. Now we need to update pip. Type "pip install --upgrade pip"
5. Now we need to install Django. Type "pip install django"
6. After these set up stages are done navigate to the directory where this project is located
7. In terminal type "python manage.py runserver"
8. Open your browser and go to this address: http://127.0.0.1:8000/employee_portal/login
9. On another tab go to this address: http://127.0.0.1:8000/admin
10. Admin information: username=admin password=123455            Test user information: username=euser password=tuser123.
11. On another tab go to this address: http://127.0.0.1:8000/client_portal/client-home
12. Now you can use the web app as you desire
13. When you are done you can deactivate virtual environment by typing "conda deactivate" to the terminal

github repo: https://github.com/fkandemir/finalproject
 
