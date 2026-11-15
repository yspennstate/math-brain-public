VERDICT: PARTIAL proved a joint Gaussian limit for adjacent independent-set counts on fixed interior phase bands

The round 3 moment result holds. Its main asymptotics were re-derived,
and an independent orthogonal expansion in edge variables reproduces its
exact covariance numerators and largest numerical sample.

The new result upgrades those moments to a joint distributional limit.
Write

\[
 f(n)=2\log_2n-2\log_2\log_2n+2\log_2(e/2)+1,
 \qquad k=\lfloor f(n)\rfloor.
\]

Let X_j count independent j-sets and let mu_j be its mean. For each fixed
0<delta<1/2, uniformly over integers with delta<={f(n)}<=1-delta,

\[
 \left(\frac{X_k-\mu_k}{\sqrt{\mu_k}},
       \frac{X_{k-1}-\mu_{k-1}}{\sqrt{\mu_{k-1}}}\right)
 \xrightarrow{d} N(0,I_2).
\]

[PROOF.md](PROOF.md) proves this with an explicit characteristic-function
bound, of size at most n^(-delta/2+o(1)) at bounded arguments. The proof
uses a monotone size-biased coupling for each marginal and positive
association to bound the joint dependence. It includes both arguments
in full. [AUDIT.md](AUDIT.md) gives a second proof of the joint-independence
step using the nonnegative threshold-covariance kernel and Fatou's lemma.

This resolves the joint-Gaussian question left open in the preceding
local report. It proves no new concentration bound for chi. Neither a
conditional law for chi given the counts nor a sensitivity estimate
relating chi to them is established. No literature-novelty claim is made;
the marginal Poisson behaviour is already discussed by Annika Heckel and
Oliver Riordan in [*How does the chromatic number of a random graph vary?*,
arXiv:2103.14014](https://arxiv.org/html/2103.14014).

Reproduce the checks from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 recheck_moments.py
OMP_NUM_THREADS=1 nice -n 15 python3 verify_joint.py
```

Both passed. The first compares exact integer numerators from two
different expansions. At n approximately 2^320.255384, k=625 and phase
.75, it reproduces Var(X_(k-1))/mu_(k-1)-1 =
5.108702812850075e-13 and Cov/(k mu_k)-1 =
8.200165028651807e-16. It also reproduces the earlier slow-convergence
example near 2^80. The run took 15.311 seconds and 25.2 MB peak RSS.

The second enumerates every graph on five and six vertices. It verifies
the entire size-biased distribution, the exact forcing-increment
identities, nonnegativity and normalization of the covariance kernel,
and the characteristic-function inequalities at 49 argument pairs per
joint distribution. Those final complex-number checks use floating
arithmetic; the distributional and kernel checks are exact. The run took
0.111 seconds and 17.3 MB peak RSS. Both scripts report actual nice=20,
despite the inherited-priority launcher diagnostic. Full outputs are in
recheck_moments.json and joint_verification.json; commands and relevant
values are in [LOG.md](LOG.md).

No mathematical check failed. One malformed documentation patch was
rejected before changing files and was reapplied. The finite checks do
not certify an asymptotic cutoff. The theorem concerns weak convergence
on fixed interior bands, not total-variation independence of the raw
counts or endpoint phases. Its error rate concerns characteristic
functions, not Kolmogorov distance.

The bounded literature check found no full solution. A new concrete lead
beyond the earlier report is Robert Morris and Oliver Riordan,
[*Random cliques in random graphs revisited*, arXiv:2504.00964](https://arxiv.org/html/2504.00964v1).
Section 1.3 and Theorem 1.4 describe almost-maximal clique families with
an overlap correction; this is a rigorous ingredient relevant to the
2025 cube-root announcement, but does not give its chromatic
concentration theorem. The precise statement and proof behind that
announcement remain to be obtained. The original brief's density-one
exponent 1/2 still differs from the published phase-dependent Zigzag
Conjecture, as established in the first session.

For a concrete next lemma on the present route, let M_k be the maximum
number of pairwise vertex-disjoint independent k-sets. Try to show
X_k-M_k=o_p(sqrt(mu_k)) on fixed phase bands lying below 2/3. Counting
intersecting pairs is a possible route, but it must include one-vertex
intersections, which do not appear in the covariance calculation. Such
a lemma would transfer the Gaussian fluctuations to a packing statistic;
a further relation to chi would still be needed.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first explicitly recorded local clock 04:30:05 +04.
