# Independent referee report

15 November 2026, Asia/Tbilisi. Manuscript examined: `claim_files/paper/main.tex`, lines 1–427; SHA-256 `149a83c091a8807bb5dcffdd5e7d1167142c27a5d2aa9e0e428d5bbc52a8a660`.

Overall verdict: MINOR. The proof of both parts of Theorem 1.1 is sound. The needed changes concern the description of novelty, the wording about conditional bridges, one missing hypothesis in the lattice lemma, conventions for empty sets, and bibliographic clarification. I found no reason to classify the dimension-four argument as MAJOR or WRONG. This conclusion concerns the supplied manuscript, not every argument in its references.

The dimension-five conclusion is already a consequence of the finiteness theorem in Chen's 2026 thesis, read with the same necessary off-diagonal convention. This includes part (b), since finite sets have upper box dimension zero. The thesis contains errors in its displayed proof; those errors should be identified precisely and should not serve as an implicit claim that the dimension-five conclusion is new. An independent covering argument recovering finiteness is given below.

| Item | Verdict | Finding |
| --- | --- | --- |
| Sources as quoted | SOUND | The quoted open-problem ranges, quantifiers and formulas match the specified arXiv version. Its diagonal and zero-slice defects are real. |
| Novelty | MINOR | Dimension five is prior work; make this consequence explicit. No earlier all-s dimension-four result was located in the searches described below. |
| `lem:var` | MINOR | The inequality is sound. Independence applies to centered bridge residuals, not to the uncentered process with random pinned endpoints. |
| `lem:smallball` | SOUND | Density, ball volume, regularization and constants are correct. |
| `lem:lattice` | MINOR | The estimate and proof are sound for nonempty anchor sets. Nonemptiness is missing from its standalone statement. |
| `lem:moments` | SOUND | Ordered tuples, repetitions, conditioning and the factorial constant are handled correctly. |
| `lem:holder` | SOUND | The two-parameter Kolmogorov exponent and continuous-version argument are correct. |
| Theorem `thm:main` (a) | SOUND | The countable-union argument gives all positive slices on one event. |
| Theorem `thm:main` (b) | SOUND | The grid-slice union, transfer and upper box covering argument are valid. |
| Remarks | MINOR | The low-dimensional formula and dimension non-subtraction example are correct; clarify prior dimension-five consequences and source conventions. |
| Numerics | SOUND | Supplied checks reproduce within floating-point error; independent covariance, Gaussian integration and simulation checks found no contradiction. |
| Bibliography | MINOR | No fabricated entry found. Explain the chapter/volume year discrepancy; retain printed KWX06 author order. Lyons's original article pagination was not directly inspected. |

## 1. Source verification

