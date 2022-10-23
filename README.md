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
