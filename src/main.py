import os

from command_line.CLParser import CLParser
from script.FileHandler import FileHandler
from script.TableMaker import TableMaker


def main():

    cl_parser = CLParser()

    args = cl_parser()
    cl_parser.print_namespace()

    table_maker = TableMaker(header=not args.header_disabled)
    file_handler = FileHandler()

    if args.files_mapping:
        file_handler.handle_json(args.files_mapping)
    else:
        file_handler(args.input, args.output)

    for input_file, output_file in zip(file_handler.input_files, file_handler.output_files):
        if (not os.path.exists(input_file)) or (os.path.getsize(input_file) == 0):
            print(f"File {os.path.basename(input_file)} does not exist or is empty, skipping...\n")
            continue

        table = table_maker(input_file, output_file)
        written = file_handler.write_table(table, output_file)

        if written:
            print(f"Computing table for {input_file}...")
            print(f'Table written to {output_file}\n\n{table}\n')
        else:
            print(f"{os.path.basename(output_file)} has not changed, there is no need to update the file")
            print(f"Nothing written to {output_file}")
            print(f"Computed Table:\n\n{table}\n")


if __name__ == '__main__':
    main()

