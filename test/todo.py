"""Incomplete fixes."""


# E501: This should be wrapped similar to how pprint does it
{'2323k2323': 24232323, '2323323232323': 3434343434343434, '34434343434535535': 3434343434343434, '4334343434343': 3434343434}
# See below
{'2323323232323': 3434343434343434,
 '2323k2323': 24232323,
 '34434343434535535': 3434343434343434,
 '4334343434343': 3434343434}

# W601: Handle complicated cases
x = {1: 2}
y = {}
y.has_key(0) + x.has_key(x.has_key(0) + x.has_key(x.has_key(0) + x.has_key(1)))

# E702: Indent correctly when breaking at semicolon
(
    1,
    2,
    3); 4; 5; 5  # pyflakes
