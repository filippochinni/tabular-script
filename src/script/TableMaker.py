from pandas import read_csv
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
        self._data_frame.index = range(1, len(self._data_frame) + 1)
        return self._data_frame
