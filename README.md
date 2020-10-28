# Zenodo_example
This is a repository for testing figshare and zenodo. It contains script1.py which generates 1000 random integers between 0-100, script2.py which passes the original dataset from script1.py througth a linear transformation y = 3x+6, and script3.py which plots the transformed data against the orignal data. 

# Reproducibility  
## create a virtual environment  
* locate to the local directory that contains the random generator scripts. 
* `pip install virtualenv` to install virtualenv package  
* `py -m venv env ` to start a virtual environment where env is the name of your environment  
* `.\env\Scripts\activate` to start the virtual environment 
* `pip install numpy, matplotlib, pandas` to install the necessary dependencies to fun the random number generator scripts  
* `python script1.py script1_output.csv` to run random number generator  
* `pip freeze > requirements.txt` to save the dependencies in requirements.txt file  
![screenshot](venv_screenshot.JPG)