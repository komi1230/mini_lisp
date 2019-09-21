import sys
from environment import Env
from environment import add_globals


def check_string(x):
    if isinstance(x, str):
        return x[0] == x[-1] == '"' or not '"' in x[1:-2]
    else:
        return False

def my_eval(x, env):
    print("Here x is : ", x)

    # Check symbol ?
    if isinstance(x, str):

        return env.find(x)[x]

    # Check list ?
    elif not isinstance(x, list):

        return x                

    # (quote exp)
    elif x[0] == 'quote':
        (_, exp) = x

        return exp

    # (if test conseq alt)
    elif x[0] == 'if': 
        (_, test, conseq, alt) = x

        if my_eval(test, env):
            return my_eval(conseq, env)

        else:
            return my_eval(alt, env)


    # (set! var exp)
    elif x[0] == 'set!': 
        (_, var, exp) = x
        env.find(var)[var] = my_eval(exp, env)

    # (define var exp)
    elif x[0] == 'define':
        (_, var, exp) = x
        if check_string(exp):
            env[var] = exp
        else:
            env[var] = my_eval(exp, env)

    # (lambda (var*) exp)
    elif x[0] == 'lambda': 
        (_, vars, exp) = x

        return lambda *args: my_eval(exp, Env(vars, args, env))

    # (exit)
    elif x[0] == 'exit':
        sys.exit("bye")

    # (begin exp*)
    elif x[0] == 'begin': 
        for exp in x[1:]:
            val = my_eval(exp, env)

        return val

    # (proc exp*)
    else:
        exps = [my_eval(exp, env) for exp in x]
        proc = exps.pop(0)

        return proc(*exps)
