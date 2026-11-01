# Quadratic interactions beyond independent-block FEI

19 September 2026. **Full Friedgut–Kalai FEI remains unproved.**

This continuation proves a dimension-independent entropy–influence bound for a class with arbitrary quadratic interactions among independent affine clauses. Unlike the preceding affine-variance construction, the quadratic factor need not have independent parameter coordinates: it can use all the clause variables, with unrestricted rank and arbitrary cross-block coupling. The higher-degree clause forms are still required to be jointly independent. That remaining assumption is not dropped. The final argument also allows an arbitrary cubic core on independent parameter coordinates, with unrestricted quadratic coupling to the clause blocks.

The arguments below are analytical, with executed exact finite checks. They are not an independent audit, Lean verification, or a comprehensive publication-priority clearance. The earlier disjoint-block theorem and its minimum-affine-influence framework are explicitly reused.

## 1. Main result and the precise enlargement

All spaces are binary vector spaces with uniform measure. For a Boolean sign function f define

\[
a_s=\widehat f(s)=\mathbb E_x f(x)(-1)^{s\cdot x},\quad
H(f)=\sum_s a_s^2\log_2(1/a_s^2),
\]
\[
\alpha_f(v)=\Pr[f(x)\ne f(x+v)],\quad
j_f(v)=\min\{\alpha_f(v),1-\alpha_f(v)\}.
\]

Write I(f)=sum_i alpha_f(e_i), J(f)=sum_i j_f(e_i), and

\[
\mathfrak I(f)=\min_{(v_1,\ldots,v_n)\text{ a basis}}\sum_i j_f(v_i).
\tag{1.1}
\]

In particular, M(f):=Ifrak(f)<=J(f)<=I(f). Zero entropy terms are zero.

**Theorem 1.** Let Q be an arbitrary polynomial of degree at most two over F_2 on n variables. Let L_j:F_2^n -> F_2^{r_j}, with r_j>=3, and suppose the combined map L=(L_1,...,L_s) is surjective. For arbitrary centres b_j set

\[
F(x)=(-1)^{Q(x)}\prod_{j=1}^s
\left(1-2\mathbf1_{\{L_jx=b_j\}}\right).
\tag{1.2}
\]

Then

\[
\boxed{H(F)\le4\mathfrak I(F)\le4J(F)\le4I(F).}
\tag{1.3}
\]

The constant four is optimal over this class. There is no bound on the number or widths of the clauses, the number of physical variables, the polar rank of Q, or the number of quadratic couplings between different clauses. Sections 2–4 first establish the result for widths at least four, together with an intermediate constant-eight bound for width three. Section 6.2 removes that loss and establishes the displayed constant four for every width.

More generally, an arbitrary polynomial of degree at most three may be added to the phase on a separate set of parameter coordinates, jointly independent of the clause parameters of width at least four. Those core coordinates may be coupled quadratically, without restriction, to all clause and free coordinates. The same constant four holds. This strengthened form is proved in Section 6.2; it is not a claim for arbitrary cubic terms involving the higher-degree clause coordinates themselves.

An empty clause family is allowed: F is then quadratic and H(F)=2 Ifrak(F). Clauses of widths one or two may additionally occur without any independence requirement, because their sign phases are affine or quadratic and can be absorbed into Q.

**What changed relative to the preceding result.** Previously the quadratic seed occupied parameter coordinates independent of the higher-degree clause parameters. Now Q may use those same parameters and arbitrarily couple different clause blocks. For example,

\[
F(x)=(-1)^{x_1x_5}
\left(1-2\mathbf1_{\{x_1=x_2=x_3=x_4=0\}}\right)
\left(1-2\mathbf1_{\{x_5=x_6=x_7=x_8=0\}}\right)
\tag{1.4}
\]

has an allowed quadratic interaction across the two clauses. Its displayed representation does not satisfy the old independence condition for the quadratic and clause parameter blocks. We do not claim to have excluded every possible alternative representation of (1.5) under the older theorem.

