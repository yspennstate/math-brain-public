import itertools, numpy as np, importlib.util
spec = importlib.util.spec_from_file_location("w", "wa_tribes.py"); w = importlib.util.module_from_spec(spec); spec.loader.exec_module(w)
def table(n, fn):
    t = np.empty(1 << n)
    for m in range(1 << n):
        t[m] = -1.0 if fn([(m >> i) & 1 for i in range(n)]) else 1.0
    return t
def ratios(n, fn):
    r = [e/i for e, i in w.E_inf_all(w.wht(table(n, fn)), n) if i > 1e-15]
    return min(r), max(r)
T = lambda wd, s: (lambda b: any(all(b[t*wd:(t+1)*wd]) for t in range(s)))
print("T(2,4)", ratios(8, T(2, 4)), "T(4,2)", ratios(8, T(4, 2)))
print("T(3,4)", ratios(12, T(3, 4)), "T(4,3)", ratios(12, T(4, 3)))
print("T(2,8)", ratios(16, T(2, 8)), "T(8,2)", ratios(16, T(8, 2)))
perms = list(itertools.permutations(range(3)))
pm = lambda b: any(all(b[3*r + p[r]] for r in range(3)) for p in perms)
print("PM(K33)", ratios(9, pm))
