import os
import cv2
import numpy as np
import app
from orangecontrib.imageanalytics.image_embedder import ImageEmbedder
import pickle
import keras.backend as k
k.set_image_dim_ordering('th')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def get_result(image_name):
    print(image_name)
    model = pickle.load(open('oil2.pkcls', 'rb'))
    print("model loaded")
    image_file_paths = [image_name]
    print(image_file_paths)
    with ImageEmbedder(model='vgg16', layer='penultimate') as embedder:
        embeddings = embedder(image_file_paths)
    print(embeddings.shape)
    print("embedded")
    pred_ind = model(embeddings)
    pred_cls = [model.domain.class_var.str_val(i) for i in pred_ind]
    print(pred_ind)
    print(pred_cls)
    k.clear_session()
    return pred_cls