This is not a theorem for arbitrary Boolean functions, arbitrary dependent higher-degree affine clauses, or arbitrary products of overlapping high-degree monomials. Such dependencies remain part of the full-scope obstruction.

## 2. A universal entropy lemma retaining coherent Fourier interference

For any Boolean multiplier q, let W be the affine span of its nonzero Fourier labels, translated to a linear subspace, and put d=dim W.

**Lemma 2.1.** For every real function g with E g^2=1,

\[
\boxed{|H(gq)-H(g)|\le d.}
\tag{2.1}
\]

Here entropy refers to the normalized squared Fourier coefficients; gq also has L2 norm one. No Boolean condition on g and no independence assumption are needed.

**Proof.** Write supp(qhat) subset w_0+W. Multiplication by q is orthogonal on the real physical function space, so convolution by qhat is orthogonal on Fourier amplitude vectors. It sends the coordinate subspace indexed by each coset C of W into the subspace indexed by C+w_0. These are pairwise orthogonal subspaces of the same finite dimension, and the map is an isometry on each one. Consequently

\[
\sum_{s\in C}\widehat g(s)^2
=\sum_{s\in C+w_0}\widehat{gq}(s)^2.
\tag{2.2}
\]

Thus the coset masses, and hence the entropy of the coset label, are exactly preserved up to translation. Conditional entropy inside a coset is between zero and log_2 |W|=d. Applying the entropy chain rule to the two distributions proves (2.1).

This is not an unsigned convolution approximation: coefficients within a coset can interfere arbitrarily, and the proof only uses their exactly conserved total squared mass. The dimension of the affine Fourier support, not the ambient dimension, is the cost.

### 2.1 Quadratic multipliers

For q=(-1)^Q, define its alternating polar form

\[
B(v,w)=Q(v+w)+Q(v)+Q(w)+Q(0).
\]

Let B also denote its matrix in a fixed basis, and let rho=rank(B), an even integer. The multiplicative derivative is a sign times the character with label Bv:

\[
q(x)q(x+v)=(-1)^{Q(v)+Q(0)}(-1)^{(Bv)\cdot x}.
\tag{2.3}
\]

Hence its autocorrelation is zero off ker B and is a character on ker B. Fourier inversion of the autocorrelation shows

\[
\widehat q(s)^2=2^{-\rho}\mathbf1_{\{s\in w_0+(\ker B)^\perp\}}
\tag{2.4}
\]

for one affine coset. Its affine support dimension is rho. Therefore Lemma 2.1 gives

\[
\boxed{H(gq)\le H(g)+\rho.}
\tag{2.5}
\]

The coefficient one on rho is sharp: take g=1 and a quadratic phase of polar rank rho. This entropy lemma is a standard consequence of orthogonal block decomposition and the entropy chain rule. It is used here as a proved ingredient, not represented as an established new general information principle.

## 3. The disjoint clause product and its directional spectra

First use coordinates in which the clauses occupy disjoint blocks B_j of sizes r_j>=3. Additional coordinates are free of the clauses. Write

\[
G(x)=\prod_j w_j(x_{B_j}),\qquad
w_j(y)=1-2\mathbf1_{\{y=b_j\}},\qquad
\epsilon_j=2^{1-r_j},
\]
\[
A=\sum_j r_j\epsilon_j,\qquad
\epsilon_* =\max_j\epsilon_j,
\tag{3.1}
\]

with A=epsilon_*=0 for an empty family. Then

\[
\mathfrak I(G)=A,\qquad H(G)\le4A.
\tag{3.2}
\]

The entropy bound and the exact minimum are proved here with their constants, while crediting their use in the preceding report.

For one clause w on r coordinates, its correlation is 1 at v=0 and 1-2epsilon at every nonzero v. Thus j_w(v)=epsilon for v!=0. For G the correlations multiply across blocks, are nonnegative, and

\[
j_G(v)=\tfrac12\left[1-\prod_{j:v_{B_j}\ne0}(1-2\epsilon_j)\right]
\ge\max_{j:v_{B_j}\ne0}\epsilon_j.
\tag{3.3}
\]

