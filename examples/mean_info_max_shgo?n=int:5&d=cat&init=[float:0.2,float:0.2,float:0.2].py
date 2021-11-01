from runthis import parse_kwargs
from pprint import pprint


def my_experiment(n,d,init):
    assert isinstance(n,int)


if __name__=='__main__':
    import os
    kwargs = parse_kwargs(__file__.split(os.path.sep)[-1])
    my_experiment(**kwargs)
    pprint(kwargs)