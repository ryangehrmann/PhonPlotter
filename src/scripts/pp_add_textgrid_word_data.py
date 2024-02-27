# =============================================================================
# Add this info manually
# =============================================================================

## NOTE: You must have the following three columns in your lexical_database
    ## for this to work:
        ## (1) 'file' (no capital letters)
            ## holds file names (with or without .wav extensions)
        ## (2) 'word'
            ## holds your transcribed word for this file
        ## (3) 'gloss'
            ## holds your gloss for this word
## NOTE: 'file' is necessary. 'word' and 'gloss' can be blank, but the columns
    ## must exist in the datbase or you will get an error

## Provide the filepath leading to your lexical_database.xlsx file
    ## Use the format r'filepath'
lexical_database = r"C:\taoiq_test\lexical_database.xlsx"

## Provide the filepath leading to the folder containing you textgrids
    ## Use the format r'filepath'
audio_folder = r"C:\taoiq_test\audio"

## After you run the script:
    ## A new folder named 'textgrids_unedited' will be added at the top level
        ## of your project folder, just in case
    ## Your original textgrids will be replaced with new ones that have
        ## word and gloss data in Tier 1. This data will be extracted from
        ## your lexical_database.

# Now you can run the script



# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# ==STOP HERE==
# Do not edit anything below unless you know what you're doing :-)
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================

#                          uuuuuuuuuuuuuuuuuuuu
#                        u" uuuuuuuuuuuuuuuuuu "u
#                      u" u$$$$$$$$$$$$$$$$$$$$u "u
#                    u" u$$$$$$$$$$$$$$$$$$$$$$$$u "u
#                  u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
#                u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
#              u" u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$u "u
#              $ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
#              $ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
#              $ $$$" ... "$...  ...$" ... "$$$  ... "$$$ $
#              $ $$$u `"$$$$$$$  $$$  $$$$$  $$  $$$  $$$ $
#              $ $$$$$$uu "$$$$  $$$  $$$$$  $$  """ u$$$ $
#              $ $$$""$$$  $$$$  $$$u "$$$" u$$  $$$$$$$$ $
#              $ $$$$....,$$$$$..$$$$$....,$$$$..$$$$$$$$ $
#              $ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $
#              "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
#                "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
#                  "u "$$$$$$$$$$$$$$$$$$$$$$$$$$$$" u"
#                    "u "$$$$$$$$$$$$$$$$$$$$$$$$" u"
#                      "u "$$$$$$$$$$$$$$$$$$$$" u"
#                        "u """""""""""""""""" u"
#                          """"""""""""""""""""

























##################################################
## Functions for Checking / Installing Packages ##
##################################################

## Function to check if packages are installed and, if not, to install them
    ## from the default Python Package Index (https://pypi.org/simple)
def install(package):
    import subprocess
    import sys
    try:
        __import__(package)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-i", package], check=True)

######################################
## Check and Install When Necessary ##
######################################

install('codecs')
install('pandas')






# =============================================================================
# Functions
# =============================================================================

## function to import excel files
def import_excel(file,sheet='Sheet1'):
    import pandas as pd    
    return pd.ExcelFile(file).parse(sheet)

## function to get list of files in a directory
def get_files(directory):
    import os
    return os.listdir(directory)

## function to copy a list of files from one directory to another
    ## file_list must be a list of file names w/ extensions
    ## source_dir and tar_dir must be in the r'filepath' format
    ## source_dir must already exist
    ## if tar_dir does not exist, it will be created
def file_copy(file_list,source_dir,tar_dir):
    import os
    import shutil
    counter = 0
    if not os.path.isdir(tar_dir):
        os.makedirs(tar_dir)
    for i in file_list:
        shutil.copy(os.path.join(source_dir,i),tar_dir)
        counter = counter +1
    return print(str(counter)+' files successfully copied!')

## Function returns a dictionary of files with a given file extension in a given directory:
    ## {file name : file path}
        ## Note, the dict keys do not include the file extension
    ## Provide
        ## ext = file extension as a string '.xlsx'
        ## folder = file path to directory as a string
def type_in(ext,folder):
    import os
    mylist = []
    for fname in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,fname)):
            mylist.append(os.path.join(folder,fname))
    mylist = [x for x in mylist if x.endswith(ext)]
    mydict = {}
    for file in mylist:
        mydict[file.split('\\')[-1].replace(ext,'')] = file    
    return mydict



# =============================================================================
# Errors
# =============================================================================

import os

## Check to make sure lexical db exists
if not lexical_database.endswith('.xlsx'):
    msg = 'Please ensure that lexical_database file path leads to a .xlsx file.'
    raise ValueError(msg)
if not os.path.isfile(lexical_database):
    msg = 'Invalid file path for lexical_database file. Please check and try again'
    raise ValueError(msg) 

## Check to make sure audio folder exists
if not os.path.isdir(audio_folder):
    msg = 'Invalid file path for my_audio folder. Please check and try again.'
    raise ValueError('Invalid file path for audio folder. Please check and try again') 

## Check to make sure lex db has 'word' and 'gloss' columns
df = import_excel(lexical_database,
                  sheet='Sheet1')
cols = [i for i in df.columns]
if not all(x in cols for x in ['word','gloss']):
    msg = 'Your lexical_database must contain both a "word" and a "gloss" column.'
    raise ValueError(msg)

## Check to make sure audio folder contains TextGrid files
if len(type_in('.TextGrid',audio_folder)) == 0:
    msg = 'The audio_folder provided contains no .TextGrid files. Please check.'
    raise ValueError(msg)



# =============================================================================
# Main Script
# =============================================================================

## Open lexical database as df
df = import_excel(lexical_database,
                  sheet='Sheet1')
## Zip up a dictionary from file name and word+gloss
    ## Remove .wav from file also
worddict = dict(zip(df['file'].replace('.wav',''),
                    '/'+df['word']+"/ "+df['gloss']))

## Get list of files
files = get_files(audio_folder)
## Just the textgrids
files = [i for i in files if '.TextGrid' in i]

## Define filepath leading to textgrids_unedited folder
import os
textgrids_unedited = os.path.join(audio_folder.replace('\\audio',''),'textgrids_unedited')
## If the folder exists, append _ to the folder name
if os.path.exists(textgrids_unedited):
    textgrids_unedited = textgrids_unedited + '_'
## Create the textgrids_unedited folder
os.makedirs(textgrids_unedited)

## Copy textgrid files to textgrids_unedited, just in case
file_copy(files,audio_folder,textgrids_unedited)

## change directory to audio_folder
os.chdir(audio_folder)
## Loop through the tg files
import codecs
for file in files:
    ## open the file
    tg = codecs.open(file,'r','utf-8')
    ## get the lines from the tg as a list
    lines = tg.readlines()
    ## close the file
    tg.close()
    ## get word data from worddict based on file name (no .TextGrid)
    word_data = worddict[file.replace('.TextGrid','')]
    ## put the word data into line 17 of the list if line 17 exists and it
        ## contains the correct text
    if len(lines) >= 17:
        if 'text = ""' in lines[17]:
            lines[17] = lines[17].replace('text = ""',
                                          'text = "'+word_data+'"')
    ## convert the lines list to a string
    lines = "".join(lines)
    ## open the file again, in write mode this time
    tg = codecs.open(file,'w','utf-8')
    ## overwrite the file with updated info
    tg.write(lines)
    ## close the file
    tg.close()