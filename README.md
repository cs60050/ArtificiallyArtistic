# ArtificiallyArtistic
This is the repository for our machine learning term project on Computer Generated Art. We shall be working on the Artistic Rendering of Images. 

##Group Members

* Ashrujit Ghoshal(14CS10060) <br />
* Sayan Ghosh(14CS10061) <br />
* Arundhati Banerjee(14CS30043) <br />
* Sayan Mandal(14CS30032) <br />
* Mousam Roy(14CS30019) <br />
* Sourav Pal(14CS10062) <br />
* Sohan Patro(14CS30044) <br />
* Projjal Chanda(14CS10057) <br />
* Pradeep Dogga(14CS10013) <br />
* Aniket Suri(14CS10004) <br />

<br />

## Contents of this repository
The folder **_Artistic Rendering of 2D images using CNN_**  contains an implementation of the paper *_A Neural Algorithm of Artistic Style_* by Leon A. Gatys,Alexander S. Ecker,Matthias Bethge.<br />
A folder containing test cases and outputs is included inside it. <br />

The folder **_NaiveImplementation_** is an attempt to implement the paper *_Separating Style and Content_* by Joshua B. Tenenbaum and William T. Freeman. <br />
The necessary training data and test set is included alongwith. <br />

The folder **_Doodles_**  contains an implementation of the paper *_Semantic Style Transfer and Turning Two-Bit Doodles into Fine Artwork_* by Alex J. Champandard <br />
A folder containing test outputs is included inside it. <br />

The folder **_Artistic rendering of videos_** is an attempt to implement the paper *_Artistic style transfer for videos_* by Manuel Ruder, Alexey Dosovitskiy, Thomas Brox <br />
A folder containing a test case  is included inside it. <br />






## Tasks

## Explanation of the approaches
### Naive approach :
Using bilinear model to separate the style and content of image and then applying the style of one image on the content of another image (by the principle of extrapolation).
### Using CNN :
We have used the VGG-19 model to achieve separation of style and content of image
### Neural Doodle
Using a deep neural network to borrow the skills of real artists and turn  two-bit doodles into masterpieces! (based on the Neural Patches algorithm (Li, 2016). )

### Artistic Videos
The algorithm allows to transfer the style from one image (for example, a painting) to a whole video sequence and generates consistent and stable stylized video sequences.

## Running 
###For the naive implementation
python BilinearClassifier.py
### For the CNN method
`python neural_style.py --content <content file> --styles <style file> --output <output file>`

(run `python neural_style.py --help` to see a list of all options)

### For neural doodle
`python3 doodle.py --style <style file> --content <content file> --output <output file> --device=gpu0 --phases=4 --iterations=80`

### For videos
`th artistic_video.lua --style_image<style file> --content_pattern<content frames>`





## Requirements

* TensorFlow
* SciPy
* Pillow
* NumPy
* Pre-trained VGG network (MD5 `8ee3263992981a1d26e73b3ca028a123`)
* Lasagne(for neural doodle)
* lua(for artistic videos)
* torch(for artistic videos)

Due to the huge size of the VGG network,it could not be pushed to github. It can be downloaded here(http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat).

