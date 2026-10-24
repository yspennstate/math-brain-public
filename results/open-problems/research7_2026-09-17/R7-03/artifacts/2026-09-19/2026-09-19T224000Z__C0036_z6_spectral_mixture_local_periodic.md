# C0036 admission-stage mathematics: `Z/6Z` spectral mixture, scalar stability, and periodic-spectrum lifting

Date: 2026-09-19 UTC / 2026-09-20 local  
Worker: `R7-03 Boundary-Case Research`  
Canonical candidate: `C0036`  
Outside source: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Conjecture 5.7, §5.2, arXiv:1406.2707  
Methods: **B7 / B18 / B27**  
Status: **PARTIAL relative to the all-group source; no C0036 claim is created here.**

## 1. Recovered state and the exact order-six obstruction

Let `Gamma=Z/6Z`, let `Q` be a translation-equivariant positive contraction on `ell^2(Gamma)`, and let

\[
p=\operatorname{FK}(Q)=(\det Q)^{1/6}.
\]

Earlier R7-03 work proved:

1. all cardinality-threshold lower inequalities at density `FK(Q)` for every finite group;
2. the full sharp two-sided Lyons 5.7 statement for every finite group of order at most four;
3. the full sharp two-sided statement for `Z/5Z`;
4. on `Z/6Z`, the sharp lower inequality for the distance-two pair event by an index-two coset lift and for the distance-three antipodal-pair event by a three-variable Maclaurin excess chain.

Thus the first unresolved principal two-point orbit is the adjacent-pair event

\[
U_{\rm adj}=\{X\subseteq Z/6Z:X\text{ contains an edge of }C_6\}.
\]

Write

\[
D_{01}=\det Q_{\{0,1\}},\qquad
D_{012}=\det Q_{\{0,1,2\}},\qquad
D_{0134}=\det Q_{\{0,1,3,4\}},\qquad
D_5=\det Q_{\{0,1,2,3,4\}}.
\]

The previous run derived the exact inclusion--exclusion identity

\[
P^Q(U_{\rm adj})
=6D_{01}-6D_{012}-3D_{0134}+6D_5-2p^6,
\tag{1.1}
\]

so the remaining sharp lower inequality is

\[
6(D_{01}-p^2)-6(D_{012}-p^3)-3(D_{0134}-p^4)+6(D_5-p^5)\ge0.
\tag{1.2}
\]

This note does not claim (1.2) globally. It gives three new structural results around it.

## 2. B18: the adjacent event as an exact spectral-mixture inequality

Let `F` be the unitary `6 x 6` discrete Fourier matrix and let the Fourier eigenvalues of `Q` be

\[
\lambda_0,\ldots,\lambda_5\in[0,1].
\]

Thus

\[
Q=F\,\operatorname{diag}(\lambda_0,\ldots,\lambda_5)F^*.
\]

A standard finite-DPP spectral sampling representation says: independently include frequency `j` in a random set `J` with probability `lambda_j`; conditional on `J`, sample the projection DPP with kernel

\[
P_J=F_JF_J^*.
\]

Let

\[
I=U_{\rm adj}^c
=\{X:X\text{ is an independent set of }C_6\},
\]

and define

\[
f(J)=P^{P_J}(I).
\]

Then exactly

\[
P^Q(I)=\mathbb E_{\lambda} f(J).
\tag{2.1}
\]

If all six eigenvalues equal `p`, then `Q=pI`, so the DPP is iid Bernoulli(`p`). Therefore

\[
P_p(I)=\mathbb E_p f(J).
\tag{2.2}
\]

Consequently (1.2) is equivalent to the six-Bernoulli product inequality

\[
\boxed{\mathbb E_{\lambda}f(J)\le \mathbb E_p f(J),
\qquad p=(\lambda_0\cdots\lambda_5)^{1/6}.}
\tag{2.3}
\]

The point is that `f` is now completely explicit.

