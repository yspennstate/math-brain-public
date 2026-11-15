PROVED

# D0017 — zero-dimensional double-time fibers of Brownian-sheet slices

For the intended statement, the answer is **yes in both dimensions 4 and 5**. The proof below establishes the stronger local assertion that every off-diagonal fiber, restricted to two disjoint compact time intervals, has upper box dimension zero, simultaneously for all positive slice parameters. Dimension 5 follows by projecting onto four spatial coordinates.

The printed statement has two defects: it includes the diagonal and the zero slice. Taken literally it is false, in every spatial dimension. These defects are documented below and are not being used as a substitute for solving the intended problem. No claim of novelty is made: the search found a 2026 thesis stating the stronger finiteness assertion for dimension 5, but no verified printed result proving the dimension-zero assertion for dimension 4.

## 1. Statement and source conventions

Let B be a continuous, two-parameter, R^d-valued Brownian sheet with independent spatial coordinates and covariance

    E[B_i(s,t) B_j(s',t')] = 1_{i=j} min(s,s') min(t,t').

Write

    Y_d^*(s) = {(u,v) in [0,infinity)^2 : u != v, B(s,u)=B(s,v)}, s>0.

We use dim_H(empty)=0. Then, for d=4 or 5,

    P{for every s>0, dim_H Y_d^*(s)=0}=1.                 (T)

Equivalently one can use ordered, strictly positive times 0<u<v; allowing a time equal to zero does not change the proof. For each fixed pair of disjoint compact intervals I,J, we prove that the upper box dimension of Y_d^*(s) intersect (I x J) is zero simultaneously for every s>0. This does not assert that the entire unbounded fiber has box dimension zero, or that a fiber is empty or finite.

