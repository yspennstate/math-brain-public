# Literature audit for C0002

Search date: 13 November 2026. Primary-source texts are under sources/;
the manifest records text hashes and source URLs. Page references below are
one-based PDF/printed arXiv pages unless a journal page is explicitly given.
Searches are evidence of what was located, not a proof that no other work exists.

## Exact source and normalization

[M. Biskup, arXiv:1712.09972v4](https://arxiv.org/abs/1712.09972v4),
*Extrema of the two-dimensional discrete Gaussian free field*, revised
17 August 2019; published in Springer Proceedings in Mathematics &
Statistics 304 (2020), 163–407, DOI 10.1007/978-3-030-32011-9_3.
Saved complete as sources/biskup_1712.09972.txt, 235 pages.

- Theorem 1.17, p. 14: bulk diagonal and off-diagonal Green asymptotics.
- Lemma 1.21, p. 15: potential-kernel expansion including its constant.
- Section 2, pp. 19–32; specifically Theorem 2.7, pp. 26–27,
  and Corollary 2.9, p. 27. The count's limit is Z_lambda(D)/(alpha lambda).
- Intermediate-level arguments: Lectures 3 and 4, pp. 33–58;
  Lemma 3.6, pp. 37–38; Lemma 3.10, pp. 39–40; Lemma 3.11,
  pp. 40–42; GMC identification in Sections 4.3–4.4, pp. 50–56;
  truncation beyond the second-moment phase in Section 4.5, pp. 57–58.
- Problem 16.2, p. 220, following Problem 16.1. Its three requests are a
  rate of convergence, limiting fluctuations, and probabilities of deviations
  tending to zero. Its following paragraph explicitly allows that last
  interpretation to be broad. The p. 220 designation is verified for arXiv v4;
  it should not be transferred automatically to the Springer volume pagination.
  A text-only check of the reproduced volume places the problem on p. 392;
  details are in sources/page_map.txt. The user's p. 220 matches arXiv v4.

The whole indicated sections, rather than only the abstract or problem
statement, were consulted. The source text retains form feeds for page lookup.

Normalization check: equations (2.32), (3.24) and (3.57) imply
E Z_lambda(D)=beta m_lambda with beta=alpha lambda. The displayed
(3.60)–(3.61) on arXiv v4 p. 44 appear to miss this factor in their
intensity constant. The constants in this report are derived directly
from the Gaussian tail, and checked against the independent conformal
integral, rather than copied from that display.

## Direct results for the specified DGFF count

[M. Biskup and O. Louidor, arXiv:1612.01424](https://arxiv.org/abs/1612.01424),
*On intermediate level sets of two-dimensional discrete Gaussian free field*,
Ann. Inst. H. Poincaré Probab. Statist. **55** (2019), no. 4, 1948–1987,
DOI 10.1214/18-AIHP939. The arXiv v1 and the
[author's final AIHP manuscript](https://www.math.ucla.edu/~biskup/PDFs/papers/GFF-intermediate-final-AIHP.pdf)
are both saved. Theorem 2.1, p. 3, is the process limit; Corollary 2.2,
p. 4, gives the count; Theorem 2.3(3), p. 4, gives its limiting intensity;
Theorem 2.5, p. 6, identifies it as weighted subcritical GMC. These results
establish the limit and its mean, without a quantitative N-rate or a
second-order fluctuation law. Section 2.4 discusses remaining questions.

[E. Aïdékon, Y. Hu and Z. Shi, arXiv:1710.00348v2](https://arxiv.org/abs/1710.00348v2),
*Large deviations for level sets of branching Brownian motion and Gaussian
free fields*. Original: Zapiski Nauchnykh Seminarov POMI **457** (2017),
12–36. English translation: *Large Deviations for Level Sets of a Branching
Brownian Motion and Gaussian Free Fields*, Journal of Mathematical Sciences
**238** (2019), no. 4, 348–365,
[DOI 10.1007/s10958-019-04243-8](https://doi.org/10.1007/s10958-019-04243-8).
Theorem 4.1, **arXiv v2 p. 14**, proves

\[
 \lim_{N\to\infty}{\log P(\#H_N(\lambda)\ge N^{2a})\over\log N}
   =-\left({2\lambda^2\over1-a}-2\right),
 \qquad 1-\lambda^2<a<1.
\]

Here their gamma=sqrt(2/pi)=sqrt(g) and their eta=lambda, so the threshold
and covariance normalization match exactly. The definition and setting
are on arXiv pp. 13–14; the proof occupies Section 4. This directly settles
the upper-deviation question on the scale N^{2a}, with speed log N and
the displayed exponent. In terms of X_N, its threshold is
sqrt(log N) N^{2(a-1+lambda^2)}. This tends to infinity; it is not a
fixed-multiple deviation of the limiting random mass. An attempted journal
PDF fetch returned HTML rather than PDF, so no unverified journal theorem
page is assigned; the exact theorem and arXiv page above are verified.

[O. Daviaud, arXiv:math/0406609v4](https://arxiv.org/abs/math/0406609v4),
*Extremes of the discrete two-dimensional Gaussian free field*, Ann.
Probab. **34** (2006), no. 3, 962–986,
DOI 10.1214/009117906000000061. Theorem 1.3, arXiv p. 4,
gives the high-point cardinality exponent and a quantitative lower-tail
estimate below that exponent. It concerns a fixed interior subbox. That
lower-tail estimate is also valid as an upper bound for the whole-box
small-count event, by inclusion. It is not a lower-tail estimate for a
fixed positive value of X_N, which has a nondegenerate random limit.

Explicitly, equation (1.8) in that theorem states, for every delta>0,
P(|H_N(lambda)|<=N^{2(1-lambda^2)-delta})<=exp(-c(log N)^2)
for all sufficiently large N. This gives an upper bound with speed
(log N)^2, without an identified sharp constant for this event.

Thus the broad third part already has substantive answers in print.
It would be incorrect to report all deviation questions as unresolved.

## Named nearby literature: what it does and does not supply

[M. Biskup and O. Louidor, arXiv:1606.00510](https://arxiv.org/abs/1606.00510),
*Full extremal process, cluster law and freezing for the two-dimensional
discrete Gaussian free field*, Advances in Mathematics **330** (2018),
589–687, DOI 10.1016/j.aim.2018.02.018. Theorem 2.1, p. 4; Theorem
2.3, p. 6; Theorem 2.6, pp. 8–9; Corollary 2.8, p. 10. These concern
the extremal process around m_N, cluster laws, and supercritical Gibbs
weights/freezing, rather than second-order behavior at fixed lambda<1.

[J. Junnila, E. Saksman and C. Webb, arXiv:1806.02118v2](https://arxiv.org/abs/1806.02118v2),
*Imaginary multiplicative chaos: moments, regularity and connections to the
Ising model*, Ann. Appl. Probab. **30** (2020), no. 5, 2099–2164,
DOI 10.1214/19-AAP1553. Theorems 1.1, 1.2 and 1.3, arXiv pp. 3–5,
give convergence/uniqueness, regularity, and moments of imaginary chaos.
No theorem translating those estimates into a quantitative rate for the
positive DGFF high-point count was located. Oscillatory chaoses and
real-positive high-point indicators are different observables.

[J. Junnila, E. Saksman and C. Webb, arXiv:1808.06838v3](https://arxiv.org/abs/1808.06838v3),
*Decompositions of log-correlated fields with applications*, Ann. Appl.
Probab. **29** (2019), no. 6, 3786–3820, DOI 10.1214/19-AAP1492.
Theorem A, p. 2, and Theorem 4.5, p. 13, supply decompositions;
Theorem 5.3, pp. 17–18, treats critical chaos; Theorem 6.1, pp. 20–21,
gives holomorphic dependence on the chaos parameter. This last result
supports studying parameter derivatives as possible fluctuation terms.
It does not identify the fluctuation of a threshold count or specify
a finite-difference DGFF-to-continuum rate.

[H. Lacoin, R. Rhodes and V. Vargas, arXiv:1307.6117](https://arxiv.org/abs/1307.6117),
*Complex Gaussian multiplicative chaos*, Comm. Math. Phys. **337**
(2015), 569–632, DOI 10.1007/s00220-015-2362-4. Theorem 3.1, p. 11,
is convergence in the inner phase I; Theorem 4.2, p. 22, gives Gaussian
white-noise limits in phase III. These are complex-exponential phase
limits, not a count CLT in the present model. More recent Lacoin work
located includes arXiv:2301.05274, *Convergence for Complex Gaussian
Multiplicative Chaos on phase boundaries* (2023/2024); its object is
again complex chaos. No DGFF-count answer was found in these searches.

[C. Garban, N. Holden, A. Sepúlveda and X. Sun, arXiv:1805.00864v2](https://arxiv.org/abs/1805.00864v2),
*Negative moments for Gaussian multiplicative chaos on fractal sets*,
Electron. Commun. Probab. **23** (2018), paper 100, 1–10,
DOI 10.1214/18-ECP168. Theorem 1.1 and Remark 1.2, arXiv p. 3,
give all negative moments and faster-than-any-power small-mass bounds
for the limiting subcritical GMC. Weak convergence does not permit
substituting an N-dependent shrinking threshold into this result. It
therefore does not itself give a finite-N lower-deviation estimate.

[N. Berestycki, C. Webb and M. D. Wong, arXiv:1701.03289](https://arxiv.org/abs/1701.03289),
*Random Hermitian matrices and Gaussian multiplicative chaos*, Probab.
Theory Related Fields **172** (2018), 103–189,
DOI 10.1007/s00440-017-0806-9. Theorem 1.1, arXiv p. 2, is a
subcritical GMC limit for characteristic-polynomial powers in unitary
invariant Hermitian ensembles. It does not estimate the DGFF count.

[J. Junnila, G. Lambert and C. Webb, arXiv:2209.06548v2](https://arxiv.org/abs/2209.06548v2),
*Multiplicative chaos measures from thick points of log-correlated fields*,
Comm. Pure Appl. Math. **77** (2024), no. 11, 4212–4286,
DOI 10.1002/cpa.22205 (first published 17 May 2024).
Theorem 1.8, p. 7, identifies thick-point and exponential-chaos limits
in L1 under its assumptions. Theorem 1.4, p. 4, applies to continuum
mollifications; Theorem 1.2, p. 3, to CUE. The discussion on p. 5
explicitly leaves graph-discretization modifications uncarried out.
This is the most directly relevant later framework located, but its
stated convergence does not provide the requested DGFF N-rate or
second-order fluctuation law.

[J. Aru, T. Lupu and A. Sepúlveda, arXiv:1805.09204](https://arxiv.org/abs/1805.09204),
*The first passage sets of the 2D Gaussian free field: convergence and
isomorphisms*, Comm. Math. Phys. **375** (2020), 1885–1929,
DOI 10.1007/s00220-020-03718-z. Proposition 4.7, arXiv p. 21,
and Proposition 4.11, p. 23, concern convergence of
metric-graph first passage sets, local sets, and Minkowski content.
These are distinct from the number of vertices above a height growing
as a fixed fraction of the maximum. No count-rate/CLT result was located.

E. Bolthausen, J.-D. Deuschel and G. Giacomin, *Entropic repulsion and
the maximum of the two-dimensional harmonic crystal*, Ann. Probab.
**29** (2001), 1670–1692, DOI 10.1214/aop/1015345767, is the
background source for the maximum and hard-wall entropic repulsion.
Its results are not here asserted to give an exact rate function for
small normalized high-point mass: a hard-wall event and that event
are not equivalent. An accessible full text was sought separately;
any access failure is recorded rather than hidden by a guessed theorem.

## Searches with no verified matching citation

The suggested Kim–Lee title "Large deviations for intermediate level sets"
could not be verified by exact-title and combined author/title searches.
Likewise, no Cerf–Dembo joint result on this DGFF count was verified.
This is not an assertion that these people have no related work.

Representative queries used: "intermediate level sets" "large deviations";
"intermediate level sets" "convergence" "rate"; "Gaussian free field"
"level set size" fluctuations; "Gaussian free field" "moderate deviations"
"level sets"; DGFF fluctuations level 2024 2025 2026; Kim Lee Gaussian
free field deviations; Cerf Dembo Gaussian field deviations; rate of
convergence Gaussian multiplicative chaos; and author/name combinations
for every group listed above. Searches through 2026 also returned
dimension >=3 cluster-count CLTs (McAuley–Muirhead, arXiv:2501.14707),
integer-valued surfaces with floors, and BBM results. These were not
treated as solutions of the specified zero-boundary two-dimensional count.

## Assessment

Located direct results settle substantial upper and lower deviation regimes.
The searches and full-text checks did not locate a quantitative convergence
rate or a limiting second-order fluctuation law for the stated count.
Accordingly this project uses PARTIAL, not RESOLVED_IN_LITERATURE.
The estimates in PROOFS.md address a remaining quantitative aspect, with
the distinction between finite-lattice chaos and the continuum limit explicit.
