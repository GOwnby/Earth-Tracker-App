# Earth-Tracker-App

A Django Python Web Application featuring interactive charts for visualizing public data about Earth's atmosphere.

The program may be used to generate the following examples in the interactive web application:

![Screenshot 2024-04-17 122646](https://github.com/GOwnby/Earth-Tracker-App/assets/37450012/e5d2d077-5fb5-4bcf-a6ec-73b0400d6f2e)
![Screenshot 2024-04-17 122718](https://github.com/GOwnby/Earth-Tracker-App/assets/37450012/e237b5db-a24a-4f02-99de-4f7ee5e0b750)
![Screenshot 2024-04-17 122739](https://github.com/GOwnby/Earth-Tracker-App/assets/37450012/a63ee4d2-f66c-4bb9-b61f-26214f492850)
![Screenshot 2024-04-17 122758](https://github.com/GOwnby/Earth-Tracker-App/assets/37450012/b92b8616-1909-40d3-8534-61078bb75ad7)
![Screenshot 2024-04-17 122818](https://github.com/GOwnby/Earth-Tracker-App/assets/37450012/1d58ab80-3199-4ee0-9764-977150243c61)
![Screenshot 2024-04-17 122908](https://github.com/GOwnby/Earth-Tracker-App/assets/37450012/4a66cc27-bf46-4d0f-b2e2-f08baa99d2d3)

# Setting up the application
In order to setup the application, [Python 3.11.8](https://www.python.org/downloads/release/python-3118/) and [MySQL server 8.0.36.0](https://dev.mysql.com/downloads/mysql/) must be installed.

Once Python and MySQL are installed, open a Terminal in Linux or MacOS, or a PowerShell Terminal in Windows.
For [installing PowerShell on Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4), it is recommended for new users to follow the instructions for 
"Installing the MSI package" as the installer is the easiest to use.

Now, we must generate the MySQL database used by this application as defined in ```settings.py```. Begin by opening the MySql command line. In MacOS or Linux, this may be done my running the following command in the terminal:```mysql```
In Windows, search for and run the MySQL Command Line Client.

Now we need to create a user and database and grant privileges on that database to the user. Run the following MySQL commands:
```
CREATE USER 'EarthTracker'@'localhost' IDENTIFIED BY '$Earth$7685Tracker$';
CREATE DATABASE EarthTrackerLive;
GRANT ALL PRIVILEGES ON EarthTrackerLive.* TO 'EarthTracker'@'localhost';
exit
```
Now we are ready to install and run the Django Python Web Application.

Navigate to the location where the Django application is saved, and install the Python packages in the requirements.txt file by running the following command:
```
pip install -r requirements.txt
```
Next, migrate changes the MySQL database (Note: If you are having trouble with these commands, try using ```python3``` instead of ```python``` in your command):
```
python manage.py makemigrations
python manage.py migrate
```
Finally, collect static files for deployment and run the server:
```
python manage.py collectstatic
python manage.py runserver
```
The Web Application may now be accessed via your browser at http://127.0.0.1:8000/
