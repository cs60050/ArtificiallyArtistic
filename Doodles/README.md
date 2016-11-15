## Contents
This folder contains the code, input and outputs for neural doodle.

## Description of the procedure
It contains an implementation of the paper *_Semantic Style Transfer and Turning Two-Bit Doodles into Fine Artwork_* by Alex J. Champandard

This uses the standard VGG-19 model as used in the earlier instance of artistic rendering of styles from one image to the content of another image.

In addition to the standard system of layers (max-pooling and convolutional) of the VGG , a new concept called as semantic mapping is being used in this case. This is done to prevent seeing incorrect and unpredictable patterns. Generally higher levels in CNN are not exploited by the lower layers in CNN (they are just connected by the back propagation error) which may give rise to such errors.


## Running
`python3 doodle.py --style <style file> --content <content file> --output <output file> --device=gpu0 --phases=4 --iterations=80`

The requirements are mentioned in the main page of this repository.
