# =============================================================================
# =============================================================================
# # 1 USER INPUTS
# =============================================================================
# =============================================================================

# =============================================================================
# 1.1 User Inputs
# =============================================================================

####################
## Project Folder ##
####################

## Provide the file path to your project folder
project_folder = r"C:\tp_example_pa-then_practice"

###############################
## What do you want to plot? ##
###############################

## Choose to plot vowel quality, pitch or voice quality on the y-axis
    ## Vowel Height:                'F1'
    ## Vowel Backness:              'F2'
    ## Pitch:                       'F0'
    ## Spectral Tilt (H1*-H2*)      'H1H2'
    ## Cepstral Peak Prominence     'CPP'
        ## You must supply one of the above
y_data = 'F0'

#####################################################
## Hertz or Semitones for Frequencies: F0, F1, F2 ##
#####################################################

## THIS ONLY APPLIES IF YOU ARE PLOTTING VOWEL QUALITY OR PITCH (frequncies)
    ## If you chose 'H1H2' or 'CPP', results will be in decibels (dB)

## Choose whether to show frequency measurements in Hertz or Semitones
    ## Hertz:       'hz'
    ## Semitones:   'st'
        ## You must supply one or the other
y_unit = 'st'

############################
## Normalize y-axis data? ##
############################

## Normalizing the y-axis data can be useful in certain circumstances:
    ## e.g. Multiple speakers (normalize by speaker)

## Choose whether to normalize measurements or not
    ## Normalize y-axis data        'yes'
    ## Do nothing to y-axis data    'no'
        ## You must supply one or the other
normalize_y = 'yes'

## Choose whether to normalize by categories in a column or not
    ## Normalize by Category    supply a valid column header as a string
    ## Normalize All Values     ''
        ## You must supply one or the other
normalize_y_by = ''

##############################
## Specify segments to plot ##
##############################

## The open ('op') segment (i.e. the vowel) will be plotted by default
    ## You may include closure voicing 'cl' and coda 'cd' also, if you wish
    ## NOTE: Do not include 'cl' or 'cd' when plotting voice quality or 
        ## vowel quality

## Include closure ('cl') segment in plot?
    ## You must supply 'yes' or 'no'
include_cl = 'no'

## Include coda ('cd') segment in plot?
    ## You must supply 'yes' or 'no'
include_cd = 'no'

###################################
## Normalize x-axis data (time)? ##
###################################

## Here you may choose to normalize time on the x-axis.
    ## Note that the result will be different depending on which segments
    ## you asked for in the previous section

## Choose whether to normalize time or not
    ## Normalize Time           'yes'
    ## Do Nothing to Time       'no'
        ## You must supply one or the other
normalize_x = 'yes'

## The rime will always be plotted between 0 and 1
    ## If you responded 'yes' to include_cd, you may specify at what time you 
    ## want the vowel to end and the coda to begin in normalized time
        ## Supply a number between 0 and 1
        ## Or supply an empty string ''
            ## If you supply an empty string, the script will ignore 'op' and
            ## 'cd' labels and combine them to 'rime', fitting the whole thing
            ## between 0 and 1
cd_time = ''

## The onset will always be plotted in negative time (i.e. before 0)
    ## If you responded 'yes' to include_cl, you may specify at what time you 
    ## want the onset closure to begin in normalized time.
        ## Supply a negative number
        ## Or supply an empty string ''
            ## If you supply an empty string, the script will just assign
            ## -0.3 as the start time for 'cl' in normalized time
cl_time = ''

###############
## Time Zoom ##
###############

## You may want to specify a specific window of time (i.e. zoom in)
    ## Zoom in?                 supply a list [start_time, end_time]
    ## Do nothing?              ''
        ## You must supply one or the other
    ## NOTE: if you normalized time, numbers must reflect re-scaled time
    ## NOTE: if you did not normalize time, numbers reflect milliseconds where
        ## 0 ms = vowel onset
time_zoom = ''

###########
## Color ##
###########

## Do you want to use color to plot categories?
    ## Use color for category:  supply a valid column header as a string
    ## Do not use color:        ''
        ## You must supply one or the other
color_column = 'T'

## Do you want to specify what color to use for each category?
    ## Specify color:           supply a dictionary of {category:colory}
    ## Assign automatically:    ''
        ## You must supply one or the other
    ## NOTE: to use this feature, you must supply a color for every category,
        ## excluding any filtered categories
color_dict = ''

###############
## Line Type ##
###############

## Do you want to use line type to plot categories?
    ## Use line type for category:  supply a valid column header as a string
    ## Do not use line type:        ''
        ## You must supply one or the other
line_column = ''

############
## Facets ##
############

## Note: "facets" are just separate plots within a larger figure

## Do you want to use facets to plot categories?
    ## Use facets for category      provide column header as a string
    ## Do not use facets            ''
facet_column = 'onset'

####################
## General Filter ##
####################

## If there are any other categories that you would like to filter, you can
    ## do that here
        ## E.g. you may want to look at monophthongs only
## Provide a dictionary formatted as follows:
    ## {column:[list,of,items,to,keep], 
    ##  column:['list,of,items,to,keep]}
    ## e.g. you can pass a list of monophthongs in
        ## {'V':['iː','ɨː','uː','eː','əː','oː','ɛː','aː','ɔː']}
    ## NOTE: categories that are filtered out will not be inlcluded when
        ## calculating outliers and y_data normalization
        ## the filtering will happen before that
## Give a dictionary or an empty string ''
filter_dict = ''