At any threshold t, the span of directions with j_G(v)<=t is precisely the direct sum of the free coordinates and the whole blocks with epsilon_j<=t. Indeed the displayed inequality gives one inclusion, and the individual block unit vectors give the other. The usual minimum-weight vector-basis formula therefore gives Ifrak(G)=sum_j r_j epsilon_j. Equivalently, sort directions by cost and retain each one increasing the span; the integral of the missing rank gives the basis cost. In particular the ordinary coordinate basis is an optimal basis, and every one of its costs is at most epsilon_*.

For a single clause the constant Fourier coefficient is 1-epsilon and every other coefficient has magnitude epsilon. Therefore

\[
H(w_r)=-2(1-\epsilon)^2\log_2(1-\epsilon)
 +(4\epsilon-2\epsilon^2)(r-1).
\tag{3.4}
\]

Using -ln(1-epsilon)<=epsilon/(1-epsilon) and ln2>1/2 gives H(w_r)<4r epsilon for r>=2. Entropies add for the product on disjoint blocks, proving (3.2). Furthermore H(w_r)/(r epsilon)->4, which will prove sharpness of (1.3).

### 3.1 Exact derivative Fourier amplitudes

For one clause, define u_v(y)=w(y)w(y+v). If v=0, then u_v=1. If v!=0, the only negative points are b and b+v. Consequently

\[
\widehat u_v(\ell)=
\begin{cases}
1-2\epsilon,&\ell=0,\\
-2\epsilon(-1)^{\ell\cdot b},&\ell\ne0,\ \ell\cdot v=0,\\
0,&\ell\cdot v=1.
\end{cases}
\tag{3.5}
\]

Since r>=3, epsilon<=1/4 and 2epsilon<=1-2epsilon. Every nonconstant Fourier amplitude in (3.5) is therefore no larger in magnitude than the constant amplitude. This is a property of this actual Boolean derivative, not a hypothesis inferred from marginal influences alone.

## 4. Quadratic coupling and the influence cost of its rank

Let F=Gq with q=(-1)^Q as above. The directional correlation factors exactly as

\[
c_F(v)=(-1)^{Q(v)+Q(0)}
\prod_j\widehat{u_{j,v_{B_j}}}((Bv)_{B_j})
\prod_{i\text{ free}}\mathbf1_{\{(Bv)_i=0\}}.
\tag{4.1}
\]

This identity follows by substituting (2.3) and taking expectations over the original independent physical blocks. Q itself need not split over those blocks; the coupled linear character Bv does.

Three consequences are decisive:

\[
\boxed{j_F(v)\ge j_G(v)\quad\text{for all }v,}
\tag{4.2}
\]
\[
\boxed{j_F(v)=j_G(v)\quad\text{when }Bv=0,}
\tag{4.3}
\]
\[
\boxed{j_F(v)\ge\tfrac12-\epsilon_*\quad\text{when }Bv\ne0.}
\tag{4.4}
\]

For (4.2), use (3.5) to bound every factor in magnitude by the corresponding constant derivative coefficient. Their product is c_G(v)>=0. For (4.3), the character in (2.3) is constant and changes only the sign of c_G(v).

For (4.4), a nonzero component of Bv in the free coordinates makes the correlation zero. Otherwise choose a clause block where (Bv) is nonzero. If v is zero on that block the coefficient is zero. If v is nonzero there, (3.5) bounds the corresponding amplitude by 2epsilon_j<=2epsilon_*. All remaining factors have magnitude at most one. Hence |c_F(v)|<=2epsilon_* and (4.4) follows.

**Theorem 4.1 (rank cost).**

\[
\boxed{\mathfrak I(F)\ge A,\qquad
\mathfrak I(F)\ge(\tfrac12-\epsilon_*)\rho,}
\tag{4.5}
\]

and, more strongly,

\[
\boxed{\mathfrak I(F)\ge A+(\tfrac12-2\epsilon_*)\rho.}
\tag{4.6}
\]

