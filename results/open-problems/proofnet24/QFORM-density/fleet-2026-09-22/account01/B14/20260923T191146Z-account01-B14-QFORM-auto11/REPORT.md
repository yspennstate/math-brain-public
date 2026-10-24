# account01/B14 — whole-law smooth localization and the Gaussian-component barrier

Run: `20260923T191146Z-account01-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`  
Status: **NEW ZERO-LOSS LOCALIZATION THEOREM + SMOOTH-CLASS GAUSSIAN BARRIER + STRICT TARGET APPLICATION. FULL QFORM OPEN.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source pins

The full conjecture remains open: for independent real coordinates with densities at most one and symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `X^T A X`, or produce a valid counterexample.

Fresh control was resolved before this run at `yspennstate/math-research-brain@6860364d5ff95a7f28120482fb6ac6044ad2b189`; immediately before the main mathematical write it had advanced, by ordinary fleet handoffs rather than a later owner stop, to `fb50f1793e7ff245df2dffbd1857f88dcae884df`. The active owner continuation remains `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and the unrestricted rough-law endpoint remains OPEN.

Fresh mathematical master before work was `yspennstate/math-open-problems@810eb1d6e50d68ab2ee70591edb690051823c163`.

The designated partner result actually used is account02/B14 run

`20260923T183045Z-account02-B14-QFORM-auto11`,

committed at `yspennstate/math-open-problems@a0ba2bed1c4d0e364c42e7c99103ad7c57d5ac19`, path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T183045Z-account02-B14-QFORM-auto11/REPORT.md`.

Its two inputs used here are:

1. if `g(x)=E phi_T(x-M)` is a Gaussian location-scale mixture and `H=E T^{-1/2}`, then

   `Var(g) <= sqrt(2/pi) H`;

2. for

   `E_N = union_{j=1}^N [4j,4j+1/N]`, `f_N=1_{E_N}`,

   every such Gaussian mixture satisfies, with `delta=||g-f_N||_1`,

   `H >= N sqrt(2 pi) (1-delta)`.                                      (1.1)

   Hence if `H<=sqrt(2 pi)`, then

   `||g-f_N||_1 >= 1-1/N`.                                             (1.2)

The same partner report also constructs the smooth cap-one random-center Gaussian mixture

`X_N=M_N+(1/(2N))G`, `M_N` uniform on `{4,8,...,4N}`,

whose density is `<0.799<1` while `E T^{-1/2}=2N`.

I do not use pointwise quadratic Fourier decay, post-rotation independence, arbitrary-joint coarea, positive conditional-density moment bounds, bounded-diameter localization, or any fixed fragment-count reduction.

---

## 2. Main localization theorem: smooth compact laws are exactly enough

The previous extreme-law localization shows that one may keep arbitrary finite unions whole. The present theorem changes mechanism: it shows that **nonsmoothness and unbounded support can be removed altogether with zero loss in the optimal density constant**, without decomposing the law into normalized fragments.

For a finite Borel measure `mu` on `R`, define its interval-density seminorm

`D(mu)=sup_{a<b} mu((a,b))/(b-a)`.

If `D(mu)<infinity`, then `mu<=D(mu) dx`, hence `mu` has a density bounded by `D(mu)`. Conversely, if `mu` has density bounded by `C`, then `D(mu)<=C`.

### Theorem 2.1 (`QFORM-WHOLE-LAW-SMOOTH-LOCALIZATION-v1`)

Let `F:R^n->R` be any Borel map. Let

`C_all(F)=sup D(F_#(prod_i f_i(x_i)dx_i))`,

where the supremum is over all probability densities `0<=f_i<=1`. Let `C_sm(F)` be the same supremum restricted to densities

`f_i in C_c^infinity(R)`, `0<=f_i<=1`, `int f_i=1`.

Then

`boxed{ C_all(F)=C_sm(F) }`                                             (2.1)

including the value `+infinity`.

The equality is exact: no support radius, diameter, moment, translation, fragment count, or separation parameter appears.

Consequently, for every fixed symmetric `A` and every affine pair `(b,c)`, the optimal bound for

`F(x)=x^T A x+b^T x+c`

is unchanged by restricting all marginals to smooth compactly supported cap-one densities. Taking the supremum over all `A` with `s_3(A)>=1` gives

