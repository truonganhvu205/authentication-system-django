# IMPORTANT
1/ [How I fixed fix for SMTP username and password not accepted error](https://youtu.be/Y_u5KIeXiVI?si=uWvDZrbO-1tqWSl-)

2/ [Sign in with app passwords](https://support.google.com/accounts/answer/185833?hl=en)

# Clone project
```bash
git init
git clone https://github.com/truonganhvu205/authentication-system-django.git
cd authentication-system-django
```

## Install pipenv
```bash
pip3 install pipenv
```

## Activate virtual environment
```bash
pipenv --python 3.10
pipenv shell
```

## Install Django & frameworks
```bash
# Django
pipenv install django
```

# Run server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Deactivate virtual environment
```bash
exit
```

# Preview project
<table align='center'>
  <tr align='center'>
    <td>Login</td>
    <td>Register account</td>
    <td>Reset password</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/authentication-system-django/blob/main/authentication-system-django/authentication-system-django-pic-1.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/authentication-system-django/blob/main/authentication-system-django/authentication-system-django-pic-2.png' />
    </td>
    <td>
      <img src='https://github.com/truonganhvu205/authentication-system-django/blob/main/authentication-system-django/authentication-system-django-pic-3.png' />
    </td>
  </tr>
</table>
