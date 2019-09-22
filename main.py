from __future__ import division
import math, sys, os
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



GLOBAL_ENV = add_globals(Env())

if "-d" in sys.argv:
    DEBUG_MODE = True
else:
    DEBUG_MODE = False

    

def repl(prompt='>>> ', debug=False):

    if debug:
        while True:
            input_seq = input(prompt)

            if input_seq is "":
                continue

            parsed_seq = parse(input_seq)
            print("Parsed seq : ", parsed_seq)
            val = my_eval(parsed_seq, env=GLOBAL_ENV)
            print("Evaluation : ", val)

            if val is not None:
                 print(to_string(val))
            else:
                 continue

    else:
        while True:
            input_seq = input(prompt)

            if input_seq is "":
                continue

            parsed_seq = parse(input_seq)
            val = my_eval(parsed_seq, env=GLOBAL_ENV)

            if val is not None:
                 print(to_string(val))
            else:
                 continue


if __name__ == "__main__":
    repl(debug=DEBUG_MODE)
