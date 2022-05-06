This repository contains an educational virus written in Python to infect
other Python scripts (files with .py extension). 

Once run, pyison.py infects all Python scripts in the same directory as 
itself. An infected file also becomes infectious, unless the virus insertion 
caused a syntax error, in which case the infected file throws an error and
quits.

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

CURE/ANTIDOTE/REMOVAL:
Infected files can be recovered by deleting any and all lines between 
(and including):

"""VIRUS_START_POINT"""
"""VIRUS_END_POINT"""

These lines mark the start and end points of the virus code.

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

THIS IS STRICTLY AN EDUCATIONAL PYTHON SCRIPT WITH NO MALICIOUS INTENTIONS.

THE AUTHOR arda-guler DENIES ANY RESPONSIBILITY FOR ANY DAMAGE OR INCONVENIENCE 
CAUSED BY THE USE OF pyison.py OR ANY MODIFIED VERSION OF pysion.py FOR MALICIOUS
PURPOSES. BY DOWNLOADING AND/OR RUNNING ANY OF THE SCRIPTS IN THIS GITHUB 
REPOSITORY, THE USER TAKES ALL RESPONSIBILITY FOR ANY CONSEQUENCES.

IT IS FORBIDDEN TO MODIFY OR REDISTRIBUTE pyison.py UNDER ANY CIRCUMSTANCES.
