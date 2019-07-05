# make image files for the NYU Depth Dataset V2

## Description

convert files from mat to image for using the [NYU Depth Dataset V2][nyuv2].

[nyuv2]: https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html

## How to use
* prepare requirements
```bash
pip3 install -r requirements.txt
```
* run
```bash
# custom implimentation : convert from depth map to colorization
python3 make_image_depth_map.py
```
or
```bash
# colorization : fill_depth_colorization-py (reference)
python3 make_image_fill_depth_colorization.py
```

## folder structure
```bash
tree -d
└── data
    ├── depth_gray
    ├── depth_hsv_color
    └── image
```

## reference
 * [NYU Depth Dataset V2](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html)
 * [fill_depth_colorization-py](https://gist.github.com/ialhashim/be6235489a9c43c6d240e8331836586a#file-fill_depth_colorization-py)
 * [blog](https://ddokkddokk.tistory.com/21)
 
## other implimentation
 * [nyuv2-python-toolbox](https://github.com/GabrielMajeri/nyuv2-python-toolbox)