from django.db import models



# Create your models here.
class Items(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.CharField(max_length=20,null=False,unique=True)
    status = models.CharField(max_length=20,null=False,default='pending')
    
    class Meta :
        managed = True
        db_table = 'items'
        ordering = ['id','item','status']
        
        