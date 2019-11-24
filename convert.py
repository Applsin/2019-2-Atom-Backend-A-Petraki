import re
csv_file = './CIDDS-001-external-week1.csv'
txt_file = './CIDDS-001-external-week1.txt'
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file,skipinitialspace=False)]
    my_output_file.close()