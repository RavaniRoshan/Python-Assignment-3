"""
Pillow Image Editor - A Mini Project on Advanced Libraries in Python
=================================================================

This project demonstrates the capabilities of the Pillow library for image processing.
It implements a simple command-line image editor with various features.

Author: [Your Name]
Date: April 11, 2025
"""

import os
import sys
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import numpy as np

class PillowImageEditor:
    """A simple image editor class using Pillow library"""
    
    def __init__(self):
        """Initialize the image editor"""
        self.image = None
        self.original_image = None
        self.filename = None
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
        
    def open_image(self, filepath):
        """Open an image file"""
        try:
            self.image = Image.open(filepath)
            self.original_image = self.image.copy()
            self.filename = os.path.basename(filepath)
            print(f"Successfully opened {self.filename}")
            print(f"Image size: {self.image.size}")
            print(f"Image format: {self.image.format}")
            print(f"Image mode: {self.image.mode}")
            return True
        except Exception as e:
            print(f"Error opening image: {e}")
            return False
            
    def display_image(self):
        """Display the current image"""
        if self.image:
            self.image.show()
        else:
            print("No image loaded.")
            
    def save_image(self, output_path=None):
        """Save the current image"""
        if not self.image:
            print("No image loaded.")
            return False
            
        if not output_path:
            # Create a new filename with "_edited" suffix
            filename, ext = os.path.splitext(self.filename)
            output_path = f"{filename}_edited{ext}"
            
        try:
            self.image.save(output_path)
            print(f"Image saved as {output_path}")
            return True
        except Exception as e:
            print(f"Error saving image: {e}")
            return False
            
    def reset_image(self):
        """Reset the image to its original state"""
        if self.original_image:
            self.image = self.original_image.copy()
            print("Image reset to original.")
        else:
            print("No original image available.")
            
    def resize_image(self, width, height):
        """Resize the image to the specified dimensions"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            self.image = self.image.resize((width, height))
            print(f"Image resized to {width}x{height}")
        except Exception as e:
            print(f"Error resizing image: {e}")
            
    def crop_image(self, left, top, right, bottom):
        """Crop the image to the specified coordinates"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            self.image = self.image.crop((left, top, right, bottom))
            print(f"Image cropped to coordinates ({left}, {top}, {right}, {bottom})")
        except Exception as e:
            print(f"Error cropping image: {e}")
            
    def rotate_image(self, degrees):
        """Rotate the image by the specified degrees"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            self.image = self.image.rotate(degrees, expand=True)
            print(f"Image rotated by {degrees} degrees")
        except Exception as e:
            print(f"Error rotating image: {e}")
            
    def flip_image(self, direction):
        """Flip the image horizontally or vertically"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            if direction.lower() == 'horizontal':
                self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
                print("Image flipped horizontally")
            elif direction.lower() == 'vertical':
                self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
                print("Image flipped vertically")
            else:
                print("Invalid direction. Use 'horizontal' or 'vertical'.")
        except Exception as e:
            print(f"Error flipping image: {e}")
    
    def adjust_brightness(self, factor):
        """Adjust the brightness of the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
            print(f"Brightness adjusted by factor of {factor}")
        except Exception as e:
            print(f"Error adjusting brightness: {e}")
            
    def adjust_contrast(self, factor):
        """Adjust the contrast of the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            enhancer = ImageEnhance.Contrast(self.image)
            self.image = enhancer.enhance(factor)
            print(f"Contrast adjusted by factor of {factor}")
        except Exception as e:
            print(f"Error adjusting contrast: {e}")
            
    def adjust_color(self, factor):
        """Adjust the color saturation of the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            enhancer = ImageEnhance.Color(self.image)
            self.image = enhancer.enhance(factor)
            print(f"Color saturation adjusted by factor of {factor}")
        except Exception as e:
            print(f"Error adjusting color: {e}")
            
    def adjust_sharpness(self, factor):
        """Adjust the sharpness of the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            enhancer = ImageEnhance.Sharpness(self.image)
            self.image = enhancer.enhance(factor)
            print(f"Sharpness adjusted by factor of {factor}")
        except Exception as e:
            print(f"Error adjusting sharpness: {e}")
    
    def apply_filter(self, filter_name):
        """Apply a filter to the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        filters = {
            'blur': ImageFilter.BLUR,
            'contour': ImageFilter.CONTOUR,
            'detail': ImageFilter.DETAIL,
            'edge_enhance': ImageFilter.EDGE_ENHANCE,
            'emboss': ImageFilter.EMBOSS,
            'sharpen': ImageFilter.SHARPEN,
            'smooth': ImageFilter.SMOOTH
        }
        
        if filter_name.lower() in filters:
            try:
                self.image = self.image.filter(filters[filter_name.lower()])
                print(f"Applied {filter_name} filter")
            except Exception as e:
                print(f"Error applying filter: {e}")
        else:
            print(f"Filter not found. Available filters: {', '.join(filters.keys())}")
            
    def convert_mode(self, mode):
        """Convert the image to a different color mode"""
        if not self.image:
            print("No image loaded.")
            return
            
        modes = ['L', 'RGB', 'RGBA', 'CMYK', '1', 'P']
        
        if mode.upper() in modes:
            try:
                self.image = self.image.convert(mode.upper())
                print(f"Image converted to {mode.upper()} mode")
            except Exception as e:
                print(f"Error converting image mode: {e}")
        else:
            print(f"Mode not supported. Available modes: {', '.join(modes)}")
            
    def add_text(self, text, position, font_size=40, color=(0, 0, 0)):
        """Add text to the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            # Create a drawing object
            draw = ImageDraw.Draw(self.image)
            
            # Use default font if available
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                # Use default font
                font = ImageFont.load_default()
                
            # Draw the text
            draw.text(position, text, font=font, fill=color)
            print(f"Text added at position {position}")
        except Exception as e:
            print(f"Error adding text: {e}")
            
    def draw_rectangle(self, coords, outline_color=(0, 0, 0), width=1):
        """Draw a rectangle on the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            draw = ImageDraw.Draw(self.image)
            draw.rectangle(coords, outline=outline_color, width=width)
            print(f"Rectangle drawn at coordinates {coords}")
        except Exception as e:
            print(f"Error drawing rectangle: {e}")
            
    def draw_circle(self, center, radius, outline_color=(0, 0, 0), width=1):
        """Draw a circle on the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            draw = ImageDraw.Draw(self.image)
            coords = (center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius)
            draw.ellipse(coords, outline=outline_color, width=width)
            print(f"Circle drawn at center {center} with radius {radius}")
        except Exception as e:
            print(f"Error drawing circle: {e}")
    
    def create_thumbnail(self, size=(128, 128)):
        """Create a thumbnail of the image"""
        if not self.image:
            print("No image loaded.")
            return
            
        try:
            # Create a copy to avoid modifying the original
            thumb = self.image.copy()
            thumb.thumbnail(size)
            
            # Save with "_thumb" suffix
            filename, ext = os.path.splitext(self.filename)
            output_path = f"{filename}_thumb{ext}"
            thumb.save(output_path)
            
            print(f"Thumbnail created and saved as {output_path}")
        except Exception as e:
            print(f"Error creating thumbnail: {e}")
    
    def create_collage(self, image_paths, cols=2, padding=10):
        """Create a collage from multiple images"""
        if not image_paths:
            print("No image paths provided.")
            return
            
        try:
            # Open all images
            images = []
            for path in image_paths:
                if os.path.exists(path):
                    img = Image.open(path)
                    images.append(img)
                else:
                    print(f"Image not found: {path}")
            
            if not images:
                print("No valid images found.")
                return
                
            # Calculate rows needed
            rows = (len(images) + cols - 1) // cols
            
            # Find maximum dimensions
            max_width = max(img.width for img in images)
            max_height = max(img.height for img in images)
            
            # Create a new image for the collage
            collage_width = cols * (max_width + padding) + padding
            collage_height = rows * (max_height + padding) + padding
            collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))
            
            # Paste images into the collage
            for i, img in enumerate(images):
                row = i // cols
                col = i % cols
                x = col * (max_width + padding) + padding
                y = row * (max_height + padding) + padding
                collage.paste(img, (x, y))
            
            self.image = collage
            self.original_image = collage.copy()
            self.filename = "collage.jpg"
            print("Collage created successfully.")
        except Exception as e:
            print(f"Error creating collage: {e}")
            
    def convert_format(self, output_format):
        """Convert the image to a different format"""
        if not self.image:
            print("No image loaded.")
            return
            
        # Strip the dot if included
        if output_format.startswith('.'):
            output_format = output_format[1:]
            
        # Check if the format is supported
        if f".{output_format.lower()}" not in self.supported_formats:
            print(f"Format not supported. Supported formats: {', '.join(self.supported_formats)}")
            return
            
        try:
            # Create a new filename with the new extension
            filename, _ = os.path.splitext(self.filename)
            output_path = f"{filename}.{output_format.lower()}"
            
            # Save in the new format
            self.image.save(output_path)
            print(f"Image converted and saved as {output_path}")
        except Exception as e:
            print(f"Error converting format: {e}")

