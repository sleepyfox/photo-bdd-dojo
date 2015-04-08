from behave import *
from unittest import *

@given("that I'm logged in")
def step_impl(context):
    context.ME = "sleepyfox@gmail.com"
    context.slikr = Slikr()
    assert True == context.slikr.login(context.ME)
    context.myCamera = Camera()

@when("I take an amazing photo")
def step_impl(context):
    context.my_photos = []
    context.my_photos.append(context.myCamera.take_photo())

@when("approve it (obviously)")
def step_impl(context):
    assert(True == context.myCamera.approve())

@then("I should be able to see it on my photo stream")
def step_impl(context):
    photos = context.myCamera.photo_stream() # returns a list of photos
    assert( True == (context.my_photos[-1] in photos))

@given("that I have already published one photo")
def step_impl(context):
    context.my_photos = []
    context.my_photos.append(context.myCamera.take_photo())

@when("I take another photo")
def step_impl(context):
    context.my_photos.append(context.myCamera.take_photo())

@then("I should see the new photo on my photo stream")
def step_impl(context):
    photos = context.myCamera.photo_stream() # returns a list of photos
    assert( True == (2 in photos))

@then("I should be able to see my previous photo on my photo stream")
def step_impl(context):
    photos = context.myCamera.photo_stream() # returns a list of photos
    assert( True == (1 in photos))

class Camera:
    def __init__(self):
        self.counter = 1
        self.photos = []

    def take_photo(self):
        self.photos.append(self.counter)
        last_photo_id = self.counter
        self.counter += 1
        return last_photo_id # ID of picture just taken

    def photo_stream(self):
        return self.photos

    def approve(self):
        return True

class Slikr:
    def login(self, user_name):
        return True
