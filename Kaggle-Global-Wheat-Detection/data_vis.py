import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
from PIL import Image
from keras.applications import ResNet50V2, InceptionV3
from keras import Model
from keras import backend as K
from keras.objectives import categorical_crossentropy
import tensorflow as tf
import time
from matplotlib import image

# Global Variables
from keras.layers import Convolution2D, TimeDistributed, Dense, Flatten, BatchNormalization, Activation, Add, \
    AveragePooling2D
from keras.optimizers import Adam

from RoiPoolingConv2DTF import RoiPoolingConv2DTF

KAGGLE_INPUT = "/kaggle/input/"
KAGGLE_WORKING = "/kaggle/working/"

TRAIN_DIR = os.path.join(KAGGLE_INPUT, 'global-wheat-detection/train/')
TEST_DIR = os.path.join(KAGGLE_INPUT, 'global-wheat-detection/test/')
TRAIN_CSV_PATH = os.path.join(KAGGLE_INPUT, 'global-wheat-detection/train.csv')

PRE_PROCESSED_CSV_PATH = os.path.join(KAGGLE_WORKING, "pre_processed_train_first_200.csv")

BBOX_COLUMNS = ["bbox_xmin", "bbox_ymin", "bbox_width", "bbox_height", "bbox_xmax", "bbox_ymax", "bbox_area"]


def delete_working_data():
    import os, re, os.path
    for root, dirs, files in os.walk(KAGGLE_WORKING):
        for file in files:
            os.remove(os.path.join(root, file))


def split_bbox_values_to_different_columns(raw_df: pd.DataFrame) -> pd.DataFrame:
    bbox_df = pd.DataFrame(columns=BBOX_COLUMNS + ["class_name"])
    for bbox_value in raw_df["bbox"].values:
        split_values = bbox_value.replace("[", "").replace("]", "").replace(" ", "").split(",")
        new_row = {
            "bbox_xmin": float(split_values[0]),
            "bbox_ymin": float(split_values[1]),
            "bbox_width": float(split_values[2]),
            "bbox_height": float(split_values[3]),
            "bbox_xmax": float(split_values[0]) + float(split_values[2]),
            "bbox_ymax": float(split_values[1]) + float(split_values[3]),
            "bbox_area": float(split_values[2]) * float(split_values[3])
        }
        class_name = "wheat"
        if new_row["bbox_area"] > 0:
            new_row["class_value"] = 1
            class_name = "wheat"
        else:
            new_row["class_value"] = 0
            class_name = "bg"
        new_row["class_name"] = class_name

        bbox_df = bbox_df.append(new_row, ignore_index=True)
    combo_df = pd.concat([raw_df, bbox_df], axis=1)
    return combo_df


def pre_process_train_csv(raw_df: pd.DataFrame) -> pd.DataFrame:
    raw_df["file_path"] = [os.path.join(TRAIN_DIR, image_id + str(".jpg")) for image_id in raw_df["image_id"].values]
    raw_df = split_bbox_values_to_different_columns(raw_df=raw_df.copy())

    missing_values_count = raw_df.isnull().values.sum()
    print("Missing Values Checking : ", missing_values_count)
    if missing_values_count > 0:
        print(raw_df.isnull().sum())

    raw_df.to_csv(PRE_PROCESSED_CSV_PATH, index=False)
    return raw_df


def read_train_dataset_and_pre_process() -> pd.DataFrame:
    read_df = pd.DataFrame()
    if os.path.isfile(PRE_PROCESSED_CSV_PATH):
        print("Found Pre-Processed-File : ", PRE_PROCESSED_CSV_PATH)
        read_df = pd.read_csv(PRE_PROCESSED_CSV_PATH)
    else:
        read_df = pd.read_csv(TRAIN_CSV_PATH)
        read_df = pre_process_train_csv(raw_df=read_df)

    print(read_df.head())
    print(read_df.describe())
    return read_df


