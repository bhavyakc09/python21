name: Read input from Excel

on:
  push:
  pull_request:
    types: [opened, reopened, synchronize]

jobs:
  read-input:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install openpyxl
        run: pip install openpyxl
      - name: Run main.py
        run: python main.py
