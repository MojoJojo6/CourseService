from django.shortcuts import render

# imports for django-rest framework
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# API description
"""
- CRUD course
- CREATE
    - create new course
    - new lesson
    - new lesson item

- READ
    - get list of all courses
    - get list of all lessons
    - get list of all lessonItems
    - get list of all 

- UPDATE
    - update course
        - name and description
    
    - update lesson
        - course id, lesson name, lesson description, sequence
        
    - update lessonItem
        - course id, lesson id, lesson item name, description, sequence

- map lesson to course and lesson item to lesson
    - 
"""
"""
        endpoint     payload         action
create  /create/     {               POST
                        name: ...,
                        desc: ...
                        }


"""
