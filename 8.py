import cv2
import os

# Folder path containing the GIF and JPG files
folder_path = "input_folder1"

# Define the output video path and properties
output_path = "video8.mp4"
fps = 24
output_size = (640, 480)  # Set your desired output video size

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Specify the codec (here, using MP4)
out = cv2.VideoWriter(output_path, fourcc, fps, output_size)

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if the file is a GIF
    if filename.lower().endswith('.gif'):
        # Read the GIF file using OpenCV
        gif = cv2.VideoCapture(file_path)

        # Iterate over the frames of the GIF
        while True:
            ret, frame = gif.read()
            if not ret:
                break

            # Resize the frame to match the output size
            frame = cv2.resize(frame, output_size)

            # Write the frame to the output video
            out.write(frame)

        # Release the GIF file
        gif.release()

    # Check if the file is a JPG
    elif filename.lower().endswith('.jpg'):
        # Read the JPG file using OpenCV
        image = cv2.imread(file_path)

        # Resize the image to match the output size
        image = cv2.resize(image, output_size)

        # Repeat the image frames for the desired duration
        duration = 2 * fps  # Duration of 2 seconds (assuming 24 fps)
        for _ in range(duration):
            out.write(image)

# Release the video writer
out.release()
