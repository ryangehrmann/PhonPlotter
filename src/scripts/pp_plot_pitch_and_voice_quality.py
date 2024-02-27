# =============================================================================
# =============================================================================
# # User Inputs
# =============================================================================
# =============================================================================

####################
## Input / Output ##
####################

## Add filepath leading to your lexical_database.xlsx file
lex = r"C:\mewari_test\lexical_database.xlsx"
## Add name of sheet in workbook that holds the lexical data
    ## Default is 'Sheet1'
lex_sheet = 'Sheet1'

## Add filepath leading to your PraatSauceOutput.txt file
ps = r"C:\mewari_test\PraatSauceOutput.txt"

## Add filepath leading to your desired 'export' folder (in project folder)
    ## The plot will be stored here
    ## If the folder does not already exist, it will be created
export_to = r"C:\mewari_test\export\pitch"

## Add name for this particular plot (will be placed in export_folder)
    ## Do not include a file extension
    ## If this file name already exists in the folder, an underscore _
        ## will be added to avoid overwriting any plots
export_file = 'this_plot'




##############################
## Include Closure Voicing? ##
##############################

## You annotated closure 'cl' in Praat
## Do you want the plot to include pitch / voice quality measures during 
    ## closure voicing?
## Give 'yes' or 'no'
include_cl = 'no'



###################################
## Continuous Variable on Y-Axis ##
###################################

## Chose a column of continuous data to plot on the y-axis
    ## choose from the following and type in the string between '':
        ## Pitch: 'F0'
        ## Spectral Tilt: 'H1H2'
        ## Cepstral Peak Prominence: 'CPP'
y_data = 'F0'

## Choose a regression technique for the y-axis data
    ## 'loess' is the default
    ## 'lowess' is similar to loess but lacks confidence intervals
    ## 'lm' is linear regression model (straight lines)
regression = 'lowess'



##################################
## Continous Variable on X-Axis ##
##################################

## This script is designed to use time as the x-axis variable



############################
## Normalize y-axis data? ##
############################

## Normalizing the y-axis data can be useful in certain circumstances:
    ## e.g. Multiple speakers (normalize by speaker)

## Would you like to normalize your y-axis data?
## Give 'yes' or 'no'
normalize_y = 'yes'

## If you are looking at pitch, you can normalize to semitones if you like
    ## DO NOT convert to semitones for voice qualty analysis - only pitch
## Give 'yes' or 'no'
semitone_y = 'yes'

## Would you like to normalize the entire pool of data points in y_data column
    ## or woud you like to normalize by a category (e.g. speaker, tone, etc..)
## If you want to normalize by cageogry, give the name of a column holding
    ## categorical variables in your lexical_databse as a string inside ''
## If you want to normalzie all data points without cageories, simply leave an
    ## empty string ''
normalize_y_by = ''



############################
## Normalize x-axis data? ##
############################

## If you want to normalize time, the following will be done:
    ## 'rime' duration ('op' and 'cd' segments combined) will be converted to
        ## fit between time = 0 (beinning of 'op') and time = 1 (end of 'cd')
    ## 'cl' duration will be converted to fit between time = -0.3 (beginning 
        ## of 'cl') and time = 0 (end of 'cl')
            ## NOTE: 'cl' will only appear if you answered 'yes' to 
                ## include_cl above
## Give 'yes' or 'no'
normalize_x = 'yes'



#################################
## Categorical Variable: Color ##
#################################

## Add name of column in lexical_database.xlsx that holds categories you would
    ## like to display with different colored lines in the plot
## Give string with column header or an empty string ''
color_data = 'voicing'

## If you would like to filter the categories in this column, you can do that
    ## here. Just add a list of the categories that you want to include.
    ## Reminder: lists are strings inside [] 
        ## Example: ['string_1', string_2','string_3']
    ## Note: the categories will be presented in the order that you list them
## Give a list of categories or an empty string '' if you do not want to filter
color_filter = ''

