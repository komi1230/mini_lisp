from __future__ import division
import math
import operator as op


class Env(dict):
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms,args))
        self.outer = outer

    def find(self, var):

        return self if var in self else self.outer.find(var)

    
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
        'list?': lambda x: isa(x,list),
        'null?':lambda x: x == [],
        'symbol?':lambda x: isa(x, Symbol)
    })
    
    return env
