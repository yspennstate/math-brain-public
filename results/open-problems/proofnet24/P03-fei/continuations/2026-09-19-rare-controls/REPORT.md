# Rare controls, arbitrary quadratic perturbations, and affine entropy excess

19 September 2026. **Full Friedgut–Kalai FEI remains OPEN.**

This continuation proves an unconditional contraction of affine entropy excess under a controlled quadratic construction. It yields a dimension- and depth-independent FEI theorem for an explicitly generated class in which high-degree terms may share entire control blocks. The quadratic perturbation theorem applies to **every sufficiently biased Boolean base**, without any clause factorization, algebraic-degree bound, or independence assumptions inside that base. A separate corollary handles arbitrary error sets of exponentially small density around a quadratic phase.

These are analytical results with executed exact self-checks. They are not a full FEI proof, independent expert review, Lean verification, or a comprehensive novelty clearance. The older conjunction-composition and affine-rank results are credited and distinguished below.

## 1. Main result: a universal excess contraction

All spaces are binary vector spaces with the uniform measure. For Boolean f, let

\[
H(f)=\sum_s\widehat f(s)^2\log_2(1/\widehat f(s)^2),\qquad
\alpha_f(v)=\Pr[f(x)\ne f(x+v)],
\]
\[
M(f)=\min_{(v_i)\text{ a basis}}\sum_i\min\{\alpha_f(v_i),1-\alpha_f(v_i)\}.
\]

The predecessor identifies M with the minimum ordinary influence under invertible linear input changes and output-character multiplication. In particular M<=J<=I. H and M are invariant under extended-affine transformations and surjective affine pullbacks, and add under products on disjoint variable blocks. A proof of the needed facts is recalled in Section 2.

For a real constant C define the affine entropy excess

\[
\Phi_C(f)=H(f)-C M(f).
\]

This is simply a signed quantity; its nonpositivity for arbitrary f is not assumed.

For c fresh independent bits z, let b(z)=1{z=0} and define

\[
\Gamma_c f(z,y)=1-b(z)(1-f(y)).
\tag{1.1}
\]

Thus the output is f(y) when z=0 and is +1 otherwise. Any other affine center of the control cube is equivalent by translation. Write

\[
\kappa=1+2/\ln2,\qquad
C_* =4+\kappa/4=\frac{17}{4}+\frac1{2\ln2}
\in(4.971347520444,4.971347520445).
\tag{1.2}
\]

**Theorem 1 (unconditional controlled-quadratic contraction).** For every Boolean f, every integer c>=4, every quadratic polynomial Q in all the c+dim(f) variables, and every C>=C_*,

\[
\boxed{\Phi_C\bigl((-1)^Q\Gamma_c f\bigr)
\le 2^{-c}\Phi_C(f).}
\tag{1.3}
\]

There is no FEI hypothesis on f in (1.3). Q may couple every old variable and every new control variable. The conclusion is an inequality relating the two excesses, not an assertion that either excess is nonpositive. This construction appends coordinates; it is not a drift inequality for the fixed-domain multiplicative-derivative chain and cannot be inserted into that chain's telescoping formula.

**Corollary 1.1 (an explicitly generated FEI class).** Start with any seed family satisfying H<=C_*M; for example the previously proved constant-four coupled-clause/cubic-core family. Close under:

1. products of functions on disjoint current variable blocks;
2. extended-affine changes and jointly surjective affine pullbacks;
3. the operation f -> (-1)^Q Gamma_c f, for c>=4 and arbitrary Q on the full enlarged variable space.

Every function F obtained after any finite number of such operations satisfies

\[
\boxed{H(F)\le C_*M(F)<5M(F)\le5J(F)\le5I(F).}
\tag{1.4}
\]

The non-strict form H<=5M applies also when M=0. The coefficient does not multiply with depth, dimension, clause width, quadratic rank, or the number of factors. More generally, any C>=C_* is preserved when its seed family is proved to satisfy H<=CM. No optimality claim is made for C_*.

For the actual multiplicative-derivative chain, the existing unconditional inequality T(F)<=2H(F) gives

\[
\mathcal T(F)\le2C_*M(F)<10M(F)
\tag{1.5}
\]

when M>0, with equality zero on characters. No closure of the constructed class under multiplicative differentiation is assumed.

