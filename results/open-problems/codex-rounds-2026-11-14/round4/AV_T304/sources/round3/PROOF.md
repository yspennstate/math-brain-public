# Conditional error propagation for the noisy-center compiler

The source is OpenAI, *Subpolynomial query complexity for well-conditioned log-concave sampling*, September 26, 2026, Section 7, especially Lemma 7.1 and Proposition 7.7 (`lem:compiler-absorption` and `prop:compiler-accuracy`). The original implementation section is saved in `sources/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/implementation.tex`.

The result below proves the local coupling implication used in the accuracy induction. The circuit coefficient bounds, fixed-seed stability, moment bounds and standalone child accuracy remain hypotheses. It does not establish those analytic inputs or the full sampling theorem.

## 1. Independent recheck of Gaussian absorption

Let a seeded map M satisfy, for every c, displacement u and seed array z,

\[
 M(c+u;z+v\otimes u/r)=M(c;z),\qquad r>0.
\]

Fix D>0 with \(\|v\|\le D\), and put

\[
 a=v/(2D),\quad n_0=r/(2D),\quad
 P=(I-aa^T)^{1/2},\quad s=(1-\|a\|^2)^{1/2}.
\]

Here P acts on the seed slots, identically in each spatial coordinate. Its eigenvalues are 1 on the orthogonal complement of a and s in the direction of a. In particular \(s\ge\sqrt3/2\), and \(Pa=sa\). These statements also hold when a=0, with P=I and s=1.

The block matrix

\[
 U=\begin{pmatrix}P&-a\\a^T&s\end{pmatrix}
\]

is orthogonal: the upper-left block of \(UU^T\) is \(P^2+aa^T=I\), the upper-right block is \(Pa-as=0\), and the bottom-right entry is \(\|a\|^2+s^2=1\). Thus, for independent standard Gaussian seed array G and standard Gaussian vector Z, the top block

\[
 H=PG-a\otimes Z
\]

is again a full array of independent standard Gaussian vectors. The pathwise identity, applied with base seeds H, gives

\[
 M(x+n_0 Z;PG)=M(x;H).
\tag{1}
\]

This rederives the earlier absorption result by orthogonal completion. The restoration sign is negative. H is not independent of Z when a is nonzero: \(\operatorname{Cov}(H,Z)=-a\otimes I\).

If x is a measurable function of an anchor Y, while (G,Z) is independent of Y, (1) holds conditionally on Y. Indeed, conditional on Y=y, x(y) is deterministic and the same orthogonal Gaussian calculation applies. It does not permit a further conditioning on the noisy center \(x(Y)+n_0Z\).

## 2. One inaccurate-center call

Work first at a fixed anchor value. All random variables below have finite second moments. Suppose additionally that, for every fixed seed array z,

\[
 |M(c;z)-M(c';z)|\le K|c-c'|,
\tag{2}
\]

and that for standard fresh seeds G the standalone law satisfies

\[
 W_2(\mathcal L(M(x;G)),N(\mu,\sigma^2I))\le e.
\tag{3}
\]

Let C be a supplied, possibly inaccurate center with

\[
 W_2(\mathcal L(C),N(x,n_0^2I))\le c.
\tag{4}
\]

Draw G independently of C. Then

\[
 W_2(\mathcal L(M(C;PG)),N(\mu,\sigma^2I))\le Kc+e.
\tag{5}
\]

To prove (5), choose an arbitrary positive \(\zeta\). By (4), couple C to \(C^*=x+n_0Z\), where Z is standard Gaussian, so that \(\|C-C^*\|_{L^2}\le c+\zeta\). Adjoin a fresh seed array G independent of the entire coupled pair. This preserves the actual product law of (C,G). Equation (2), applied to the identical transformed seed array PG at both centers, yields

\[
 \|M(C;PG)-M(C^*;PG)\|_{L^2}\le K(c+\zeta).
\]

By (1), the second output has exactly the standalone law \(\mathcal L(M(x;G))\). The triangle inequality for W₂ and (3) therefore give \(K(c+\zeta)+e\). Letting \(\zeta\) tend to zero proves (5). Equivalently, one can glue a near-optimal coupling for (3) to the first comparison at their common intermediate output.

No standalone guarantee has been applied at the actual random center C or conditional on C. The only call to (3) is at x, after absorption.

## 3. An affine expression with independent occurrences

Fix an anchor y. Consider finitely many child calls, indexed by i, obeying Sections 1–2 with parameters \(x_i,n_i,P_i,K_i,c_i,e_i,\mu_i,\sigma_i\). Assume that each pair consisting of its supplied center and its fresh seed array is independent of the corresponding pair for every other occurrence. A center's full supplying subtree is included in its pair. Let R be another independent standard Gaussian vector.

For deterministic coefficients \(b_0,a_i\), choose n such that

\[
 s_E^2=n^2-\sum_i a_i^2\sigma_i^2\ge0,
\]

and form

\[
 T=b_0+\sum_i a_i M_i(C_i;P_iG_i)+s_ER,
 \qquad E=b_0+\sum_i a_i\mu_i.
\]

Then

\[
 W_2(\mathcal L(T),N(E,n^2I))
 \le\sum_i|a_i|(K_ic_i+e_i).
\tag{6}
\]

For each i, choose a coupling of the actual child output to \(B_i\sim N(\mu_i,\sigma_i^2I)\) with RMS error arbitrarily close to the bound (5). Take the product of these couplings across i, and adjoin R independently. This keeps the actual joint child law because the occurrences are independent. The comparison sum \(b_0+\sum_i a_iB_i+s_ER\) has mean E and covariance \((\sum_i a_i^2\sigma_i^2+s_E^2)I=n^2I\), and is Gaussian. The L² triangle inequality bounds the coupled difference by the right side of (6), up to the arbitrarily small coupling errors. Taking their limit proves (6).

For the compiler's assignment \(\sigma_i=n/(2A')\), with \(\sum_i|a_i|\le A'\) and \(A'>0\),

