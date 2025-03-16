# EXCAHNGE RATE JSON WRİTER FOR TURKEY

## USAGE

### To download the libraries, type this:

```
pip install -r gereksinimler.txt
```

### then run main.py with your IDE or terminal

# FILE EXPLANATIONS


## *downloadwebdriver.py*

### This file works if you get a webdriver not found error and allows you to download the webdriver from google


## *getdata.py*

### This file goes to the tcmb.gov.tr website and gets the exchange rates and then writes them to a dictionary data called jsondata If you dont have a webdriver it will run *downloadwebdriver.py* and open a video tutorial to install the webdriver


## *writejsondata.py*

### This file contains a function that takes a dictionary data as a parameter creates a file named *kur.json* in the directory containing the dictionary data in the parameter and writes the dictionary data to this file


## *main.py*

### This file gathers all other files together first *getdata.py* runs and sends the output variable jsondata to the function in *writejsondata.py* and the file is written here