The control bits must be fresh at the moment of construction. Replacing them by arbitrary dependent old parameters is **not** covered. The seed hypothesis is essential: applying (1.3) to an unproved seed does not establish FEI for it or for its controlled output.

## 2. Affine influence facts and an unfolded version

Let c_f(v)=E f(x)f(x+v). The folded directional cost is j_f(v)=(1-|c_f(v)|)/2. Define also

\[
M_0(f)=\min_{(v_i)\text{ a basis}}\sum_i\alpha_f(v_i).
\tag{2.1}
\]

M_0 permits invertible input changes but not an output character. Always M<=M_0<=I. The distinction is necessary: a nonconstant character has M=0 but M_0=1.

For any nonnegative weights w(v) on the nonzero vectors of a finite binary space of dimension n, the minimum basis weight has the rank-integral formula

\[
\min_{\text{basis }(v_i)}\sum_i w(v_i)
=\int_0^{\max w}\left[n-\dim\operatorname{span}\{v:w(v)\le t\}\right]dt.
\tag{2.2}
\]

Every basis has at most the displayed cheap-span rank below each threshold, proving one inequality by integration. Greedily retain vectors that increase the span, in increasing weight order. At each threshold they span precisely all available vectors, so the greedy basis attains equality. Ties do not affect the integral. Use w=j for M and w=alpha for M_0.

The autocorrelations of a disjoint product factor. Hence

\[
j_{fg}(v,w)=\frac{1-|c_f(v)c_g(w)|}{2}
\ge\max(j_f(v),j_g(w)).
\]

Embedded directions (v,0),(0,w) retain their costs, so the cheap spans split as direct sums. Formula (2.2) proves M(fg)=M(f)+M(g). This does not assert that M_0 tensorizes for arbitrary functions; it need not. For a surjective input map A, cheap spans lift to inverse images under A, proving invariance of M. Fourier labels inject under A^T, preserving H. Invertible maps, translations, and characters give the other invariances.

These M facts are reused from the affine-variance report. They are not newly discovered in this continuation.

## 3. Exact affine influence of a control

Set p=2^{-c}, mu=E f, and d=1-mu in [0,2]. Write G=Gamma_c f. For a direction (u,v), with u in the control space,

\[
\alpha_G(u,v)=
\begin{cases}
p\alpha_f(v),&u=0,\\
pd,&u\ne0.
\end{cases}
\tag{3.1}
\]

If u=0, only the active control section contributes. If u is nonzero, the active sections z=0 and z=u are disjoint, each contributing p Pr(f=-1); their sum is pd. No assumption about the internal dependence of f is involved.

For every Boolean f, alpha_f(v)<=2Pr(f=-1)=d by the union bound on its negative set and its translate. If c>=2, all the costs in (3.1) are at most 1/2. They therefore coincide with their folded costs.

For a threshold t<pd, only directions in the kernel of the control projection are cheap, and their span is 0 direct-sum span{v:alpha_f(v)<=t/p}. At t>=pd, all directions are cheap. Integrating this statement with (2.2) gives

\[
\boxed{M(\Gamma_c f)=p[M_0(f)+cd],\qquad c\ge2.}
\tag{3.2}
\]

The ordinary coordinate calculation likewise gives

\[
I(\Gamma_c f)=p[I(f)+cd].
\tag{3.3}
\]

The c=0 or c=1 endpoint is not silently included. For example, an input with negative mean can make the control cost in (3.1) exceed one half when c=1; folding must then be handled separately.

One must not replace M_0 by M in (3.2). For a one-bit character and c=4, the actual values are M(f)=0, M_0(f)=1, and M(G)=5/16, not 4/16. The exact verifier checks this warning directly.

## 4. Exact entropy of a control and a uniform surplus estimate

For t>=0 define eta(t)=-t log_2 t, with eta(0)=0. Values at t>1 are allowed and are negative; eta there is an algebraic scalar function, not the entropy of a probability.

The nonzero Fourier coefficients of G are explicit. With s indexing the old variables and a indexing the c control variables,

\[
\widehat G(s,a)=p\widehat f(s)\quad(s\ne0),
\]
\[
\widehat G(0,a)=-pd\quad(a\ne0),\qquad
\widehat G(0,0)=1-pd.
\tag{4.1}
\]

