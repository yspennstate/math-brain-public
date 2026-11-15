VERDICT: PARTIAL a complete single-event conjugacy refinement and a sharp joint-event compatibility inequality for the 103-type table

RBS remains unresolved. The preceding stationarity result passed an
independent exact check: all 103 fair-AND costs, all 103 dual inequalities,
their three equality cases, rank four, and both attained extrema agree.
No predecessor file was edited.

The proposed ab/ba fixed-point row has now been added. It raises the
homogeneous constraint rank from four to five, or six with normalization.
Moreover it supplies every further constraint obtained by equating
single word-equality probabilities whose difference words are conjugate
up to inversion in the free group. The 21 equality events split into ten
conjugacy classes. Their eleven representative-difference rows reduce to
the four stationarity basis rows, the ab/ba row, and six zero rows.
PROOF.md gives the complete classification, explicit identities and a
determinant-one rank witness.

These constraints still admit the impossible singleton

\[
\widehat\pi=(0,1,2,0,3,4,1).
\]

It asserts a=bb and ab!=ba at every root. The first relation would give
A=B^2 globally and therefore force commutation. The type does occur at
one root of an explicit five-point completion; the obstruction concerns
its frequency distribution.

A new sharp inequality on the same table excludes it. For arbitrary
finite permutations A,B, put

\[
E=\{v:A(v)=B^2(v)\},\qquad F=\{v:B(A(v))\ne A(B(v))\}.
\]

Then

\[
|E\cap F|\leq |E^c\cap F|,
\qquad d_H(BA,AB)\leq2d_H(A,B^2).
\]

The proof counts exits from E under B and matches them to entrances.
A four-point model attains both inequalities with positive sides, proving
that their coefficients are sharp. In type frequencies the stronger
inequality is

\[
\sum_\pi x_\pi(2I_{a=bb}(\pi)-1)I_{ab\ne ba}(\pi)\leq0.
\]

It bounds the frequency of the new singleton by 1/2 in every finite
model and every limit. Its fair-AND cost is exactly

\[
\tfrac92\log2+\tfrac34\log3-\tfrac5{16}\log5
-\tfrac{21}{16}\log7=0.8861651107500812\ldots>\log2,
\]

so the earlier entropy inequality does not already exclude it. A separate
conditional probability table and the integer comparison
2^56*3^12 > 5^5*7^21 verify this cost and its sign.

Validation commands, run in this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 compatibility_audit.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_compatibility.py
```

Both passed. The main audit checked all 15,017 permutation pairs on one
through five points, totaling 74,421 roots, in 0.218 seconds with
17,088,512 bytes peak RSS. The independent verifier reconstructs partitions
and probability laws differently, checks the rank minor by elimination,
and tests the boundary inequality directly from permutations without the
type table. It passed in 0.0421 seconds with 16,203,776 bytes peak RSS.
Both use only the standard library, one process, one thread, a 180-second
alarm and a below-1-GiB RSS check. The nice diagnostic reflects inherited
priority 20, checked by both scripts. Data are in compatibility_result.json
and independent_verification.json. Scripts read the round-5 exact table
at its existing path; no predecessor script is imported or executed.

What failed: the first expanded audit had a mistyped C3 test tuple;
direct evaluation corrected it before the exhaustive checks. No proposed
inequality failed. The fair-AND extrema remain log 2 and (3/2)log 2,
and its general-p upper cap remains unchanged: the attaining finite
models survive every valid refinement. No genuine positive-gap code,
new non-sofic candidate or new instance of RBS was obtained. The bound
1/2 is not claimed optimal for the particular singleton. Sufficiency of
the strengthened constraints and priority of these finite refinements
have not been established.

The bounded literature check found no resolution. Opened sources:
Brandon Seward, *Krieger's finite generator theorem for actions of
countable groups II*, [arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4);
Lewis Bowen and Michael Chapman, *Surjunctivity does not characterize
cosoficity of invariant random subgroups*,
[arXiv:2511.06586](https://arxiv.org/abs/2511.06586);
Zongrui Hu, Leiye Xu, Shuhao Zhang, *Positive Rokhlin Entropy Implies
Infinite L^1-Orbit Multiplicity: A Negative Answer to Thouvenot's Question*,
[arXiv:2607.11549](https://arxiv.org/abs/2607.11549).
The latter two concern an IRS analogue and an amenable-action consequence,
respectively. This search is not proof of absence of later work.

Next: add the symmetric boundary row for B=A^2 and derive more
joint-event transport inequalities visible in this window. Test whether
the new singleton's frequency bound 1/2 can be sharpened using its
additional relation aa=1. An actual positive-gap group/code remains
essential for any application to RBS; this finite refinement supplies none.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 2026-11-15 11:15 Asia/Tbilisi (first clock reading 11:15:52).
