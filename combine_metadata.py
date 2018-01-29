import os
import csv


ALL_METADATA_CSV_NAME = "all_metadata.csv"


def _get_metadata_dict(metadata_dir_path):
    metadata_dict = {}
    metadata_file_name_list = [f for f in os.listdir(metadata_dir_path) if f.lower().endswith(".csv")]
    for metadata_file_name in metadata_file_name_list:
        metadata_file_path = metadata_dir_path + '/' + metadata_file_name
        with open(metadata_file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                field_name = row[0]
                field_value = row[1]
                if field_name in metadata_dict.keys():
                    metadata_dict[field_name].append(field_value)
                else:
                    metadata_dict[field_name] = [field_value]
    return metadata_dict


def output_all_metadata_csv(metadata_dict):
    with open(ALL_METADATA_CSV_NAME, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for field_name, field_value_list in metadata_dict.items():
            csv_row = [field_name] + field_value_list
            csv_writer.writerow(csv_row)


def main():
    metadata_dict = _get_metadata_dict("/home/pphaneuf/glu_metadata")
    output_all_metadata_csv(metadata_dict)


if __name__ == "__main__":
    main()