## Note that all categorical variable labels will be drawn from your
    ## lexical database column headers and categories. If you want to change
    ## their appearnce, go back to your lexical database and edit the labels
    ## there. Then save the lexical database. update the column names above
    ## and re-run this script.




# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# ==STOP HERE==
# Do not edit anything below until you know what you're doing :-)
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





















































# =============================================================================
# =============================================================================
# # 2 IMPORT / EXPORT
# =============================================================================
# =============================================================================

# =============================================================================
# 2.1 Packages
# =============================================================================

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

## Function to check if packages are installed and, if not, to  install them
    ## from a test repository (https://test.pypi.org/simple/)
    ## that holds the repaired version of scikit-misc for loess regression
        ## See Mar. 4, 2023 comment from has2k1 at 
            ## https://github.com/has2k1/scikit-misc/issues/12
def install_special(package):
    import subprocess
    import sys
    try:
        __import__(package)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-i", "https://test.pypi.org/simple/", package], check=True)    

######################################
## Check and Install When Necessary ##
######################################

install('plotnine')
install('pandas')
install('numpy')
install('math')
install_special('scikit-misc==0.2.0rc1')

############
## Import ##
############

import os
import pandas as pd
import numpy as np
## math and pandas will be imported in formulas below



# =============================================================================
# 2.2 Error Check 1: User Inputs Related to Data Import
# =============================================================================

####################
## project_folder ##
####################

## Is it a string?
if not isinstance(project_folder,str):
    msg = 'project_folder must be a string. Please check.'
    raise ValueError(msg)

## Is it a valid folder?
if not os.path.isdir(project_folder):
    msg1 = 'project_folder must be a valid file path on your hard drive. Please check. '
    msg2 = "Hint: be sure to format the file path as r'FILEPATH'"
    raise ValueError(msg1 + msg2)

###########################
## lexical_database.xlsx ##
###########################

## Define file path to lexical database xlsx file and sheet name
lex = os.path.join(project_folder,'lexical_database.xlsx')
lex_sheet = 'Sheet1'

## Is it a valid file?
if not os.path.isfile(lex):
    msg = 'Your project folder must contain lexical_database.xlsx. Please check.'
    raise ValueError(msg)

##########################
## PraatSauceOutput.txt ##
##########################

## Define file path to  and praatsauceoutput txt file
ps = os.path.join(project_folder,'PraatSauceOutput.txt')

## Is it a valid file?
if not os.path.isfile(ps):
    msg = 'Your project folder must contain PraatSauceOutput.txt. Please check.'
    raise ValueError(msg)



# =============================================================================
# 2.3 Data Import
# =============================================================================

############################
## Function: Import Datas ##
############################

## Function to import lexical database and praatsauce database
    ## Imports lexical_database and praatsauceoutput
    ## Replaces '.wav' in file names in lexdb if needed
    ## Renames 'Filename' in ps data to 'file'
    ## Renames 'f0' to 'F0' in ps data
    ## Renames 'H1H2c' to 'H1H2' in ps data
    ## Merges the two dfs based on shared 'file' category
    ## If 'vo' was used instead of 'ov', it is changed to 'ov'
def tp_import_data(lex,lex_sheet,ps):
    #####################
    ## Functions First ##
    #####################
    ## function to import excel files
    def import_excel(file,sheet='Sheet1'):
        import pandas as pd    
        return pd.ExcelFile(file).parse(sheet)
    ##############################################################
    ## function to import csv files
    def import_csv(file):
        import pandas as pd
        return pd.read_csv(file)
    ##############################################################
    ## function to merge two df's on shared column
    def merge_dfs(df1,df2,col):
        import pandas as pd
        return pd.merge(df1,df2,on=col)
    ##############################################################
    #######################
    ## Let's Get Started ##
    #######################
    ## import lexical database
    dflex = import_excel(lex,lex_sheet)
    ## if .wav is in dflex under 'file', remove it
    dflex['file'] = [str(i).replace('.wav','') for i in dflex['file']]
    ## import praatsauce data
    dfps = import_csv(ps)
    ## rename a few ps columns
    dfps = dfps.rename(columns = {'Filename' : 'file',
                                  'f0':'F0',
                                  'H1H2c':'H1H2'})
    ## merge the two dfs based on shared 'file' column
    df = merge_dfs(dflex,dfps,'file')
    ## If 'vo' was used instead of 'ov' to label onset voicing, fix it
    if 'vo' in df.columns:
        df = df.rename(columns={'vo':'ov'})
    return df

#########################
## Function: Filter df ##
#########################

## Function to filter df for multiple elements under one column
    ## Supply a df, a column, and list holding the desired strings
        ## Returns a df with only those strings under the given column
def filter_df(dataframe, column, filter_list):
    df = dataframe.copy(deep=True)
    df = df.apply(lambda row: row[df[column].isin(filter_list)])
    return df

##################
## Import Datas ##
##################

## Import df
df = tp_import_data(lex, lex_sheet, ps)

############################
## Drop Onsets and Codas? ##
############################

## If we're not interested in 'cl' and 'cd', let's drop them
if all([x == 'no' for x in [include_cd,include_cl]]):
    df = df.copy(deep=True)[df['Label'] == 'op']
## If we're only interested in one or the other, drop as needed
elif include_cl == 'yes' and include_cd == 'no':
    df = filter_df(df, 'Label', ['op','cl'])
elif include_cl == 'no' and include_cd == 'yes':
    df = filter_df(df, 'Label', ['op','cd'])



# =============================================================================
# 2.4 Data Export
# =============================================================================

#################
## Export Data ##
#################

