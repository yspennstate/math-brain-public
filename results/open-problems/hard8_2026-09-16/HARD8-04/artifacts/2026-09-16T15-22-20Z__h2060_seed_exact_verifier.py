#!/usr/bin/env python3
"""Independent exact verification of H(2060) from the public length-515 seed.

The four explicit +/- sequences are the seed515 data published in Hadamard-T,
credited there to a decode of Schneider's public 2026-08-23 H(2060) artifact.
This checker does not execute that repository's automation. It checks the
periodic supplementary identity, independently assembles a standard
Goethals-Seidel matrix, and checks all row pairs by exact Hamming arithmetic.
"""
import hashlib
v=515
S=[
"+-+-+++++-++-++-+--++++--+++-+++-+++---++++--+-+------++-++----+++---------++-++++++--+++-+-++++-+-++++------+--+-++++-++++++----+----++++--+---+-+------+-+--+---++-+++--+--+-----+++--+-+-++-+-+-------++-+-+++---++-----+-+--+---+-+-++-+++-+--+-----+++-++-++---+-++-++--+-----++---+-+-++--++++++++--+-+-+++---+++-----+++-+++++---+--+----+--+-+++-++---++---+---++----+-++++-++-+---+++-----+---++-+-++--+-+--++-+-+--+-++-+++---+-+----++-++--++++-++-+-++++--+---+-+-+--++++-+-+---+---+-+-++--+--+--+--+++--+--++-++++---",
"-++--+++---+-+---++++--+---+++-+--+++-+-++++--+++---++++++-++++--+--++-+++-+--+++--++++++-+-+-+++----++-++-+-+-++++-+-+---+--++-+--+--+--+-+-++-+---++++-+--+--+++--+-----+++++-+---++---+++-+-+---++--+++-++++-+---+++++--++-++--++-+++-++-++------+---+-++-++++-++-+-+++-++-+---+-+++++---+--+-+--+++++-++----+++-+++--+--+-++-++---++++--+-++++-+-+-+-++++--++-++-+-++++-++-----+---+-+++--+--+-+----++--++-++----+---+-----+--+++-+-+--+++-+-+---+-+-+-++++--+----+--+----+-+-+---++-+++-----+++-------+-+--+-++-----++-----+--",
"-+---+-++-++++++-+-----+++++++--+--++++-+++-+++-++-++++-+-++--+-+++-+----++++-+++--+---+++-+-++++-++++-++++----+-++-----+-++----++--++--++-+----+---+++--+++-++++++--++--++-++-+---++-+----+-----+++++-+-+-+++++-+++++++-++----+--+---+--+--++++-+++-++++-+-+--+--+--++-+-++++-+---+-+--++----+---++++-++--+-++-+--+-+----+--+---++--+--+++++----+++-+-++-++-+-------+--+-+++--++++---+++++-+-+-+-+++++++++--+-++-+++-++----++-+--+---+++-+---+-+-++++--+++++---+++--+-++++-+++--++++--+-+--+--++-++-++--+-+--+---+--++---+-++-+++-",
"----+--+--++++--+-+-+++-++-+-+--++---+-+-+++++---+++--++-----+-+--+--++++-+---++-++++--+++++--+--++-++-+-+++--+---+--++++++-+-+---++++---+---++-+++---++-+++++--+--+++-+-+-+-++-+-----+-+---+-+---++-+---++-+++--+-+++-++++--++-++-+++-++++-+++-++-++-++++-+--+----+-----+-----+--++--++-++---+++-+-++-------+-++-++-++--+++---+-++++-+++-----+---+++++++++-++--+-++-----+-+-+----+++++-+---++--+-++++--+--+-+-----+++-+++--+---+-+-+--+++-+++---+-++-+-+++++----+++-+--+---+++-+++---+-+-+----++++-+++-++++-+-++++-++---++------+-"
]
assert [len(s) for s in S]==[v]*4
Q=[[1 if c=='+' else -1 for c in s] for s in S]
P=[]
for sh in range(v):
    P.append(sum(sum(a[i]*a[(i+sh)%v] for i in range(v)) for a in Q))
assert P[0]==4*v and all(x==0 for x in P[1:])
print('seed_lengths',[len(s) for s in S])
print('row_sums',[sum(a) for a in Q])
print('aggregate_paf_peak',P[0])
print('aggregate_paf_offpeak_max_abs',max(map(abs,P[1:])))

def circ_row(seq,i):
    return [seq[(j-i)%v] for j in range(v)]
def tr_row(seq,i):
    return [seq[(i-j)%v] for j in range(v)]
def xr_row(seq,i,transpose=False):
    return (tr_row(seq,i) if transpose else circ_row(seq,i))[::-1]
def neg(a):
    return [-x for x in a]

A,B,C,D=Q
rows=[]
for br in range(4):
    for i in range(v):
        if br==0:
            rr=circ_row(A,i)+xr_row(B,i)+xr_row(C,i)+xr_row(D,i)
        elif br==1:
            rr=neg(xr_row(B,i))+circ_row(A,i)+neg(xr_row(D,i,True))+xr_row(C,i,True)
        elif br==2:
            rr=neg(xr_row(C,i))+xr_row(D,i,True)+circ_row(A,i)+neg(xr_row(B,i,True))
        else:
            rr=neg(xr_row(D,i))+neg(xr_row(C,i,True))+xr_row(B,i,True)+circ_row(A,i)
        assert len(rr)==4*v and all(x in (-1,1) for x in rr)
        bits=0
        chars=[]
        for x in rr:
            bits=(bits<<1)|(x==1)
            chars.append('+' if x==1 else '-')
        rows.append((bits,''.join(chars)))
n=4*v
assert len(rows)==n
h=hashlib.sha256()
for _,s in rows:
    h.update((s+'\n').encode('ascii'))
digest=h.hexdigest()
print('plain_gs_sha256',digest)
expected=n//2
pairs=0
for i in range(n):
    bi=rows[i][0]
    for j in range(i+1,n):
        d=(bi^rows[j][0]).bit_count()
        if d!=expected:
            raise AssertionError((i,j,d,n-2*d))
        pairs+=1
print('order',n)
print('pair_count',pairs)
print('offdiag_dot_max_abs',0)
print('diag',n)
print('HHt_exact','PASS')
print('note','independent GS indexing convention; digest need not match source canonicalization')
print('ALL_EXACT_H2060_CHECKS_PASSED')