Signs from translating the control center do not change their squares. Put

\[
v=2pd-p^2d^2=\operatorname{Var}(G),
\]
\[
R(p,d)=\eta((1-pd)^2)-p\eta((1-d)^2)+(p-p^2)\eta(d^2).
\]

Summing the squared coefficients in (4.1), including their multiplicities, proves the exact identity

\[
\boxed{H(G)=pH(f)+2cv+R(p,d).}
\tag{4.2}
\]

This is a direct signed Fourier expansion. There is no replacement of overlapping amplitudes by an unsigned probability mixture.

**Lemma 4.1.** For 0<p<=1/4 and 0<=d<=2,

\[
\boxed{R(p,d)\le\kappa pd,\qquad \kappa=1+2/\ln2<4.}
\tag{4.3}
\]

**Proof.** The inequality -t ln t<=1-t on [0,1] gives

\[
\eta((1-pd)^2)\le(2pd-p^2d^2)/\ln2\le2pd/\ln2.
\tag{4.4}
\]

If 1<=d<=2, eta(d^2)<=0 and eta((1-d)^2)>=0. The other terms only decrease (4.4).

If 0<=d<=1/2, then eta(d^2)<=eta((1-d)^2). To prove this last inequality, consider

\[
g(d)=d^2\ln d-(1-d)^2\ln(1-d).
\]

Its endpoint values on [0,1/2] are zero, and g''(d)=2 ln(d/(1-d))<=0, so concavity gives g>=0. Thus
(p-p^2)eta(d^2)-p eta((1-d)^2)<=0 in this range as well.

Finally, if 1/2<=d<=1, eta(d^2)<=d. Indeed eta(d^2)/d=2d log_2(1/d) is decreasing on this interval and equals one at d=1/2. Here

\[
(p-p^2)\eta(d^2)-p\eta((1-d)^2)\le pd.
\]

Combining the cases proves (4.3). For kappa<4, use ln2>2/3, which follows by strict Jensen from integrating 1/t on [1,2]. Endpoint values are by continuity.

From (4.2)–(4.3),

\[
H(G)\le pH(f)+(4c+\kappa)pd.
\tag{4.5}
\]

Combine with the exact affine minimum (3.2). For every real C,

\[
\boxed{\Phi_C(G)\le p\Phi_C(f)-Cp[M_0(f)-M(f)]
-pd[c(C-4)-\kappa].}
\tag{4.6}
\]

In particular, if C>=4+kappa/c, then Phi_C(G)<=p Phi_C(f). This is an unconditional excess inequality for every input f. When c>=4 and C>=C_*, that condition holds uniformly.

The standard conjunction/selection construction and its coefficient expansion overlap earlier composition work. The new role of (3.2) and (4.6) is to control the affine-minimum excess before an arbitrary quadratic coupling, including dense changes of physical coordinates.

## 5. Quadratic perturbations of arbitrary rare Boolean functions

The previous coupling theorem used products of independent clauses. That factorization is **not** needed for the following result.

**Theorem 5.1 (rare-base rank cost).** Let g be any Boolean function on n bits with negative density delta=Pr(g=-1)<=1/8. Let Q be any quadratic polynomial and let B be its alternating polar matrix of rank rho. Then

\[
\boxed{M(g(-1)^Q)\ge M(g)+(\tfrac12-4\delta)\rho.}
\tag{5.1}
\]

Also,

\[
\boxed{|H(g(-1)^Q)-H(g)|\le\rho.}
\tag{5.2}
\]

Consequently, for C>=0,

\[
\boxed{\Phi_C(g(-1)^Q)\le\Phi_C(g)
-[C(\tfrac12-4\delta)-1]\rho.}
\tag{5.3}
\]

In particular, delta<=1/16 and C>=4 imply that the affine entropy excess cannot increase. There are no requirements on the arrangement of the negative points of g, its algebraic degree, clause representation, or coordinate dependence.

### 5.1 Direction-by-direction proof of the rank cost

For u_v(x)=g(x)g(x+v), let a_v=Pr(u_v=-1)=alpha_g(v). The union bound gives a_v<=2delta<=1/4. Thus

\[
\widehat u_v(0)=1-2a_v\ge1/2,
\]

while every nonconstant coefficient satisfies

