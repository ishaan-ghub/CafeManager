from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.
class beverage(models.Model):
    BEVERAGE_CHOICES = [
        ('MT', 'Masala tea'),
        ('GT', 'Ginger tea'),
        ('ET', 'Elaichi tea'),
        ('PT', 'Plain tea'),
        ('LT', 'Lemon tea'),
        ('GrT', 'Green tea'),
        ('CC', 'Cold coffee'),
        ('CP', 'Cappuccino'),
        ('FC', 'Filter coffee'),
        ('VM', 'Virgin mojito'),
        ('MS', 'Masala soda'),
        ('LS', 'Lemon soda'),
        ('OM', 'Oreo milkshake'),
        ('BS', 'Butterscotch shake'),
    ]
    name = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='softdrinks/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=BEVERAGE_CHOICES)
    description = models.TextField(default='')
    prices = models.CharField(default='Re',max_length=10)
    
    def __str__(self) -> str:
        return self.name
    
# one to many model- reviews

class review(models.Model):
    drink= models.ForeignKey(beverage,on_delete= models.CASCADE,related_name= 'reviews')
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.IntegerField()
    comment= models.TextField()
    date_added= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.drink.name}'

# Many to many- stores    

class store(models.Model):
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    drink_varieties= models.ManyToManyField(beverage, related_name= 'stores')

    def __str__(self):
        return self.name
    
# One to one- certificates

class certificate(models.Model):
    drink= models.OneToOneField(beverage, on_delete=models.CASCADE, related_name='certificate')
    certificate_no= models.CharField(max_length=100)
    issued_date= models.DateTimeField(default=timezone.now) 
    valid_untill= models.DateTimeField(default=timezone.now()+ timedelta(days=732))

    def __str__(self):
        return f'Certificate for {self.drink.name}'