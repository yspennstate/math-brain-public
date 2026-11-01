SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-24T07:07:55Z.
attacking: exact same-constant reduction of the central L-infinity theorem to smooth compact cap-one product laws, with continuity proved only on the smooth core and partner majority-sheet stability applied to a concrete inequality.

# Smooth-core equivalence for the height problem, and fixed-instance C0 on the core

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.

Status: `QFORM-SMOOTH-CORE-SAME-CONSTANT-v1 PROVED / QFORM-SMOOTH-CORE-C0-v1 PROVED / FULL QFORM OPEN / FULL ROUGH CONTINUITY OPEN`.

Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Statement and exact scope

Let

\[
Q_A(X)=X^TAX,
\]

where `A` is real symmetric and `X_1,...,X_n` are independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1` almost everywhere. In the owner target, `A` has at least three eigenvalues of modulus at least one.

Define the optimal height constants

\[
C_{\rm all}:=\sup \|p_{Q_A}\|_\infty,
\]

where the supremum is over every owner-target instance, and

\[
C_{\rm sm}:=\sup \|p_{Q_A}\|_\infty,
\]

where the same supremum is restricted to marginals

\[
f_i\in C_c^\infty(\mathbb R),\qquad 0\le f_i\le1,\qquad \int f_i=1.
\]

The first new theorem is

\[
\boxed{C_{\rm all}=C_{\rm sm}.}
\tag{1.1}
\]

Thus the **central universal L-infinity conjecture is exactly equivalent, with no constant loss, to its smooth compact cap-one subproblem.** Roughness of the one-dimensional marginals is not itself an obstruction to the universal height estimate.

The second new theorem is qualitative and deliberately separate:

> For every fixed target instance with all marginals in `C_c^infinity`, the output density belongs to `C_0(R)`.

The proof gives an instance-dependent Fourier-integrability constant and makes no universal regularity claim. It does not use independence after spectral rotation.

Finally, for arbitrary rough absolutely continuous inputs and every nonzero symmetric `A`, the output `X^TAX` is absolutely continuous. This is qualitative only and contains no universal height information.

The full unrestricted QFORM height theorem remains OPEN because (1.1) does not supply a universal bound on `C_sm`. Full rough-input continuity also remains a separate open conclusion in the programme.

## 2. Qualitative absolute continuity for every nonzero quadratic form

### Proposition 2.1 — `QFORM-NONZERO-AC-v1`

Let `X` have any absolutely continuous joint law on `R^n`; no product structure or density cap is needed here. If `A` is real symmetric and `A!=0`, then

\[
Q_A(X)=X^TAX
\]

has an absolutely continuous law on `R`.

### Proof

Set

\[
q(x)=x^TAx,
\qquad
\nabla q(x)=2Ax.
\]

The critical set is

\[
Z:=\{x:\nabla q(x)=0\}=\ker A.
\]

Since `A!=0`, `ker A` is a proper linear subspace and therefore has `n`-dimensional Lebesgue measure zero.

Let `N subset R` be Lebesgue null. Apply the coarea formula locally on balls and then let the radius tend to infinity:

\[
\int_{q^{-1}(N)} |\nabla q(x)|\,dx
=
\int_N \mathcal H^{n-1}(q^{-1}(t))\,dt
=0.
\tag{2.1}
\]

On `q^{-1}(N)\setminus Z`, the nonnegative function `|nabla q|` is strictly positive. Therefore (2.1) implies

\[
|q^{-1}(N)\setminus Z|=0.
\]

Since `|Z|=0`, also `|q^{-1}(N)|=0`. Any absolutely continuous input law assigns probability zero to this preimage. Hence

\[
\Pr\{Q_A(X)\in N\}=0,
\]

which is exactly absolute continuity of the pushforward law.

Under the owner hypothesis `s_3(A)>=1`, in particular `A!=0`, so every admissible product input has an output density before any quantitative work begins. No false arbitrary-joint **bounded coarea density** statement is being used: the argument proves only null-set preservation.

## 3. Cap-preserving smooth compact approximation in one dimension

### Lemma 3.1

Let `f` be a probability density on `R` with `0<=f<=1`. For every `epsilon>0` there exists

\[
g\in C_c^\infty(\mathbb R),\qquad 0\le g\le1,\qquad \int g=1,
\]

such that

\[
\|f-g\|_1<\epsilon.
\tag{3.1}
\]

### Proof

Choose `R` so large that

\[
a:=\int_{|x|>R}f(x)\,dx<\epsilon/4.
\]

Put

\[
f_R=f\,1_{[-R,R]}.
\]

Let `phi_eta` be a nonnegative compactly supported `C^infinity` approximate identity of mass one. Since convolution with a probability kernel preserves the cap,

\[
0\le h:=f_R*\phi_\eta\le1,
\qquad
\int h=1-a.
\]

For sufficiently small `eta`,

\[
\|h-f_R\|_1<\epsilon/2.
\]

Choose a nonnegative `psi in C_c^infinity` of mass one. After a sufficiently wide dilation and a translation far outside `supp(h)`, construct a smooth bump `b` satisfying

\[
\int b=a,
\qquad
0\le b\le1,
\qquad
\operatorname{supp}b\cap\operatorname{supp}h=\varnothing.
\]

Then `g=h+b` is smooth, compactly supported, a probability density, and still obeys `g<=1`. Moreover

\[
\|f-g\|_1
\le
\|f-f_R\|_1+\|f_R-h\|_1+\|b\|_1
<2a+\epsilon/2<\epsilon.
\]

This proves the lemma.

## 4. Product and deterministic-pushforward stability

For product densities

\[
F(x)=\prod_{j=1}^n f_j(x_j),
\qquad
G(x)=\prod_{j=1}^n g_j(x_j),
\]

the standard telescoping identity gives

\[
F-G
=\sum_{j=1}^n
(f_j-g_j)
\prod_{i<j}f_i
\prod_{i>j}g_i.
\]

Integrating absolute values and using that every other marginal has mass one,

\[
\boxed{
\|F-G\|_1\le\sum_{j=1}^n\|f_j-g_j\|_1.
}
\tag{4.1}
\]

If `T:R^n->R` is any measurable deterministic map and `mu=T_#(Fdx)`, `nu=T_#(Gdx)`, then for every Borel set `E`,

