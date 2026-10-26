"""The profile calculus closes on the class generated from cube cycles by
concatenation and by nesting under a single pair.

Grammar:
    W ::= w_r                (a fully crossing r-pair cycle, r >= 2)
        | W W                (concatenation)
        | a W a              (nesting under one new pair)

Predicted profile, by the three rules:
    f_{w_r}(x) = (1-x^r)/r + (1-(1-x)^r)/r
    f_{UV}     = f_U f_V
    f_{aUa}    = the constant p_T(U) = int_0^1 f_U

so every word in the class has an explicitly computable profile, and its
volume is the integral of a product of shifted polynomials.

This script generates random words from the grammar, computes the
predicted volume symbolically (exact rational integration of polynomial
products), and compares against the raw polytope volume from the engine.

Run:  python -u calculus_closure.py
"""
import sys, os, random, string
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import pairing_volume_exact

# polynomials as coefficient lists in x, exact rationals
def pmul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        if u:
            for j, v in enumerate(b):
                if v:
                    out[i + j] += u * v
    return out

def pint01(p):
    return sum(c / (i + 1) for i, c in enumerate(p))

def cycle_poly(r):
    """(1-x^r)/r + (1-(1-x)^r)/r as a coefficient list."""
    from math import comb
    p = [Fr(0)] * (r + 1)
    p[0] += Fr(1, r)
    p[r] -= Fr(1, r)
    p[0] += Fr(1, r)
    for k in range(r + 1):
        p[k] -= Fr(comb(r, k) * (-1) ** k, r)
    return p

class Node:
    def __init__(self, kind, r=None, kids=None):
        self.kind, self.r, self.kids = kind, r, kids or []

def gen(rng, depth=0):
    if depth >= 2 or rng.random() < 0.45:
        return Node("cycle", r=rng.choice([2, 2, 3, 3, 4]))
    if rng.random() < 0.5:
        return Node("cat", kids=[gen(rng, depth + 1), gen(rng, depth + 1)])
    return Node("nest", kids=[gen(rng, depth + 1)])

def profile(node):
    if node.kind == "cycle":
        return cycle_poly(node.r)
    if node.kind == "cat":
        return pmul(profile(node.kids[0]), profile(node.kids[1]))
    return [pint01(profile(node.kids[0]))]      # constant

def word(node, letters):
    if node.kind == "cycle":
        ls = [next(letters) for _ in range(node.r)]
        return "".join(ls) * 2
    if node.kind == "cat":
        return word(node.kids[0], letters) + word(node.kids[1], letters)
    a = next(letters)
    return a + word(node.kids[0], letters) + a

def wpm(w):
    pos = {}
    for i, ch in enumerate(w):
        pos.setdefault(ch, []).append(i)
    pm = [0] * len(w)
    for ch, (a, b) in pos.items():
        pm[a], pm[b] = b, a
    return tuple(pm)

def main():
    rng = random.Random(20260824)
    alphabet = string.ascii_letters
    ok = bad = 0
    for trial in range(14):
        node = gen(rng)
        letters = iter(alphabet)
        try:
            w = word(node, letters)
        except StopIteration:
            continue
        if len(w) > 22:
            continue
        pred = pint01(profile(node))
        got = pairing_volume_exact(wpm(w), "T")
        match = (pred == got)
        ok += match
        bad += (not match)
        print(f"{w:<24} predicted {str(pred):<12} engine {str(got):<12} "
              f"{'OK' if match else 'MISMATCH'}", flush=True)
    print(f"\n{ok} match, {bad} mismatch")
    if bad == 0:
        print("THE CALCULUS CLOSES on the generated class")

if __name__ == "__main__":
    main()
