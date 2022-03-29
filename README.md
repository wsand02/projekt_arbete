# projekt_arbete

**I WOULD REFRAIN FROM USING THIS IN A PRODUCTION ENVIRONMENT**

Imageboard made with Django that I made for an assignment back in High School.

Updated to work with at least Python 3.10.4.

## Features

Users can create threads and then reply to them.

Threads can include images, replies cannot.

Captcha used to prevent spam threads.

Doesn't use accounts to identify users, instead uses a randomly generated key that is linked to a post and stored in a cookie.
This key allows the user to edit or delete the post they created.

Posts older than 12 hours can be deleted with the `python manage.py cleanup` command.

## Local development installation instructions

* Clone the repo
* Create virtual environment `python -m venv env`
* Activate virtual environment `env\scripts\activate`
* Install dependencies `pip install -r requirements.txt`
* Create a file called `local_settings.py` in `mysite/settings`
* Append `SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']` to the file you just created.
* Run the dev server `python manage.py runserver`
* Visit http://127.0.0.1:8000/

PS: Only tested with Windows.

