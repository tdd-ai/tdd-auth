# Single-Sign-On

## Set-Up 

```
$ git clone https://github.com/tdd-ai/tdd-auth.git
$ cd tdd-auth/Single-Sign-On/
$ cp config/vars.env config/.env
$ nano config/.env # you need to set some env variables here 
$ python3 -m venv venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
```

### Apply Migrations

```
(venv)$ export $(grep -v '^#' config/.env | xargs)
(venv)$ cd src/
(venv)$ python manage.py migrate
(venv)$ python manage.py admin_setup # this will create super user using the credentials in .env file
```

## Starting Server

```
(venv)$ python manage.py runserver
```

## Integrating a `Service`

### Step 1

- Create a Service

### Step 2

- Reserve a `callback_url` which receives **`POST`** request
- The `callback_url` will receive User-Profile Data as fields specified in **[UserSerializer](./src/users/serializers.py)**
- This `callback_url` will be hit on two triggers: 1) `Service` Creation 2) `Connection` Creation
- On Service Creation, it will receive SSO-Admin Details (which will be used to authenticate any requests from the SSO in future)
- On Connection Creation, it will receive the User's details which got connected to the service
### Step 3

- Hit [the URL](./src/services/urls.py) for Service Creation