**Proof.** The first bound in (4.5) follows by minimizing (4.2) over bases. Every basis contains at least rho vectors outside ker B, since their images must span the rho-dimensional quotient. Equation (4.4) then proves the second bound.

For (4.6), take a basis attaining Ifrak(F) and let t be its number of vectors outside ker B; t>=rho. Its n-t vectors in ker B form an independent set. Complete that set to a basis by t vectors from the coordinate basis of G. Each added vector costs at most epsilon_*, and every completed G-basis has cost at least A. Therefore the cost of the n-t retained vectors, which agrees for F and G by (4.3), is at least A-t epsilon_*. The other t vectors each cost at least 1/2-epsilon_*. It follows that

\[
\mathfrak I(F)\ge A+t(\tfrac12-2\epsilon_*)
\ge A+\rho(\tfrac12-2\epsilon_*),
\]

because epsilon_*<=1/4. No assertion that an arbitrary optimal basis has exactly rho nonkernel vectors is used.

### 4.1 Proof of the entropy–influence bounds

Combining (2.5), (3.2), and (4.5), for epsilon_*<=1/4,

\[
H(F)\le H(G)+\rho\le4A+\rho
\le4\mathfrak I(F)+4\mathfrak I(F)=8\mathfrak I(F).
\]

When every width is at least four, epsilon_*<=1/8. Equation (4.6) then gives

\[
\mathfrak I(F)\ge A+\rho/4,
\qquad H(F)\le4A+\rho\le4\mathfrak I(F).
\]

The quadratic entropy increase is thus paid by an explicitly proved increase in the minimum affine influence. This is the new ingredient beyond simply tensorizing the old seed entropies.

The exact entropy H(G), not just the bound 4A, can also be retained in these calculations. The constants displayed in Theorem 1 are uniform over the stated classes; sharper instance-specific ratios are possible.

## 5. Affine invariance and dependent quadratic parameter forms

For completeness, an invertible coordinate transformation whose columns are v_i changes the ordinary influences to alpha_f(v_i). Multiplication by a character can independently replace each one by its complement. Hence Ifrak is exactly the minimum ordinary influence over invertible affine changes and output characters. Such transformations preserve spectral entropy.

Given the jointly surjective clause map L in Theorem 1, extend its rows to an invertible coordinate system on the physical input space. The clauses now have the disjoint-block form of Section 3; the remaining coordinates are free of the clauses. Q remains quadratic, with its polar rank unchanged. The bounds from Sections 2–4, with the width-three improvement from Section 6.2, apply in these coordinates; invariance of H and Ifrak returns the result to the original physical coordinates.

In particular, there is no requirement that the linear forms appearing in Q be independent of the rows of L, and no requirement that the mixed terms in Q vanish. Quadratic forms may involve every clause and the free coordinates. There can be arbitrarily many dependencies between the quadratic and clause descriptions.

Clauses of width one or two have indicator phases that are polynomials of degree at most two in their affine forms. They can therefore be absorbed into Q even when their forms are dependent on the remaining clause forms. After this absorption, joint surjectivity is only imposed on the clauses of width at least three. If none remain, the function is quadratic and has constant two.

**Limit of this extension.** Joint surjectivity of the higher-degree clauses is still used in (4.1). A product of arbitrary overlapping high-degree monomials need not satisfy it. Dropping that assumption would remove the factorization used to establish (4.2) and (4.4); those inequalities are not asserted in that case.

## 6. Exact spectrum and exact affine influence for one quadratic-twisted clause

The rank estimate is itself sharp. Consider

\[
F(x)=(-1)^{Q(x)}(1-2\mathbf1_{\{x=b\}})
\]

on r>=3 variables, with polar rank rho. Let epsilon=2^{1-r}. Then

\[
\boxed{\mathfrak I(F)=(r-\rho)\epsilon+\rho(\tfrac12-\epsilon)
=r\epsilon+(\tfrac12-2\epsilon)\rho.}
\tag{6.1}
\]

