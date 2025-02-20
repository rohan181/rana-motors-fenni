from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
import datetime
from django.db.models import F, Sum
from django.core.exceptions import ValidationError
from ordered_model.models import OrderedModel

class Product(models.Model):
    CATEGORY = (
			('uttara', 'uttara'),
			('badda', 'badda'),
			)

    PRODUCT = (
			('local', 'local'),
			('public', 'public'),
			) 
    pcode= models.CharField(max_length=200,null=True,blank=True)  
    productcatagory= models.CharField(max_length=200,null=True)   
        
    #shopname = models.CharField(max_length=200, null=True, choices=CATEGORY)        
    name = models.TextField(max_length=30,null=True)
    status=models.CharField(max_length=10,choices=PRODUCT,default='public',null=True)
    # added = models.DateTimeField(auto_now_add=True,null=True)
    # brand= models.CharField(max_length=200,null=True)
    quantity = models.PositiveIntegerField(default=0,null=True)
    price = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   
    
    groupname= models.CharField(max_length=200,null=True,blank=True)
   
    mother = models.BooleanField(null=True,blank=True)
    subpartquantity = models.PositiveIntegerField(default=0,null=True)
    
    def __str__(self):
        return self.name
    
    def total_price(self):
        return (self.quantity * self.price)



       
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
   
    Phone = models.CharField(max_length=200)
    balance = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        default=0,
        null=True,
        blank=True
    )
    
       
    def __str__(self):
        return self.name +" "+str(self.id)




    #class Meta:
      #  ordering = ('name',)           

class UserItem(models.Model):
    PRODUCT = (
			('Direct', 'Direct'),
			('Exchange', 'Exchange'),
			)
    PRODUCT1 = (
			('LocalContainer', ' LocalContainer'),
			('publicContainer', 'publicContainer'),
			)        
    engine = (
			
			('incomplete', 'incomplete'),
            ('complete', 'complete'),
			)

    credit = (('noncredit', 'noncredit'),
			('credit', 'credit'),
			
			)                  
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,related_name='product')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0,null=True)
    price1 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
    price2 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True
    )
    added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    model_no = models.CharField(max_length=200,blank=True,null=True)
    engine_no = models.CharField(max_length=200,null=True,default='',blank=True)
    status=models.CharField(max_length=10,choices=PRODUCT,default='Direct',null=True)
    credit=models.CharField(max_length=10,choices=credit,default='noncredit',null=True)
    productype=models.CharField(max_length=100,choices=PRODUCT1,default='LocalContainer',null=True)
    enginecomplete=models.CharField(max_length=10,choices=engine,default='incomplete',null=True)
    remarks = models.CharField(max_length=500,blank=True,null=True)
    exchange_ammount = models.PositiveIntegerField(default=0,null=True,blank=True)
    #exchange_engine = models.CharField(max_length=500,blank=True,default='')
    sparename = models.CharField(max_length=200,null=True,blank=True)
    groupproduct = models.BooleanField(null=True,blank=True)
   
    @property
    def price(self):
        return (self.product.price)

    @property
    def total_price(self):
        return (self.quantity * self.price1)

    @property
    def total_price1(self):
        return (self.quantity * self.product.price)




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)
    UserItem  = models.ManyToManyField(UserItem,blank=True)
    added = models.DateTimeField(auto_now_add=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    invoicenumber = models.CharField(max_length=300,null=True,blank=True)
    address = models.CharField(max_length=800,null=True,blank=True)
    vehicleno  = models.CharField(max_length=800,null=True,blank=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    
    totalprice = models.PositiveIntegerField(default=0,null=True,blank=True)
    totalprice1 = models.PositiveIntegerField(default=0,null=True,blank=True)
    due = models.PositiveIntegerField(default=0,null=True,blank=True)
    smssend= models.BooleanField(null=True,blank=True,default=False)
    datetime= models.DateTimeField(null=True) 
    @property
    def total_price(self):
        return (self.quantity * self.UserItem.price1)
    

    @property
    def total_price1(self):
        return (self.quantity * self.UserItem.price2)
    






class sold(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    returnquantity = models.PositiveIntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    exchange_ammount = models.PositiveIntegerField(default=0,null=True)
    costprice = models.PositiveIntegerField(default=0,null=True)
    left = models.PositiveIntegerField(default=0,null=True)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    remarks = models.CharField(max_length=500,blank=True,null=True)
    
    price1 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
    price2 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True,
        blank= True
    )
    name = models.CharField(max_length=200,null=True,blank=True)
    engine_no = models.CharField(max_length=200,null=True,default='',blank=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    sparename = models.CharField(max_length=200,null=True,blank=True)
    groupproduct = models.BooleanField(null=True,blank=True)
    datetime= models.DateTimeField(null=True,blank=True)
    @property
    def total_price(self):
        return self.quantity * self.price1 +self.exchange_ammount

    @property
    def profit(self):
        return (self.total_price-self.costprice ) /self.costprice  
    @property
    def profit1(self):
        return self.profit*100   
    @property  
    def totalprofit(self):
        return self.total_price-self.costprice     
    @property
    def total_price1(self):
        return self.quantity * self.price1   
    @property
    def total_price2(self):
        return self.quantity * self.price2  
    @property     
    def total_costprice(self):
        return self.quantity * self.costprice     

    def __str__(self):
        return self.product.name 


    @property
    def invoice(self):
        return (self.id+" " +" "+ self.added+"")       
    
    def clean(self):
        if self.returnquantity > self.quantity:
            raise ValidationError("Return quantity cannot be greater than sold quantity.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    

class returnn(models.Model):    


     category = (
			('CASH RETURN', 'CASH RETURN'),
			('DUE RUTURN', 'DUE RUTURN'),
            ('BOTH', 'BOTH'),
			)    
     sold = models.ForeignKey(sold, on_delete=models.CASCADE,null=True,blank=True)
     quantity = models.PositiveIntegerField(default=1)
     returnreason = models.CharField(max_length=300,null=True,default='',blank=True)
     returnprice = models.PositiveIntegerField(default=0,null=True)
     added = models.DateTimeField(auto_now_add=True,null=True,blank=True)
     cashreturnprice = models.PositiveIntegerField(default=0,null=True)
     duereturnprice = models.PositiveIntegerField(default=0,null=True)
     status=models.CharField(max_length=50,choices= category ,default='CASH RETURN',null=True)
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)    
     datetime= models.DateTimeField(null=True) 




class bill(models.Model):  
     category = (
			('CASH ','CASH'),
			('BANK', 'BANK'),
            ('BOTH', 'BOTH'),
			) 
     order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)      
     name = models.TextField(max_length=20,null=True)
     ammount = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
     billinvoiceid= models.TextField(max_length=20,null=True)
     added = models.DateTimeField(auto_now_add=True,null=True,blank=True)
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True) 
     smssend= models.BooleanField(null=True,blank=True,default=False)
     datetime= models.DateTimeField(null=True) 
     status=models.CharField(max_length=50,choices= category ,default='CASH',null=True)
     bankname= models.CharField(max_length=300,null=True,default='',blank=True)
     brunchname= models.CharField(max_length=300,null=True,default='',blank=True)
     ChequeNo= models.CharField(max_length=300,null=True,default='',blank=True)
     issueDate= models.DateField(null=True,blank=True) 
     ClearingDate=models.DateField(null=True,blank=True)

class Customerbalacesheet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True,related_name='customer')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True,related_name='order')
    returnn = models.ForeignKey(returnn, on_delete=models.CASCADE,null=True,blank=True,related_name='returnn')
    bill = models.ForeignKey(bill, on_delete=models.CASCADE,null=True,related_name='bill')
    
    duebalanceadd = models.PositiveIntegerField(default=0,null=True)
    balance = models.PositiveIntegerField(default=0,null=True)
    added = models.DateTimeField(auto_now_add=True,null=True)
    datetime= models.DateTimeField(null=True)  
    
    
    
 

    

    

