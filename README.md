# Pillow Image Editor
## Python Advanced Libraries Mini Project

A comprehensive image editing application built using Python's Pillow library, demonstrating various image processing capabilities and user interaction through a command-line interface.

### Project Overview
This project was developed as part of the Advanced Libraries in Python course assignment. It showcases the implementation of image processing operations using the PIL (Python Imaging Library) module, specifically its fork, Pillow.

### Features
- Basic Image Operations:
  - Open and save images in various formats
  - Display images
  - Resize images
  - Crop images
  - Rotate images
  - Flip images (horizontal/vertical)

- Image Enhancement:
  - Adjust brightness
  - Adjust contrast
  - Adjust color saturation
  - Adjust sharpness
  - Apply various filters (blur, contour, detail, edge enhance, emboss, sharpen, smooth)

- Drawing Operations:
  - Add text with customizable font, size, and color
  - Draw rectangles
  - Draw circles
  - Create collages from multiple images

- Format Operations:
  - Convert between different image formats
  - Create thumbnails
  - Convert to grayscale

### Requirements
- Python 3.x
- Required packages:
  ```
  Pillow
  numpy
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd pillow-image-editor
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Run the program:
   ```bash
   python pillow_image_editor.py
   ```

2. Follow the interactive menu to perform various operations:
   - Enter numbers 1-20 to select different operations
   - Follow the prompts for each operation
   - Enter 0 to exit the program

### Example Operations
1. Opening an image:
   ```
   Enter choice: 1
   Enter the path to the image: test_image.png
   ```

2. Adjusting brightness:
   ```
   Enter choice: 8
   Enter brightness factor (0.0-2.0, 1.0 is original): 1.2
   ```

3. Adding text:
   ```
   Enter choice: 14
   Enter text: Hello World
   Enter x position: 100
   Enter y position: 100
   Enter font size: 40
   Enter RGB color (comma-separated): 255,0,0
   ```

### Project Structure
- `pillow_image_editor.py`: Main program file containing the image editor implementation
- `requirements.txt`: List of Python dependencies
- `README.md`: Project documentation

### Features in Detail
1. **Image Enhancement**
   - Brightness adjustment (0.0 to 2.0)
   - Contrast adjustment (0.0 to 2.0)
   - Color saturation (0.0 to 2.0)
   - Sharpness adjustment (0.0 to 2.0)

2. **Filters**
   - Blur
   - Contour
   - Detail
   - Edge Enhance
   - Emboss
   - Sharpen
   - Smooth

3. **Format Support**
   - JPEG
   - PNG
   - BMP
   - GIF
   - TIFF

### Error Handling
The program includes comprehensive error handling for:
- File operations
- Invalid input values
- Unsupported operations
- Memory constraints

### Best Practices Demonstrated
- Object-Oriented Programming
- Error Handling
- User Input Validation
- Code Documentation
- Modular Design

### Future Enhancements
Potential areas for improvement:
- Graphical User Interface (GUI)
- Batch processing capabilities
- Additional filters and effects
- Image metadata handling
- Undo/Redo functionality

### Contributing
This is a college assignment project. While it's not open for contributions, you're welcome to fork the repository and extend it for your own use.

### License
This project is created for educational purposes as part of a college assignment.

### Author
[Your Name]
[Your College Name]
[Your Course/Class]

### Acknowledgments
- Python Pillow Documentation
- Course Instructors and Teaching Assistants
- [Any other acknowledgments]

---
*Note: This project was created as part of a college assignment demonstrating the use of advanced Python libraries, specifically focusing on image processing using Pillow.* 