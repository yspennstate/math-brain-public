VERDICT: PARTIAL a strict geometric improvement of the earlier interaction-energy bound

The variance-limit conjecture is not proved. Both earlier results check
out. The new piece uses spatial continuity of the insertion cost to
strictly improve round 3's constant kappa.

With the earlier notation E_n=sum_j j V_{n,j}, let

\[
 F(c)=c^2+\frac4\pi e^{-\pi c^2}
                  -2c\operatorname{erfc}(\sqrt\pi c),
 \qquad \kappa=F(c_*),\quad c_*=\arg\min_{c\ge0}F(c).
\]

PROOF.md establishes, for every fixed c>0,

\[
 \limsup_n E_n\le
 F(c)-\frac{\pi c^4}{256}e^{-9\pi c^2}.
\]

In particular, defining

\[
 K=\kappa-\frac{\pi c_*^4}{256}e^{-9\pi c_*^2},
\]

gives limsup E_n<=K<kappa. This also replaces kappa by K in the earlier
variance-tail and noise-covariance bounds:

\[
 \limsup_n\sum_{j>m}V_{n,j}\le\frac K{m+1},\qquad
 \limsup_n(\operatorname{Var}(L_n)-C_n(\rho))\le K(1-\rho).
\]

The improvement is explicitly positive; no claim that it is large or
that it beats the best published variance bound is made. K is an upper
bound, not a proposed limiting variance.

The extra geometric input is elementary: x->d(x;S) is 2-Lipschitz,
where d is the optimal tour's insertion cost. Near an isolated base
point, two small disks lie on opposite sides of the threshold R=c/sqrt(n)
in the earlier squared-error envelope. The envelope prefers insertion
cost zero on one disk and 2R on the other. Spatial continuity prevents
simultaneously attaining those choices. The proof quantifies the deficit
on each disk pair, then sums over disjoint neighborhoods of isolated
points. Their exact expected count supplies the factor exp(-9pi c^2).
Boundary strips are treated explicitly. No local rearrangement theorem
for optimal tours is assumed.

This does not contradict round 3's scalar sharpness theorem: that theorem
does not impose spatial continuity. Its discontinuous scalar extremizer
cannot attain the envelope on these isolated neighborhoods.

AUDIT.md rechecks the old constant from truncated exponential moments,
the energy scale with replacement pairs, spatial continuity by a second
detour argument, the local deficit by translating one disk, and the
expected count through the joint density. The translation check even
allows a larger local deficit; the stated constant is conservative and
not optimized. Endpoint fields, coincident locations, n=2, boundary
control, disjointness, and positivity of F(c)-eta(c) were checked. No
mathematical error was found. All calculations are analytic; no simulation,
numerical optimization, or numerical variance estimate was run.

The web search tool was used for a status check lasting less than five
minutes. The opened source was Sourav Chatterjee,
[*A general method for lower bounds on fluctuations of random variables*](https://arxiv.org/html/1706.04290v3),
arXiv:1706.04290v3, Section 3, problem (2). No closing theorem was found
in the recorded searches, so no SOLVED_ELSEWHERE.md was written. This is
not an exhaustive literature review or a claim of novelty relative to
all published variance bounds.

Reproduce the artifact checks with:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
cat PROOF.md AUDIT.md
head -n 1 REPORT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
'
```

LOG.md records the reads, searches, choice, proof, and audit. The sandbox
reports `nice: setpriority: Operation not permitted`; no verified priority
adjustment is claimed. Only short file reads were run. All writes stay
in this folder; no git, subagents, or external messages were used.

What failed or remains uncertain: no fixed-order energy convergence,
fixed-noise covariance limit, variance convergence, or value of a limiting
variance is established. Improving a limsup cannot resolve uniqueness of
subsequential limits. The present continuity argument does not bridge
that gap. No unsuccessful numerical experiments are being omitted.

Next worker: target V_{n,1}=n Var(E[L_n|X_1]), including the boundary,
or fixed-noise covariance convergence. The present lemma also supplies a
concrete spatial constraint for any attempted variational analysis of
insertion fields. Optimizing its disk constants would remain an upper-bound
improvement and would not itself address convergence.

Task: "take the NEXT checkable step on this problem, building on that work"
— T222, 2026-11-15 approximately 05:02 Asia/Tbilisi (task-start estimate).
