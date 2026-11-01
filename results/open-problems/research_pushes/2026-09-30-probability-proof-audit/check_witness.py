"""Exact finite constants only; does not verify the analytic theorem."""
from fractions import Fraction as F
from math import factorial
import json

r = F(1, 32)
def derivative(x):
    return (x-r)/(x*x*(1-x))
assert derivative(r) == 0
assert derivative(2*r) == F(128, 15)
assert derivative(F(1, 2)) == F(15, 4)
exp_lower = sum((F(11, 4)**k/F(factorial(k)) for k in range(7)), F(0))
assert exp_lower == F(9019421, 589824) and exp_lower > 15
harnack_margin = F(121,180)-F(95,124)**2
assert harnack_margin == F(58999,691920) and harnack_margin > 0
valley_margin = F(9,20)*derivative(2*r)-derivative(F(1,2))
assert valley_margin == F(9,100)
print(json.dumps({"status":"PASS", "r":str(r), "exp_lower":str(exp_lower),
    "harnack_margin":str(harnack_margin), "valley_margin":str(valley_margin),
    "scope":"Exact finite constants, not a formal proof of analytic claims"}, indent=2))
