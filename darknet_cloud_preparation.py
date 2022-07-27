import os
import shutil

import cv2
from tqdm import tqdm


input_path = 'raw'
tmp_path = 'tmp'
output_path = 'upload'
downloaded_path = 'downloaded'
done_path = 'negyzetesitett'

if not os.path.exists(input_path):
    os.mkdir(input_path)
if not os.path.exists(tmp_path):
    os.mkdir(tmp_path)
if not os.path.exists(output_path):
    os.mkdir(output_path)
if not os.path.exists(downloaded_path):
    os.mkdir(downloaded_path)
if not os.path.exists(done_path):
    os.mkdir(done_path)

image_names = []

for image_name in tqdm(os.listdir(input_path)):
    image = cv2.imread(os.path.join(input_path, image_name))
    if image is None:
        print(f'Can\'t read image:{image_name}')
        continue
    image_names.append(image_name)
    image = cv2.resize(image, (image.shape[1]//10, image.shape[0]//10))
    cv2.imwrite(os.path.join(tmp_path, image_name), image)

with open(os.path.join(output_path, 'images.txt'), 'w', newline='\n') as f:
    for image_name in image_names:
        f.write(f'data/kepek/{image_name}\n')

shutil.make_archive(os.path.join(output_path, 'darknet_kepek'), 'zip', tmp_path)