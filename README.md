# fourier_py

## Summary

### How to start

1. Record your voice with an app to .wav (like `Sound Recorder` in Windows Store)
2. Open file

## Util commands

### Initialize git repository

```bash
rm -rf .git
git init
git add --all
git commit -m "first commit"
git branch -m master main
git remote add origin git@github.com:adriatp/fourier_py.git
git push origin main --force
```

### Initialize virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### Push changes to origin

```bash
git add --all
git commit -m "next commit"
git push origin main
```