## Colors will be automatically selected for your categories
## If you would like to specify what color each category should be, you can 
    ## do that here. Just add a dictionary of categories and colors.
    ## Note: this dictionary must include EVERY category in the color_data
        ## column (after the filter is applied, if you are using that)
        ## If you leave a category out, you will get an error
    ## Reminder: your dictionaries should be sets of two strings inside {}
        ## Example: {'voiced':'blue','voiceless','red'}
## Give a dictionary or an empty string ''
color_dict = ''



#####################################
## Categorical Variable: Line Type ##
#####################################

## Add name of column in lexical_database.xlsx that holds categories you would
    ## like to display with different line types in the plot
## Give string with column header or an empty string ''
line_data = ''

## If you would like to filter the categories in this column, you can do that
    ## here. Just add a list of the categories that you want to include.
    ## Reminder: lists are strings inside [] 
        ## Example: ['string_1', string_2','string_3']
    ## Note: the categories will be presented in the order that you list them
## Give a list of categories or an empty string '' if you do not want to filter
line_filter = ''



######################################
## Categorical Variable: Facet Wrap ##
######################################

## Add name of column in lexical_database.xlsx that holds categories you would
    ## like to display in separate sub-plots (called facets)
        ## Give string with column name or 'none'
facet_data = ''

## If you would like to filter the categories in this column, you can do that
    ## here. Just add a list of the categories that you want to include.
    ## Reminder: lists are strings inside [] 
        ## Example: ['string_1', string_2','string_3']
    ## Note: the facets will be presented in the order that you list them here
    ## Give a list of categories or 'none'
facet_filter = ''

## Note that all categorical variable labels will be drawn from your
    ## lexical database column headers and categories. If you want to change
    ## their appearnce, go back to your lexical database and edit the labels
    ## there. Then save the lexical database. update the column names above
    ## and re-run this script.



###########################
## Miscellaneous Filters ##
###########################

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
# # Check and Import Modules
# =============================================================================
# =============================================================================

## Function to import a package or, if it's not installed, install it
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        import pip
        pip.main(['install', package]) 

## Make sure plotnine and pandas are installed
import_or_install('os')
import_or_install('plotnine')
import_or_install('pandas')
import_or_install('numpy')
import_or_install('math')

## Import
import os
import pandas as pd
import numpy as np
import math
from plotnine import *





# =============================================================================
# =============================================================================
# # Data Import
# =============================================================================
# =============================================================================


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

## Import df
df = tp_import_data(lex, lex_sheet, ps)




# =============================================================================
# =============================================================================
# # Data Export
# =============================================================================
# =============================================================================

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
# # Miscellaneous Filtering
# =============================================================================
# =============================================================================

## Function to filter df for multiple elements under one column
    ## Supply a df, a column, and list holding the desired strings
        ## Returns a df with only those strings under the given column
def df_col_filter(dataframe, column, filter_list):
    df = dataframe.copy(deep=True)
    df = df.apply(lambda row: row[df[column].isin(filter_list)])
    return df

## Check to make sure that filter_dict is either {} or ''
if filter_dict != '' and isinstance(filter_dict,dict)==False:
    raise ValueError('Please supply '' or a dictionary for "filter_dict".')
## Check to make sure that the columns passed into filter_dict are valid
if isinstance(filter_dict,dict)==True:
    for col in filter_dict:
        if col not in df.columns:
            raise ValueError('A column name in "filter_dict" is invalid.')
        ## If they are, filter the df accordingly
        else:
            df = df_col_filter(df, col, filter_dict[col])



# =============================================================================
# =============================================================================
# # Include Closure Voicing?
# =============================================================================
# =============================================================================

## Drop 'cl' if they don't want to include it
if include_cl == 'no':
    df = df.copy(deep=True)[df['Label']!='cl']
## If they want to keep it...
elif include_cl == 'yes':
    ## We will drop any rows in 'cl' that occur before 'ov'
    ## Empty list to hold droppable rows
    drop_list = []
    ## Loop through the df
    for label, ov, time in zip(df['Label'],df['ov'],df['t_ms']):
        ## any row that is in 'cl' but occurs before ov time
        if label == 'cl' and time < ov:
            ## add drop to drop_list
            drop_list.append('drop')
        ## otherwise
        else:
            ## add keep to drop_list
            drop_list.append('keep')
    ## add drop_list to df
    df['drop'] = drop_list
    ## filter by drop_list
    df = df[df['drop']=='keep']
