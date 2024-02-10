## Setup

I'm using Ubuntu so you may want to use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install), but Windows is fine for all of this -- there are mainly just CLI differences. You should at least use [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4) instead of CMD.

[Install Python](https://www.python.org/downloads/) and install [git](https://git-scm.com/downloads) if needed. Ensure that you can run `python` command as well as `git`.

Clone this repo:

```
cd ./example-clone-path # or wherever you are cloning to
git clone https://github.com/parsehex/python-learning
cd python-learning
```

Create and enter a new [virtual environment](https://docs.python.org/3/library/venv.html):

```
python -m venv .venv

# if on Windows and PowerShell (use .bat if CMD):
./.venv/Scripts/Activate.ps1

# Mac / Linux:
source ./.venv/bin/activate
```

Finally, install dependencies:

```
pip install -r requirements.txt
```

## Topics to Cover

- Pandas
- [pywin32](https://pypi.org/project/pywin32/) / make a lib at least
  - pywin32 is a package that provides access to various Windows APIs, one of which being Excel's Win32 COM API.
    - This essentially lets you call and use the same functions and objects that you do via VBA. This way, we write Python that interfaces with these things.
    - See [this SO answer](https://stackoverflow.com/a/39880844) for good info and an example on controlling excel via python in this mannaer.
  - Create module to abstract vba details away
- Jupyter notebooks
  - These are good for trying out a section of code or exploring data. You can see the outputs of your code inline with the code itself, so it's a very nice additional way to work with Python.
    - An important note is that we don't want to commit any data from the results of the notebooks to github. See [this SO answer](https://stackoverflow.com/a/74753885) for a git commit hook that will remove outputs from notebooks before commiting.
    - An alternative that doesn't store outputs to begin with, lets you make a notebook out of a `.py` file is [Jupytext](https://github.com/mwouts/jupytext)
- Tkinter
  - Create a DataFrame Table reusable component (`./tkinter/apps/DF_test.py`)
