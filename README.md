create env

```bash
conda create -n wineq python=3.7
```

activate env

```bash
conda activate wineq
```

create a req file

install the req

```bash
pip install -r requirements.txt
```

download data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5

git init

dvc init

dvc add_data_given/winequality.csv

git add .

git commit -m "first commit"

onliner updates for readme
git add . && git commit -m "update Readme.md"

git remode add origin https://github.com/Sree-Sharon-S/wineq.g
git branch -M main
git push origin main

git rm -r --cached 'data/raw/winequality.csv' git commit -m "stop tracking data/raw/winequality.csv"

tox command
tox

for rebuilding
tox -r

pytest command
pytest -v

setup commands
pip install -e .

build your own package commands
python setup.py sdist bdist_wheel
