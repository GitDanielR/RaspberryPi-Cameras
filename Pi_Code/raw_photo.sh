test_type = $1
cam_num = $2
num_photos = $3

v4l2-ctl -d /dev/video0 --stream-mmap --stream-to=/home/afdl/Documents/$test_type/camera$cam_num.raw --stream-count=$num_photos