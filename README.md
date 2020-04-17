Face Morphing
===================

Create a morphing sequences betwen two faces. 

Input: Two images containing faces  
Output: A video showing the fluid transformation from one face to the other  

Requirements
-------------
```
numpy
scikit_image
opencv_python
Pillow
skimage
dlib
```

Getting Started
-------------

#### Test with demo images

A photo of Jennie from Blackpink       |  A photo of Rihanna
:-------------------------:|:-------------------------:
![](/images/aligned_images/jennie.png)  |  ![](/images/aligned_images/rih.png)


Generate a morphing animation video sequence

```
python3 code/__init__.py --img1 images/aligned_images/jennie.png --img2 images/aligned_images/rih.png --output output.mp4
```

![Morphed Video](results/output.gif)

#### Test with your own images

1. Put your images in `Images` folder

2. Auto align faces with `python code/utils/align_images.py images/ images/aligned_images --output_size=1024`
This will look for faces in the images - crop out, align (center the nose and make the eyes horizontal), and then rescale the resulting images and save them in "aligned_images" folder.
3. Run `code/__init__.py` above on your aligned face images with arg `--img1` and `--img2`.



Key Features
-------------
1. Detect and **auto align faces** in images (Optional for face morphing) 
2. Generate **corresponding features points** between the two images using Dlib's Facial Landmark Detection
3. Calculate the **triangular mesh** with Delaunay Triangulation for each intermediate shape
4. Warp the two input images towards the intermediate shape, perform **cross-dissolve** and obtain intermediate images each frame

More Results
-------------
![Morphed Video](results/final-club-final.gif)

![Morphed Video](results/ld-final.gif)


To Do
-------------
Morph multiple images into a complete sequence  
Morph with body landmarks

Citations
-------------

Adivces on working with facial landmarks with dlib and opencv https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/ 
