# =============================================================================
# Add this info manually
# =============================================================================

## Provide the filepath to your project folder where the error report will 
    ## be placed
project_folder = r"C:\talieng_project"

## Now you can run the script
## This script will return a list of errors or let you know if there are none
## If errors are found, manually edit the TextGrids to fix the errors
## DON'T FORGET TO SAVE THE TEXTGRIDS WHEN YOU EDIT THEM
## Once you have addressed the errors, run the script again, to be sure





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
# Functions
# =============================================================================

## function to import csv files
def import_csv(file):
    import pandas as pd
    return pd.read_csv(file)

## function to import excel files
def import_excel(file,sheet='Sheet1'):
    import pandas as pd    
    return pd.ExcelFile(file).parse(sheet)

## This function identifies NaNs (they are not equal to themselves)
def isNaN(num):
    return num!= num

# =============================================================================
# Error Checks and Data Import
# =============================================================================

## Check to make sure lexical db exists and is .xlsx
## Get file path to lexdb
import os
lexical_database = os.path.join(project_folder,'lexical_database.xlsx')
## Check
if not lexical_database.endswith('.xlsx'):
    msg = 'Please ensure that lexical_database.xlsx is in your project folder.'
    raise ValueError(msg)
if not os.path.isfile(lexical_database):
    msg = 'Please ensure that lexical_database.xlsx is in your project folder.'
    raise ValueError(msg) 

## import lexdb as a dataframe
dflex = import_excel(lexical_database)
## Get rid of .wav if it's in the file names
dflex['file'] = [i.replace('.wav','') for i in dflex['file']]

## Check to make sure ps output exists and is .txt
## get file path to PraatSauceOutput.txt
ps_output = os.path.join(project_folder,'PraatSauceOutput.txt')
## Check
if not ps_output.endswith('.txt'):
    msg = 'Please ensure that PraatSauceOutput.txt is in your project folder.'
    raise ValueError(msg)
if not os.path.isfile(ps_output):
    msg = 'Please ensure that PraatSauceOutput.txt is in your project folder.'
    raise ValueError(msg) 

## Check that 'ov' is a column in ps_output
## import PraatSauceOutput.txt as a dataframe
df = import_csv(ps_output)
## change 'Filename' to 'file' in df (praatsauce datas)
df = df.rename(columns={'Filename':'file'})
## Check
if not 'ov' in df.columns:
    msg = 'Tier 3 label "ov" does not appear in your PraatSauceOuput.txt file.'
    raise ValueError(msg)
    


# =============================================================================
# Get dictionaries with relevant infos for Tiers 2 and 3
# =============================================================================

## define list of Tier 2 segments
segment_list = ['cl','op','cd']

## Empty dictionaries to hold {file:{label:time}}] for Tiers 2 and 3
    ## In Tier 2, time = seg_Start for the segment (segment tier)
    ## in Tier 3, time = the time of the point (point tier)
t2dict = {}
t3dict = {}

## Loop through files
for file in list(set(df['file'])):
    ## Get fresh df and reset index
    dfi = df[df['file']==file].reset_index(drop=True)
    ############
    ## Tier 3 ##
    ############
    ## Set dictionary for this file
    this_t3dict = {}
    ## List of points
    labels = ['ov']
    ## Loop through labels
    for label in labels:
        ## Get value for this label
        value = dfi.loc[0,label]
        ## If value for this label is not a NaN
        if isNaN(value) == False:
            ## Add label and value to this_t3dict
            this_t3dict[label] = value
    ## Add these infos to t3dict
    t3dict[file] = this_t3dict
    ############
    ## Tier 2 ##
    ############
    ## Set dictionary for this file
    this_t2dict = {}
    ## List of labels
    labels = list(set(dfi['Label']))
    ## Loop through labels
    for label in labels:
        ## Get list of unique seg_Start values for this label
        starts = list(set(dfi[dfi['Label']==label]['seg_Start']))
        ## Write start list to this_t2dict by label key
        this_t2dict[label] = starts
    ## Add these infos to t2dict
    t2dict[file] = this_t2dict

# =============================================================================
# Calculate IQR for each segment
# =============================================================================

## Fresh df
dfi = df.copy(deep=True)
## Just t=1
dfi = dfi[dfi['t']==1]
## Add duration column
dfi['duration'] = ''
## Calculate duration
duration = []
for start, end in zip(dfi['seg_Start'], dfi['seg_End']):
    duration.append(end - start)
dfi['duration'] = duration

## Empty dictionary to hold whisker values
whiskerdict = {}

## Empty dictionary to hold segment durations for each file
durdict = {}

## Create an empty dict for each file in durdict
for file in list(set(dfi['file'])):
    durdict[file] = {}

## Loop through labels in 'Label'
for label in segment_list:
    ## Get df for this label
    dfl = dfi[dfi['Label']==label]
    ## Get quartiles & interquartile range
    quartile_up = dfl['duration'].quantile(0.75)
    quartile_down = dfl['duration'].quantile(0.25)
    iqr = quartile_up - quartile_down
    ## Get whiskers
    whisker_up = quartile_up + iqr*2
    whisker_down = quartile_down - iqr*2
    ## Write these numbers to a dict
    thisdict = {}
    thisdict['up'] = whisker_up
    thisdict['down'] = whisker_down
    ## Append thisdict to whiserkdict for this label
    whiskerdict[label] = thisdict
    ## Loop through files
    for file in dfl['file']:
        durdict[file][label] = list(set(dfl[dfl['file']==file]['duration']))[0]
        
# =============================================================================
# Error Checks
# =============================================================================

## Prepare errors dictionary
    ## Add every file as a key
    ## Add an empty list for each key
        ## {file:[]}
