SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-23T21:56:03Z.
attacking: dependence-safe two-sided Plancherel for conjugate quadratic pairs, replacing exact matched-opposition by a difference-curvature criterion while retaining all same-bank curvature exactly.

# account03/B03 r41 — local-phase two-bank Plancherel and difference-curvature stability

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Classification:** `NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / NONPERTURBATIVE OPPOSITION-STABILITY BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. Full-target continuity remains OPEN. This report proves a dependence-safe integrated estimate and a genuine linear one-copy small-ball bound on a broad two-sided branch. It does not treat a small quadratic matrix perturbation as a small random variable; arbitrary same-bank curvature is retained exactly as a unit-modulus phase.

## 1. Source and correction scope


The live corrections retained here include:
- no law-uniform pointwise quadratic van-der-Corput estimate for arbitrary cap-one laws;
- no independence after rotating the original coordinates;
- no cap-one conditional law for one conjugate sum/difference variable given the other (`QFORM-UV-CONDITIONAL-CAP-FALSE`);
- no arbitrary-joint coarea shortcut;
- no replacement of a small operator perturbation by a small random quadratic perturbation without moments/support control.

The current designated partner result is account04/B03:

`yspennstate/math-open-problems@05ff82a8d052b024ae584e60dffb7b198fcd7db4`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260923T183012Z-account04-B03-dependent-riesz-r2/REPORT.md`.

It proves the dependent sum/difference fractional-budget theorem quoted in Section 4 below.

## 2. Two-bank local-phase Plancherel theorem

### Theorem 2.1 — `QFORM-TWO-BANK-LOCAL-PHASE-PLANCHEREL-v1`

Let `X=(X_1,X_2)` and `Y=(Y_1,Y_2)` be independent random vectors whose four scalar coordinates are mutually independent and have probability densities at most one. Let `C` be an invertible real `2 x 2` matrix, and let `F,G:R^2->R` be arbitrary measurable functions. Put

`S = F(X)+G(Y)+X^T C Y`.                                            (2.1)

Then for every `t!=0`,

`boxed:
 |phi_S(t)| <= min{1, 2 pi |det C|^(-1/2)|t|^(-1)}.
`                                                                       (2.2)

Consequently,

`boxed:
 int_R |t|^(-1/2)|phi_S(t)| dt
 <= 8 sqrt(2 pi)|det C|^(-1/4),
`                                                                       (2.3)

`boxed:
 sup_s E|S-s|^(-1/2) <= 8 |det C|^(-1/4),
`                                                                       (2.4)

and

`boxed:
 int_R |t|^(-1/2)|phi_S(t)|^2 dt
 <= (16/3)sqrt(2 pi)|det C|^(-1/4).
`                                                                       (2.5)

If `S'` is an independent copy of the whole random variable `S`, then

`boxed:
 E|S-S'|^(-1/2) <= (16/3)|det C|^(-1/4).
`                                                                       (2.6)

Moreover `S` has an `L^2` density and

`boxed:
 ||p_S||_2^2 <= 4 |det C|^(-1/2).
`                                                                       (2.7)

### Proof

Write `f_X(x)=f_1(x_1)f_2(x_2)` and `f_Y(y)=g_1(y_1)g_2(y_2)`, and for fixed `t` define

`a_t(x)=f_X(x)e^{itF(x)}`,  `b_t(y)=f_Y(y)e^{itG(y)}`.                (2.8)

Since each scalar density is at most one and has mass one,

`||a_t||_2^2 = int f_X^2 <=1`,  `||b_t||_2^2<=1`.                   (2.9)

With Fourier convention

`hat b(xi)=int_R2 e^{i xi.y} b(y)dy`,                                (2.10)

Fubini gives

`phi_S(t)=int_R2 a_t(x) hat b_t(t C^T x) dx`.                        (2.11)

Cauchy-Schwarz, the change of variables `xi=t C^T x`, and Plancherel yield

`|phi_S(t)|
 <= ||a_t||_2 [int |hat b_t(t C^T x)|^2 dx]^(1/2)
 = ||a_t||_2 |t|^(-1)|det C|^(-1/2)||hat b_t||_2
 <= 2 pi |det C|^(-1/2)|t|^(-1)`.                                  (2.12)

This proves (2.2). Notice that the internal terms `F(X),G(Y)` can have arbitrary size, sign and measurable structure: they occur only through unit-modulus factors in (2.8). No moment or support assumption is present.

Let

`A=2 pi |det C|^(-1/2)`.                                             (2.13)

Direct integration at the crossover `|t|=A` gives

