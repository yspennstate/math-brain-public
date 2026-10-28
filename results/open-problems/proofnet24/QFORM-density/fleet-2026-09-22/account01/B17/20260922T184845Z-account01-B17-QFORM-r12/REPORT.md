# account01/B17 — two orthogonal same-sign heavy rows do not escape the 3sqrt(2) ceiling

Programme: QFORM-DENSITY-3EIG-20260922  
Run: 20260922T184845Z-account01-B17-QFORM-r12  
Assignment: Sharp constant and witnesses  
Status: AUXILIARY_ONLY / SHARP-WITNESS EXCLUSION; full QFORM conjecture OPEN  
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Target, fresh controls, and corrections

The full target remains: for every dimension n, every independent real input X_i with probability density bounded by one, and every real symmetric A with at least three eigenvalues of absolute value at least one, prove a universal finite bound on the essential supremum of the density of X^TAX, or give a counterexample. Continuity is separate.


The exact partner result applied is account02/B17 run `B17-20260922T181037Z-r11`, canonical report `yspennstate/math-open-problems@fbf14cd80c31d2100cf849494016bb4703aefdd7:proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T181037Z-r11/REPORT.md`. In particular I use its Lemma 3.1 and Corollary 3.2, not merely its summary.

## 2. Partner lemma, restated with exact normalization

If X has a probability density f<=1, G~N(0,1) is independent, ell in [0,1], and

`H_ell = sqrt(12 ell) X + sqrt(1-ell) G`,

then for every a>=0,

`E exp(-a H_ell^2) <= (1+2a)^(-1/2)`.                                             (2.1)

Indeed, with D=1+2a(1-ell), conditioning on X gives

`E_G exp[-a(sqrt(12ell)X+sqrt(1-ell)G)^2]`
`=D^(-1/2) exp[-12ell a X^2/D]`.

The cap-one bathtub inequality from the partner report gives

`E exp(-bX^2) <= int_{-1/2}^{1/2} exp(-b x^2) dx <= (1+b/6)^(-1/2)`.

Substitute b=12ell a/D to obtain (2.1) exactly. The second inequality is strict for b>0, so (2.1) is strict for every a>0 whenever ell>0.

This one-dimensional square-Laplace domination is the engine used twice below.

## 3. Exact target-admissible two-heavy family

Fix two leverages ell_1,ell_2 in [0,1]. Let J=diag(1,1,-1). For every integer m>=1 form a physical-to-spectral frame R_m with rows

- one heavy row `sqrt(ell_1)e_1`;
- m rows `sqrt((1-ell_1)/m)e_1`;
- one heavy row `sqrt(ell_2)e_2`;
- m rows `sqrt((1-ell_2)/m)e_2`;
- m rows `m^(-1/2)e_3`.

Thus

`R_m^T R_m = I_3`.

Consequently the physical symmetric matrix

`A_m = R_m J R_m^T`

has, for every finite m, nonzero spectrum exactly `{1,1,-1}`. Hence every A_m satisfies the original three-large-eigenvalue hypothesis exactly; no asymptotic spectral approximation is being made.

Take all physical coordinates independent. The two heavy coordinates X_1,X_2 are arbitrary laws with densities bounded by one. All 3m diffuse coordinates are independent `Unif[-1/2,1/2]`. The resulting spectral coordinates are

`Y_{1,m}=sqrt(ell_1)X_1 + sqrt((1-ell_1)/m) sum_{r=1}^m U_{1r}`,
`Y_{2,m}=sqrt(ell_2)X_2 + sqrt((1-ell_2)/m) sum_{r=1}^m U_{2r}`,
`Y_{3,m}=m^(-1/2) sum_{r=1}^m U_{3r}`,

and

`Q_m=X^T A_m X = Y_{1,m}^2+Y_{2,m}^2-Y_{3,m}^2`.                       (3.1)

This is the first genuinely two-noncollinear-heavy-row regime after the partner's one-heavy theorem. The two heavy directions are orthogonal and lie in the same-sign spectral plane. Any common rotation inside the positive eigenspace is equivalent because J is the identity on that plane.

Put

`S_m=sqrt(12/m) sum_{r=1}^m U_r`.

Then `S_m` has variance one and converges locally to a standard Gaussian. In standardized coordinates,

`12 Q_m = H_{1,m}^2+H_{2,m}^2-S_{3,m}^2`,

where

`H_{i,m}=sqrt(12ell_i)X_i+sqrt(1-ell_i)S_{i,m}`

and the three terms are independent. The limiting variables are

