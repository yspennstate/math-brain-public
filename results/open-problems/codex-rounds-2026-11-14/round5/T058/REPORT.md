VERDICT: PARTIAL proved that maximum disjoint independent-set packings inherit the Gaussian count fluctuations below phase 2/3

Let
\[
 f(n)=2\log_2n-2\log_2\log_2n+2\log_2(e/2)+1,
 \quad k=\lfloor f(n)\rfloor,
 \quad \mu_k=\binom nk2^{-\binom k2}.
\]
Let X_k count independent k-sets, and let M_k be the maximum number of
pairwise vertex-disjoint independent k-sets. For every fixed
0<a<b<2/3, uniformly when a<={f(n)}<=b,
\[
 \mathbb E\frac{X_k-M_k}{\sqrt{\mu_k}}
 \le (1+o(1))\frac{\mu_k^{3/2}k^2}{2n}
 \le n^{3b/2-1+o(1)}=o(1).
\]
Thus the preceding joint Gaussian limit remains valid with M_k replacing
X_k. M_k may be centered at either mu_k or its own expectation, with
normalization sqrt(mu_k). [PROOF.md](PROOF.md) contains the proof;
[AUDIT.md](AUDIT.md) gives independent counts and checks.

This proves the concrete packing lemma proposed by round 4. The key new
term is one-vertex intersections, which contribute zero to the earlier
covariance but prevent disjointness. If Y counts all intersecting
unordered pairs of independent k-sets, then X_k-M_k<=Y deterministically
and EY~mu_k^2 k^2/(2n) on every fixed interior phase band. This asymptotic
and the resulting packing approximation are the extension beyond the
previous report. No literature-novelty claim is made.

The earlier joint-limit proof was independently re-derived, including
the forcing increment, characteristic-function equation, positive
threshold-covariance kernel and uniform overlap estimate. It holds.
Its exhaustive verification was also rerun successfully from this
folder, writing only local output.

Commands:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T058/verify_joint.py
OMP_NUM_THREADS=1 nice -n 15 python3 verify_packing.py
OMP_NUM_THREADS=1 nice -n 15 python3 audit_scales.py
```

All runs passed. The exact packing check enumerates every graph on five
and six vertices and every k=2,...,n. Two independent packing algorithms
agree throughout. Pair expectations, incidence double counts, deletion
bounds, large-n overlap recurrences and the proof's convexity bounds
also pass. The run took 153.034 seconds with 41.4 MB peak RSS. The
independent log-space diagnostic reproduces the exact normalized scales
within 3.2e-9 in log10 units and cheaply extends them through log2(n)=2560.
Every script verifies actual nice=20. Outputs are joint_verification.json,
packing_verification.json and scale_audit.json; details are in
[LOG.md](LOG.md).

No mathematical check failed. The numerical audit caught an underflowing
display of tiny error bounds; those are now recorded in logarithmic units.
One documentation patch was rejected before changing files and reapplied.
Convergence can be very slow: at phase 5/8, EY/sqrt(mu_k) is still about
20,003 near n=2^320. The proof supplies no finite cutoff. Values above
phase 2/3 test the method's limitation, not a counterexample to a packing
limit.

The bounded literature check found no full solution. Opened sources were
Annika Heckel and Oliver Riordan,
[*How does the chromatic number of a random graph vary?*, arXiv:2103.14014](https://arxiv.org/html/2103.14014),
and Robert Morris and Oliver Riordan,
[*Random cliques in random graphs revisited*, arXiv:2504.00964](https://arxiv.org/html/2504.00964v1).
The latter concerns distributions of clique families, rather than a full
chromatic concentration theorem. The 2025 cube-root announcement remains
a separate lead whose precise chromatic theorem was not obtained. As the
first local report established, the published conjecture is phase dependent.
Conjecture 10 is stated along all n, with exponent
lambda(n)=max(theta(n),1-theta(n))/2 and theta(n)=log(mu_k)/log(n).
It is not the brief's density-one exponent 1/2 formulation. This was
checked directly in the opened paper.

The chromatic concentration problem remains open in this work. The
packing covers o_p(n) vertices. Its Gaussian fluctuation says nothing
here about the chromatic cost of the remaining graph. No variance
asymptotic for M_k or result at phase 2/3 is asserted. The conflict upper
bound becomes insufficient above 2/3; this does not prove the packing
approximation false there.

Next worker: establish whether the packing loss can be replaced by a
deterministic correction with residual o_p(sqrt(mu_k)) on bands above
2/3. This requires controlling its fluctuations, rather than its mean;
counting intersecting triples or overlapping edges in the conflict graph
is a concrete first test. A separate conditional estimate for the
chromatic number of the unpacked graph is still required to reach chi.
Obtain the exact cube-root theorem before asserting a new chromatic bound.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first recorded local clock 07:45:50 +04.
