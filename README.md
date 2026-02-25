# Applying quantum techniques on calcium imaging data to uncover co-activation patterns and community structure within neurons

## Getting started

Clone the Repository:
```
git clone https://github.com/c-carolinel/jc.git
cd jc
```

## Branching guidelines

Start from the develop branch:
```
git checkout develop
git pull origin develop
```

Add files and commit
```
git add 'filename'
git commit -m 'description'
```

Push your commits onto the develop branch:
```
git push origin develop
```

## Using the virtual environment (venv)

Create venv
```
python -m venv myenv
```

Activate the venv
```
source venv/bin/activate
```

Register kernel with Jupyter
```
pip install ipykernel
python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"
```

### Requirements

Generate requirements.txt
```
pip freeze > requirements.txt
```

Download packages from requirements.txt
```
pip install -r requirements.txt
```
