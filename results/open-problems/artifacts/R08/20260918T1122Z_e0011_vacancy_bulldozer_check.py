#!/usr/bin/env python3
"""
Exact finite checker for R08 / E0011 vacancy-bulldozer lemma.

State values: 0=vacant, 1=CO, 2=O.
Patch: active 2x3 rectangle x in {-1,0,1}, y in {0,1},
plus its nearest-neighbor boundary (16 sites total).

Initial assumption: the 2x2 window x in {-1,0}, y in {0,1} is vacant.
All other local sites are arbitrary, subject only to r=infinity stability:
there is no adjacent CO/O pair.

Tie rule: for a newly adsorbed particle with multiple opposite-type neighbors,
choose the first available neighbor in fixed priority E,W,N,S. This is one
specific positive-probability tie-break outcome in the source process.

Claim checked: after the fixed 12-mark word below, the translated 2x2 window
x in {0,1}, y in {0,1} is vacant for every stable local environment.
"""

from itertools import product

DIRS = ((1,0),(-1,0),(0,1),(0,-1))  # E,W,N,S
ACTIVE = {(x,y) for x in (-1,0,1) for y in (0,1)}
CELLS = set(ACTIVE)
for x,y in tuple(ACTIVE):
    for dx,dy in DIRS:
        CELLS.add((x+dx,y+dy))
CELLS = tuple(sorted(CELLS))
IDX = {c:i for i,c in enumerate(CELLS)}

FIXED_VACANT = {(-1,0),(-1,1),(0,0),(0,1)}
VARIABLE = tuple(c for c in CELLS if c not in FIXED_VACANT)

WORD = (
    ("CO", (1,0)),
    ("CO", (0,0)),
    ("CO", (1,0)),
    ("CO", (0,0)),
    ("CO", (1,0)),
    ("CO", (0,1)),
    ("CO", (0,1)),
    ("CO", (0,0)),
    ("O2", ((-1,0),(-1,1))),
    ("O2", ((0,0),(0,1))),
    ("CO", (-1,0)),
    ("CO", (-1,1)),
)

TARGET = {(0,0),(0,1),(1,0),(1,1)}

def stable(s):
    for x,y in CELLS:
        a = s[IDX[(x,y)]]
        for dx,dy in ((1,0),(0,1)):  # each edge once
            q=(x+dx,y+dy)
            if q in IDX:
                b=s[IDX[q]]
                if (a==1 and b==2) or (a==2 and b==1):
                    return False
    return True

def co_action(s, c):
    s=list(s)
    i=IDX[c]
    if s[i] != 0:
        return tuple(s)
    s[i]=1
    x,y=c
    for dx,dy in DIRS:
        q=(x+dx,y+dy)
        if q in IDX and s[IDX[q]]==2:
            s[i]=0
            s[IDX[q]]=0
            break
    return tuple(s)

def o2_action(s, a, b):
    s=list(s)
    ia,ib=IDX[a],IDX[b]
    if s[ia] != 0 or s[ib] != 0:
        return tuple(s)
    s[ia]=2
    s[ib]=2
    # Each newly attached oxygen is allowed one instantaneous reaction.
    # Endpoint order does not affect this word, but is fixed for determinism.
    for c in (a,b):
        i=IDX[c]
        if s[i] != 2:
            continue
        x,y=c
        for dx,dy in DIRS:
            q=(x+dx,y+dy)
            if q in IDX and s[IDX[q]]==1:
                s[i]=0
                s[IDX[q]]=0
                break
    return tuple(s)

def apply_word(s):
    for kind,arg in WORD:
        if kind=="CO":
            s=co_action(s,arg)
        else:
            s=o2_action(s,*arg)
    return s

def main():
    assert len(CELLS)==16
    assert len(VARIABLE)==12
    total=0
    stable_count=0
    final_stable_count=0
    for vals in product((0,1,2), repeat=len(VARIABLE)):
        total += 1
        s=[0]*len(CELLS)
        for c,v in zip(VARIABLE,vals):
            s[IDX[c]]=v
        s=tuple(s)
        if not stable(s):
            continue
        stable_count += 1
        t=apply_word(s)
        if stable(t):
            final_stable_count += 1
        else:
            raise AssertionError(("final state not stable", s, t))
        if any(t[IDX[c]] != 0 for c in TARGET):
            raise AssertionError(("target window not vacant", s, t))
    assert total == 3**12 == 531441
    assert stable_count == 50785
    assert final_stable_count == stable_count
    print("PASS exact exhaustive vacancy-bulldozer check")
    print(f"local_cells={len(CELLS)} variable_cells={len(VARIABLE)}")
    print(f"assignments={total} stable_assignments={stable_count}")
    print(f"word_length={len(WORD)}")
    print("initial_vacancy_window=[-1,0]x[0,1]")
    print("final_vacancy_window=[0,1]x[0,1]")
    print(f"all_{stable_count}_stable_environments_pass=True")

if __name__ == "__main__":
    main()