\[
|\mu(E)-\nu(E)|
\le \int |F-G|
=\|F-G\|_1.
\tag{4.2}
\]

In particular this holds for `T=q_A`. No regularity of `T` and no output continuity are needed.

## 5. Main theorem: exact smooth-core reduction for the universal height

### Theorem 5.1 — `QFORM-SMOOTH-CORE-SAME-CONSTANT-v1`

Suppose there is a constant `C<infinity` such that for **every** owner-target matrix `A` and every collection of smooth compact cap-one probability marginals,

\[
\|p_{Q_A}\|_\infty\le C.
\tag{5.1}
\]

Then the identical inequality holds for **every arbitrary measurable cap-one probability marginal**. Consequently

\[
C_{\rm all}=C_{\rm sm}.
\]

### Proof

Fix an arbitrary target instance `(A,f_1,...,f_n)`. By Lemma 3.1 choose, for each integer `k`, smooth compact cap-one probability densities `g_{j,k}` such that

\[
\sum_{j=1}^n\|f_j-g_{j,k}\|_1\longrightarrow0.
\tag{5.2}
\]

Let `mu_k` and `mu` be the output laws of the smoothed and original product inputs. By (4.1)-(4.2),

\[
\sup_E|\mu_k(E)-\mu(E)|\to0.
\tag{5.3}
\]

For every bounded interval `I`, the hypothesis (5.1) gives

\[
\mu_k(I)\le C|I|.
\]

Passing to the limit through (5.3),

\[
\boxed{\mu(I)\le C|I|\quad\text{for every bounded interval }I.}
\tag{5.4}
\]

By Proposition 2.1 the law `mu` has a density `p`. Lebesgue differentiation applied to (5.4) yields

\[
p(t)\le C
\quad\text{for almost every }t,
\]

so

\[
\|p\|_\infty\le C.
\]

Therefore `C_all<=C_sm`; the opposite inequality is immediate because the smooth class is a subclass of the full class. This proves (1.1).

### Consequence

A proof of the central owner theorem may, with **no change in the best universal constant**, impose

\[
f_i\in C_c^\infty,\quad 0\le f_i\le1
\]

