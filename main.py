import json
import csv
import time
import webbrowser
from conversion import *
import os.path

def main():
    qsf_output = {}
    qsf_input = None
    csv_input_name = ""

    if 0 <= 1 < len(sys.argv):
        csv_input_name = sys.argv[1]
    else:
        csv_input_name = input("What is the name of your file? ")

    # Build default qsf
    print("\nBuilding default .qsf")
    qsf_output = buildDefaultQsf(qsf_output)

    # Get qsf input from csv and convert to list
    print("Gathering csv data")
    qsf_input = gatherCsvData(qsf_input, csv_input_name)
    start_time = time.time()

    # Loop through every row and create questions
    print("Creating survey questions and blocks")
    qsf_output = createQuestions(qsf_input, qsf_output)

    #Create .qsf file
    print("Creating .qsf file")
    convertCsvToQsf(qsf_output)

    print("\nConversion took %s seconds.\n" % (time.time() - start_time))

if __name__ == "__main__":
    main()