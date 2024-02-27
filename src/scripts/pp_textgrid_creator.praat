################################################################
###  Read in all .wav files in a directory
###  and create new .TextGrid files
################################################################

## Use backslashes - no trailing back slash

form Read in .wav files and create new .TextGrid files
    comment Enter directory where sound files are kept:
    comment DO NOT put a final slash on file path
    sentence soundDir C:\my_project\audio
    comment Enter directory where text grids are to be kept:
    comment DO NOT put a final slash on file path
    sentence tgDir C:\my_project\audio
endform

Create Strings as file list... list 'soundDir$'/*.wav

numberOfFiles = Get number of strings

for ifile to numberOfFiles
   select Strings list
   fileName$ = Get string... ifile
   baseFile$ = fileName$ - ".wav"
   Read from file... 'soundDir$'/'baseFile$'.wav
   object_name$=selected$ ("Sound")
   To TextGrid: "ipa closure voicing", "voicing"
   Write to text file... 'tgDir$'/'baseFile$'.TextGrid

endfor

################################################################
#END OF SCRIPT
################################################################