`int |t|^(-1/2) min(1,A/|t|) dt = 8 sqrt(A)`,                       (2.14)

and

`int |t|^(-1/2) min(1,A^2/t^2) dt = (16/3)sqrt(A)`.                 (2.15)

These are (2.3) and (2.5). The one-dimensional Riesz identity

`int_R e^{itx}|t|^(-1/2)dt = sqrt(2 pi)|x|^(-1/2)`                  (2.16)

is used only through positive regularization. Applying (2.16) to the one-copy transform and then to the exact whole-copy identity

`|phi_S(t)|^2 = E exp(it(S-S'))`                                    (2.17)

gives (2.4) and (2.6). Finally, integrating the square of (2.2) gives

`int |phi_S(t)|^2 dt <= 4A=8 pi |det C|^(-1/2)`,                    (2.18)

so Plancherel gives (2.7). `square`

The theorem is a direct physical-product version of the crossing philosophy, but the feature needed here is that *both* arbitrary same-bank phases survive with no loss. That is what turns the exact matched-opposite r40 result into a robust difference-curvature statement below.

## 3. Conjugate quadratic pairs: arbitrary same-bank curvature is harmless

Let `X=(X_1,X_2)` have independent cap-one coordinates and let `X'` be an independent copy. Put

`U=X-X'`,  `V=X+X'`.                                                  (3.1)

The vectors `U,V` are dependent. Let `P_-,P_+` be arbitrary real symmetric `2 x 2` matrices and include arbitrary affine data:

`R_-(U)=U^T P_- U + ell_-^T U+d_-`,
`R_+(V)=V^T P_+ V + ell_+^T V+d_+`.                                 (3.2)

Define

`H=P_-+P_+`,  `K=P_+-P_-`.                                           (3.3)

Expansion in the genuine independent original-copy pair `(X,X')` gives the exact identity

`R_-(U)+R_+(V)
 = F(X)+G(X')+2 X^T K X'`,                                           (3.4)

where

`F(X)=X^T H X+(ell_-+ell_+)^T X+d_-/2+d_+/2`,
`G(X')=X'^T H X'+(-ell_-+ell_+)^T X'+d_-/2+d_+/2`.                  (3.5)

No independence of `U,V` has been introduced. In particular, `H` can be arbitrarily large and indefinite.

### Theorem 3.1 — `QFORM-CONJUGATE-DIFFERENCE-CURVATURE-HALFRIESZ-v1`

If `K=P_+-P_-` is invertible, then with

`S=R_-(U)+R_+(V)`                                                     (3.6)

one has

`boxed:
 |phi_S(t)| <= min{1, pi |det K|^(-1/2)|t|^(-1)},
`                                                                       (3.7)

`boxed:
 sup_s E|S-s|^(-1/2)
 <= 4 sqrt(2)|det K|^(-1/4),
`                                                                       (3.8)

and, in the exact assigned whole-copy form,

`boxed:
 int_R |t|^(-1/2)|phi_S(t)|^2 dt
 <= (16/3)sqrt(pi)|det K|^(-1/4).
`                                                                       (3.9)

Equivalently, for an independent copy `S'`,

`boxed:
 E|S-S'|^(-1/2)
 <= (8 sqrt(2)/3)|det K|^(-1/4).
`                                                                       (3.10)

**Proof.** Apply Theorem 2.1 to (3.4) with `Y=X'`, internal phases (3.5), and `C=2K`. Since `|det(2K)|=4|det K|`, equations (2.2), (2.4), (2.5), and (2.6) give exactly (3.7)-(3.10). `square`

This strictly extends r40's exact matched-opposite case. There `P_+=-P_-`, so `H=0` and `K=-2P_-`. Here no smallness is required of `H`: all departure from exact opposition that lands in the same-bank quadratic terms is retained exactly inside the phases `F,G`.

### Corollary 3.2 — nonperturbative approximate-opposition stability

Suppose `P_+=-P_-+E`, `sigma_min(P_-)=kappa>0`, and

`||E||_op <= theta kappa`,  `0<=theta<2`.                              (3.11)

Then

`K=-2P_-+E`,  `sigma_min(K)>=(2-theta)kappa`,                        (3.12)

hence

`|det K| >= [(2-theta)kappa]^2`.                                    (3.13)

Therefore

`boxed:
 sup_s E|S-s|^(-1/2)
 <= 4 sqrt(2)[(2-theta)kappa]^(-1/2).
`                                                                       (3.14)

