Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-03 source-status reconciliation: E0034

Run date: 2026-09-18 UTC  
Slot: R7-03 Boundary-Case Research  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Own root: `research7_2026-09-17/R7-03/`  
Start-of-run master snapshot: `48b7d98ad4277d4654d0a4aa9e9e5811ab4e2f87`  
Fresh pre-write master snapshot: `0732d401b39c7e5f6fc5b489b875895fc3cb974d`  
Candidate state: **REJECT AS KNOWN / RESOLVED IN LITERATURE**; no claim created.

## 1. Exact source and source scope

Canonical intake ID: `E0034`. It satisfies the R7-03 shard gate because `sum(ord(c) for c in "E0034") mod 7 = 2`.

Original outside source:

- Author: Sourav Chatterjee.
- Title: *A general method for lower bounds on fluctuations of random variables*.
- Original arXiv submission: 2017; source version checked: arXiv v3, 2018-07-26; published in *Annals of Probability* 47(4), 2019.
- Source URL: https://arxiv.org/abs/1706.04290 and HTML source version https://arxiv.org/html/1706.04290v3.
- Exact locator: Section 3, Open problems, item (6), PDF p. 27 in the intake; the HTML version states verbatim: “Extend the lower bound result for first-passage percolation to the case of discrete edge weights.”

The source's FPP result preceding the open problem required a smooth-density class. The later literature explicitly identifies that regularity restriction and removes it.

Historical repository intake at the captured snapshot classified E0034 as `attempted_unsolved`; prior attempt `E0034-A001` correctly noticed that a naive symmetric resampling perturbation loses monotone sign, but incorrectly treated that as the surviving barrier. No canonical `operations/claims/E0034.md` exists at the start snapshot. A separate 2026-09-18 successor screen had also called E0034 HARD; the source-status check below supersedes that screening classification.

## 2. Dated literature check

Checked on 2026-09-18.

### 2.1 Bates–Chatterjee

Erik Bates and Sourav Chatterjee, *Fluctuation lower bounds in planar random growth models*, arXiv:1810.03656 (first posted 2018-10-08; checked v5, 2021-08-26), published in *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 56(4), 2020.

Their paper says the earlier Chatterjee lower bound applied to distributions satisfying the smooth condition (2.3), and then states that its result expands the FPP lower bound to “optimal generality.” Theorem 3.1 says: if `s = ess inf X_e` and

`P(X_e = s) < p_c(Z^2)`, 

then for every sequence `y_n` with `||y_n||_1 >= n`, the fluctuations of `T(0,y_n)` are at least order `sqrt(log n)`.

Theorem 3.3 covers the positive-minimum regime under the natural oriented-percolation condition

`s > 0`, `P(X_e=s) < \vec p_c(Z^2)`,

plus a weak moment condition. Their Remark 3.4 records the complementary percolation-cone obstruction. Their paper also states that the independent Damron–Hanson–Houdré–Xu work removes the extra moment condition in this positive-minimum regime.

Crucially, these theorems place **no continuity requirement on the edge-weight law**. They therefore include finite or countably supported discrete edge-weight laws whenever the standard nondegeneracy/percolation conditions hold.

### 2.2 Damron–Hanson–Houdré–Xu

Michael Damron, Jack Hanson, Christian Houdré and Chen Xu, *Lower bounds for fluctuations in first-passage percolation for general distributions*, arXiv:1810.08270 (posted 2018-10-18), published in *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 56(2), 2020, DOI 10.1214/19-AIHP1004.

Their abstract says that the stronger fluctuation statements had previously been proved for special edge-weight distributions and that they obtain them for **general edge-weight distributions**. In the paper, the FPP condition is the standard one excluding the zero-edge supercritical regime and, for positive infimum, the oriented-percolation flat-edge regime. This is independently source-matching evidence that Chatterjee's item (6) was solved shortly after the source paper.

No negative search is being used to certify status: the rejection is based on positive, direct source-matching theorems.

## 3. B2 — attack the unrestricted negation / identify the necessary obstruction

A literal reading “all discrete edge-weight laws” cannot support a universal `sqrt(log n)` fluctuation lower bound. Let a discrete law have `s=0` and

`P(X_e=0) > p_c(Z^2)=1/2`.

Then the zero-weight edges percolate. As recorded explicitly in Bates–Chatterjee Remark 3.2 and Damron–Hanson–Houdré–Xu Remark 1, point-to-point passage times can be stochastically tight rather than having diverging `sqrt(log n)` fluctuations. Thus the correct source-level extension must preserve the standard anti-percolation hypothesis; discreteness itself is not the obstruction.

Similarly, if `s>0` and the atom at `s` lies above the oriented percolation threshold, directions inside the oriented percolation cone have only order-one centered fluctuations. This explains the exact boundary in the later theorems.

So the mathematically correct dichotomy is:

- **nonpathological discrete laws:** `sqrt(log n)` fluctuation lower bound holds;
- **percolative minimal-weight laws:** a universal such lower bound is false for geometric reasons unrelated to atomicity.

This quantifier correction matters because it prevents misclassifying the natural percolation obstruction as a failure to solve the discrete-law problem.

## 4. B6 — deform the smooth-law proof to atoms via an exact monotone coupling