def plot_images_samples(raw_df: pd.DataFrame, title='Image examples', rows=3, cols=3, fig_size=(10, 10),
                        is_bounding_box_to_plot=True):
    fig, axs = plt.subplots(rows, cols, figsize=fig_size)
    for row in range(rows):
        for col in range(cols):
            idx = np.random.randint(len(raw_df), size=1)[0]

            img = Image.open(raw_df.iloc[idx]["file_path"])
            axs[row, col].imshow(img)

            if is_bounding_box_to_plot:
                bboxes = raw_df[raw_df.image_id == raw_df.iloc[idx]["image_id"]][BBOX_COLUMNS]

                for bbox in bboxes.values:
                    rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2],
                                             bbox[3], linewidth=0.8, edgecolor='red', facecolor='none')

                    point_top_left = patches.Circle((bbox[0], bbox[1]), color="white", radius=2)
                    point_bottom_right = patches.Circle((bbox[4], bbox[5]), color="yellow",
                                                        radius=2)
                    axs[row, col].add_patch(rect)
                    axs[row, col].add_patch(point_top_left)
                    axs[row, col].add_patch(point_bottom_right)

            axs[row, col].axis('off')

    plt.suptitle(title)
    plt.show()


def my_model() -> (keras.models.Model, keras.models.Model, keras.models.Model):
    # create the base pre-trained model
    # base_model = InceptionV3(weights=None, include_top=False, input_shape=(1024, 1024, 3))
    base_model = keras.applications.MobileNetV2(weights=None, include_top=False, input_shape=(1024, 1024, 3))
    # base_model = keras.applications.MobileNetV2(weights="imagenet", include_top=False)

    feature_ext_output = base_model.output

    rpn_x = Convolution2D(512, (3, 3), padding='same', activation='relu', kernel_initializer='normal',
                          name='rpn_conv1')(
        feature_ext_output)

    x_class = Convolution2D(NUM_ANCHORS, (1, 1), activation='sigmoid', kernel_initializer='uniform',
                            name='rpn_out_class')(rpn_x)
    x_regr = Convolution2D(NUM_ANCHORS * 4, (1, 1), activation='linear', kernel_initializer='zero',
                           name='rpn_out_regress')(rpn_x)

    rpn = [x_class, x_regr, feature_ext_output]
    # endregion

    # region ROI classifier
    pooling_regions = 14
    input_shape_for_classfier = (NUM_ROIS, 14, 14, 1024)

    out_roi_pool = RoiPoolingConv2DTF(pooling_regions, NUM_ROIS)([feature_ext_output, ROI_INPUT])
    # region conv_block_td
    x = conv_block_td(out_roi_pool, 3, [512, 512, 2048], stage=5, block='a', input_shape=input_shape_for_classfier,
                      strides=(2, 2),
                      trainable=True)
    # endregion

    # region identity_block_td
    x = identity_block_td(x, 3, [512, 512, 2048], stage=5, block='b', trainable=True)
    x = identity_block_td(x, 3, [512, 512, 2048], stage=5, block='c', trainable=True)
    x = TimeDistributed(AveragePooling2D((7, 7)), name='avg_pool')(x)

    # endregion

    out = TimeDistributed(Flatten())(x)

    out_class = TimeDistributed(Dense(CLASSES_COUNT, activation='softmax', kernel_initializer='zero'),
                                name='dense_class_{}'.format(CLASSES_COUNT))(out)
    # note: no regression target for bg class
    out_regr = TimeDistributed(Dense(4 * (CLASSES_COUNT - 1), activation='linear', kernel_initializer='zero'),
                               name='dense_regress_{}'.format(CLASSES_COUNT))(out)

    classifier = [out_class, out_regr]

    # endregion

    model_rpn = Model(inputs=[base_model.input], outputs=rpn[:2])
    model_classifier = Model(inputs=[base_model.input, ROI_INPUT], outputs=classifier)
    model_all = Model(inputs=[base_model.input, ROI_INPUT], outputs=rpn[:2] + classifier)

    return model_rpn, model_classifier, model_all


