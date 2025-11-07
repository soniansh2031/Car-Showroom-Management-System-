import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import os
import random
import io

class Car:
    def __init__(self, car_id, brand, model, year, price, image_path=None):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.is_available = True
        self.image_path = image_path

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
        # Adding some sample data with image paths
        self.add_car(Car(1, "Toyota", "Camry", 2022, 25000, "toyota_camry.jpg"))
        self.add_car(Car(2, "Honda", "Civic", 2021, 22000, "honda_civic.jpg"))
        self.add_car(Car(3, "Ford", "Mustang", 2023, 35000, "ford_mustang.jpg"))
        self.add_car(Car(4, "BMW", "X5", 2022, 55000, "bmw_x5.jpg"))
        self.add_car(Car(5, "Mercedes", "C-Class", 2023, 45000, "mercedes_c.jpg"))
        
        self.add_customer(Customer(1, "John Doe", "john@email.com"))
        self.add_customer(Customer(2, "Jane Smith", "jane@email.com"))
        self.add_customer(Customer(3, "Robert Johnson", "robert@email.com"))

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

class CarShowroomWithImagesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Premium Car Showroom Management System with Images")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f0f0f0")
        self.showroom = Showroom()
        
        # Create images directory if it doesn't exist
        self.images_dir = "car_images"
        if not os.path.exists(self.images_dir):
            os.makedirs(self.images_dir)
        
        # Configure styles
        self.setup_styles()
        self.setup_ui()

    def setup_styles(self):
        # Define custom fonts
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.header_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=10)
        
        # Define colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.accent_color = "#e74c3c"
        self.success_color = "#27ae60"
        self.light_bg = "#ecf0f1"
        self.dark_text = "#2c3e50"

    def setup_ui(self):
        # Create main header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        header_label = tk.Label(
            header_frame, 
            text="PREMIUM CAR SHOWROOM MANAGEMENT SYSTEM WITH IMAGES", 
            font=self.title_font,
            fg="white",
            bg=self.primary_color
        )
        header_label.pack(pady=20)
        
        # Create notebook for tabs with custom style
        style = ttk.Style()
        style.configure("Custom.TNotebook", background=self.light_bg)
        style.configure("Custom.TNotebook.Tab", padding=[10, 5])
        
        self.notebook = ttk.Notebook(self.root, style="Custom.TNotebook")
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_home_tab()
        self.create_cars_tab()
        self.create_car_gallery_tab()
        self.create_customers_tab()
        self.create_sales_tab()
        self.create_add_car_tab()
        self.create_add_customer_tab()
        self.create_sell_car_tab()

    def create_home_tab(self):
        home_frame = tk.Frame(self.notebook, bg=self.light_bg)
        self.notebook.add(home_frame, text="Dashboard")
        
        # Welcome message
        welcome_label = tk.Label(
            home_frame,
            text="Welcome to Premium Car Showroom",
            font=self.title_font,
            fg=self.primary_color,
            bg=self.light_bg
        )
        welcome_label.pack(pady=20)
        
        # Stats frame
        stats_frame = tk.Frame(home_frame, bg=self.light_bg)
        stats_frame.pack(pady=20)
        
        # Car stats
        car_frame = tk.Frame(stats_frame, bg=self.secondary_color, relief=tk.RAISED, bd=2)
        car_frame.pack(side=tk.LEFT, padx=20, pady=10)
        
        car_count = len(self.showroom.cars)
        available_count = len([car for car in self.showroom.cars if car.is_available])
        
        car_label = tk.Label(
            car_frame,
            text=f"Total Cars\n{car_count}",
            font=self.header_font,
            fg="white",
            bg=self.secondary_color
        )
        car_label.pack(padx=20, pady=10)
        
        available_label = tk.Label(
            car_frame,
            text=f"Available\n{available_count}",
            font=self.normal_font,
            fg="white",
            bg=self.secondary_color
        )
        available_label.pack(padx=20, pady=(0, 10))
        
        # Customer stats
        customer_frame = tk.Frame(stats_frame, bg=self.success_color, relief=tk.RAISED, bd=2)
        customer_frame.pack(side=tk.LEFT, padx=20, pady=10)
        
        customer_count = len(self.showroom.customers)
        
        customer_label = tk.Label(
            customer_frame,
            text=f"Total Customers\n{customer_count}",
            font=self.header_font,
            fg="white",
            bg=self.success_color
        )
        customer_label.pack(padx=20, pady=10)
        
        # Sales stats
        sales_frame = tk.Frame(stats_frame, bg=self.accent_color, relief=tk.RAISED, bd=2)
        sales_frame.pack(side=tk.LEFT, padx=20, pady=10)
        
        sales_count = len(self.showroom.sales)
        
        sales_label = tk.Label(
            sales_frame,
            text=f"Total Sales\n{sales_count}",
            font=self.header_font,
            fg="white",
            bg=self.accent_color
        )
        sales_label.pack(padx=20, pady=10)
        
        # Recent activity
        activity_frame = tk.Frame(home_frame, bg="white", relief=tk.RAISED, bd=1)
        activity_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
        
        activity_label = tk.Label(
            activity_frame,
            text="Recent Activity",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        )
        activity_label.pack(pady=10)
        
        # Sample recent activities
        activities = [
            "Toyota Camry added to showroom",
            "John Doe registered as customer",
            "BMW X5 sold to Jane Smith",
            "Mercedes C-Class added to showroom"
        ]
        
        for activity in activities:
            activity_item = tk.Label(
                activity_frame,
                text=f"• {activity}",
                font=self.normal_font,
                fg=self.dark_text,
                bg="white",
                anchor="w"
            )
            activity_item.pack(fill=tk.X, padx=20, pady=2)

    def create_cars_tab(self):
        cars_frame = tk.Frame(self.notebook, bg=self.light_bg)
        self.notebook.add(cars_frame, text="View Cars")
        
        # Title
        title_label = tk.Label(
            cars_frame,
            text="Cars in Showroom",
            font=self.title_font,
            fg=self.primary_color,
            bg=self.light_bg
        )
        title_label.pack(pady=10)
        
        # Control frame
        control_frame = tk.Frame(cars_frame, bg=self.light_bg)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        refresh_btn = tk.Button(
            control_frame,
            text="Refresh",
            command=self.refresh_cars,
            bg=self.secondary_color,
            fg="white",
            font=self.normal_font,
            relief=tk.FLAT,
            padx=10
        )
        refresh_btn.pack(side=tk.RIGHT, padx=5)
        
        # Display area with custom styling
        display_frame = tk.Frame(cars_frame, bg="white", relief=tk.RAISED, bd=1)
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.cars_text = tk.Text(
            display_frame,
            height=20,
            bg="white",
            fg=self.dark_text,
            font=self.normal_font,
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        scrollbar = tk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.cars_text.yview)
        self.cars_text.configure(yscrollcommand=scrollbar.set)
        
        self.cars_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Initial display
        self.refresh_cars()

    def refresh_cars(self):
        self.cars_text.delete(1.0, tk.END)
        cars_display = self.showroom.get_cars_display()
        self.cars_text.insert(tk.END, cars_display)
        
        # Color coding for availability
        lines = cars_display.split('\n')
        for i, line in enumerate(lines):
            if "Available" in line:
                start_idx = f"{i+1}.0"
                end_idx = f"{i+1}.{len(line)}"
                self.cars_text.tag_add("available", start_idx, end_idx)
                self.cars_text.tag_config("available", foreground=self.success_color)
            elif "Sold" in line:
                start_idx = f"{i+1}.0"
                end_idx = f"{i+1}.{len(line)}"
                self.cars_text.tag_add("sold", start_idx, end_idx)
                self.cars_text.tag_config("sold", foreground=self.accent_color)

    def create_car_gallery_tab(self):
        gallery_frame = tk.Frame(self.notebook, bg=self.light_bg)
        self.notebook.add(gallery_frame, text="Car Gallery")
        
        # Title
        title_label = tk.Label(
            gallery_frame,
            text="Car Gallery",
            font=self.title_font,
            fg=self.primary_color,
            bg=self.light_bg
        )
        title_label.pack(pady=10)
        
        # Create canvas and scrollbar for gallery
        canvas_frame = tk.Frame(gallery_frame, bg=self.light_bg)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg=self.light_bg)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.light_bg)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Display cars in gallery format
        self.display_car_gallery(scrollable_frame)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def display_car_gallery(self, parent_frame):
        # Clear existing widgets
        for widget in parent_frame.winfo_children():
            widget.destroy()
            
        # Display cars in a grid
        row, col = 0, 0
        for car in self.showroom.cars:
            # Create card for each car
            card_frame = tk.Frame(parent_frame, bg="white", relief=tk.RAISED, bd=2)
            card_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Car image
            try:
                # Create a placeholder image if the actual image doesn't exist
                if os.path.exists(os.path.join(self.images_dir, car.image_path)):
                    image = Image.open(os.path.join(self.images_dir, car.image_path))
                    image = image.resize((200, 150), Image.LANCZOS)
                else:
                    # Create a placeholder image
                    image = Image.new('RGB', (200, 150), color=(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
                
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(card_frame, image=photo, bg="white")
                image_label.image = photo  # Keep a reference
                image_label.pack(pady=5)
            except Exception as e:
                # If image loading fails, show a colored rectangle
                placeholder = tk.Frame(card_frame, width=200, height=150, bg=f"#{random.randint(0, 0xFFFFFF):06x}")
                placeholder.pack(pady=5)
            
            # Car details
            details_frame = tk.Frame(card_frame, bg="white")
            details_frame.pack(pady=5)
            
            tk.Label(details_frame, text=f"{car.brand} {car.model}", font=self.header_font, bg="white").pack()
            tk.Label(details_frame, text=f"Year: {car.year}", font=self.normal_font, bg="white").pack()
            tk.Label(details_frame, text=f"Price: ${car.price}", font=self.normal_font, bg="white").pack()
            
            status_color = self.success_color if car.is_available else self.accent_color
            status_text = "Available" if car.is_available else "Sold"
            tk.Label(details_frame, text=status_text, font=self.normal_font, fg=status_color, bg="white").pack()
            
            # Move to next column/row
            col += 1
            if col > 2:  # 3 columns per row
                col = 0
                row += 1

    def create_customers_tab(self):
        customers_frame = tk.Frame(self.notebook, bg=self.light_bg)
        self.notebook.add(customers_frame, text="View Customers")
        
        # Title
        title_label = tk.Label(
            customers_frame,
            text="Registered Customers",
            font=self.title_font,
            fg=self.primary_color,
            bg=self.light_bg
        )
        title_label.pack(pady=10)
        
        # Control frame
        control_frame = tk.Frame(customers_frame, bg=self.light_bg)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        refresh_btn = tk.Button(
            control_frame,
            text="Refresh",
            command=self.refresh_customers,
            bg=self.secondary_color,
            fg="white",
            font=self.normal_font,
            relief=tk.FLAT,
            padx=10
        )
        refresh_btn.pack(side=tk.RIGHT, padx=5)
        
        # Display area
        display_frame = tk.Frame(customers_frame, bg="white", relief=tk.RAISED, bd=1)
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.customers_text = tk.Text(
            display_frame,
            height=20,
            bg="white",
            fg=self.dark_text,
            font=self.normal_font,
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        scrollbar = tk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.customers_text.yview)
        self.customers_text.configure(yscrollcommand=scrollbar.set)
        
        self.customers_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Initial display
        self.refresh_customers()

    def refresh_customers(self):
        self.customers_text.delete(1.0, tk.END)
        self.customers_text.insert(tk.END, self.showroom.get_customers_display())

    def create_sales_tab(self):
        sales_frame = tk.Frame(self.notebook, bg=self.light_bg)
        self.notebook.add(sales_frame, text="View Sales")
        
        # Title
        title_label = tk.Label(
            sales_frame,
            text="Sales Records",
            font=self.title_font,
            fg=self.primary_color,
            bg=self.light_bg
        )
        title_label.pack(pady=10)
        
        # Control frame
        control_frame = tk.Frame(sales_frame, bg=self.light_bg)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        refresh_btn = tk.Button(
            control_frame,
            text="Refresh",
            command=self.refresh_sales,
            bg=self.secondary_color,
            fg="white",
            font=self.normal_font,
            relief=tk.FLAT,
            padx=10
        )
        refresh_btn.pack(side=tk.RIGHT, padx=5)
        
        # Display area
        display_frame = tk.Frame(sales_frame, bg="white", relief=tk.RAISED, bd=1)
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.sales_text = tk.Text(
            display_frame,
            height=20,
            bg="white",
            fg=self.dark_text,
            font=self.normal_font,
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        scrollbar = tk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.sales_text.yview)
        self.sales_text.configure(yscrollcommand=scrollbar.set)
        
        self.sales_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Initial display
        self.refresh_sales()

    def refresh_sales(self):
        self.sales_text.delete(1.0, tk.END)
        self.sales_text.insert(tk.END, self.showroom.get_sales_display())

    def create_add_car_tab(self):
        add_car_frame = tk.Frame(self.notebook, bg=self.light_bg)
        self.notebook.add(add_car_frame, text="Add Car")
        
        # Title
        title_label = tk.Label(
            add_car_frame,
            text="Add New Car",
            font=self.title_font,
            fg=self.primary_color,
            bg=self.light_bg
        )
        title_label.pack(pady=10)
        
        # Form container
        form_frame = tk.Frame(add_car_frame, bg="white", relief=tk.RAISED, bd=1)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=100, pady=20)
        
        # Form fields with styling
        field_padding = 10
        
        # Car ID
        car_id_frame = tk.Frame(form_frame, bg="white")
        car_id_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            car_id_frame,
            text="Car ID:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.car_id_entry = tk.Entry(
            car_id_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.car_id_entry.pack(side=tk.RIGHT, padx=10)
        
        # Brand
        brand_frame = tk.Frame(form_frame, bg="white")
        brand_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            brand_frame,
            text="Brand:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.brand_entry = tk.Entry(
            brand_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.brand_entry.pack(side=tk.RIGHT, padx=10)
        
        # Model
        model_frame = tk.Frame(form_frame, bg="white")
        model_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            model_frame,
            text="Model:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.model_entry = tk.Entry(
            model_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.model_entry.pack(side=tk.RIGHT, padx=10)
        
        # Year
        year_frame = tk.Frame(form_frame, bg="white")
        year_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            year_frame,
            text="Year:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.year_entry = tk.Entry(
            year_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.year_entry.pack(side=tk.RIGHT, padx=10)
        
        # Price
        price_frame = tk.Frame(form_frame, bg="white")
        price_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            price_frame,
            text="Price:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.price_entry = tk.Entry(
            price_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.price_entry.pack(side=tk.RIGHT, padx=10)
        
        # Image path
        image_frame = tk.Frame(form_frame, bg="white")
        image_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            image_frame,
            text="Image Path:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.image_entry = tk.Entry(
            image_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.image_entry.pack(side=tk.RIGHT, padx=10)
        
        # Add button
        add_btn = tk.Button(
            form_frame,
            text="Add Car",
            command=self.add_car,
            bg=self.success_color,
            fg="white",
            font=self.header_font,
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        add_btn.pack(pady=30)

    def add_car(self):
        try:
            car_id = int(self.car_id_entry.get())
            brand = self.brand_entry.get()
            model = self.model_entry.get()
            year = int(self.year_entry.get())
            price = float(self.price_entry.get())
            image_path = self.image_entry.get()
            
            if not brand or not model:
                messagebox.showerror("Error", "Brand and Model cannot be empty!")
                return
                
            car = Car(car_id, brand, model, year, price, image_path)
            self.showroom.add_car(car)
            messagebox.showinfo("Success", f"Car '{car}' added to showroom.")
            
            # Clear entries
            self.car_id_entry.delete(0, tk.END)
            self.brand_entry.delete(0, tk.END)
            self.model_entry.delete(0, tk.END)
            self.year_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.image_entry.delete(0, tk.END)
            
            # Refresh displays
            self.refresh_cars()
            self.display_car_gallery(self.notebook.nametowidget(self.notebook.tabs()[1]))
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data types!")

    def create_add_customer_tab(self):
        add_customer_frame = tk.Frame(self.notebook, bg=self.light_bg)
        self.notebook.add(add_customer_frame, text="Add Customer")
        
        # Title
        title_label = tk.Label(
            add_customer_frame,
            text="Add New Customer",
            font=self.title_font,
            fg=self.primary_color,
            bg=self.light_bg
        )
        title_label.pack(pady=10)
        
        # Form container
        form_frame = tk.Frame(add_customer_frame, bg="white", relief=tk.RAISED, bd=1)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=100, pady=20)
        
        # Form fields with styling
        field_padding = 10
        
        # Customer ID
        customer_id_frame = tk.Frame(form_frame, bg="white")
        customer_id_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            customer_id_frame,
            text="Customer ID:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.customer_id_entry = tk.Entry(
            customer_id_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.customer_id_entry.pack(side=tk.RIGHT, padx=10)
        
        # Name
        name_frame = tk.Frame(form_frame, bg="white")
        name_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            name_frame,
            text="Name:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.customer_name_entry = tk.Entry(
            name_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.customer_name_entry.pack(side=tk.RIGHT, padx=10)
        
        # Contact
        contact_frame = tk.Frame(form_frame, bg="white")
        contact_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            contact_frame,
            text="Contact:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.customer_contact_entry = tk.Entry(
            contact_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.customer_contact_entry.pack(side=tk.RIGHT, padx=10)
        
        # Add button
        add_btn = tk.Button(
            form_frame,
            text="Add Customer",
            command=self.add_customer,
            bg=self.success_color,
            fg="white",
            font=self.header_font,
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        add_btn.pack(pady=30)

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
        sell_car_frame = tk.Frame(self.notebook, bg=self.light_bg)
        self.notebook.add(sell_car_frame, text="Sell Car")
        
        # Title
        title_label = tk.Label(
            sell_car_frame,
            text="Sell Car to Customer",
            font=self.title_font,
            fg=self.primary_color,
            bg=self.light_bg
        )
        title_label.pack(pady=10)
        
        # Form container
        form_frame = tk.Frame(sell_car_frame, bg="white", relief=tk.RAISED, bd=1)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=100, pady=20)
        
        # Form fields with styling
        field_padding = 10
        
        # Car ID
        car_id_frame = tk.Frame(form_frame, bg="white")
        car_id_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            car_id_frame,
            text="Car ID:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.sell_car_id_entry = tk.Entry(
            car_id_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.sell_car_id_entry.pack(side=tk.RIGHT, padx=10)
        
        # Customer ID
        customer_id_frame = tk.Frame(form_frame, bg="white")
        customer_id_frame.pack(fill=tk.X, padx=20, pady=field_padding)
        
        tk.Label(
            customer_id_frame,
            text="Customer ID:",
            font=self.header_font,
            fg=self.dark_text,
            bg="white"
        ).pack(side=tk.LEFT)
        
        self.sell_customer_id_entry = tk.Entry(
            customer_id_frame,
            font=self.normal_font,
            relief=tk.FLAT,
            bg=self.light_bg,
            width=30
        )
        self.sell_customer_id_entry.pack(side=tk.RIGHT, padx=10)
        
        # Sell button
        sell_btn = tk.Button(
            form_frame,
            text="Sell Car",
            command=self.sell_car,
            bg=self.accent_color,
            fg="white",
            font=self.header_font,
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        sell_btn.pack(pady=30)

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
            self.display_car_gallery(self.notebook.nametowidget(self.notebook.tabs()[1]))
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid IDs!")

def main():
    root = tk.Tk()
    app = CarShowroomWithImagesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()