## Define file path to output folder and output file name
export_to = os.path.join(project_folder,'export')
export_file = y_data+'_plot'

## Check to make sure target directory exists and, if not, make it
if not os.path.isdir(export_to):
    os.makedirs(export_to)

## Get full file path to export file
export_path = os.path.join(export_to,export_file+'.png')

## If the export_file already exists
if os.path.isfile(export_path):
    export_file = export_file+'_'
    while export_file+'.png' in os.listdir(export_to):
        export_file = export_file + '_'
    export_path = os.path.join(export_to,export_file+'.png')





# =============================================================================
# =============================================================================
# # 3 FILTERING / SCALING
# =============================================================================
# =============================================================================

# =============================================================================
# 3.1 Error Check 2: User Inputs Related to Filtering Lexical Database
# =============================================================================


## filter_dict must be an empty string or a dictionary
if not isinstance(filter_dict, dict) and filter_dict != '':
    msg = 'Please supply a dictionary or and empty string for filter_dict.'
    raise ValueError(msg)

## filter_dict keys must be strings and valid columns
if isinstance(filter_dict, dict):
    cols = [x for x in filter_dict]
    for col in cols:
        if not isinstance(col, str):
            msg = 'filter_dict keys must be strings. Please check.'
            raise ValueError(msg)
        if col not in df.columns:
            msg = 'filter_dict keys must be valid column headers. Please check.'
            raise ValueError(msg)
## filter_dict values must be lists
        if not isinstance(filter_dict[col],list):
            msg = 'filter_dict values must be lists. Please check.'
            raise ValueError(msg)
## Those lists must contain strings that are valid categories under the column
        cats = [x for x in filter_dict[col]]
        for cat in cats:
            if not isinstance(cat, str) or isinstance(cat, int):
                msg = 'filter_dict values must be lists that contain only strings or integers. Please check.'
                raise ValueError(msg)
            if cat not in list(set(df[col])):
                msg = 'filter_dict values must be lists that contain categories that actually occur in the column indicated in the corresponding filter_dict key. Please check.'
                raise ValueError(msg)                



# =============================================================================
# 3.2 General Filter
# =============================================================================

##################################
## Filter the df, if called for ##
##################################

if isinstance(filter_dict,dict):
    for col in cols:
        df = filter_df(df, col, filter_dict[col])





# =============================================================================
# =============================================================================
# # 4 NORMALIZATION
# =============================================================================
# =============================================================================

# =============================================================================
# 4.1 Error Check 3: User Inputs Related to Y-Axis & X-Axis Values
# =============================================================================

############
## y_data ##
############

## is valide continuous variable?
if y_data not in ['F1','F2','F0','H1H2','CPP']:
    msg = 'y_data must be string "F1", "F2", "F0", "H1H2", or "CPP". Please check.'
    raise ValueError(msg)

############
## y_unit ##
############

## If they did not ask for a frequency measurment (F0, F1, F2)
    ## Make y_unit == 'dB'
if y_data not in ['F0','F1','F2']:
    y_unit = 'dB'

## But if they did ask for frequency, make sure they specified 'hz' or 'st'
else:
    if y_unit not in ['hz','st']:
        msg = 'y_unit must be string "hz" or string "st". Please check.'
        raise ValueError(msg)

#################
## normalize_y ##
#################

## is 'yes' or 'no'?
if normalize_y not in ['yes','no']:
    msg = 'normalize_y must be string "yes" or string "no". Please check.'
    raise ValueError(msg)

####################
## normalize_y_by ##
####################

## is '' or a valid column header?
if normalize_y_by not in df.columns and normalize_y_by != '':
    msg = 'normalize_y_by must be a string and a valid column header. Pleaes check.'
    raise ValueError(msg)

##############################
## Specify segments to plot ##
##############################

## If they asked for vowel quality (F1, F2), set both to 'no'
if y_data in ['F1','F2']:
    include_cl = 'no'
    include_cd = 'no'

## If they asked for pitch or voice quality, make sure both are 'yes' or 'no'
if include_cl not in ['yes','no']:
    msg = 'Please provide string "yes" or "no" for include_cl.'
if include_cd not in ['yes','no']:
    msg = 'Please provide string "yes" or "no" for include_cd.'

#################
## normalize_x ##
#################

## is 'yes' or 'no'
if normalize_x not in ['yes','no']:
    msg = 'normalize_x must be string "yes" or string "no". Please check.'
    raise ValueError(msg)

#############
## cd_time ##
#############

## Function to test whether a variable is a number (i.e. is an int or a float)
def is_number(x):
    if isinstance(x,int) == False and isinstance(x,float) == False:
        return False
    else:
        return True

## If cd_time is relevant...
if normalize_x == 'yes' and include_cd == 'yes':
    ## It must be a number or ''
    if is_number(cd_time) == False and cd_time != '':
        msg = 'cd_time must be a number (integer or float) or an empty string "". Please check.'
        raise ValueError(msg)
    ## If it's a number, it must be between 0 and 1
    if is_number(cd_time) and (cd_time <= 0 or cd_time >= 1):
        msg = 'cd_time must be between 0 and 1. Please check.'
        raise ValueError(msg)

## If cl_time is relevant...
if normalize_x == 'yes' and include_cl == 'yes':
    ## It must be a number or ''
    if is_number(cl_time) == False and cl_time != '':
        msg = 'cl_time must be a number (integer or float) or an empty string "". Please check.'
        raise ValueError(msg)
    ## If it's a number, it must be less than 0
    if is_number(cl_time) and cl_time >= 0:
        msg = 'cl_time must be less than 0 (i.e. a negative number). Please check.'
        raise ValueError(msg)

