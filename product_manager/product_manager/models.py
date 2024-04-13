from django.db import models
from django.utils import timezone

# Customer Model
class Customer(models.Model):
    DocumentType = models.CharField(max_length=21)
    DocumentNumber = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.DocumentType} {self.DocumentNumber}'

# ApplicationStatus Model
class ApplicationStatus(models.Model):
    StatusDescription = models.CharField(max_length=100)
    CreationDate = models.DateTimeField(default=timezone.now)
    ModificationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.StatusDescription

# Application Model
class Application(models.Model):
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    StatusID = models.ForeignKey(ApplicationStatus, on_delete=models.CASCADE)
    CreationDate = models.DateTimeField(default=timezone.now)
    ModificationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.CustomerID} - {self.StatusID}'

# BasicInformation Model
class BasicInformation(models.Model):
    ApplicationID = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=20)
    Email = models.EmailField()
    CreationDate = models.DateTimeField(default=timezone.now)
    ModificationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.FirstName} {self.LastName}'

# EconomicInformation Model
class EconomicInformation(models.Model):
    ApplicationID = models.OneToOneField(Application, on_delete=models.CASCADE, primary_key=True)
    Profession = models.CharField(max_length=100)
    EconomicActivity = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100)
    PositionInCompany = models.CharField(max_length=100)
    CompanyContact = models.CharField(max_length=100)
    Income = models.DecimalField(max_digits=10, decimal_places=2)
    Expenses = models.DecimalField(max_digits=10, decimal_places=2)
    Assets = models.DecimalField(max_digits=10, decimal_places=2)
    Liabilities = models.DecimalField(max_digits=10, decimal_places=2)
    NetWorth = models.DecimalField(max_digits=10, decimal_places=2)
    FullAddress = models.CharField(max_length=255)
    CreationDate = models.DateTimeField(default=timezone.now)
    ModificationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.CompanyName

# CardOffer Model
class CardOffer(models.Model):
    ApplicationID = models.ForeignKey(Application, on_delete=models.CASCADE)
    CardType = models.CharField(max_length=50)
    Franchise = models.CharField(max_length=50)
    CreditLimit = models.DecimalField(max_digits=10, decimal_places=2)
    APR = models.DecimalField(max_digits=5, decimal_places=2)
    Rewards = models.CharField(max_length=100)
    AnnualFee = models.DecimalField(max_digits=6, decimal_places=2)
    CreationDate = models.DateTimeField(default=timezone.now)
    ModificationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.CardType} - {self.Franchise}'
