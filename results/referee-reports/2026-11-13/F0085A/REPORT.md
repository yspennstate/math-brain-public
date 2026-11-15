PARTIAL

# F0085: stable Poisson allocation and percolation

The literature search found partial resolutions, but no complete resolution of the four questions. This investigation does not prove either of the remaining near-one assertions. It provides full proofs of structural deductions and a quantitative sufficient block criterion, identifies the missing estimate, and computes finite-grid torus evidence. No novelty is claimed for the structural deductions or the comparison argument.

## Statement and conventions

Let \(\Xi\) be a homogeneous Poisson process of intensity 1 on \(\mathbb R^d\), with a common appetite \(0<\alpha<1\). An allocation \(\psi\) assigns Lebesgue sites to centres, to \(\infty\) (unclaimed), or to a null exceptional set labelled \(\Delta\). Every centre's territory has volume at most \(\alpha\). Sites prefer closer centres; centres prefer closer sites, and prefer taking more sites when unsated. Stability excludes a mutually improving site–centre pair. Use the canonical allocation of Hoffman–Holroyd–Peres (HHP).

For percolation use the exact convention of Freire–Popov–Vachkovskaia (FPV):

\[
C_\alpha=\overline{\bigcup_{\xi\in\Xi}\psi_\alpha^{-1}(\xi)},
\qquad U_\alpha=\mathbb R^d\setminus C_\alpha.
\]

A set percolates if it has an unbounded connected component. FPV's \(C_\alpha\) includes territory boundaries. It is not permissible to change the boundary convention merely because boundaries have zero Lebesgue measure: that can change connectedness. In particular, the literal union of HHP's open canonical territories excludes inter-territory boundaries; it is not the closed claimed set in FPV's theorem. The four nontrivial questions concern \(d\ge2\):

| Question | Verified literature result |
|---|---|
| Does \(U_\alpha\) percolate for all sufficiently small positive \(\alpha\)? | Yes, every \(d\ge2\): FPV Theorem 1.1(ii). |
| Does \(U_\alpha\) fail to percolate for all \(\alpha<1\) sufficiently close to 1? | No resolution found. Not proved here, in any \(d\ge2\). |
| Does \(C_\alpha\) fail to percolate for all sufficiently small positive \(\alpha\)? | Yes, every \(d\ge2\): FPV Theorem 1.1(i). |
| Does \(C_\alpha\) percolate for some \(\alpha<1\), hence all larger appetites? | Yes for all sufficiently large \(d\): FPV Theorem 1.2. No resolution found for every remaining low dimension, in particular \(d=2\). |

These are statements about what the search verified, not a claim that a negative search proves that no later theorem exists. The search covers the requested paper families and queries for work through 2026; details are in [SEARCH_NOTES.txt](sources/SEARCH_NOTES.txt). The stopping condition “all four questions answered in print” was not met.

In \(d=1\), neither phase has an unbounded component for any \(0<\alpha<1\). Indeed, both have positive density, respectively \(\alpha\) and \(1-\alpha\). Ergodicity gives points of both phases arbitrarily far in either direction. An unbounded connected subset of the line contains a ray, which would exclude the other phase on that ray. Thus the small-appetite vacant-percolation assertion requires \(d\ge2\).

## Literature: exact results used

All source texts are saved as plain text with explicit PDF-page markers and the downloaded payload's SHA256. PDF bytes were held in RAM for extraction and were never saved. Page references below refer to the exact saved version; journal and preprint pagination are distinguished.

