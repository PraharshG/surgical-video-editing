import cv2
import os

def save_frames(input_video_path, output_folder, frame_interval=100):
    # Open the video file
    cap = cv2.VideoCapture(input_video_path)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get the frames per second (fps) and total number of frames
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"Video FPS: {fps}")
    print(f"Total Frames: {total_frames}")

    # Loop through the frames
    for frame_number in range(total_frames):
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Save every 'frame_interval' frame to the output folder
        if frame_number % frame_interval == 0:
            output_path = os.path.join(output_folder, f"frame_{frame_number}.jpg")
            cv2.imwrite(output_path, frame)

    # Release the video capture object
    cap.release()
    print("Frames saved successfully.")

# Example usage:
video_path = "My Videos/202109080914_45_1.mp4"
output_folder = "datasets/test_images/in"
save_frames(video_path, output_folder, frame_interval=100)

