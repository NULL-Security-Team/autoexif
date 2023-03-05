#!/bin/bash
##############################
##        Auto Exif         ##
##############################
##  Created By Sir Cryptic  ##
############################## 
##  Developer Sir Cryptic   ## 
##############################
##       Greetz Mobly       ##
##       Greetz R!ff        ##
##       Greetz Double A    ##
##       Greetz lucci       ##
##############################
############################## 
##      Developed On        ##
##        BackBox           ##
##############################
while true
do
if [ -f /etc/bash_completion.d/readline ]; then
    . /etc/bash_completion.d/readline
fi

HISTFILE="$HOME/.bash_history"
history -a "$HISTFILE"

# enable arrow key support
if [[ $- == *i* ]]; then
    bind '"\e[A": history-search-backward'
    bind '"\e[B": history-search-forward'
    bind '"\e[C": forward-char'
    bind '"\e[D": backward-char'
fi
history -r
history -a
history -w
clear
#COLOUR
red='\e[1;31m'
yellow='\e[0;33m'
Blue='\e[1;34m'
title="Auto~Exif"
echo -e '\033]2;'$title'\007'

 echo -e "                ▌║█║▌│║▌│║▌║▌█║AutoExif▌│║▌║▌│║║▌█║▌║█"
 echo -e '\e[0;33m┌───────────────────────────────────────────────────────────────────┐
