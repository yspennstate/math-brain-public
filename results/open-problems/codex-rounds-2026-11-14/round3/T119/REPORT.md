VERDICT: COMPUTED exact rational certificate of Harangi's four-atom cubic upper bound

The earlier report's main conclusion survives an independent computation:
Harangi's explicit four-atom witness gives an upper bound strictly below
0.450789952. The new result is a reproducible certificate of that numerical
substitution, rather than another reading of the published tables.

With the published parameters interpreted as exact rational numbers, the
witness value B satisfies

\[
 B\in[0.45078995170969821695,\ 0.45078995170969821696],
 \qquad \alpha_3\le B<0.450789952.
\]

This verifies a published bound. It does not improve the stronger published
5-RSB bound 0.45078521, and it does not determine alpha_3. The earlier report
had not independently evaluated either witness.

`PROOF.md` gives the published inequality, exact inputs, integer brackets
for the powers x^(557/1000), rational logarithm series with explicit tails,
and endpoint propagation. `certify.py` uses only Python integers and exact
fractions for the certificate. `recheck.py` evaluates the original ordered
sums in double precision. `audit_decimal.py` independently evaluates them
at 70 and 110 decimal digits and checks containment in the certificate.

Commands, from this folder:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 certify.py --audit
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 certify.py --digits 24 --series-terms 64 --audit
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_decimal.py
```

All four commands passed. The refined certificate with structural audits
took about one second and used about 17 MB peak RSS. Checks include exact
grouped-versus-ordered weights, integer-root boundaries, range-reduction
signs, degenerate measures, cancellation in the one-atom case, and increased
precision. Full outputs and resource measurements are in `LOG.md`.

The five-minute literature check found no solution of the cubic problem.
Primary sources opened were Viktor Harangi,
[*Improved replica bounds for the independence ratio of random regular
graphs*, arXiv:2204.01353v4](https://arxiv.org/html/2204.01353), and
Balázs Gerencsér and Viktor Harangi,
[*Boosted second moment method in random regular graphs*,
arXiv:2510.12600v3](https://arxiv.org/html/2510.12600v3). The latter's 2026
revision still presents the small-degree constant as unresolved. The short
search is not an exhaustive claim about the literature.

What failed: an initial RLIMIT_AS guard was rejected by macOS before any
arithmetic; the fixed-size programs instead report and check actual peak
RSS. `nice -n 15` prints a permission warning because the processes already
inherit nice 20, which is lower priority. Direct priority checks confirm
nice 20 throughout. No mathematical check failed.

Limits and uncertainties: the interpolation theorem is a cited input, not
reproved here. The strongest 5-RSB witness and the supplied lower bound
have not been independently certified. No minimization was attempted;
nothing here proves a matching lower bound or an exact formula.

Next worker: obtain Harangi's cubic 5-RSB parameters (example 11 on the
[author's examples page](https://www.renyi.hu/~harangi/rsb.htm)), implement
the nested sums from the published theorem, and certify the stated
0.450785209433452 value. The rational power and logarithm methods here
can be reused, with a separate derivation of the nested exponents and
normalization. This would audit the strongest bound before any new search.

Task: “take the NEXT checkable step on this problem, building on that work.”
Session opened 15 November 2026, approximately 01:31 Asia/Tbilisi
(first recorded shell clock: 01:31:47 +04).
