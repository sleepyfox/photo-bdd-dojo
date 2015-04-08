from behave import *
from unittest import *
from camera import Camera
from slikr import Slikr

@given("that I'm logged in")
def step_impl(context):
    context.ME = "sleepyfox@gmail.com"
    context.slikr = Slikr()
    assert True == context.slikr.login(context.ME)
    context.myCamera = Camera()

@when("I take an amazing photo")
def step_impl(context):
    context.my_amazing_photo = context.myCamera.take_photo()

@when("approve it (obviously)")
def step_impl(context):
    assert(True == context.myCamera.approve())

@then("I should be able to see it on my photo stream")
def step_impl(context):
    LATEST = -1
    photos = context.myCamera.photo_stream() # returns a list of photos
    assert( True == (context.my_amazing_photo in photos))

@given("that I have already published one photo")
def step_impl(context):
    context.my_amazing_photo = context.myCamera.take_photo()

@when("I take another photo")
def step_impl(context):
    context.my_other_amazing_photo = context.myCamera.take_photo()

@then("I should see the new photo on my photo stream")
def step_impl(context):
    photos = context.myCamera.photo_stream() # returns a list of photos
    assert( True == (context.my_other_amazing_photo in photos))

@then("I should be able to see my previous photo on my photo stream")
def step_impl(context):
    photos = context.myCamera.photo_stream() # returns a list of photos
    assert( True == (context.my_amazing_photo in photos))