`boxed{ C_QFORM(all cap-one laws)=C_QFORM(C_c^infinity cap-one laws). }` (2.2)

Thus proving the full conjecture with one constant `C` for the smooth compact cap-one class would prove it for the original arbitrary-law class with **the same `C`**.

### Proof

Only the nontrivial inequality `C_all(F)<=C_sm(F)` needs proof.

#### Step 1: compactify a single marginal without renormalization

Let `f` be any probability density with `0<=f<=1`. For `R>0`, put

`delta_R=int_{|x|>R} f(x) dx`.

Choose any bounded interval `I_R` contained in the complement of `[-R,R]` and of length exactly `delta_R`, and define

`h_R(x)=f(x)1_{[-R,R]}(x)+1_{I_R}(x)`.

Then `0<=h_R<=1`, `int h_R=1`, and `h_R` is compactly supported. Moreover

`||h_R-f||_1 <= int_{|x|>R} f + |I_R| =2 delta_R ->0`.                 (2.3)

No centering or moment assumption was used. The filler interval can be placed arbitrarily far away; its location never enters the estimate.

#### Step 2: smooth while preserving the density cap exactly

Fix a nonnegative standard mollifier `eta in C_c^infinity`, `int eta=1`, and let

`eta_eps(x)=eps^{-1} eta(x/eps)`.

Set

`h_{R,eps}=h_R * eta_eps`.

Then

- `h_{R,eps} in C_c^infinity`;
- `int h_{R,eps}=1`;
- `0<=h_{R,eps}<=||h_R||_infinity ||eta_eps||_1<=1`;
- `||h_{R,eps}-h_R||_1 ->0` as `eps->0`.

Combining with (2.3), every arbitrary cap-one probability density is an `L^1` limit of compactly supported smooth probability densities obeying the **same cap one**.

This is a whole-law smoothing operation. It never labels, normalizes or pays individual remote components.

#### Step 3: tensor approximation has no dimensional constant for fixed `n`

Choose approximants `g_i^{(k)}` for each `f_i`. For probability densities,

`|| prod_i f_i - prod_i g_i^{(k)} ||_1
 <= sum_i ||f_i-g_i^{(k)}||_1`.                                      (2.4)

This follows by the usual telescoping expansion; all untouched factors have `L^1` norm one. Hence the product source measures converge in total variation.

#### Step 4: pushforward and the density seminorm

Pushforward by any Borel map contracts total variation, so if

`mu_k=F_#(prod_i g_i^{(k)}dx_i)`, `mu=F_#(prod_i f_i dx_i)`,

then `||mu_k-mu||_TV ->0`.

For every finite interval `J`, therefore `mu_k(J)->mu(J)`. If `D(mu_k)<=C` for all `k`, then

`mu(J)<=C |J|`

for every interval `J`; hence `mu<=C dx` and `D(mu)<=C`. Equivalently,

`D(mu)<=liminf_k D(mu_k)`.                                            (2.5)

By definition `D(mu_k)<=C_sm(F)`, so (2.5) yields `D(mu)<=C_sm(F)`. Taking the supremum over the original arbitrary product law proves (2.1). The reverse inequality is immediate because the smooth compact class is a subclass. `square`

### Remarks on the exact scope

1. The theorem is stronger than a QFORM-specific approximation: it is valid for every Borel output map `F` because only total-variation contraction is used.
2. The compact support radii of the approximants may diverge. Thus a theorem whose constant depends on support diameter or moments does **not** automatically transfer. The theorem transfers exactly a uniform constant.
3. The construction is translation-equivariant up to the arbitrary compactification window. A common or fragment-dependent translation changes no constant.
4. No fixed component count is asserted. This is compatible with the live correction that bounded-diameter and fixed-fragment-count localization are false.

---

## 3. A sharper consequence of the partner result: even smooth compact laws stay far from the admissible Gaussian-mixture class

Theorem 2.1 removes roughness. One might hope that the remaining smooth compact class can then be uniformly approximated by the Gaussian-mixture input class covered by the new arbitrary-matrix Gaussian theorem. Partner account02/B14 proves this cannot be done for the rough `f_N`. The next lemma upgrades its obstruction to the **smooth compact class itself**.

