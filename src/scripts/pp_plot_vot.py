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

###########
## Color ##
###########

## Specify a Color Column holding categorical data
    ## provide column header as a string 
    ## or provide an empty string if you do not want to use colors
color_column = 'T'

## Provide a dictionary of {categories:colors}
    ## or provide an empty string if you do not want to specify colors
color_dict = ''

############
## Facets ##
############

## Note: "facets" are just separate plots within a larger figure

## Specify a Facet Column holding categorical data
    ## provide column header as a string
    ## or provide an empty string if you do not want to use facets
facet_column = 'T'

####################
## General Filter ##
####################

## If there are any other categories that you would like to filter, you can
    ## do that here
        ## E.g. you may want to look at monophthongs only, or speaker 1 only
## Provide a dictionary formatted as follows:
    ## {column:[list of items to keep], 
    ##  column:[list of items to keep]}
        ## e.g. {'speaker':['F1','M1']} 
        ## all speakers othern than F1 and M1 will be excluded
## NOTE: categories that are filtered out will not be inlcluded when
    ## calculating outliers and y_data normalization
    ## the filtering will happen before that
## If you do not want to filter, just provide an empty string ''
filter_dict = {'onset':['vl_stop']}

###############
## Bin Width ##
###############

## If you would like to manually set historgram bin width, do so here
    ## Give an integer (i.e. a whole number that IS NOT in '')
## If you do not want to specify bin width, provide an empty string ''
bin_width = 4

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



# =============================================================================
# 2.4 Data Export
# =============================================================================

#################
## Export Data ##
#################

## Define file path to output folder and output file name
export_to = os.path.join(project_folder,'export')
export_file_histo = 'vot_histogram'
export_file_box = 'vot_box'

## Check to make sure target directory exists and, if not, make it
if not os.path.isdir(export_to):
    os.makedirs(export_to)

## Get full file path to export file
export_path_histo = os.path.join(export_to,export_file_histo+'.png')
export_path_box = os.path.join(export_to,export_file_box+'.png')

## If the export_file already exists
if os.path.isfile(export_path_histo):
    export_file_histo = export_file_histo+'_'
    while export_file_histo+'.png' in os.listdir(export_to):
        export_file_histo = export_file_histo + '_'
    export_path_histo = os.path.join(export_to,export_file_histo+'.png')
if os.path.isfile(export_path_box):
    export_file_box = export_file_box+'_'
    while export_file_box+'.png' in os.listdir(export_to):
        export_file_box = export_file_box + '_'
    export_path_box = os.path.join(export_to,export_file_box+'.png')




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
            if not isinstance(cat, str):
                msg = 'filter_dict values must be lists that contain only strings. Please check.'
                raise ValueError(msg)
            if cat not in list(set(df[col])):
                msg = 'filter_dict values must be lists that contain categories that actually occur in the column indicated in the corresponding filter_dict key. Please check.'
                raise ValueError(msg)                



# =============================================================================
# 3.2 General Filter
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
# # 4 Calculate VOT
# =============================================================================
# =============================================================================

# =============================================================================
# 4.1 Error Check 3: User Inputs Related to VOT Values
# =============================================================================

###############
## bin_width ##
###############

## is '' or an integer?
if bin_width != '' and isinstance(bin_width, int) == False:
    msg = 'bin_width must be an integer or an empty string. Please check.'

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

##################
## facet_column ##
##################

## is '' or a valid column header?
if facet_column not in df.columns and facet_column != '':
    msg = 'facet_column must be a string and a valid column header. Pleaes check.'
    raise ValueError(msg)

##########################################################
## blanks in categorical variable columns: color, facet ##
##########################################################

## We want the users to be aware if there are rows in their category columns
    ## that are left empty. This could be an oversight and mess up results. 
## If the user specified a color or facet column that contains
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
# 4.2 Calculate VOT
# =============================================================================

## Filter for Label == 'op'
df = df[df['Label']=='op']

## Filter time for t = 1
df = df[df['t']==1]

## Calculate VOT in ms
## Empty list to hold vot
vot_list = []
## Loop through df
for ov, op_start in zip(df['ov'],df['seg_Start']):
    ## Append vot in ms to vot_list
    vot_list.append((ov-op_start)*1000)
## Write vot_list datas into df in new column 'vot'
df['vot'] = vot_list



# =============================================================================
# =============================================================================
# # 5 PLOTS
# =============================================================================
# =============================================================================

# =============================================================================
# 5.1 Generate Histogram Plot & Export File
# =============================================================================

#########################
## Function: Histogram ##
#########################

## Function to produce a histogram and export it to project folder
    ########################    
    ## These Are Required ##    
    ########################
    ## df (dataframe)
    ## x: column containing a continuous variable to plot along x-axis
    ## filename: provide a name for the exported plot image file
    ########################
    ## These Are Optional ##
    ########################
    ## color: column containing a categorical variable. Will show multiple
        ## regression lines, one per variable (e.g. voicing, tone, etc...)
    ## color_choice: dictionary specifying colors for EVERY variable in the 
        ## column specified for color (e.g. {'voiced':'blue','voiceless':red})
        ## Can only be used if you specified a column for color
    ## facet = column containing a categorical variable. Will show multiple 
        ## plots, one for each variable in this column
    ## axis_labels = list specifying labels for x and y axes. Provide x fist.
        ## (e.g. ['Time (ms)','f0 (Hz)'])
    ## title = a string continaing plot title (e.g. 'f0 and Register')
    #########################
    ## These Are Automatic ##
    #########################
    ## If negative numbers are included on x, a vertical line will be drawn
        ## at x=0
