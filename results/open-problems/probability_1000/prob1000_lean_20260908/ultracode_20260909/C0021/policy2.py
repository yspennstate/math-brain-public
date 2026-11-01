from dp_exact import *
from fractions import Fraction
def show(t):
    if t in ('u','+','-'): return t
    return '['+' '.join(show(c) for c in t)+']'
def best_moves(t):
    opts=[]
    for (a,b) in queries(t):
        opts.append((1+(V(a)+V(b))/2,a,b))
    m=min(o[0] for o in opts)
    return [o for o in opts if o[0]==m], opts
seen=set()
def walk(t,depth=0):
    if t in ('+','-') or t in seen: return
    seen.add(t)
    bm,opts=best_moves(t)
    print('  '*depth+f"{show(t)}  V={V(t)} ({float(V(t)):.4f})  optimal moves:")
    for v,a,b in bm:
        print('  '*depth+f"    -> +: {show(a)} (V={float(V(a)):.4f})   -: {show(b)} (V={float(V(b)):.4f})")
    others=[o for o in opts if o[0]!=bm[0][0]]
    for v,a,b in others:
        print('  '*depth+f"    (worse {float(v):.4f}) +: {show(a)}  -: {show(b)}")
    for v,a,b in bm[:1]:
        walk(a,depth+1); walk(b,depth+1)
walk(full(2))
