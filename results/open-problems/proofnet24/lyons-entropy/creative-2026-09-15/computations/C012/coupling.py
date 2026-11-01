"""Explicit global two-parameter Fourier diamond coupling.

The exact construction accepts rational (x,y,z) coordinates. The CLI accepts
angles and prints a numerical evaluation; its mathematical proof is in C012.md.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, math, argparse
from exact_core import sign_action, act_weights, TAU

CERT = json.loads((Path(__file__).resolve().parent/'certificate.json').read_text())
CUBE = [F(n, CERT['cube']['denominator']) for n in CERT['cube']['numerators']]
TIP = [F(n, CERT['tip']['denominator']) for n in CERT['tip']['numerators']]
VERTEX_WEIGHTS = {s: sign_action(CUBE, *s) for s in product((-1,1), repeat=3)}
VERTEX_WEIGHTS[(0,0,2)] = TIP
VERTEX_WEIGHTS[(0,0,-2)] = act_weights(TIP, TAU)

def barycentric(x, y, z):
    """Nonnegative vertex masses on conv([-1,1]^3, (0,0,+/-2)).

    Formula is exact for Fractions. Its domain is |x|,|y|<=1 and
    |x|+|z|<=2, |y|+|z|<=2. Every physical ellipsoid point is in this domain.
    """
    if abs(z) <= 1:
        return {(sx,sy,sz): (1+sx*x)*(1+sy*y)*(1+sz*z)/8
                for sx,sy,sz in product((-1,1), repeat=3)}
    eps = 1 if z > 0 else -1
    lam = 2-abs(z)
    if lam == 0:
        if x != 0 or y != 0: raise ValueError('Outside the transport polytope')
        return {(0,0,2*eps): F(1)}
    out = {(sx,sy,eps): lam*(1+sx*x/lam)*(1+sy*y/lam)/4
           for sx,sy in product((-1,1), repeat=2)}
    out[(0,0,2*eps)] = 1-lam
    return out

def weights_at_coordinates(x, y, z):
    masses = barycentric(x,y,z)
    return [sum(v*VERTEX_WEIGHTS[key][i] for key,v in masses.items()) for i in range(90)]

def weights(theta, phi):
    point = (math.cos(2*theta), math.sin(2*theta)*math.cos(phi),
             math.sqrt(3)*math.sin(2*theta)*math.sin(phi))
    return point, weights_at_coordinates(*point)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--theta', type=float, default=math.atan(F(2,3)))
    parser.add_argument('--phi', type=float, default=math.pi/3)
    args = parser.parse_args()
    point, w = weights(args.theta,args.phi)
    print(json.dumps({'theta':args.theta,'phi':args.phi,'coordinates':point,
                      'minimum_weight':min(w),'total_weight':sum(w),
                      'weight_indexing':'certificate.json diamonds', 'weights':w}, indent=2))
