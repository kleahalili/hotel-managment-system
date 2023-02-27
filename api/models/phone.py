from django.db import models
from django.contrib.auth.models import User
from random import randint
import datetime
from django.utils import timezone
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.conf import settings

class PhoneNumber(models.Model):
    number = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.number

class PhoneNumberVerification(models.Model):
    phone = models.ForeignKey(PhoneNumber,on_delete=models.CASCADE, related_name='phone')                                
    pin = models.IntegerField(verbose_name='pin')                      
    sent = models.DateTimeField(verbose_name='sent', null=True)

    def pin_expired(self):
        expiration_date = self.sent + datetime.timedelta(
            minutes=5)
        return expiration_date <= timezone.now()

    def send_confirmation(self):
        if all([
                settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN,
                settings.TWILIO_FROM_NUMBER
        ]):
            try:
                twilio_client = Client(settings.TWILIO_ACCOUNT_SID,
                                       settings.TWILIO_AUTH_TOKEN)
                twilio_client.messages.create(
                    body="Your activation pin is %s" % self.pin,
                    to=str(self.phone.number),
                    from_=settings.TWILIO_FROM_NUMBER)
                self.sent = timezone.now()
                self.save()
            except TwilioRestException as e:
                raise ValueError(e)
        else:
            raise ValueError("Twilio credentials are not set")

    def is_valid(self, pin):
        return self.pin == pin and (not self.pin_expired())
    
    def __str__(self):
        return f"Phone: {self.phone.number} Pin: {self.pin} Sent: {self.sent}"
    