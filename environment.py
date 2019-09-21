from __future__ import division
import math
import operator as op


class Env(dict):
    def __init__(self, parms=(), args=(), outer=dict):
        self.update(zip(parms, args))
        self.outer = outer

    def find(self, var):
        if var in self:
            return self

        else:
            return self.outer

    
def add_globals(env):
    env.update(vars(math))
    env.update({
        '+':op.add,
        '-':op.sub,
        '*':op.mul,
        '/':op.truediv,
        'not':op.not_,
        '>':op.gt,
        '<':op.lt,
        '>=':op.ge,
        '<=':op.le,
        '=':op.eq,
        'equal?':op.eq,
        'eq?':op.is_,
        'length':len,
        'cons':lambda x,y: [x]+y,
        'car':lambda x: x[0],
        'cdr':lambda x: x[1:],
        'append':op.add,
        'list':lambda *x: list(x),
        'list?': lambda x: isinstance(x,list),
        'null?':lambda x: x == [],
        'symbol?':lambda x: isinstance(x, str)
    })
    
    return env
