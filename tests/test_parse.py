

def test_parse_str():
    from runthis.conventions import parse_kwargs
    kwargs = parse_kwargs(s='func?a=17&b=34&c=55')
    assert kwargs.get('c')=='55'


def test_parse_int():
    from runthis.conventions import parse_kwargs
    kwargs = parse_kwargs(s='func?a=17&b=float:34&c=int:55')
    assert kwargs.get('c')==55
    assert isinstance(kwargs.get('c'),int)
    assert kwargs.get('b') == 34.0
    assert isinstance(kwargs.get('b'), float)


if __name__=='__main__':
    test_parse_int()