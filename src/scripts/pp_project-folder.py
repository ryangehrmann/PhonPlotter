# =============================================================================
# Add this info manually
# =============================================================================

## Provide a string to name your project
    ## Must contain no spaces, but _ is ok
project_name = 'project_name'

## Provide a file path leading to an excel spreadsheet w/ phonological data
    ## Enter a file path string with r outside the quotations marks
        ## e.g. r'C:\project\my_spreadsheet.xlsx'
    ## The excel file must have a column labeled file (no capitals)
        ## These must correspond to the file names in the audio folder (below)
my_excel = r'C:\project\my_spreadsheet.xlsx'

## Provide a string specifying the name of the tab in your excel database
    ## that holds the relevant data (e.g. 'Sheet1')
my_tab = 'Sheet1'

## Does your audio folder contain sub-folders for different speakers?
    ## If so, please name the sub-folders according to speaker codes
        ## e.g. F1 (female one), F2 (female two), M1 (male one), etc...
    ## Enter string 'yes' or 'no'
multiple_speakers = 'no'

## How many tokens do each of your sound files contain?
    ## Enter an integer number (not a string - no quotation marks)
tokens = 3

## Provide a file path leading to folder that holds audio
    ## Enter a file path string with r outside the quotations marks
        ## e.g. r'C:\project\audio'
my_audio = r'C:\project\audio'



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




import os
mylist = []
for fname in os.listdir(my_audio):
    if os.path.isfile(os.path.join(my_audio,fname)):
        mylist.append((os.path.join(my_audio,fname)))
for file in mylist:
    if file.endswith('.WAV'):
        os.rename(os.path.join(my_audio,file),
                  os.path.join(my_audio,file[:-4]+'.wav'))

mylist = []
for fname in os.listdir(my_audio):
    if os.path.isfile(os.path.join(my_audio,fname)):
        mylist.append((os.path.join(my_audio,fname)))

# =============================================================================
# Functions
# =============================================================================

## Function returns a dictionary of sub-folders in a folder:
    ## {name of sub-folder : file path of sub-folder}
def folders_in(path_to_parent):
    import os
    mylist = []
    for fname in os.listdir(path_to_parent):
        if os.path.isdir(os.path.join(path_to_parent,fname)):
            mylist.append(os.path.join(path_to_parent,fname))
    mydict = {}
    for folder in mylist:
        mydict[folder.split('\\')[-1]] = folder
    return mydict

## Function returns a dictionary of .wav files in a folder:
    ## {.wav file name : file path to .wav file}
        ## Note, the dict keys do not include '.wav'
    ## ALSO will convert .WAV to .wav extensions
def wav_in(path_to_parent):
    import os
    mylist = []
    ## Populate mylist with file paths for audio files in audio folder
    for fname in os.listdir(path_to_parent):
        if os.path.isfile(os.path.join(path_to_parent,fname)):
            mylist.append(os.path.join(path_to_parent,fname))
    ## If '.WAV' was used, convert to '.wav'
    for fname in mylist:
        if fname.endswith('.WAV'):
            os.rename(os.path.join(path_to_parent,fname),
                      os.path.join(path_to_parent,fname[:-4]+'.wav'))
    ## Just keep '.wav' files now
    mylist = [x for x in mylist if x.endswith('.wav')]
    ## Create a dictionary of file name : file path
    mydict = {}
    for file in mylist:
        mydict[file.split('\\')[-1].replace('.wav','')] = file    
    return mydict

## Function to copy and rename a file
def copy_rename(old_file_path, new_file_path):
    import shutil
    shutil.copy(old_file_path, new_file_path)

## function to export excel files
def export_excel(df,file,index=False):
    import pandas as pd
    df_export = pd.ExcelWriter(file,engine='xlsxwriter')
    df.to_excel(df_export,sheet_name='Sheet1',index=index)
    return df_export.save()



# =============================================================================
# Check packages
# =============================================================================

## Function to check if packages are installed and, if not, to install them
    ## from the default Python Package Index (https://pypi.org/simple)
def install(package):
    import subprocess
    import sys
    try:
        __import__(package)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-i", package], check=True)

install('xlsxwriter')

