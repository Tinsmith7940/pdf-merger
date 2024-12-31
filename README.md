# PDF-Merger
A simple utility script for merging multiple pdf files together

## Usage
This can be used by calling the `main.py` script:
`python main.py`

or

`python3 main.py`

```sh
>> python main.py -h
usage: Simple pdf merger utility [-h] -f FILES [FILES ...]

options:
  -h, --help            show this help message and exit
  -f, --files FILES [FILES ...]
                        pdf file(s), space delimmited, to merge (e.g. '-f
                        file1.pdf file2.pdf file3.pdf')
```
## Example usage
Let's say we have some pdfs to merge in our `Documents` folder
- copy the `main.py` into the same Documents folder
- open a terminal
- change into the Documents directory (e.g. `cd ~/Documents`)
- now type `python main.py 1.pdf 2.pdf`
  - `python` -tells the computer to use python to run the script
  - `main.py`- the script that actually merges the files
  - `1.pdf etc...` - these are the files we want to merge. The script will merge in the order that they are listed (in this case 1.pdf will be at the beginning, 2.pdf next, etc...)
- The file `merged_output.pdf` will be created
 
```sh
>> cd ~/Documents
>> python main.py 1.pdf 2.pdf
```

## Setup
### Installation
Make sure the following are setup on your machine:
- Python 3
```sh
python --version
```
Make sure that the printed version `is 3.x.x`
- pypdf - this can be installed with `pip`
```sh
pip install pypdf
```
### Script
Clone this repo, or copy the `main.py` file into your desired local folder