## Raise an error if anything other than 'yes' or 'no' for include_cl
else:
    raise ValueError("Please provide 'yes' or 'no' for include_cl.")



# =============================================================================
# =============================================================================
# # Continuous Variable on Y-Axis, Zeroes & Outliers
# =============================================================================
# =============================================================================

## Function to replace zeroes and outliers with NaNs for a variable in a column
    ## Supply a dataframe (data) and a column with the continous variable
        ## OPTIONAL: supply a column with categories and the outliers will
            ## be calculated within those categories
def zeroes_outliers(data,data_column,
                    cat_column=''):
    ## Get [whisker_up,whisker_down] for a data_column in a dataframe "data"
    def whiskers(data,data_column):
        ## Calculate quantiles and interquartile range
        q_up = data[data_column].quantile(0.75)
        q_down = data[data_column].quantile(0.25)
        iqr = q_up - q_down
        ## Calculate whiskers
        whisker_up = q_up + iqr*1.5
        whisker_down = q_down - iqr*1.5
        return [whisker_up,whisker_down]
    ## Fresh copy of dataframe
    dfz = data.copy(deep=True)
    ## Deal with categories if applicable
    if cat_column != '' and cat_column in dfz.columns:
        ## Get list of categories from cat_column
        cats = list(set(dfz[cat_column]))
        ## Loop through categories
        for cat in cats:
            ## Get a dfcat for this category only
            dfcat = dfz.copy(deep=True)[dfz[cat_column]==cat]
            ## Write this cateogry's whiskers to dfz using the embedded
                ## whiskers() function
            dfz.loc[dfz[cat_column]==cat,'whisker_up'] = whiskers(dfcat,data_column)[0]
            dfz.loc[dfz[cat_column]==cat,'whisker_down'] = whiskers(dfcat,data_column)[1]
    ## But if there are no categories specified...
    else:
        ## Write whiskers for the whole data_column
        dfz['whisker_up'] = whiskers(dfz,data_column)[0]
        dfz['whisker_down'] = whiskers(dfz,data_column)[1]
    ## Empty list to hold data free of zeroes and outliers
    fixed_list = []
    ## Zip and loop through data
    for up, down, value in zip(dfz['whisker_up'],dfz['whisker_down'],
                               dfz[data_column]):
        ## If value is too high, too low, equal to 0 or NaN
        if value > up or \
            value < down or \
                value == 0 or \
                    value != value:
                        ## Write a NaN to to fixed_list
                        fixed_list.append(np.nan)
        else:
            ## Otherwise, write value to fixed_list
            fixed_list.append(value)
    ## Overwrite data_column with the fixed data list
    dfz[data_column] = fixed_list
    return dfz

## Check that a valid column name was passed into y_data
if y_data not in ['F0','H1H2','CPP']:
    raise ValueError("Please provlide 'F0, 'H1H2' or 'CPP' for y_data.")

## For removing zeroes and outliers, we need to know about normalization
    ## If they are asking for normalization by category, we should remove
        ## Zeroes and Outliers by category too
    ## Otherwise, just remove them based on the entire column

## First, let's raise errors if anything's wrong with the normalization 
    ## variables

## Raise error if normalize_y is not 'yes' or 'no'
if normalize_y not in ['yes','no']:
    raise ValueError("Please provide 'yes' or 'no' for normalize_y.")
## Raise error if semitone_y is not 'yes' or 'no'
if semitone_y not in ['yes','no']:
    raise ValueError("Please provide 'yes' or 'no' for semitone_y.")
## Raise error if normalize_y_by is not '' or a valid column
if normalize_y_by not in df.columns and normalize_y_by != '':
    raise ValueError("Please provlide a valid column or '' for normalize_y_by.")

## If normalize_y == 'no', then normalize_y_by should == ''
if normalize_y == 'no':
    normalize_y_by = ''