The source is D. Khoshnevisan, *Slices of Brownian Sheet: New Results, and Open Problems*, arXiv:math/0510518, 24 October 2005. Open Problem 2 appears in Section 8.2, PDF/printed p. 33, with discussion continuing on p. 34. It was subsequently published as *Slices of a Brownian Sheet: New Results and Open Problems*, in *Seminar on Stochastic Analysis, Random Fields and Applications V*, Progress in Probability 59, pp. 135–174 (2008), DOI [10.1007/978-3-7643-8458-6_9](https://doi.org/10.1007/978-3-7643-8458-6_9). We use the 2005 preprint's page numbers and theorem numbers throughout unless otherwise stated.

The displayed definition (8.2), p. 33, imposes neither u!=v nor u<v. Its question also includes s=0. Therefore:

- The literal Y_d(s) contains the diagonal {(t,t):t>=0}, of Hausdorff dimension 1, for every s.
- B(0,t)=0 for all t, so the literal Y_d(0) is the quadrant, of dimension 2. Removing the diagonal still leaves dimension 2 at s=0.
- For every s>0, the result proved here makes the literal, diagonal-included Y_d(s) have dimension exactly 1 for d=4,5.

Restricting to distinct times and positive s is an interpretation of the intended question, supported by the double-point definition (1.9), p. 3, and by the finiteness question in Open Problem 3, p. 34. It is not a restriction printed in (8.2). Appendix A.3, equation (A.6), p. 36, defines dimension through an infimum over positive exponents; this gives zero for the empty set. With the alternative convention dim_H(empty)=-infinity, (T) should be written dim_H Y_d^*(s)<=0.

## 2. Literature search and the gap

Searches were performed on 13 November 2026 before proof work. Public PDFs were processed entirely in memory and only text was saved; see sources/manifest.jsonl. The search included the named authors/titles, exact and variant phrases for exceptional slices and double points of slices, and forward-citation searches of the 2005 preprint and published chapter. This is a documented search, not a guarantee of exhaustive bibliographic coverage.

### Results directly concerning slices

1. **Source survey.** Theorem 1.4, p. 4, equation (1.11), characterizes intersections of the exceptional-slice set with a deterministic compact F subset (0,infinity) by positivity of Cap_{(d-4)/2}(F). Equation (1.12), p. 4, gives

       dim_H D_d = min(1, (3-d/2)_+) almost surely,
       D_d = {s>=0: B(s,u)=B(s,v) for some 0<u<v}.

   The survey credits the dimension formula to Mountford. Its equation (1.10), p. 4, credits Lyons for existence of nontrivial exceptional slices exactly when d<=5. Remark 1.5 records that all positive slices have double points when d<=3, citing Penrose. Theorem 1.2, p. 3, concerns zero sets of slices in dimensions 2 and 3; it is an analogy, not a proof for double times. The earlier survey *Brownian sheet and quasi-sure analysis*, Fields Inst. Commun. 44 (2004), pp. 25–47, arXiv:math/0406557, was also checked for the Wiener-space Ornstein–Uhlenbeck representation and its simultaneous-versus-fixed-time distinction (Sections 1 and 8). Section 5, Theorem 5.1, pp. 20–21, and equation (8.1), p. 33, give the related three-parameter and two-parameter dimension formulas, understood off the trivial diagonal and boundary axes.

2. **T. S. Mountford (1990).** *Double points and the Ornstein–Uhlenbeck process on Wiener space*, Illinois J. Math. 34(1), 38–48, DOI [10.1215/ijm/1255988489](https://doi.org/10.1215/ijm/1255988489). This is the exceptional-slice dimension result quoted in item 1: dimension 1 for d=4, and 1/2 for d=5. The original full text was obstructed by a publisher access challenge; an original theorem number is not claimed. The result and its attribution were checked in the survey itself, p. 4. In the usual identification, U_r(t)=e^{-r/2} B(e^r,t) is the stationary Wiener-space Ornstein–Uhlenbeck process. Smooth changes r<->e^r preserve local dimensions and translate exceptional OU times to exceptional positive slice parameters.

3. **Keming Chen (2026).** *Uniform dimension results of level-sets of stable sheets*, EPFL doctoral thesis 11211, presented 21 April 2026, DOI [10.5075/epfl-thesis-11211](https://doi.org/10.5075/epfl-thesis-11211). Theorem **1.3.3**, printed p. **7** (PDF p. **19**), repeated in Section **4.4.1**, printed p. **107** (PDF p. **119**), states finiteness of double-time fibers for all positive slices in d=5. Theorem **1.3.4**, p. **7**, repeated on p. **108** (PDF p. **120**), asserts the existence of infinite fibers in d=4, in every positive interval of slice parameters. An infinite set can have dimension zero. These results therefore do not supply the missing d=4 dimension assertion. The definitions have the same diagonal/boundary omissions; the intended off-diagonal positive-s interpretation is necessary there too. This report does not rely on the thesis proof. In particular, its observation around (4.42) calls a difference of two one-parameter Brownian motions a two-parameter Brownian sheet; that identification is not valid and is not used here.

### Related papers checked, and why their theorems do not answer (T)

4. **R. C. Dalang, D. Khoshnevisan, E. Nualart, D. Wu and Y. Xiao (2012).** *Critical Brownian sheet does not have double points*, Ann. Probab. 40(4), 1829–1859, DOI [10.1214/11-AOP665](https://doi.org/10.1214/11-AOP665), [arXiv:1009.0235](https://arxiv.org/abs/1009.0235). Theorem **1.1**, electronic reprint p. **1**, compares full-sheet double points with intersections of independent sheets, under unequal coordinates in every parameter direction. Corollary **1.3**, reprint p. **2**, gives existence iff d<4N. For N=2 its critical dimension is **8**, whereas the slice problem fixes one coordinate equal and concerns d=4,5. This theorem does not say exceptional slice fibers at d=4,5 are empty, or zero-dimensional. Electronic reprint pagination is expressly different from the journal's.

5. **D. Khoshnevisan, D. Wu and Y. Xiao (2006).** *Sectorial Local Non-Determinism and the Geometry of the Brownian Sheet*, Electronic J. Probab. 11, paper 32, 817–843, DOI [10.1214/EJP.v11-353](https://doi.org/10.1214/EJP.v11-353). Lemma **1.1**, p. **819**, is the sectorial conditional-variance estimate. Theorem **1.3**, p. **820**, gives uniform dimensions of images for N<=d/2. Lemma **3.1**, p. **826**, controls clusters of nearby image values on a grid. Theorem **4.1**, p. **840**, concerns spatial multiple-point sets of the full sheet. Equation **(4.2)**, p. **840**, quotes Rosen's multiple-time dimension formula. None is the all-s slice double-time statement. The proof below uses a simpler, directly proved Brownian-bridge estimate tailored to disjoint time intervals, with a similar high-moment strategy.

6. **R. C. Dalang and C. Mueller (2015).** *Multiple points of the Brownian sheet in critical dimensions*, Ann. Probab. 43(4), 1577–1593, DOI [10.1214/14-AOP912](https://doi.org/10.1214/14-AOP912), [arXiv:1303.0403](https://arxiv.org/abs/1303.0403). Theorems **1.1** and **1.2**, reprint p. **2**, and Theorem **1.3**, reprint p. **3**, concern k occurrences of a common spatial value at the critical equality (k-1)d=2kN. Arbitrarily many distinct double pairs on a slice need not share a spatial value. This is a different constraint. No paper matching the supplied random-walk/Wiener-sheet/lattice title was located; this is the actual Dalang–Mueller critical-multiple-points paper that was checked.

7. **Z. Chen and Y. Xiao (2012).** *On intersections of independent anisotropic Gaussian random fields*, Sci. China Math. 55(11), 2217–2232, DOI [10.1007/s11425-012-4521-9](https://doi.org/10.1007/s11425-012-4521-9). The author manuscript was read for its hitting/capacity setup and intersection results. It concerns independent fields and deterministic parameter sets, rather than a uniform assertion about the fibers here.

8. **D. Khoshnevisan and Y. Xiao (2007).** *Images of the Brownian Sheet*, Trans. Amer. Math. Soc. 359(7), 3125–3151, [author manuscript](https://www.math.utah.edu/~davar/PPT/IMAGE-BS/IMG8.pdf). Theorem **1.1**, manuscript p. **2**, and Theorem **1.2**, manuscript p. **3**, concern capacity criteria for images, and Theorem **1.4**, manuscript pp. **3–4**, concerns interior points under rotations. The sectorial-LND development is relevant methodology, not the required uniform slice theorem. Also checked the cited Khoshnevisan (1999) *Brownian sheet images and Bessel–Riesz capacity*, Trans. Amer. Math. Soc. 351, 2607–2622, as identified in the survey; and the distinction from Khoshnevisan–Shi (1999), *Brownian sheet and capacity*, Ann. Probab. 27, 1135–1159, as identified in the later hitting-probability papers.

9. **C. Y. Lee and Y. Xiao (2025).** *Hitting probabilities, thermal capacity, and Hausdorff dimension results for the Brownian sheet*, [arXiv:2501.14255v2](https://arxiv.org/abs/2501.14255), revised 9 October 2025. Theorems **1.2–1.4**, manuscript pp. **2–3**, concern fixed deterministic E,F and W(E) intersect F. They do not provide the simultaneous random-s fiber statement. Khoshnevisan–Xiao (2015), *Brownian motion and thermal capacity*, Ann. Probab. 43, 405–434, is its one-parameter predecessor, not a resolution of this question.

10. **J. Rosen (1984).** *Self-intersections of random fields*, Ann. Probab. 12(1), 108–119, DOI [10.1214/aop/1176993376](https://doi.org/10.1214/aop/1176993376). Located the author's public PDF, but it has no extractable text layer; no page images were produced and no original theorem number is claimed. The dimension formula used below is checked through item 5, equation (4.2), p. 840. **J.-P. Kahane**, *Some Random Series of Functions*, 2nd ed. (1985), especially Chapter 10, is explicitly cited in the source's Appendix A and in the sectorial-LND paper for capacity, dimension, and moment methods. It supplies background, not an identified post-2005 resolution.

11. **Forward citations, 2005–2026.** An OpenAlex lookup of the published chapter returned three citing records: *Hausdorff dimension of limsup random fractals* (2013), *Packing dimension of images of additive Lévy processes* (2013/2014), and **K. Chen and G. Woessner**, *Zeros of the Brownian Sheet*, J. Theor. Probab. 38, article 33 (2025), DOI [10.1007/s10959-024-01399-1](https://doi.org/10.1007/s10959-024-01399-1). The last addresses the survey's projection problem, not Open Problem 2. Broader searches found the 2026 thesis in item 3. Index coverage is incomplete; the retained citation snapshot and the explicit scope distinctions are preferable to a claim that no other paper exists.

## 3. Dimension counting and why it is not a proof

At a deterministic s>0, t -> s^{-1/2}B(s,t) is standard d-dimensional Brownian motion. For d>=4 it has no nontrivial double times almost surely. This puts the exceptional s-set in a Lebesgue-null random set, by Fubini; it does not permit an uncountable intersection of probability-one events.

Away from u=v and s=0, consider X(s,u,v)=B(s,v)-B(s,u). There are three real parameters with Brownian exponent 1/2, and d independent spatial constraints. Codimension counting predicts

    dim_H{(s,u,v):s>0,u<v,X(s,u,v)=0}=3-d/2, d<6.

The source's Theorem 5.1 and (8.1) give this dimension in the relevant cases. Projecting onto s predicts min(1,3-d/2), and the source's Theorem 1.4/(1.12) proves that value. In d=4 this is 1, despite zero Lebesgue measure; in d=5 it is 1/2. In d>=6 there are no positive exceptional slices, by Lyons' result quoted in the source.

Subtracting one slice parameter suggests a fiber dimension max(0,2-d/2): zero for d=4,5 and positive for d<=3. But dimension does not generally subtract under projections for *every* fiber. A set can consist of a horizontal interval plus one vertical interval: its dimension and the dimension of its projection are both 1, yet it has a fiber of dimension 1. Thus equality of total and projected dimensions is insufficient.

For d=1,2,3 the standard Brownian double-time formula is dim_H{(u,v):u<v,W(u)=W(v)}=2-d/2 almost surely. It follows from the multiple-time formula quoted as (4.2), p. 840, in item 5, with N=1 and k=2. These dimensions are respectively 3/2, 1, and 1/2. A single deterministic positive slice therefore disproves the dimension-zero assertion in each of those dimensions. Intersection local times on two separated time intervals exist below d=4 and explain this positive fiber dimension, in accord with the source's discussion on p. 34.

## 4. Complete proof of (T)

We prove the d=4 case. Fix a compact slice interval K=[a,b] with 0<a<b, and two disjoint compact time intervals

    I=[A,B], J=[C,D], 0<=A<B<C<D<infinity.

It suffices initially to take all endpoints dyadic rational. Let delta=2^{-n}, with n large enough that these endpoints lie on the delta lattice. All norms of spatial vectors below are Euclidean.

### Lemma 1: conditional variance, including repeated endpoints

Fix a deterministic s in K. For time pairs z_j=(u_j,v_j) in I x J put

    X_j=B(s,v_j)-B(s,u_j).

For a proposed next pair (u,v), let

    U={A,B,u_1,...,u_k}, V={C,D,v_1,...,v_k},
    rho_U(u)=min_{x in U}|u-x|, rho_V(v)=min_{y in V}|v-y|.

For any one spatial coordinate, the conditional variance of X=B(s,v)-B(s,u), given X_1,...,X_k, satisfies

    Var(X | X_1,...,X_k) >= (a/2)(rho_U(u)+rho_V(v)).       (1)

**Proof.** The scalar process t -> B_i(s,t) is sqrt(s) times Brownian motion. Condition further on its values at every time in U union V. The previous X_j are measurable with respect to these additional observations, so adding them can only decrease the Gaussian conditional variance. The remaining randomness at u and v consists of Brownian bridges in disjoint intervals; the bridges are independent.

If u is a conditioned time, its bridge variance is zero and rho_U(u)=0. Otherwise let l< u<r be its nearest conditioned neighbors inside I. The bridge variance is

    s (u-l)(r-u)/(r-l) >= (s/2) min(u-l,r-u)
                       = (s/2) rho_U(u).

The same formula holds for v, with V. Adding the two independent bridge variances and using s>=a proves (1). This also covers coinciding previous u-coordinates, coinciding previous v-coordinates, identical pairs, and deterministic time zero. No nonsingularity of the covariance of previous observations is required. For completeness, the bridge formula follows by subtracting from Brownian motion on [l,r] its linear interpolation between the endpoint values; its covariance with those endpoint observations is zero and its variance is s(u-l)(r-u)/(r-l). Disjoint bridge residuals have covariance zero and hence are independent. ∎

### Lemma 2: conditional small-ball bound

For d=4, any r>0, and the notation of Lemma 1,

    P{|X|<=r | X_1,...,X_k}
       <= C r^4 / (r^2+rho_U(u)+rho_V(v))^2,              (2)

where C depends on a only and is uniform in the values of the previous observations.

**Proof.** The spatial coordinates of the conditional Gaussian vector are independent, with a common scalar variance sigma^2 and a possibly nonzero mean. If rho=rho_U+rho_V>0, its density is at most (2 pi sigma^2)^{-2}. Integrating this bound over the radius-r ball, and using (1), gives min(1,C_0 r^4/rho^2). For rho<=r^2 the right side of (2) is at least C/4; choose C>=4. For rho>r^2 the small-ball density bound is at most 4 C_0 r^4/(r^2+rho)^2. This proves (2) with C>=max(4,4C_0), also when rho=0 and the conditional law may be degenerate. ∎

### Lemma 3: the critical lattice sum

If 0<delta<=r^2<=1, and U,V are finite anchor sets with at most k+2 elements each, then

    sum_{u in I intersect delta Z, v in J intersect delta Z}
       r^4/(r^2+rho_U(u)+rho_V(v))^2
       <= C (k+2)^2 r^4 delta^{-2}(1+log(1/delta)).       (3)

The constant depends only on the two interval lengths.

**Proof.** Assign each grid point to one of its nearest anchors. For one anchor x, there are at most four lattice points at distance in [j delta,(j+1)delta), for each integer j>=0; this bound includes endpoint and tie cases. Apply this in each coordinate and sum over at most (k+2)^2 anchor pairs. With L a fixed upper bound for the sum of the two interval lengths plus 2, the left side of (3) is at most

    16 (k+2)^2 r^4 delta^{-2}
       sum_{q=0}^{ceil(L/delta)} (q+1)/(r^2/delta+q)^2.

Here q=j+l has q+1 possible decompositions into nonnegative integers. Since r^2/delta>=1, the summand is at most 1/(q+1). The harmonic sum is bounded by C_L(1+log(1/delta)). This proves (3). ∎

### Lemma 4: arbitrarily high moments on a fixed grid slice

For deterministic s in K define the near-collision count

    N_n(s,r) = #{(u,v) in (I x J) intersect (delta Z)^2:
                           |B(s,v)-B(s,u)|<=r}.

For each integer p>=1, uniformly over s in K and delta<=r^2<=1,

    E[N_n(s,r)^p]
       <= C_p [r^4 delta^{-2}(1+log(1/delta))]^p.        (4)

**Proof.** Expand the p-th power as a sum over ordered p-tuples of grid pairs, allowing repetitions. For each tuple, condition the event at the last pair on the actual random vectors X_1,...,X_{p-1}. Lemma 2 bounds this conditional probability by a deterministic function of its pair and the preceding endpoint sets. Sum that bound over the last pair using Lemma 3. The factor is at most

    C (p+1)^2 r^4 delta^{-2}(1+log(1/delta)),

independently of the preceding pairs or their observed values. Repeat for p-1,...,1, using the virtual interval endpoints even when there are no preceding pairs. The product of the numerical factors is bounded by C^p((p+1)!)^2 and can be absorbed into C_p. Repeated endpoints cause no missing terms: they were included in Lemmas 1–3. ∎

### Lemma 5: uniform spatial and temporal continuity

For every 0<alpha<1/2, on each fixed compact parameter rectangle, almost surely there is a finite random H such that

    |B(s,t)-B(s',t')| <= H max(|s-s'|,|t-t'|)^alpha.     (5)

**Proof.** On a fixed bounded rectangle, the variance of a coordinate increment is at most C(|s-s'|+|t-t'|). Split the difference through (s',t): the two resulting white-noise increments have variances bounded by T|s-s'| and S|t-t'|, and Var(X+Y)<=2Var(X)+2Var(Y). Thus, for every q>=2, the Gaussian moment bound gives

    E|B(s,t)-B(s',t')|^q <= C_q max(|s-s'|,|t-t'|)^{q/2}.

Enclose the rectangle in a square of dyadic side length. At mesh 2^{-n} there are O(2^{2n}) nearest-neighbor grid edges. Markov's inequality bounds the probability that any such edge has increment larger than 2^{-n alpha} by

    C_q 2^{-n(q(1/2-alpha)-2)}.

Choose q with q(1/2-alpha)>2. The probabilities are summable, so Borel–Cantelli bounds every edge increment at every sufficiently fine level by 2^{-n alpha}. The finitely many earlier levels can be absorbed in a finite random constant.

To pass to arbitrary points at distance rho, choose m with 2^{-m-1}<rho<=2^{-m}. Round both points down on the level-m grid. Their rounded locations can be joined by a fixed number of level-m edges. Successive roundings of either point at levels k and k+1 can likewise be joined by a fixed number of level-(k+1) edges. Sum the resulting geometric series over k>=m, and use continuity of B to pass to the limits. The result is at most a finite random constant times 2^{-m alpha}, hence at most H rho^alpha. This proves (5) for 0<alpha<1/2, including the exponents used below. ∎

### Uniform covering and conclusion

Fix 0<eta<=1 and choose

    alpha=1/2-eta/16, so 2-4alpha=eta/4.

Fix also an integer M>=1, to be used later as an upper bound for H. For all sufficiently large n put r_n=2M delta^alpha. Then delta<=r_n^2<=1. Let K_n=K intersect delta Z; its cardinality is at most C_K delta^{-1}.

By (4), Markov's inequality, and a union bound,

    P{max_{s in K_n} N_n(s,r_n)>delta^{-eta}}
       <= C_{p,M} (1+n)^p
                     delta^{p(eta+4alpha-2)-1}
        = C_{p,M} (1+n)^p delta^{3p eta/4-1}.           (6)

Choose an integer p with 3p eta/4>1. Because delta=2^{-n}, the right side is summable over n. Borel–Cantelli shows that almost surely, for all large n,

    N_n(s,r_n)<=delta^{-eta} for every s in K_n.         (7)

This argument is made for each M, and we intersect the resulting countably many probability-one events. On the probability-one continuity event (5), choose an integer M>=max(1,H). No conditioning on the event {H<=M} was used in the moment estimate.

Now fix *any* real s in K and any exact double pair (u,v) in I x J. Round s,u,v down to the delta grid, obtaining s_n,u_n,v_n within their respective intervals. Since B(s,u)=B(s,v), (5) gives

    |B(s_n,v_n)-B(s_n,u_n)|<=2H delta^alpha<=r_n.

Consequently (u_n,v_n) is counted in N_n(s_n,r_n), and the exact pair lies in the grid square of side delta based at that pair. By (7), for every s in K its entire exact zero fiber in I x J is covered by at most delta^{-eta} such squares for all sufficiently large n. The starting scale is uniform over s.

It follows that the upper box dimension of each of these compact fibers is at most eta. Indeed the diameter of each covering square is sqrt(2) delta. Alternatively, for every beta>eta their beta-dimensional covering cost is at most

    2^{beta/2} delta^{beta-eta} -> 0.

Thus their Hausdorff dimension is at most eta as well. Intersect the probability-one events for eta=1/m, m>=1. Every one of these fibers has upper box and Hausdorff dimension zero, simultaneously for all s in K.

Finally take a countable exhaustion over dyadic K bounded away from zero and over dyadic intervals I,J with a positive gap. These rectangles cover every pair 0<=u<v<infinity. The reverse-ordered pairs are their images under (u,v)->(v,u), an isometry. Hausdorff dimension is stable under countable unions. This proves (T) for d=4 with one null set covering all positive s and all nontrivial pairs.

For d=5, the first four coordinates of B form a four-dimensional Brownian sheet. Every double pair of B is a double pair of this projection. The already proved zero-dimensional bound therefore applies to every s at once. If both dimensions are realized on a common probability space, the union of their two null sets is still null. This completes the proof. ∎

## 5. Verification and computation

The proof was audited analytically a second way: at fixed s, the covariance of scalar increments indexed by (u_i,v_i) is exactly s times the overlap length of [u_i,v_i] and [u_j,v_j]. Its Schur complement gives the conditional variance directly. This agrees with the lower bound obtained by conditioning on all Brownian endpoints and decomposing into independent bridges. The kernel sum's critical exponent is 2, equal to the two time-coordinate dimensions; the leftover sum is harmonic, not power divergent. The slice union costs delta^{-1}, which is absorbed by choosing a fixed, sufficiently large moment p for each eta. The random Holder constant is handled by a countable union over deterministic M.

`code/audit_proof.py` independently evaluates 960 small covariance configurations, including repeated endpoints, using covariance matrices and Moore–Penrose inverses. All agree with the bridge lower bound to floating-point tolerance (the smallest difference is -1.34e-14). It also checks lattice sums over several grids and radii. These calculations are sanity checks; the proof is the analytic argument above. Results are in `data/proof_audit.json`.

The discretized experiments are complete. `code/simulate.py` used four seeds (170170–170173), grid spacing 1/2048, five independent spatial coordinates, and the first four coordinates for the coupled d=4 experiment. It generated the Brownian sheet exactly at vertices of [0,2] x [0,3] by independent N(0,delta_s delta_t) rectangle increments, cumulated in t and then in s. Only a row and selected slices were retained. Near-pairs were sought on separated intervals u in [1/4,5/4] and v in [3/2,5/2], for 2049 sampled s values in [1,2]. Thus no diagonal or s=0 coincidences enter.

The slice values were divided by sqrt(s). At scale h=2^{-j} and threshold coefficient c in {0.5,1,2}, a sampled slice was called near-exceptional if its minimum cross-interval distance was <=c sqrt(h). We counted its occupied s-boxes of side h. Separately, for each seed and dimension we selected the sampled slice with the smallest observed distance, and counted occupied (u,v)-boxes for all its near-pairs at the same threshold. The selection rule is part of the experiment; the selected slice is not asserted to be an exact exceptional slice.

Regressions used log N(h) against log(1/h), with 1/16>=h>=8/2048, requiring at least three nonempty scales. The table gives the number of fitted seeds, then the median and range of their fitted slopes:

| d | c | Near-exceptional s-set: fits; median [range] | Selected near-fiber: fits; median [range] |
|---|---|---|---|
| 4 | 0.5 | 2/4; 0.010 [-0.623, 0.643] | 2/4; -0.279 [-0.558, 0.000] |
| 4 | 1 | 3/4; -0.375 [-0.974, 0.687] | 3/4; 0.049 [-0.874, 0.061] |
| 4 | 2 | 4/4; -0.120 [-1.125, 0.703] | 4/4; -0.135 [-1.563, 0.434] |
| 5 | 0.5 | 1/4; 0.011 [0.011, 0.011] | 1/4; 0.300 [0.300, 0.300] |
| 5 | 1 | 3/4; -0.585 [-0.792, 0.337] | 3/4; -0.661 [-0.792, -0.083] |
| 5 | 2 | 3/4; -0.174 [-0.949, 0.596] | 3/4; -0.475 [-1.080, 0.138] |

These are **unstable approximation exponents, not Hausdorff-dimension measurements**. In particular, negative slopes arise because the near-hit cutoff shrinks as h decreases and sampled candidates disappear. Empty scales and substantial threshold/seed dependence prevent a reliable numerical estimate of the known exceptional-set dimensions 1 and 1/2, or of the zero fiber dimension. At the finest cutoff c=1, only two of four d=4 samples and one of four d=5 samples contain any near-pair in the chosen compact region. Existence somewhere on the infinite sheet does not ensure a hit in this particular compact region. The simulation therefore supplies an explicit, reproducible, inconclusive finite-resolution experiment, rather than confirmation of the theorem.

All counts and fits, including empty scales, are retained in `data/box_counts.csv`, `data/simulation_summary.json`, `data/simulation_aggregate.json`, and the per-seed minimum-distance CSV files. Reproduce with:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
      python3 code/simulate.py --n 2048 --replicates 4
    python3 code/summarize_simulation.py

The four runs took 73.1 seconds total and peaked at 579.8 MiB of process RSS on this Mac. The inherited nice value was verified as 10; numerical thread limits and cKDTree workers were set to 1. No PDF, page image, publication, push, or external write was made.

## 6. Scope of the result

The mathematical conclusion concerns the corrected, intended off-diagonal statement at positive slice parameters. The literal printed statement remains false for the elementary reasons in Section 1. The proof does not claim finite fibers in dimension 4, does not confuse zero dimension with emptiness, and does not infer uniform statements merely from a fixed-s Brownian theorem. Literature novelty has not been certified.

Task: “Open problem D0017” — received 2026-11-13 09:25 +04 (Asia/Tbilisi).
