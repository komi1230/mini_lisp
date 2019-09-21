def tokenize(s):

    return s.replace('(', ' ( ').replace(')', ' ) ').split()


def read_from(tokens):

    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')

    token = tokens.pop(0)

    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from(tokens))
        tokens.pop(0) # pop off ')'

        return L

    elif ')' == token:
        raise SyntaxError('unexpected )')

    else:
        return atom(token)
    

def parse(s):

    return read_from(tokenize(s))

    
def atom(token):
    try:
        return int(token)

    except ValueError:
        try:
            return float(token)

        except ValueError:
            return str(token)

        
def to_string(exp):
    if isinstance(exp, list):
        return  '('+' '.join(map(to_string, exp))+')'

    else:
        return str(exp)
