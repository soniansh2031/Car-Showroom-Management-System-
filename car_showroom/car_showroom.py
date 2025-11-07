1class Car:
    def __init__(self, car_id, brand, model, year, price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.is_available = True

    def __str__(self):
        return f"{self.car_id} - {self.brand} {self.model} ({self.year}) - ${self.price}"

class Customer:
    def __init__(self, customer_id, name, contact):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"{self.customer_id} - {self.name} - {self.contact}"

class Showroom:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.sales = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Car '{car}' added to showroom.")

    def remove_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)
                print(f"Car with ID {car_id} removed from showroom.")
                return
        print(f"Car with ID {car_id} not found.")

    def display_cars(self):
        if not self.cars:
            print("No cars available in showroom.")
            return
        
        print("\n--- Available Cars ---")
        for car in self.cars:
            status = "Available" if car.is_available else "Sold"
            print(f"{car} - {status}")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer '{customer}' added to records.")

    def display_customers(self):
        if not self.customers:
            print("No customers registered.")
            return
            
        print("\n--- Registered Customers ---")
        for customer in self.customers:
            print(customer)

    def sell_car(self, car_id, customer_id):
        # Find the car
        car = None
        for c in self.cars:
            if c.car_id == car_id:
                car = c
                break
        
        if not car:
            print(f"Car with ID {car_id} not found.")
            return
            
        if not car.is_available:
            print(f"Car with ID {car_id} is already sold.")
            return

        # Find the customer
        customer = None
        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
                break
        
        if not customer:
            print(f"Customer with ID {customer_id} not found.")
            return

        # Process sale
        car.is_available = False
        sale_record = {
            'car': car,
            'customer': customer
        }
        self.sales.append(sale_record)
        print(f"Car '{car}' sold to '{customer}'")

    def display_sales(self):
        if not self.sales:
            print("No sales recorded yet.")
            return
            
        print("\n--- Sales Records ---")
        for i, sale in enumerate(self.sales, 1):
            print(f"{i}. {sale['car']} sold to {sale['customer']}")

def main():
    showroom = Showroom()
    
    # Adding some sample data
    showroom.add_car(Car(1, "Toyota", "Camry", 2022, 25000))
    showroom.add_car(Car(2, "Honda", "Civic", 2021, 22000))
    showroom.add_car(Car(3, "Ford", "Mustang", 2023, 35000))
    
    showroom.add_customer(Customer(1, "John Doe", "john@email.com"))
    showroom.add_customer(Customer(2, "Jane Smith", "jane@email.com"))
    
    while True:
        print("\n=== Car Showroom Management System ===")
        print("1. Display Cars")
        print("2. Add Car")
        print("3. Remove Car")
        print("4. Display Customers")
        print("5. Add Customer")
        print("6. Sell Car")
        print("7. Display Sales")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            showroom.display_cars()
            
        elif choice == '2':
            try:
                car_id = int(input("Enter Car ID: "))
                brand = input("Enter Brand: ")
                model = input("Enter Model: ")
                year = int(input("Enter Year: "))
                price = float(input("Enter Price: "))
                
                car = Car(car_id, brand, model, year, price)
                showroom.add_car(car)
            except ValueError:
                print("Invalid input. Please enter valid data types.")
                
        elif choice == '3':
            try:
                car_id = int(input("Enter Car ID to remove: "))
                showroom.remove_car(car_id)
            except ValueError:
                print("Invalid input. Please enter a valid Car ID.")
                
        elif choice == '4':
            showroom.display_customers()
            
        elif choice == '5':
            try:
                customer_id = int(input("Enter Customer ID: "))
                name = input("Enter Name: ")
                contact = input("Enter Contact: ")
                
                customer = Customer(customer_id, name, contact)
                showroom.add_customer(customer)
            except ValueError:
                print("Invalid input. Please enter valid data types.")
                
        elif choice == '6':
            try:
                car_id = int(input("Enter Car ID to sell: "))
                customer_id = int(input("Enter Customer ID: "))
                showroom.sell_car(car_id, customer_id)
            except ValueError:
                print("Invalid input. Please enter valid IDs.")
                
        elif choice == '7':
            showroom.display_sales()
            
        elif choice == '8':
            print("Thank you for using Car Showroom Management System!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-8.")

if __name__ == "__main__":
    main()