def histogram(df,x,filename,
              bin_width='',
              color='', 
              color_choice='',
              facet='',
              axis_labels = '',
              title = ''):
    ## Import what we need from plotnine
    from plotnine import ggplot, geom_histogram, aes, geom_vline, \
        facet_wrap, scale_fill_manual, labs, ggtitle
    # ========================================================================
    # color and bin_width
    # ========================================================================
    ## First we deal with color and bin_width
        ## Both of these are determined within geom_histogram()
        ## So we need to make appropriate versions of these
    ## neither color nor bin_width
    if all([i == '' for i in [color,bin_width]]):
        geom = geom_histogram(aes(x=x))
    ## color is specified, not bin_width
    elif color != '' and bin_width == '':
        geom = geom_histogram(aes(x=x,fill=color))
    ## bin_width is specified, not color
    elif color == '' and bin_width != '':
        geom = geom_histogram(aes(x=x),binwidth=bin_width)
    ## both color and bin_width are specified
    elif all([i!='' for i in [color,bin_width]]):
        geom = geom_histogram(aes(x=x,fill=color),binwidth=bin_width)
    # ========================================================================
    # building the line plot
    # ========================================================================
    ## Start building the plot
    thisplot = ggplot(df) + geom
    ## Add a vertical line at vot = 0
    thisplot = thisplot + geom_vline(xintercept = 0)
    if color_choice != '':
        thisplot = thisplot + scale_fill_manual(values=color_choice)
    if facet != '':
        thisplot = thisplot + facet_wrap(facet,ncol=1)
    if axis_labels != '':
        thisplot = thisplot + labs(x=axis_labels[0],y=axis_labels[1])
    if title != '':
        thisplot = thisplot + ggtitle(title)
    # ========================================================================
    # exporting the line plot
    # ========================================================================
    ## Get the export_to file path (a global variable)
    global export_to
    ## Export the file
    return thisplot.save(filename=filename,path=export_to)

## Produce vot histogram plot
histogram(df,'vot',export_file_histo,
          bin_width=bin_width,
          color=color_column, 
          color_choice=color_dict,
          facet=facet_column,
          axis_labels = ['VOT (ms)','Count'],
          title = '')

# =============================================================================
# 5.1 Generate Box & Whisker Plot & Export File
# =============================================================================

## Function to produce a box & whisker plot and export it to project folder
    ########################    
    ## These Are Required ##    
    ########################
    ## df (dataframe)
    ## x: column containing a categorical variable to plot along x-axis
    ## y: column containing a continuous variable to plot along y-axis
    ## filename: provide a name for the exported plot image file
    ########################
    ## These Are Optional ##
    ########################
    ## outliers: do you want to show outliers in the boxplot? No by default.
    ## color: column containing a categorical variable. Will show multiple
        ## boxes/whiskers, one per variable (e.g. voicing, tone, etc...)
    ## color_choice: dictionary specifying colors for EVERY variable in the 
        ## column specified for color (e.g. {'voiced':'blue','voiceless':red})
        ## Can only be used if you specified a column for color
    ## facet = column containing a categorical variable. Will show multiple 
        ## plots, one for each variable in this column
    ## axis_labels = list specifying labels for x and y axes. Provide x fist.
        ## (e.g. ['Tone Category','f0 (Hz)'])
    ## title = a string continaing plot title (e.g. 'f0 and Register')
def box_plot(df,x,y,filename,
             outliers='',
             color='',
             color_choice='',
             facet='',
             axis_labels='',
             title=''):
    ## Import what we need from plotnine
    from plotnine import ggplot, geom_boxplot, aes, scale_color_manual, \
    facet_wrap, labs, ggtitle
    # ========================================================================
    # building the line plot
    # ========================================================================
    ## Start building the plot
    thisplot = ggplot(df)
    ## If they want outliers, get it inside geom_boxplot here
    if outliers != '':
        thisplot = thisplot + geom_boxplot()
    else:
        thisplot = thisplot + geom_boxplot(outlier_shape='')
    ## If color is specified, get it inside the aes
    if color != '':
        thisplot = thisplot + aes(x=x,y=y,color=color)
    ## If color is not specified, no color in aes
    else:
        thisplot = thisplot + aes(x=x,y=y)
    ## Deal with the remaining conditions
    if color_choice != '':
        thisplot = thisplot + scale_color_manual(values=color_choice)
    if facet != '':
        thisplot = thisplot + facet_wrap(facet)
    if axis_labels != '':
        thisplot = thisplot + labs(x=axis_labels[0],y=axis_labels[1])
    if title != '':
        thisplot = thisplot + ggtitle(title)
    # ========================================================================
    # exporting the box plot
    # ========================================================================
    ## Get the export_to file path (a global variable)
    global export_to
    ## Export the file
    return thisplot.save(filename=filename,path=export_to)


## Produce vot box & whisker plot
box_plot(df,color_column,'vot',export_file_box,
         color=color_column, 
         color_choice=color_dict,
         facet=facet_column,
         axis_labels = ['','VOT (ms)'],
         title = '')