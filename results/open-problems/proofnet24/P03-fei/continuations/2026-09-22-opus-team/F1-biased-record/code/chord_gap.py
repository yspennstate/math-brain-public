"""Chord-interpolation gap near 1/2: at points midway between grid nodes, compare the chord value V(p) used by the
iteration with the best one-step composition value T(V)(p) (AND/OR splits, pair g-families, uniform-core g) computed
directly at p.  T(V)(p) > V(p) means the iteration prices inputs below anything one more composition step achieves.
Usage: python chord_gap.py <vig npz>"""
import sys
import numpy as np
import trace_policy as TP

ps = [0.5 - (k + 0.5) / 2048 for k in range(0, 12)]
print("p          chord V - C     best one-step T(V) - C    gap T - chord")
for p in ps:
    ch = TP.V(p)[0] - TP.C
    best = TP.moves(p)[0][0] - TP.C
    print("%.7f   %+.4e      %+.4e            %+.3e" % (p, ch, best, best - ch), flush=True)
