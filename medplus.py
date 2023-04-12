'''
Write a Python class,
MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.
Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type
If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class
'''

class MedPlus:
    def _init_(self,medicine: str,batch_number: int,price: float):
        if type(medicine) is not str:
            raise TypeError("Medicine should be of type string")
        if type(batch_number) is not int:
            raise TypeError("Batch Number should be of type integer")
        if type(price) is not float:
            raise TypeError("Price should be of type float")
        self.medicine = medicine
        self.batch_number = batch_number
        self.price = price
med1 = MedPlus(8987,"123",50)