\[
|\widehat u_v(\ell)|
=2|\widehat{1_{\{u_v=-1\}}}(\ell)|\le2a_v\le1-2a_v.
\tag{5.4}
\]

The quadratic derivative is a sign times the character with label Bv. It follows that

\[
j_{g(-1)^Q}(v)\ge\alpha_g(v),
\quad j_{g(-1)^Q}(v)=\alpha_g(v)\ \text{when }Bv=0,
\tag{5.5}
\]

and, when Bv!=0,

\[
j_{g(-1)^Q}(v)\ge\tfrac12-2\delta.
\tag{5.6}
\]

Take a basis minimizing M(g(-1)^Q), and let t of its vectors lie outside ker B. Necessarily t>=rho. Complete its n-t kernel vectors to a basis using t vectors of any fixed basis for g. Every added direction costs at most 2delta. Therefore the retained kernel vectors have total g-cost at least M(g)-2delta t. Add (5.6) on the t other vectors:

\[
M(g(-1)^Q)\ge M(g)+t(\tfrac12-4\delta)
\ge M(g)+\rho(\tfrac12-4\delta).
\]

The coefficient is nonnegative under the stated delta<=1/8 assumption. This proves (5.1). In particular M(g)=M_0(g) here, since all directional correlations of g are nonnegative.

### 5.2 Entropy proof retaining coherent interference

For q=(-1)^Q, the squared Fourier law is uniform on an affine coset of (ker B)^perp, whose dimension is rho. This follows by Fourier inversion of q's autocorrelation: it is zero off ker B and a character on ker B.

Multiplication by q is an orthogonal map on Fourier amplitudes. It maps each coset subspace of (ker B)^perp isometrically into a translated coset subspace. Hence it preserves every coset's total squared amplitude. The entropy of the coset label is unchanged; the conditional entropy inside a coset lies between zero and rho. This proves (5.2), and combining it with (5.1) proves (5.3).

This coset entropy lemma is reused from the quadratic-coupling report; the new part of Theorem 5.1 is its compatibility with **every rare base**, not only independently factored clauses.

### 5.3 Sharpness and necessity of the density assumption

For a one-point defect g=w_n on n>=3 bits, delta=2^{-n}. Every nonzero kernel direction has cost 2delta. Every direction outside ker B has cost 1/2-2delta. The latter assertion uses v^T Bv=0 in the exact two-point derivative spectrum. Therefore

\[
M(w_n(-1)^Q)=2n\delta+(\tfrac12-4\delta)\rho,
\tag{5.7}
\]

attaining (5.1) for every allowed polar rank. Thus the rank coefficient is sharp along these attainable dyadic densities.

There is no unrestricted monotonicity of M under quadratic multiplication. On two bits let g=(-1)^{x_1x_2}, of negative density 1/4 and M(g)=1. Multiplying by the same quadratic makes the function constant, with M=0. The rarity condition is doing mathematical work.

### 5.4 A global ratio consequence

Whenever delta<=1/16 and M(g)>0,

\[
\boxed{\frac{H(g(-1)^Q)}{M(g(-1)^Q)}
\le\max\left\{\frac{H(g)}{M(g)},4\right\}.}
\tag{5.8}
\]

This follows from H(gq)<=H(g)+rho and M(gq)>=M(g)+rho/4. Cases with zero denominator are characters with zero entropy and are interpreted separately. Thus putting an arbitrary quadratic background under a rare error pattern cannot create an entropy–influence ratio above both four and that of the error pattern. This statement assumes no FEI bound on the pattern.

## 6. Proof of Theorem 1 and the recursive class theorem

For G=Gamma_c f, its negative density is

\[
\delta_G=2^{-c}\Pr(f=-1)=pd/2\le2^{-c}\le1/16
\]

when c>=4. Apply (4.6) and then (5.3). With rho the polar rank of Q,

\[
\begin{aligned}
\Phi_C((-1)^QG)
\le{}&p\Phi_C(f)-Cp[M_0(f)-M(f)]\\
&-pd[c(C-4)-\kappa]
-[C(\tfrac12-4\delta_G)-1]\rho.
\end{aligned}
\tag{6.1}
\]

For C>=C_*, every subtracted coefficient is nonnegative: M_0>=M, c(C-4)>=kappa, and C(1/2-4delta_G)>=C/4>=1. This proves Theorem 1.

