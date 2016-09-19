# ArtificiallyArtistic
This is the repository for our machine learning term project on Computer Generated Art. We shall be working on the Artistic Rendering of Images. 

##Group Members :

Ashrujit Ghoshal(14CS10060) <br />
Sayan Ghosh(14CS10061) <br />
Arundhati Banerjee(14CS30043) <br />
Sayan Mandal(14CS30032) <br />
Mousam Roy(14CS30019) <br />
Sourav Pal(14CS10062) <br />
Sohan Patro(14CS30044) <br />
Projjal Chanda(14CS10057) <br />
Pradeep Dogga(14CS10013) <br />
Aniket Suri(14CS10004) <br />

<br />

## Contents of this repository :
The folder **_Artistic Rendering of 2D images using CNN_**  contains an implementation of the paper *_A Neural Algorithm of Artistic Style_* by Leon A. Gatys,Alexander S. Ecker,Matthias Bethge.<br />
A folder containing test cases and outputs is inclued inside it.


## Tasks :

## Explanation of the approaches :

### Using CNN :


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

