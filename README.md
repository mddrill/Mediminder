# Mediminder

Hey guys, I created a git repo for our project. For the backend we'll use django and the django REST Framework.

To set it up, first make sure you have python 3, pip, virtualenv, and git installed

For Mac
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
sudo easy_install pip
pip install virtualenv
```

Git should already be installed if you have Xcode, if not install Xcode from the app store

For Windows you'll have to download python 3 from here https://www.python.org/downloads/
I think pip should install with python 3 automatically
Then `pip install virtualenv`
And download git from here https://git-scm.com/download/win

Then clone this repository
```
cd ~
git clone https://github.com/mddrill/Mediminder
cd ~/Mediminder
```

Then create the virtual environment

On Mac
```
virtualenv -p python3 venv
source venv/bin/activate
```
On Windows
```
virtualenv -p python3 venv
venv/scripts/activate
```

Then install the dependencies through requirements.txt
```
pip install -r requirements.txt
```

Now create the database
```
python manage.py makemigrations
python manage.py migrate
```
I haven't tested any of the windows commands because I'm on Mac, but they should all work, if they don't let me know.

There are thre endpoints, `/doctors/` and `/patients/` for creating doctor and patient accounts and `/instructions/` for the instructions.

We're gonna do Test Driven Development, I've created failing tests for you guys to pass.

For example code, you guys can look here https://github.com/mddrill/WallAppBackend. There's also a good django REST tutorial here http://www.django-rest-framework.org/tutorial/1-serialization/.
