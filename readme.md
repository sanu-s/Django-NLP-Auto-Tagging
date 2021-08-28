# Auto Image Tagging System

Django Project that helps the user to upload images and add tags. The system creates the categories of the input tags using NLP.



## Setting up Project

Install Virtual Environment

```bash
pip3 install virtualenv
```
Move to the project root directory and create a Virtual Environent

```bash
virtualenv venv
```

Activate the Virtual Environment

```bash
source venv/bin/activate
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all th packages

```bash
pip3 install -r requirements.txt
```

## Run the project


```bash
python3 manage.py runserver
```

## Procedure to upload Images and add Tags

* Navigate to Admin

  `http://localhost:8000/admin/`

* Login Using

  - username: sanu
  - password: mytestapp

* Click `imagess` from `IMAGE_AUTO_TAG` table

* Click `Add Images` button on left side

* Select image and type tags as comma seperated

* Click `Save` to save image or click `Save and add another` to add more images

## View Output Categories

We can view the output categories as image names in admin page or in terminal window

Eg: `living_thing->animal->Lion`


