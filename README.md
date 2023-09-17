# No Spoilers Backend

Python backend portion of no spoilers! application.

## Setup

```bash
python3 -m pip
pip3 install poetry
poetry config virtualenvs.in-project true
poetry install
```

Visual Studio Code > Select Interpreter > Python 3.11.5 (.venc: poetry)

Add an `.env` file to the project root in the following format (ask for username:password and @cluster):

```bash
MONGO_URI=mongodb+srv://username:password@cluster0.1234.mongodb.net/
```
