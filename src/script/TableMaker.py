from pandas import read_csv, DataFrame, concat as pd_concat
from tabulate import tabulate


class TableMaker:
    def __init__(self, header: bool = True):
        self.header = 0 if header else None

    def __call__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

        self._data_frame = self._read_data()

        table = tabulate(self._data_frame, headers='keys', showindex=False, tablefmt='psql', colalign=('center',))
        return table.replace("nan", "   ")

    def _read_data(self):
        self._data_frame = read_csv(self.input_file, header=self.header, encoding_errors='ignore')
        self._data_frame = self._insert_line_padding()
        self._data_frame.index = range(1, len(self._data_frame) + 1)
        return self._data_frame

    def _insert_line_padding(self):
        new_rows = []
        blank_row = [""] * len(self._data_frame.columns)

        new_rows.append(blank_row)
        for _, row in self._data_frame.iterrows():
            new_rows.append(row.tolist())
            new_rows.append(blank_row)

        self._data_frame = DataFrame(new_rows, columns=self._data_frame.columns)
        return self._data_frame

