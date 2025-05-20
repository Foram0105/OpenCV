import cv2
import os

# Define input and output folder
input_folder = "input_images"
output_folder = "filtered_images"
output_resized_folder = "output_images"

# Ensure the output folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(output_resized_folder, exist_ok=True)

# Get user input for resizing
width = int(input("Enter the width for resized images: "))
height = int(input("Enter the height for resized images: "))

# Load an image from the input_images folder
image = cv2.imread("Images.png")

if image is None:
    print(f"Error: Unable to load image {image}")
else:
    # Resize the image
    resized_image = cv2.resize(image, (width, height))

    # Apply three filters to the image
    blurimage = cv2.GaussianBlur(image, (7, 7), 5)
    blurimage1 = cv2.medianBlur(image, 5)
    blurimage2 = cv2.bilateralFilter(image, 9, 75, 75)

    # Define output image paths
    output_path = os.path.join(output_folder, "sample_gaussian.jpg")
    output_path1 = os.path.join(output_folder, "sample_medianblur.jpg")
    output_path2 = os.path.join(output_folder, "sample_bilateralfilter.jpg")
    output_path3 = os.path.join(output_resized_folder, "sample_resized_image.jpg")

    # Save the filtered images
    cv2.imwrite(output_path, blurimage)
    print(f"Filtered image saved at: {output_path}")
    cv2.imwrite(output_path1, blurimage1)
    print(f"Filtered image saved at: {output_path1}")
    cv2.imwrite(output_path2, blurimage2)
    print(f"Filtered image saved at: {output_path2}")
    cv2.imwrite(output_path3, resized_image)
    print(f"Resized image saved at: {output_path3}")

# Wait until user closes display image
cv2.waitKey(0)
cv2.destroyAllWindows()