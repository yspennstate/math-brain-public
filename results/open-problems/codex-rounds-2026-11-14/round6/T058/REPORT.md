VERDICT: PARTIAL proved that a deterministic correction transfers the joint Gaussian packing limit to every fixed interior phase band

Let k=floor(f(n)), t={f(n)} and mu=binom(n,k)2^-binom(k,2), with
f as in the earlier reports. Let X count independent k-sets and M be
their maximum disjoint packing size. Let H include each possible k-set
independently with probability q=2^-binom(k,2), and define the deterministic
correction c_n=E[|H|-nu(H)]. For every fixed 0<a<b<1, uniformly when
a<=t<=b, [PROOF.md](PROOF.md) proves
\[
 X-M-c_n=o_p(\sqrt\mu),\qquad
 0\le c_n\le\frac{\mu^2k^2}{2n}.
\]
Consequently the round-4 joint Gaussian limit holds for
\[
 \left(\frac{M-\mu+c_n}{\sqrt\mu},
       \frac{X_{k-1}-\mu_{k-1}}{\sqrt{\mu_{k-1}}}\right).
\]
This extends round 5 beyond phase 2/3 by controlling fluctuations of
the packing loss rather than requiring its expectation to be small.

The main new bound is finite and applies to the independent model:
\[
 \operatorname{Var}(|H|-\nu(H))
 \le Nq(1-q)[1-(1-q)^R]
 \le\frac{\mu^2k^2}{n},
 \quad N=\binom nk,\quad R=N-1-\binom{n-k}k.
\]
Adding one hyperedge changes the loss by 0 or 1, and changes it by zero
if it intersects no present hyperedge. The product-variance inequality
then gives this bound. The k-set family in the graph is close in total
variation to H by Robert Morris and Oliver Riordan,
[*Random cliques in random graphs revisited*, arXiv:2504.00964v1,
Theorem 3.1](https://arxiv.org/html/2504.00964v1#S3).
All its hypotheses are checked in the proof: the expected number of
pairs sharing a graph-edge constraint is
O(mu^2 k^5/n^2+mu k^2 n2^-k)=o(1) throughout the stated bands.
Chebyshev and total variation transfer the centered loss estimate.
The already proved joint count theorem supplies the final joint limit.
No literature-novelty claim is made.

The earlier result holds. Its pair expectation, common-vertex constant,
overlap estimate and deterministic deletion bound were independently
re-derived. Exact small-graph counts reproduce the expectation formula;
the round-4 forcing and joint-characteristic-function checks were also
rerun successfully. See [LOG.md](LOG.md) and [AUDIT.md](AUDIT.md).

Commands, run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify_centered.py
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T058/verify_joint.py
OMP_NUM_THREADS=1 nice -n 15 python3 audit_scales.py
```

The final exhaustive check passed for 1,083,424 independent hypergraphs
and 550,992 edge-addition checks, with exact rational variance bounds
at the prescribed q and at q=1/4,3/4. Independent packing algorithms and
closed-form expectations and variances agree. Original-graph enumeration
also checks the earlier pair formula and computes the total variation
of entire labelled families in four small cases. This run took 1.2563
seconds and 17.3 MB peak RSS. The predecessor joint-law check passed in
0.1370 seconds and 18.9 MB. Both verify actual nice=20. The launcher's
priority diagnostic reflects that inherited nice value.

The large-n audit passed all nine exact overlap and convexity-bound
checks at phases .5,.75,.875 near n=2^80,2^160,2^320. An independent
log-space calculation agrees within 2.3e-11 in log10 units. It took
185.92 seconds and 69.7 MB peak RSS, with actual nice=20. Floating
diagnostics extend through log2(n)=2560; these are diagnostics, not
certified probability bounds. Full outputs are centered_verification.json,
joint_verification.json and scale_audit.json.

At phase .75 near log2(n)=320.255384, log10(EY/sqrt(mu)) is 22.00050
for the old uncentered conflict bound, while log10(mu k^2/n) is
-15.40389 for the new normalized independent-model variance bound.
The exact edge-sharing expectation has log10(Delta)=-13.53056.
Convergence is slower near the upper phase boundary: at phase .875
near log2(n)=160, log10(Delta) is still positive. No finite cutoff
or quantitative total variation rate is asserted.

No mathematical check has failed. One documentation patch with incomplete
context was rejected before changing any file. The direct mean-loss
bound still only gives an uncorrected packing approximation below phase
2/3. Total variation alone does not transfer unbounded expectations,
so the proof retains the independent-model correction c_n. It does not
show E(X-M)=c_n+o(sqrt(mu)), nor Var(M)~mu. The correction is defined
exactly, but no explicit approximation at additive o(sqrt(mu)) accuracy
is supplied. Endpoint phases are excluded.

The bounded literature check found no full solution. The opened
Annika Heckel and Oliver Riordan paper,
[*How does the chromatic number of a random graph vary?*,
arXiv:2103.14014v3](https://arxiv.org/html/2103.14014), Conjecture 10,
uses the all-n phase-dependent exponent
max(theta(n),1-theta(n))/2, with theta(n)=log(mu)/log(n).
The brief's density-one exponent 1/2 is not that conjecture.
The opened [Oxford cube-root talk announcement](https://www.maths.ox.ac.uk/node/70763)
states an upper bound for certain n; no exact chromatic theorem or
full solution was obtained in the search budget. No SOLVED_ELSEWHERE.md
is warranted.

The chromatic concentration problem remains open in this work.
The packing covers o_p(n) vertices and the chromatic cost of the
remaining vertices is uncontrolled. The next worker can make c_n
explicit at additive o(sqrt(mu)) accuracy by controlling higher conflict
clusters in the independent model, or supply a quantitative coupling
and tail estimate to justify actual-mean centering. To reach chi, a
conditional estimate for the chromatic number after choosing the packing
is still needed. Obtain the precise cube-root theorem before claiming
a new chromatic concentration bound.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first recorded local clock 10:13:54 +04.
