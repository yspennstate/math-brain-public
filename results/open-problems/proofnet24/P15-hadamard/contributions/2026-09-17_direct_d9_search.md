# Direct H(2092) construction attack — d=9 GS branch

Date: 2026-09-17. Direct user-requested research contribution; no scheduler change.

## Target and status

Target: construct a real Hadamard matrix of order `2092=4*523`. The repository's P15 handoff treats 2092 as the current documented construction target after 668 and 2060 became externally known. This note does **not** claim that H(2092) has been constructed. Status remains OPEN/PARTIAL.

I continued the common order-nine multiplier Goethals-Seidel branch. Let

`K=<19>={1,19,60,94,217,361,410,462,468} <= F_523^*`

and `C_j=3^j K`, `j in Z/58Z`. For the surviving positive row-sum profile `(17,17,17,35)`, the four negative sets contain zero and respectively 28,28,28,27 nonzero K-orbits. If `A_i=1-2 1_{X_i}`, the exact target is

`sum_i PAF_{A_i}(s)=0` for every nonzero `s in Z_523`.

The previously proved split-617 lifting theorem remains the exact closure gate: satisfying all 29 paired character equations over F_617 is sufficient for the full integer PAF identity, hence yields a GS construction that can be expanded and checked by exact `H H^T=2092 I` arithmetic.

## New direct search

I implemented a fresh witness-first stochastic search in the original integer PAF space, preserving the orbit cardinalities exactly. A move swaps one selected and one unselected K-orbit in one of the four blocks. Every candidate is expanded to four length-523 sign sequences, its periodic autocorrelations are recomputed, and the exact integer objective

`E = sum_{s=1}^{522} (sum_i PAF_{A_i}(s))^2`

is evaluated. Thus `E=0` is an exact construction threshold; no floating-point residual is used as a proof decision.

A direct run reached the following checkpoint:

- exact residual energy `E = 20736`;
- residual value distribution over the 522 nonzero shifts:
  - `-12`: 18 shifts
  - `-8`: 72 shifts
  - `-4`: 126 shifts
  - `0`: 108 shifts
  - `4`: 126 shifts
  - `8`: 36 shifts
  - `12`: 18 shifts
  - `16`: 18 shifts
- 108/522 nonzero shifts are already exact zeros, but this is **not** a Hadamard witness.

The corresponding selected nonzero K-coset indices are

```
X0: 0 3 5 6 8 9 12 16 17 19 20 21 26 27 29 30 31 34 36 37 39 40 41 46 47 49 52 55
X1: 1 2 5 6 8 9 10 12 17 19 20 21 24 27 28 29 30 32 35 36 38 40 42 45 46 51 53 56
X2: 2 4 5 6 7 10 11 14 15 16 17 18 19 23 29 30 32 35 36 37 39 40 43 44 46 51 56 57
X3: 2 3 6 9 10 11 13 15 17 21 25 29 32 33 35 36 38 41 43 44 45 47 50 53 54 55 56
```

Zero is additionally in every negative set. The row sums are therefore exactly `(17,17,17,35)`.

As an independent diagnostic against the split-617 closure gate, this checkpoint satisfies only one of the 29 exact F_617 character blocks (block 7). Thus the low integer residual is not being misrepresented as a modular certificate.

I also attacked the other surviving d=9 row-sum profile `(37,19,19,1)` (orbit counts 27,28,28,29 with zero positive) and did not obtain an exact witness. No failed heuristic run is an impossibility result.

## Mathematical observations preserved for the next attack

Because the sequences are K-invariant, the residual is constant on each of the 58 nonzero K-cosets. Therefore the 522-shift objective has only 58 distinct residual coordinates, each repeated nine times. The zero-frequency row-sum identity forces the sum of the 58 orbit residuals to be zero. Every residual is divisible by four. It is consequently more efficient to repair the 58-dimensional orbit residual vector directly rather than optimize 522 independent-looking equations.

The best checkpoint above has `E/(9*16)=144`; equivalently, after dividing each orbit residual by four, the sum of the 58 squared integer residual coordinates is 144. This gives a sharply finite local-repair target, but not a proof that a repair exists.

The next useful construction move is an exact multi-orbit repair search around this checkpoint (two- and three-swap neighborhoods, then meet-in-the-middle deltas) while simultaneously requiring the split-617 equations. If a zero is reached, expand immediately to the 2092-by-2092 GS matrix and execute the full exact Gram check before claiming closure.

## Scope / honesty

- No H(2092) construction is claimed here.
- No nonexistence claim is made for d=9, GS, or arbitrary H(2092).
- The universal Hadamard conjecture remains open.
- This checkpoint is search progress only, not publication-grade mathematical progress.
