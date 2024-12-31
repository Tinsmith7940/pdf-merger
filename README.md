# PyPDF-Merge
A simple utility script for merging multiple pdf files together

## Usage
This can be used simply by calling the `main.py` script:
`python main.py`
or
`python3 main.py`

## Example usage
Let's say we have some pdfs to merge in our `Documents` folder
- copy the `main.py` into the same documents folder
- open a terminal
- change into the documents directory (e.g. `cd ~/Documents`)
- now type `python main.py 1.pdf 2.pdf`
  - `python` -tells the computer to use python to run the script
  - `main.py`- the script that actually merges the files
  - `1.pdf etc...` - these are the files we want to merge. The script will merge in the order that they are listed (in this case 1.pdf will be at the beginning, 2.pdf next, etc...)

## Setup
### Installation
Make sure the following are setup on your machine:
- Python 3
```python
python --version
```
Make sure that the printed version `is 3.x.x`
- pypdf - this can be installed with `pip`
```
pip install pypdf
```
### Script
Clone this repo, or copy the `main.py` file into your desired local folder