def show_menu():
    """Display the menu options"""
    print("\n==== Pillow Image Editor ====")
    print("1. Open image")
    print("2. Display current image")
    print("3. Save image")
    print("4. Resize image")
    print("5. Crop image")
    print("6. Rotate image")
    print("7. Flip image")
    print("8. Adjust brightness")
    print("9. Adjust contrast")
    print("10. Adjust color saturation")
    print("11. Adjust sharpness")
    print("12. Apply filter")
    print("13. Convert to grayscale")
    print("14. Add text")
    print("15. Draw rectangle")
    print("16. Draw circle")
    print("17. Create thumbnail")
    print("18. Create collage")
    print("19. Convert format")
    print("20. Reset to original")
    print("0. Exit")
    return input("Enter your choice: ")

def main():
    """Main function to run the image editor"""
    editor = PillowImageEditor()
    
    while True:
        choice = show_menu()
        
        if choice == '0':
            print("Exiting...")
            break
            
        elif choice == '1':
            filepath = input("Enter the path to the image: ")
            editor.open_image(filepath)
            
        elif choice == '2':
            editor.display_image()
            
        elif choice == '3':
            output_path = input("Enter output path (or press Enter for default): ")
            if not output_path.strip():
                output_path = None
            editor.save_image(output_path)
            
        elif choice == '4':
            try:
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                editor.resize_image(width, height)
            except ValueError:
                print("Invalid dimensions. Please enter integers for width and height.")
                
        elif choice == '5':
            try:
                left = int(input("Enter left coordinate: "))
                top = int(input("Enter top coordinate: "))
                right = int(input("Enter right coordinate: "))
                bottom = int(input("Enter bottom coordinate: "))
                editor.crop_image(left, top, right, bottom)
            except ValueError:
                print("Invalid coordinates. Please enter integers.")
                
        elif choice == '6':
            try:
                degrees = float(input("Enter degrees to rotate: "))
                editor.rotate_image(degrees)
            except ValueError:
                print("Invalid value. Please enter a number.")
                
        elif choice == '7':
            direction = input("Enter flip direction (horizontal/vertical): ")
            editor.flip_image(direction)
            
        elif choice == '8':
            try:
                factor = float(input("Enter brightness factor (0.0-2.0, 1.0 is original): "))
                editor.adjust_brightness(factor)
            except ValueError:
                print("Invalid value. Please enter a number.")
                
        elif choice == '9':
            try:
                factor = float(input("Enter contrast factor (0.0-2.0, 1.0 is original): "))
                editor.adjust_contrast(factor)
            except ValueError:
                print("Invalid value. Please enter a number.")
                
        elif choice == '10':
            try:
                factor = float(input("Enter color factor (0.0-2.0, 1.0 is original): "))
                editor.adjust_color(factor)
            except ValueError:
                print("Invalid value. Please enter a number.")
                
        elif choice == '11':
            try:
                factor = float(input("Enter sharpness factor (0.0-2.0, 1.0 is original): "))
                editor.adjust_sharpness(factor)
            except ValueError:
                print("Invalid value. Please enter a number.")
                
        elif choice == '12':
            print("Available filters: blur, contour, detail, edge_enhance, emboss, sharpen, smooth")
            filter_name = input("Enter filter name: ")
            editor.apply_filter(filter_name)
            
        elif choice == '13':
            editor.convert_mode('L')
            
        elif choice == '14':
            text = input("Enter text: ")
            try:
                x = int(input("Enter x position: "))
                y = int(input("Enter y position: "))
                size = int(input("Enter font size (default 40): ") or "40")
                color_input = input("Enter RGB color (comma-separated, default 0,0,0): ") or "0,0,0"
                color = tuple(map(int, color_input.split(',')))
                editor.add_text(text, (x, y), size, color)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                
        elif choice == '15':
            try:
                x1 = int(input("Enter top-left x: "))
                y1 = int(input("Enter top-left y: "))
                x2 = int(input("Enter bottom-right x: "))
                y2 = int(input("Enter bottom-right y: "))
                color_input = input("Enter RGB color (comma-separated, default 0,0,0): ") or "0,0,0"
                color = tuple(map(int, color_input.split(',')))
                width = int(input("Enter line width (default 1): ") or "1")
                editor.draw_rectangle((x1, y1, x2, y2), color, width)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                
        elif choice == '16':
            try:
                x = int(input("Enter center x: "))
                y = int(input("Enter center y: "))
                radius = int(input("Enter radius: "))
                color_input = input("Enter RGB color (comma-separated, default 0,0,0): ") or "0,0,0"
                color = tuple(map(int, color_input.split(',')))
                width = int(input("Enter line width (default 1): ") or "1")
                editor.draw_circle((x, y), radius, color, width)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                
        elif choice == '17':
            try:
                width = int(input("Enter thumbnail width (default 128): ") or "128")
                height = int(input("Enter thumbnail height (default 128): ") or "128")
                editor.create_thumbnail((width, height))
            except ValueError:
                print("Invalid dimensions. Please enter integers.")
                
        elif choice == '18':
            num_images = int(input("Enter number of images for collage: "))
            paths = []
            for i in range(num_images):
                path = input(f"Enter path for image {i+1}: ")
                paths.append(path)
            cols = int(input("Enter number of columns (default 2): ") or "2")
            editor.create_collage(paths, cols)
            
        elif choice == '19':
            format_name = input("Enter new format (jpg, png, etc.): ")
            editor.convert_format(format_name)
            
        elif choice == '20':
            editor.reset_image()
            
        else:
            print("Invalid choice. Please try again.")
            
        print("\nPress Enter to continue...")
        input()

if __name__ == "__main__":
    main()
