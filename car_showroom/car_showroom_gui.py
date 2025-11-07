import tkinter as tk
from tkinter import ttk, messagebox

class Car:
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
        self.load_sample_data()

    def load_sample_data(self):
        # Adding some sample data
        self.add_car(Car(1, "Toyota", "Camry", 2022, 25000))
        self.add_car(Car(2, "Honda", "Civic", 2021, 22000))
        self.add_car(Car(3, "Ford", "Mustang", 2023, 35000))
        
        self.add_customer(Customer(1, "John Doe", "john@email.com"))
        self.add_customer(Customer(2, "Jane Smith", "jane@email.com"))

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)
                return True
        return False

    def get_cars_display(self):
        if not self.cars:
            return "No cars available in showroom."
        
        result = "Available Cars:\n"
        for car in self.cars:
            status = "Available" if car.is_available else "Sold"
            result += f"{car} - {status}\n"
        return result

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customers_display(self):
        if not self.customers:
            return "No customers registered."
            
        result = "Registered Customers:\n"
        for customer in self.customers:
            result += f"{customer}\n"
        return result

    def sell_car(self, car_id, customer_id):
        # Find the car
        car = None
        for c in self.cars:
            if c.car_id == car_id:
                car = c
                break
        
        if not car:
            return f"Car with ID {car_id} not found."
            
        if not car.is_available:
            return f"Car with ID {car_id} is already sold."

        # Find the customer
        customer = None
        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
                break
        
        if not customer:
            return f"Customer with ID {customer_id} not found."

        # Process sale
        car.is_available = False
        sale_record = {
            'car': car,
            'customer': customer
        }
        self.sales.append(sale_record)
        return f"Car '{car}' sold to '{customer}'"

    def get_sales_display(self):
        if not self.sales:
            return "No sales recorded yet."
            
        result = "Sales Records:\n"
        for i, sale in enumerate(self.sales, 1):
            result += f"{i}. {sale['car']} sold to {sale['customer']}\n"
        return result

class CarShowroomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Showroom Management System")
        self.root.geometry("800x600")
        self.showroom = Showroom()
        
        self.setup_ui()

    def setup_ui(self):
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_cars_tab()
        self.create_customers_tab()
        self.create_sales_tab()
        self.create_add_car_tab()
        self.create_add_customer_tab()
        self.create_sell_car_tab()

    def create_cars_tab(self):
        cars_frame = ttk.Frame(self.notebook)
        self.notebook.add(cars_frame, text="View Cars")
        
        # Title
        title_label = ttk.Label(cars_frame, text="Cars in Showroom", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Display area
        self.cars_text = tk.Text(cars_frame, height=20, width=80)
        scrollbar = ttk.Scrollbar(cars_frame, orient=tk.VERTICAL, command=self.cars_text.yview)
        self.cars_text.configure(yscrollcommand=scrollbar.set)
        
        self.cars_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Refresh button
        refresh_btn = ttk.Button(cars_frame, text="Refresh", command=self.refresh_cars)
        refresh_btn.pack(pady=10)
        
        # Initial display
        self.refresh_cars()

    def refresh_cars(self):
        self.cars_text.delete(1.0, tk.END)
        self.cars_text.insert(tk.END, self.showroom.get_cars_display())

    def create_customers_tab(self):
        customers_frame = ttk.Frame(self.notebook)
        self.notebook.add(customers_frame, text="View Customers")
        
        # Title
        title_label = ttk.Label(customers_frame, text="Registered Customers", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Display area
        self.customers_text = tk.Text(customers_frame, height=20, width=80)
        scrollbar = ttk.Scrollbar(customers_frame, orient=tk.VERTICAL, command=self.customers_text.yview)
        self.customers_text.configure(yscrollcommand=scrollbar.set)
        
        self.customers_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Refresh button
        refresh_btn = ttk.Button(customers_frame, text="Refresh", command=self.refresh_customers)
        refresh_btn.pack(pady=10)
        
        # Initial display
        self.refresh_customers()

    def refresh_customers(self):
        self.customers_text.delete(1.0, tk.END)
        self.customers_text.insert(tk.END, self.showroom.get_customers_display())

    def create_sales_tab(self):
        sales_frame = ttk.Frame(self.notebook)
        self.notebook.add(sales_frame, text="View Sales")
        
        # Title
        title_label = ttk.Label(sales_frame, text="Sales Records", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Display area
        self.sales_text = tk.Text(sales_frame, height=20, width=80)
        scrollbar = ttk.Scrollbar(sales_frame, orient=tk.VERTICAL, command=self.sales_text.yview)
        self.sales_text.configure(yscrollcommand=scrollbar.set)
        
        self.sales_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Refresh button
        refresh_btn = ttk.Button(sales_frame, text="Refresh", command=self.refresh_sales)
        refresh_btn.pack(pady=10)
        
        # Initial display
        self.refresh_sales()

    def refresh_sales(self):
        self.sales_text.delete(1.0, tk.END)
        self.sales_text.insert(tk.END, self.showroom.get_sales_display())

    def create_add_car_tab(self):
        add_car_frame = ttk.Frame(self.notebook)
        self.notebook.add(add_car_frame, text="Add Car")
        
        # Title
        title_label = ttk.Label(add_car_frame, text="Add New Car", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Form fields
        ttk.Label(add_car_frame, text="Car ID:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.car_id_entry = ttk.Entry(add_car_frame)
        self.car_id_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(add_car_frame, text="Brand:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.brand_entry = ttk.Entry(add_car_frame)
        self.brand_entry.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(add_car_frame, text="Model:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.model_entry = ttk.Entry(add_car_frame)
        self.model_entry.grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Label(add_car_frame, text="Year:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.year_entry = ttk.Entry(add_car_frame)
        self.year_entry.grid(row=4, column=1, padx=10, pady=5)
        
        ttk.Label(add_car_frame, text="Price:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        self.price_entry = ttk.Entry(add_car_frame)
        self.price_entry.grid(row=5, column=1, padx=10, pady=5)
        
        # Add button
        add_btn = ttk.Button(add_car_frame, text="Add Car", command=self.add_car)
        add_btn.grid(row=6, column=0, columnspan=2, pady=20)

    def add_car(self):
        try:
            car_id = int(self.car_id_entry.get())
            brand = self.brand_entry.get()
            model = self.model_entry.get()
            year = int(self.year_entry.get())
            price = float(self.price_entry.get())
            
            if not brand or not model:
                messagebox.showerror("Error", "Brand and Model cannot be empty!")
                return
                
            car = Car(car_id, brand, model, year, price)
            self.showroom.add_car(car)
            messagebox.showinfo("Success", f"Car '{car}' added to showroom.")
            
            # Clear entries
            self.car_id_entry.delete(0, tk.END)
            self.brand_entry.delete(0, tk.END)
            self.model_entry.delete(0, tk.END)
            self.year_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            
            # Refresh displays
            self.refresh_cars()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data types!")

    def create_add_customer_tab(self):
        add_customer_frame = ttk.Frame(self.notebook)
        self.notebook.add(add_customer_frame, text="Add Customer")
        
        # Title
        title_label = ttk.Label(add_customer_frame, text="Add New Customer", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Form fields
        ttk.Label(add_customer_frame, text="Customer ID:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.customer_id_entry = ttk.Entry(add_customer_frame)
        self.customer_id_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(add_customer_frame, text="Name:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.customer_name_entry = ttk.Entry(add_customer_frame)
        self.customer_name_entry.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(add_customer_frame, text="Contact:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.customer_contact_entry = ttk.Entry(add_customer_frame)
        self.customer_contact_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Add button
        add_btn = ttk.Button(add_customer_frame, text="Add Customer", command=self.add_customer)
        add_btn.grid(row=4, column=0, columnspan=2, pady=20)

    def add_customer(self):
        try:
            customer_id = int(self.customer_id_entry.get())
            name = self.customer_name_entry.get()
            contact = self.customer_contact_entry.get()
            
            if not name or not contact:
                messagebox.showerror("Error", "Name and Contact cannot be empty!")
                return
                
            customer = Customer(customer_id, name, contact)
            self.showroom.add_customer(customer)
            messagebox.showinfo("Success", f"Customer '{customer}' added to records.")
            
            # Clear entries
            self.customer_id_entry.delete(0, tk.END)
            self.customer_name_entry.delete(0, tk.END)
            self.customer_contact_entry.delete(0, tk.END)
            
            # Refresh displays
            self.refresh_customers()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid Customer ID!")

    def create_sell_car_tab(self):
        sell_car_frame = ttk.Frame(self.notebook)
        self.notebook.add(sell_car_frame, text="Sell Car")
        
        # Title
        title_label = ttk.Label(sell_car_frame, text="Sell Car to Customer", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Form fields
        ttk.Label(sell_car_frame, text="Car ID:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.sell_car_id_entry = ttk.Entry(sell_car_frame)
        self.sell_car_id_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(sell_car_frame, text="Customer ID:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.sell_customer_id_entry = ttk.Entry(sell_car_frame)
        self.sell_customer_id_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Sell button
        sell_btn = ttk.Button(sell_car_frame, text="Sell Car", command=self.sell_car)
        sell_btn.grid(row=3, column=0, columnspan=2, pady=20)

    def sell_car(self):
        try:
            car_id = int(self.sell_car_id_entry.get())
            customer_id = int(self.sell_customer_id_entry.get())
            
            result = self.showroom.sell_car(car_id, customer_id)
            messagebox.showinfo("Result", result)
            
            # Clear entries
            self.sell_car_id_entry.delete(0, tk.END)
            self.sell_customer_id_entry.delete(0, tk.END)
            
            # Refresh displays
            self.refresh_cars()
            self.refresh_sales()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid IDs!")

def main():
    root = tk.Tk()
    app = CarShowroomGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()