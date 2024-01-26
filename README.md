# QR_System
QR recognition software and auditing facility
##Getting Started
1. Access the Github Repository
2. Clone the Repository Locally

##Prerequisites
1. Download Anaconda Navigator
2. Create an environment in Python Version (3.7.x)

##Install Dependencies
1. Install python(pip command)
2. Install Django
In the command prompt or terminal, run the following command to install Django:
pip install django
3. Install requirements.txt 
pip install -r requirements.txt
4. Install Static and Media Files (whitenoise)using pip command

##Database Setup
1. Run migrations
python manage.py makemigrations
python manage.py migrate

2. Create a superuser for admin panel
python manage.py createsuperuser

##Run the Development Server
1. python manage.py runserver
The project should now be accessible at http://127.0.0.1:8000/ in your web browser.

##Access the Admin panel
1. To access the Django admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

##Notes
1. Update the ALLOWED_HOSTS setting in settings.py to match your production server's domain or IP address.

#Host
1. Now you can host the website in Render using your credentials to use it as live webpage.
