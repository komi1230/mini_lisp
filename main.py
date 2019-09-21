from __future__ import division
import math
import operator as op

from environment import Env
from environment import add_globals
from evaluator import my_eval
from parser import (
    parse,
    tokenize,
    read_from,
    atom,
    to_string
)



global_env = add_globals(Env())


def repl(prompt='>>> '):

    while True:
        val = my_eval(parse(input(prompt)), env=global_env)
        if val is not None:
            print(to_string(val))


if __name__ == "__main__":
    repl()