A product node adds Phi_C exactly, an extended-affine node preserves it, and a controlled-quadratic node multiplies its upper bound by p. Induction on any finite construction proves Corollary 1.1. More explicitly, for any expression with arbitrary seed functions f_l at its leaves,

\[
\Phi_C(F)\le\sum_l 2^{-g_l}\Phi_C(f_l),
\tag{6.2}
\]

where g_l is the total number of fresh control bits on that leaf-to-root path. This formula discards the additional nonnegative credits in (6.1). It does not assume the leaf excesses have a sign. Taking proven nonpositive seed excesses gives the class FEI theorem.

### 6.1 Concrete dependencies now included

Let P(y,w)=prod_{i=1}^r y_i+prod_{j=1}^s w_j, with r,s>=3, and set

\[
F(z,y,w)=(-1)^{Q(z,y,w)+(z_1z_2z_3z_4)P(y,w)}.
\tag{6.3}
\]

The two high-degree terms share all four control variables. Their displayed clause parameter maps are not jointly independent. Nevertheless the seed (-1)^P is a disjoint product of one-point clauses, so (1.4) applies with arbitrary Q, including quadratic terms between the petals and controls.

One may first use a quadratic-coupled seed P=Q_0(y,w)+P_0(y,w). Controlling it multiplies Q_0 by z_1z_2z_3z_4, creating degree-six terms coupling old blocks. Repeating the construction produces higher-degree dependencies of unbounded depth without increasing C_*. Dense extended-affine maps can be inserted between stages.

This proves a result beyond requiring all high-degree clause parameter maps in the displayed representation to be jointly independent. It does not claim to exclude every possible alternative representation under an older theorem. Nor does it include arbitrary overlapping clauses: each dependency must arise through an allowed controlled construction, or another separately proved seed theorem.

### 6.2 Additional seed family: unstructured sparse errors around quadratics

Let g be arbitrary with 0<delta=Pr(g=-1)<=1/16 and put ell=log_2(1/delta). Its constant Fourier mass is (1-2delta)^2 and its remaining mass is v=4delta(1-delta). Conditional entropy on the nonempty frequencies gives

\[
H(g)\le h_2(v)+v\log_2(2^n-1).
\]

Since h_2(v)<=v log_2(e/v), and t log_2(e/t) is increasing for t<=1,

\[
H(g)\le4\delta[n+\ell+\log_2 e-2]
\le4\delta(n+\ell).
\tag{6.4}
\]

Every invertible input change preserves delta, and all directional correlations are positive, so M=M_0. The cube edge-isoperimetric inequality, applied to a minimizing linear representative, gives

\[
M(g)\ge2\delta\ell.
\tag{6.5}
\]

This is the established biased-function entropy/isoperimetry argument, not a new claim that arbitrary rare functions satisfy a universal constant. Combining it with (5.8), and noting ell<=n for a nonempty error set, gives

\[
\boxed{H(g(-1)^Q)\le\left(2+\frac{2n}{\ell}\right)M(g(-1)^Q).}
\tag{6.6}
\]

Thus every function differing from an arbitrary quadratic phase on a set of density at most min(1/16,2^{-n/2}) satisfies H<=6M. With density at most min(1/16,2^{-3n/4}), the constant is 14/3<C_*, so these functions can be added as seeds in Corollary 1.1. The error set is entirely unstructured; no degree, factorization, or independence condition is imposed on it.

If delta=0 the function is quadratic and H=2M. For merely polynomially small or fixed small delta, the constant in (6.6) need not be dimension-independent. No such stronger conclusion is asserted.

### 6.3 Relation to the existing allocation program

For completeness, D_cross(f)=2H(f)-E H(ff^Z) satisfies D_cross>=A(f), where A is the conditional allocation entropy. This follows by averaging derivative spectra to the XOR convolution and using the entropy chain rule. Repeated multiplicative derivatives lower the algebraic degree of the phase, so entropy telescoping terminates and gives T<=2H. Consequently every FEI estimate proved here bounds the whole allocation chain with twice its constant. The global bound T/J for arbitrary functions is still unknown.

## 7. Why the contraction does not finish unrestricted FEI

There are two distinct limitations.

