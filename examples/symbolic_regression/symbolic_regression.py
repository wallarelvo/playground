#!/usr/bin/env python
import sys
import os
import time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

import playground.config as config
import playground.play as play
from playground.gp_tree.tree_generator import TreeGenerator
from playground.gp_tree.tree import TreeEvaluator
from playground.gp_tree.tree_evaluation import evaluate
from playground.functions import FunctionRegistry
from playground.operators.selection import Selection
from playground.operators.crossover import GPTreeCrossover
from playground.operators.mutation import GPTreeMutation

# SETTINGS
config_fp = "config.json"


if __name__ == '__main__':
    # setup
    config = config.load_config(config_fp)

    functions = FunctionRegistry()
    evaluator = TreeEvaluator(config, functions)
    tree_generator = TreeGenerator(config, evaluator)

    # genetic operators
    selection = Selection(config)
    crossover = GPTreeCrossover(config)
    mutation = GPTreeMutation(config)

    random.seed(10)  # seed random so results can be reproduced

    # run symbolic regression
    start_time = time.time()
    population = tree_generator.init()

    # play.play(population, selection, crossover, mutation, config)
    play.play_multicore(
        population,
        functions,
        evaluate,
        selection,
        crossover,
        mutation,
        config
    )

    end_time = time.time()
    print("GP run took: %2.2fsecs\n" % (end_time - start_time))
