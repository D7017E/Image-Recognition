import sys, getopt
from naoqi import ALProxy

# https://www.tutorialspoint.com/python/python_command_line_arguments.htm

def main(argv):
    
    message = 'Hello World!'
    try: 
        opts, args = getopt.getopt(argv, "m:")
    except getopt.GetoptError:
        print("pepper_talk.py -m <message>")
        sys.exit(2)
    
    if len(opts) >= 1:
        message = ''
        opt, arg = opts[0] 
        if opt in ("-m", "--message"):
            message += arg
        for arg in args:
            message += arg

    tts = ALProxy("ALTextToSpeech", "130.240.238.32", 9559)
    tts.say(message)

if __name__ == "__main__": 
    main(sys.argv[1:])