errors = {}
for file in list(set(df['file'])):
    errors[file] = []

## Loop through files
for file in list(set(df['file'])):
    ## Get dictionaries for this file
    t2 = t2dict[file]
    t3 = t3dict[file]
    dur = durdict[file]
    
    ############################################
    ## Step 1:                                ##
    ## Check for the Mandatory Segment Labels ##
    ############################################
    ## Every tg must have 'op' on Tier 2 and 'ov' on Tier 3
    if 'op' not in t2:
        errors[file].append('"op" is missing from Tier 2')
    if 'ov' not in t3:
        errors[file].append('"ov" is missing from Tier 3')
    
    #####################################
    ## Step 2:                         ##
    ## Check for Repeat Segment Labels ##
    #####################################
    ## There must be no repeat segment labels on Tier 2 or Tier 3
    ## For t2, if a label repeats, it will have two values in the list for
        ## that label key
    ## Empty list to hold any labels that are duplicated
    badlist = []
    ## Loop through labels in t2
    for label in t2:
        ## If there is more than one value associated with that label
        if len(t2[label]) > 1:
            ## Append that label to the badlist
            badlist.append(label)
    ## Loop through the badlist and write errors to the errors dict
    for z in badlist:
        errors[file].append('There are duplicate ' + \
                            str(z) + \
                            ' segment labels on Tier 2')
    ## For t3, if a label repeats, PraatSauce only takes the one that falls
        ## later chronologically. We have no way to check for this    

    #######################################    
    ## Step 3:                           ##
    ## Check for Aberrant Segment Labels ##
    #######################################
        ## All segment labels must appear in the lists above
    for label in t2:
        if label not in segment_list:
            errors[file].append('Aberrant label "' + \
                                str(label) + \
                                '" appears in Tier 2')
    for label in t3:
        if label not in ['ov']:
            errors[file].append('Aberrant label "' + \
                                str(label) + \
                                '" appears in Tier 3')

    #############################################
    ## Step 4:                                 ##
    ## Check for Aberrant Segment Label Orders ##
    #############################################
        ## Tier 2 labels should only occur in cl - op - cd order
        ## Tier 3 labels should only occur in ov - cv - rv order
    t2_correct = ['cl','op','cd']
    t3_correct = ['ov','cv','rv']
    ## First, we need to fix t2 so that it doesn't have lists for values
        ## Any list longer than 1 will be dropped
        ## Any list of one will be converted to just that one value
    new_t2 = {}
    for label in t2:
        if len(t2[label]) == 1:
            new_t2[label] = t2[label][0]
    t2 = new_t2
    
    ## Now we need to sort t2's labels by time in ascending order
    sort_labels = sorted(t2.items(), key=lambda x: x[1])
    sorted_labels = []
    for i in sort_labels:
        sorted_labels.append(i[0])
    ## Now, if sorted_labels does not match the correctly ordered list above,
        ## we have to report an error
    ## First, drop any labels from t2_correct that do not occur in this word
    t2_correct = [i for i in t2_correct if i in t2]
    ## Now check if they match
    if sorted_labels != t2_correct:
        errors[file].append('Tier 2 labels appear in the wrong order')
    
    ## Moving on to t3, let's sort
    sort_labels = sorted(t3.items(), key=lambda x: x[1])
    sorted_labels = []
    for i in sort_labels:
        sorted_labels.append(i[0])
    ## Now, if sorted_labels does not match the correctly ordered list above,
        ## we have to report an error
    ## First, drop any labels from t3_correct that do not occur in this word
    t3_correct = [i for i in t3_correct if i in t3]
    ## Now check if they match
    if sorted_labels != t3_correct:
        errors[file].append('Tier 3 labels appear in the wrong order')

    ##############################################    
    ## Step 5:                                  ##
    ## Check for Segment Duration Abnormalities ##
    ##############################################
        ## Every segment duration should fall within the whiskers
    for label in dur:
        if dur[label] > whiskerdict[label]['up']:
            ## Round it and convert it to ms
            thisdur = round(dur[label]*1000)
            errors[file].append('The '+str(label)+\
                                ' segment is suspiciously long (' +\
                                    str(thisdur) +\
                                    ' ms).'
                                    )
        elif dur[label] < whiskerdict[label]['down']:
            ## Round it and convert it to ms
            thisdur = round(dur[label]*1000)
            errors[file].append('The '+str(label)+\
                                ' segment is suspiciously short (' +\
                                str(thisdur) +\
                                ' ms).'
                                )



# =============================================================================
# Preparing the Error Report
# =============================================================================

## empty list to hold error report
errorlist = []

## Loop through errors dictionary
for file in sorted(list(errors)):
    ## if there are errors to report for this file
    if len(errors[file]) > 0:
        ## Get word
        word = list(set(dflex[dflex['file']==file]['word']))[0]
        ## Loop through the errors
        for error in errors[file]:
            ## write them to errorlist with the file name
            errorlist.append(str(file) + ' ' + str(word) + ': ' + str(error))

## Write an encouraging message if there are no errors
if errorlist == []:
    errorlist.append('No errors to report. Good work!')

## change directory to project folder
import os
os.chdir(project_folder)

## define name of annotation error report text file
output = 'annotation_error_report.txt'
output_path = os.path.join(project_folder,output)

## Remove the annotation error report if there is one present already
if os.path.isfile(output_path):
    os.remove(os.path.join(project_folder,output))

## open the error report file in write mode
import codecs
errorfile = codecs.open(output,'w','utf-8')

## Loop through errorlist
for i in errorlist:
    ## Write each error to the error report file
    errorfile.write(i+'\n')

## Close the error report file
errorfile.close()