Indeed every nonzero direction in ker B costs epsilon. Every direction off ker B costs 1/2-epsilon: its derivative label Bv is nonzero and has dot product v^T Bv=0, so (3.5) gives absolute correlation 2epsilon. These costs are ordered as written when r>=3, and a basis extending ker B attains (6.1).

There is also a complete three-mass description of the squared spectrum. Translate b to zero and normalize q(0)=1, which does not change entropy. Put beta=2^{-rho/2} and

\[
N_+=\frac{2^\rho+2^{\rho/2}}2,\qquad
N_-=\frac{2^\rho-2^{\rho/2}}2.
\]

The nonzero Fourier coefficients of q have magnitude beta. Their sum is q(0)=1, so N_+ of them are positive and N_- negative. Since F=q-2 delta_0, its Fourier coefficients subtract epsilon from every label. Thus its squared spectrum consists of

\[
(\beta-\epsilon)^2\text{ repeated }N_+\text{ times},\quad
(\beta+\epsilon)^2\text{ repeated }N_-\text{ times},\quad
\epsilon^2\text{ repeated }2^r-2^\rho\text{ times}.
\tag{6.2}
\]

Zero masses are allowed. Formula (6.2) determines H(F) exactly as a function only of r and rho. It is not an assertion that differently arranged quadratic factors have identical Fourier labels; only their coefficient-magnitude multiset is the same in this one-clause setting.

At rho=0 this reduces to the familiar one-point law. Its ratio H/Ifrak tends to four as r grows, proving the optimality claim in Theorem 1. At nonzero rho the exact minimum (6.1) attains the lower bound (4.6), showing that its rank coefficient cannot generally be increased.

### 6.2 Cubic cores, and the improvement from eight to four

The following form includes every width-three clause and allows more general, interacting cubic terms on their combined core variables.

Write the coordinates as (z,y), where z belongs to a k-dimensional core and y contains the mutually disjoint clause blocks of widths at least four, together with any free coordinates. Let G(y) be their product. Suppose a Boolean core g has the derivative spectral-gap property

\[
\max_\ell|\widehat{g g^v}(\ell)|\le1-2\gamma
\quad\text{for every nonzero core direction }v.
\tag{6.3}
\]

Here gamma>0, and all transforms use the uniform core measure. Let Q(z,y) be arbitrary quadratic and set F=g(z)G(y)(-1)^Q. Write its polar matrix in block form as

\[
B=\begin{pmatrix}B_{cc}&D\\D^T&E\end{pmatrix},\qquad
r=\operatorname{rank}[D^T\ E].
\tag{6.4}
\]

Thus r is the rank of the map giving the **y component** of Bv, not necessarily the full polar rank. Keep A and epsilon_* for G only. If

\[
\epsilon_*\le\gamma\le\tfrac12-\epsilon_*,
\]

then

\[
\boxed{H(F)\le k+H(G)+r,}
\tag{6.5}
\]
\[
\boxed{\mathfrak I(F)\ge\gamma k+A+(\tfrac12-2\epsilon_*)r.}
\tag{6.6}
\]

**Entropy proof.** For each fixed physical core value z, the y-section is, up to a sign, G(y)(-1)^{Q(0,y)} times the character with label D^T z. Parseval in the core Fourier variables shows that the y marginal of the full squared spectrum is exactly the average of these section spectra. Let W=im(E)+im(D^T), of dimension r. The multiplier (-1)^{Q(0,y)} has Fourier support in a translate of im(E), so Lemma 2.1 preserves every W-coset mass up to a fixed translation. The subsequent shifts D^T z lie in W and do not change those masses. Hence the y marginal has exactly the W-coset masses of p_G, up to translation. Its entropy is at most H(p_G mod W)+r<=H(G)+r. The remaining conditional core-label entropy is at most k. This proves (6.5) without replacing the actual shared-section mixture by independent samples.