###############
## time_zoom ##
###############

## is '' or a list
if time_zoom != '' and isinstance(time_zoom, list) == False:
    msg = 'time_zoom must be '' or a list with start and end times. Please check.'
    raise ValueError(msg)

## If they did provide a list for time_zoom...
if isinstance(time_zoom, list):

## just two items in the list?
    if len(time_zoom) != 2:
        msg = 'time_zoom must be a list with 2 items: start and end times. Please check.'
        raise ValueError(msg)

## items in list are floats or integers?
    for time in time_zoom:
        if isinstance(time,int) == False and isinstance(time,float) == False:
            msg = 'time_zoom list must hold numbers only (integers or floats). Please check'
            raise ValueError(msg)

## first item < second item?
    if time_zoom[0] > time_zoom[1]:
        msg = 'The first number in time_zoom list must be less than the second number. Please check.'
        raise ValueError(msg)

## If cl_time is specified, the first item in time_zoom cannot be less than cl_time
    if normalize_x == 'yes' and include_cl == 'yes' and cl_time != '':
        if time_zoom[0] < cl_time:
            msg = 'The first number in time_zoom list cannot be less than cl_time. Please check.'
            raise ValueError(msg)
## If cl_time is not specified, but inclue_cl == 'yes', the first itme in time_zoom cannot be less than -0.3
    elif normalize_x == 'yes' and include_cl == 'yes' and cl_time == '':
        if time_zoom[0] < -0.3:
            msg = 'The first number in time_zoom list cannot be less than -0.3. Please check.'
            raise ValueError(msg)
## If cl_time is not specified and inclue_cl == 'no', the first itme in time_zoom cannot be less than 0
    elif normalize_x == 'yes' and include_cl == 'no':
        if time_zoom[0] < 0:
            msg = 'The first number in time_zoom list cannot be less than 0. Please check.'
            raise ValueError(msg)

## 2nd item in time_zoom cannot be greater than 1.
    if normalize_x == 'yes' and time_zoom[1] > 1:
        msg = 'The second number in time_zoom list must be 1 or less. Please check.'
        raise ValueError(msg)

##################
## color_column ##
##################

## is '' or a valid column header?
if color_column not in df.columns and color_column != '':
    msg = 'color_column must be a string and a valid column header. Pleaes check.'
    raise ValueError(msg)

################
## color_dict ##
################

## is '' or a dictionary?
if color_dict != '' and isinstance(color_dict, dict) == False:
    msg = 'color_dict must be '' or a dictionary. Please check.'
    raise ValueError(msg)

## color_dict keys must be strings and valid categories in color_column
if isinstance(color_dict, dict):
    cats = [x for x in color_dict]
    for cat in cats:
        if not isinstance(cat, str):
            msg = 'color_dict keys must be strings. Please check.'
            raise ValueError(msg)
        if cat not in list(set(df[color_column])):
            msg = 'color_dict keys must be valid categories under the color_column. Please check.'
            raise ValueError(msg)
## color_dict values must be strings
        if not isinstance(color_dict[cat],str):
            msg = 'color_dict values must be strings. Please check.'
            raise ValueError(msg)
## Those value strings must be colors
        colors = ['red','brown','orange','yellow','green','blue','purple','pink','gray','grey','white','black']
        if color_dict[cat] not in colors:
            msg = 'color_dict values must be colors. Please check.'
            raise ValueError(msg)

## color_dict must have all categories specified, none missing
    if set(cats) != set(df[color_column]):
        color_cats = ', '.join(list(set(df[color_column])))
        msg1 = 'color_dict must specify a color for each category in the color column. '
        msg2 = 'Those categories are ' + color_cats + '. '
        msg3 = 'Please check.'
        raise ValueError(msg1 + msg2 + msg3)

#################
## line_column ##
#################

## is '' or a valid column header?
if line_column not in df.columns and line_column != '':
    msg = 'line_column must be a string and a valid column header. Pleaes check.'
    raise ValueError(msg)

##################
## facet_column ##
##################

## is '' or a valid column header?
if facet_column not in df.columns and facet_column != '':
    msg = 'facet_column must be a string and a valid column header. Pleaes check.'
    raise ValueError(msg)

#####################################################################
## blanks in categorical variable columns: color, line type, facet ##
#####################################################################

## We want the users to be aware if there are rows in their category columns
    ## that are left empty. This could be an oversight and mess up results. 
## If the user specified a color, line type or facet column that contains
    ## blank cells, we will throw an error and ask them to mark every cell
    ## in the column.
## If they want to ignore some cells, they should put 'ignore' or something
    ## in those cells in the database and then use the script's filter
    ## function to remove those cells.
## This way, we ensure users' intentionality when it comes to using
    ## categorical variables.

## Dictionary of column categories {string : variable}
    ## we will need the strings to refrence in the error messages
mydict = {'color_column' : color_column,
          'line_column' : line_column,
          'facet_column' : facet_column}

## Loop through mydict
for col in mydict:
    ## Are the columns specified?
    if mydict[col] != '':
        ## Do they columns contain any NaNs?
        if np.nan in df[mydict[col]]:
            msg1 = col + ' contains blank cells in lexical_database.xlsx. '
            msg2 = 'You must provide a category for every cell in ' + col + '.'
            msg3 = 'If there are cells that you wish to ignore in ' + col + ', '
            msg4 = 'Just fill those cells with "ignore" and use the filter '
            msg5 = 'function in this script to remove cells with "ignore" '
            msg6 = 'under ' + col + '.'
            raise ValueError(msg1 + msg2 + msg3 + msg4 + msg5 + msg6)



