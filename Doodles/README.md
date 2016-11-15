This folder contains the code, input and outputs for neural doodle.

It contains an implementation of the paper *_Semantic Style Transfer and Turning Two-Bit Doodles into Fine Artwork_* by Alex J. Champandard

This uses the standard VGG-19 model as used in the earlier instance of artistic rendering of styles from one image to the content of another image.

## Running
`python3 doodle.py --style <style file> --content <content file> --output <output file> --device=gpu0 --phases=4 --iterations=80`

The requirements are mentioned in the main page of this repository.