**Influence proof.** Let L_t(F) be the span of directions with j_F(v)<=t. For t<gamma, property (6.3) forces the core component of every cheap direction to vanish: otherwise the core derivative factor alone bounds the absolute full correlation by 1-2gamma. A nonzero core component of Bv then kills the constant core derivative coefficient. A nonzero y component of Bv either kills a free-coordinate factor or gives a clause amplitude at most 2epsilon_*, which would cost at least 1/2-epsilon_*>=gamma. Thus every such direction has the form (0,w), with w in

\[
K=\ker D\cap\ker E.
\]

On this subspace its cost equals j_G(w). The codimension of K in the y space is r, since the matrices [D;E] and [D^T E] are transposes. Therefore, for t<gamma,

\[
\operatorname{codim}L_t(F)\ge k+
\max\{r,\operatorname{codim}L_t(G)\}.
\]

The cheap-direction span for G is the full y space for t>=epsilon_*, and its missing-rank integral equals A. Integration from zero to gamma consequently gives at least

\[
\gamma k+A+(\gamma-\epsilon_*)r.
\]

For gamma<=t<1/2-epsilon_*, every cheap direction must still have zero y component of Bv, by the same clause coefficient estimate. Its span is contained in the kernel of the rank-r map [D^T E], so the missing rank is at least r on this entire interval. Adding that interval's contribution proves (6.6). Values exactly at the interval endpoints do not affect the rank integral. No claim that cheap vectors themselves form a subspace is needed; their spans are what enter the calculation.

**Application to arbitrary cubic cores.** Let g=(-1)^P, with deg P<=3. The set R of core directions for which P(x+v)+P(x) is affine is a linear subspace. Closure follows from the derivative identity and preservation of affine functions under translation. Choose a basis adapted to R. A direction in R cannot occur in a cubic monomial in that basis, since differentiating in it would leave a quadratic term. Thus all terms involving R are of degree at most two and can be absorbed into Q. The residual core, on the quotient, has a non-affine quadratic derivative in every nonzero direction. Such a derivative phase has polar rank at least two and therefore all Fourier amplitudes have magnitude at most one half, by (2.4). This proves (6.3) with gamma=1/4. Coordinates of R become free y coordinates; this change acts only inside the original core and preserves independence from the clause blocks.

For widths at least four, epsilon_*<=1/8. Equations (6.5)–(6.6) now give

\[
H(F)\le k+4A+r
\le4\left[\tfrac14 k+A+(\tfrac12-2\epsilon_*)r\right]
\le4\mathfrak I(F).
\tag{6.7}
\]

A width-three clause is a cubic phase on its three parameter coordinates. Combining all such clauses into the cubic core and using (6.7) proves Theorem 1 with constant four for **all** the allowed clause widths, not just widths at least four. The first constant-eight calculation in Section 4 is a valid intermediate estimate, not the final result.

The pure-cubic special case is established elementary background: constant-sized lower bounds for nontrivial directional influences already give FEI for bounded algebraic degree. The contribution here is the simultaneous compatibility with arbitrarily wide rare clauses and unrestricted quadratic coupling, established by the conditional coset and rank calculations. General cubic terms sharing the wide-clause variables, or genuinely dependent higher-degree clause forms, are still outside the hypotheses.


### 6.3 A bounded-degree core extension

The same argument permits an arbitrary independent core phase P of degree at most d>=3, at the cost of the explicit constant 2^{d-1}. Absorb every clause of width at most d into that core; the remaining independent clauses have widths at least d+1. Allow arbitrary quadratic coupling between the core, clause, and free coordinates. Then

\[
\boxed{H(F)\le2^{d-1}\mathfrak I(F).}
\tag{6.8}
\]

To prove this, the directions where the phase derivative is affine again form a subspace. In an adapted basis, all degree-at-least-three terms are supported on its complementary core; the other terms are absorbed into Q. For every nonzero direction of the residual core, the derivative polynomial has degree at most d-1 and is not affine.