## Now, let's remove zeroes and outliers    
## If normalize_y_by is unspecified...
if normalize_y_by == '':
    ## Remove zeroes and outliers for the whole column
    df = zeroes_outliers(df, y_data)
## But if normalize_y_by is specified 
elif normalize_y_by != '':
    ## Remove zeroes and outliers by category
    df = zeroes_outliers(df, y_data, 
                         cat_column = normalize_y_by)



# =============================================================================
# =============================================================================
# # Normalized Y-Axis Data?
# =============================================================================
# =============================================================================

## Function to normalize variables in a column relative to the mean
    ## Supply a dataframe (data) and a column with the continuous variable
        ## OPTIONAL: If you want semitone conversion, pass in 'yes'
        ## OPTIONAL: supply a column with categories and the normalization
            ## will be calculated within those categories
def normalize(data,data_column,
              semitones='no',
              cat_column=''):
    ## Fresh copy of dataframe
    dfz = data.copy(deep=True)
    ## A copy of the dataframe that will be edited to remove NaNs
    dfedit = data.copy(deep=True)
    ## Drop all nans
    def isNaN(num):
        return num!=num
    dfedit = dfedit[isNaN(dfedit[data_column])==False]
    ## Drop all zeroes
    dfedit = dfedit[dfedit[data_column]!=0]
    ## Deal with categories if applicable
    if cat_column != '' and cat_column in dfedit.columns:
        ## Get list of categories from cat_column
        cats = list(set(dfedit[cat_column]))
        ## Loop through categories
        for cat in cats:
            ## Get a dfcat for this category only
            dfcat = dfedit.copy(deep=True)[dfedit[cat_column]==cat]
            ## Get mean value
            y_mean = sum(dfcat[data_column]) / len(dfcat[data_column])
            ## Write this cateogry's mean y value to dfz
            dfz.loc[dfz[cat_column]==cat,'y_mean'] = y_mean
    ## But if there are no categories specified...
    else:
        ## Just write the mean for the whole data column to dfz
        dfz['y_mean'] = sum(dfedit[data_column]) / len(dfedit[data_column])
    ## Empty list to hold normalized data
    norm_list = []
    ## Zip and loop through the data
    for mean, value in zip(dfz['y_mean'],dfz[data_column]):
        ## Normalize without semitones
        if semitones=='no':
            norm_list.append(value-mean)
        ## Normalize with semitones
        else:
            import math
            norm_list.append(12*(math.log2(value/mean)))           
    ## Overwrite data_column with norm_list
    dfz[data_column] = norm_list
    return dfz

## If normalize_y is 'no'
if normalize_y == 'no':
    ## Do nothing
    pass
## But if they do want to normalize...
elif normalize_y == 'yes':
    ## Change semitone_y to 'no' unless y_data is F0
    if y_data != 'F0':
        semitone_y = 'no'
    ## If normalize_y_by is unspecified:
    if normalize_y_by == '':
        ## Normalize the entire column (semitones if asked for)
        df = normalize(df, y_data, semitones = semitone_y)
    ## But if normalize_y_by is specified
    elif normalize_y_by != '':
        ## Normalize within categories (semitones if asked for)
        df = normalize(df, y_data, semitones = semitone_y,
                       cat_column = normalize_y_by)



# =============================================================================
# =============================================================================
# # Normalized X-Axis Data (time)?
# =============================================================================
# =============================================================================

## Function to combine 'op' and 'cd' labels to new 'rime'
    ## Updates seg_Start and seg_End appropriately
