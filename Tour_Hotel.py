'''
Tour Expenditure at Given Hotel 

The family has spent the vacation in Goa and now they are returning home to do so they will have to check out from the hotel.

Tariff on Room: Delux Room- 7500 INR

                            Non AC Room- 4500 INR 

You  as a developer has to create a program for a hotel owner which has the following requirements,

The program should begin with taking input from the checkout counter 

Type of room booked 
Total number of days 
Total Amount on Food (Amount is expected )
There are the following cases to be considered while generating a bill.

The tax on food amount is dependent on the type of room booked.

Tax on food for the deluxe room will be billed  18% of the total food amount.

Tax on food for the Non AC room will be billed  5% of the total food amount.

You are supposed to include a tip of 10% on the food amount.

The output from your program should include;

The  Room Tariff on the number of days spend, GST on a meal(Breakdown of GST is necessary based on CGST and SGST and same has to get reflected on console ) 

The tip amount, and the grand total for the meal including both the tax and the tip.

Format the output so that all of the values are displayed using two decimal places.
'''

class HotelBill:
    def _init_(self, room_type: str, num_days: int, food_amount: float):
        self.room_type = room_type
        self.num_days = num_days
        self.food_amount = food_amount

    def calculate_bill(self):
        if self.room_type == 'Delux Room':
            room_tariff = 7500 * self.num_days
            food_tax = 0.18 * self.food_amount
        elif self.room_type == 'Non AC Room':
            room_tariff = 4500 * self.num_days
            food_tax = 0.05 * self.food_amount
        else:
            raise ValueError("Invalid room type")
        
        tip_amount = 0.1 * self.food_amount
        cgst = sgst = 0.5 * food_tax
        total_amount = room_tariff + self.food_amount + food_tax + tip_amount + cgst + sgst

        print(f"Room Tariff: {room_tariff:.2f}")
        print(f"GST on Food: CGST {cgst:.2f}, SGST {sgst:.2f}")
        print(f"Tip Amount: {tip_amount:.2f}")
        print(f"Total Bill: {total_amount:.2f}")
bill = HotelBill('Delux Room', 5, 3000)
bill.calculate_bill()