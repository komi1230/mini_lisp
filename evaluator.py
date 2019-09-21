from environment import Env
from environment import add_globals

global_env = add_globals(Env())
Symbol = str
isa = isinstance


def my_eval(x, env):
    # Check symbol ?
    if isa(x, Symbol):

        return env.find(x)[x]

    # Check list ?
    elif not isa(x, list):

        return x                

    # (quote exp)
    elif x[0] == 'quote':
        (_, exp) = x

        return exp

    # (if test conseq alt)
    elif x[0] == 'if': 
        (_, test, conseq, alt) = x

        return eval((conseq if eval(test, env) else alt), env)

    # (set! var exp)
    elif x[0] == 'set!': 
        (_, var, exp) = x
        env.find(var)[var] = eval(exp, env)

    # (define var exp)
    elif x[0] == 'define':
        (_, var, exp) = x
        env[var] = eval(exp, env)

    # (lambda (var*) exp)
    elif x[0] == 'lambda': 
        (_, vars, exp) = x

        return lambda *args: eval(exp, Env(vars, args, env))

    # (begin exp*)
    elif x[0] == 'begin': 
        for exp in x[1:]:
            val = eval(exp, env)

        return val

    # (proc exp*)
    else:
        exps = [my_eval(exp, env) for exp in x]
        proc = exps.pop(0)

        return proc(*exps)