The key point is conceptual as well as quantitative: `E` is **not** discarded and `X^T E X` is never declared small. The exact expansion simply moves its same-bank contribution into `F,G`, which Theorem 2.1 permits at arbitrary size on the realized support.

## 4. Designated partner result applied on the same dependent variables

The completed account04/B03 theorem applies directly to (3.2) when `P_-` and `P_+` are invertible. At `theta=1/2` it gives, for all `s,t`,

`boxed:
 E |R_-(U)-s|^(-1/4)|R_+(V)-t|^(-1/4)
 <= sqrt(calB(P_-)calB(P_+)),
`                                                                       (4.1)

with in particular `calB(P)<=128|det P|^(-1/4)`.

This yields the actual dependent joint-window inequality

`boxed:
 P(|R_-(U)-s|<=r, |R_+(V)-t|<=r)
 <= sqrt(calB(P_-)calB(P_+)) r^(1/2).
`                                                                       (4.2)

At `r=eps^2`,

`boxed:
 P(|R_-(U)-s|<=eps^2, |R_+(V)-t|<=eps^2)
 <= sqrt(calB(P_-)calB(P_+)) eps.
`                                                                       (4.3)

Equations (4.1)-(4.3) preserve the actual dependence of `(U,V)`. The new theorem does something complementary: it controls the **sum** by returning to `(X,X')` and using the cross-difference matrix `K`, rather than trying to spend another formal Holder exponent on (4.1).

## 5. A genuine third square recovers linear one-copy small-ball scaling

Let `Z` be a genuine original scalar coordinate, independent of the entire `(X,X')` bank, with density at most one. Let `d!=0`, and set

`T=d(Z+h)^2+S+c_0`.                                                    (5.1)

For the square term the usual density envelope is

`g(w)<=|d|^(-1/2)|w|^(-1/2)`                                        (5.2)

on its allowed side. Conditioning on `S` and using (3.8) therefore gives

`boxed:
 ||p_T||_(infinity,ess)
 <= 4 sqrt(2)|d|^(-1/2)|det K|^(-1/4).
`                                                                       (5.3)

Consequently every interval `I` obeys

`boxed:
 P(T in I)
 <= 4 sqrt(2)|d|^(-1/2)|det K|^(-1/4)|I|.
`                                                                       (5.4)

This is the requested recovery of **linear one-copy small-ball scaling** from a dependence-safe integrated-time mechanism. It proves essential boundedness on this branch. This argument does **not** prove continuity of the resulting density.

Under the approximate-opposition assumptions (3.11), (5.3) becomes

`boxed:
 ||p_T||_(infinity,ess)
 <= 4 sqrt(2)|d|^(-1/2)[(2-theta)kappa]^(-1/2).
`                                                                       (5.5)

For example, if `theta<=1`, `|d|>=1`, and `kappa>=1`, the branch constant is at most `4 sqrt(2)=5.65685424949...`.

## 6. Why this is not a hidden independence or pointwise-decay argument

The only independent banks in Theorem 2.1 are the genuine original-coordinate banks `X,Y`. In the conjugate application they are `X,X'`, which are independent by construction. The dependent variables `U=X-X'` and `V=X+X'` are never conditioned against one another. Their dependence is retained in the partner estimate (4.1), and the sum is handled by exact algebra (3.4).

The Fourier decay (2.2) is also not the refuted one-dimensional quadratic van-der-Corput claim. It comes from two-dimensional Plancherel across an invertible **bilinear cross map**. Arbitrary fragmented-support quadratic phases `e^{itF}`, `e^{itG}` are allowed because they leave `L^2` norms unchanged.

## 7. Exact remaining B03 implication

The r40 warning was: approximate opposition cannot be paid by declaring a small matrix perturbation to be a small random quadratic perturbation. Corollary 3.2 removes that obstruction whenever the difference-curvature matrix

`K=P_+-P_-`                                                           (7.1)

stays quantitatively invertible. The same-bank residual `H=P_-+P_+` can be arbitrary.

Thus the first genuinely unpaid two-sided endpoint is now the **singular/near-singular difference-curvature regime** `det K ->0`. If instead a quantitatively invertible same-bank two-dimensional quadratic matrix can be exposed, the already-proved orientation-free rank-two affine half-Riesz theorem can pay that branch after conditioning on the opposite original bank. The hard mixed endpoint is where both the cross-difference determinant and every such same-bank determinant become small while the original spectral hypothesis still carries three large modes. That is the next structural/analytic bridge; no conclusion about it is asserted here.

The full unrestricted QFORM conjecture remains OPEN. Full-target continuity remains OPEN.
