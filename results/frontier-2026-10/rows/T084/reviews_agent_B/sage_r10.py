# T084, agent B: SAGE at RAD 6 (every R10 negative's exponent is in the hull of positives within L1 distance 6 at q = 0,
# r10_radius.txt) on R10 pair (0,1), then the S8 controls ((3,7) must not certify; (0,1) is the open case).
import json
MARK = chr(10) + 'if __name__ =='
exec(open('sage_cert.py').read().split(MARK)[0])
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
C = Npoly(colsR10, 0, 1)
for qv in [0.0, 0.05, 0.2, 0.4]: print(json.dumps(dict(matroid='R10', pair=(0, 1), RAD=6, **sage(C, qv, RAD=6))), flush=True)
Acon = [0b0111, 0b1011, 0b1101, 0b1111]
cs8 = [1, 2, 4, 8] + [sum(((Acon[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
for pr in [(3, 7), (0, 1)]:
    for qv in [0.0, 0.01, 0.2]: print(json.dumps(dict(control='S8', pair=pr, RAD=16, **sage(Npoly(cs8, *pr), qv, RAD=16))), flush=True)