### Proposition 2.1 — exact table for `f`

For `J subset Z/6Z`:

- if `|J|=0` or `1`, then `f(J)=1`;
- if `|J|>=4`, then `f(J)=0`;
- if `|J|=2` and the cyclic distance between the two frequencies is `d=1,2,3`, then respectively

\[
f(J)=\frac56,\qquad \frac12,\qquad \frac13;
\tag{2.4}
\]

- if `|J|=3`, then

\[
f(J)=\begin{cases}
1/4,&J\text{ contains one representative of each residue class mod }3,\\
0,&\text{otherwise.}
\end{cases}
\tag{2.5}
\]

There are therefore six two-frequency sets with value `5/6`, six with value `1/2`, three with value `1/3`; and eight three-frequency sets with value `1/4`, twelve with value `0`.

#### Proof

A rank-`r` projection DPP has exactly `r` points. Thus `f=1` in ranks 0 and 1, while `f=0` for ranks at least four because the independence number of `C_6` is three.

For `|J|=2`, the projection DPP selects a coordinate pair `S` with probability

\[
|\det F_{S,J}|^2.
\]

All six adjacent coordinate pairs have the same weight. For `S={0,1}` and a spectral pair of cyclic distance `d`,

\[
|\det F_{S,J}|^2
=\frac1{36}|1-e^{\pi i d/3}|^2
=\begin{cases}
1/36,&d=1,\\
1/12,&d=2,\\
1/9,&d=3.
\end{cases}
\]

Hence the probability of selecting an adjacent pair is six times this number, which gives (2.4).

For `|J|=3`, the only independent coordinate triples are the two alternating triples `{0,2,4}` and `{1,3,5}`. The Fourier minor on an alternating coordinate triple is a `3 x 3` Fourier minor after identifying frequencies modulo three. It vanishes exactly when two frequencies have the same residue modulo three. Otherwise its squared determinant is `1/8`. The two alternating coordinate triples have the same weight, so `f=2(1/8)=1/4` in the residue-complete case and zero otherwise. ∎

### Corollary 2.2 — monotonicity of the projection statistic

The exact table implies

\[
J\subseteq J'\quad\Longrightarrow\quad f(J)\ge f(J').
\tag{2.6}
\]

This does **not** by itself prove (2.3): independent Bernoulli coordinates with fixed geometric mean need not be coordinatewise stochastically ordered by the equal-parameter product law. What it does is change the unresolved adjacent-pair problem from a DPP inequality into a finite explicit product-measure comparison for one decreasing set function.

## 3. B7: strict local positivity around the scalar spectrum

The most natural possible counterexample locus is a small symmetry-breaking perturbation of the scalar kernel. It is not available.

### Theorem 3.1 — scalar spectra are strict local minima of the adjacent gap

Fix `p in (0,1)`. Let

\[
\lambda_i(\varepsilon)=p e^{\varepsilon x_i},
\qquad \sum_{i=0}^5 x_i=0,
\tag{3.1}
\]

for sufficiently small `varepsilon`, so that every eigenvalue remains in `(0,1)`. The product, and hence `FK(Q)`, stays exactly equal to `p`.

Define the adjacent gap

\[
G(\lambda)=P^Q(U_{\rm adj})-P_p(U_{\rm adj}).
\]

Then

\[
G(\lambda(\varepsilon))
=\frac{\varepsilon^2}{2}\,x^TM_p x+O(\varepsilon^3),
\tag{3.2}
\]

where `M_p` is circulant. On the zero-sum subspace its Fourier-mode eigenvalues are

\[
\boxed{\mu_{1}=\mu_5=p^2(1-p)^2(1+p),}
\tag{3.3}
\]

\[
\boxed{\mu_{2}=\mu_4=p^2(1-p)(2-p^2),}
\tag{3.4}
\]

and

\[
\boxed{\mu_3=p^2(1-p)^2(p+2).}
\tag{3.5}
\]

