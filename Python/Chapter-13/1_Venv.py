# Virtual environments in Python allow you to create isolated spaces so that you can have different versions of packages for different projects without conflicts.

import pandas as pd
print(pd.__version__)

# To create and activate a virtual environment, you can use the following commands in your terminal:
# python -m venv myenv. Creates a virtual environment named 'myenv'
# myenv\Scripts\activate. Activates the virtual environment

# pip freeze. Lists all installed packages in the current environment

# pip freeze > requirements.txt. Saves the list of installed packages to a file
# pip install -r requirements.txt. Installs packages from the requirements file
# deactivate. Deactivates the virtual environment