# MR START




class supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
   
    Phone = models.CharField(max_length=200)
    balance = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        default=0,
        null=True,
        blank=True
    )
       
    def __str__(self):
        return self.name     





 
class mrentry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier= models.ForeignKey(supplier, on_delete=models.CASCADE,blank=True,null=True)
  
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True,null=True)
   # UserItem  = models.ManyToManyField(UserItem,blank=True)
    left = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        default=0,
        null=True,
        blank=True
    )
    added = models.DateTimeField(auto_now_add=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=800,null=True,blank=True)
    vehicleno  = models.CharField(max_length=800,null=True,blank=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    totalprice = models.PositiveIntegerField(default=0,null=True,blank=True)
    totalprice1 = models.PositiveIntegerField(default=0,null=True,blank=True)
    due = models.PositiveIntegerField(default=0,null=True,blank=True)
    datetime= models.DateTimeField(null=True) 
    @property
    def total_price(self):
        return (self.quantity * self.UserItem.price1)
           





class mrentryrecord(models.Model):
   


    supplier = models.ForeignKey(supplier, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mrentry = models.ForeignKey(mrentry, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    paid = models.PositiveIntegerField(default=0,null=True)
    exchange_ammount = models.PositiveIntegerField(default=0,null=True)
    costprice = models.PositiveIntegerField(default=0,null=True)
    left = models.PositiveIntegerField(default=0,null=True)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    remarks = models.CharField(max_length=500,blank=True,null=True)
    
    price1 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
    price2 = models.DecimalField(
        default=0,
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
    name = models.CharField(max_length=200,null=True,blank=True)
    engine_no = models.CharField(max_length=200,null=True,default='',blank=True)
    Phone = models.CharField(max_length=200,null=True,blank=True)
    sparename = models.CharField(max_length=200,null=True,blank=True)
    groupproduct = models.BooleanField(null=True,blank=True)
    datetime= models.DateTimeField(null=True) 
    @property
    def total_price(self):
        return self.quantity * self.price1 +self.exchange_ammount

    @property
    def profit(self):
        return (self.total_price-self.costprice ) /self.costprice  
    @property
    def profit1(self):
        return self.profit*100   
    @property  
    def totalprofit(self):
        return self.total_price-self.costprice     
    @property
    def total_price1(self):
        return self.quantity * self.price1   
    @property     
    def total_costprice(self):
        return self.quantity * self.costprice     

    def __str__(self):
        return self.product.name 


 







class paybillcatogory(models.Model):    
   name = models.TextField(max_length=100,null=True)

   def __str__(self):
        return self.name


class temppaybill(models.Model):    
   paybillcatogory = models.ForeignKey(paybillcatogory, on_delete=models.CASCADE,null=True,blank=True) 
   user = models.ForeignKey(User, on_delete=models.CASCADE)  
   ammount = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True,
        default=0,
    )
   remarks = models.CharField(max_length=800,null=True,blank=True)
   datetime= models.DateTimeField(null=True)





class paybill(models.Model):    
   paybillcatogory = models.ForeignKey(paybillcatogory, on_delete=models.CASCADE,null=True,blank=True)   
   ammount = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   pettycashbalance = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   reloadpetteycash = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True
    )
   typecat=models.CharField(max_length=800,null=True,blank=True)

   user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)   
   remarks = models.CharField(max_length=300,null=True,blank=True)
   added = models.DateTimeField(auto_now_add=True,null=True)
   datetime= models.DateTimeField(null=True)



class dailyreport(models.Model):  


   category = (
			('COMMISION', 'COMMISION'),
			('DISCOUNT', 'DISCOUNT'),
            ('FUND TRANSFER','FUND TRANSFER'),
            ('CORPORATE','CORPORATE'),
			  )   
   order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)  
   mrentry = models.ForeignKey(mrentry,on_delete=models.CASCADE,null=True,blank=True)
   added = models.DateTimeField(auto_now_add=True,null=True) 
   ammount = models.PositiveIntegerField(default=0,null=True)
   petteyCash = models.PositiveIntegerField(default=0,null=True)
   returnn = models.ForeignKey(returnn,on_delete=models.CASCADE,null=True,blank=True)
   
   bill = models.ForeignKey(bill,on_delete=models.CASCADE,null=True,blank=True)
   returnprice = models.PositiveIntegerField(default=0)
   returncostprice = models.PositiveIntegerField(default=0)
   billexpense = models.PositiveIntegerField(default=0)
   remarks = models.TextField(max_length=200,null=True,blank= True)
   reporttype = models.CharField(max_length=800,choices=category,null=True,blank=True)
   datetime= models.DateTimeField(null=True) 

   @property
   def paiddtotal(self):
        return self.order.paid






