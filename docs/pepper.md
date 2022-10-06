# Set up
## Python 2.7
### Ubuntu
On ubuntu it is not enough to have ubuntu, you also need to install python2.7-dev: \
To install python 2.7 run the command:
>sudo apt install python2.7 

Then to install python2.7-dev run:
> sudo apt install python2.7-dev

## naoqi
### Ubuntu
Download and extract the python SDK from:
> https://developer.softbankrobotics.com/pepper-naoqi-25-downloads-linux

The SDK then needs to be added to the python path, to get the path open the naoqi folder in a terminal and navigate to:
> ~/lib/python2.7/site-packages/

In the terminal run the "path working directory" command:
> pwd

This prints out the path we need to add to python. To do this open the bashrc file and append the export statement, this can for example be:
> export PYTHONPATH=${PYTHONPATH}:/home/anders/Documents/naoqi/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages

To verify that it works, open a new terminal and run:
> python2.7

And import naoqi
> import naoqi

To further verify, you can run:
>from naoqi import ALProxy

>tts = ALProxy("ALTextToSpeech", "130.240.238.32", 9559)

>tts.say("Hello, world!")