`H_i=sqrt(12ell_i)X_i+sqrt(1-ell_i)G_i`, i=1,2,

and an independent `G_3~N(0,1)`.

## 4. Central-density theorem

### Theorem 4.1 — QFORM-TWO-ORTHOGONAL-SAMESIGN-HEAVY-NOESCAPE-v1

For the exact source-valid family (3.1), for arbitrary independent cap-one heavy laws X_1,X_2,

`lim_{m->infinity} p_{Q_m}(0) <= 3 sqrt(2)`.                                (4.1)

If at least one of ell_1,ell_2 is positive, the limiting central density is strictly below `3sqrt(2)`.

#### Proof in the limiting model

Let

`P=H_1^2+H_2^2`, `N=G_3^2`, `q=P-N`.

The density of N on u>0 is

`g(u)=(2 pi u)^(-1/2) exp(-u/2)`.

Therefore

`p_q(0)=E g(P)`
`=(2pi)^(-1/2) E[P^(-1/2) exp(-P/2)]`.

Using

`x^(-1/2)=pi^(-1/2) int_0^infinity s^(-1/2) exp(-s x) ds`

and Tonelli,

`p_q(0)=1/(pi sqrt(2)) int_0^infinity s^(-1/2)`
`          E exp[-(s+1/2)H_1^2] E exp[-(s+1/2)H_2^2] ds`.                  (4.2)

Apply the partner bound (2.1) to each factor. Since

`1+2(s+1/2)=2(1+s)`,

(4.2) yields

`p_q(0) <= 1/(pi sqrt(2)) int_0^infinity s^(-1/2)/(2(1+s)) ds`
`        =1/(pi sqrt(2)) * (pi/2)`
`        =1/(2sqrt(2))`.                                                   (4.3)

Since `Q=q/12`, density scaling gives

`p_Q(0)=12 p_q(0)<=3sqrt(2)`.

If ell_1>0 or ell_2>0, the corresponding square-Laplace inequality is strict for every positive value of the integration parameter, so the inequality in (4.3) is strict.

#### Transfer from the finite exact frames

The local CLT for the bounded continuous summands gives densities s_m of S_m satisfying

`||s_m-phi||_infinity ->0`, `||s_m-phi||_1->0`, and `sup_m ||s_m||_infinity<infinity` after finitely many initial m.

For fixed ell_i in (0,1), convolution contraction gives both uniform and L1 convergence of the density of H_{i,m} to that of H_i. At ell_i=0 this is the local CLT itself; at ell_i=1 the heavy law is fixed. In every case the H_{i,m} densities have a finite m-uniform cap depending only on the fixed ell_i.

Let P_m=H_{1,m}^2+H_{2,m}^2. If h_{i,m} are the one-dimensional densities with caps M_i, then the square densities satisfy `g_i(u)<=M_i/sqrt(u)`, and their convolution therefore gives the uniform bound

`||p_{P_m}||_infinity <= pi M_1 M_2`.                                      (4.4)

The square density of S_{3,m} is

`g_m(u)=[s_m(sqrt(u))+s_m(-sqrt(u))]/(2sqrt(u))`, u>0.

Thus

`|g_m(u)-g(u)| <= ||s_m-phi||_infinity / sqrt(u)`.

By (4.4), `E P_m^(-1/2)` is uniformly finite: split the integral at one and use the bounded density on (0,1) and `u^(-1/2)<=1` on [1,infinity). Therefore

`|E g_m(P_m)-E g(P_m)| ->0`.                                               (4.5)

The laws of P_m converge to P in total variation after the same endpoint convention. The singularity of g at zero is harmless uniformly because (4.4) gives

`sup_m int_0^delta g(u)p_{P_m}(u)du = O(sqrt(delta))`.

On [delta,infinity), g is bounded, so total-variation convergence applies. Hence

`E g(P_m) -> E g(P)`.                                                       (4.6)

Combining (4.5)-(4.6) proves convergence of the finite exact central densities to the limiting value bounded in (4.3), and after the factor 12 proves (4.1). ∎

## 5. Full limiting peak for centered unit intervals

The arbitrary-law theorem above is deliberately only a central-density statement. If the two heavy laws are the centered unit intervals, the result strengthens to the full limiting density supremum.

### Proposition 5.1 — full mode at zero for the centered-interval family

Suppose the two heavy variables are `Unif[-1/2,1/2]`. Then for every finite m the three standardized coordinate densities are even and nonincreasing on `[0,infinity)`: each is a convolution of symmetric unimodal interval densities. Hence, if P_m=H_{1,m}^2+H_{2,m}^2, its density is

