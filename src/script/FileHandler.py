import os
from datetime import datetime
from json import load as json_load


class FileHandler:
    def __init__(self):
        self.input_files = []
        self.output_files = []

    def __call__(self, input_files, output_files):
        self.input_files = input_files
        self.output_files = output_files

    def handle_json(self, filename):
        with open(filename, 'r') as input_file:
            files_map = json_load(input_file)

        for key, value in files_map.items():
            reference_path = filename
            reference_dir = os.path.dirname(reference_path)

            input_path_join = os.path.join(reference_dir, key)
            output_path_join = os.path.join(reference_dir, value)

            input_path = os.path.abspath(input_path_join)
            output_path = os.path.abspath(output_path_join)

            self.input_files.append(input_path)
            self.output_files.append(output_path)

    def write_table(self, table, output_file):
        file_name = os.path.splitext(os.path.basename(output_file))[0]

        if not self._check_differences(table, output_file):
            return False

        sep = '\t' * 8
        timestamp = f"Last Update: {datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}"

        with open(output_file, 'w', encoding='utf-8') as output_file_write:
            output_file_write.write(f"{file_name}{sep}{timestamp}\n\n\n")
            output_file_write.write(table)

        return True

    def _check_differences(self, table, output_file):
        with open(output_file, 'r', encoding='utf-8') as output_file:
            old_table = output_file.read().partition('\n\n\n')[2]

        if old_table != table:
            return True

        return False
