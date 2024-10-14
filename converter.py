import os
import subprocess

folder = r"input-your-own-folder-here"
output_file = "output.mp4"
frame_rate = 30

command = [
    "ffmpeg",
    "-framerate", str(frame_rate),
    "-i", os.path.join(folder, "frame_%04d.png"),
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    output_file
]

subprocess.run(command)
