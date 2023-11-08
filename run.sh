#!/bin/bash
#automate netlas nuclei scan

# Run python3 main.py
python3 main.py

# Check if python3 main.py ran successfully
if [[ $? -ne 0 ]]; then
  echo "python3 main.py failed to run successfully."
  exit 1
fi

#httpx
cat lol.txt | ./httpx > output.txt


if [[ $? -ne 0 ]]; then
  echo "Failed"
  exit 1
fi

# Run nuclei
nuclei -l output.txt -v -severity high,critical -c 50
