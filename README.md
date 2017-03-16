Setup Development Environment (Debian/Ubuntu)
=============================================

On Debian-like systems simply type:

sudo apt-get install git git-core

1. Clone this repository

git clone git://github.com/marinpareja/testdjangoweb.git

2. To install virtualenv, pop into your command line shell and type:

easy_install virtualenv

3. Don’t worry, this is the last you’ll see of easy_install now that we have pip. (In more recent versions, pip comes bundled with virtualenv!)

So now you have virtualenv installed and you’re ready to go! What exactly do you do now? First, you must decide where you want to store your virtual environments, personally I keep them in a hidden directory under my home. Then, we will create our actual new virtual environment.

mkdir ~/.virtualenvs
virtualenv ~/.virtualenvs/testdjangoweb

4. Development environment is ready to use, lunch development server
source ~/.virtualenvs/testdjangoweb/bin/activate

cd testdjangoweb
python manage.py runserver
