# =============================================================================
# =============================================================================
# # 1 USER INPUTS
# =============================================================================
# =============================================================================

####################
## Project Folder ##
####################

## Provide the file path to your project folder
project_folder = r'C:\taoiq_test'

############
## Vowels ##
############

## You must provide the name of the column which holds vowels in your database
    ## You must specify a column here, you cannot provide an empty string
vowel_column = 'V'

########################
## Hertz or Semitones ##
########################

## Choose whether to show F1-F2 measurements in Hertz or Semitones
    ## Hertz:       'hz'
    ## Semitones:   'st'
        ## You must supply one or the other
unit = 'st'

###########################
## Normalize F1-F2 data? ##
###########################

## Normalizing the F1-F2 data can be useful in certain circumstances:
    ## e.g. Multiple speakers (normalize by speaker)

## Choose whether to normalize measurements or not
    ## Normalize y-axis data        'yes'
    ## Do nothing to y-axis data    'no'
        ## You must supply one or the other
normalize = 'yes'

## Choose whether to normalize by categories in a column or not
    ## Normalize by Category    supply a valid column header as a string
    ## Normalize All Values     ''
        ## You must supply one or the other
normalize_by = 'speaker'

###########
## Color ##
###########

## Specify a Color Column holding categorical data
    ## provide column header as a string 
    ## or provide an empty string if you do not want to use colors
color_column = 'V'

## Provide a dictionary of {categories:colors}
    ## or provide an empty string if you do not want to specify colors
color_dict = ''

###########
## Shape ##
###########

## Specify a Shape Column holding categorical data
    ## provide column header as a string
    ## or provide an empty string if you do not want to use dot shapes
shape_column = ''

###################################
## Ellipse (confidence interval) ##
###################################

## Specify a column here (typically same as color_column) to draw elliptical 
    ## confidence intervals for those categories on the scatter plot
    ## or provide an empty string if you do not want ellipses
ellipse_column = 'V'

############
## Facets ##
############

## Note: "facets" are just separate plots within a larger figure

## Specify a Facet Column holding categorical data
    ## provide column header as a string
    ## or provide an empty string if you do not want to use facets
facet_column = 'speaker'

####################
## General Filter ##
####################

## If there are any other categories that you would like to filter, you can
    ## do that here
        ## E.g. you may want to look at monophthongs only, or speaker 1 only
## Provide a dictionary formatted as follows:
    ## {column:[list of items to keep], 
    ##  column:['list of items to keep]}
        ## e.g. {'speaker':['F1','M1']} 
        ## all speakers othern than F1 and M1 will be excluded
## NOTE: categories that are filtered out will not be inlcluded when
    ## calculating outliers and y_data normalization
    ## the filtering will happen before that
## If you do not want to filter, just provide an empty string ''
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


















































# =============================================================================
# =============================================================================
# # 2 PACKAGES
# =============================================================================
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
# =============================================================================
# # 2 ERROR CHECK 1: PROJECT FOLDER
# =============================================================================
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

#################
## Export Data ##
#################

## Define file path to output folder and output file name
export_to = os.path.join(project_folder,'export')
export_file = 'f1f2_scatter_plot'

## Check to make sure target directory exists and, if not, make it
if not os.path.isdir(export_to):
    os.makedirs(export_to)

## Get full file path to export file
export_path = os.path.join(export_to,export_file+'.png')

## If the export_file already exists, append '_' to the end
if os.path.isfile(export_path):
    export_file = export_file+'_'
    while export_file+'.png' in os.listdir(export_to):
        export_file = export_file + '_'
    export_path = os.path.join(export_to,export_file+'.png')


# =============================================================================
# =============================================================================
# # 4 DATA IMPORT & DROP CL, CD
# =============================================================================
# =============================================================================

# =============================================================================
# 2.3 Data Import
# =============================================================================

###########################
## Function: Import Data ##
###########################

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

#################
## Import Data ##
#################

## Import df
df = tp_import_data(lex, lex_sheet, ps)

#################
## Drop cl, cd ##
#################

df = df.copy(deep=True)[df['Label']=='op']



# =============================================================================
# =============================================================================
# # 5 ERROR CHECK 2: USER INPUTS
# =============================================================================
# =============================================================================

# =============================================================================
# 3.1 Error Check 2: User Inputs Related to Filtering Lexical Database
# =============================================================================

##################
## vowel_column ##
##################

## The user must provide a vowel_column. It cannot be an empty string
if vowel_column == '':
    msg = 'Please provide a valid column header for vowel_column. This is required.'
    raise ValueError(msg)

############################################
## Function: Check String / Column Header ##
############################################

## Function raises a value error if col is not a string or col is not a column 
    ## header in the given dataframe
    ## provide a dataframe and a dictionary
    ## the dictionary should hold variable : string version of variable
        ## the strings are used to report errors
def str_col(data,variables):
    for var in variables:
        if var != '':
            if not isinstance(var,str) or var not in data.columns:
                msg = variables[var] + \
                    ' must be a string and a valid column header. Please check.'
                raise ValueError(msg)

