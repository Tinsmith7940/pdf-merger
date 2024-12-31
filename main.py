from pypdf import PdfWriter
import argparse
from pathlib import Path
import sys

# Command line arguments
parser = argparse.ArgumentParser("Simple pdf merger utility")
parser.add_argument("-f", "--files", nargs="+", help="pdf file(s), space delimmited, to merge (e.g. '-f file1.pdf file2.pdf file3.pdf')", required=True)
parser.add_argument("-o", "--output", help="name of the merged pdf file. Defaults to 'merged_output.pdf'", default="merged_output.pdf")
args = parser.parse_args()
files = args.files
output_file = args.output

# Check that all files are valid before processing
errors = []
for file in files:
    c_file = Path(file)
    valid_file = c_file.is_file()
    if not valid_file:
        errors.append("'" + file + "' is not a valid file path")

if len(errors) > 0:
    for error in errors:
        print(error)
    # Exit script after printing errors
    sys.exit()

# Merge
merger = PdfWriter()

for pdf in files:
    merger.append(pdf)

# Write to file
merger.write(output_file)
merger.close()
