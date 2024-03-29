# Q-voter model simulation

A Dash web application with simulation of evolution of Q-voter model with two kinds of agent behaviours:
* with anti-conformity,
* with independence.
  
![obraz](https://github.com/Manik2000/q-voter/assets/65563314/4d56ce5b-5d03-4bf6-8ee3-a9408f57d2f2)

## Q-voter model

Q-voter model is a model of binary opinion dynamics (agent opinion is either $+1$ or $-1$). Each agent (a member of some society) can be influenced by their $q$ neighbours. If the neighbours' opinion are consistent, then the agent adopts this opinion. Otherwise, the agents keeps their opinion.

However, some we can introduce some agent behaviours:
* **anti-conformity** &mdash; if the neighbours' opinions are consistent, then the agent adopts the opposite opinion with some probabilty $p$,
* **independence** &mdash; the agent becomes independent with probability $p$ and flips its opinon with probability $f$.

In this app q-voter model evolution is simulated on a square lattice with periodic boundary conditions. There are different kinds of lattices &mdash; see image below.

![](assets/lattices.png)

## Structure

```
├── assets
├── LICENSE
├── README.md
├── .gitignore
├── app.py <- contains Dash app layout and logic
└── scripts/
    ├── lattice.py <- contains functions for generating initial lattices
    └── simulation.py <- contains functions simulating evolution of q-voter models
```

## Web application

You can view the application [here](https://q-voter-simulation.onrender.com/). It is hosted as a web service on [Render](https://render.com/).

## Running application on your own

Please clone the repository, install packages from `requirements.txt` and run `python app.py` in the console.