\[
 \sum_i a_i^2\sigma_i^2
 \le \left(\sum_i|a_i|\right)^2n^2/(4(A')^2)
 \le n^2/4.
\]

Thus the residual is well defined. With no child terms the expression is exactly \(b_0+nR\) and has zero error.

For random anchors Y, (6) holds for almost every y with its conditional quantities. Also

\[
 W_2(\mathcal L(T),\mathcal L(E(Y)+nR))
 \le \left\|\sum_i|a_i|(K_ic_i(Y)+e_i(Y))\right\|_{L^2(Y)},
\tag{7}
\]

where R in the comparison law is independent of Y. To obtain (7), choose conditional near-optimal couplings, keep the anchor identical on the two sides, and integrate the squared conditional bound. Such couplings can be chosen measurably for Borel probability kernels on Euclidean spaces: approximate both marginals by finite partitions, choose a minimizing finite transport plan with a fixed tie-breaking rule, and refine the partitions. Disintegrating within each cell and taking successively finer approximations gives measurable near-optimal couplings. Finite second moments control the partition tails. Taking the infimum gives (7). In particular the L² triangle inequality gives the weaker, sufficient bound \(\sum_i|a_i|\|K_ic_i+e_i\|_{L^2(Y)}\).

## 4. Expansion through a finite expression tree

Now let the centers themselves be supplied by finite affine expression trees of the preceding kind. Each occurrence has its own copy of its entire supplying subtree, so Section 3 applies at every node after conditioning on the common anchors. Write \(\epsilon_E(y)\) for an expression's conditional W₂ error relative to its exact value plus its prescribed Gaussian. Assume every child mean routine has fixed-seed constant at most K and standalone error at most

\[
 B\sigma_i\delta^{p_i}D_i(y),\qquad 0<\delta<1.
\]

Section 3 gives the precise recurrence

\[
 \epsilon_E(y)\le\sum_i|a_i|
 [K\epsilon_{E_i}(y)+B\sigma_i\delta^{p_i}D_i(y)].
\tag{8}
\]

This is the source's `eq:compiler-error-recursion`. Assume the root coefficient sum is at most \(A_f\), every center expression's coefficient sum is at most A, and the expression tree has at most h mean-occurrence tiers. Assume also that

- root mean calls have \(p_i=p\) and \(\sum_i|a_i|\sigma_i\le n/2\);
- every deeper mean call has \(p_i=p-1/4\) and \(\sigma_i\le S\);
- \(\|D_i\|_{L^2(Y)}\le\overline D\) for every occurrence.

Then

\[
 \|\epsilon_{\mathrm{root}}\|_{L^2(Y)}
 \le B\overline D\delta^p
 \left[\frac n2+A_fS\delta^{-1/4}
       \sum_{j=1}^{h-1}(KA)^j\right].
\tag{9}
\]

Indeed, expand (8) until reaching affine leaves, whose errors are zero. A root intrinsic error carries no K and has weighted noise sum at most n/2. For an intrinsic error at tier \(j+1\), the product of absolute expression coefficients along its path has total sum at most \(A_fA^j\). The path crosses j earlier Lipschitz comparisons, giving \(K^j\). Its noise unit is at most S and its label is \(p-1/4\). Apply the L² triangle inequality and the bound \(\overline D\) to these finitely many terms, separately at each tier, and sum. This proves (9), including trees with unequal branch lengths. No count of occurrences is omitted: their total weights are bounded by the products of coefficient sums.

The single loss of 1/4 at all deeper tiers is a hypothesis about the assigned child labels. The source's `eq:compiler-labels` makes this assignment relative to the parent routine, rather than repeatedly relative to each expression tier. If losses accumulated at every tier, (9) would not follow in this form.

## 5. The source's exponent budget

The source asserts a fixed expression depth h and

\[
 KA\le P_d\delta^{1/3},\qquad
 B\le P_d,\qquad \overline D\le P_dD(x),
\]

where each \(P_d\) is bounded by a fixed power of \(1+\log d\); it can increase between displays. Let \(T_0=\sigma\) in a mean parent and \(T_0=1\) in a sampling parent. Its noise and coefficient estimates give \(n\le C T_0\) and \(A_fS\le C T_0\). Specifically:

- for a mean parent, \(n=\sqrt3\sigma/2\), \(A_f=C_1\), and \(S\le C\sigma\);
- for a sampling parent, \(n=\eta/\sqrt2\le1\), \(A_f=C_1r\), and \(S\le C/r\).

In particular, a sampling-parent estimate must be normalized by 1, not by its possibly small \(\eta\).

The first deeper-tier term in (9) has factor

\[
 \delta^{-1/4}P_d\delta^{1/3}=P_d\delta^{1/12}.
\]

Every additional tier contributes another \(P_d\delta^{1/3}\). For \(\delta=d^{-e}\) with fixed e>0, both \((1+\log d)^c\delta^{1/12}\) and \((1+\log d)^c\delta^{1/3}\) tend to zero for every fixed c. There are only h−1 such terms. Equation (9) therefore implies

\[
 \|\epsilon_{\mathrm{root}}\|_{L^2(Y)}
 \le P_dT_0\delta^pD(x).
\tag{10}
\]

Thus the local recurrence pays for the stated 1/4 label loss. The margin is positive: \(1/3-1/4=(4-3)/12=1/12\). Equivalently, the ratio of the stability gain \(d^{-e/3}\) to the accuracy loss \(d^{-e/4}\) is \(d^{-e/12}\).

## 6. Attempts to break the implication

**Shared center-supplying randomness breaks (6).** In one dimension let \(r=D=1\), \(v=-1\), and \(M(x;z)=(x+z)/2\). This map has exactly the required shift identity, fixed-seed Lipschitz constant 1/2, and standalone law \(N(x/2,1/4)\). Here \(n_i=1/2\) and \(P_i=\sqrt3/2\). For two calls use the same center C=Z/2, with independent standard Z,G₁,G₂,R. Then

\[
 Q_i=M(C;P_iG_i)=Z/4+\sqrt3G_i/4.
\]

Each call separately is exact for \(N(0,1/4)\), so its c and e are zero. Choose \(a_1=a_2=1/2\), \(A'=1\), and output noise n=1. These obey the compiler assignment \(\sigma_i=n/(2A')=1/2\). The prescribed residual variance is \(1-2(1/2)^2(1/2)^2=7/8\). But

\[
 \operatorname{Var}((Q_1+Q_2)/2+\sqrt{7/8}R)
 =1/16+3/32+7/8=33/32,
\]

whereas the purported comparison variance is 1. The W₂ error is \(\sqrt{33/32}-1>0\), despite zero marginal child errors. Independently, \(\operatorname{Cov}(Q_1,Q_2)=1/16\); adding the cross term \(2a_1a_2\operatorname{Cov}(Q_1,Q_2)=1/32\) to the intended variance 1 gives the same 33/32. The source explicitly avoids this counterexample by duplicating the supplying subtrees as well as the child seed arrays.

**Conditioning on the noisy center is invalid.** In this same scalar call, conditioning on Z fixes the center. The output then has variance 3/16 and mean Z/4, rather than the restored marginal law \(N(0,1/4)\). The proof above conditions only on the parent anchors, before drawing the independent center noise and child seeds.

**Independent errors need not cancel.** Replacing two exact Gaussian child outputs by the same deterministic positive displacement b creates a weighted output-mean displacement b when their weights are 1/2. Its W₂ cost is at least b. A proposed root-sum-square error bound would give only \(b/\sqrt2\). Thus the absolute-coefficient triangle bound used in (6) cannot be sharpened by assuming centered coupling errors without an additional hypothesis.

Zero translation vector, zero expression coefficients, empty expressions, and variable finite branch lengths are covered by Sections 1, 3 and 4. No inverse of a zero coefficient is used; the compiler uses a positive declared coefficient bound even when all actual coefficients vanish.

## 7. Scope of the conclusion

The conditional noisy-center recurrence and its finite-tree error budget are valid under the explicit hypotheses above. The independence required by this argument is present in the source's uncached-tree construction. This checks the probabilistic step after the Gaussian identity and the stated exponent arithmetic. It leaves the tensor estimates, numerical circuit construction, all coefficient and fixed-seed estimates, query-cap recursion, final sampling reduction and complete Lean import graph unaudited.
