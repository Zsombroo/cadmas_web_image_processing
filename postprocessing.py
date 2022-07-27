import os

import cv2
from tqdm import tqdm


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized


raw_path = 'raw'
output_path = 'negyzetesitett'

bboxes = []
with open('bounding_boxes.txt', 'r') as f:
    for row in f:
        bboxes.append(row.strip().split('/')[-1].split(';'))

bbox_factor = 1.2

for bbox_data in tqdm(bboxes):
    image = cv2.imread(os.path.join(raw_path, bbox_data[0]))
    X = int(float(bbox_data[1]) * image.shape[1])
    Y = int(float(bbox_data[2]) * image.shape[0])
    width = int(min(1, float(bbox_data[4]) * bbox_factor) * image.shape[1])
    height = int(min(1, float(bbox_data[3]) * bbox_factor) * image.shape[0])
    if width > height:
        height = width
    if height > width:
        width = height
    x0 = X - width//2
    x1 = X + width//2
    y0 = Y - height//2
    y1 = Y + height//2
    image = image[max(0,y0):min(y1, image.shape[0]), max(0,x0):min(x1,image.shape[1])]
    w, h, _ = image.shape
    if w > h and h > 1000:
        image = image_resize(image, width=1000, height=None)
    else:
        image = image_resize(image, width=None, height=1000)
    cv2.imwrite(os.path.join(output_path, bbox_data[0]), image)