from django.core.mail import send_mail
from django.db import models
import telepot
class Dht(models.Model):
 temp = models.FloatField(null=True)
 hum = models.FloatField(null=True)
 dt = models.DateTimeField(auto_now_add=True,null=True)

 def __str__(self):
  return str(self.temp)


 def save(self, *args, **kwargs):
     if self.temp > 40:
         send_mail(
             'température dépasse la normale,'+str(self.temp),
             'anomalie dans la machine le,'+str(self.dt),
             'safae.kaddouri@ump.ac.ma',
             ['meriem.tahri@ump.ac.ma'],
             fail_silently=False,
         )
         token = '5939207829:AAEgH1Pvy52c_aIQF3m-wTP90AIuPJQtX7Q'
         rece_id = 5510971333
         bot = telepot.Bot(token)
         bot.sendMessage(rece_id, 'BONJOUR SAFAE.')
         print(bot.sendMessage(rece_id, 'BONJOUR SAFAE.'))
     return super().save(*args, **kwargs)
# Create your models here.