`r_m(u)=1/2 int_0^(2pi) h_{1,m}(sqrt(u)cos theta) h_{2,m}(sqrt(u)sin theta) dtheta`,

which is nonincreasing in u because every integrand is pointwise nonincreasing in u. The density of N_m=S_{3,m}^2 is also nonincreasing.

For q_m=P_m-N_m,

- if t>=0, `p_{q_m}(t)=int_0^infinity r_m(t+u)g_m(u)du <=p_{q_m}(0)`;
- if t=-a<0, `p_{q_m}(-a)=int_0^infinity r_m(u)g_m(u+a)du <=p_{q_m}(0)`.

Therefore the global mode is exactly zero for every finite m:

`||p_{Q_m}||_infinity = p_{Q_m}(0)`.

Combining with Theorem 4.1 gives

`limsup_{m->infinity} ||p_{Q_m}||_infinity <=3sqrt(2)`,                    (5.1)

strict in the limit if ell_1+ell_2>0.

Thus two orthogonal noncollinear macroscopic rows in the same-sign spectral plane cannot asymptotically beat the known `3sqrt(2)` witness, even at the global output mode, for the natural centered-interval extremal stress family.

## 6. Exact centered-interval integral and numerical controls

For the centered heavy interval let U_* be uniform on `[-sqrt(3),sqrt(3)]`. In the limiting standardized model

`H_ell=sqrt(ell)U_*+sqrt(1-ell)G`.

For a>0 define `D=1+2a(1-ell)`. Then the exact Laplace transform is

`L_ell(a)=D^(-1/2) * [sqrt(pi)/(2 sqrt(3ell a/D))] * erf(sqrt(3ell a/D))`,

with the continuous ell=0 value `(1+2a)^(-1/2)`. Hence the physical central peak is exactly the one-dimensional integral

`P(ell_1,ell_2)=12/(pi sqrt(2)) int_0^infinity s^(-1/2)`
`               L_{ell_1}(s+1/2)L_{ell_2}(s+1/2) ds`.                    (6.1)

A deterministic numerical checker of (6.1) gives the following controls (not proof certificates):

- `(ell_1,ell_2)=(0,0)`: `4.2426406871... =3sqrt(2)`;
- `(0.25,0)`: `4.2136463121...`;
- `(0.5,0)`: `4.0990952116...`;
- `(1,0)`: `3.5306641258...`;
- `(0.25,0.25)`: `4.1848968254...`;
- `(0.5,0.5)`: `3.9617322644...`;
- `(0.75,0.75)`: `3.5152361600...`;
- `(1,1)`: `2.9642054723...`.

The strict analytic inequality already proves every nonzero-leverage case is below `3sqrt(2)`; the numbers only show the size of the gap in representative cases.

## 7. What this removes and what remains

This run uses the completed account02/B17 one-heavy square-Laplace theorem in an actual new inequality twice and closes the first orthogonal noncollinear two-heavy extension. Together with the partner's arbitrary-orientation one-heavy theorem, it removes the following candidate sharp-witness mechanism:

- one arbitrary macroscopic row at any spectral orientation; and
- two orthogonal macroscopic rows carried by the same-sign two-dimensional eigenspace, with arbitrary cap-one heavy laws at the central level, and centered intervals at the full limiting density level.

This does not prove the full conjecture and does not prove that `3sqrt(2)` is the universal sharp constant. The first sharp-witness mechanisms still not excluded by this argument are:

1. two genuinely nonorthogonal macroscopic rows whose product-source geometry creates correlated positive-plane coordinates;
2. one positive and one negative heavy row (opposite-sign mixed leverage);
3. three or more interacting heavy rows;
4. finite-m local overshoot that disappears in the diffuse limit;
5. additional spectral directions beyond the exact rank-three stress family;
6. fragmented cap-one laws whose global mode is away from zero.

The highest-value next B17 step is to attack item 1: prove or refute the two-dimensional radial Laplace domination

`E exp(-a ||sqrt(12)V X + G_{I-VV^T}||^2) <= (1+2a)^(-1)`

for arbitrary 2x2 V with `VV^T<=I` and independent cap-one X_1,X_2. It is true for the orthogonal-column case by the theorem above; the nonorthogonal case is exactly where the product law and Gaussian completion cease to factor. A source-valid counterexample to this inequality would be a concrete new sharp-witness direction, while a proof would eliminate the entire two-heavy same-sign mesoscopic regime at once.

Full QFORM status: OPEN / NOT PROVED. Continuity status: separately OPEN.
