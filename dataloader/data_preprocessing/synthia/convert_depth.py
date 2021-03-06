import os
import sys
import numpy as np
import cv2
import PIL.Image as pil

sys.path.append("../../../")
import dataloader.file_io.dir_lister as dl
import dataloader.file_io.get_path as gp

"""
The synthia dataset saves its depth information in 3 identical channels in a 16-Bit image. This format is not compatible
with the transforms from mytransforms and therefore this preprocessing file has to be executed. It will create a new
folder called "Depth_1_channel" which contains the 16-Bit depth images with just one channel.
"""

path_getter = gp.GetPath()
path = path_getter.get_data_path()
data_path = os.path.join(path, 'synthia', 'RAND_CITYSCAPES', 'Depth', 'Depth')
out_path = os.path.join(path, 'synthia', 'RAND_CITYSCAPES', 'Depth_1_channel')
if not os.path.isdir(out_path):
    os.mkdir(out_path)
filelist = dl.DirLister.get_files_by_ending(data_path, '.png')
print("{} files found".format(len(filelist)))
for file in filelist:
    image = cv2.imread(file, -1)
    filename = os.path.split(file)[-1]
    image = image[:, :, 0].reshape(image.shape[0], image.shape[1])
    cv2.imwrite(os.path.join(out_path, filename), image)
