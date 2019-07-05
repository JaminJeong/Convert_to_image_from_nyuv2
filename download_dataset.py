import os
import wget

def download_dataset(folder_dir='data', url='http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/nyu_depth_v2_labeled.mat'):
  mat_file = os.path.join(folder_dir, 'nyu_depth_v2_labeled.mat')
  if not os.path.isfile(mat_file):
    print('Beginning file download with wget module')
    wget.download(url, folder_dir)

  return mat_file

def make_result_dir(folder_dir, image_dir, depth_gray, depth_hsv_color):
  if not os.path.isdir(folder_dir):
    os.mkdir(folder_dir)

  if not os.path.isdir(image_dir):
    os.mkdir(image_dir)
  if not os.path.isdir(depth_gray):
    os.mkdir(depth_gray)
  if not os.path.isdir(depth_hsv_color):
    os.mkdir(depth_hsv_color)
