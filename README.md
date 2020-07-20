# django-rest-image-upload template

This repository provide REST-API based image transaction. It generates unique API-Key for users and validate the authority. Django frameworks provides good rest api packages and simple admin page. So you can focus on writing core processes.  

I wrote this django codes for deploying services which processes images.   
For example, you can deploy your OCR service with this django app.  
I added base64 decoding feature because I prefer image transfer with json format.  

I hope this would be helpful.

---

# How To Use

## 0. Make a virtual environment

I only recommend to use virtual env when you just play with this repo. If you intend to deploy django based web into real world, it could be smart to using global system python environment for python dependecies.  

_check this out : [django-top-10-mistakes](https://www.toptal.com/django/django-top-10-mistakes)_

## 1. Clone this repository

```
git clone https://github.com/YongWookHa/django-rest-image-upload.git
```

## 2. Install dependencies

```
python -m pip install -r requirements.txt
```

## 3. Prepare for running server
**migrate db**  
```
python manage.py migrate --run-syncdb  
```
**create super-user**  
```
python manage.py createsuperuser  
```

## 4. Runserver  
```
python manage.py runserver  
```

## 5. Browse local urls

> [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
> [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  
> [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api)  
> [http://127.0.0.1:8000/api/images](http://127.0.0.1:8000/api/images)  
> [http://127.0.0.1:8000/api/base64](http://127.0.0.1:8000/api/base64)  

## 6. customize as much as you need
enjoy the code

# TODO
- Encrypt API-KEYs
- Add server-side request processing