A nonzero multilinear polynomial of degree at most s on the uniform binary cube has probability of being one at least 2^{-s}. Here is the standard elementary induction: split on a variable occurring in a highest-degree monomial, so the coefficient of that variable is a nonzero polynomial of degree at most s-1. Whenever that coefficient equals one, exactly one of the two sections equals one. Apply induction to the coefficient. Constant polynomials supply the base case. Applying this to a non-affine derivative plus any affine polynomial, and to its complement, proves that every Fourier amplitude of its sign phase is at most 1-2^{2-d}. Hence (6.3) holds with gamma=2^{1-d}.

The wide clauses now satisfy epsilon_*<=2^{-d}=gamma/2. Equations (6.5)–(6.6), with H(G)<=4A, imply (6.8): 1/gamma=2^{d-1}>=4, and (1/2-2epsilon_*)/gamma>=1. The pure bounded-degree FEI estimate is established background, not a new solution of that special case. This corollary combines it with arbitrarily wide rare clauses and quadratic couplings. Allowing d to grow does not give a universal constant, so (6.8) is not unrestricted FEI.

## 7. Consequence for the full derivative chain on the new class

Use the independent uniform multiplicative-derivative chain f_{k+1}=f_k f_k(.-Z_{k+1}). Let

\[
\mathfrak A(f)=H(S\mid S\triangle T,S\cap T),\quad
\mathcal T(f)=\sum_{k\ge0}2^{-k}\mathbb E\mathfrak A(f_k),
\]

where S,T are independent squared-Fourier samples at that state. The predecessor proves the unconditional comparison T(f)<=2H(f). Its elementary proof uses D_cross>=A and the exact entropy telescoping identity; it does not assume FEI.

Therefore for the full class of Theorem 1, including its arbitrary cubic-core extension,

\[
\boxed{\mathcal T(F)\le8\mathfrak I(F).}
\tag{7.1}
\]

For the bounded-degree extension (6.8), the corresponding bound is T(F)<=2^d Ifrak(F). These are bounds on the actual entire derivative chain. We do not assume that later derivatives remain in the class. The independent entropy proof above supplies the bound.

## 8. Global attempts that did not close the conjecture

### 8.1 Replacing the accumulated allocation entropy by a single affine-influence drift

The prior report mentioned the possible quantity

\[
\Delta_{\rm aff}(f)=2\mathfrak I(f)-\mathbb E_z\mathfrak I(f f^z).
\]

This continuation computed it for odd majority in dimensions 3 through 19, using exact Walsh correlations and symmetry-generated rank filtrations; displayed entropy ratios in this exploratory probe are floating point. The observed ratio D_cross/Delta_aff rose from 2 at dimension three to about 2.65849 at dimension nineteen. The observed drift stayed between 2 and 2.577 on this range. These finite observations do NOT establish a divergent asymptotic, disprove a universal constant, or prove the drift inequality.

The exploratory program and output are retained separately. They are not part of the rational proof certificate and are not counted as a new universal theorem. No unproved affine-drift estimate is used in Sections 1–7.

### 8.2 Why the rank argument is not already a universal FEI proof

Quadratic perturbations have character-valued multiplicative derivatives. This is what turns the coupled expectation into the individual derivative coefficients in (4.1). A higher-degree perturbation generally has a sum of many Fourier characters in each derivative. The resulting signed sums need not retain either the constant-coefficient dominance (4.2) or the uniform nonkernel cost (4.4). No bound for that general interference was proved here.

Every Boolean phase has an algebraic normal form, but its monomials need not have independent parameter blocks. Expressing a phase as a sum of monomials is not enough to apply this theorem. The existence of a representation whose entropy cost is universally paid by I is still unproved.

The exact full-scope targets remain a universal bound on the accumulated allocation T/J, the correctly quantified hereditary-erasure inequality, or another complete all-dimensional argument. The earlier scalar and full-resolvent pointwise inequalities remain disproved and are not revived. A smaller constant on the present class is not itself progress on the missing universal bound.

## 9. Executed checks and provenance

Run `python verify_quadratic_coupling.py --output verification.json` with the included unchanged `prior_exact_entropy.py`.

