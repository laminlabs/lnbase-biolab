import lnschema_core


def biosample() -> str:
    """Pipeline: 21 base62.

    21 characters (62**21=4e+37 possibilities) outperform UUID (2*122=5e+36).
    """
    return lnschema_core.id.base62(n_char=21)


def techsample() -> str:
    """Pipeline: 21 base62.

    21 characters (62**21=4e+37 possibilities) outperform UUID (2*122=5e+36).
    """
    return lnschema_core.id.base62(n_char=21)
