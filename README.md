## Setup

## Topics to Cover

- Pandas
- [pywin32](https://pypi.org/project/pywin32/) / make a lib at least
  - pywin32 is a package that provides access to various Windows APIs, one of which being Excel's Win32 COM API.
    - This essentially lets you call and use the same functions and objects that you do via VBA. This way, we write Python that interfaces with these things.
    - See [this SO answer](https://stackoverflow.com/a/39880844) for good info and an example on controlling excel via python in this mannaer.
  - Create module to abstract vba details away
- Jupyter notebooks
  - These are good for trying out a section of code or exploring data. You can see the outputs of your code inline with the code itself, so it's a very nice additional way to work with Python.
    - An important note is that we do not want to commit any data from the results of the notebooks to github. See [this SO answer](https://stackoverflow.com/a/74753885) for a git commit hook that will remove outputs from notebooks before commiting.
    - An alternative that doesn't store outputs to begin with, lets you make a notebook out of a `.py` file is [Jupytext](https://github.com/mwouts/jupytext)
- Tkinter
  - Attempt to create a DataFrame Table reusable component