# =============================================================================
# 4.2 X-Axis Formatting & Time Zoom
# =============================================================================

###############################
## Function: Normalize Time  ##
###############################

## Function overwrites df['t'] with normalized time
    ## provide df, and low and high values for normalization window
def normalize_time(data,low,high):
    ## Get fresh copy of df
    df = data.copy(deep=True)
    ## Save a copy of the original 't' column
    df['t_orig'] = df['t']
    ## Empty list to hold normalized time
    mylist = []
    ## Loop through time values
    for time, start, end in zip(df['t_ms'],df['seg_Start'],df['seg_End']):
        mylist.append((((time - start) / (end - start)) * (high - low)) + low)
    df['t'] = mylist
    return df

###############################################
## Function: Convert 'op' and 'cd' to 'rime' ##
###############################################

## Function to change 'op' and 'cd' labels to 'rime'. Also fixes segment start
    ## and end times, accordingly. Nothing is done to 'cl' rimes.
def convert_to_rime(data):
    ## Fresh df
    df = data.copy(deep=True)
    ## df with 'op' and 'cd' labels
    dfr = df.copy(deep=True)[df['Label'] != 'cl'].reset_index(drop=True)
    ## empty dict to hold rime start and end times
    mydict = {}
    ## loop through files
    for file in list(set(dfr['file'])):
        ## df with this file
        dff = dfr.copy(deep=True)[dfr['file']==file]
        ## Get seg_Start and seg_End for this file
        if 'cd' in list(set(dff['Label'])):
            seg_Start = list(set(dff[dff['Label']=='op']['seg_Start']))[0]
            seg_End = list(set(dff[dff['Label']=='cd']['seg_End']))[0]
        else:
            seg_Start = list(set(dff['seg_Start']))[0]
            seg_End = list(set(dff['seg_End']))[0]
        ## write seg_Start and seg_End to mydict for this file
        mydict[file] = [seg_Start, seg_End]
    ## empty lists
    start_list = []
    end_list = []
    rime_list = []
    ## Loop through dfr
    for i in range(0,len(dfr['file'])):
        file = dfr.loc[i,'file']
        start_list.append(mydict[file][0])
        end_list.append(mydict[file][1])
        rime_list.append('rime')
    ## Overwrite
    dfr['seg_Start'] = start_list
    dfr['seg_End'] = end_list
    dfr['Label'] = rime_list
    ## Get 'cl' rows
    dfc = df.copy(deep=True)[df['Label']=='cl']
    ## Reconstitute df if necessary
    if len(dfc) > 0:
        df = pd.concat(dfr,dfc)
    else:
        df = dfr
    return df

#####################################
## Empty list to hold split-up dfs ##
#####################################

dflist = []

#########################################
## Normalize or Re-Phase Time for 'cl' ##
#########################################

## Get df of 'cl' only, if applicable
    ## Note: 'cl' will still be here if include_cl == 'yes'
if 'cl' in list(set(df['Label'])):
    dfc = filter_df(df,'Label',['cl'])
    
    if normalize_x == 'yes':
        
        if cl_time == '':
            
            dfc = normalize_time(dfc, -0.3, 0)
        
        elif cl_time != '':
            
            dfc = normalize_time(dfc, cl_time, 0)
        
    elif normalize_x == 'no':

        ## Adjust 'cl' to seg_End = 0 ms
            ## Just subtract seg_End from every 't_ms' and * 1000
        mylist = []
        for t_ms, end in zip(dfc['t_ms'],dfc['seg_End']):
            mylist.append((t_ms - end)*1000)
        ## Overwrite old 't' column
        dfc['t'] = mylist
        
    ## Add to dflist
    dflist.append(dfc)
        
#########################################
## Normalize or Re-Phase Time for Rime ##
#########################################

## Get df of rime ('op' and 'cd')
dfr = filter_df(df, 'Label', ['op','cd'])

## Blank lists of words with no 'cd' and words with 'cd'
cd_no = []
cd_yes = []

## Fill blank lists
## Loop through files in dfr
for file in list(set(dfr['file'])):
    ## Get df for this file
    dff = filter_df(dfr,'file',[file])
    ## If there is a 'cd', add file to cd_yes
    if 'cd' in list(set(dff['Label'])):
        cd_yes.append(file)
    ## If there is not a 'cd', add file to cd_no
    else:
        cd_no.append(file)

## Deal with 'op' only files first
if len(cd_no) > 0:
    ## Get df with 'op'-only files
    dfo = filter_df(dfr,'file',cd_no)
    
    if normalize_x == 'yes':
        
        dfo = normalize_time(dfo, 0, 1)

    elif normalize_x == 'no':
        
        ## Adjust 'op' to seg_Start = 0 ms
            ## Just subtract seg_Start from every 't_ms' and * 1000
        mylist = []
        for t_ms, start in zip(dfo['t_ms'],dfo['seg_Start']):
            mylist.append((t_ms - start)*1000)
        ## Overwrite old 't' column
        dfo['t'] = mylist 
    
    ## Add dfo to dflist
    dflist.append(dfo)

## Now, we deal with 'op'+'cd' files
    ## Note: 'cd' will still be here if include_cd == 'yes'
