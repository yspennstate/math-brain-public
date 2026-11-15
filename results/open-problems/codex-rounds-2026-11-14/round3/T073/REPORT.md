VERDICT: PARTIAL strictly improved high-noise uniqueness criterion for the continuous-time fair-tie process on Z^2

The earlier result holds. Independently re-derived its stationary last-ring
argument and checked all 81 ordered local pairs, its integral, its endpoint
value, and its exact root bracket with verify_previous.py.

The new result is uniqueness of the stationary measure whenever

\[
(2-4\varepsilon)(1-\varepsilon^3/2)
 -\frac{17}{630}\varepsilon^4(1/2-\varepsilon)^4<1,
\qquad 0\le\varepsilon\le1/2.
\]

Its threshold is approximately 0.248076820004086075039, compared with the
earlier 0.248076921333013. The improvement is approximately 1.01328926e-7.
In particular, the whole interval [0.24807685,0.5] is now covered. At its
left endpoint the new contraction factor is approximately
0.99999987814192776, whereas the earlier factor is
1.00000028978957623. Thus this is a strict extension of the preceding
result, although a small one. The low-noise coexistence problem remains
unresolved by this work.

The new ingredient is a stationary three-neighbor disagreement bound.
Writing a=1/2-epsilon and d for the disagreement density in the ordered
stationary coupling, every triple A of neighbors of x satisfies

\[
\mathbb E\prod_{y\in A}D_y
 \ge\frac{17}{1260}\varepsilon^4a^3d.
\]

A disagreement at x is held while four diagonal sites are forced to
alternating common values. Each selected neighbor then has one common 0,
one common 1, the disagreeing center, and an arbitrary ordered axial input.
Its last update produces a disagreement with conditional probability at
least a. The required seven-clock partial order has 272 linear extensions;
its last-source-ring integral contributes 272/8!. Iterated conditional
expectation handles dependence among the selected updates. Counting the
unused local slack when three or four neighbors disagree then yields the
subtracted term above. The complete, self-contained proof is in
[PROOF.md](PROOF.md).

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py
```

Both commands exited 0 in under one second. The second saves
[audit_output.json](audit_output.json). It checks all 81 ordered local
pairs, reconstructs the update rule independently, checks all three axial
input cases and the rotated helper geometry, counts 272 by three methods,
and verifies the clock integral and all numerical claims by exact rational
arithmetic. Factored and expanded contraction formulas agree. Exact root
bounds are

\[
\frac{146438707495522750369}{590295810358705651712}
 < e_1 <
\frac{1171509659964182002953}{4722366482869645213696},
\]

with width 1/4722366482869645213696. Independent decimal-grid sign checks
also bracket the root. Measured peak memory was approximately 16 MB, with
one thread and a 30-second CPU limit. The worker inherited nice 20; the
requested nice prefix prints `setpriority: Operation not permitted` on this
Mac because priority is already 20. Both scripts check actual nice >=15
before the audit.

The initial literature check finished within five minutes. No solution
changing the earlier picture was located. Opened the arXiv pages and full
texts of Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority
vote process on trees*, [arXiv:2501.16202](https://arxiv.org/abs/2501.16202),
and Damiano De Gaspari, *Fredrickson Andersen Model and Noisy Majority Vote
Process on Nonamenable Graphs*,
[arXiv:2508.06935](https://arxiv.org/abs/2508.06935). The pages still list
only their 2025 first versions. Their results concern trees and suitable
expansion, respectively. Also opened G. Gielis, C. Maes, K. Vande Velde,
*Randomly interacting particle systems: The uniqueness regime*, Annales
de l'I. H. P., section A 70 (1999), 445–472,
[full text](https://www.numdam.org/item/AIHPA_1999__70_5_445_0.pdf).
The short check did not establish a directly comparable numerical bound
for the exact homogeneous continuous-time fair-tie rule. No assertion of
literature novelty or optimality is made.

Failures and uncertainty: no audit assertion failed. A speculative v2 URL
for De Gaspari returned 404. Requiring all four neighboring disagreements
gave a weaker local correction; the saved proof uses triples. The audit
cannot formally verify the infinite-volume or conditional-probability
arguments; these are proved in writing and challenged in
[LOG.md](LOG.md). No low-noise coexistence proof, conclusion at the new
threshold, or result for retained ties was obtained. The brief literature
check cannot establish the absence of a solution or of stronger published
high-noise bounds.

The next worker should first check whether published uniqueness criteria
already imply this interval for exactly rule (1). Within this local method,
the remaining two-disagreement slack is a concrete next target: when two
neighbors disagree and the other two are common and equal, the local gap
is a. Seek a dependence-correct lower bound for that event weighted by
disagreement. The present coefficient also leaves half the three-neighbor
slack unused. Improving these local bounds would still address high-noise
uniqueness; low-noise coexistence requires a different argument controlling
large error clusters on Z^2.

Task: “take the NEXT checkable step on this problem, building on that work”
— 2026-11-15, 01:09 +04 (Asia/Tbilisi).