1. **Hoffman, Holroyd and Peres, “A stable marriage of Poisson and Lebesgue,” Ann. Probab. 34 (2006), 1241–1272**, DOI [10.1214/009117906000000098](https://doi.org/10.1214/009117906000000098), [arXiv:math/0505668v4](https://arxiv.org/abs/math/0505668v4). The Open problems paragraph (iii) is on PDF p.31. It asks the two questions for unclaimed sites and the corresponding questions for claimed sites, then points to [5] for progress. The saved v4 has numbered sections 1–9 followed by “Open problems”; it is not labelled Section 12 in this version. Theorem 3, PDF p.5: almost sure essential uniqueness and an isometry-equivariant factor allocation. Theorem 4, p.5: at intensity 1 and \(\alpha<1\), every centre is sated. Theorem 5, pp.5–6: bounded territories, local finiteness of territories meeting a bounded set, and finitely many open components in the canonical version. Theorem 6(ii), p.6, proved via Theorem 28(ii), pp.27–30: at \(\alpha=1\), every site is coveted by infinitely many centres. Propositions 21–22, pp.21–22: monotonicity in centres and appetite. Theorem 24, p.24: the canonical version, open territories and open unclaimed set, and null territory boundaries.

2. **Freire, Popov and Vachkovskaia, “Percolation for the stable marriage of Poisson and Lebesgue,” Stochastic Processes Appl. 117 (2007), 514–525**, DOI [10.1016/j.spa.2006.09.002](https://doi.org/10.1016/j.spa.2006.09.002), [arXiv:math/0511186v3](https://arxiv.org/abs/math/0511186v3). Their closure convention is on PDF p.3; Definition 1.1 and Theorem 1.1 are on p.4. Hypotheses: unit-intensity homogeneous Poisson centres, deterministic equal appetites, Euclidean distance, \(d\ge2\). Theorem 1.1(i) proves small-appetite claimed nonpercolation; (ii) proves small-appetite unclaimed percolation, in every such dimension. Theorem 1.2, p.6, proves

   \[
   \limsup_{d\to\infty}2^d\alpha_p(d)\le1.
   \]

   In particular, \(\alpha_p(d)<1\) for every sufficiently large dimension; no explicit starting dimension is stated. Its proof uses a Boolean model contained in \(C_\alpha\), p.6. It does **not** prove vacant nonpercolation near 1, or claimed percolation below 1 in every dimension. Page 6 explicitly leaves the latter question open in small dimensions and reports numerical evidence near 0.7 in the plane. The small-appetite proof is not an independent-radius Boolean comparison: Lemma 2.1, pp.8–9, constructs dependent covering radii; Lemma 2.2, p.10, proves truncated radii are local; Lemma 2.3, p.11, gives independence of separated passable boxes; Lemmas 2.4–2.5 and (2.11)–(2.13), pp.11–15, complete the multiscale estimate and the planar contour argument for the vacant set.

3. **Hoffman, Holroyd and Peres, “Tail Bounds for the Stable Marriage of Poisson and Lebesgue,” Canadian J. Math. 61 (2009), 1279–1299**, DOI [10.4153/CJM-2009-060-7](https://doi.org/10.4153/CJM-2009-060-7). The **published** Theorem 1.3(ii), journal p.1281, PDF p.3, states, for every fixed \(d\) and \(\alpha<1\),

   \[
   \mathbb E^*\exp\{c(R^*)^d\}<\infty,
   \qquad c=c(d,\alpha)>0,
   \]

   where \(R^*\) is the essential territory radius of the Palm centre. This is Theorem 2(ii), PDF p.4, in the saved arXiv:math/0507324 preprint. Published Lemma 1.5, p.1281, compares the conditional site distance with \(R^*\). Published Theorem 1.6, p.1283, is continuity under local agreement of centre configurations at fixed appetite. Published Lemma 5.1 and Corollary 5.2, pp.1289–1290, concern **replete centres** for intensity \(\lambda\le1\), with appetite fixed at 1. Lemma 5.3 and Corollary 5.4, p.1290, concern **decisive sites** for \(\lambda\ge1\). These qualitative results do not give a uniform critical decay constant or the block comparison estimate below. Point-to-centre distance is infinite on unclaimed sites, so the subcritical exponential bound must not be written as an unconditional moment bound for that distance.

4. **Gouéré, “Subcritical regimes in some models of continuum percolation,” Ann. Appl. Probab. 19 (2009), 1292–1318**, DOI [10.1214/08-AAP575](https://doi.org/10.1214/08-AAP575), [arXiv:0712.3638v3](https://arxiv.org/abs/0712.3638v3). Theorem 1.10, saved PDF p.10: for sufficiently small appetite, the claimed cluster diameter has finite moments of every positive order. Lemma 1.11, p.10, and Lemma 5.1, p.25, supply a dependent radius envelope and its tail. Section 5, pp.25–28, verifies locality of truncated marks, not independence of all radii. This strengthens small-appetite control; it does not settle either remaining near-one question.

5. **Díaz-Pachón, “Percolation for the stable marriage of Poisson and Lebesgue with random appetites,” Stochastics 85 (2013), 252–261**, DOI [10.1080/17442508.2011.651215](https://doi.org/10.1080/17442508.2011.651215), [arXiv:0909.5325v6](https://arxiv.org/abs/0909.5325v6). Theorem 3.1, saved PDF p.5: independent nonnegative appetites \(\alpha V_\xi\), independent of Poisson centres, with a finite \((2+\delta)\)-moment, yield small-scale claimed nonpercolation and vacant percolation; its moment assertion is stated with appetite chosen sufficiently small for each moment order. Constant \(V\) includes the original setting. No near-one theorem is given there.

The other requested leads concern different objects:

| Work checked | Exact location and distinction |
|---|---|
| Deijfen–Holroyd–Peres, **Stable Poisson Graphs in One Dimension**, EJP 16 (2011), 1238–1253; [arXiv:1101.3716](https://arxiv.org/abs/1101.3716), DOI 10.1214/EJP.v16-897 | Theorems 1.2–1.3, saved PDF p.5, and the finite-interval criterion, p.6, concern stub multi-matchings and graph components. They do not concern the union of Lebesgue territories. |
| Holroyd–Pemantle–Peres–Schramm, **Poisson matching**, AIHP PS 45 (2009), 266–287; [arXiv:0712.1867](https://arxiv.org/abs/0712.1867), DOI 10.1214/08-AIHP170 | Theorems 5–6, saved preprint PDF p.6: one-/two-colour stable **point matching** distance tails. These do not give a stable territory-radius bound or F0085 percolation. |
| Markó–Timár, **A Poisson allocation of optimal tail**, Ann. Probab. 44 (2016), 1285–1307; [arXiv:1103.5259](https://arxiv.org/abs/1103.5259), DOI 10.1214/15-AOP1001 | Theorem 1.1, saved PDF p.1: a constructed allocation for \(d\ge3\) with Palm diameter tail \(O(e^{-cr^d})\). It uses stable marriage inside a different construction; it is not a theorem about the original Euclidean stable allocation. |
| Chatterjee–Peled–Peres–Romik, **Gravitational allocation to Poisson points**, Ann. Math. 172 (2010), 617–671; [arXiv:math/0611886](https://arxiv.org/abs/math/0611886), DOI 10.4007/annals.2010.172.617 | Theorem 2, saved preprint PDF p.8, and Theorem 3, p.9: gravitational basins and integral-curve crossings, for \(d\ge3\). They concern a different allocation. Their **Phase Transitions in Gravitational Allocation**, GAFA 20 (2010), 870–917, [arXiv:0903.4647](https://arxiv.org/abs/0903.4647), concerns cell large deviations, not this appetite-percolation question. |

Searches also checked the 2023 Cox–Boolean paper “Continuum percolation in a nonstabilizing environment” against its primary abstract; its directing Poisson line environment is a different model. The 2024 finite-dependence paper of Köhler-Schindler–Sulser, [arXiv:2405.07345](https://arxiv.org/abs/2405.07345), Theorem 2, saved PDF p.3, gives general domination functions depending on degree and dependence range, not an allocation-specific block estimate. Neither is evidence that F0085 was resolved.

Also checked: Duminil-Copin–Raoufi–Tassion, **Subcritical phase of d-dimensional Poisson–Boolean percolation and its vacant set**, Annales Henri Lebesgue 3 (2020), 677–700, DOI [10.5802/ahl.43](https://doi.org/10.5802/ahl.43). Theorem 1.2, journal p.679 / saved PDF p.3, gives occupied sharpness under a finite \((5d-3)\)-moment; Theorem 1.6, p.682 / PDF p.6, concerns vacant-set sharpness for compactly supported radii. Its starting model is an independently marked Poisson process with a fixed radius law. It cannot be applied directly to the correlated stopping radii of stable allocation. Follow-up searches of Boolean critical bounds did not verify an additional explicit low-dimensional extension, so this report does not declare every dimension other than 2 resolved.

Source caution: the printed parameter inequalities in DRT Theorem 1.6 appear reversed relative to its own decreasing vacant-connectivity function. This was checked with two text extractors and the indexed publisher text. None of those inequalities is used here.

## Proofs and the near-one attack

Write \(v_d=\mathcal L B(0,1)\), and

\[
R_\alpha(\xi)=\mathop{\rm ess\,sup}_{x:\psi_\alpha(x)=\xi}|x-\xi|.
\]

The following arguments explain both valid comparison tools and the limit of the present proof attempt.

### 1. The claimed set is a union of dependent stopping balls

For every fixed \(\alpha<1\), almost surely

\[
C_\alpha=\bigcup_{\xi\in\Xi}\overline B(\xi,R_\alpha(\xi)),
\tag{1}
\]

and this collection of balls is locally finite.

**Proof.** If \(|x-\xi|<R_\alpha(\xi)\), then \(\xi\) covets sites sufficiently close to \(x\): a positive volume of its territory is farther from \(\xi\). If \(x\notin C_\alpha\), a neighbourhood of \(x\) contains no claimed sites. Almost every site in that neighbourhood is unclaimed and would form an unstable pair with \(\xi\). Therefore the open ball, and then its closure, is contained in \(C_\alpha\).

Conversely, each open canonical territory is contained in its closed radius ball. To take closures of the union, first prove local finiteness. If a compact set lies in \(B(0,M)\), Campbell's formula and translation covariance give

\[
\mathbb E\#\{\xi: \overline B(\xi,R_\alpha(\xi))\cap B(0,M)\ne\varnothing\}
\le v_d\mathbb E^*(R^*+M)^d<\infty.
\]

The last inequality follows from HHP's published Theorem 1.3(ii). Thus only finitely many balls meet each bounded set almost surely. Their union is closed, proving the reverse inclusion and (1). Independence of radii has not been used or asserted. The same ball equality holds for finitely many centres by the first argument and finiteness. ∎

The boundary in (1) is contained in a countable union of spheres, hence is null. Mass transport, using saturation of every centre, gives claimed volume density \(\alpha\) and vacant volume density \(1-\alpha\).

### 2. The proposed uniform small-radius bound is false

For every fixed \(0<\alpha<1\),

\[
\sup_{\xi\in\Xi}R_\alpha(\xi)=\infty\quad\hbox{almost surely}.
\tag{2}
\]

**Proof.** Fix \(r,\varepsilon>0\), and choose an integer \(N\) such that
\(N\alpha>v_d(r+\varepsilon)^d\). A ball of radius \(\varepsilon\) containing at least \(N\) centres has positive probability. Such balls occur almost surely among infinitely many disjoint, well-separated deterministic balls, by independence of Poisson counts. If every centre in one such ball had radius at most \(r\), their disjoint territories would fit inside a ball of radius \(r+\varepsilon\), with total volume at least \(N\alpha\), a contradiction. Apply this for every positive integer \(r\). ∎

Thus the scale \(\alpha^{1/d}\) is not a deterministic upper bound for all territories. In the opposite direction, saturation implies

\[
R_\alpha(\xi)\ge(\alpha/v_d)^{1/d},\qquad
\bigcup_{\xi\in\Xi}\overline B(\xi,(\alpha/v_d)^{1/d})\subset C_\alpha.
\tag{3}
\]

Indeed, a smaller ball has volume less than the required territory. Formula (3) is FPV's Boolean **lower** comparison. If \(\lambda_c(d)\) is the Boolean critical intensity for balls of radius \(1/2\), it yields

\[
\alpha_p(d)\le v_d2^{-d}\lambda_c(d).
\]

FPV then uses Penrose's high-dimensional limit \(v_d\lambda_c(d)\to1\) to obtain Theorem 1.2. This does not yield the requested conclusion in all low dimensions.

### 3. A valid random upper-radius envelope

For \(\alpha<2^{-d}\), define

\[
\mathcal R_\alpha(\xi)=\inf\{r>0:v_dr^d>\alpha\#(\Xi\cap B(\xi,2r))\}.
\tag{4}
\]

Then \(R_\alpha(\xi)\le\mathcal R_\alpha(\xi)<\infty\) almost surely. This is a strict-inequality variant of the covering construction in Gouéré's Lemma 1.11.

**Proof.** Suppose the inequality in (4) holds at \(r\). Centres in \(B(\xi,2r)\) can claim less than the volume of \(B(\xi,r)\). There is consequently a positive volume of sites in the latter ball that are unclaimed or assigned outside \(B(\xi,2r)\). Such a site \(x\), chosen off the exceptional null set, desires \(\xi\): in the second case its assigned centre is farther than \(r\), while \(|x-\xi|<r\). Stability says \(\xi\) cannot covet \(x\), so its radius is at most \(|x-\xi|<r\). Take the infimum over admissible radii. Poisson volume growth gives eventual admissibility when \(2^d\alpha<1\). ∎

There is an explicit Palm tail estimate. Put \(q=2^d\alpha<1\), \(\kappa=(1+q)/(2q)>1\), and \(H(u)=u\log u-u+1\). For

\[
r^d\ge\frac{2\alpha}{v_d(1-q)},
\]

\[
\mathbb P^*(\mathcal R_\alpha(0)>r)
\le\exp[-2^dv_dH(\kappa)r^d].
\tag{5}
\]

**Proof.** Under the Palm law the count in (4) is \(1+Z\), where \(Z\) is Poisson with mean \(\mu=2^dv_dr^d\). If \(\mathcal R>r\), then \(Z\ge\mu/q-1\). The displayed lower bound on \(r\) ensures \(\mu/q-1\ge\kappa\mu\). Chernoff's bound, obtained by applying Markov's inequality to \(e^{(\log\kappa)Z}\), gives \(\mathbb P(Z\ge\kappa\mu)\le e^{-\mu H(\kappa)}\). ∎

For any cutoff \(s\), whether \(\mathcal R_\alpha(\xi)\le s\) is determined by centres within distance \(2s\), apart from immaterial endpoint conventions. This is genuine truncated locality. The entire family of radii remains dependent. Neither (4) nor (5) extends to appetites near 1, and a short territory radius alone is not a certificate that outside centres cannot change an allocation.

### 4. Local full coverage near 1, with a proof of the order of limits

Fix a compact cube \(K\). Let \(\Xi_m=\Xi\cap[-m,m]^d\), and let \(R_{m,\alpha}\) be the radii of the stable allocation of the **whole space** to those finitely many centres. Define

\[
G_{m,\alpha}(K)=\left\{K\subset\bigcup_{\xi\in\Xi_m}B(\xi,R_{m,\alpha}(\xi))\right\}.
\]

Then

\[
\lim_{m\to\infty}\lim_{\alpha\uparrow1}\mathbb P(G_{m,\alpha}(K))=1.
\tag{6}
\]

In particular, for the infinite allocation,

\[
\mathbb P(K\subset C_\alpha)\longrightarrow1\quad(\alpha\uparrow1).
\tag{7}
\]

**Proof.** We give the continuity details because they matter here.

First, radii of sated centres increase when appetite increases. HHP Proposition 22(ii) says that the residual volume \(\alpha-\gamma_\xi(\psi,r)\) increases, where \(\gamma\) is territory volume inside \(B(\xi,r)\). For a sated centre the residual is positive exactly when \(R(\xi)>r\). Similarly, Proposition 21(ii), at fixed appetite and using saturation, shows that adding centres increases the radii of existing centres.

For a fixed finite set of centres, \(R_{\alpha_n}(\xi)\uparrow R_1(\xi)\) whenever \(\alpha_n\uparrow1\). To see this without assuming appetite continuity, couple the allocations. Site-to-centre distances decrease by Proposition 22(i). Away from bisectors, each site's label eventually becomes constant: once its distance is finite there are only finitely many possible centres within that distance. Each centre's territories lie in the fixed bounded ball of its appetite-1 radius. Dominated convergence therefore gives limiting territory volume 1. The limit is stable: if a site desired a centre that coveted it, take a farther limiting territory site, off the common exceptional null set. Both labels eventually agree with their limiting labels, creating the same strict unstable pair for large \(n\). Essential uniqueness identifies the limit with the appetite-1 allocation. Positive volume beyond each \(r<R_1(\xi)\) then proves convergence of the radii. All finite centres are sated, since finitely much appetite cannot exhaust Lebesgue measure on the whole space; their radii are bounded, for example by the argument in (4) with a ball of volume greater than their total appetite.

Next hold appetite equal to 1 and let \(m\to\infty\). The finite configurations converge locally to \(\Xi\). HHP's published Theorem 1.6 gives almost-everywhere convergence of their canonical allocations to the infinite critical allocation. For each fixed centre, the preceding centre-monotonicity bounds \(R_{m,1}(\xi)\) above by \(R_1(\xi)\). Almost-everywhere convergence preserves a positive volume of its territory beyond any \(r<R_1(\xi)\), so \(R_{m,1}(\xi)\uparrow R_1(\xi)\).

By HHP Theorem 6(ii), at criticality every site is coveted by infinitely many centres. For the canonical open territories, coveting a site implies \(|x-\xi|<R_1(\xi)\): a farther territory point has an open neighbourhood with positive volume. Hence the critical open balls cover all of \(\mathbb R^d\). Compactness gives a finite subcover of \(K\), with a positive common margin. The finite-window radius convergence just proved preserves that subcover for some finite \(m\). Finite-configuration appetite continuity then preserves it for all \(\alpha<1\) sufficiently close to 1. The events are increasing in \(m\) and \(\alpha\); this almost-sure eventual coverage proves (6). Their balls are contained in the infinite claimed set by monotonicity, proving (7). ∎

The argument yields a finite local certificate, not finite-range dependence of the full allocation. Crucially, \(K\) is fixed in (6); the window size required for a given failure probability has not been bounded.

### 5. An explicit finite-range criterion sufficient for both near-one conclusions

Here is a quantified comparison whose hypotheses are proved exactly, except for the numerical probability bound required to apply it.

Fix a block side \(\ell>0\) and integer \(m\ge0\). For \(z\in\mathbb Z^d\), let

\[
Q_z=\ell z+[-\ell/2,\ell/2]^d,\qquad
W_z=\ell z+[-(m+1/2)\ell,(m+1/2)\ell]^d.
\]

Compute the whole-space stable allocation to the finite set \(\Xi\cap W_z\). Call \(z\) good if its open stopping balls cover \(Q_z\). Let \(p=\mathbb P(z\text{ is bad})\), \(k=2m+2\), \(q=k^d\), and \(\Delta=3^d-1\). If, for some \(\alpha<1\),

\[
p\le(100\Delta)^{-q},
\tag{8}
\]

then \(C_\alpha\) percolates almost surely and \(U_\alpha\) does not percolate almost surely.

**Proof.** Goodness is a measurable function of the Poisson points in \(W_z\) alone. For a finite set of centres, full cover by its open balls is equivalently positivity of the minimum on \(Q_z\) of the continuous function \(\max_\xi(R(\xi)-|x-\xi|)\); this also verifies measurability. The field is \((2m+1)\)-dependent in the sup norm: separated collections of windows use disjoint Poisson restrictions. Colour \(\mathbb Z^d\) by its coordinates modulo \(k\). Within each of the \(q\) colours, the windows are disjoint and the bad indicators are jointly independent.

Every set of \(n\) distinct bad vertices therefore has probability at most \(p^{n/q}\): select a colour represented at least \(n/q\) times. The number of self-avoiding star-neighbour paths of \(n\) vertices from a specified vertex is at most \(\Delta^n\). Thus

\[
\mathbb P(\text{a bad star-path of }n\text{ vertices starts at }z)
\le (\Delta p^{1/q})^n\le100^{-n}.
\tag{9}
\]

Almost surely there is no infinite bad star-component, by letting \(n\to\infty\) and taking a countable union over starting vertices. Every good cube is contained in \(C_\alpha\), by the finite-centre ball inclusion and monotonicity. An unbounded component of the open set \(U_\alpha\) would consequently visit an unbounded star-connected family of bad cubes. Local finiteness of the cube lattice would give an infinite bad star-component, contradicting (9). Hence \(U_\alpha\) has no unbounded component.

For claimed percolation, restrict the block field to a coordinate copy of \(\mathbb Z^2\). If the origin is good but its nearest-neighbour good component is finite, the external vertex boundary contains a surrounding bad star-circuit. A circuit with \(n\ge4\) vertices surrounding the origin lies in \([-n,n]^2\). There are at most \((2n+1)^2 8^n\) candidate walks, and the probability that all its distinct vertices are bad is at most \(p^{n/q}\). Thus the probability that the origin fails to lie in an infinite good component is bounded above by

\[
p+\sum_{n\ge4}(2n+1)^2(8p^{1/q})^n<1,
\]

since \(8p^{1/q}\le1/100\) and the series is less than \(10^{-6}\). There is positive probability of an infinite good component. Adjacent good cubes have a common face and lie entirely in \(C_\alpha\), so their union is an unbounded connected subset of \(C_\alpha\). Ergodicity of the underlying Poisson process upgrades the existence probability to 1. ∎

This proof makes the finite-range requirement explicit and uses a direct contour bound. Liggett–Schonmann–Stacey, **Domination by product measures**, Ann. Probab. 25 (1997), 71–95, DOI [10.1214/aop/1024404279](https://doi.org/10.1214/aop/1024404279), can replace the deliberately crude bound (8) once the same local field and a sufficiently high marginal have been established. It cannot supply that high marginal itself.

**The unresolved estimate.** Formula (6) permits the window ratio \(m\) to grow as \(p\) shrinks. In (8), however, the required smallness of \(p\) depends on \(m\) through \(q=(2m+2)^d\). The order of limits in (6) does not imply that any pair \((m,\alpha<1)\) satisfies (8). Nor does it prove the weaker quantitative hypothesis for an LSS comparison. A proof must control block failure and influence range together, or use a different renormalisation construction. The noncritical radius constant \(c(d,\alpha)\) has no verified uniform lower bound as \(\alpha\uparrow1\), and bounding a territory radius does not rule out a chain of reallocations caused by distant centres. No step closing this gap was found. Equations (6)–(9) are therefore partial results, not a proof of either open assertion.

## Computation: finite-grid evidence only

There are **536 sweep allocations**, plus three pilot runs. Each realization uses a Poisson number of centres with mean \(L^2\), conditionally independent uniform centre positions on a square torus of side \(L\), and grid sites at pixel centres. The same centre configuration is used for all appetites of a seed and for both resolutions at \(L=64\). Different seeds give independent Poisson realizations. Periodic Euclidean distance is used throughout.

| Torus side \(L\) | Mesh \(h\) | Grid sites | Poisson seeds | Appetites per seed | Allocations |
|---|---|---:|---:|---:|---:|
| 32 | 1/8 | 65,536 | 16 | 12 | 192 |
| 64 | 1/8 | 262,144 | 12 | 12 | 144 |
| 96 | 1/8 | 589,824 | 8 | 12 | 96 |
| 64 | 1/16 | 1,048,576 | 8 | 13 | 104 |

Requested coarse appetites are 0.2, 0.4, 0.55, 0.6, 0.65, 0.675, 0.7, 0.725, 0.75, 0.8, 0.9, and 0.95. The finer sweep adds 0.625. Each centre has integer quota \(q=\lfloor\alpha/h^2+1/2\rfloor\), so the actual grid appetite is \(\alpha_h=qh^2\); both values are recorded. Maximum rounding error is \(h^2/2\), namely 0.0078125 or 0.001953125. The realized Poisson density is also recorded. Two \(L=32\) realizations at the highest appetite had total quota greater than the number of sites; they were retained, with all sites claimed and some centres unsated. The larger tori had no such cases. No sample was resampled to enforce subcriticality.

**Algorithm and checks.** [torus_allocation.py](code/torus_allocation.py) implements centre-proposing Gale–Shapley with growing nearest-site preference lists. A site retains its closest proposer; a rejected centre continues proposing until it fills its quota or exhausts all sites. Lists double on demand, up to the entire site set. There is no spatial cutoff. Termination and stability follow from finitely many proposals, improving site choices, and exhaustion of all sites a centre could prefer to a final assignee. The model solved exactly, up to floating-point distance comparisons, is this atomic grid model; no continuum discretisation-error theorem is asserted.

Every result was audited by a separate geometric enumeration of sites inside each centre's final preference radius, checking all possible blocking pairs with tolerance \(10^{-10}\). An unsated centre's audit searches the whole torus. Across the sweeps, **780,192,050** candidate pairs were checked and zero violations found. Quota accounting independently verifies

\[
\text{claimed fraction}=\min\{1,Nq/\#\text{sites}\}
=\min\{1,(N/L^2)\alpha_h\},
\]

with maximum discrepancy \(1.11\times10^{-16}\). On 16 small instances, Gale–Shapley agreed exactly with an independent solver that scans every site–centre pair in global distance order, including cases with unsated centres. Periodic component counts, largest sizes and winding flags agreed with an independent lifted-grid breadth-first search on 618 test cases.

Both 4-neighbour and 8-neighbour components are measured, with periodic seam merging and integer displacement tracking. A winding flag means a noncontractible cycle in the component, not merely contact with opposite edges of a plotted square. All claimed winding indicators and largest sizes were nondecreasing in appetite, and their vacant counterparts nonincreasing, for every seed. Four-/eight-neighbour results measure sensitivity to the grid connectivity convention; they are not certified lower/upper bounds for continuum connectivity.

Selected fine-grid results follow. Component sizes are mean fractions of the **whole torus** under 4-neighbour adjacency; winding columns give counts out of eight independent realizations.

| Actual appetite \(\alpha_h\) | Claimed winding | Vacant winding | Largest claimed / torus | Largest vacant / torus |
|---:|---:|---:|---:|---:|
| 0.398438 | 0/8 | 8/8 | 0.0046 | 0.6006 |
| 0.601563 | 0/8 | 8/8 | 0.0663 | 0.3878 |
| 0.648438 | 0/8 | 8/8 | 0.1840 | 0.3313 |
| 0.675781 | 4/8 | 5/8 | 0.3580 | 0.2692 |
| 0.699219 | 6/8 | 3/8 | 0.5032 | 0.2039 |
| 0.726563 | 8/8 | 1/8 | 0.6307 | 0.1159 |
| 0.800781 | 8/8 | 0/8 | 0.7696 | 0.0267 |
| 0.949219 | 8/8 | 0/8 | 0.9472 | 0.0053 |

The following are interpolated **finite-grid 50% winding crossovers**. For a plateau at 50%, its midpoint is used. Vacant columns refer to loss of winding as appetite increases.

| \(L,h\) | Claimed, 4-neighbour | Claimed, 8-neighbour | Vacant, 4-neighbour | Vacant, 8-neighbour |
|---|---:|---:|---:|---:|
| 32, 1/8 | 0.648 | 0.621 | 0.664 | 0.693 |
| 64, 1/8 | 0.647 | 0.631 | 0.635 | 0.667 |
| 96, 1/8 | 0.664 | 0.625 | 0.644 | 0.680 |
| 64, 1/16 | 0.676 | 0.665 | 0.688 | 0.699 |

The finer sweep suggests claimed onset around 0.67 and vacant loss around 0.69. A broad transition region around **0.65–0.73** is a reasonable description of these experiments, consistent with FPV's rough planar estimate near 0.7. This is not a confidence interval or a rigorous bracket. Resolution drift is substantial, there are only eight fine-grid seeds, and no infinite-volume or zero-mesh extrapolation has been validated. These experiments do not establish whether there is a single common continuum threshold, a coexistence interval, or an interval with neither phase percolating.

See the original figures [torus_winding.svg](data/torus_winding.svg) and [torus_largest_components.svg](data/torus_largest_components.svg). Raw per-run component sizes, phase-normalized sizes, winding flags, quotas and audits are in the four `data/torus_*.csv` files; aggregates are in [summary.csv](data/summary.csv), and the crossover estimates in [finite_grid_crossovers.csv](data/finite_grid_crossovers.csv). Centre coordinates and selected full allocations are also saved. The field `max_audit_radius` denotes the search radius used by the blocking-pair audit; for unsated centres it is inflated to cover the torus and is not a territory-radius statistic.

## Reproduction and final audit

Run `sh code/reproduce.sh` from this directory to repeat the sweeps and analyses. The script uses the exact seeds, meshes and appetites above. Python dependencies are NumPy, SciPy and Matplotlib; source extraction additionally uses pypdf, with pdftotext used for the DRT font issue. The numerical code sets library thread limits to one, uses `cKDTree(workers=1)`, and enforces nice at least 10; this run's priority was exactly nice 10. Only one sweep process ran at a time. Maximum measured RSS was **1544.109375 MiB**, about 1.62 decimal GB. The sum of measured allocation, component and audit times was 807.521 seconds. Nothing was published or pushed.

[numerical_checks.json](data/numerical_checks.json) records the independent solver and winding checks. [audit_summary.json](data/audit_summary.json) records complete run accounting, stability, volume balance and monotonicity checks. [proof_constant_checks.json](data/proof_constant_checks.json) cross-checks the contour-series estimate by direct summation and a geometric majorant and checks the Chernoff threshold algebra. The source pagination was checked against the saved page markers; published HHP tail-theorem page headers were checked separately. [artifact_audit.json](data/artifact_audit.json) records the final file-format and syntax audit, and [manifest.json](data/manifest.json) hashes the report, log, code, sources and data.

The unresolved mathematical work is precisely the joint estimate of local block failure and influence range discussed after (8). Neither the conditional criterion nor the finite simulations are reported as a proof of the remaining questions.

Task: “Open problem F0085” — started 2026-11-13 08:07 +04 (Asia/Tbilisi).
