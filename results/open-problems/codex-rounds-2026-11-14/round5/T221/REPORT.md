VERDICT: PARTIAL exact stationary extrema for the fair-AND collision table, with an explicit missing compatibility constraint

RBS remains unresolved. The preceding completion lemma, information
inequality and AND cap survived independent rederivation. Both new
scripts independently reconstruct the 103 admissible types and match
all 515 earlier cost entries. No predecessor artifact was edited.

The new step implements the preceding report's proposed stationarity
constraints on the triple patterns at (1,a,b), (a,aa,ab), and (b,ba,bb).
The ten equations have rank four; including normalization gives rank
five. A direct rank argument and a determinant-one minor certify this.

For the fair-bit three-input AND encoder, the resulting relaxation has
the exact extrema

\[
 \min\sum_\pi x_\pi C_\pi=\log2,
 \qquad
 \max\sum_\pi x_\pi C_\pi=\tfrac32\log2.
\]

The unrestricted table minimum is 0.6895216759678042, below log 2.
Thus stationarity removes the isolated low-cost patterns. The new lower
bound has an explicit dual certificate with two nonzero stationarity
multipliers. All 103 inequalities are verified by integer-product
comparisons; exactly three are equalities. PROOF.md gives the
coefficients, six-case compressed table, exact comparison procedure,
and separate probability calculations for the two nontrivial tight
types. One-point and two-point models attain the two extrema.

The upper cap does not improve. For every Bernoulli parameter p, the
preceding two-point and three-point models attain the two branches of
h(p)+p max{h(p),h(p^2)} at every root, so stationarity cannot lower it.

The relaxation also has an explicit limitation. The singleton type
(0,1,2,3,0,4,5) is admissible and triple-stationary, but cannot be a
frequency distribution of finite models, or a limit of such distributions.
It asserts ab fixes every root and ba fixes none. These permutations
are conjugate and must have equal fixed-point counts. A six-point
completion verifies that this type does occur at an individual root.
Its AND cost exceeds log 2, so adding the finite information inequality
does not exclude this impossible frequency distribution either.

The proof also gives the general weighted defect certificate with free
stationarity multipliers, ready for specified word-defect tolerances.
No genuine positive-gap group/code is supplied, and no new instance of
RBS follows. Priority of the refinement has not been established.

Validation commands, run in this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 stationarity_audit.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_certificate.py
```

Both passed. The first used SciPy/HiGHS with one solver thread to locate
the extrema, then certified the lower bound exactly. Its final run took
1.155 seconds and 73,089,024 bytes peak RSS. It additionally checked
all 617 generator assignments on one through four points, totaling
2,421 roots, for stationarity, the information inequality and the missing
conjugacy identity. The maximum discrepancy from earlier costs was
1.111e-15.

The independent verifier uses only the standard library. It computes
laws by inclusion-exclusion instead of class-bit enumeration, checks
all 103 certificate inequalities, all six grouped minima, both attainable
extrema, and the rank minor. It independently matches all 515 earlier
costs within 2.221e-16. Its final run took 0.200 seconds and 17,137,664
bytes peak RSS. Solver tolerances do not enter the certificate signs.

Data: stationarity_table.json, stationarity_certificate.json,
stationarity_result.json and independent_verification.json. LOG.md
records commands, findings and checks. Every run used one process,
OMP_NUM_THREADS=1, a 180-second alarm and an RSS check below 1 GiB.
The nice wrapper's diagnostic reflects inherited priority 20, asserted
by both scripts. No mathematical check failed; no git, external writes
or subagents were used.

The bounded literature check found no resolution. Opened references:

- Brandon Seward, *Krieger's finite generator theorem for actions of
  countable groups II*, [arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4).
- Lewis Bowen and Michael Chapman, *Surjunctivity does not characterize
  cosoficity of invariant random subgroups*,
  [arXiv:2511.06586v1](https://arxiv.org/html/2511.06586v1).
- Zongrui Hu, Leiye Xu, Shuhao Zhang, *Positive Rokhlin Entropy Implies
  Infinite L^1-Orbit Multiplicity: A Negative Answer to Thouvenot's
  Question*, [arXiv:2607.11549](https://arxiv.org/abs/2607.11549).

The latter two address an IRS analogue and an amenable-group consequence,
respectively. This search is not proof of absence of later work.

What did not work: stationarity gives no smaller universal AND upper cap,
and its equations, even with the entropy inequality, do not characterize
realizable type frequencies. The proposed stationary entropy-violating
example did not appear; the exact lower certificate explains why for
fair AND. The extension is limited to this finite relaxation.

Next: add the fixed-point identity for ab and ba to this same 103-type
table, then identify further conjugacy constraints visible through word
equality events. The singleton above gives a concrete test that the
additional row must exclude. A separate essential obstacle remains:
a certified genuine positive-gap candidate is needed for an RBS
application. Larger tables alone do not supply one.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 2026-11-15 08:38 Asia/Tbilisi.