### Proposition 3.1 (`QFORM-SMOOTH-CAPONE-GAUSSIAN-BUDGET-SEPARATION-v1`)

There exist `h_N in C_c^infinity(R)`, `0<=h_N<=1`, `int h_N=1`, such that every Gaussian location-scale mixture

`g(x)=E phi_T(x-M)`

with

`E T^{-1/2} <= sqrt(2 pi)`

satisfies

`boxed{ ||g-h_N||_1 >= 1-2/N. }`                                     (3.1)

Thus the inverse-half-scale Gaussian-mixture class used in the completed arbitrary-matrix Gaussian theorem is **not TV-dense even in the smooth compact cap-one class** that is exactly sufficient for full QFORM by Theorem 2.1.

### Proof

Use the partner's

`f_N=1_{E_N}`, `E_N=union_{j=1}^N[4j,4j+1/N]`.

Its one-dimensional total variation is `Var(f_N)=2N`.

For the standard compactly supported mollifier `eta`, let

`m_1=int |u| eta(u) du`.

The standard BV translation inequality gives

`||tau_y f_N-f_N||_1 <= |y| Var(f_N)=2N|y|`.

Hence

`||f_N*eta_eps-f_N||_1
 <= int eta_eps(y)||tau_y f_N-f_N||_1 dy
 <= 2N eps m_1`.                                                     (3.2)

Choose

`eps_N <= 1/(2 m_1 N^2)`

and set

`h_N=f_N*eta_{eps_N}`.

Then `h_N` is smooth, compactly supported, has mass one and satisfies `0<=h_N<=1`, while (3.2) gives

`||h_N-f_N||_1<=1/N`.                                                 (3.3)

Partner inequality (1.2) says every Gaussian mixture with inverse-half-scale budget at most `sqrt(2 pi)` satisfies

`||g-f_N||_1>=1-1/N`.

The triangle inequality and (3.3) therefore give

`||g-h_N||_1 >= ||g-f_N||_1-||h_N-f_N||_1 >=1-2/N`,

which is (3.1). `square`

### Interpretation

This isolates the missing endpoint very cleanly:

- **regularity is not the obstruction:** arbitrary cap-one laws reduce exactly to smooth compact cap-one laws;
- **support boundedness is not the obstruction:** the reduction is compact;
- **the obstruction is the component certificate:** paying `E T^{-1/2}` before random centers/fragments are aggregated is stronger than controlling the final marginal density.

A successful extension of the Gaussian proof to all cap-one inputs must therefore replace componentwise inverse-scale payment by a whole-marginal quantity, or aggregate centers before the reciprocal scale appears.

---

## 4. Strict target application: an indefinite off-diagonal family where component-first Gaussian inversion loses `N^2` but the actual density is at most `4`

This section applies the completed partner construction to an actual full-target density inequality, not merely to an approximation metric.

Take the partner's smooth random-center Gaussian variable

`X_N=M_N+sigma_N G`,

where `M_N` is uniform on `{4,8,...,4N}` and

`sigma_N=1/(2N)`, `T_N=sigma_N^2=1/(4N^2)`.

Partner account02/B14 proves its final density is `<0.799<1` for every `N`, while its Gaussian component budget is

`E T_N^{-1/2}=2N`.                                                    (4.1)

Let `X_{N,1},...,X_{N,4}` be independent copies and define

`Q_N=2 X_{N,1}X_{N,2}+2 X_{N,3}X_{N,4}`.                             (4.2)

Its coefficient matrix is

`A = [[0,1],[1,0]] direct_sum [[0,1],[1,0]]`,

with spectrum `{1,-1,1,-1}`. Hence (4.2) is a strict instance of the owner's full three-large-eigenvalue target, and it is indefinite and genuinely off-diagonal in the original independent coordinates.

### 4.1 Whole-law physical-space bound

For arbitrary independent cap-one variables `U,V` and arbitrary shifts `a,b`, the translated hyperbolic product satisfies

`||p_{2(U-a)(V-b)}||_2 <=2`.                                         (4.3)

Indeed, condition on `V-b=v`. The scaled `U-a` density has `L^2` norm at most `(2|v|)^(-1/2)`, since `||f_U||_2<=1`. Minkowski gives

`||p||_2 <= 2^{-1/2} E|V-b|^{-1/2}`.

The cap-one bathtub bound is

