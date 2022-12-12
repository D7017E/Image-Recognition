# Image-Recognition

## Content
### NN Prototypes: 

- **Tensorflow classification on our dataset**: A tensorflow CNN that can classify images, and loads a dataset of images.
- **Tensorflow classification**: A tensorflow CNN that can classify images from downloaded datasets. 

### SRC: 
- **Background switch**: Script that switches a background of a image to a new one. Works for a set amount of objects most significantly for humans. 
- **MediaPipe hands**: Script for utilization of media pipe to detect hands. 
- **Pepper test**: Script that can verify that naoqi for Pepper is installed correctly by having Pepper tell a message. 
- **Test result**: Utilized to evaluate models. 

## Tensorflow CNN
We decided not to utilize our own CNN model since our dataset was not large enough. We did utilize a pre-made dataset provided by tensorflow since the hands was not towards the camera at an angle similar to Pepper angle. Another likely issue with tensorflow dataset was the background which was completely white, which was something we attempted to solve by insertion of backgrounds or removal of them. Our tensorflow CNN turned out to not be a viable solution for our time frame even when we attempted to create our own dataset to be used instead. 