def combine_rime(dataframe):
    ## Fresh copy of df
    df = dataframe.copy(deep=True)
    ## And another copy for editing
    dfedit = dataframe.copy(deep=True)
    ## We only need one row per file for this, just keep t=1
    dfedit = dfedit[dfedit['t']==1]
    ## Start with just 'op'
    dfop = dfedit[dfedit['Label']=='op']
    ## Empty dict to hold start and end times for op segments
    optimedict = {}
    ## Add to optimedict file:[start,end]
    for file, start, end in zip(dfop['file'],dfop['seg_Start'],
                                dfop['seg_End']):
        optimedict[file] = [start,end]
    ## Now let's take just 'cd'
    dfcd = dfedit[dfedit['Label']=='cd']
    ## Empty dict to hold start and end times to cd segments
    cdtimedict = {}
    ## Add to cdtime dict file:[start,end]
    for file, start, end in zip(dfcd['file'],dfcd['seg_Start'],
                                dfcd['seg_End']):
        cdtimedict[file] = [start, end]
    ## Empty dict to hold start and end times for the whole rime
    rimetimedict = {}
    ## Loop through optimedict
    for file in optimedict:
        ## If this file has a coda (i.e. appears in cdtimedict)...
        if file in cdtimedict:
            ## Write start from optimedict and end from cdtimedict in rimetimedict
            rimetimedict[file] = [optimedict[file][0],
                                  cdtimedict[file][1]]
        ## If there is no coda...
        else:
            ## Write start and end from optimedict in rimetimedict
            rimetimedict[file] = optimedict[file]
    ## Returning to df, overwrite 'op' and 'cd' with 'rime'
    df.loc[df['Label']!='cl','Label'] = 'rime'
    ## Loop through rimetimedict
    for file in rimetimedict:
        ## Write new seg_Start and seg_End times for rime
        df.loc[(df['file']==file) & (df['Label']=='rime'),'seg_Start'] = \
            rimetimedict[file][0]
        df.loc[(df['file']==file) & (df['Label']=='rime'),'seg_End'] = \
            rimetimedict[file][1]
    return df

## Function to convert time to ms or normalize it to given scales
    ## If no scales are given...
        ## 'cl' is converted to negative time in ms (ending at 0)
        ## 'rime' is converted to positive time in ms (beginning at 0)
    ## Optional: If scales are given...
        ## provide {segment:[start,end]} (e.g. {'rime':[0,1]}) or ''
            ## NOTE: 'cl' is not automatically converted to negative here
                ## if you want negative 'cl' time, put a negative number
                ## in the starting position
def convert_time(data,
                 scale=''):
    ## Get copy of df
    df = data.copy(deep=True)
    ## If they want time scaled...
    if scale != '' and isinstance(scale,dict):
        ## Empty list to hold scaled time
        time_scaled = []
        ## Loop through df...
        for time, start, end, segment in zip(df['t_ms'], df['seg_Start'], 
                                             df['seg_End'],df['Label']):
            ## Get lower end of scale range for this label
            sc_d = scale[segment][0]
            ## Get upper end of scale range for this label
            sc_u = scale[segment][1]
            ## Append converted time to time_scaled
            time_scaled.append((((time-start) / (end-start)) * (sc_u - sc_d)) + sc_d)
        ## Overwrite df['t'] with time_scaled
        df['t'] = time_scaled
    ## If they did not want time scaled...
    else:
        ## Empty list to hold time converted to ms
        time_ms = []
        ## Loop through df
        for time, start, end, segment in zip(df['t_ms'],df['seg_Start'],
                                             df['seg_End'],df['Label']):
            ## If label is 'cl'...
            if segment == 'cl':
                ## Calculate negative time and append to time_ms
                time_ms.append((time-end)*1000)
            ## Otherwise...
            else:
                ## Calculate positive time and append to time_ms
                time_ms.append((time-start)*1000)
        ## Overwrtie df['t'] with time_ms
        df['t'] = time_ms
    return df

## We always combine rime in this script
df = combine_rime(df)

## Raise error if normalize_x is not 'yes' or 'no'
if normalize_x not in ['yes','no']:
    raise ValueError("Please provide 'yes' or 'no' for normalize_x.")

## If they asked for time normalization...
if normalize_x == 'yes':
    ## Normalize time with 0 < rime < 1 and -0.3 < cl < 0
    df = convert_time(df,
                      scale={'cl':[-0.3,0],
                             'rime':[0,1]})
else:
    df = convert_time(df)



# =============================================================================
# =============================================================================
# # Categorical Variable: Color   
# =============================================================================
# =============================================================================


## Function to filter df for multiple elements under one column
    ## Supply a df, a column, and list holding the desired strings
        ## Returns a df with only those strings under the given column
