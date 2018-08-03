def to_euro(x):

    """Returns Euro value"""

    currency = float("{0:.2f}".format(x * 0.81))
    return currency


def to_yen(x):

    """Returns Yen value"""

    currency = float("{0:.2f}".format(x * 106.45))
    return currency


def to_peso(x):

    """Returns Peso value"""

    currency = float("{0:.2f}".format(x * 17.58))
    return currency
