from PIL import Image, ImageDraw, ImageFont
import os

# Create a simple default avatar
def create_default_avatar():
    # Create a 300x300 image with a blue background
    img = Image.new('RGB', (300, 300), color='#007bff')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple user icon (circle)
    draw.ellipse([75, 75, 225, 225], fill='white')
    
    # Save the image
    os.makedirs('media/avatars', exist_ok=True)
    img.save('media/avatars/default.png')
    print("Default avatar created successfully!")

if __name__ == "__main__":
    create_default_avatar()
