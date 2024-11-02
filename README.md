# RankerScript

RankerScript is a command line tool that reads files in CSV format and outputs them in a tabular format.<br>
Inputs and Output files needs to be specified as cl args; multiple I/O files couples can be specified.<br>
Alternatively, a JSON file can be provided with mapping of input files to output files.

## Usage
### Command line usage
```
rankerscript [-h] [-i INPUT] [-o OUTPUT] [--files-mapping FILES_MAPPING] [--header-disabled]
```
### Options

`-h`, `--help` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp; Show this help message and exit

`-i INPUT`, `--input INPUT` &emsp;&emsp;&emsp;&emsp;Input file path, CSV format, can use relative path

`-o OUTPUT`, `--output OUTPUT` &emsp;&emsp;&ensp;Output file path, can use relative path

`--files-mapping FILES_MAPPING` &emsp;&ensp;JSON file with mapping of input files to output files

`--header-disabled` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp; First row of input files is NOT header


## Requirements
### Python
- Python 3.8 or higher
### Dependencies
- pandas
- tabulate
