# Image-Recognition

Repository to experiment with image-recognition for Pepper. 

## Prerequisites

- Python (versions vary depending on scripts. If no version mention we used Python 3.10) - [Download and install Python](https://www.python.org/downloads/).
- Anaconda - [Installation guide](./docs/anaconda/anaconda_install.md).

## NN Prototypes: 

- **Tensorflow classification on our dataset**: [Tensorflow CNN](./NN_prototypes/tensorflow_image_classification_own_dataset.ipynb) that can classify images, and loads a dataset of images. The dataset is structured into a folder named "own_dataset" and contain multiple subfolders with the names of the labels, filled with images associated with the labels.
- **Tensorflow classification**: [Tensorflow CNN](./NN_prototypes/tensorflow_image_classification.ipynb) that can classify images from downloaded datasets. 

## SRC: 
- **Background switch**: [Script](./src/background_switch/background_example.ipynb) that switches a background of a image to a new one. Works for a set amount of objects most significantly for humans. 
- **MediaPipe hands**: [Script](./src/mediapipe_hands/mediapipehands.py) for utilization of media pipe to detect hands. 
- **Pepper test**: [Bash Script](./src/pepper_test/pepper_talk.sh) that can verify that naoqi for Pepper is installed correctly by having Pepper tell a message. 
- **Test result**: Utilized to evaluate models. 

## Conclusion

### Tensorflow CNN
We decided not to utilize our own CNN model since our dataset was not large enough. We did utilize a pre-made dataset provided by tensorflow since the hands was not towards the camera at an angle similar to Pepper angle. Another issue with tensorflow dataset was the background which was completely white, which was something we attempted to solve by insertion of backgrounds or removal of them. Our tensorflow CNN turned out to not be a viable solution for our time frame even when we attempted to create our own dataset to be used instead. 

### MediaPipe 
Instead of utilizing our CNN models we took the route of utilizing MediaPipe because of our limited datasets. MediaPipe allowed us to train a KNN on the result from MediaPipe. 