def df_col_filter(dataframe, column, filter_list):
    df = dataframe.copy(deep=True)
    df = df.apply(lambda row: row[df[column].isin(filter_list)])
    return df

## color_data errors
## Raise error if color_data is not a column
if color_data != '' and color_data not in df.columns:
    raise ValueError("Please provide a valid column for color_data.")

## color_filter errors
## Raise error if color_filter is not an empty string or a list
if color_filter != '' and isinstance(color_filter,list)==False:
    raise ValueError("Please provide a list or an empty string '' for color_filter.")
## Raise error if color_filter is a list, but it contains items not found in
    ## the color_data column
if isinstance(color_filter,list):
    if any([i not in list(set(df[color_data])) for i in color_filter]):
        raise ValueError("Please check color_filter list. An element is not found in color_data column.")

## color_dict errors
## Raise error if color_dict is not an empty string or a dictionary
if color_dict != '' and isinstance(color_dict,dict)==False:
    raise ValueError("Please provide a dictionary or an empty string '' for color_dict.")
## But if it is specified...
elif color_dict != '':
    ## And color_filter is specified
    if color_filter != '':
        ## If contents of color_dict and color_filter are not the same
        if set(color_dict) != set(color_filter):
            ## Raise an error if anything occurs in color_filter that is not
                ## also in color_dict
            if any([x not in color_dict for x in color_filter]):
                raise ValueError("The items in color_dict do not match the items in color_filter.")
            ## But if anything occurs in color_dict that does not occur in 
                ## color_filter, then we can just remove it from color_dict
            else:
                new_dict = {}
                for x in color_dict:
                    if x in color_filter:
                        new_dict[x] = color_dict[x]
                color_dict = new_dict
    ## Otherwise, if color_filter is not specified...
    else:
        ## If contents of color_dict and color_data column are not the same
        if set(color_dict) != set(df[color_data]):
            ## Raise an error if anything occurs in color_data column that is
                ## not also in color_dict column
            if any([x not in color_dict for x in list(set(df[color_data]))]):
                raise ValueError("The items in color_dict do not match the items in the color_data column.")
            ## But if anything occurs in color_dict that does not occur in 
                ## color_data col, then we can just remove it from color_dict
            else:
                new_dict = {}
                for x in color_dict:
                    if x in list(set(df[color_data])):
                        new_dict[x] = color_dict[x]
                color_dict = new_dict        

## If color_data is specified
if color_data != '':
    ## Drop any rows with NaN in the color_data column
    df = df.dropna(subset=[color_data])
    ## Drop any rows with '' in the color_data column
    df = df[df[color_data]!='']
    ## If the color_filter is specified...
    if color_filter != '':
        ## Drop any rows that are not in the color_filter list
        df = df_col_filter(df,color_data,color_filter)
        ## Set order for logical presentation of color categories
        df[color_data] = df[color_data].astype('category')
        df[color_data] = df[color_data].cat.reorder_categories(color_filter)


# =============================================================================
# =============================================================================
# # Categorical Variable: Line Type
# =============================================================================
# =============================================================================

## line_data errors
## Raise error if line_data is not a column
if line_data != '' and line_data not in df.columns:
    raise ValueError("Please provide a valid column for line_data.")

## line_filter errors
## Raise error if line_filter is not an empty string or a list
if line_filter != '' and isinstance(line_filter,list)==False:
    raise ValueError("Please provide a list or an empty string '' for line_filter.")
## Raise error if line_filter is a list, but it contains items not found in
    ## the line_data column
if isinstance(line_filter,list):
    if any([i not in list(set(df[line_data])) for i in line_filter]):
        raise ValueError("Please check line_filter list. An element is not found in line_data column.")

## If line_data is specified
if line_data != '':
    ## Drop any rows with NaN in the line_data column
    df = df.dropna(subset=[line_data])
    ## Drop any rows with '' in the line_data column
    df = df[df[line_data]!='']
    ## If the line_filter is specified...
    if line_filter != '':
        ## Drop any rows that are not in the line_filter list
        df = df_col_filter(df,line_data,line_filter)
        ## Set order for logical presentation of line type categories
        df[line_data] = df[line_data].astype('category')
        df[line_data] = df[line_data].cat.reorder_categories(line_filter)