All are strictly positive for `0<p<1`. Hence the scalar spectrum is a strict local minimum of the adjacent-event gap on the fixed-product manifold.

In particular, no sufficiently small nonconstant perturbation of `pI` can refute (1.2).

#### Proof

For any fixed coordinate set `S` of size `k`, Cauchy--Binet gives

\[
D_S(\lambda)
=\sum_{|T|=k}|\det F_{S,T}|^2\prod_{j\in T}\lambda_j.
\tag{3.6}
\]

Under (3.1),

\[
\prod_{j\in T}\lambda_j(\varepsilon)
=p^k\exp\left(\varepsilon\sum_{j\in T}x_j\right).
\]

The first derivative of `G` vanishes at `varepsilon=0` by cyclic symmetry together with `sum x_i=0`. The second derivative is therefore

\[
x^TM_px,
\]

where, if

\[
A_S=\sum_{|T|=|S|}|\det F_{S,T}|^2\,1_T1_T^T,
\]

then

\[
M_p=6p^2A_{01}-6p^3A_{012}-3p^4A_{0134}+6p^5A_{01234}.
\tag{3.7}
\]

Each summand is circulant after the orbit coefficient from (1.1) is included, hence so is `M_p`. Direct exact evaluation of the Fourier minors gives the first row

\[
\begin{aligned}
r_0&=p^2(5p^3-2p^2-3p+2),\\
r_1&=\frac{p^2}{6}(24p^3-8p^2-5p+1),\\
r_2&=\frac{p^2}{2}(8p^3-2p^2-3p+1),\\
r_3&=\frac{2p^2}{3}(6p^3-2p^2-2p+1),\\
r_4&=r_2,\qquad r_5=r_1.
\end{aligned}
\tag{3.8}
\]

For the real symmetric circulant matrix, mode `m` has eigenvalue

\[
r_0+2r_1\cos(\pi m/3)+2r_2\cos(2\pi m/3)+r_3\cos(\pi m).
\tag{3.9}
\]

Substitution and factorization yield exactly (3.3)--(3.5). The modes `1,...,5` span the zero-sum subspace, so `M_p` is positive definite there. Taylor's theorem, uniformly on the unit sphere of that five-dimensional subspace, gives strict positivity of `G` for every sufficiently small nonzero fixed-product perturbation. ∎

The boundary values cause no hidden local counterexample: at `p=0` the lower Bernoulli comparator has no occupied point, while `p=1` forces every `lambda_i=1`.

## 4. B27: a periodic-spectrum product lifting theorem

The order-six source also has exact nontrivial families on which the **full two-sided** conjecture follows from smaller groups.

### Theorem 4.1 — periodic Fourier spectrum decomposes into independent smaller cyclic DPPs

Let `d|n` and let `Q` be a `Z/nZ`-equivariant positive contraction with Fourier eigenvalues satisfying

\[
\lambda_{j+d}=\lambda_j
\quad (j\bmod n).
\tag{4.1}
\]

Then, after partitioning coordinates by their residue class modulo `n/d`, `Q` is a direct sum of `n/d` identical `d x d` circulant kernels `K` whose Fourier eigenvalues are `lambda_0,...,lambda_{d-1}`. Consequently

\[
P^Q=(P^K)^{\otimes n/d}.
\tag{4.2}
\]

Moreover

\[
\operatorname{FK}(Q)=\operatorname{FK}(K)
=\left(\prod_{a=0}^{d-1}\lambda_a\right)^{1/d},
\tag{4.3}
\]

and likewise

\[
\operatorname{FK}(I-Q)=\operatorname{FK}(I-K).
\tag{4.4}
\]

Therefore, whenever the full sharp two-sided Lyons 5.7 statement holds for `K` on `Z/dZ`, it holds for `Q` on `Z/nZ`.

#### Proof

Let `zeta=e^{2pi i/n}` and write `r=x-y`. Using (4.1),

