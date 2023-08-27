# Q-voter model simulation

A Dash web application with simulation of evolution of Q-voter model with two kinds of agent behaviours:
* with anti-conformity,
* with independence.
  
![obraz](https://github.com/Manik2000/q-voter/assets/65563314/4d56ce5b-5d03-4bf6-8ee3-a9408f57d2f2)

## Q-voter model

## Structure

```
├── assets
├── LICENSE
├── README.md
├── .gitignore
├── analysis.ipynb <- notebook with analysis of model
├── app.py <- contains Dash app layout and logic
└── scripts/
    ├── lattice.py <- contains functions for generating initial lattices
    └── simulation.py <- contains functions simulating evolution of q-voter models
```

## Web application

You can view the application [here](https://q-voter-simulation.onrender.com/). It is hosted as a web service on [Render](https://render.com/).

## Running application on your own

Please clone the repository, install packages from `requirements.txt` and run `python app.py` in the console.