\e[1;31m│Exif Tool AutoMated For Easy Conveinience\e[3;34m Created by "Sir Cryptic"\e[0m\e[1;31m │
\e[0;33m├───────────────────────────────────────────────────────────────────┤
\e[0m\e[1;31m│You Must Install Dependencies For This Script To Work Properly     │\e[3;39m
\e[0;33m└───────────────────────────────────────────────────────────────────┘\e[0m
┌───────────────────────────────────────────────────────────────────┐
│(1) Read Image MetaData (Basic)                                    │
│(2) Read Image MetaData (Expert)                                   │
│(3) Read Image MetaData (From Website)                             │
│(4) Wipe Data From Image (Except JFIF Groups)                      │
│(5) Wipe All GPS Data From Image                                   │
│(6) Wipe All MetaData From Image (Adds Comment Back In)            │
│(7) Extract GPS from AVCH video                                    │
│(8) Extract Info From Thumbnail                                    │
│(9) Wipe Photoshop MetaData                                        │
│(h) Help                                                           │
│(i) Install Dependencies & Script                                  │
│(c) Contact Information                                            │
├───────────────────────────────────────────────────────────────────┤
│                          CTRL + C To Exit                         │
└───────────────────────────────────────────────────────────────────┘
'

echo -e $Blue" ┌─["$red"Auto$Blue]──[$red~$Blue]─["$yellow"Exif$Blue]:"
read -e -p" └─────► " x

option1='1'
option2='2'
option3='3'
option4='4'
option5='5'
option6='6'
option7='7'
option8='8'
option9='9'
info='h'
installdeps='i'
contact='c'
if [ "$x" == "$option1" ]; then                    #readmetadata basic
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘'
read -e -p"└─────► " meta1 >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
'

exiftool $meta1

echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'

read


elif [ "$x" == "$option2" ]; then                          #readmetadatadeep
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘'
read -e -p"└─────► " mdeep >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
'

cat $mdeep | exiftool -

echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'

read

elif [ "$x" == "$option3" ]; then                          #webextract
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: http://a.domain.com/bigfile.jpg           │
├───────────────────────────────────────────────────────────────────┘'
read -e -p"└─────► " pi1host >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
'

curl -s $pi1host | exiftool -fast -

echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'

read

elif [ "$x" == "$option4" ]; then                          #Option4
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘'
read -e -p"└─────► " pi4 >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Wiping JFIF Data!                        │
└───────────────────────────────────────────────────────────────────┘
'
exiftool -all= --jfif:all $pi4

echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                     Data Wiped Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'
read


elif [ "$x" == "$option5" ]; then                          #AVCHextract
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘'
read -e -p"└─────► " pi5 >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Wiping GPS Data!                         │
└───────────────────────────────────────────────────────────────────┘
'

exiftool -gps:all= $pi5

echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                     Data Wiped Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'
read

elif [ "$x" == "$option6" ]; then                          #Option6
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘'
read -e -p"└─────► " pi6 >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Replacing Data!                          │
└───────────────────────────────────────────────────────────────────┘
'

exiftool -all= -comment='Protected By NULLSecurity Team - AutoExif' $pi6
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                     Data Replaced Using AutoExif                  │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'
read

elif [ "$x" == "$option7" ]; then                          #Option7
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Videos/lulz.m2ts           │
├───────────────────────────────────────────────────────────────────┘'
read -p "└─────► " avch >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
'

exiftool -ee -p '$gpslatitude, $gpslongitude, $gpstimestamp' $avch

echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'

read



elif [ "$x" == "$option8" ]; then                          #AVCHExtract
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘'
read -e -p"└─────► " pi8 >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
'

exiftool $pi8 -thumbnailimage -b | exiftool -

echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'

read


elif [ "$x" == "$option9" ]; then                          #Option9
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│        Delete Photoshop meta information from an image            │
├───────────────────────────────────────────────────────────────────┤
│    (note that the Photoshop information also includes IPTC).      │
└───────────────────────────────────────────────────────────────────┘    '
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│          usage example: /home/username/Pictures/lulz.png          │
├───────────────────────────────────────────────────────────────────┘'
read -e -p"└─────► " psd >> ~/.bash_history
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          Extracting Data!                         │
└───────────────────────────────────────────────────────────────────┘
'

exiftool -Photoshop:All= $psd

echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                 Data Extracted Using AutoExif                     │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
└───────────────────────────────────────────────────────────────────┘    
'

read



elif [ "$x" == "$info" ]; then                          #Option10

clear
echo -e '\e[1;33m\e[0m\e[1;31m
┌─────────────────────────────────────────────────────────────────────────────┐
│ You can Put This Script In The Desired Folder You Like Where The Media      │
│ Is Located Then You can execute the script if you have the dependencies     │
│ Already Installed.                                                          │
│ when the script is in the media folder you want you can just type the       │      
│ Image name Along with file type instead of typing the image location aswell │
│ For eg: instead of /home/username/Pictures/lulz.png                         │
│ I would just type : lulz.png                                                │
│ Alternativly i would just install the script and dependcies together        │
│ Allowing me to just type autoexif to open the script in any cli             │
├─────────────────────────────────────────────────────────────────────────────┤
│                  Press ENTER To Go Back To The Main Menu                    │
└─────────────────────────────────────────────────────────────────────────────┘ 
'
read

elif [ "$x" == "$installdeps" ]; then                          #Option10
clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                          ExifTool Installation!                   │
└───────────────────────────────────────────────────────────────────┘'
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│            Are You Sure You Want To Install ExifTool ?            │
├───────────────────────────────────────────────────────────────────┤
│          PRESS ENTER TO START ANY OTHER OPTION TO CANCEL          │
├───────────────────────────────────────────────────────────────────┘'
read -p "└─────► " r
echo -e '\e[0;31m───────────────────────────────────────────────────────────────────\e[0;39m'
$r sudo bash install.sh
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                       Fully Installed ExifTool                    │
├───────────────────────────────────────────────────────────────────┤
│               Press ENTER To Go Back To The Main Menu             │
├───────────────────────────────────────────────────────────────────┘'
read -p "└─────► " r

elif [ "$x" == "$contact" ]; then                 #CONTACTME                    

clear
echo -e '
┌───────────────────────────────────────────────────────────────────┐
│                    \e[0;31msircryptic@protonmail.com\e[1;34m                      │
├───────────────────────────────────────────────────────────────────┤
│             Press ENTER To Go Back To The Main Menu               │
├───────────────────────────────────────────────────────────────────┘'
read -p "└─────► "


else 

error

fi
done

## © 2023 - rjw dly4ever##
