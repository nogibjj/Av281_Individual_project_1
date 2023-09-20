# Continuous Integration using GitHub Actions of Python Data Science Project

My project utilizes the "Auto" dataset for data visualizations, and the "Nba" dataset for testing purposes. The goal of this project is to test and display the exploratory data analysis functions in lib.py created using pandas. The github actions workflow makes sure that upon each push, the code undergoes linting, formatting, installing dependencies, and testing of the entire project (python script and Jupyter notebook).

## Contents:
* Jupyter Notebook with:
  * Cells that perform descriptive statistics using `Pandas`, with functions from lib.py
  * Tested by using nbval plugin for pytest
* [Python Script](https://github.com/nogibjj/Av281_Individual_project_1/blob/main/main.py) performing the `Pandas` descriptive stats function.
* [lib.py](https://github.com/nogibjj/Av281_Individual_project_1/blob/main/lib.py) file that shares the common code between the script and notebook
* [Makefile](https://github.com/nogibjj/Av281_Individual_project_1/blob/main/Makefile) with the following:
  * Run all tests (test notebook, script and lib)
  * Formats code with Python black
  * Lints code with Ruff
  * Installs code via:  pip install -r requirements.txt
* [test_main.py](https://github.com/nogibjj/Av281_Individual_project_1/blob/main/test_main.py) to test script
* [test_lib.py](https://github.com/nogibjj/Av281_Individual_project_1/blob/main/test_lib.py) to test library
* [requirements.txt](https://github.com/nogibjj/Av281_Individual_project_1/blob/main/requirements.txt)
* [GitHub Actions](https://github.com/nogibjj/Av281_Individual_project_1/tree/main/.github/workflows) performs all four Makefile commands with badges for each one

## Requirements:
- black==22.3.0
- click==8.1.3 
- django == 3.2
- pytest==7.1.3
- pytest-cov==4.0.0
- pylint==2.15.3
- ruff==0.0.284
- boto3==1.24.87
- fastapi==0.85.0
- uvicorn==0.18.3
- nbval==0.10.0
- nbqa==1.7.0
- numpy
- pandas==2.1.0
- matplotlib==3.7.2
- seaborn==0.12.2
- ipykernel

## Lib.py



<p align = "center"><img width="1000" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Mini_project_2/blob/main/Images_for_mini_project_2/Screenshot%202023-09-13%20at%204.42.48%20PM.png"></p>

Then run the command 'make install'

followed by 'make test'

### Testing
<p align = "center"><img width="1000" alt="Screenshot 2023-09-11 at 11 53 56 AM" src="https://github.com/nogibjj/Av281_Mini_project_2/blob/main/Images_for_mini_project_2/Screenshot%202023-09-13%20at%204.46.20%20PM.png"></p>

then 'make format'

### Formatting
<p align = "center"><img width="407" alt="Screenshot 2023-09-11 at 11 53 56 AM" src="https://github.com/nogibjj/Av281_Mini_project_2/blob/main/Images_for_mini_project_2/Screenshot%202023-09-13%20at%204.46.45%20PM.png"></p>

followed my 'make lint'

### Linting
<p align = "center"><img width="417" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Mini_project_2/blob/main/Images_for_mini_project_2/Screenshot%202023-09-13%20at%204.47.07%20PM.png"></p>

then, using the line 'python3 main.py', descriptive statistics are printed as shown below:

### Descriptive Stats
<p align = "center"><img width="417" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Mini_project_2/blob/main/Images_for_mini_project_2/Screenshot%202023-09-13%20at%204.47.33%20PM.png"></p>

### Data Visualization
<p align = "center"><img width="1000" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Mini_project_2/blob/main/Images_for_mini_project_2/Screenshot%202023-09-17%20at%206.07.41%20PM.png"></p>

