from django.db import models

# Create your models here.
class Electronik(models.Model):
    SMARTPHONE_GADGET = 'smartphone_gadget'
    OFFICE_INSTRUMENT = 'office_instrument'
    COMPUTER_GADGET = 'computer_gadget'
    APPLIANCE_MACHINE = 'appliance_machine'
    KITCHEN_GADGET = 'kitchen_gadget'
    BLACK='black'
    WHITE='white'
    BLUE='blue'
    GREEN='green'
    YELLOW='yellow'
    ORANGE='orange'
    GREY='grey'
    HP='hp'
    ACER='acer'
    APPLE='apple'
    SAMSUNG='samsung'
    ARTEL='artel'
    XIOMI='xiomi'
    HUAWEI='huawei'
    OPPO='oppo'
    BREND=(
    (HP,'hp'),
    (ACER,'acer'),
    (APPLE,'apple'),
    (SAMSUNG,'samsung'),
    (ARTEL,'artel'),
    (XIOMI,'xiomi'),
    (HUAWEI,'huawei'),
    (OPPO,'oppo')
    )
    TAG=(
        (SMARTPHONE_GADGET ,'smartphone_gadget'),
        (OFFICE_INSTRUMENT , 'office_instrument'),
        (COMPUTER_GADGET ,'computer_gadget'),
        (APPLIANCE_MACHINE , 'appliance_machine'),
        (KITCHEN_GADGET , 'kitchen_gadget')
    )
    COLOR=(
        (BLACK, 'black'),
        (WHITE, 'white'),
        (BLUE, 'blue'),
        (GREEN, 'green'),
        (YELLOW, 'yellow'),
        (ORANGE, 'orange'),
        (GREY, 'grey'),
    )

    name=models.CharField(max_length=255 )
    brand=models.CharField(max_length=255,choices=BREND)
    color=models.CharField(max_length=10, choices=COLOR,null=True,blank=True)
    category=models.CharField(max_length=30,choices=TAG)
    image=models.ImageField(upload_to='media/images')
    price=models.DecimalField(max_digits=9,decimal_places=2)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    count=models.IntegerField(default=0)

    @property
    def imageURL(self):
        return self.image.url
    def __str__(self):
        return f'{self.id}---{self.name}'