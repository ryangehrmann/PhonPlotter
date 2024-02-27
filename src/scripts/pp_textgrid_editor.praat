##  This script opens all the sound files in a given directory, plus their associated textgrids so that you can review/change the marks.

## Use backslashes
## DO INCLUDE TRAILING BACKSLASH

form Enter wav file directory
	sentence Directory C:\my_project\audio\
	comment Enter TextGrid directory
	comment DO INCLUDE a backslash
	sentence Grids C:\my_project\audio\
endform

extension$ = ".wav"

Create Strings as file list... list 'directory$'*'extension$'
number_of_files = Get number of strings
for x from 1 to number_of_files
     select Strings list
     current_file$ = Get string... x
     Read from file... 'directory$''current_file$'
	 file_name$ = left$ (current_file$,length (current_file$) - 4 )
     object_name$ = selected$ ("Sound")
     Read from file... 'grids$''file_name$'.TextGrid
     plus Sound 'object_name$'
     Edit
     pause  Mark your segments! 
     minus Sound 'object_name$'
     Write to text file... 'directory$''file_name$'.TextGrid
     select all
     minus Strings list
     Remove
endfor	

select Strings list
Remove
print Congratulations! All files processed -- that was fun!

## written by Katherine Crosswhite
## crosswhi@ling.rochester.edu