First, (1.3) transports a seed's excess; it does not make an unknown positive excess nonpositive. Second, a four-bit control has to be added independently. Removing controls by restriction or reusing dependent old bits does not preserve any proved constant here.

An exact reduction makes the first limitation concrete. Given an arbitrary non-character f, choose an extended-affine representative f_0 with ordinary influence I(f_0)=M(f_0)=M(f). Then M_0(f_0)=M(f), and tensorization implies

\[
M_0(f_0^{\otimes q})=M(f_0^{\otimes q})=qM(f).
\]

Indeed the middle quantity is qM by the established tensor theorem, while M_0 lies between it and the ordinary influence qM. Choose a global sign so E f_0>=0, without changing any of these quantities. For any fixed c>=2, (3.2) gives

\[
M(\Gamma_c(f_0^{\otimes q}))
=2^{-c}[qM(f)+c(1-(E f_0)^q)].
\tag{7.1}
\]

Its ordinary influence is exactly the same. Formula (4.2) gives

\[
H(\Gamma_c(f_0^{\otimes q}))=2^{-c}qH(f)+O_c(1),
\tag{7.2}
\]

because all the remaining scalar terms are uniformly bounded for d in [0,2]. Thus

\[
\frac{H(\Gamma_c(f_0^{\otimes q}))}
{I(\Gamma_c(f_0^{\otimes q}))}
\longrightarrow\frac{H(f)}{M(f)}.
\tag{7.3}
\]

For c=4 every output has negative density at most 1/16 (in fact at most 1/32 after the chosen sign). Therefore restricting FEI to that biased test family, with an *arbitrary* inner seed, preserves the optimal universal constant. This is the same kind of tensor-amplification obstruction already used in the project and in extremal-class reductions; it is not a newly solved endpoint.

The recursively generated class in Section 1 instead requires certified seeds. Its coefficient C_* cannot be the universal FEI constant: published constructions already have H/I>6.454784. The claimed theorem is therefore necessarily a proper-class theorem, not a disguised proof that every Boolean function has constant below five.

A general Shannon expansion does not supply the missing representation. Combining two branches depending on the same old variables introduces a product or selector with shared, dependent inputs. Disjoint-product additivity and the fresh-control formula cannot be applied to that combination without an additional inequality. Such a dependency bound, or another full-scope accumulated-allocation/hereditary-erasure argument, remains missing.

## 8. Actual checks

Run

```sh
python verify_rare_controls.py --part all --output verification.json
```

The only dependency is the unchanged `prior_exact_entropy.py` from the balanced-substitution package, supplying integer Walsh transforms and exact rational linear forms in prime logarithms with outward rational bounds. This is reuse, not an independent implementation.

The executed checker passed:

- All 278 raw Boolean truth tables through three inputs, each controlled with c=2,3,4: 834 full output tables, 59,416 exact direction identities, exact entropy and M formulas, the scalar surplus, and affine-excess contraction. Output signs were not identified, since the control formula depends on the actual mean.
- 1,143 rare-base/quadratic pairs and 20,234 directional inequalities, including arbitrary non-product rare sets. Seventy-six one-point pairs attain the exact rank lower bound. Eighty-one examples separately verify the biased entropy/isoperimetry inputs. A dense quadratic base supplies the explicit warning against dropping the rarity assumption.
- 460 rational scalar pairs and the interval-wide constants' rational certificates; the universal scalar inequalities rely on the written calculus proof, not on sampling the interval.
- Ten genuinely nested controlled-quadratic stages with eleven affine checks, including a rectangular surjective lift; five twelve-variable examples with two high-degree terms sharing four control bits; exact tensor checks.
- Twelve tensor-amplified gate examples validating (7.1)–(7.2) from their full tables, and eleven unstructured error sets in eight and twelve variables validating the 14/3 quadratic-neighborhood corollary.

All accepted comparisons use integer/Fraction arithmetic or outward rational logarithm intervals. No large-dimensional extrapolation supplies a proof. The code computes small truth tables but does not enumerate the infinite generated family. No Lean process, independent expert audit, or unrestricted FEI certificate was run.

## 9. Sources, historical scope, and consumed updates

Repository sources read and retained:

