# https://stackoverflow.com/questions/7069682/how-to-get-arguments-with-flags-in-bash

message=''
while getopts 'm:' OPTION; 
do
    case "$OPTION" in 
        m)  
            message="${OPTARG}"
            echo "Telling Pepper to say: ${message}"
            python2 ./cmd/pepper_talk.py -m $message
            ;;
    esac
done