The original Chatterjee method used multiplicative perturbations adapted to smooth densities. Bates–Chatterjee replace this by a coupling available for every probability law.

Let `X, X^(1),...,X^(m)` be i.i.d. with arbitrary law `mu` and define

`X^max = max(X,X^(1),...,X^(m))`.

Then `X^max >= X` pointwise, so the perturbation has a fixed sign. Moreover `Law(X^max) << mu` and its Radon–Nikodym derivative is bounded by `m+1`.

For a discrete law with ordered atoms `a_j`, masses `p_j`, and cumulative masses `F_j = sum_{i<=j} p_i`, this bound has the exact elementary form

`P(X^max=a_j) = F_j^(m+1)-F_(j-1)^(m+1)`

and therefore, whenever `p_j>0`,

`P(X^max=a_j)/p_j = sum_{r=0}^m F_j^(m-r) F_(j-1)^r <= m+1`.

Thus the universal absolute-continuity estimate is especially transparent for a purely atomic distribution. The analogous minimum coupling has the same bound using tail probabilities.

Now Bernoulli-thin the replacement: independently on each edge, replace `X` by `X^max` with probability `epsilon`. Bates–Chatterjee's Hellinger calculation gives a one-edge affinity `1-O(epsilon^2)` and hence, for independent edges with perturbation probabilities `epsilon_i`,

`d_TV(product original, product perturbed) <= C (sum_i epsilon_i^2)^(1/2)`.

This is precisely the quadratic perturbation cost needed for the multiscale fluctuation argument, and it requires no density.

### Binary sanity check

For `X in {0,1}` with `P(X=0)=p`,

`P(X^max=0)=p^(m+1)`,
`P(X^max=1)=1-p^(m+1)`.

The likelihood ratios are `p^m` at zero and

`(1-p^(m+1))/(1-p)=1+p+...+p^m <= m+1`

at one. Under the natural coupling, `X^max-X` equals one exactly on the event that `X=0` and at least one auxiliary copy is one, of probability

`p(1-p^m)`.

Hence the later coupling not only survives atoms; in the simplest discrete case its monotonicity and nontrivial shift can be computed exactly.

## 5. B30 — localize the old gluing failure

Prior attempt E0034-A001 used ordinary resampling and identified a random-sign cancellation. That is a real defect of **that coupling**, not a structural defect of discrete FPP.

The min/max construction localizes and removes the failure:

1. `max` gives an upward perturbation edge by edge and `min` gives a downward perturbation edge by edge, so there is no first-order sign cancellation.
2. The perturbed law remains absolutely continuous with uniformly bounded density relative to the original law, even when the original law is atomic.
3. Bernoulli thinning makes the one-coordinate Hellinger loss quadratic in the perturbation probability.
4. Tensorization converts that to the needed product total-variation control.
5. FPP geometry then converts the monotone edge perturbations across dyadic annuli into the `sqrt(log n)` passage-time fluctuation lower bound.

Therefore the precise old gluing failure was **coupling choice**, not discreteness. The later literature supplies exactly the missing monotone atomic coupling.

## 6. Source-level corollary for discrete laws

A direct specialization of Bates–Chatterjee Theorem 3.1 gives:

**Corollary.** Let the edge weights in planar FPP be i.i.d., nonnegative, nondegenerate and discrete. Put `s=ess inf X_e`. If

`P(X_e=s) < p_c(Z^2)`,

then for every sequence `y_n` with `||y_n||_1 >= n`, the passage time `T(0,y_n)` has fluctuations at least of order `sqrt(log n)` in the same concentration-function sense used by Chatterjee.

If `s>0`, the condition can be relaxed to `P(X_e=s) < \vec p_c(Z^2)` under the standard weak moment assumption of Bates–Chatterjee Theorem 3.3; Damron–Hanson–Houdré–Xu remove that extra moment condition. In particular, every finite-support discrete law satisfying the appropriate minimum-atom percolation condition lies in the solved class.

This is exactly the mathematical extension asked for in Chatterjee's Open Problems item (6), modulo the standard pathologies for which the desired conclusion is genuinely false.

## 7. Admission disposition

E0034 must **not** be admitted by R7-03. Recommended status is:

`KNOWN / RESOLVED_IN_LITERATURE_2018_2020`.

This run does not edit the shared intake, QUEUE, RESULTS, or POSTED ledgers; coordinator reconciliation owns those changes. No `operations/claims/E0034.md` is created.

R7-03 therefore remains `PENDING_ADMISSION` and its successor metric stays `UNKNOWN/UNMEASURED`; no target-specific stagnation count starts.

## 8. References checked

- Sourav Chatterjee, *A general method for lower bounds on fluctuations of random variables*, arXiv:1706.04290v3 (2018 source version), Ann. Probab. 47(4), 2019.
- Erik Bates and Sourav Chatterjee, *Fluctuation lower bounds in planar random growth models*, arXiv:1810.03656v5, Ann. Inst. H. Poincaré Probab. Statist. 56(4), 2020.
- Michael Damron, Jack Hanson, Christian Houdré and Chen Xu, *Lower bounds for fluctuations in first-passage percolation for general distributions*, arXiv:1810.08270, Ann. Inst. H. Poincaré Probab. Statist. 56(2), 2020, DOI 10.1214/19-AIHP1004.
