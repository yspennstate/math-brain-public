#!/usr/bin/env python3
"""Exact reconstruction/check of H(2060) from the public Schneider-derived seed.

Source snapshot: JD-Jones-ASES/Hadamard-T@eec1bed6216c44675d946fe80d47695a7ae2ab40
  data/seed515.json (four normalised length-515 +/- sequences)

The checker constructs a standard Goethals-Seidel array of order 4*515 and
checks every row pair exactly using Python integer XOR/bit_count.  For +/-1
rows r,s of length n, <r,s> = n - 2*Hamming(r,s), so this is an exact
integer HH^T=nI check, not floating-point arithmetic.
"""
from __future__ import annotations
import hashlib

V = 515
N = 4 * V
SEED = [
"+-+-+++++-++-++-+--++++--+++-+++-+++---++++--+-+------++-++----+++---------++-++++++--+++-+-++++-+-++++------+--+-++++-++++++----+----++++--+---+-+------+-+--+---++-+++--+--+-----+++--+-+-++-+-+-------++-+-+++---++-----+-+--+---+-+-++-+++-+--+-----+++-++-++---+-++-++--+-----++---+-+-++--++++++++--+-+-+++---+++-----+++-+++++---+--+----+--+-+++-++---++---+---++----+-++++-++-+---+++-----+---++-+-++--+-+--++-+-+--+-++-+++---+-+----++-++--++++-++-+-++++--+---+-+-+--++++-+-+---+---+-+-++--+--+--+--+++--+--++-++++---",
"-++--+++---+-+---++++--+---+++-+--+++-+-++++--+++---++++++-++++--+--++-+++-+--+++--++++++-+-+-+++----++-++-+-+-++++-+-+---+--++-+--+--+--+-+-++-+---++++-+--+--+++--+-----+++++-+---++---+++-+-+---++--+++-++++-+---+++++--++-++--++-+++-++-++------+---+-++-++++-++-+-+++-++-+---+-+++++---+--+-+--+++++-++----+++-+++--+--+-++-++---++++--+-++++-+-+-+-++++--++-++-+-++++-++-----+---+-+++--+--+-+----++--++-++----+---+-----+--+++-+-+--+++-+-+---+-+-+-++++--+----+--+----+-+-+---++-+++-----+++-------+-+--+-++-----++-----+--",
"-+---+-++-++++++-+-----+++++++--+--++++-+++-+++-++-++++-+-++--+-+++-+----++++-+++--+---+++-+-++++-++++-++++----+-++-----+-++----++--++--++-+----+---+++--+++-++++++--++--++-++-+---++-+----+-----+++++-+-+-+++++-+++++++-++----+--+---+--+--++++-+++-++++-+-+--+--+--++-+-++++-+---+-+--++----+---++++-++--+-++-+--+-+----+--+---++--+--+++++----+++-+-++-++-+-------+--+-+++--++++---+++++-+-+-+-+++++++++--+-++-+++-++----++-+--+---+++-+---+-+-++++--+++++---+++--+-++++-+++--++++--+-+--+--++-++-++--+-+--+---+--++---+-++-+++-",
"----+--+--++++--+-+-+++-++-+-+--++---+-+-+++++---+++--++-----+-+--+--++++-+---++-++++--+++++--+--++-++-+-+++--+---+--++++++-+-+---++++---+---++-+++---++-+++++--+--+++-+-+-+-++-+-----+-+---+-+---++-+---++-+++--+-+++-++++--++-++-+++-++++-+++-++-++-++++-+--+----+-----+-----+--++--++-++---+++-+-++-------+-++-++-++--+++---+-++++-+++-----+---+++++++++-++--+-++-----+-+-+----+++++-+---++--+-++++--+--+-+-----+++-+++--+---+-+-+--+++-+++---+-++-+-+++++----+++-+--+---+++-+++---+-+-+----++++-+++-++++-+-++++-++---++------+-"
]
EXPECTED_SOURCE_ROW_SUMS = (-17, 5, 39, 15)
SOURCE_SEED_BLOB_SHA = "7292d2cec866c6df2a2156cb63550a56ab92816f"
SOURCE_GIST_CANONICAL_SHA256 = "c7a145d86210740dd3f8ea21ca896a54d6916007a042638f17c8c47f097200f7"

