'''
Demo Script
'''

import numpy as np
from skimage import io
from ip_basic import fill_in_multiscale
import matplotlib.pyplot as plt


def get_depth_image(idx):
    depth_img_file = './data/' + ('%s.png' % idx)
    depth = io.imread(depth_img_file).astype(np.float32)
    depth /= 255.0
    depth = depth.astype(np.int32)
    return depth


def demo():
    depth_in = get_depth_image(998)
    depths_out, process_dict = fill_in_multiscale(depth_in)
    plt.matshow(depths_out)
    plt.colorbar()
    plt.savefig('./data/depth_out_998_v2.png', format='png')
    print('done')


if __name__ == '__main__':
    demo()
