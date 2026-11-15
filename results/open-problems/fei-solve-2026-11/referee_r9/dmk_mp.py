import mpmath as mp
from tower_recompute import PM, T, dual, table
from tower_recompute_mp import compose
mp.mp.dps = 40
M, D = (table(*PM(3)), 9), (table(*dual(PM(3))), 9)
T26, T36 = (table(*T(2, 6)), 12), (table(*T(3, 6)), 18)
st = (mp.mpf(0), mp.mpf(0), mp.mpf(1), mp.mpf(0), mp.mpf(1))
st, r, _ = compose(st, *D)
for k in range(1, 14):
    st, r, err = compose(st, *M)
    line = f"D,M^{k:<2d} plain {mp.nstr(r, 22)} mean {mp.nstr(st[0], 8)}"
    if k in (8, 9):
        line += f"  +T26 {mp.nstr(compose(st, *T26)[1], 22)}"
    if k == 10:
        line += f"  +T36 {mp.nstr(compose(st, *T36)[1], 22)}"
    print(line, flush=True)
