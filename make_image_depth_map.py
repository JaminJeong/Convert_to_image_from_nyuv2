# import skimage.io as io
import numpy as np
import h5py
import cv2
from download_dataset import *

folder_dir = "data"

image_dir = os.path.join(folder_dir, "image")
depth_gray = os.path.join(folder_dir, "depth_gray")
depth_hsv_color = os.path.join(folder_dir, "depth_hsv_color")

make_result_dir(folder_dir, image_dir, depth_gray, depth_hsv_color)
mat_file = download_dataset(folder_dir, 'http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/nyu_depth_v2_labeled.mat')

# read mat file
f = h5py.File(mat_file)

N = len(f['images'])

for index_num in range(N):
    # for n in range(N):
    # read 0-th image. original format is [3 x 640 x 480], uint8
    img = f['images'][index_num]

    # reshape
    img_RGB = np.empty([480, 640, 3])
    img_RGB[:,:,0] = img[0,:,:].T
    img_RGB[:,:,1] = img[1,:,:].T
    img_RGB[:,:,2] = img[2,:,:].T

    # imshow
    img_RGB = img_RGB.astype('float32')
    img_RGB = img_RGB/255.0
    img_RGB = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2BGR)
    img_RGB = img_RGB * 225.0
    img_RGB = img_RGB.astype(np.uint8)

    cv2.imwrite(os.path.join(image_dir, '{:04d}.jpg'.format(index_num)), img_RGB)

    # read corresponding depth (aligned to the image, in-painted) of size [640 x 480], float64
    depth = f['depths'][index_num]

    # reshape for imshow
    depth_HSV = np.empty([480, 640, 3])
    depth_GRAY = np.empty([480, 640, 3])
    # np.max(depth_HSV[:,:,0]) # 3
    # np.min(depth_HSV[:,:,0]) # 1
    depth_GRAY[:,:,0] = depth[:,:].T / 4.0 * 180
    depth_GRAY[:,:,1] = depth[:,:].T / 4.0 * 180
    depth_GRAY[:,:,2] = depth[:,:].T / 4.0 * 180
    cv2.imwrite(os.path.join(depth_gray, '{:04d}.jpg'.format(index_num)), depth_GRAY)

    depth_HSV[:,:,0] = depth[:,:].T / 4.0 * 180
    depth_HSV[:,:,1] = 200
    depth_HSV[:,:,2] = 200
    depth_HSV = cv2.cvtColor(depth_HSV.astype(np.uint8), cv2.COLOR_HSV2BGR)
    cv2.imwrite(os.path.join(depth_hsv_color, '{:04d}.jpg'.format(index_num)), depth_HSV)
