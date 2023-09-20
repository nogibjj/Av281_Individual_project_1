# Continuous Integration using GitHub Actions of Python Data Science Project
[![OnInstall](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/test.yml)
[![Format](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/lint.yml)
[![Continuous Delivery](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/run.yml/badge.svg)](https://github.com/nogibjj/Av281_Individual_project_1/actions/workflows/run.yml)

My project utilizes the "Auto.csv" dataset for data visualizations, and the "nba.csv" dataset for testing purposes. The goal of this project is to test and display the exploratory data analysis functions in lib.py created using pandas. The github actions workflow makes sure that upon each push, the code undergoes linting, formatting, installing dependencies, and testing of the entire project (python script and Jupyter notebook).

## Video Link:
- https://youtu.be/0_4KWPFAijw

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
The lib.py script contains the function definitions used in both main.py, desc_stats.ipynb and all the test scripts.

## Workflow



### Testing
<p align = "center"><img width="1000" alt="Screenshot 2023-09-11 at 11 53 56 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/test_1.png"></p>
<p align = "center"><img width="1000" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/test_2.png"></p>

### Formatting
<p align = "center"><img width="1000" alt="Screenshot 2023-09-11 at 11 53 56 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/format.png"></p>


### Linting
<p align = "center"><img width="1000" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/lint.png"></p>


### Run: Descriptive Stats (main.py)
<p align = "center"><img width="1000" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/main.png"></p>

## Data Visualizations
#### Count of each unique value in a specified column:
<p align = "center"><img width="800" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/count.png"></p>

#### Boxplot of a specified column:
<p align = "center"><img width="800" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/box.png"></p>

#### Histogram of a specified column:
<p align = "center"><img width="800" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/hist.png"></p>

#### Heatmap of correlation matrix of dataset:
<p align = "center"><img width="800" alt="Screenshot 2023-09-11 at 11 55 09 AM" src="https://github.com/nogibjj/Av281_Individual_project_1/blob/main/images_for_Individual_project_1/heatmap.png"></p>
