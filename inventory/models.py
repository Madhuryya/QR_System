from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw



class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    description_of_item = models.CharField(max_length=30, unique=False)
    po = models.CharField(max_length=100, unique=False, default="unknown")
    quantity = models.IntegerField(default=1)
    # img = models.ImageField(upload_to='qr_codes', blank=True)
    
    location = models.CharField(max_length=200, unique=False, default="none")
    registration = models.CharField(max_length=200, unique=False, default="none")
    status = models.CharField(max_length=200, unique=False, default="none")
    remarks = models.CharField(max_length=200, unique=False, default="none")
    qrcode = models.ImageField(upload_to='qr_codes', blank=True)
    is_deleted = models.BooleanField(default=False)
    audited = models.BooleanField(default=False)

    def __str__(self):
	    return self.description_of_item
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # link = "https://qr-system.onrender.com"+"/inventory/stock/"+str(self.id)+"/edit"
        link = "http://127.0.0.1:8000/"+"inventory/stock/"+str(self.id)+"/edit"

        qrcode_img = qrcode.make(link)
        canvas = Image.new('RGB', (400,400), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.description_of_item}'+'.png'
        buffer = BytesIO()

        canvas.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

        