# Mediminder

Hey guys, I created a git repo for our project.

To set it up, first make sure you have python 3, pip, virtualenv, and git installed

For Mac
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
sudo easy_install pip
pip install virtualenv
```

Git should already be installed if you have Xcode

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
venv/bin/activate
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

I think we should do Test Driven Development. I'm gonna create tests that we need to pass and then assign tasks to you guys.
