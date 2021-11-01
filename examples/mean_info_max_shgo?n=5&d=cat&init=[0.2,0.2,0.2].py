from runthis import parse_kwargs


def my_experiment(n,d,init):
    return int(n)


if __name__=='__main__':
    import os
    kwargs = parse_kwargs(__file__.split(os.path.sep)[-1])
    my_experiment(**kwargs)