# =============================================================================
# =============================================================================
# # Categorical Variable: Facet Wrap
# =============================================================================
# =============================================================================

## facet_data errors
## Raise error if facet_data is not a column
if facet_data != '' and facet_data not in df.columns:
    raise ValueError("Please provide a valid column for facet_data.")

## facet_filter errors
## Raise error if facet_filter is not an empty string or a list
if facet_filter != '' and isinstance(facet_filter,list)==False:
    raise ValueError("Please provide a list or an empty string '' for facet_filter.")
## Raise error if facet_filter is a list, but it contains items not found in
    ## the facet_data column
if isinstance(facet_filter,list):
    if any([i not in list(set(df[facet_data])) for i in facet_filter]):
        raise ValueError("Please check facet_filter list. An element is not found in facet_data column.")

## If facet_data is specified
if facet_data != '':
    ## Drop any rows with NaN in the facet_data column
    df = df.dropna(subset=[facet_data])
    ## Drop any rows with '' in the facet_data column
    df = df[df[facet_data]!='']
    ## If the facet_filter is specified...
    if facet_filter != '':
        ## Drop any rows that are not in the facet_filter list
        df = df_col_filter(df,facet_data,facet_filter)
        ## Set order for logical presentation of facet categories
        df[facet_data] = df[facet_data].astype('category')
        df[facet_data] = df[facet_data].cat.reorder_categories(facet_filter)


# =============================================================================
# =============================================================================
# # Axis Labels
# =============================================================================
# =============================================================================

## Generate a y-axis label
## Dictionary of y_data columns and associated units
units = {'F0':'Hz','H1H2':'dB','CPP':'dB'}
## Get unit from the units dictionary
unit = units[y_data]
## Overwrite unit with 'semitones' if they asked for semitones and norm above
if y_data == 'F0':
    if semitone_y == 'yes' and normalize_y == 'yes':
        unit = 'semitones'
## 
if normalize_y == 'yes':
    norm = ' relative to mean'
else:
    norm = ''
y_label = y_data + ' (' + unit + norm + ')'

## Generate an x-axis label
if normalize_x == 'yes':
    x_label = 'Time (normalized)'
else:
    x_label = 'Time (ms)'



# =============================================================================
# =============================================================================
# # Generate Plot & Export File
# =============================================================================
# =============================================================================

# =============================================================================
# Line Plot Function
# =============================================================================
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
              yscale ='',
              axis_labels = '',
              title = ''):
    ## Import what we need from plotnine
    from plotnine import ggplot, aes, geom_line, stat_smooth, scale_color_manual,\
    labs, facet_wrap, ggtitle, coord_cartesian, geom_vline, geom_hline
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
    # building the line plot
    # ========================================================================
    ## Start building the plot
    thisplot = ggplot(df) + stat
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
    if yscale != '':
        thisplot = thisplot + coord_cartesian(ylim=yscale)
    if any(n < 0 for n in df[x]):
        thisplot = thisplot + geom_vline(xintercept = 0)
    if normalize_y == 'yes':
        thisplot = thisplot + geom_hline(yintercept = 0, 
                                         linetype = 'dashed',
                                         color = 'gray')
    # ========================================================================
    # exporting the line plot
    # ========================================================================
    ## Get the export_to file path (a global variable)
    global export_to
    ## Export the file
    return thisplot.save(filename=filename,path=export_to)

## Generate plot and export file
myplot = line_plot(df,'t',y_data,export_file,
                   method = regression,
                   color = color_data, 
                   color_choice = color_dict, 
                   linetype = line_data, 
                   facet = facet_data,
                   axis_labels = [x_label,y_label])



# =============================================================================
# =============================================================================
# =============================================================================
# # # Things I Could Add Later
# =============================================================================
# =============================================================================
# =============================================================================

## Make combine_rime optional
## y-axis scaling
## titles
## manual axis labels
## A way to filter any column for categories