def conv_block_td(input_tensor, kernel_size, filters, stage, block, input_shape, strides=(2, 2), trainable=True):
    # conv block time distributed

    nb_filter1, nb_filter2, nb_filter3 = filters
    bn_axis = 3

    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'

    x = TimeDistributed(
        Convolution2D(nb_filter1, (1, 1), strides=strides, trainable=trainable, kernel_initializer='normal'),
        input_shape=input_shape, name=conv_name_base + '2a')(input_tensor)
    x = TimeDistributed(BatchNormalization(axis=bn_axis), name=bn_name_base + '2a')(x)
    x = Activation('relu')(x)

    x = TimeDistributed(Convolution2D(nb_filter2, (kernel_size, kernel_size), padding='same', trainable=trainable,
                                      kernel_initializer='normal'), name=conv_name_base + '2b')(x)
    x = TimeDistributed(BatchNormalization(axis=bn_axis), name=bn_name_base + '2b')(x)
    x = Activation('relu')(x)

    x = TimeDistributed(Convolution2D(nb_filter3, (1, 1), kernel_initializer='normal'), name=conv_name_base + '2c',
                        trainable=trainable)(x)
    x = TimeDistributed(BatchNormalization(axis=bn_axis), name=bn_name_base + '2c')(x)

    shortcut = TimeDistributed(
        Convolution2D(nb_filter3, (1, 1), strides=strides, trainable=trainable, kernel_initializer='normal'),
        name=conv_name_base + '1')(input_tensor)
    shortcut = TimeDistributed(BatchNormalization(axis=bn_axis), name=bn_name_base + '1')(shortcut)

    x = Add()([x, shortcut])
    x = Activation('relu')(x)
    return x


def identity_block_td(input_tensor, kernel_size, filters, stage, block, trainable=True):
    # identity block time distributed

    nb_filter1, nb_filter2, nb_filter3 = filters
    bn_axis = 3

    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'

    x = TimeDistributed(Convolution2D(nb_filter1, (1, 1), trainable=trainable, kernel_initializer='normal'),
                        name=conv_name_base + '2a')(input_tensor)
    x = TimeDistributed(BatchNormalization(axis=bn_axis), name=bn_name_base + '2a')(x)
    x = Activation('relu')(x)

    x = TimeDistributed(
        Convolution2D(nb_filter2, (kernel_size, kernel_size), trainable=trainable, kernel_initializer='normal',
                      padding='same'), name=conv_name_base + '2b')(x)
    x = TimeDistributed(BatchNormalization(axis=bn_axis), name=bn_name_base + '2b')(x)
    x = Activation('relu')(x)

    x = TimeDistributed(Convolution2D(nb_filter3, (1, 1), trainable=trainable, kernel_initializer='normal'),
                        name=conv_name_base + '2c')(x)
    x = TimeDistributed(BatchNormalization(axis=bn_axis), name=bn_name_base + '2c')(x)

    x = Add()([x, input_tensor])
    x = Activation('relu')(x)

    return x