if len(cd_yes) > 0:
    
    ## Get df with 'op'+'cd' files
    dfopcd = filter_df(dfr,'file',cd_yes)
    
    if normalize_x == 'yes':
    
        ## If they did not specify cd_time, then we convert 'op' and 'cd' to 
            ## 'rime' and normalize the whole rime 0 - 1
        if cd_time == '':
            
            dfopcd = convert_to_rime(dfopcd)
            
            dfopcd = normalize_time(dfopcd, 0, 1)
        
        ## If they did specify cd_time, then we keep 'op' and 'cd' separate,
            ## and normalize them separately
        elif cd_time != '':
        
            ## Get separate dfs for 'op' sections and for 'cd' sections
            dfop = filter_df(dfopcd,'Label',['op'])
            dfcd = filter_df(dfopcd,'Label',['cd'])
            
            dfop = normalize_time(dfop, 0, cd_time)
            dfcd = normalize_time(dfcd, cd_time, 1)
            
            dfopcd = pd.concat([dfop, dfcd])
    
    elif normalize_x == 'no':
        
        ## convert 'op' + 'cd' to rime
        dfopcd = convert_to_rime(dfopcd)
        
        ## Adjust 'rime' to seg_Start = 0 ms
            ## Just subtract seg_Start from every 't_ms' and * 1000
        mylist = []
        for t_ms, start in zip(dfopcd['t_ms'],dfopcd['seg_Start']):
            mylist.append((t_ms - start)*1000)
        ## Overwrite old 't' column
        dfopcd['t'] = mylist 
            
    ## Add dfopcd to dflist
    dflist.append(dfopcd)

## Reconstitute df from dflist
df = pd.concat(dflist)    



# =============================================================================
# 4.3 Y-Axis Data: Zeroes and Outliers
# =============================================================================

#############################
## Function: Remove Zeroes ##
#############################

## Function to replace zeroes in a column with NaNs
def remove_zeroes(data, column):
    ## Fresh copy of dataframe
    df = data.copy(deep=True)
    ## Fresh list to hold values
    mylist = []
    ## Loop through values in column
    for value in df[column]:            
        ## Replace zeroes with NaNs
        if value == 0 or value != value:
            mylist.append(np.nan)
        else:
            mylist.append(value)
    ## overwrite column with edited data from mylist
    df[column] = mylist
    ## return df with no zeroes in column
    return df

###############################
## Function: Remove Outliers ##
###############################

## Function to replace outliers in a column with NaNs
def remove_outliers(data, column):
    ## Get fresh copy of dataframe
    df = data.copy(deep=True)
    ## Calculate quantiles and interquartile range
    q_up = df[column].quantile(0.75)
    q_down = df[column].quantile(0.25)
    iqr = q_up - q_down
    ## Calculate whiskers
    whisker_up = q_up + iqr*1.5
    whisker_down = q_down - iqr*1.5
    ## Fresh list to hold values
    mylist = []
    ## Loop through values
    for value in df[column]:
        ## Replace outliers with NaNs
        if value > whisker_up or value < whisker_down:
            mylist.append(np.nan)
        else:
            mylist.append(value)
    ## overwrite column with edited data from mylist
    df[column] = mylist
    ## return df with no outliers in column
    return df

###################
## Remove Zeroes ##
###################

df = remove_zeroes(df, y_data)

#####################
## Remove Outliers ##
#####################

## We will remove outliers relative to the whole y_data column unless they
    ## asked for normalization by a certain category

## If they asked for normalization by category
if normalize_y_by != '':
    ## We'll make a dictionary of dfs keyed by the categories
    mydict = {}
    ## Loop through categories in normalize_y_by column
    for cat in list(set(df[normalize_y_by])):
        ## Make a separate df for each category and add to mydict
        mydict[cat] = df.copy(deep=True)[df[normalize_y_by] == cat]
    ## Loop through categories in mydict
    for cat in mydict:
        ## Get df for this category
        thisdf = mydict[cat]
        ## Remove outliers for this category's df
        thisdf = remove_outliers(thisdf, y_data)
        ## Overwrite df in mydict
        mydict[cat] = thisdf
    ## Get list of dfs in mydict
    mylist = [mydict[x] for x in mydict]
    ## Concatenate list of dfs to reconstitute df
    df = pd.concat(mylist)

## Otherwise, normalize the whole y_data column
else:
    df = remove_outliers(df, y_data)



# =============================================================================
# 4.4 Y-Axis Data: Normalization
# =============================================================================

##############################
## Function: Normalize Data ##
##############################

## Function to normalize variables in a column relative to the mean
    ## Supply a dataframe (data) and a column with the continuous variable
        ## OPTIONAL: If you want semitone conversion, pass in 'yes'
        ## OPTIONAL: supply a column with categories and the normalization
            ## will be calculated within those categories
def normalize(data, column,
              semitones='no',
              cat_column=''):
    ## Fresh copy of dataframe
    df = data.copy(deep=True)
    ## And another copy of the dataframe
    df1 = data.copy(deep=True)
    ## Drop all nans
    def isNaN(num):
        return num!=num
    df1 = df1[isNaN(df1[column])==False]
    ## Deal with categories if applicable
    if cat_column != '':
        ## Loop through categories
        for cat in list(set(df1[cat_column])):
            ## Get a dfcat for this category only
            dfcat = df1.copy(deep=True)[df1[cat_column]==cat]
            ## Get mean value
            y_mean = sum(dfcat[column]) / len(dfcat[column])
            ## Write this cateogry's mean y value to df
            df.loc[df[cat_column]==cat,'y_mean'] = y_mean
    ## But if there are no categories specified...
    else:
        ## Just write the mean for the whole data column to df
        df['y_mean'] = sum(df1[column]) / len(df1[column])
    ## Empty list to hold normalized data
    norm_list = []
    ## Zip and loop through the data
    for mean, value in zip(df['y_mean'],df[column]):
        ## Normalize without semitones
        if semitones=='no':
            norm_list.append(value-mean)
        ## Normalize with semitones
        else:
            import math
            norm_list.append(12*(math.log2(value/mean)))           
    ## Overwrite column with norm_list
    df[column] = norm_list
    return df

