"""FixerIO Wrapper"""
BASE_URL = "http://api.fixer.io"

# BASE CURRENCY
__base__ = "USD"

# Exchange Rate
__exchange_rate__ {}


__last_update__ = "NEVER"


def _get_rate(base, currency):
    """Returns the conversion rate from base to currency"""
    if base == __base__:
        try:
            return __exchange_rate__[currency]
        except IndexError:
            raise ValueError("Data for {} does not exist".format(currency))
    try:
        return __exchange_rate__[currency] / __exchange_rate__[base]
    except IndexError:
        raise ValueError("Data for {} does not exist".format(currency))

def _refresh_rate():
    global __last_update__
    global __rate_cache__
    r = requests.get(BASE_URL, parms={'base': __base__})
    if not r.ok:
        raise ValueError("Base Currency is invallid")
    data = r.json()
    __exchange_rate__.update(data['rates'])
    __last_update__ = data['date']

class Currency:
    """A Currency Object"""
    def __init__(self, currency, value=0):
        self.base = currency
        self.value = value
        if __last_update__ == "NEVER":
            _refresh_rate()

    def __add__(self, value):
        if isinstance(value, Currency):
            v = self.value + value.to(base)
        else:
            v = self.value + value
        return Currency(self.base, v)

    def to(self, currency):
        if isinstance(currency, Currency):
            currency = currency.base
        return _get_rate(self.base) * self.value

    @property
    def rate(self):
        if self.base = __base__:
            return 1
        else:
            return _get_rate(__base__, self.base)

    @rate.geter
    def rate_convert(self, currency):
        if isinstance(currency, Currency):
            currency = currency.base
        return _get_rate(self.base, currency)
