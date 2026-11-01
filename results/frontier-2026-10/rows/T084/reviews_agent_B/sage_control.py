# T084, agent B: positive control for sage_cert.sage - M(K4) disjoint and F7 are proved Potts-Rayleigh by the pairing
# certificate, so SAGE must reach s* <= 0 on them (s* = 0 expected at q = 0 where the K4 pairing is tight).
import json
MARK = chr(10) + 'if __name__ =='
exec(open('sage_cert.py').read().split(MARK)[0])
src = open('exact_pr_k4.py').read(); exec(src[:src.index("K4 = ")])
K4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for name, cols, e, f in [('K4 disjoint', graphic(K4, 4), 0, 5), ('F7', [1, 2, 4, 3, 5, 6, 7], 0, 1)]:
    C = Npoly(cols, e, f)
    for qv in [0.0, 0.05, 0.3]: print(json.dumps(dict(control=name, **sage(C, qv))), flush=True)