###########################
## Normalize Y-Axis Data ##
###########################

## If they asked for normalized y-axis data, we'll do that
    ## If they asked for normalization by category, we'll do that   
    ## If they asked for semitone conversion, we'll do that too

## First, set the semitone condition
if y_unit == 'st':
    semitones = 'yes'
    ## You have to normalize to get semitones, so set that condition too
    normalize_y = 'yes'
else:
    semitones = 'no'

## If they want normalization by category...
if normalize_y == 'yes' and normalize_y_by != '':
    df = normalize(df, y_data, 
                   semitones = semitones, 
                   cat_column = normalize_y_by)
## If they want general normalization
elif normalize_y == 'yes':
    df = normalize(df, y_data,
                   semitones = semitones)

#######################################
## Drop Values Outside of Time Scale ##
#######################################

if time_zoom != '':
    df = df.copy(deep=True)[df['t'] > time_zoom[0]]
    df = df.copy(deep=True)[df['t'] < time_zoom[1]]





# =============================================================================
# =============================================================================
# # 5 PLOTS
# =============================================================================
# =============================================================================

# =============================================================================
# 5.1 Axis labels
# =============================================================================

## Beautify units for the y-axis label
if y_unit == 'hz':
    y_unit = 'Hz'
elif y_unit == 'st':
    y_unit = 'semitones'
else:
    y_unit = 'dB'

## Specify whether y-axis data is normalized
if normalize_y == 'yes':
    norm = ' relative to mean'
else:
    norm = ''

## Create label for y-axis
y_label = y_data + ' (' + y_unit + norm + ')'

## Create label for x-axis
if normalize_x == 'yes':
    x_label = 'Time (normalized)'
else:
    x_label = 'Time (ms)'

# =============================================================================
# 5.2 Generate Plot & Export File
# =============================================================================

#########################
## Function: Line Plot ##
#########################

## Function to produce a line plot and export it to project folder
    ########################    
    ## These Are Required ##    
    ########################
    ## df (dataframe)
    ## x: column containing a continuous variable to plot along x-axis
    ## y: column containing a continuous variable to plot along y-axis
    ## filename: provide a name for the exported plot image file
    ########################
    ## These Are Optional ##
    ########################
    ## method: provide your preferred regression technique
        ## defaults to 'loess', but you may choose from various options listed
        ## in the plotnine documentation for stat_smooth
    ## color: column containing a categorical variable. Will show multiple
        ## regression lines, one per variable (e.g. voicing, tone, etc...)
    ## color_choice: dictionary specifying colors for EVERY variable in the 
        ## column specified for color (e.g. {'voiced':'blue','voiceless':red})
        ## Can only be used if you specified a column for color
    ## linetype: column contaiing a categorical variable. Will show multiple
        ## regression lines, one per variable (e.g. voicing, tone, etc...)
    ## facet = column containing a categorical variable. Will show multiple 
        ## plots, one for each variable in this column
    ## background_tokens = 'yes' if you want to include a smoothed line for 
        ## each individual file in the background behind the regression lines
    ## xscale = list specifying minimum and maximum x axis values. Provide
        ## minimum first (e.g. [xmin, xmax])
    ## yscale = list specifying minimum and maximum y axis values. Provide 
        ## minimum first (e.g. [ymin, ymax])
    ## axis_labels = list specifying labels for x and y axes. Provide x fist.
        ## (e.g. ['Time (ms)','f0 (Hz)'])
    ## title = a string continaing plot title (e.g. 'f0 and Register')
    #########################
    ## These Are Automatic ##
    #########################
    ## If negative numbers are included on x, a vertical line will be drawn
        ## at x=0
