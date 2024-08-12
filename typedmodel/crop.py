import cv2
import numpy as np
import os

def crop_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Threshold the image to get a binary image
            _, binary_img = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY_INV)

            # Define a kernel size for dilation and closing
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))  # Adjust the size as needed

            # Apply dilation to connect characters
            dilated_img = cv2.dilate(binary_img, kernel, iterations=1)

            # Apply closing operation to close small gaps
            closed_img = cv2.morphologyEx(dilated_img, cv2.MORPH_CLOSE, kernel)

            # Find contours in the closed image
            contours, _ = cv2.findContours(closed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                # Get the bounding box of the largest contour
                x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))

                # Optionally expand the bounding box to include more area
                expand_x = int(w * 0.1)  # Expand by 10% of width
                expand_y = int(h * 0.1)  # Expand by 10% of height
                x = max(x - expand_x, 0)
                y = max(y - expand_y, 0)
                w = min(w + 2 * expand_x, img.shape[1] - x)
                h = min(h + 2 * expand_y, img.shape[0] - y)

                # Crop the image
                cropped_img = img[y:y+h, x:x+w]
                
                # Save the cropped image
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, cropped_img)

if __name__ == "__main__":
    input_folder = r'C:\Users\shado\OneDrive\Desktop\imagetolatex\data\formula_images'
    output_folder = r'C:\Users\shado\OneDrive\Desktop\imagetolatex\data\fixed_formula_images'
    crop_images(input_folder, output_folder)