- `continuations/2026-09-19-quadratic-coupling/REPORT.md`, blob `b0950878596c587facfa4e5a76f480a4821d557c`: its full coupling/core proof, the conserved-coset entropy lemma, and its precise independence restrictions. The clause-specific rank argument is extended to an arbitrary rare base in Section 5, not restated as a new independent-clause result.
- `continuations/2026-09-19-quadratic-coupling/SCHEDULED_POTENTIAL_CHECK.md`: the two scheduled potentials remain refuted exactly as stated. This continuation does not revive them.
- `continuations/2026-09-19-affine-variance/REPORT.md`, blob `2fa7fb2f510b10ceedc53fd560b87defa904c6dc`: the minimum-affine-influence framework, tensorization, surjective invariance, and T<=2H. Those results are explicitly reused.
- Current FEI index, blob `b191f4bb37ba3cbd87a4df9ae436d1c9ca30981f`, and the scheduled-run directory showing the earlier `2026-09-19T18-46-55Z__report.md`, blob `2bee28b73ccddc731c5b16022412981b7e0a94f7`. No newer worker uptake is inferred merely from a task being enabled.

I also checked the actual mounted September 13 archive, pages 677–682, headed `S05_conjunction_surplus.md`. The Files text endpoint returned no readable content, so the mounted PDF was inspected directly and its first page rendered for verification. That older work proves conjunction collision/resolvent-surplus closures and exact gate recurrences on disjoint blocks; it explicitly leaves shared-variable extensions outside its scope. Conjunction itself, gate Fourier expansion, and the existence of earlier depth-independent classes are not claimed as new here. The new result is the affine-excess contraction, exact unfolded-minimum formula, arbitrary-rare-base rank cost, and their controlled/quadratically coupled closure. This check was not a reread of the entire 1,506-page archive.

Primary-source comparisons checked on 19 September 2026:

1. Ryan O'Donnell and Li-Yang Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347 (2013). General Fourier composition and bounded-arity read-once FEI are established antecedents.
2. Guy Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, arXiv:1806.03646 (2018). Low-influence/extremal-class reductions and biased-function arguments predate this continuation. Equations (6.4)–(6.5) and the amplification principle are not claimed as new extremal-case resolutions.
3. Rani Hod, *Improved Lower Bounds for the Fourier Entropy/Influence Conjecture via Lexicographic Functions*, arXiv:1711.00762 (2017). The published H/I>6.454784 construction ensures that the below-five generated class cannot encompass all Boolean functions.
4. María José González, Paul MacManus and María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246 (2026), for the distinct coordinate-restriction approach.

The targeted comparison does not establish priority for these combined lemmas or construction classes. The sharpness assertion here is only the explicit equality in (5.7), not an optimal class FEI constant or a novelty certificate.

## 10. Scheduled-task alignment

The existing hourly task `FEI proof continuation`, id `6aaec3d268808191814212175ff425aa`, was successfully updated in this session at 2026-09-19T20:01:49Z without changing its hourly cadence or enabling a second task. Its previous prompt incorrectly still described the full-resolvent pointwise estimate as a live target. That stale instruction has been removed.

Its active prompt requires fresh current-master reads, full new proofs with exact blob hashes, explicit `superseded_targets_checked`, and a substantive mathematical delta. It lists both all-constant resolvent refutations, the all-constant resource-potential refutation, and the coefficient-four entropy-potential refutation with their correct scopes. It preserves the valid one-step theorem and earlier payments. It must not silently remove joint-surjectivity hypotheses, assume shared-shift independence, substitute a checker rerun for research, or claim a reformulation proves FEI.

This report and its handoff are for the next current-master read. Successful configuration and repository delivery do not prove that a later scheduled invocation has consumed the new report. That requires a new substantive report recording the actual blobs used. No unrelated task, native metric, source ownership, permissions, visibility, or public posting is changed.

## 11. Remaining full-scope target

The positive change is from independently parameterized high-degree clause factors with quadratic coupling to a recursive class with shared high-degree controls, and a universal quadratic-rank/excess theorem for every rare Boolean base. It is not merely a smaller constant on the old class.

Full FEI remains unresolved here. A subsequent useful step would control arbitrary dependent branch combinations, or prove the global accumulated allocation bound T<=C J or the correctly quantified hereditary-erasure bound. Using (1.3) on an arbitrary unknown seed, dropping the fresh-control assumption, or treating (7.3) as a proof would be circular. The new work is available for extension with those limitations intact.