from the start. The hard step is still a dimension- and matrix-uniform height estimate; the rough-source passage is free once the smooth estimate is known.

This reduction does not justify any pointwise quadratic Fourier decay. Smooth densities may still depend on the frequency in a counterexample family, and the universal pointwise decay correction remains in force.

## 6. Smooth core automatically has a C0 output for every fixed rank-at-least-three matrix

### Theorem 6.1 — `QFORM-SMOOTH-CORE-C0-v1`

Let `F in C_c^infinity(R^n)` be any joint probability density, not necessarily a product after changing coordinates. Let `A` be real symmetric of rank `r>=3`. Then the pushforward of `F(x)dx` by `x^TAx` has a density in

\[
C_0(\mathbb R).
\]

For the owner target this applies to every smooth-core product instance because `s_3(A)>=1` implies `rank(A)>=3`.

### Proof

Choose an orthogonal matrix `U` so that

\[
U^TAU=\operatorname{diag}(\lambda_1,\dots,\lambda_r,0,\dots,0),
\qquad \lambda_j\ne0.
\]

This rotation is used only to analyze one fixed smooth joint amplitude. **No independence of the rotated coordinates is asserted or needed.**

Writing `x=U(y,z)` with `y in R^r`, define the active-coordinate marginal

\[
\rho(y)=\int_{\mathbb R^{n-r}}F(U(y,z))\,dz.
\]

Because `F` is smooth and compactly supported,

\[
\rho\in C_c^\infty(\mathbb R^r)\subset\mathcal S(\mathbb R^r).
\]

The output characteristic function is

\[
\Phi(t)=\int_{\mathbb R^r}
\exp\!\left(it\sum_{j=1}^r\lambda_j y_j^2\right)
\rho(y)\,dy.
\tag{6.1}
\]

Use the Fourier convention

\[
\widehat\rho(\xi)=\int e^{-i\xi\cdot y}\rho(y)\,dy,
\qquad
\rho(y)=(2\pi)^{-r}\int e^{i\xi\cdot y}\widehat\rho(\xi)\,d\xi.
\]

The standard regularized Fresnel identity gives, for `t!=0`,

\[
\left|
\int_{\mathbb R^r}
 e^{it y^T\Lambda y+i\xi\cdot y}\,dy
\right|
=
\pi^{r/2}|t|^{-r/2}|\det\Lambda|^{-1/2},
\tag{6.2}
\]

where `Lambda=diag(lambda_1,...,lambda_r)`. Pairing this tempered-distribution identity with the Schwartz function `widehat rho`, or equivalently inserting a Gaussian damping factor and passing to the limit, yields

\[
|\Phi(t)|
\le
(2\pi)^{-r}\pi^{r/2}|\det\Lambda|^{-1/2}
\|\widehat\rho\|_1 |t|^{-r/2}.
\tag{6.3}
\]

Also `|Phi(t)|<=1`. Since `r>=3`,

\[
\int_{|t|\ge1}|t|^{-r/2}\,dt<\infty,
\]

so

\[
\Phi\in L^1(\mathbb R).
\]

Fourier inversion therefore supplies the canonical density

\[
p(s)=\frac1{2\pi}\int_{\mathbb R}e^{-its}\Phi(t)\,dt,
\]

and the Riemann-Lebesgue theorem gives

\[
\boxed{p\in C_0(\mathbb R).}
\]

The coefficient in (6.3) depends on the fixed matrix and on `rho` through `||widehat rho||_1`; it is not a universal QFORM height estimate.

## 7. Exact separation of the two owner conclusions

Theorems 5.1 and 6.1 give the following logical picture.

1. **Absolute continuity:** automatic already for every `A!=0` and every absolutely continuous joint input law (Proposition 2.1).
2. **Universal essential height:** the hard central theorem, but it is exactly enough to prove it on the smooth compact cap-one product core (Theorem 5.1).
3. **Continuity on the smooth core:** automatic for each fixed target matrix because rank at least three gives an integrable fixed-instance characteristic function (Theorem 6.1).
4. **Continuity for arbitrary rough cap-one inputs:** not obtained merely by Theorem 5.1. The approximation in Theorem 5.1 transfers interval domination / essential height through total variation, but a common `L^infinity` bound plus `L1` convergence does not by itself force uniform convergence of density representatives. An additional stability or smoothing mechanism is needed.

