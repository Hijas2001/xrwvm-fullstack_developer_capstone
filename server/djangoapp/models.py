# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make
    
    # Any other fields you might want to add
    # Example: logo_url = models.URLField() for car make's logo
    
    def __str__(self):
        return self.name  # Return the name as the string representation

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-one relationship to CarMake
    name = models.CharField(max_length=100)  # Name of the car model (e.g., Corolla, Focus)
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # You can add more choices here if needed
    ]
    
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Car type (Sedan, SUV, Wagon)
    
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )  # Year of the car, restricted between 2015 and 2023
    
    # Any other fields you might want to add
    # Example: price = models.DecimalField(max_digits=10, decimal_places=2) for price of the car
    
    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Returns the full name: Make + Model