\[
\begin{aligned}
Q(x,y)
&=\frac1n\sum_{j=0}^{n-1}\lambda_j\zeta^{jr}\\
&=\frac1n\sum_{a=0}^{d-1}\lambda_a\zeta^{ar}
\sum_{\ell=0}^{n/d-1}(\zeta^{dr})^\ell.
\end{aligned}
\]

The inner geometric sum is zero unless `n/d` divides `r`. Hence there are no matrix entries between different coordinate residue classes modulo `n/d`. Inside one class, write `x=c+(n/d)u`, `y=c+(n/d)v`. Then

\[
Q(x,y)=\frac1d\sum_{a=0}^{d-1}\lambda_a e^{2\pi i a(u-v)/d},
\]

which is precisely the `Z/dZ` circulant kernel `K`. This proves the direct-sum statement and hence the product decomposition of the DPP.

The determinant of `Q` is the product of each eigenvalue repeated `n/d` times, giving (4.3); the same calculation applies to `I-Q`.

Finally, a monotone coupling witnessing either stochastic domination for `P^K` can be taken independently on each block. The product of those couplings witnesses the corresponding domination for (4.2). This proves both sides. ∎

### Corollary 4.2 — full sharp families on `Z/6Z`

The cumulative R7-03 work already proves the full sharp two-sided theorem on groups of orders one, two and three. Therefore Conjecture 5.7 holds completely on `Z/6Z` for every spectrum of any of the forms

\[
(a,a,a,a,a,a),
\tag{4.5}
\]

\[
(a,b,a,b,a,b),
\tag{4.6}
\]

or

\[
(a,b,c,a,b,c),
\tag{4.7}
\]

with arbitrary entries in `[0,1]`. These are not merely adjacent-event results: they give the source's full two-sided stochastic domination for all increasing events on these spectral families.

## 5. What moved and what did not

The formal R7-03 target metric remains uninstantiated because no successor has been admitted:

\[
\boxed{\texttt{UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED}.}
\]

The previous auxiliary pair-orbit coverage statistic also remains

\[
\boxed{2/3\to2/3},
\]

because the arbitrary-spectrum adjacent-pair event is still not proved. The progress in this note is structural rather than a manufactured metric movement:

- exact spectral-mixture reduction of the remaining adjacent event;
- strict local positivity at every scalar spectrum with `0<p<1`;
- full sharp two-sided closure of all period-1, period-2 and period-3 Fourier spectra on `Z/6Z`.

The simplest unresolved case is therefore an aperiodic six-tuple of Fourier eigenvalues bounded away from the scalar locus. Any counterexample to the adjacent event must live there.

## 6. Failure / next obstruction

The decreasing statistic `f(J)` in §2 tempts one to smooth the six Bernoulli parameters toward equal geometric mean. The local Hessian theorem proves that such equalization is favorable infinitesimally at the scalar point, and Theorem 4.1 proves several exact low-dimensional equality-compatible strata. What is missing is a **global** monotone operation on an arbitrary six-tuple `lambda` that preserves `prod lambda_i` and never decreases the adjacent gap.

No such global smoothing statement is proved here, and no numerical observation is promoted to a theorem.

A useful next attack is to seek either:

1. a two-coordinate multiplicative smoothing inequality directly for the explicit table `f(J)`; or
2. a certificate that every interior minimizer of the gap is periodic or scalar, which would combine with Theorem 4.1 and Theorem 3.1.

## 7. Exact finite self-check

After the mathematics was derived, the companion exact SymPy script checks:

- all Fourier-minor weight sets used above;
- the complete `f(J)` table and its multiplicities;
- monotonicity of `f` under set inclusion;
- the exact Fourier-mode factorization (3.3)--(3.5).

Its output ends `ALL_EXACT_CHECKS_PASS`. This is owner-track self-validation, not an independent P26/OTHER audit and not a proof of the unrestricted all-group source.