The correct preprint is [arXiv:math/0510518v1](https://arxiv.org/abs/math/0510518v1), submitted 24 October 2005. It is not math/0511054. The manuscript already gives the correct identifier at lines 404–405. Downloaded sources and layout-preserving extracts are in `referee_sources/`; the following text-line numbers refer to [Kho05.txt](referee_sources/Kho05.txt). The mathematical displays below transcribe the source; ellipses do not change their quantifiers.

| Manuscript | Source location | Source formula or short quotation | Assessment |
| --- | --- | --- | --- |
| 51–54 | p. 3, (1.9); text 121–127 | `D_d := {s >= 0 : B(s,t_1)=B(s,t_2) for some t_2>t_1>0}`; `(1.10): P{D_d != {0}}>0 <=> d<=5` | Definition, dimension range, positive probability and attribution to Lyons match. |
| 54–56 | p. 4, (1.12); text 133–141 | `dim_H D_d = 1 wedge (3-d/2)^+`, a.s. | Mountford attribution and the dimension-one value for d=4 match. Fixed-s nonintersection plus Fubini gives zero Lebesgue measure. |
| 58–65 | pp. 33–34, (8.2), Open Problem 2; text 1738–1746 | `Y_d(s) := {(t_1,t_2) in R_+^2 : B(s,t_1)=B(s,t_2)}`; `d in {4,5}`; `dim_H Y_d(s)=0`, `s>=0`; “outside a single null-set”; “I conjecture that the answer is ‘yes.’” | The source really prints the diagonal-inclusive definition and includes s=0 in this question. |
| 84–89 | p. 34, Open Problem 3; text 1755–1760 | `d in {4,5}`; `Y_d(s)` finite, `s>0`; “outside a single null set”; “likely to be ‘no.’” | The manuscript states its quantifiers correctly. The source expects a negative answer and entertains uncountable exceptional fibers. |
| 99–103 | p. 33, (8.1); text 1727–1736 | `dim_H Dhat_d=(3-d/2)^+`; `dim_H Dbar_d=2 wedge (3-d/2)^+`, a.s. | The stated three-parameter zero-set dimension is the intended off-diagonal conclusion. |
| 101 | p. 20, Theorem 5.1, (5.2); text 983–988 | `E compact subset (0,infinity)^2`, `G compact subset (0,infinity)^3`; `Cap_(d/2)(G)>0 => P{Dhat_d intersect G != empty}>0 => H_(d/2)(G)>0`; `Cap_((d-2)/2)(E)>0 => P{Dbar_d intersect E != empty}>0 => H_((d-2)/2)(E)>0` | The cited theorem supplies hitting criteria, with the dimension statement obtained by the codimension argument in Section 8.2. It is not itself a theorem about every fiber. |

There is an additional convention issue in the source: its definitions (5.1), text 971–977, also omit the distinct-time restriction. Taken literally, `Dhat_d` contains the two-dimensional surface `(s,t,t)`, contradicting (8.1) in dimensions four and five. Thus the restriction is needed when using Theorem 5.1 and (8.1), as well as when reading (8.2). Manuscript lines 99–101 already say away from the diagonal and s=0; retain that qualification. An optional sentence could make explicit that the source's distinct-time convention is implicit in those displays too.

The repair at manuscript lines 63–67 is fair. Independently of the source's intended meaning, the continuous Brownian sheet has `B(0,t)=0` for every t on one event, so `Y_d(0)=[0,infinity)^2`. For s>0, `Y_d(s)` always contains `{(t,t):t>=0}`. Consequently the literal dimension-zero question is false, and the literal finiteness question is false. Restricting to s>0 and u unequal to v recovers the substantive double-time question. The manuscript discloses the repair rather than silently attributing the corrected definition to the source.

The source's Remark 1.5, text 140, has a further typographical `R_+^d` for the one-dimensional slice-parameter set. The manuscript's statement that every positive slice has double points for d<=3 is the intended Penrose result; it does not repeat that typographical error.

No fix is needed to the quoted mathematical facts at lines 48–65 or 99–106, subject to these stated conventions. These checks used the [preprint PDF](https://arxiv.org/pdf/math/0510518), not equation numbers inferred from the publisher's abstract.

## 2. Novelty and Chen's thesis

The [EPFL record](https://infoscience.epfl.ch/entities/publication/a90f4af0-e1aa-47fa-929e-148198a9855b) identifies Keming Chen's *Uniform dimension results of level-sets of stable sheets*, thesis 11211, 2026, supervised by Thomas Mountford, [DOI 10.5075/epfl-thesis-11211](https://doi.org/10.5075/epfl-thesis-11211). The full [PDF](https://infoscience.epfl.ch/bitstreams/8d7f6337-2a97-4e51-8f31-0ed34f610a55/download) was downloaded as [Che26.pdf](referee_sources/Che26.pdf), and read, including Chapter 4.4. Locations below refer to [Che26.txt](referee_sources/Che26.txt).

| Thesis location | Content and consequence |
| --- | --- |
| p. 7, (1.7), text 446–452 | Defines a pair set `D_d(s)` with the same omitted diagonal restriction as Kho05. Literal finiteness would be impossible. |
| p. 7, Theorem 1.3.3, text 475–476; pp. 107–108, text 5897–5939 | Claims finiteness of the double-time set for every slice in dimension five. The chapter is addressing the common-null-set question; it is not merely a fixed deterministic-s statement. Read with u unequal to v and s>0, it implies both (a) and (b) of this manuscript in d=5. |
| p. 7, Theorem 1.3.4, text 482–484; p. 108, text 5990–5991 | In dimension four, each interval `(s,s+epsilon)` contains a slice with infinitely many double times. This does not give positive Hausdorff dimension, and does not contradict the manuscript. |
| p. 107, (4.42), text 5883–5892 | Makes the Brownian-sheet identification mentioned in manuscript lines 88–89. That identification is false. |
| p. 107, (4.44), text 5902–5933 | Uses an incorrect small-ball power `2pd` for a vector in `R^(pd)`. |

Part (a) for d=5 is therefore a previously stated theorem's consequence, and so is part (b). Remark `rem:scope` correctly reports the intended contents of Theorems 1.3.3 and 1.3.4 and correctly identifies the issue at (4.42). Its use of “states” is defensible because of the defects in the thesis proof. What is missing is the explicit consequence for novelty. Lines 83–89 should say that the d=5 conclusions already follow from the earlier finiteness result, while the present argument establishes the dimension-four bound and independently recovers dimension five. That clarification should also be visible near the abstract's claim at lines 32–35; no theorem needs to be removed.

The error at (4.42) can be checked without any difficult probabilistic theorem. At deterministic s, write the two local, independent slice increments as `U(x)` and `V(y)`, with Brownian variance rate s. Their difference `F(x,y)=V(y)-U(x)` satisfies

`Cov(F(x,y),F(x',y')) = s[min(x,x') + min(y,y')]`.

A Brownian sheet has product covariance, not this sum. Every rectangular mixed increment of F is identically zero; a Brownian sheet's nondegenerate rectangular increment has positive variance. This remains a counterexample regardless of the thesis's additional issues with choosing random intersection points. Replace the manuscript's brief observation with this covariance computation if the criticism of the thesis is retained.

There is a separate error in (4.44): `X_(2p)` has pd independent scalar coordinates after separating its p vector differences, not 2pd. With bounded nondegenerate covariance its small-ball order is `r^(pd)`. The corrected covering exponent is

`2(2p+1)-pd = 2-p` when d=5,

which is negative for p>=3. Thus the displayed mistake does not by itself refute the finiteness conclusion. One must still justify nondegeneracy and handle repeated endpoints. The manuscript should not suggest that the false covariance identification alone invalidates the dimension-five result or restores novelty there.

Here is an independent way to close those issues, also checking the magnitude of that conclusion. Localize s to `[a,b]`, times to `[0,T]`, and distinct endpoint separations to at least epsilon, then take countable unions.

1. A triple point gives two independent Brownian increments between three ordered times. Their joint d=5 covariance is bounded below on the localized set. The parameter count is four, and the Gaussian vector dimension is ten. A grid of mesh delta, Holder transfer with alpha<1/2, and a density bound give a probability at most `C delta^(10 alpha-4)` on the event that the Holder constant is at most a fixed M. Choose alpha>2/5. This excludes triple points on every positive slice simultaneously.
2. Three distinct unordered double-time pairs must then have six distinct endpoints. For any fixed pairing, the three Brownian interval-indicator functions are linearly independent: taking distributional derivatives at an endpoint belonging to only one pair forces its coefficient to vanish. Their Gram matrix is positive definite; compactness and endpoint separation give a uniform positive least eigenvalue. There are seven parameters and fifteen Gaussian coordinates. The same covering bound is `C delta^(15 alpha-7)`, which tends to zero for alpha>7/15. There are finitely many pairings, followed by countably many localizations and bounds on M.

It follows that every positive slice in dimension five has at most two unordered double-time pairs, hence at most four ordered off-diagonal pairs, on one event. This independent argument is sufficient to recover finiteness without treating (4.42) as a Brownian sheet. It is supplied here to assess the prior-result caveat, not as a claim that the thesis's printed proof is correct.

Literature search, conducted 15 November 2026:

| Source checked | What it addresses; relevance to novelty |
| --- | --- |
| [KWX06](https://doi.org/10.1214/EJP.v11-353), full PDF | Sectorial LND, uniform image dimensions and multiple points of the full sheet. No all-s off-diagonal double-time dimension theorem was found there. |
| [Dalang et al. 2012](https://arxiv.org/abs/1009.0235), full PDF | Full-sheet double points and critical dimension d=4N, not the present family of fibers with a shared slice parameter. |
| [Dalang–Mueller 2015](https://arxiv.org/abs/1303.0403), full PDF | Full-sheet k-multiple points in critical dimensions. It does not state this dimension-four fiber result. |
| [Zhenlong Chen 2013](https://www.wseas.org/multimedia/journals/mathematics/2013/56-153.pdf), full PDF | Polar sets and capacity/dimension bounds for generalized-sheet slice sets; Theorem 5 concerns the full three-parameter coincidence set and its projection, not zero-dimensionality of every double-time fiber. Distinguish this author from Keming Chen. |
| [Chen–Woessner 2025](https://doi.org/10.1007/s10959-024-01399-1), publisher text and [arXiv:2405.20019](https://arxiv.org/abs/2405.20019) | Simultaneous projection dimensions of the sheet's zero set. This addresses Open Problem 4, not the present Open Problem 2. |
| Chen 2026, Chapter 4.4 | Prior dimension-five finiteness; dimension-four infinitude, with the proof qualifications above. |

Searches included combinations of “Brownian sheet”, “double times”, “double-time”, “slices”, “self-intersections”, “dimension zero”, “Open Problem 2”, and “Keming Chen”, and searches restricted to arXiv. The direct [arXiv API query](https://export.arxiv.org/api/query?search_query=all:%22Brownian%20sheet%22%20AND%20all:slices&start=0&max_results=100), retained in `arxiv_slice_search.xml`, returned only Kho05. Google Scholar with `as_ylo=2005` returned a verification page, retained as `scholar_since2005.html`; it was not a usable search result. The negative finding for d=4 is a report of the searches and sources checked, not proof that no other result exists.

## 3. Section 2: conditional variance and small balls

### Lemma `lem:var`, manuscript 139–180

| Lines | Check |
| --- | --- |
| 139–150 | The interval separation ensures every pair is off the diagonal. Adding all four interval endpoints ensures the nearest surrounding anchors for u are in U, and those for v are in V. No grid separation hypothesis is used. |
| 154–159 | The claimed constant a/2 is valid uniformly in s in `[a,b]`. The proof actually gives s/2 before using s>=a. |
| 163–168 | Every earlier scalar difference is measurable from the anchor values. For these Gaussian linear sigma fields both conditional variances are deterministic. Enlarging the conditioning space decreases the squared projection residual, including when the earlier covariance matrix is singular. |
| 170–176 | If ell<u<m are consecutive anchors, the residual variance is `s(u-ell)(m-u)/(m-ell)`. If h is the smaller adjacent distance and H the larger, this is `s h H/(h+H) >= s h/2`. If u is an anchor, both quantities are zero. |
| 177–180 | Residuals on the two separate pinned intervals are independent. The variance of their difference is the sum of their variances. This proves the displayed lower bound. |

The conditional-variance identity at lines 165–166 should be read in this deterministic Gaussian setting. For arbitrary sigma fields the identity gives an expectation of `Var(Z|G)` conditional on F, not a general pointwise inequality with the random quantity `Var(Z|G)`. The preceding Gaussian qualification makes the application correct. A short Gaussian projection argument would avoid suggesting an invalid general statement.

The wording at lines 170–171 is literally inaccurate: the process W pinned at random anchor values is not independent of those values. Define the residual on each anchored interval by

`beta(t)=W(t)-[(m-t)W(ell)+(t-ell)W(m)]/(m-ell)`.

These centered bridges are independent of the anchor sigma field and of one another. Subtracting the linear interpolants does not change the conditional variances. Fix: replace “the process W ... independent of G” by a statement about these residual bridges. This is a wording repair, not a failure of the variance estimate.

Adversarial endpoint checks:

- If an earlier endpoint is epsilon away from u, the lower bound can be only order epsilon. There is no lower bound of order delta uniform over arbitrary configurations. The proof never needs one.
- If an earlier endpoint coincides with u, its contribution to rho is zero. The v contribution still works if v is not an anchor.
- If both coordinates are anchors, rho=0, even if the new difference is not determined by the earlier differences. The lower bound is then deliberately uninformative but true.
- If the new pair repeats an earlier pair, the actual conditional variance is zero and rho=0. This is also allowed.
- The four differences from the corners of a rectangle of pairs satisfy a linear relation. When the fourth pair is predicted by the other three, both its coordinates are already anchors, so rho=0. The estimate does not incorrectly assume full rank.

Uniformity as a approaches zero is neither claimed nor true with a positive fixed constant. The subsequent proof localizes to a>0 and takes a countable union.

### Lemma `lem:smallball`, manuscript 183–202

Conditioning on all vector differences preserves independence between coordinate blocks, because the blocks were independent and each is conditioned only through its own data. Each target coordinate has the same deterministic conditional variance sigma squared, and an arbitrary conditional mean. For rho>0 the maximum joint density is `(2 pi sigma^2)^(-2)`. The Euclidean four-ball has volume `pi^2 r^4/2`. Therefore

`P{|X|<=r | past} <= r^4/(8 sigma^4) <= r^4/(2 a^2 rho^2)`.

The calculation at lines 195–198 is correct. For rho<=r squared, `C r^4/(r^2+rho)^2 >= C/4`; take C>=4. For rho>r squared, `(r^2+rho)^2<=4 rho^2`; take C>=2/a squared. Thus the displayed choice `C=max(4,2/a^2)` works. It also covers rho=0 and zero conditional variance by the bound one. No bound on the conditional mean is required, and no hidden dependence on the number of earlier pairs occurs. The conditional-probability claim is an almost-sure claim on the conditioning law's support, as line 188 says.

## 4. Section 3: lattice sums and moments

### Lemma `lem:lattice`, manuscript 207–231

The standalone statement at line 211 permits U or V to be empty, making the minimum in rho undefined. Fix: require `1<=|U|,|V|<=k+2`. All anchor sets used in the proof of the main theorem already have at least two points, so this omission has no downstream effect.

For nonempty U and V the estimate is correct:

1. Assigning to a nearest anchor is legitimate, including ties, which can be broken deterministically. The proof does not require anchors on the lattice.
2. Each distance shell `[j delta,(j+1)delta)` contains at most two lattice points around a fixed anchor. The intervals written at lines 221–222 have length delta and are half-open, so each contains exactly one point of the infinite lattice. At j=0 an anchor on the lattice can be counted twice in this upper bound, which is harmless.
3. Distances are at most the corresponding interval lengths, so j+l<=L/delta. For q=j+l there are q+1 nonnegative ordered choices of j,l. The factor four accounts for both sides of both anchors.
4. With lambda=r squared/delta>=1, `(q+1)/(lambda+q)^2<=1/(q+1)`. Summing gives the harmonic logarithm. The q=0 term is bounded because r squared>=delta.
5. Replacing `1+log(1+L/delta)` by `C_L[1+log(1/delta)]` is uniform for 0<delta<=1. The constant depends only on the two lengths, not anchor separation, anchor positions or s.

The logarithm comes from the two endpoint-distance variables against a degree-minus-two kernel. It does not come from ordering the pairs or from the later union over slice parameters. A sharper version would retain a logarithm involving r, but the printed bound is sufficient.

### Lemma `lem:moments`, manuscript 239–262

The expansion at lines 250–252 is the ordinary p-th moment: all ordered p-tuples of grid pairs are included, with repetitions. There is no requirement to order u coordinates, v coordinates or pair spans. No sorting argument, omitted permutation or factor p factorial is needed.

For fixed first p-1 pairs, the probability of their intersection is multiplied by a deterministic upper bound for the last conditional event. Earlier events are measurable with respect to the conditioning vector, and the small-ball bound is uniform in its values. Summing the last pair first is therefore valid even if its conditional covariance is singular. This proves lines 256–259 without any independence assertion between the pair events.

The last-pair anchor sets have at most p+1 points each. The lattice sum gives `C(p+1)^2 Lambda`. Iterating down through j=1 gives

`E N^p <= C^p [product_(j=1)^p (j+1)^2] Lambda^p = C^p ((p+1)!)^2 Lambda^p`.

For p=1 the two boundary anchors in each interval suffice. Dependence only on p, a and the two lengths is as stated; dependence on b or the inter-interval gap is not needed for this deliberately loose bound. For fixed p the factorial growth causes no problem in the later argument.

### Explicit p=2 attack

For one scalar coordinate, write `h=v-u`, `h'=v'-u'`, and `c=min(v,v')-max(u,u')`. All these intervals overlap because I lies entirely before J. Directly from independent Brownian increments,

`Cov((X_1,X_2)) = s [[h,c],[c,h']]`,

`Var(X_2 | X_1) = s[h'-c^2/h]`.

This is an independent formula against which the bridge estimate can be checked. Repeated pairs give c=h=h' and zero conditional variance. One shared endpoint and a change epsilon in the other gives variance of order s epsilon. For example, `(u,v)=(1/2,5/2)` and `(u',v')=(1/2+epsilon,5/2+epsilon)` give `s(2 epsilon-epsilon^2/2)`; for small epsilon the manuscript's lower bound with s in place of a is s epsilon. Approaching an earlier endpoint therefore does not break the estimate.

In the exact second-moment sum, repetitions contribute `E N`, not `(E N)^2`. They are not lost: the regularized conditional kernel allows probability one when rho=0. Indeed `r^4 delta^(-2)>=1` under the hypothesis r squared>=delta. The moment scale is large enough to absorb these terms. Explicit integration of the above two-pair law is reported in Section 6.

### What the dimension-five analogue can and cannot say

The manuscript does not claim `(r^5 delta^(-2) log(1/delta))^p` in dimension five. Such a claim would be false. At r squared=delta and on fixed separated intervals, `E N` is of order `r^5 delta^(-2)=delta^(1/2)`. Since N is integer-valued, `E N^2>=E N`; the proposed squared dimension-five scale is only order `delta log^2(1/delta)`. Their ratio diverges.

The direct five-dimensional small-ball kernel is instead bounded by `C r^5/(r^2+rho)^(5/2)`. Summing its two-dimensional lattice shells gives `C(k+2)^2 r^4 delta^(-2)` with no logarithm: the sum of `(q+1)/(r^2/delta+q)^(5/2)` is bounded by a constant times `(r^2/delta)^(-1/2)`. Iteration gives a valid bound `C_p(r^4 delta^(-2))^p`. Using the actual unconditioned variance for the first factor improves this, for fixed positive gap, to

`E N^p <= C_p r^5 delta^(-2) (r^4 delta^(-2))^(p-1)`.

Neither improvement is required. Lines 326–329 correctly project to four coordinates and use the dimension-four theorem. This avoids an unjustified replacement of every r-fourth-power by an r-fifth-power.

## 5. Section 4 and the theorem

### Holder lemma, manuscript 267–281

The increment decomposition in lines 276–278 gives a variance bound by a constant times `|s-s'|+|t-t'|` on a compact rectangle. The Gaussian q-th moment is bounded by a constant times the q/2 power of the maximum parameter distance. With parameter dimension two, Kolmogorov gives exponent strictly below `1/2-2/q`. For each prescribed alpha<1/2 choose a finite q sufficiently large. The sheet is already continuous, so agreement with the Holder modification on a countable dense set implies agreement everywhere on the rectangle, on one event. No assertion about an arbitrary discontinuous version is being made.

### Slice union and transfer, manuscript 284–315

| Lines | Audit |
| --- | --- |
| 285 | Dyadic endpoints ensure that all left endpoints belong to the sufficiently fine grids; this is used in downward rounding. a>0 is retained throughout. |
| 286 | `alpha=1/2-eta/16` lies in `(0,1/2)`, and `2-4 alpha=eta/4`. |
| 287–290 | `r_n=2M delta^alpha` gives `r_n^2/delta=4M^2 delta^(2 alpha-1)>=1`. For fixed M, its upper bound by one holds eventually. The factor `16M^4 delta^(-eta/4)(1+n log 2)` is correct. |
| 292 | The number of slice grid points is `O(delta^(-1))`, using mesh delta in s. A finer mesh is not needed since the same Holder exponent controls both parameter coordinates. |
| 293–298 | Markov and the union bound give `(1+n)^p delta^(3p eta/4-1)`. Taking an integer `p>4/(3 eta)` makes the exponent positive. With delta=2^(-n), the resulting geometric factor dominates the polynomial, hence the probabilities are summable. No independence across slices or n is required. |
| 303–304 | Intersecting over deterministic integers M before choosing a random M>=H is essential and is done. It avoids substituting a random radius into an unproved probability estimate. |
| 306–312 | Downward rounding remains in K, I and J because their left endpoints lie on the lattice. Both sheet increments are bounded by H delta^alpha; exact equality at the original times yields the two-term radius 2H delta^alpha. Endpoints, u=0 and non-grid real s are covered. |
| 313–315 | For each real s, every exact pair rounds to a grid pair at its rounded slice s_n. The same s_n is used for the whole fiber. At most delta^(-eta) grid squares cover that fiber. The estimate is uniform in s; its eventual starting scale may depend on the sample, M, eta and the fixed intervals. |

Controlling only dyadic scales suffices for upper box dimension: every intermediate scale lies between two successive dyadic scales with bounded ratio. The square diameter factor square-root-two also has no effect. Intersecting the probability-one events over eta=1/m proves dimension at most zero for every s in K. It is not an intersection over uncountably many slices.

### All intervals and all positive slices, manuscript 317–329

There are countably many dyadic triples K,I,J. Arbitrary disjoint compact intervals have a positive gap and can be enlarged to nondegenerate disjoint dyadic intervals, including when one is a singleton or starts at zero. Symmetry handles the reversed order. Any s>0 lies in a dyadic K bounded away from zero. Monotonicity of upper box dimension proves (b) for every such interval pair on the same event.

Every off-diagonal point lies in one of countably many separated dyadic rectangles or their transposes. Hausdorff dimension is bounded by upper box dimension on each bounded rectangle and is stable under countable unions. This proves (a) for every s>0 on that event. The argument never assumes countable stability of upper box dimension, which would be false. It does not claim global upper box dimension zero for the unbounded off-diagonal set or for a union accumulating on the diagonal.

The five-dimensional projection proof at lines 326–329 is valid pathwise, simultaneously in s: a five-coordinate equality implies equality of the first four. The same theorem holds for every larger integer dimension by the same inclusion, although the manuscript only needs d=5; this observation is not needed to prove its statement.

For formal completeness, line 69 should also state `dim_B(empty)=0`. Only the Hausdorff empty-set convention is explicit. With an alternative convention assigning minus infinity to the box dimension of the empty set, equality to zero in (b) would need to be phrased as an upper bound or given the stated convention. This is a definitional clarification, not a counterexample for nonempty sets.

### Other remarks

- Line 80: on the common event, `Y_d(s)` is the union of its dimension-one diagonal and `Y_d^*(s)` of dimension zero. The dimension-one assertion for every s>0 follows. It does not apply to s=0, and the manuscript does not claim it there.
- Lines 92–96: [Rosen 1984, Theorem 2, p. 109](https://www.math.csi.cuny.edu/~rosen/15-ilt-random-fields.pdf) gives the multiple-time dimension `Nr-d(r-1)/2` when `Nr>d(r-1)/2`. Taking N=1 and r=2 gives `2-d/2` for d=1,2,3. Ordering u<v only removes a transpose and does not change dimension. The scan was read visually; `pdftotext` alone did not recover this theorem. [KWX06 (4.1)–(4.2)](https://www.stt.msu.edu/~xiaoyimi/KWXEJP06.pdf), local text 1428–1438, uses distinct times and confirms the formula. This is a fixed deterministic-s assertion, enough to refute a simultaneous dimension-zero claim in low dimensions; the remark does not need the stronger assertion for every random s.
- Lines 99–106: subtracting the dimension of a projection from that of a total set is not a bound for every fiber. The horizontal-plus-vertical-segment counterexample is valid. The dimension calculation is a heuristic motivation, and the manuscript correctly supplies the missing uniform argument rather than treating the heuristic as a proof.
- Lines 125–131: KWX06 Lemma 1.1 is sectorial LND; Lemma 3.1 is a uniform bound on clusters of close grid values, proved through moments. The comparison is fair. The statements about full-sheet double-point papers and Chen–Woessner concern different sets and do not import a fiber theorem that those papers did not prove.

## 6. Numerical audit

All numerical computations used one thread, no multiprocessing and no language-model helpers. BLAS/OpenMP thread counts were set to one before imports; the tree counting operation is single-threaded. The independent run took 4.06 seconds with measured peak resident memory 186,875,904 bytes, about 178.2 MiB. These are diagnostic checks, not a proof of an uncountable almost-sure statement.

### Supplied script

A byte-identical copy of `claim_files/code/check_lemmas.py` was run under `referee_checks/supplied/code/`, so its relative output path could not overwrite the submitted data. Results are in [supplied/data/lemma_checks.json](referee_checks/supplied/data/lemma_checks.json), [supplied_run.log](referee_checks/supplied_run.log), and [supplied_comparison.json](referee_checks/supplied_comparison.json).

| Quantity | Submitted JSON | Rerun |
| --- | --- | --- |
| Seed | 17017 | 17017 |
| Variance configurations | 960 | 960 |
| Smallest conditional variance minus lower bound | -2.353672812205332e-14 | -1.3322676295501878e-14 |
| Largest normalized lattice sum | 0.844094367663364 | 0.8440943676633638 |
| Lattice configurations | 48 | 48 |

The largest absolute difference between corresponding normalized lattice sums was `2.7755575615628914e-16`; the variance-margin difference was `1.021405182655144e-14`. Singular covariance pseudoinverses produce these roundoff-sized negative margins. They are well below the script's tolerances and do not disprove a nonnegative exact variance. The script normalizes by `1+log_2(1/delta)`, whereas the proof uses a natural logarithm; the two are comparable by absolute constants. No claim that the implicit lemma constant equals one is justified or needed.

### Independent conditional-variance calculation

[independent_checks.py](referee_checks/independent_checks.py) uses an independent-increment basis, projects the target interval indicator onto the span of the earlier ones by least squares, and takes the squared residual norm. This is a different computation from subtracting a covariance pseudoinverse. It checks 3,900 configurations with k=0,...,12, continuous endpoints, repeated grid endpoints, and deliberately clustered endpoints at separations 0, 1e-10, 1e-7 and 1/1024. Slice rates range from 0.125 to 4.

There were no failures. The smallest `conditional variance - bridge variance` was `-1.39e-17`, the smallest `bridge variance - s rho/2` was `-1.11e-16`, and the smallest `conditional variance - s rho/2` was zero. These first two negative values are numerical cancellation at zero. The minimum ratio of conditional variance to the positive bound was 1. The test explicitly checks degeneracies rather than discarding them.

### Exact Gaussian first and second moments

For the two-pair covariance in Section 4, the second probability was computed by integrating the radial density of `X_1` over its ball and the conditional noncentral-chi-square ball probability of `X_2`. Degenerate pairs were handled separately. All ordered pair configurations, including repetitions, were summed with their exact grid multiplicities on I=[0,1], J=[2,3]. Grids n=3,4,5, dimensions four and five, and alpha=0.35,0.49 give twelve calculations. Forty- and sixty-four-point radial quadrature agreed to at most `8.53e-14` in the final second moments. This is a numerical convergence check, not a rigorous quadrature error bound.

For s=0.5 and r=delta^0.35:

| d | n | Exact-law `E N` | Exact-law `E N^2` |
| --- | --- | --- | --- |
| 4 | 3 | 0.60143138 | 4.00860772 |
| 4 | 4 | 0.82652019 | 10.40272978 |
| 4 | 5 | 1.19425317 | 28.61854496 |
| 5 | 3 | 0.13349056 | 0.48572530 |
| 5 | 4 | 0.14308661 | 0.84786876 |
| 5 | 5 | 0.16178603 | 1.59304785 |

Over all twelve cases, `E N^2 / [r^4 delta^(-2)(1+log(1/delta))]^2` ranged from 0.02242 to 0.06087 in d=4 and from 0.001248 to 0.005703 in d=5. The first-moment calculation is directly the sum of `P{chi_d^2 <= r^2/[s(v-u)]}`. On separated fixed intervals its small-r order is `r^d delta^(-2)` without a logarithm. The logarithm in the manuscript is a safe moment bound, not a claim about the exact first-moment asymptotic.

### Brownian-sheet simulation

Four thousand independent five-dimensional Brownian sheets were generated by independent Gaussian rectangle increments with delta-t=1/128 and delta-s=0.5, followed by cumulative sums in both parameters. Counts used s=0.5 and 1, n=4,6,7, alpha=0.35 and 0.49, and either the first four or all five coordinates: 24 parameter combinations. The same fine sheet was subsampled across resolutions, preserving the correct coupling. No interpolation was used to assert exact zeros.

The following subset uses s=0.5, alpha=0.35; errors are one Monte Carlo standard error. Let `S_d=r^d delta^(-2)(1+log(1/delta))`.

| d | n | Simulated mean ± SE | Exact mean | Simulated second moment ± SE | mean / S_d | second / S_d squared |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | 4 | 0.851 ± 0.0514 | 0.82652 | 11.307 ± 1.507 | 0.04274 | 0.02852 |
| 4 | 6 | 1.805 ± 0.1404 | 1.77035 | 82.0405 ± 13.885 | 0.02885 | 0.02097 |
| 4 | 7 | 2.71875 ± 0.2328 | 2.65718 | 224.0778 ± 41.011 | 0.02528 | 0.01937 |
| 5 | 4 | 0.12975 ± 0.0131 | 0.14309 | 0.70025 ± 0.1298 | 0.01720 | 0.01230 |
| 5 | 6 | 0.173 ± 0.0226 | 0.18796 | 2.067 ± 0.4922 | 0.01186 | 0.009708 |
| 5 | 7 | 0.1825 ± 0.0296 | 0.22126 | 3.528 ± 1.035 | 0.009272 | 0.009106 |

The n=4 second moments agree with the direct Gaussian calculations within about 1.2 standard errors. Across all 24 means the largest discrepancy from the exact mean was 2.86 estimated standard errors. Counts cluster strongly: the d=4 n=4 case included a path with 61 pairs, so second-moment estimates have appreciable sampling error. The finite-grid dimension-five ratios do not validate a pure r-fifth-power moment bound; the analytic repeated-pair counterexample in Section 4 rules that bound out. With the actual four-coordinate scale, the displayed d=5 normalized second moments are 0.001766, 0.0005282 and 0.0003050.

Full results, seed 20261115, timing and memory are in [independent_results.json](referee_checks/independent_results.json). The numerical claims at manuscript lines 356–359 are modest and supported by the supplied checks. The linked public repository also exists. Neither the supplied computations nor these additional simulations establish finiteness or dimension of exceptional slices.

## 7. Every bibliography entry

All eleven DOI-bearing scholarly entries were checked using publisher-deposited Crossref metadata or, for the EPFL thesis, DataCite and the EPFL record. Raw responses and a summary are retained in `referee_sources/*_metadata.json` and [bibliography_metadata.json](referee_sources/bibliography_metadata.json). Printed PDFs were used to resolve metadata conflicts. The three GitHub references were checked with the connected GitHub read tools; no messages or mutations were sent to GitHub.

| Entry and manuscript lines | Verified record | Finding / fix |
| --- | --- | --- |
| Che26, 394–395 | Keming Chen, *Uniform dimension results of level-sets of stable sheets*. Doctoral thesis, EPFL, Lausanne, 2026, no. 11211. [DOI](https://doi.org/10.5075/epfl-thesis-11211). | Author, title, institution, year and identifier agree. Adding the thesis number and direct EPFL link would make access easier. |
| CW25, 396–397 | Keming Chen and Guillaume Woessner, *Zeros of the Brownian Sheet*. Journal of Theoretical Probability 38(2), article 33, 2025, 31 pages. [DOI](https://doi.org/10.1007/s10959-024-01399-1); [arXiv:2405.20019](https://arxiv.org/abs/2405.20019). | All printed fields agree. “33” is an article number, as the manuscript says. A DOI containing 2024 does not change the publication year 2025. |
| DKNWX12, 398–399 | Robert C. Dalang, Davar Khoshnevisan, Eulalia Nualart, Dongsheng Wu and Yimin Xiao, *Critical Brownian sheet does not have double points*. Annals of Probability 40(4), 1829–1859, 2012. [DOI](https://doi.org/10.1214/11-AOP665); [arXiv:1009.0235](https://arxiv.org/abs/1009.0235). | All printed fields and author order agree. |
| DM15, 400–401 | Robert C. Dalang and Carl Mueller, *Multiple points of the Brownian sheet in critical dimensions*. Annals of Probability 43(4), 1577–1593, 2015. [DOI](https://doi.org/10.1214/14-AOP912); [arXiv:1303.0403](https://arxiv.org/abs/1303.0403). | All printed fields agree. |
| Kho05, 402–405 | Davar Khoshnevisan, *Slices of a Brownian Sheet: New Results and Open Problems*. In *Seminar on Stochastic Analysis, Random Fields and Applications V*, Progress in Probability 59, 135–174, Birkhäuser Basel. [Chapter DOI](https://doi.org/10.1007/978-3-7643-8458-6_9); [arXiv:math/0510518](https://arxiv.org/abs/math/0510518). | Author, title, series, volume, pages and DOI agree. The [chapter's publisher citation](https://link.springer.com/chapter/10.1007/978-3-7643-8458-6_9) and Crossref say 2007; the [book record](https://link.springer.com/book/10.1007/978-3-7643-8458-6) says copyright 2008, hardcover publication 17 December 2007 and eBook publication 12 March 2008. Thus 2008 is a defensible volume year, not a fabricated date. Optional fix: specify the 2008 proceedings volume and note the chapter record's 2007 date; alternatively follow the chapter citation consistently. Keep the explicit arXiv numbering note. |
| Kho02, 406–407 | Davar Khoshnevisan, *Multiparameter Processes: An Introduction to Random Fields*. Springer Monographs in Mathematics, Springer New York, 2002. [Publisher/DOI](https://doi.org/10.1007/b97363). | All printed fields agree. |
| KWX06, 408–409 | Davar Khoshnevisan, Dongsheng Wu and Yimin Xiao, *Sectorial Local Non-Determinism and the Geometry of the Brownian Sheet*. Electronic Journal of Probability 11, paper 32, 817–843, 2006. [DOI](https://doi.org/10.1214/EJP.v11-353); [printed PDF](https://www.stt.msu.edu/~xiaoyimi/KWXEJP06.pdf). | Printed fields agree. Crossref and the old journal index list Xiao first, then Khoshnevisan and Wu; the printed title page places Khoshnevisan left, Wu right, Xiao below. Retain the manuscript's printed author order. This is a metadata conflict, not an author error in the manuscript. |
| Lyo86, 410–411 | T. J. Lyons, *The critical dimension at which quasi-every Brownian path is self-avoiding*. Advances in Applied Probability, special supplement *Analytic and Geometric Stochastics*, 1986, 87–99, distributed with volume 18. | The [publisher's announcement](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3F957A7812671D171555F7106DD6AA3D/S002190020011890Xa.pdf/jpr_volume_23_issue_4_cover_and_back_matter.pdf) confirms author/title, supplement and distribution with volume 18 in December 1986. The page range 87–99 agrees with Kho05's bibliography and other reference lists; I did not obtain the original article scan, and a Cambridge book bibliography instead gives 87–100. No reliable DOI for the article was found. Do not attach the announcement's DOI to Lyons's article. Optional fix: name the special supplement; direct original-pagination verification remains outstanding. |
| Mou90, 412–413 | T. S. Mountford, *Double points and the Ornstein-Uhlenbeck process on Wiener space*. Illinois Journal of Mathematics 34(1), 38–48, 1990. [DOI](https://doi.org/10.1215/ijm/1255988489). | All printed fields agree. |
| Pen89, 414–415 | M. D. Penrose, *On the Existence of Self-Intersections for Quasi-Every Brownian Path in Space*. Annals of Probability 17(2), 482–502, 1989. [DOI](https://doi.org/10.1214/aop/1176991411). | All printed fields agree. |
| Pen90, 416–417 | M. D. Penrose, *Quasi-everywhere properties of Brownian level sets and multiple points*. Stochastic Processes and their Applications 36(1), 33–43, 1990. [Publisher/DOI](https://doi.org/10.1016/0304-4149(90)90040-Y). | All printed fields agree. |
| Ros84, 418–419 | Jay Rosen, *Self-Intersections of Random Fields*. Annals of Probability 12(1), 108–119, 1984. [DOI](https://doi.org/10.1214/aop/1176993376); [author's scan](https://www.math.csi.cuny.edu/~rosen/15-ilt-random-fields.pdf). | All printed fields agree; verified against the title page as well as the registration record. |
| MathBrainRepo, 420–421 | the author, [math-brain-public](https://github.com/yspennstate/math-brain-public), public repository created 24 October 2026. | URL exists and contains the described research memory, code and tests. The citation title is descriptive rather than the current README heading; not an error. No journal/volume/pages/DOI are claimed. |
| MathBrainPaper, 422–423 | the author, *Math Brain: Shared, Auditable Memory for Multi-Agent Mathematical Research*, [source and PDF directory](https://github.com/yspennstate/math-brain-public/tree/main/papers/math-brain-2026-10-24), source dated 26 October 2026. | Author, title, month and URL agree. The directory's 24 October name is not the source's publication date. No journal or DOI is claimed. |
| BrainFramework, 424–425 | [brain-framework-public](https://github.com/yspennstate/brain-framework-public), public repository created 5 November 2026, README title *Brain framework*. | URL, year and subject agree. No journal/volume/pages/DOI are claimed. |

Capitalization and standard journal abbreviations are not errors. DOI letter case is immaterial. I have not silently converted the publisher's contradictory year metadata or the journal's contradictory author metadata into manuscript corrections.

## 8. Required edits and remaining limits

| Manuscript line(s) | Problem | Fix |
| --- | --- | --- |
| 32–35, 82–89 | Prior d=5 finiteness is cited but its implication for both claims is left implicit. The criticism of the thesis could be read as discounting all prior d=5 work. | State that both d=5 conclusions follow from Chen's intended finiteness theorem; locate the contribution of the present argument in d=4 and its independent projection consequence. If discussing a gap, give the additive covariance at (4.42) and distinguish the theorem's conclusion from its printed proof. |
| 69, 75–76 | The box-dimension convention for an empty set is not explicit. | Set `dim_B(empty)=0` alongside the Hausdorff convention, or state the box bound as at most zero with the intended convention. |
| 165–171 | Generic-looking conditional-variance monotonicity display and independence wording are imprecise. | Use Gaussian projection monotonicity and define independent centered bridge residuals after subtracting anchor interpolation. |
| 211 | Empty finite anchor sets are permitted in a statement involving a minimum. | Require U and V nonempty. |
| 402–404 | Publisher chapter year 2007 and proceedings year 2008 differ. | Optional bibliographic clarification as in Section 7; 2008 alone has legitimate support from the volume record. |
| 410–411 | Original Lyons pagination could not be directly checked; supplement is unnamed. | Naming *Analytic and Geometric Stochastics* would identify the item more precisely. Do not invent a DOI. Resolve 87–99 versus the isolated 87–100 citation from an original scan if available. |

The theorem does not depend on the source's diagonal-inclusive formulas, Chen's finiteness argument, any numerical fit, or either bibliographic metadata conflict. The printed dimension-four probability estimates and covering argument supply the asserted common-null-set result on their own.

Task: “You are an independent referee for a short probability paper.” Request time was not supplied in the prompt; work began 15 November 2026 at 01:31 Asia/Tbilisi.
