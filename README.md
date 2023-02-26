#Background
Hyoco Impress stores sign screen messages as .yml files and the sign schedule 
routine as .hsc files.  Schedule files use mixed binary and utf16-LE format 
text.  utf16 path strings point to the included .yml message files. Paths 
start with a LE 16-bit word containing the number of bytes in the path and use 
the forward slash (/) as the folder delimiter.  Paths end with a null 
terminating 16-bit word.
Impress stores the absolute path to .yml files.  So, if you change the folder 
or filename in any way, the .hsc schedule will be invalid.  This Python script 
was built to find all the paths in all of the .hsc files' text, lookup the 
current path to each filename in the .hsc, and replace each path with the 
current path. 

Github repository: https://github.com/gumctech127/hyoco_sign

#Installation
Python 3 (Tested with python 3.11.1)
A virtual environment is suggested.

##Package requirements:
numpy==1.24.2
pandas==1.5.3
python-dateutil==2.8.2
pytz==2022.7.1
six==1.16.0

#Usage
Adjust the 'main' area of readhsc.py to pass the path of the .hsc file folder to the Hyoco class.  Then run the script.