The final checker passed twice with identical non-timing output. It checks 2,086 Boolean-function/quadratic pairs, 263 coupled-clause examples and 103,488 directional formulas, 18 surjective affine lifts, 76 cubic-core examples with 32,000 directional comparisons and 76 marginal-coset identities, and 192 cubic polynomials with possibly nontrivial affine-derivative radical. It also checks the exact three-mass spectrum and affine influence for every tested one-clause example, as well as closed-form sharpness values. The cubic-core tests include exact joint directional correlations, the marginal coset identity (6.5), the stronger rank bound (6.6), and the adapted-coordinate radical removal. It uses integer Walsh transforms, Fraction probabilities, exact minimum-weight binary bases, exact coset mass comparisons, and outward rational logarithm intervals. It verifies the universal entropy-gate identities on every Boolean truth table through dimension three and every quadratic polar form in those dimensions. It checks the coupled class on full truth tables with arbitrary internal and cross-block quadratic terms, the predicted correlation formula in every direction of each tested example, the minimum-influence lower bounds, and surjective affine transformations. Separate closed-form evaluations approach the sharp constant four without enumerating large truth tables. The actual counts and results are in verification.json; none are extrapolated to certify all dimensions.

An initial attempt to evaluate very large one-point logarithms through general integer factorization was stopped by the runtime timeout. The final checker instead uses direct range-reduced rational logarithm enclosures for those values. The passed output comes from that final code, not from the interrupted run.

The entropy arithmetic dependency is copied unchanged from the balanced-substitution checker (Git blob `e867ba6b12e1a3e7588fd812eba6841319cd97b9`, SHA256 `9600d6b961d26f9131277b830894c0e9497fefdaee2a9291507885cdf40326ab`). Reuse of that dependency is not an independent implementation or audit.

Consumed source: `proofnet24/P03-fei/continuations/2026-09-19-affine-variance/REPORT.md`, Git blob `2fa7fb2f510b10ceedc53fd560b87defa904c6dc`, read in full. It supplies the prior affine minimum, seed calculation, and unconditional T<=2H comparison. The latest index was fetched at blob `5f9136739dcd11c90629aa4482ac0be1edfde16f`. The earlier addressing barrier was read at blob `c1e52dff50095854d85c20e8b13a5385d91efaca`, to avoid proposing an already disproved positive-power edge majorant. At initial inspection the scheduled-continuation directory exposed its contract and no substantive run report; no later-run uptake is inferred from that observation.

Outside primary-source comparison, checked 19 September 2026: O'Donnell–Tan, arXiv:1304.1347, establishes the broader prior composition framework; Gangopadhyay–Stanica, IACR ePrint 2014/054, discusses monomial, direct-sum, concatenation, plateaued, and affine-quadratic classes; González–MacManus–Pereyra, arXiv:2606.00246, studies a restriction-induction framework. The accessible abstracts and targeted searches were checked. Their full papers were not all line-by-line compared in this session, so no claim is made that the present class theorem or every ingredient is absent from the literature. Standard quadratic Fourier facts and the minimum-weight basis principle are background.

## 10. Worker handoff

Source status: **full FEI OPEN**. Positive delta: a constant-four theorem with arbitrary quadratic coupling for jointly independent affine clauses of every width, and more generally for an arbitrary independent cubic core coupled to clauses of width at least four; exact entropy-coset conservation and rank-dependent lower bounds for minimum affine influence. The initial constant-eight loss for width three is removed by the cubic-core argument.

For continuation, do not replace quadratic coupling by arbitrary polynomial coupling in (4.1), and do not drop joint surjectivity of the higher-degree clause forms. The exact next obstruction is the signed sum over multiple derivative Fourier characters produced by genuinely higher-degree dependence. A proof for that situation needs an additional argument, not a reuse of the single-character rank calculation. Keep the independent all-scope allocation/erasure routes available. No schedule, ownership, source status, visibility, or native metric is changed by this research report.
