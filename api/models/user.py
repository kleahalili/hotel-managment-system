from django.contrib.auth.models import User

User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False