# ArtificiallyArtistic
This is the repository for our machine learning term project on Computer Generated Art. We shall be working on the Artistic Rendering of Images. 

The Group Members Are:

Ashrujit Ghoshal(14CS10060)

Sayan Ghosh(14CS10061)

Arundhati Banerjee(14CS30043)

Sayan Mandal(14CS30032)

Mousam Roy(14CS30019)

Sourav Pal(14CS10062)

Sohan Patro(14CS30044)

Projjal Chanda(14CS10057)

Pradeep Dogga(14CS10013)

Aniket Suri(14CS10004)


The folder Artistic Rendering of 2D images using CNN  contains an implementation of the paper A Neural Algorithm of Artistic Style: By:Leon A. Gatys,Alexander S. Ecker,Matthias Bethge.
A folder containing test cases and outputs is inclued in it.


## Running

`python neural_style.py --content <content file> --styles <style file> --output <output file>`

(run `python neural_style.py --help` to see a list of all options)

## Requirements

* TensorFlow
* SciPy
* Pillow
* NumPy
* Pre-trained VGG network (MD5 `8ee3263992981a1d26e73b3ca028a123`)

Due to the huge size of the VGG network,it could not be pushed to github. It can be downloaded here(http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat).

