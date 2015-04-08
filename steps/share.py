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

@given("that I have already published one photo")
def step_impl(context):
    context.my_amazing_photo = context.myCamera.take_photo()

@when("I take another amazing photo")
def step_impl(context):
    context.my_other_amazing_photo = context.myCamera.take_photo()

@then("I should be able to see {thing} on my photo stream")
def step_impl(context, thing):
    if thing == "it":
        photo = context.my_amazing_photo
    elif thing == "the new photo":
        photo = context.my_other_amazing_photo
    else: # == "my previous photo"
        photo = context.my_amazing_photo
    assert(True == (photo in context.myCamera.photo_stream()))
