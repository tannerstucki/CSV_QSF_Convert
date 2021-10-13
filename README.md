# CSV_to_QSF_convert
For now, the order of columns in the csv must match this template:
https://docs.google.com/spreadsheets/d/1jdelmImMemFBtSrb_-7ZdGRkE48Up4PyEnKl3TaOht0/edit#gid=158088693

To run this automation, pull the csv file into the same folder as the script.

The first command line argument is the name of the csv file. If this is empty, it will prompt you to give the csv file name.
The second command line argument is the name of the opp. This can be empty but it will prompt you to add one when running. If still empty, it will input a placeholder opp name.
The third command line argument is the way text in cells is delimited. If it is empty, it will default to new line delimiters. If there is anything, it will assume comma delimiters.

Here is an example run command:
python3 main.py [csv name] [opp name]