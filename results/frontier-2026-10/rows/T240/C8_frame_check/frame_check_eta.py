"""Piece-boundary frame check for C8. Each piece rebuilds frame(nodes[k0]) from a float eigensolver in a new process;
r_out of the previous piece is measured in the frame that process built at the same node. This script rebuilds the
frames next to each boundary in ONE process and recomputes the logged switch norms on both sides of the boundary
(the previous piece's last segment, whose Pn is the boundary frame, and the next piece's first segment, whose P is the
boundary frame), and the trap's frame-change norm at node K. Bit-identical floats on both sides say both processes built
the same boundary frame (any difference that left every norm unchanged would also leave every radius r = |z| unchanged).
Usage: python frame_check_eta.py  (run in a copy of C8_eta_cell)"""
import sys, json, hashlib
sys.path[:0] = ['scripts', '.']
import entry_eta as E, entry
from entry import opnorm2_up
E.setup('1/2', '1/5000')
tq, nodes, slopes, ys, yslopes = E.build('1600', '0.004')
K = len(tq) - 1
def frm(k): return E.frame(entry.jac_f(E.fl(nodes[k])))
def sha(P): return hashlib.sha256(';'.join(','.join(str(x) for x in r) for r in P).encode()).hexdigest()[:16]
def swn(Pinvn, P): return float(opnorm2_up([[sum(Pinvn[i][l] * P[l][j] for l in range(3)) for j in range(3)] for i in range(3)]))
logged = {}
for n in ('q1', 'q2', 'q3', 'q4', 'q5', 'q6b', 'q6c', 'q6d'):
    for l in open('logs/%s.jsonl' % n, encoding='utf-8'):
        r = json.loads(l)
        if 'k' in r and 'sw' in r: logged.setdefault(r['k'], []).append((n, r['sw']))
ok = True
for b in (89, 178, 267, 356, 700, 1020, 1045):
    Pm, _ = frm(b - 1); Pb, Pib = frm(b); Pp, Pip = frm(b + 1)
    before, after = swn(Pib, Pm), swn(Pip, Pb)
    lb, la = logged.get(b - 1, []), logged.get(b, [])
    good = all(v == before for _, v in lb) and all(v == after for _, v in la) and lb and la
    ok &= bool(good)
    print('node %4d frame %s  sw(k=%d) %r logged %s  sw(k=%d) %r logged %s  %s' % (b, sha(Pb), b - 1, before, lb, b, after, la, 'SAME' if good else 'DIFFERS'))
tr = [json.loads(l) for l in open('logs/trap.jsonl', encoding='utf-8')][-1]
print('trap row keys with sw:', [k for k in tr if 'sw' in k.lower()], {k: tr[k] for k in tr if 'sw' in k.lower()})
PK, _ = frm(K); xs0, ysx = E.plateau_float(); Ps, Pis = E.frame(entry.jac_f(E.fl(xs0)))
print('node %d frame %s  swf %r' % (K, sha(PK), swn(Pis, PK)))
# the trap's need radius depends on both frames it builds (at node K and at the plateau); recompute it as run_trap does
from fractions import Fraction as F
from iv_exact import I
r = F(tr['r_end'])
diff = [I.of(nodes[K][i] - xs0[i]) + E.DH * I.of(ys[K][i] - ysx[i]) for i in range(3)]
off = E.norm2_up(E.matvec_rat(Pis, diff))
need = float(E.up(off + F(opnorm2_up([[sum(Pis[i][l] * PK[l][j] for l in range(3)) for j in range(3)] for i in range(3)])) * r))
good = float(off) == tr['offset'] and need == tr['need_rho']
ok &= good
print('trap offset %r logged %r  need_rho %r logged %r  %s' % (float(off), tr['offset'], need, tr['need_rho'], 'SAME' if good else 'DIFFERS'))
print('FRAMES REPRODUCED' if ok else 'FRAME MISMATCH')