def training(raw_df: pd.DataFrame):
    lambda_rpn_regr = 1.0
    lambda_rpn_class = 1.0

    lambda_cls_regr = 1.0
    lambda_cls_class = 1.0

    epsilon = 1e-4

    def rpn_loss_regr(num_anchors):
        def rpn_loss_regr_fixed_num(y_true, y_pred):
            x = y_true[:, :, :, 4 * num_anchors:] - y_pred
            x_abs = K.abs(x)
            x_bool = K.cast(K.less_equal(x_abs, 1.0), tf.float32)

            return lambda_rpn_regr * K.sum(
                y_true[:, :, :, :4 * num_anchors] * (
                        x_bool * (0.5 * x * x) + (1 - x_bool) * (x_abs - 0.5))) / K.sum(
                epsilon + y_true[:, :, :, :4 * num_anchors])

        return rpn_loss_regr_fixed_num

    def rpn_loss_cls(num_anchors):
        def rpn_loss_cls_fixed_num(y_true, y_pred):
            return lambda_rpn_class * K.sum(
                y_true[:, :, :, :num_anchors] * K.binary_crossentropy(y_pred[:, :, :, :],
                                                                      y_true[:, :, :, num_anchors:])) / K.sum(
                epsilon + y_true[:, :, :, :num_anchors])

        return rpn_loss_cls_fixed_num

    def class_loss_regr(num_classes):
        def class_loss_regr_fixed_num(y_true, y_pred):
            x = y_true[:, :, 4 * num_classes:] - y_pred
            x_abs = K.abs(x)
            x_bool = K.cast(K.less_equal(x_abs, 1.0), 'float32')
            return lambda_cls_regr * K.sum(
                y_true[:, :, :4 * num_classes] * (x_bool * (0.5 * x * x) + (1 - x_bool) * (x_abs - 0.5))) / K.sum(
                epsilon + y_true[:, :, :4 * num_classes])

        return class_loss_regr_fixed_num

    def class_loss_cls(y_true, y_pred):
        return lambda_cls_class * K.mean(categorical_crossentropy(y_true[0, :, :], y_pred[0, :, :]))

    # Model making
    model_rpn, model_classifier, model_all = my_model()

    optimizer = Adam(lr=1e-4)
    optimizer_classifier = Adam(lr=1e-4)
    model_rpn.compile(optimizer=optimizer, loss=[rpn_loss_cls(NUM_ANCHORS), rpn_loss_regr(NUM_ANCHORS)])
    model_classifier.compile(optimizer=optimizer_classifier,
                             loss=[class_loss_cls, class_loss_regr(CLASSES_COUNT - 1)],
                             metrics={'dense_class_{}'.format(CLASSES_COUNT): 'accuracy'})
    model_all.compile(optimizer='sgd', loss='mae')

    num_epochs = 2
    epoch_length = 1000
    num_epochs = int(num_epochs)
    iter_num = 0

    losses = np.zeros((epoch_length, 5))
    rpn_accuracy_rpn_monitor = []
    rpn_accuracy_for_epoch = []
    start_time = time.time()

    best_loss = np.Inf

    class_mapping_inv = {v: k for k, v in CLASSES_MAPPING.items()}
    print('Starting training')

    print("Loading Dataset into memory")
    maximum_files = len(raw_df['file_path'].values)

    def generate_arrays_from_data():
        while 1:
            my_index = np.random.randint(low=0, high=maximum_files, size=1)[0]
            file_name = raw_df['file_path'].values[my_index]
            X = np.array(Image.open(file_name))
            X = np.reshape(X, newshape=(1, 1024, 1024, 3))
            Y_class = df[["class_value"]].values[my_index]
            Y_bbox = df[["bbox_xmin", "bbox_ymin", "bbox_xmax", "bbox_ymax"]].values[my_index]
            yield X, [np.array(Y_class), np.array(Y_bbox)]

    history = model_rpn.fit_generator(generator=generate_arrays_from_data(), steps_per_epoch=5, epochs=150,
                                      verbose=1)

    print(history.history.keys())
    # "Loss"
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()


# Void Main
df = read_train_dataset_and_pre_process()

NUM_ROIS = 32
INPUT_SHAPE_IMG = (1024, 1024, 3)
IMG_INPUT_TENSOR = keras.Input(shape=INPUT_SHAPE_IMG)
ROI_INPUT = keras.Input(shape=(NUM_ROIS, 4))
ANCHOR_BOX_SCALES = [128, 256, 512]
ANCHOR_BOX_RATIOS = [[1, 1], [1, 2], [2, 1]]
NUM_ANCHORS = len(ANCHOR_BOX_SCALES) * len(ANCHOR_BOX_RATIOS)

CLASSES_UNIQUE_COUNTS = dict(df["class_name"].value_counts())
CLASSES_LIST = list(df["class_name"].unique())
CLASSES_COUNT = len(CLASSES_LIST)
CLASSES_MAPPING = {}
for i, class_name in enumerate(CLASSES_LIST):
    CLASSES_MAPPING[class_name] = i

# plot_images_samples(raw_df=df, title="Random Images Samples", rows=2, cols=2)
training(df)