def line_plot(df,x,y,filename,
              method='loess',
              color='', 
              color_choice='', 
              linetype='', 
              facet='',
              background_tokens='',
              xscale='',
              yscale ='',
              axis_labels = '',
              title = ''):
    ## Import what we need from plotnine
    from plotnine import ggplot, aes, geom_line, stat_smooth, scale_color_manual,\
    labs, facet_wrap, ggtitle, coord_cartesian, geom_vline, geom_hline, theme_bw
    # ========================================================================
    # method, color & linetype
    # ========================================================================
    ## First we deal with method, color and linetype
        ## All of these are determined within geom_line & stat_smooth
        ## So we need to make appropriate versions of these
    ## neither color nor linetype specified
    if all([i=='' for i in [color,linetype]]):
        geom = geom_line(aes(x=x,y=y,group='file'),stat='smooth',alpha=0.1)
        stat = stat_smooth(aes(x=x,y=y),method=method)
    ## color is specified, not linetype
    elif color!='' and linetype=='':
        geom = geom_line(aes(x=x,y=y,color=color,group='file'),stat='smooth',alpha=0.1)
        stat = stat_smooth(aes(x=x,y=y,color=color),method=method)
    ## linetype is specified, not color
    elif color=='' and linetype!='':
        geom = geom_line(aes(x=x,y=y,linetype=linetype,group='file'),stat='smooth',alpha=0.1)
        stat = stat_smooth(aes(x=x,y=y,linetype=linetype),method=method)
    ## both color and linetype are specified
    elif all([i!='' for i in [color,linetype]]):
        geom = geom_line(aes(x=x,y=y,color=color,linetype=linetype,group='file'),stat='smooth',alpha=0.1)
        stat = stat_smooth(aes(x=x,y=y,color=color,linetype=linetype),method=method)
    # ========================================================================
    # axis scales
    # ========================================================================
    if xscale != '' and yscale != '':
        scales = coord_cartesian(xlim=xscale, ylim=yscale)
    elif xscale != '' and yscale == '':
        scales = coord_cartesian(xlim=xscale)
    elif xscale == '' and yscale != '':
        scales = coord_cartesian(ylim=yscale)
    else:
        scales = ''
    # ========================================================================
    # building the line plot
    # ========================================================================
    ## Start building the plot
    thisplot = ggplot(df) + stat
    if scales != '':
        thisplot = thisplot + scales
    if color_choice != '':
        thisplot = thisplot + scale_color_manual(values=color_choice)
    if facet != '':
        thisplot = thisplot + facet_wrap(facet)
    if background_tokens != '':
        thisplot = thisplot + geom
    if axis_labels != '':
        thisplot = thisplot + labs(x=axis_labels[0],y=axis_labels[1])
    if title != '':
        thisplot = thisplot + ggtitle(title)
    if any(n < 0 for n in df[x]):
        thisplot = thisplot + geom_vline(xintercept = 0)
    if normalize_y == 'yes':
        thisplot = thisplot + geom_hline(yintercept = 0, 
                                         linetype = 'dashed',
                                         color = 'gray')
    # ========================================================================
    # aesthetics
    # ========================================================================
    ## Get rid of gray background
    thisplot = thisplot + theme_bw()
    # ========================================================================
    # exporting the line plot
    # ========================================================================
    ## Get the export_to file path (a global variable)
    global export_to
    ## Export the file
    return thisplot.save(filename=filename,path=export_to)

## Generate plot and export file
myplot = line_plot(df,'t',y_data,export_file,
                   method = 'loess',
                   color = color_column, 
                   color_choice = color_dict, 
                   linetype = line_column, 
                   facet = facet_column,
                   xscale = time_zoom,
                   axis_labels = [x_label,y_label])





# =============================================================================
# =============================================================================
# =============================================================================
# # # Things I Could Add Later
# =============================================================================
# =============================================================================
# =============================================================================

## produce a number of separate plots at the same time by category
## y-axis scaling
## titles
## manual axis labels





# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# # # # OLD STUFF, MAYBE USEFUL LATER
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================

# =============================================================================
# =============================================================================
# # Devoicing
# =============================================================================
# =============================================================================

###############
## Devoicers ##
###############

# ## Would you like to identify and analyze stops in a phonologically 'voiced'
#     ## category that are phonetically devoiced?
#     ## This will look for times when you annotated 'cv' and 'rv' on tier 3
#     ## If you never annotated those, then this will not be applicable
# ## If you ask for this, a new column will be generated called 'devoicing'
#     ## You can use this column as a category above
# ## Give the name of a column and the name of the category in that column
#     ## that represents voiced stops in a dictionary.
#         ## e.g. {'column':'category'}
#     ## otherwise, give an empty string to skip this step
# vd_stops = ''

# ## If they asked for devoicing analysis...
# if vd_stops != '':
#     ## Make sure that they supplied a dictionary
#     if isinstance(vd_stops,dict) == False:
#         raise ValueError("Please supply a dictionary or '' for 'vd_stopss'.")
#     ## And make sure that dictionary has only one item in it
#     elif len(vd_stops) > 1:
#         raise ValueError("Please supply only one key:value item in your 'vd_stops' dictionary.")
#     key = [x for x in vd_stops][0]
#     value = [vd_stops[x] for x in vd_stops][0]
#     ## And make sure it holds column key that is a real column
#     if key not in df.columns:
#         raise ValueError("The column name given for 'vd_stops' is not in the lexical database.")
#     ## And make sure it holds a category value that is a real category
#     elif value not in list(set(df[key])):
#         raise ValueError("The category value given for 'vd_stops' is not in the given column.")
#     ## Raise an error if 'cv' and 'rv' are not columns
#     elif any([i not in df.columns for i in ['cv','rv']]):
#         raise ValueError("'cv' and 'rv' were not annotated. Devoicing analysis is not possible. Please change vd_category to ''.")
#     ## Otherwise, let's find the devoicers...
#     else:
#         ## Empty list to hold devoicing status
#         dev_list = []
#         ## Loop through df
#         for ov, cv, op_start, cat in zip(df['ov'],df['cv'],df['seg_Start'],
#                                          df[key]):
#             ## When you hit the vd_stop category
#             if cat == value:
#                 ## It's devoiced if onset voicing is after op starts
#                 if ov >= op_start:
#                     dev_list.append('devoiced')
#                 ## It's voiced if there is no cv annotated (i.e. it's a nan)
#                 elif cv != cv:
#                     dev_list.append('voiced')
#                 ## It's partially devoiced if cv is annoated (i.e. not a nan)
#                 elif cv == cv:
#                     dev_list.append('partially devoiced')
#             ## Otherwise, it's not a voiced stop at all so we put nan
#             else:
#                 dev_list.append(np.nan)
#         ## Write dev_list to the df in new column 'devoicing'
#         df['devoicing'] = dev_list

# ## Set order for logical presentation of devoicing categories
# if vd_stops != '':
#     df['devoicing'] = df['devoicing'].astype('category')
#     df['devoicing'] = df['devoicing'].cat.reorder_categories(['voiced',
#                                                               'partially devoiced',
#                                                               'devoiced'])