import csv
import os
from pprint import pprint


def _get_metadata_key_dict(key_file_path_list):
    metadata_key_dict = {}
    for key_file_path in key_file_path_list:
        metadata_key_dict.update({key_file_path: []})
        with open(key_file_path) as key_file:
            csvreader = csv.reader(key_file)
            next(csvreader)  # skips header line
            for row in csvreader:
                metadata_key_dict[key_file_path].append(row[0])
    return metadata_key_dict


def _sort_metadata(metadata_key_dict, metadata_dir_path):
    metadata_file_name_list = [f for f in os.listdir(metadata_dir_path) if f.lower().endswith(".csv")]
    metadata_name_dict =
    for metadata_file_name in metadata_file_name_list:
        metadata_file_path = metadata_dir_path + '/' + metadata_file_name
        with open(metadata_file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            print(metadata_file_path)


def main():
    key_file_path_list = ["SSW_GLU_AC.csv", "SSW_GLU_GLY.csv", "SSW_GLU_XYL.csv", "SSW_GLU_XYL_GLY_AC.csv"]
    metadata_key_dict = _get_metadata_key_dict(key_file_path_list)
    _sort_metadata(metadata_key_dict, "/home/pphaneuf/git/metadata")


if __name__ == "__main__":
    main()
