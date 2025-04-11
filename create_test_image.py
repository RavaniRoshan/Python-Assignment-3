from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
width = 800
height = 600
image = Image.new('RGB', (width, height), 'white')

# Get a drawing context
draw = ImageDraw.Draw(image)

# Draw some shapes
draw.rectangle([100, 100, 700, 500], outline='blue', width=2)
draw.ellipse([200, 150, 600, 450], outline='red', width=2)
draw.line([100, 100, 700, 500], fill='green', width=3)

# Add some text
try:
    font = ImageFont.truetype("arial.ttf", 40)
except:
    font = ImageFont.load_default()
    
draw.text((300, 50), "Test Image", fill='black', font=font)

# Save the image
image.save('test_image.png')
print("Test image created successfully as 'test_image.png'") 