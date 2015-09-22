# scripts-tools
Miscellaneous scripts and tools used around the house

__subtitle-timing-conflict.py__ -- Check simple timing collisions in .ASS subtitle files -- if a line begins before the previous line is finished.

__zero-bd-chapters.py__ -- Splits a Blu-ray formatted (HH:MM:SS.sss) chapter file into multiple files, zeroes out the first timestamp of each file, and adjusts the rest accordingly.  Useful if the source playlist references multiple sequential .m2ts files and you want to create a chapter list for each video.

__util.py__ -- Various utility functions used for scripting, required for use of the scripts.