class plreport(models.Model):
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True,blank=True)
      mrentry = models.ForeignKey(mrentry,on_delete=models.SET_NULL,null=True,blank=True)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      stockquantity = models.PositiveIntegerField(default=0)
      costprice= models.PositiveIntegerField(default=0)
      price1= models.PositiveIntegerField(default=0)
      price2= models.PositiveIntegerField(default=0)
      changequanitity =models.PositiveIntegerField(default=0)
      reporttype= models.CharField(max_length=500,blank=True,null=True)
      added = models.DateTimeField(auto_now_add=True,null=True,blank=True)
      datetime= models.DateTimeField(null=True) 
      reporttype = models.CharField(max_length=800,null=True,blank=True)




class corpocatagory(models.Model):
             
    #shopname = models.CharField(max_length=200, null=True, choices=CATEGORY)        
    name = models.TextField(max_length=200,null=True)
    def __str__(self):
        return self.name


class corportepay(models.Model):    
    ammount = models.PositiveIntegerField(default=0)
    supplier= models.ForeignKey(supplier,on_delete=models.CASCADE,null=True,blank=True)
    added = models.DateTimeField(auto_now_add=True,null=True) 
    remarks = models.TextField(max_length=100,null=True)
    corpocatagory= models.ForeignKey(corpocatagory,on_delete=models.CASCADE,null=True,blank=True)
    datetime= models.DateTimeField(null=True)  





class supplierbalancesheet(models.Model):
    supplier = models.ForeignKey(supplier, on_delete=models.CASCADE,null=True,blank=True,related_name='supplier')
    mrentry = models.ForeignKey(mrentry, on_delete=models.CASCADE,null=True,blank=True,related_name='mrentry')
   
    corportepay= models.ForeignKey(corportepay, on_delete=models.CASCADE,null=True,related_name='corportepay')
    
    
    balance = models.PositiveIntegerField(default=0,null=True)
    duebalanceadd =  models.PositiveIntegerField(default=0,null=True)
    added = models.DateTimeField(auto_now_add=True,null=True)       
    datetime= models.DateTimeField(null=True)
   


