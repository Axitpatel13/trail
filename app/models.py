from django.db import models
from django.contrib.auth.models import User
from users.models import user

class site_info(models.Model):
    site_title = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self):
        return self.site_title
    
    class Meta:
        verbose_name_plural = "Site Info"    

#____________________________(Services)___________________________________#    
class services(models.Model):    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    url_to_go = models.URLField(max_length=500,blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Service"
#___________________________________________________________________________#    
    
#____________________________(About Us)_____________________________________#    
class about_us(models.Model):
    description = models.TextField()   
    
    class Meta:
        verbose_name_plural = "About Us"
#____________________________________________________________________________#    

#____________________________(Case Studies)___________________________________#    
class case_studies(models.Model):
    title = models.CharField(max_length=100)    
    description = models.TextField() 
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Case Studies"

#_____________________________(Testimonials)___________________________________#    
class testimonial(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Testimonial"
        
#______________________________(Contact Us)____________________________________#    
class contact_us(models.Model):
    full_name = models.CharField(max_length=80)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = "Contact"
        
class payment_request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    paypal_address = models.CharField(max_length=500,null=True,blank=True)
    btc_address = models.CharField(max_length=500,null=True,blank=True)
    payoneer_address = models.CharField(max_length=500,null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50,choices=(('Approved','Approved'),('Declined','Declined')),default='Pending')
    def __str__(self):
        return self.user.username +' | '+ str(self.status)