# =============================================================================
# Checking input data
# =============================================================================

import os

## Check project name variable
if ' ' in project_name:
    msg1 = 'There is a space in your project_name variable. ' 
    msg2 = 'Remove the space or replace it with an underscore character _'
    raise ValueError(msg1 + msg2)

## Check Excel location variable is a real .xlsx file on the hd
if not my_excel.endswith('.xlsx'):
    msg = 'Please ensure that my_excel file path leads to a .xlsx file.'
    raise ValueError(msg)
if not os.path.isfile(my_excel):
    msg = 'Invalid file path for my_excel file. Please check and try again'
    raise ValueError(msg) 

## Check audio file location variable is a real folder on the hd
if not os.path.isdir(my_audio):
    msg = 'Invalid file path for my_audio folder. Please check and try again.'
    raise ValueError('Invalid file path for audio folder. Please check and try again') 

## Check that they indicatd 'yes' or 'no' for multiple_speakers
if multiple_speakers not in ['yes','no']:
    msg = 'Please respond "yes" or "no" for variable multiple_speakers.'
    raise ValueError(msg)

## Check that they supplied an integer for tokens
if not isinstance(tokens,int):
    msg = 'Please provide an integer for variable tokens.'
    raise ValueError(msg)

## If they indicated multiple speakers, make sure that there are sub-folders
    ## under my_audio and no .wav files
if multiple_speakers == 'yes':
    if not len(folders_in(my_audio)) > 0:
        msg1 = 'You indicated multiple speakers but my_audio folder does '
        msg2 = 'not contain sub-folders. Your .wav files should be in '
        msg3 = 'sub-folders by speaker.'
        raise ValueError(msg1 + msg2 + msg3)
    if len(wav_in(my_audio)) > 0:
        msg1 = 'You indicated multiple speakers, but my_audio contains .wav '
        msg2 = 'files. Your .wav files should be in sub-folders by speaker.'
        raise ValueError(msg1 + msg2)

## If they indicated one speaker, make sure that there are no sub-folders
    ## under my_audio, just .wav files
elif multiple_speakers == 'no':
    if len(folders_in(my_audio)) > 0:
        msg1 = 'You did not indicate multiple speakers but my_audio folder '
        msg2 = 'contains sub-folders. Your .wav files should not be in '
        msg3 = 'sub-folders, they should be in the main may_audio folder.'
        raise ValueError(msg1 + msg2 + msg3)
    if not len(wav_in(my_audio)) > 0:
        msg1 = 'You did not indicate multiple speakers, but my_audio contains '
        msg2 = 'no .wav files. Your .wav files should be in the main my_audio '
        msg3 = 'folder.'
        raise ValueError(msg1 + msg2 + msg3)





# =============================================================================
# Import excel
# =============================================================================

## function to check if file path leads to valid .xlsx file
def is_xlsx(file_path):
    import os
    if not file_path.endswith('.xlsx'):
        raise ValueError('Please provide a file path to an Excel (.xlsx) file for my_excel')
    elif not os.path.isfile(my_excel):
        raise ValueError('Please provide a valid file path for my_excel')

is_xlsx(my_excel)

## Function to check if a given tab exists in an excel workbook
def is_tab(file_path, sheet_name):
    import openpyxl
    workbook = openpyxl.load_workbook(file_path)
    mylist = []
    for sheet in workbook.worksheets:
        mylist.append(sheet.title)
    if my_tab not in mylist:
        raise ValueError('Please provide a valid tab name for my_tab. The tab name provided does not exist.')

is_tab(my_excel,my_tab)

## function to import dataframe from an excel file
def import_df_file(file,sheet='Sheet1'):
    import pandas as pd    
    return pd.ExcelFile(file).parse(sheet)

df = import_df_file(my_excel,
                    sheet = my_tab)

## Strip '.wav' from df['file']
df['file'] = [str(x).replace('.wav','') for x in df['file']]

## Convert df['file'] to string
df['file'] = df['file'].apply(str)



# =============================================================================
# Create project folder
# =============================================================================

import os

## Create filepath to project folder
folder = os.path.join("C:\\",project_name)
## Create filepath to project audio folder
audio_folder = os.path.join(folder,'audio')

