# playground [![Build Status](https://travis-ci.org/chutsu/playground.png)][1]
Playground is a Gentic Programming framework implemented in Python. Currently
features:

- Genetic Programming in Trees
- Tree Genetic Operators:
    - Selection
        - Roulette wheel selection
        - Tournament selection
    - Crossover
        - One point crossover
    - Mutation
        - Point mutation
        - Hoist mutation
        - Subtree mutation
        - Shrink mutation
        - Expand mutation
- Multicore Evaluation
- Multinode Evaluation (experimental)
- JSON config files
- Ability to record evolution process to database (PostgreSQL or JSON flat
  file)


## Requirements

- Python (version 2.7 +)
- sympy (version 0.7.3 +)

## Install

Currently the best way is to clone the repo and install the dependencies:

    git clone git@github.com:chutsu/playground.git
    pip install -r requirements.txt  # installs dependencies for playground

To see playground in action, checkout the `examples` folder, at the moment
the best example is the [symbolic regression][4] example.
([what is symbolic regression?][3]):

    cd examples/symbolic_regression
    python symbolic_regression.py
    # alternatively you can run the example with PyPy, it might be faster :)
    pypy symbolic_regression.py

The example uses data in `examples/symbolic_regression/sine.dat` to find the
answer (an equation), this is also an example of data-driven search.

More examples to follow, it can solve alot of other problems, such as
evolving digital circuits, neural nets, etc ... :)


## Optional Requirements

If you want evolution recording (such as fitness/evaluation score vs time):

- PostgreSQL (version 9.3 +)
- Psycopg2 (version 2.5 +)


## Licence
LGPL License
Copyright (C) <2013> Chris Choi

This program is free software: you can redistribute it and/or modify it under
the terms of the Lesser GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.

[![](https://d2weczhvl823v0.cloudfront.net/chutsu/playground/trend.png)][2]

[1]: https://travis-ci.org/chutsu/playground
[2]: https://bitdeli.com/free
[3]: http://www.symbolicregression.com/?q=faq
[4]: https://github.com/chutsu/playground/tree/master/examples/symbolic_regression
