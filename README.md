# E-prescription

This is a simple medical application where doctors can add patient record and prescribe drug for a patient and pharmacist can add drugs and administer prescription to patients.

When a doctor prescribe a medication, a unique number is generated which when inserted in the pharmacy end, the pharmacist can see all drugs prescribed for the patient by the doctor and also see information about the illness.

## Technology Stack & Tools

- Language: Python
- Backend Framework: Django

## Requirements For Initial Setup

- Install Python (Dont Forget to Tick Add to Path while installing Python)
- Install [Django](https://docs.djangoproject.com/en/5.0/intro/install/)
- Open Terminal and Execute Following Commands :
```
pip install djangorestframework
```
## Setting Up

- Fork/Clone/Download the Repository 
- Open project folder in a terminal and execute the following commands:
- NB: In place of python in the following commands, you can also use py depending on which one works for you
```
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```
- Give username, email, password and your admin account will be created.
- Run the application by entering the following command:
```
python manage.py runserver 
```
- Go to admin by entering http://127.0.0.1:8000/admin on your favourite browser
- After login, add doctor and pharmacy user
- Admin can add/delete/view/edit Pharmacist.
- Admin can view/edit/delete doctor(s).
- You can access the main application enter following URL in Your favourite browser
```
http://127.0.0.1:8000/account
```

## :brain: Author

- IJONI VICTOR 😁😁😁

> Please :pray: don't forget to star :star: the project 😁😁 . Thanks :+1:
