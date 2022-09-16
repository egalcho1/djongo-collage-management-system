from email import message
from re import S
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.template import Context,loader
from django.contrib import messages
from django.urls import reverse
from .models import *
from django.contrib import sessions
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password,check_password
import hashlib
import qrcode
import random
