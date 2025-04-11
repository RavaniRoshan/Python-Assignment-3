#!/usr/bin/env python3
"""
Pillow Image Editor Demo Script
===============================
This script demonstrates the capabilities of the Pillow Image Editor
by automatically running through various editing operations.

Usage:
    python pillow_image_editor_demo.py [path_to_image]

If no image path is provided, the script will attempt to create a sample image.
"""

import os
import sys
import time
from PIL import Image, ImageDraw

# Import the PillowImageEditor class
try:
    from pillow_image_editor import PillowImageEditor
except ImportError:
    print("Error: Could not import PillowImageEditor. Make sure pillow_image_editor.py is in the same directory.")
    sys.exit(1)

def create_sample_image(filename="sample_image.png", size=(600, 400)):
    """Create a sample image with some shapes for testing"""
    print(f"Creating sample image '{filename}'...")
    
    # Create a blank image with white background
    image = Image.new('RGB', size, color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Draw some shapes
    # Rectangle
    draw.rectangle([(50, 50), (200, 150)], outline=(255, 0, 0), width=2)
    
    # Circle
    draw.ellipse([(250, 50), (350, 150)], outline=(0, 255, 0), width=2)
    
    # Line
    draw.line([(400, 50), (550, 150)], fill=(0, 0, 255), width=3)
    
    # Text
    draw.text((150, 200), "Sample Image", fill=(0, 0, 0))
    
    # Save the image
    image.save(filename)
    print(f"Sample image created: {filename}")
    return filename

def demo_editor(image_path):
    """Run a demonstration of the PillowImageEditor functionality"""
    print("\n==== Pillow Image Editor Demo ====\n")
    
    # Create editor instance
    editor = PillowImageEditor()
    
    # Open image
    print("1. Opening image...")
    if not editor.open_image(image_path):
        print("Failed to open image. Exiting demo.")
        return
    
    # Display image
    print("\n2. Displaying image...")
    editor.display_image()
    time.sleep(1)  # Give time for the image to be displayed
    
    # Resize image
    print("\n3. Resizing image to 400x300...")
    editor.resize_image(400, 300)
    editor.display_image()
    time.sleep(1)
    
    # Rotate image
    print("\n4. Rotating image by 45 degrees...")
    editor.rotate_image(45)
    editor.display_image()
    time.sleep(1)
    
    # Apply a filter
    print("\n5. Applying blur filter...")
    editor.apply_filter('blur')
    editor.display_image()
    time.sleep(1)
    
    # Adjust brightness
    print("\n6. Increasing brightness...")
    editor.adjust_brightness(1.5)
    editor.display_image()
    time.sleep(1)
    
    # Convert to grayscale
    print("\n7. Converting to grayscale...")
    editor.convert_mode('L')
    editor.display_image()
    time.sleep(1)
    
    # Add text
    print("\n8. Adding text...")
    editor.convert_mode('RGB')  # Convert back to RGB for colored text
    editor.add_text("Pillow Demo", (50, 50), font_size=30, color=(255, 0, 0))
    editor.display_image()
    time.sleep(1)
    
    # Draw a circle
    print("\n9. Drawing a circle...")
    editor.draw_circle((200, 150), 50, outline_color=(0, 0, 255), width=2)
    editor.display_image()
    time.sleep(1)
    
    # Create a thumbnail
    print("\n10. Creating a thumbnail...")
    editor.create_thumbnail(size=(100, 100))
    
    # Reset to original
    print("\n11. Resetting to original image...")
    editor.reset_image()
    editor.display_image()
    time.sleep(1)
    
    # Save edited image
    print("\n12. Saving edited image...")
    editor.add_text("Final Image", (50, 50), font_size=30, color=(0, 255, 0))
    editor.save_image("demo_output.png")
    
    print("\n==== Demo Complete ====")
    print("Check the following files:")
    print("- demo_output.png (saved edited image)")
    filename, ext = os.path.splitext(image_path)
    print(f"- {filename}_thumb{ext} (thumbnail)")

def main():
    # Check if an image path was provided
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        image_path = sys.argv[1]
        print(f"Using provided image: {image_path}")
    else:
        # Create a sample image if none was provided
        image_path = create_sample_image()
    
    # Run the demo
    demo_editor(image_path)

if __name__ == "__main__":
    main()
