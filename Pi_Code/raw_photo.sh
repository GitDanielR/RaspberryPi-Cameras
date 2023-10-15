v4l2-ctl -d /dev/video0 --set-fmt-video=width=1280,height=800,pixelformat="Y10 "
v4l2-ctl -d /dev/video0 --stream-mmap --stream-to=/home/afdl/Documents/Experiment/camera.raw --stream-count=50