# Crack The Code (Temporary Name)
<p align="center">
    <img width="500" alt="Crack The Code" src="ReadMeAssets\title.png">
</p>

A game, similar to Wordle, where you should guess the number before six attempts.

## Developing

```
git clone https://github.com/lezzthanthree/DSProject.git
```

This also needs a Tkinter and pygame package.

```
pip install tkinter
```
```
pip install pygame
```

## Compiling
```
pyinstaller Main.py  --onefile --noconsole
```
The assets also needs to be moved inside the `dist` folder to work.