# mobilki_backend

żeby odpalić backend robimy:

pip install pip_requirements.txt
python manage.py migrate  
python manage.py runserver  


## logowanie:

/auth/token/login POST (generuje token), przekazujemy go w requestach i wtedy jesteśmy zalogowani
/auth/token/loguout

## rejestracja:

/auth/users  POST