FLIP = str.maketrans("+-", "-+")

def vals(s: str):
    return [1 if c == "+" else -1 for c in s]

def paf(a):
    return [sum(a[j] * a[(j+t) % V] for j in range(V)) for t in range(V)]

def circ_rows(s: str):
    # C[i,j] = s[(i-j) mod V]
    return ["".join(s[(i-j) % V] for j in range(V)) for i in range(V)]

def transpose_circ_rows(s: str):
    # C^T[i,j] = s[(j-i) mod V]
    return ["".join(s[(j-i) % V] for j in range(V)) for i in range(V)]

def neg(rows):
    return [r.translate(FLIP) for r in rows]

def mul_R(rows):
    # Right multiplication by the back-identity R.
    return [r[::-1] for r in rows]

def bitrow(line: str) -> int:
    return int("".join("1" if c == "+" else "0" for c in line), 2)

def main():
    assert len(SEED) == 4
    assert all(len(s) == V and set(s) == {"+", "-"} for s in SEED)
    arrays = [vals(s) for s in SEED]
    sums = tuple(sum(a) for a in arrays)
    assert sums == EXPECTED_SOURCE_ROW_SUMS
    assert sum(x*x for x in sums) == N

    agg = [0] * V
    for a in arrays:
        p = paf(a)
        for t, x in enumerate(p):
            agg[t] += x
    assert agg[0] == N
    assert all(x == 0 for x in agg[1:])

    A, B, C, D = [circ_rows(s) for s in SEED]
    Bt, Ct, Dt = [transpose_circ_rows(s) for s in SEED[1:]]
    BR, CR, DR = map(mul_R, (B, C, D))
    BtR, CtR, DtR = map(mul_R, (Bt, Ct, Dt))

    grid = [
        [A, BR, CR, DR],
        [neg(BR), A, neg(DtR), CtR],
        [neg(CR), DtR, A, neg(BtR)],
        [neg(DR), neg(CtR), BtR, A],
    ]

    rows = []
    sha = hashlib.sha256()
    for bi in range(4):
        for i in range(V):
            line = "".join(grid[bi][bj][i] for bj in range(4))
            assert len(line) == N and set(line) <= {"+", "-"}
            sha.update((line + "\n").encode("ascii"))
            rows.append(bitrow(line))
    assert len(rows) == N

    pair_count = 0
    max_abs_offdiag = 0
    min_hamming = N
    max_hamming = 0
    for i in range(N):
        # diagonal row norm is exactly N because all entries are +/-1.
        ri = rows[i]
        for j in range(i):
            pair_count += 1
            h = (ri ^ rows[j]).bit_count()
            ip = N - 2*h
            if abs(ip) > max_abs_offdiag:
                max_abs_offdiag = abs(ip)
            if h < min_hamming:
                min_hamming = h
            if h > max_hamming:
                max_hamming = h
            if ip != 0:
                raise AssertionError(f"nonorthogonal pair {(i,j)} inner_product={ip}")

    assert pair_count == N*(N-1)//2
    assert max_abs_offdiag == 0
    assert min_hamming == max_hamming == N//2

    print(f"source_seed_blob_sha={SOURCE_SEED_BLOB_SHA}")
    print(f"source_gist_canonical_sha256={SOURCE_GIST_CANONICAL_SHA256}")
    print(f"row_sums={sums} sumsq={sum(x*x for x in sums)}")
    print(f"aggregate_paf_zero={agg[0]} max_abs_nonzero_shift={max(abs(x) for x in agg[1:])}")
    print(f"constructed_plain_gs_sha256={sha.hexdigest()}")
    print(f"pair_count={pair_count}")
    print(f"offdiag_max_abs={max_abs_offdiag}")
    print(f"offdiag_hamming_min={min_hamming} offdiag_hamming_max={max_hamming}")
    print(f"HHt_diagonal={N} HHt_offdiag=0")
    print(f"VERDICT: HADAMARD order={N} all {pair_count} row pairs orthogonal")

if __name__ == "__main__":
    main()
