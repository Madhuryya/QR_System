from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw



class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    img = models.ImageField(upload_to='qr_codes', blank=True)
    placedAt = models.CharField(max_length=100, unique=False, default="unknown")
    desc = models.CharField(max_length=200, unique=False, default="none")
    qrcode = models.ImageField(upload_to='qr_codes', blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        link = "https://qr-system.onrender.com"+"/inventory/stock/"+str(self.id)+"/edit"
        qrcode_img = qrcode.make(link)
        canvas = Image.new('RGB', (400,400), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()

        canvas.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)



        