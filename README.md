# convolutionKernel.py

Applies a convolution kernel to an image

## Arguments/usage

### Box blur

`python3 convolutionKernel.py *filename* box-blur *kernel size*`

### Normalized box-blur

`python3 convolutionKernel.py *filename* normalized-box-blur *kernel size*`

### Gaussian blur

`python3 convolutionKernel.py *filename* gaussian-blur *kernel size* *sigma*`

### Custom

`python3 convolutionKernel.py *filename* *kernel entries in right-to-left, top-to-bottom order*`

## Keybinds

**X**: Close window

**S**: Save convoluted image

## Progress

### 32.jpg

* Doesn't seem to be a box-blur; seems to be a Gaussian blur unless there's some weird custom kernel. Closest match I can get by guessing prime numbers is a 17x17 Gaussian-blur kernel with σ = 5 on a 183x191 nearest-neighbor downsize of the original image (apparent dimensions counted on the 32.jpg image by hand), but it's not an exact match.
* Downsizing before applying the kernel is for sure the way to go, because otherwise it gets really messed up.

### 55.jpg

* For sure a convolution kernel meant to get outlines. Can't find an exact match.
* Colors seem to be inverted for some reason, which I don't believe convolution kernels can do on their own. Maybe this is a part of the step if we were to apply this to other forms of data.
* The border is grey; I've seen convolution kernels do this when I was testing with custom ones, but I'm not sure which one is the right one because the colors are inverted as per the previous point. Should make a program to invert the colors (subtract the greyscale and/or individual RGB values from 255) and then use that to help compare.

For sure

## To-do

1. Create a program to score image similarities by just summing the diferences between each pixel in the two images.
2. Create program to turn the scaled-up image of the scaled-down image of the trees on 32.jpg and 55.jpg (i.e. the images are made of pixels that were sized up to be ~5x5 blocks of pixels) into an image that's just the original scaled-down image by identifying the pixels based on the greyscale values being similar to a certain threshold in a square region and then averaging their values to find the most probable pixel color. Basically just clean up the tree image so we can pretty much get what image Cicada created as a result of the convolution kernel they applied. This does not account for JPEG compression.
3. Create a program to deconvolute a given image with a given kernel using linear algebra.
4. Create a program to generate the 8 different possible results of JPEG compressing an image with the given settings (the settings Cicada used are known) by offsetting the image by 0-7 pixels to get different alignments within the JPEG grid of 8x8 pixels.
5. Create a program using the `cv2` module in Python that can upscale or downscale images using nearest-neighbor (and optionally others if we want to test those).
6. Make this program (convolutionKernel.py) output either the image data or a filepath to the image when piping into something else, and taking the same if piped into, so that it can work with the other programs being developed.
7. Create a program to test out various convolution kernels of integers and their normalized counterparts, and then use the JPEG compression program to compare it to the actual images in 32.jpg and 55.jpg. This will require the original downsized image which may just be the original from the Internet downsized via nearest-neighbor (this can be confirmed by the algorithm in to-do item 2) as well as upsizing the image to its size in 32.jpg/55.jpg after applying the kernel but before applying the JPEG compression. This is the final step, and requires all steps before it.

## The big picture

I think that the weird prescence of both a blurred and outlined tree that was seemingly intentionally made to be a much lower resolution than the source image when all other artwork in Liber Primus is much higher resolution very clearly hints at convolution kernels. I also believe that even if the blurred tree is meant to "fit" into the outlined tree, the inner tree wouldn't be blurred— the prescence of both trees makes the convolution kernel connection very strong.

I think some data (either some section of text layed out in a grid or the base60 data already arranged in a grid) potentially either needs to have these convolution kernels applied to them or removed from them via deconvolution as one of the steps.

Even though applying a convolution kernel will probably not get integer results, it doesn't get integer results on images either and they just round to the nearest value, so it should be fine and not a stretch to do so with the non-image data.

Other ideas I have seen and agree we should check (interpreting the Gaussian blur as just a reference to something, and the outline as just fitting the solid tree into it):
* Using the Gaussian distribution as a function on the text data, such as having the x value be the value before this step or doing something else where x is the position of the value in the text. For this kind of method, some σ value has to be used.
* Intepreting a Gaussian blur as referencing Gaussian primes in some way, which are complex numbers which would make things weirder and 2-dimensional
* Overlaying text from the two tree sections on top of each other in alternating rows based on how the tree images should be overlayed
* Somehow combining the text from the two tree sections in some other way, interpreting the images as just meaning the two sections "fit together" somehow
