#!/usr/bin/env python3



import sys

import subprocess

import argparse

import os




# Block that will allow LED light to turn on

replacement_block = [

    "000000000000000010",

    "000100000000000000",

    "000000000000000000",

    "000000000000000001",

    "000000000000110010",

    "000000000000110000",

    "000000000000000100",

    "000000000000000000",

    "000000000000000000",

    "000000000000000000",

    "000000000000000000",

    "000000000000000000",

    "000000000000000000",

    "000000000000000000",

    "000000011000000000",

    "000000000000000000",

]






# Tiles that control the LED color. io 4 controls blue, 5 controls green, 6 controls red
# Move items in list to change what colors you want on. 

target_tiles = [



    ".io_tile 6 31",

    ".io_tile 4 31"

]



    

 #   ".io_tile 5 31",




# Block replacement function. Chatgpt did most of this

def replace_tiles(filename):

    try:

        with open(filename, "r") as file:

            lines = file.readlines()



        output_lines = []

        i = 0

        while i < len(lines):

            line = lines[i].rstrip()



            if line in target_tiles:

                # Keep the tile marker

                output_lines.append(line + "\n")

                i += 1  # move to the first line under .io_tile



                # Replace next 16 lines

                output_lines.extend(line + "\n" for line in replacement_block)

                i += 16  # skip the original 16 lines

            else:

                output_lines.append(lines[i])

                i += 1



        # Write back to the file (or a new one if you want)

        with open(filename, "w") as file:

            file.writelines(output_lines)



    except FileNotFoundError:

        print(f"Error: File {filename} not found.")

        sys.exit(1)



def main():


# Using argparse to allow required arguments to be called for each command

	parser = argparse.ArgumentParser()

  # creates bin_file attribute for later use in the args variable
	parser.add_argument("bin_file" , type = str)

  
	#parser.add_argument("asc_file" , nargs = "?",  type = str)

  # Creating args variable
	args = parser.parse_args()

  # Storing all args in a list to be used with command
	args_list = [args.bin_file, "omm.asc"]



	# Bellow arg code unclean bc I was testing stuff but will remove uneeded stuff later

	if args_list[1] != None:

	

		try:

			subprocess.run(["iceunpack"] + args_list, check = True)

		except subprocess.CalledProcessError:

			sys.exit(1)

	
# This else should be one of the things not needed bc we will always be using unpack with both arguments
# Was here originally bc I was testing with unpack by itself and noticed if only bin file is given then asc is printed to terminal
	else:

	

		args_list.pop()

		try:

			subprocess.run(["iceunpack"] + args_list, check = True)

		except subprocess.CalledProcessError:

			sys.exit(1)

			

			

			
# calling the replacement function
	replace_tiles("omm.asc")

  
# Swapping the order of the files bc icepack requires the asc file to be first
	args_list[0], args_list[1] = args_list[1], args_list[0]

	

	

	try:

		subprocess.run(["icepack"] + args_list, check=True)

	except subprocess.CalledProcessError:

		#print("icepack failed. Check your device and arguments.")

		sys.exit(1)

   


  # Removing the asc file from list so that iceprog can be run as it will only allow 1 argument
	args_list.pop(0)

	
# Deleting omm.asc from directory
	os.remove("omm.asc")



	try:

		subprocess.run(["iceprog"] + args_list, check=True)

	except subprocess.CalledProcessError:

		#print("icepack failed. Check your device and arguments.")

		sys.exit(1)     

        



if __name__ == "__main__":

    main()

