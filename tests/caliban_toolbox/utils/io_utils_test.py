# Copyright 2016-2019 The Van Valen Lab at the California Institute of
# Technology (Caltech), with support from the Paul Allen Family Foundation,
# Google, & National Institutes of Health (NIH) under Grant U24CA224309-01.
# All rights reserved.
#
# Licensed under a modified Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.github.com/vanvalenlab/deepcell-toolbox/LICENSE
#
# The Work provided may be used for non-commercial academic purposes only.
# For any other use of the Work, including commercial use, please contact:
# vanvalenlab@gmail.com
#
# Neither the name of Caltech nor the names of its contributors may be used
# to endorse or promote products derived from this software without specific
# prior written permission.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for io_utils"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import shutil

import numpy as np
# from tensorflow.python.keras.preprocessing.image import array_to_img
# from tensorflow.python.platform import test
from skimage.external import tifffile as tiff

from caliban_toolbox.utils import io_utils


# def _write_image(filepath, img_w=30, img_h=30):
#     bias = np.random.rand(img_w, img_h, 1) * 64
#     variance = np.random.rand(img_w, img_h, 1) * (255 - 64)
#     imarray = np.random.rand(img_w, img_h, 1) * variance + bias
#     if filepath.lower().endswith('tif') or filepath.lower().endswith('tiff'):
#         tiff.imsave(filepath, imarray[:, :, 0])
#     else:
#         img = array_to_img(imarray, scale=False, data_format='channels_last')
#         img.save(filepath)
#

# class TestIOUtils(test.TestCase):
#
#     def test_get_image(self):
#         temp_dir = self.get_temp_dir()
#         # test tiff files
#         test_img_path = os.path.join(temp_dir, 'phase.tif')
#         _write_image(test_img_path, 300, 300)
#         test_img = io_utils.get_image(test_img_path)
#         self.assertEqual(np.asarray(test_img).shape, (300, 300))
#         # test png files
#         test_img_path = os.path.join(temp_dir, 'feature_0.png')
#         _write_image(test_img_path, 400, 400)
#         test_img = io_utils.get_image(test_img_path)
#         self.assertEqual(np.asarray(test_img).shape, (400, 400))
#
#     def test_nikon_getfiles(self):
#         temp_dir = self.get_temp_dir()
#         for filename in ('channel.tif', 'multi1.tif', 'multi2.tif'):
#             _write_image(os.path.join(temp_dir, filename), 300, 300)
#
#         images = io_utils.nikon_getfiles(temp_dir, 'channel')
#         self.assertListEqual(images, ['channel.tif'])
#         multi_images = io_utils.nikon_getfiles(temp_dir, 'multi')
#         self.assertListEqual(multi_images, ['multi1.tif', 'multi2.tif'])
#         no_images = io_utils.nikon_getfiles(temp_dir, 'bad_channel_name')
#         self.assertListEqual(no_images, [])
#
#
# if __name__ == '__main__':
#     test.main()