Thus continuity should remain downstream and separate from the central `L^infinity` estimate, exactly as required by the assignment.

## 8. Completed designated-partner result applied to an actual inequality

The newest designated partner `fleet02/B15` completed the majority-sheet stability theorem for

\[
q_R(X)=\langle r_1,X\rangle^2+\langle r_2,X\rangle^2-\langle r_3,X\rangle^2,
\qquad R^TR=I_3.
\]

For two cap-one product input families `f=(f_j)` and `g=(g_j)`, its canonical positive-sheet densities obey

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le40\sum_j\sqrt{\|f_j-g_j\|_1}.
}
\tag{8.1}
\]

Separately, its source-pinned ruled theorem pays the height

\[
\boxed{
0\le r_f^+(s)\le\pi\sqrt2,
\qquad s\ge0,
}
\tag{8.2}
\]

and the partner then constructs `r_f^+ in C_0([0,infinity))` for arbitrary rough cap-one inputs. The height (8.2) is established before continuity.

Apply this to the literal exact-target form

\[
q(x,y,z)=x^2+y^2-z^2,
\]

whose matrix has eigenvalues `1,1,-1`. Let

\[
f_1=f_2=f_3=\mathbf1_{[-1/2,1/2]}.
\]

By Lemma 3.1 choose smooth compact cap-one probability densities `g_j` with

\[
\|f_j-g_j\|_1\le10^{-8}
\qquad(j=1,2,3).
\]

Then (8.1) gives the concrete inequality

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le40\cdot3\cdot10^{-4}
=0.012.
}
\tag{8.3}
\]

At the same time (8.2) gives

\[
\boxed{
\Pr\{q(X)\in I,\ q(X)\ge0\}
\le\pi\sqrt2\,|I|,
\qquad
\pi\sqrt2=4.442882938\ldots .
}
\tag{8.4}
\]

This is an actual completed-partner theorem used at an explicit inequality. It also illustrates precisely why the partner's square-root submass stability is stronger than the generic smooth-core reduction: (8.3) gives **uniform density convergence**, hence transports `C_0` regularity on the majority half-line, whereas Theorem 5.1 alone transports only the height.

No post-rotation independence is used in this application. The partner theorem itself is orientation-uniform and product-preserving in the original coordinates; the displayed example merely chooses `R=I_3` to make the numerical application transparent.

## 9. Why this does not solve the full conjecture

Theorem 5.1 reduces the full height problem to smooth compact cap-one product laws with the same optimal constant, but it leaves the principal analytic/geometric difficulty unchanged:

\[
\sup_{\substack{s_3(A)\ge1\\ f_i\in C_c^\infty,\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty
\stackrel{?}{<}\infty.
\]

The smooth fixed-instance Fourier estimate (6.3) has a coefficient depending on `A` and on derivatives/geometry of the rotated joint amplitude, so it cannot be promoted to a law- and matrix-uniform estimate. In particular, it does not resurrect the refuted law-uniform pointwise quadratic Fourier decay.

The remaining full-target obstruction is therefore genuinely the **uniform smooth-core height estimate in coupled/diffuse original-coordinate geometry**, not rough-source approximation or qualitative output regularity. The designated partner additionally shows that on one ruled majority sheet, a stronger submass mechanism does transport continuity. The complementary two-sheet/convex contribution and the arbitrary coupled matrix remain unpaid.

## 10. Dependencies and corrections consumed

- Fresh owner control and programme revision `2026-09-22.15 / 2026-09-22.5`; full QFORM still OPEN.
- Live corrections retained: no uniform pointwise quadratic Fourier decay; no independence after rotation; no projection-only/X-ray shortcut; arbitrary-joint rank-three bounded coarea claim false; conditional projected-density positive-moment gate false.
- Designated partner actually applied: `fleet02/B15`, canonical run `20260924T063601Z-fleet02-B15-QFORM-auto11-r1`, math commit `c139eb3d840570fdee57c2f4786801ea0afa271b`, with rigor addendum `8b81ce7a92535ef66f276f03d54bb11f531d0928`.

No numerical simulation, moment assumption, centered-input assumption, connected-support assumption, or rotated-product assumption enters the new theorems.
