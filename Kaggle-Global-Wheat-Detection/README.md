# kaggle-global-wheat-detection
Kaggle Competition - Global Wheat Detection - https://www.kaggle.com/c/global-wheat-detection

# Preparing for Development
1. [Download All](https://www.kaggle.com/c/global-wheat-detection/data) Dataset from competition
2. Extract the data and create the structure as per follows in `C:/kaggle` directory

![directory_structure](https://user-images.githubusercontent.com/25280661/83326123-fd7b6680-a28e-11ea-9723-f7e9f07d49f4.png)

3. Keep the `pre_processed_train.csv` in `C:/kaggle/working/` Directory.


# TO DO List:

### Notebook Setup
- [x] Notebook Setup with Reading Dataset Functions

### Pre Processing
- [x] *Function* = Pre Process.
- [x] *Function* = Split the `bbox` values to individual columns.
- [ ] *Function* = Add images rows to `df` which are not having any bouding boxes but are there in `train` directory. Mark those bouding box values to 0.
- [ ] *Function* = Add `bbox_area` column to `df` by calculating multiplication of `bbox_width` and `bbox_height`.
- [ ] *Function* = Removes those rows from `df` which are having `bbox_area` more than given `area_threshold` value.

### Data Augmentation
- [ ] *Function* = Generate Flipped Horizontal Random Images and store to `KAGGLE_WORKING` directory and also append rows to `df` with the `bbox` values.
- [ ] *Function* = Generate Flipped Vertical Random Images and store to `KAGGLE_WORKING` directory and also append rows to `df` with the `bbox` values.
- [ ] *Function* = Generate some zoomed and cropped into `1024`x`1024` resolution images and store to `KAGGLE_WORKING` directory and also append rows to `df` with the `bbox` values.

### Data Visualisation
- [x] Function = Create generic function to plot random image samples with bounding boxes
 

 ## References
 - [GlobalWheatDetection EDA](https://www.kaggle.com/aleksandradeis/globalwheatdetection-eda)
 - [Augmentations, Data Cleaning and Bounding Boxes](https://www.kaggle.com/reighns/augmentations-data-cleaning-and-bounding-boxes)