## Create project folder and project audio folder (if it does not yet exist)
if os.path.exists(folder):
    raise ValueError('Project folder '+folder+' already exists. Please delete the old project folder or choose a new project name.')
else:
    os.mkdir(folder)
    os.mkdir(audio_folder)



# =============================================================================
# Create lexical_database and copy wav files to audio folder
# =============================================================================

## Create an empty dataframe with the same columns as the imported df
    ## this df1 will be lexical_database
import pandas as pd
df1 = pd.DataFrame(columns = df.columns)

## if there are multiple speakers...
if multiple_speakers == 'yes':
    ## Get a list of sub-folder names
    sub_folders = folders_in(my_audio)
    ## Loop through the sub_folders
    for sub in sub_folders:
        ## Get file path for this sub
        thisfolder = sub_folders[sub]
        ## Get dictionary of {.wav files : file paths} in thisfolder
        wavs = wav_in(thisfolder)
        ## Loop through wav files in thisfolder
        for wav in wavs:
            ## Raise error if wav not in the Excel file column
            if wav not in [str(x) for x in df['file']]:
                msg = 'File ' + str(wav) + ' in folder ' + str(sub) + \
                    ' not found in Excel database. Please check.'
                raise ValueError(msg)
            ## Otherwise, get infos from Excel and append to new df1 with 
                ## appropriate affixes, then copy the file with new name to
                ## project audio folder
            else:
                ## Get list of token numbers as strings
                toks = list(range(1,tokens+1))
                toks = [str(x) for x in toks]
                ## Loop through toks
                for tok in toks:
                    ## define a new file name with relevant infos
                    wav_new = project_name + '_' + sub + '_' + str(wav)
                    if tokens > 1:
                        wav_new = wav_new + '_' + tok
                    ## subset df to just the row with the file in question
                    thisdf = df.copy(deep=True)[df['file'] == wav].reset_index(drop=True)
                    ## overwrite the file name
                    thisdf.loc[0,'file'] = wav_new
                    ## concat thisdf to df1
                    df1 = pd.concat([df1,thisdf]).reset_index(drop=True)
                    ## define old .wav file path
                    old_file_path = wavs[wav]
                    ## define new .wav file path
                    new_file_path = os.path.join(audio_folder,wav_new+'.wav')
                    ## copy audio file to project audio folder
                    copy_rename(old_file_path, new_file_path)
    ## export df1 to project folder
    export_excel(df1,
                 os.path.join(folder,'lexical_database.xlsx'),
                 index=False)



## if there is just one speaker...
else:
    ## Get dictionary of {.wav files : file paths} in my_audio
    wavs = wav_in(my_audio)
    ## Loop through wav files in my_audio
    for wav in wavs:
        ## Raise error if wav not in the Excel file column
        if wav not in [str(x) for x in df['file']]:
            msg = 'File ' + str(wav) + ' is in audio folder, but is' + \
                ' not found in Excel database. Please check.'
            raise ValueError(msg)
        ## Otherwise, get infos from Excel and append to new df1 with 
            ## appropriate affixes, then copy the file with new name to
            ## project audio folder
        else:
            ## Get list of token numbers as strings
            toks = list(range(1,tokens+1))
            toks = [str(x) for x in toks]
            ## Loop through toks
            for tok in toks:
                ## define a new file name with relevant infos
                wav_new = project_name + '_' + str(wav)
                if tokens > 1:
                    wav_new = wav_new + '_' + tok
                ## subset df to just the row with the file in question
                thisdf = df.copy(deep=True)[df['file'] == wav].reset_index(drop=True)
                ## overwrite the file name
                thisdf.loc[0,'file'] = wav_new
                ## concat thisdf to df1
                df1 = pd.concat([df1,thisdf]).reset_index(drop=True)
                ## define old .wav file path
                old_file_path = wavs[wav]
                ## define new .wav file path
                new_file_path = os.path.join(audio_folder,wav_new+'.wav')
                ## copy audio file to project audio folder
                copy_rename(old_file_path, new_file_path)
    ## export df1 to project folder
    export_excel(df1,
                 os.path.join(folder,'lexical_database.xlsx'),
                 index=False)