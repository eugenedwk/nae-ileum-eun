# Romanize - a Romanization Service API
Currently supported for Korean names only


## Prerequisites
- python v3.10.8
- pip 22.3.1

## Quickstart
```bash
$ python main.py
```

## Developer Environment Setup
1. Ensure you're on a unix-like operating system (MacOS, Ubuntu, etc.)
   - If using windows, try WSL2 (windows subsystem for linux): https://learn.microsoft.com/en-us/windows/wsl/install
2. Download the appropriate `Miniconda` installer for your computer
https://docs.conda.io/en/main/miniconda.html
1. Move the downloaded `.sh` installer file in your home directory.
    - To find the path to your home directory, run the following:
        ```bash
        $ cd ~
        $ pwd
        ```
2. Run the `.sh` installer file
```bash
$ bash Miniconda3-latest-*.sh
```
   - Follow the prompts on the installer screens.
   - If you are unsure about any setting, accept the defaults. You can change them later.
   - To make the changes take effect, close and then re-open your terminal window.
   - Test your installation. In your terminal window or Anaconda Prompt, run the following (a list of installed packages appears if it has been installed correctly):
```bash
$ conda list
``` 
3. Create a virtual environment for this project
```bash
$ conda create -n venv-romanize python=3.10.8
```
4. Activate the virtual environment
```bash
$ conda activate venv-romanize
```
5. Install the necessary packages for this project
```bash
$ cd api/
$ pip install -r requirements.txt
```