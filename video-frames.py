import os
import cv2

# Path to the video file
vid_path = "..."

# Extract video name without extension
video_name = os.path.splitext(os.path.basename(vid_path))[0]
print(f"Video name: {video_name}")

# Create the output directory if it doesn't exist
outdir = os.path.join("...", video_name)
if not os.path.exists(outdir):
    os.makedirs(outdir)
    print(f"Created directory: {outdir}")
else:
    print(f"Directory already exists: {outdir}")

# Open the video file
vid_cap = cv2.VideoCapture(vid_path)
if not vid_cap.isOpened():
    print(f"Failed to open video file: {vid_path}")
    exit(1)

# Get the frames per second (fps) of the video
fps = vid_cap.get(cv2.CAP_PROP_FPS)
print(f"Frames per second: {fps}")

interval = 10000  # Interval in milliseconds to capture frames

frame_count = 0
while vid_cap.isOpened():
    # Set the position of the video to the next frame
    vid_cap.set(cv2.CAP_PROP_POS_MSEC, frame_count * interval)
    success, image = vid_cap.read()
    if success:
        # Create the filename for the image
        filename = os.path.join(outdir, f"{video_name}_{frame_count}.png")
        # Write image to the outdir
        cv2.imwrite(filename, image)
        print(f"Saved frame {frame_count} at {frame_count * interval} ms to {filename}")
    else:
        print(f"No more frames to read at {frame_count * interval} ms")
        # Break the loop if there are no more frames to read
        break

    frame_count += 1

# Release the video capture object
vid_cap.release()
print("Video processing completed.")