`E|V-b|^{-1/2} <= int_{-1/2}^{1/2}|x|^{-1/2}dx=2 sqrt2`,

which proves (4.3).

The two terms in (4.2) are independent. Young/Cauchy-Schwarz therefore yields

`boxed{ ||p_{Q_N}||_infinity <= 2*2=4 }`                              (4.4)

for every `N`.

The same bound remains true if arbitrary independent outside original coordinates are added with arbitrary quadratic coefficients and arbitrary cross-couplings to the four active coordinates: condition on the outside block, complete each active hyperbolic pair to translated products, use (4.3) pointwise, and average. The active `4x4` principal block already has two eigenvalues `>=1` and two `<=-1`; interlacing keeps the ambient matrix inside the target.

### 4.2 What component-first Gaussian inversion pays on the same exact law

Now condition on the four random centers in the partner representation. The four Gaussian variances are all `T_N`. In the completed Gaussian-mixture theorem write

`D=T_N I_4`, `B=D^{1/2} A D^{1/2}=T_N A`.

Since `A^2=I_4`,

`W_3=e_3(B^2)=e_3(T_N^2 I_4)=4 T_N^6`.                                (4.5)

The theorem's exact conditional Fourier estimate gives

`||p_{Q_N | centers}||_infinity
 <= (I_3/(2 pi)) W_3^{-1/6}`
` = (I_3/(2 pi)) 4^{-1/6} T_N^{-1}`
` = (I_3 2^{2/3}/pi) N^2`                                            (4.6)

with `I_3=2.942468198...`. Numerically,

`I_3 2^{2/3}/pi = 1.48678636...`.

Thus the raw component-first certificate is

`||p_{Q_N | centers}||_infinity <= 1.48678636... N^2`,                 (4.7)

and averaging the conditional suprema retains the `N^2` loss. In contrast, the actual whole-law density obeys (4.4):

`boxed{ ||p_{Q_N}||_infinity <=4 while the component-first bound grows as 1.4868 N^2. }`  (4.8)

This is the partner phenomenon in an indefinite, off-diagonal, exact-target family. It confirms quantitatively that translation/fragment aggregation has to happen **before** reciprocal component scale is paid.

---

## 5. Localization compiler for the remaining full proof

Theorem 2.1 gives a precise legal reduction for future workers:

> To prove full QFORM with constant `C`, it is enough to prove the interval small-ball estimate
> `P(X^TAX+b^TX+c in J)<=C|J|`
> uniformly for all compactly supported smooth cap-one product laws, with `C` independent of every support radius, translation, moment, derivative norm and fragment geometry.

No approximation factor is lost when passing back to arbitrary laws.

Proposition 3.1 simultaneously rules out the tempting next shortcut:

> One may **not** replace that smooth class by Gaussian location-scale mixtures satisfying a uniform `E T^{-1/2}` budget and appeal to TV closure. Those mixtures remain almost distance one from an explicit sequence of smooth compact cap-one densities.

The safe order is therefore

`whole cap-one marginal -> cap-preserving compact/smooth approximation -> whole-law analytic certificate`,

not

`fragment labels -> narrow components -> reciprocal scale/component peak -> average labels`.

This conclusion is fully compatible with the partner's BV obstruction and with the live correction that fixed fragment count/diameter reductions are false.

---

## 6. Remaining gap

This run resolves the **law-topology/localization** part of the rough endpoint: arbitrary tails, nonsmoothness, remote fragments and lack of moments can all be removed, with the exact optimal QFORM constant preserved, by whole-law cap-preserving compactification and smoothing.

It does **not** prove the unrestricted conjecture. The unresolved problem is now analytic/structural even on the smooth compact class: derive a dimension-free whole-law density bound from only `s_3(A)>=1` without introducing a certificate whose constant depends on support geometry, derivatives, moment size, component peak, a false pointwise Fourier envelope, or a non-product rotated representation.

The most relevant next step for B14 is to test whether the current arbitrary-matrix Gaussian proof can be rewritten so that its inverse-scale average is replaced by a functional of the **aggregate smoothed marginal** that is bounded solely by `||f_i||_infinity<=1`. Partner (1.1) shows no one-dimensional estimate depending only on the latent scale can do this; any successful replacement must retain overlap/cancellation between translated components through the quadratic map.
