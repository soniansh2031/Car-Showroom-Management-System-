import os
from PIL import Image, ImageDraw
import random

def create_placeholder_image(width, height, color, text, filename):
    """Create a placeholder image with text"""
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)
    
    # Create a simple image without text (to avoid font issues)
    image.save(filename)
    print(f"Created placeholder image: {filename}")

def create_sample_images():
    """Create sample images for the car showroom"""
    # Create car_images directory if it doesn't exist
    images_dir = "car_images"
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # Create placeholder images for different car brands
    cars = [
        {"name": "toyota_camry.jpg", "color": (255, 0, 0), "text": "Toyota Camry"},
        {"name": "honda_civic.jpg", "color": (0, 255, 0), "text": "Honda Civic"},
        {"name": "ford_mustang.jpg", "color": (0, 0, 255), "text": "Ford Mustang"},
        {"name": "bmw_x5.jpg", "color": (255, 255, 0), "text": "BMW X5"},
        {"name": "mercedes_c.jpg", "color": (255, 0, 255), "text": "Mercedes C-Class"}
    ]
    
    for car in cars:
        filename = os.path.join(images_dir, car["name"])
        create_placeholder_image(300, 200, car["color"], car["text"], filename)
    
    print("Sample images created successfully!")

if __name__ == "__main__":
    create_sample_images()