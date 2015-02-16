import os
import sys
import re

def parse_dir(dirname, extntype):
	file_list = os.listdir(dirname)
	for files in file_list:
		filepath = os.path.join(dirname,files)
		if os.path.isdir(filepath):
			parse_dir(filepath, extntype)
		else:
			if re.search(extntype, filepath):
				print filepath

def main():
	input_dir = raw_input("Enter the search Directory name: ")
	input_extn = raw_input("Enter the mime type : ")
	print "seaching in directory %s !!!!" % input_dir
	parse_dir(input_dir, input_extn)
 
if __name__ == "__main__":
	main()
