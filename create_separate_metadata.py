import os
import csv
from collections import OrderedDict

COMBO_METADATA_CSV_PATH = "/home/pphaneuf/temp/Metadata_spreadsheet.csv"
METADATA_OUTPUT = "/home/pphaneuf/temp/output"


def get_all_metadata_dict_list(combo_metdata_csv_path):
    all_metadata_dict_list = []
    with open(combo_metdata_csv_path,'r') as f:
        reader = csv.reader(f)
        next(reader)  # skips the instructions
        headerlist = next(reader)
        for row in reader:
            d = OrderedDict()
            for i, x in enumerate(row):
                d[headerlist[i]] = x
            all_metadata_dict_list.append(d)
    return all_metadata_dict_list


METADATA_FILE_NAME_ENTRY_LIST = ["project", "ALE-number", "Flask-number", "Isolate-number", "technical-replicate-number"]
def get_metadata_file_name(metadata_dict):
    metadata_file_name = ""
    for metadata_file_name_entry in METADATA_FILE_NAME_ENTRY_LIST:
        if metadata_file_name != "": metadata_file_name += '-'
        metadata_file_name += metadata_dict[metadata_file_name_entry]
    return metadata_file_name


all_metadata_dict_list = get_all_metadata_dict_list(COMBO_METADATA_CSV_PATH)

for metadata_dict in all_metadata_dict_list:
    csv_file_name = METADATA_OUTPUT + str(get_metadata_file_name(metadata_dict)) + ".csv"
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for key, value in metadata_dict.items():
            writer.writerow([key, value])
