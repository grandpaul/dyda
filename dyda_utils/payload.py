# Copyright 2018 DT42
#
# This file is part of BerryNet.
#
# BerryNet is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BerryNet is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BerryNet.  If not, see <http://www.gnu.org/licenses/>.

import base64
import json

from datetime import datetime

import cv2
import numpy as np


def encode_np_array(img):
    retval, jpg_bytes = cv2.imencode('.jpg', img)
    return jpg_bytes


def stringify_jpg(jpg_bytes):
    return base64.b64encode(jpg_bytes).decode('utf-8')


def destringify_jpg(stringified_jpg):
    """
    :return: JPEG bytes
    :rtype: bytes
    """
    return base64.b64decode(stringified_jpg.encode('utf-8'))


def jpg2bgr(jpg_bytes):
    """
    :return: BGR bytes
    :rtype: numpy array
    """
    array = np.frombuffer(jpg_bytes, dtype=np.uint8)
    return cv2.imdecode(array, flags=1)


def jpg2rgb(jpg_bytes):
    """
    :return: RGB bytes
    :rtype: numpy array
    """
    return cv2.cvtColor(jpg2bgr(jpg_bytes), cv2.COLOR_BGR2RGB)


def bgr2rgb(bgr_nparray):
    """Convert image nparray from BGR to RGB.
    Args:
        bgr_nparray: Image nparray in BGR color model.
    Returns:
        Image nparray in RGB color model.
    """
    return cv2.cvtColor(bgr_nparray, cv2.COLOR_BGR2RGB)


def rgb2bgr(rgb_nparray):
    """Convert image nparray from RGB to BGR.
    Args:
        rgb_nparray: Image nparray in RGB color model.
    Returns:
        Image nparray in BGR color model.
    """
    return cv2.cvtColor(rgb_nparray, cv2.COLOR_RGB2BGR)


def serialize_payload(json_object):
    return json.dumps(json_object)


def serialize_jpg(jpg_bytes):
    """Create Serialized JSON object consisting of image bytes and meta
    :param imarray: JPEG bytes
    :type imarray: bytes
    :return: serialized image JSON
    :rtype: string
    """
    obj = {}
    obj['timestamp'] = datetime.now().isoformat()
    obj['bytes'] = stringify_jpg(jpg_bytes)
    return json.dumps(obj)


def deserialize_payload(payload):
    return json.loads(payload)