#######################################################################
## Categorical Variable Columns: Check String / Column Header Status ##
#######################################################################

## Dictionary holding variables and str versions of them
vardict = {vowel_column : 'vowel_column',
           color_column : 'color_column',
           shape_column : 'shape_column',
           ellipse_column : 'ellipse_column',
           facet_column : 'facet_column',
           normalize_by : 'normalize_by'}

## Check status
str_col(df,vardict)

####################################################
## Categorical Variable Columns: Check for Blanks ##
####################################################

## We want the users to be aware if there are rows in their category columns
    ## that are left empty. This could be an oversight and mess up results. 
## If the user specified a categorical variable column that contains
    ## blank cells, we will throw an error and ask them to mark every cell
    ## in the column.
## If they want to ignore some cells, they should put 'ignore' or something
    ## in those cells in the database and then use the script's filter
    ## function to remove those cells.
## This way, we ensure users' intentionality when it comes to using
    ## categorical variables.

## Loop through vardict (see above)
for var in vardict:
    ## Are the columns specified?
    if var != '':
        ## Do they columns contain any NaNs?
        if np.nan in df[var]:
            col = vardict[var]
            msg1 = col + ' contains blank cells in lexical_database.xlsx. '
            msg2 = 'You must provide a category for every cell in ' + col + '.'
            msg3 = 'If there are cells that you wish to ignore in ' + col + ', '
            msg4 = 'Just fill those cells with "ignore" and use the filter '
            msg5 = 'function in this script to remove cells with "ignore" '
            msg6 = 'under ' + col + '.'
            raise ValueError(msg1 + msg2 + msg3 + msg4 + msg5 + msg6)

##########
## unit ##
##########

## unit must be either 'hz' or 'st' only
if unit not in ['hz','st']:
    msg = 'Please provide a string "hz" or "st" for unit.'
    raise ValueError(msg)

###############
## normalize ##
###############

## normalize must be 'yes' or 'no' only
if normalize not in ['yes','no']:
    msg = 'Please provide a string "yes" or "no" for normalize.'
    raise ValueError(msg)

################
## color_dict ##
################

## is '' or a dictionary?
if color_dict != '' and isinstance(color_dict, dict) == False:
    msg = 'color_dict must be an empty string ("") or a dictionary. Please check.'
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
## filter_dict ##
#################

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
            if not isinstance(cat, str):
                msg = 'filter_dict values must be lists that contain only strings. Please check.'
                raise ValueError(msg)
            if cat not in list(set(df[col])):
                msg = 'filter_dict values must be lists that contain categories that actually occur in the column indicated in the corresponding filter_dict key. Please check.'
                raise ValueError(msg)



# =============================================================================
# =============================================================================
# # 6 APPLY FILTER
# =============================================================================
# =============================================================================

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

##################################
## Filter the df, if called for ##
##################################

if isinstance(filter_dict,dict):
    for col in cols:
        df = filter_df(df, col, filter_dict[col])



# =============================================================================
# =============================================================================
# # 7 REMOVE ZEROES & OUTLIERS, NORMALIZE
# =============================================================================
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

###################
## Remove Zeroes ##
###################

df = remove_zeroes(df, 'F1')
df = remove_zeroes(df, 'F2')

##############################
## Function: Normalize Data ##
##############################

## Function to normalize variables in a column relative to the mean
    ## Supply a dataframe (data) and a column with the continuous variable
        ## OPTIONAL: If you want semitone conversion, pass in 'yes'
        ## OPTIONAL: supply a column with categories and the normalization
            ## will be calculated within those categories
