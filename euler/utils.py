def take_while(seq, test):
    """
    yields sequence items while test is true. Does not preserve first item that
    fails test in seq.
    :param seq:
    :param test:
    :return:
    """
    for i in seq:
        if test(i):
            yield i
        else:
            break