def normalize_data(data, column,
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

####################
## Normalize Data ##
####################

## The data will be normalized if unit == 'st' and/or normalize == 'yes'
    ## In the first case, normalize relative to st
    ## In the second, normalize relative to hz

if unit == 'st' or normalize == 'yes':
    ## New var st_convert will determine if conversion to st happens
    if unit == 'st':
         st_convert = 'yes'
    else:
        st_convert = 'no'
    ## For each formant...
    for formant in ['F1','F2']:
        ## ...normalize as indicated
        df = normalize_data(df,formant,
                            semitones = st_convert,
                            cat_column = normalize_by)

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

#####################
## Remove Outliers ##
#####################

## We will remove outliers relative to the vowel categories held in the
    ## vowel_column

## Dictionary of dfs keyed by the vowel categories
mydict = {}

## Loop through vowel categories in vowel_column
for cat in list(set(df[vowel_column])):
    ## Make a separate df for each vowel category and add to mydict
    mydict[cat] = df.copy(deep=True)[df[vowel_column] == cat]

## Loop through vowel category dfs in mydict
for cat in mydict:
    ## Get df for this category
    thisdf = mydict[cat]
    ## Remove F1 and F2 outliers for this category's df
    thisdf = remove_outliers(thisdf, 'F1')
    thisdf = remove_outliers(thisdf, 'F2')
    ## Overwrite df in mydict
    mydict[cat] = thisdf

## Get list of dfs in mydict
mylist = [mydict[x] for x in mydict]

## Concatenate list of dfs to reconstitute df
df = pd.concat(mylist)



# =============================================================================
# =============================================================================
# # 9 NORMALIZE TIME
# =============================================================================
# =============================================================================

## We'll normalize time just so that we can restrict time to 0.1 > t  < 0.9

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

####################
## Normalize Time ##
####################

df = normalize_time(df,0,1)

##################################
## Middle 80% of vowel duration ##
##################################

df = df.copy(deep=True)[df['t'] < 0.9]
df = df.copy(deep=True)[df['t'] > 0.1]



# =============================================================================
# =============================================================================
# # GET AVERAGE F1-F2 BY FILE
# =============================================================================
# =============================================================================

############################################
## Function: Get Average F1 and F2 Values ##
############################################

## Function returns a dictionary of average F1 and F2 values by file
    ## file : [F1,F2]
def avgF1F2(data):
    ## Fresh copy of df
    df = data.copy(deep=True)
    ## Empty dictionary
    mydict = {}    
    ## Loop through files
    for file in list(set(df['file'])):
        ## Get df for this file
        thisdf = df[df['file'] == file]
        ## Get lists of F1 and F2 values with nans excluded
        thisF1 = [x for x in thisdf['F1'] if x == x]
        thisF2 = [x for x in thisdf['F2'] if x == x]
        ## Get average F1 and F2 values based on those lists
        avgF1 = sum(thisF1) / len(thisF1)
        avgF2 = sum(thisF2) / len(thisF2)
        ## Write averages to mydict for this file
        mydict[file] = [avgF1, avgF2]
    return mydict

## Get dictionary of average F1 and F2 values
avgF1F2_dict = avgF1F2(df)

## New df
dfa = pd.DataFrame(columns=['file','F1','F2'])

## Fill df from dictionary
for file in avgF1F2_dict:
    dfa.loc[len(dfa.index)] = [file,
                               avgF1F2_dict[file][0],
                               avgF1F2_dict[file][1]]

## Fill in categorical columns that we still need for the plot
for col in [vowel_column, color_column, shape_column, facet_column, ellipse_column]:
    if col != '':
        mylist = []
        for file in dfa['file']:
            thislist = [x for x in df[df['file']==file][col]]
            mylist.append(thislist[0])
        dfa[col] = mylist



# =============================================================================
# =============================================================================
# # 11 GENERATE & EXPORT F1-F2 SCATTER PLOT
# =============================================================================
# =============================================================================

## define axis labels
if normalize == 'yes':
    xlab = 'Normalized F2 (' + unit + ')'
    ylab = 'Normalized F1 (' + unit + ')'
elif normalize == 'no':
    xlab = 'F2 (' + unit + ')'
    ylab = 'F1 (' + unit + ')'

# #################################
# ## Function: F1F2 Scatter Plot ##
# #################################

    ## ellipse: if it's the same as color, then you will get color-coded 
        ## ellipses. Otherwise, you will get different line types
def f1f2(df,x,y,filename,
          color='',
          color_choice='',
          shape='',
          ellipse='',
          facet='',
          axis_labels=''):
    
    ## Import
    from plotnine import ggplot, aes, geom_point, stat_ellipse, \
        scale_color_manual, facet_wrap, labs, theme_bw, scale_x_reverse, \
            scale_y_reverse
    
    ## Define aes for geom_point based on color and shape variables
    if color_column != '' and shape_column != '':
        geom = geom_point(aes(x='F2',y='F1',
                              color=color_column,
                              shape=shape_column))
    elif color_column != '' and shape_column == '':
        geom = geom_point(aes(x='F2',y='F1',
                              color=color_column))
    elif color_column == '' and shape_column != '':
        geom = geom_point(aes(x='F2',y='F1',
                              shape=shape_column))
    else:
        geom = geom_point(aes(x='F2',y='F1'))
    
    ## Start building the plot
    thisplot = ggplot(df) + geom
    
    ## If ellipse, add ellipse
    if ellipse != '':
        if ellipse == color_column:
            thisplot = thisplot + stat_ellipse(aes(x='F2',y='F1',color=ellipse))
        else:
            thisplot = thisplot + stat_ellipse(aes(x='F2',y='F1',linetype=ellipse))
    
    ## This and that
    if color_choice != '':
        thisplot = thisplot + scale_color_manual(values=color_choice)
    if facet != '':
        thisplot = thisplot + facet_wrap(facet)
    if axis_labels != '':
        thisplot = thisplot + labs(x=axis_labels[0],y=axis_labels[1])
    
    ## Reverse the scales so...
        ## open vowels are on bottom, close vowels on top
        ## front vowels on on left, back vowels on right
    thisplot = thisplot + scale_x_reverse()+ scale_y_reverse() 
    
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
    return thisplot.save(filename = filename,
                         path = export_to)

f1f2(dfa,'F2','F1',export_file,
     color = color_column,
     color_choice = color_dict,
     shape = shape_column,
     ellipse = ellipse_column,
     facet = facet_column,
     axis_labels = [xlab,ylab])