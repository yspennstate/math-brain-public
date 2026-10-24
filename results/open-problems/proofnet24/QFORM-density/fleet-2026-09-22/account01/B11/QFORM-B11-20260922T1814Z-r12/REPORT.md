SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B11, 2026-09-22T18:14:13Z.
attacking: exact-rank-three indefinite grouped-coordinate compiler; reduce the many-small-pair chamber to one weak spectral direction and test the scalar-conditioning bridge.

# account01/B11 — finite-heavy / diffuse-transverse reduction for indefinite exact rank three

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `QFORM-B11-20260922T1814Z-r12`  
Control observed before the write: OWNER CONTROL revision `2026-09-22.11`  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Conditional end-to-end position

The full theorem remains open. This report pays a structural part of the exact-rank-three indefinite chamber.

Let

`A=R Lambda R^T`, `R^T R=I_3`,

where `Lambda` is invertible with signature `(2,1)` or `(1,2)` and all three eigenvalues have absolute value at least one. Write the physical rows of `R` as `r_i^T` and their leverages as `c_i=||r_i||^2`.

The previous B11 run proves a universal density bound whenever one physical pair has spectral area

`G_ij=||r_i cross r_j||^2`

bounded below by a positive universal constant. The remaining vague obstruction was therefore called the many-small-pair/grouped-coordinate chamber.

The new result below gives an exhaustive product-coordinate trichotomy. With a fixed heavy threshold `1/4`, either

1. the low physical coordinates already carry all three spectral directions with conditioning at least `1/2`, and an orientation-free Fourier argument gives the explicit continuous-density bound `6e`; or
2. the heavy set carries two spectral directions strongly, forcing one physical heavy pair with `G_ij>=1/220`, so the previous strong-pair theorem gives an absolute bound `<3800`; or
3. exactly one spectral direction is weak on the low set. The heavy set has at most eleven coordinates and carries more than half the mass of that one direction, while the low coordinates form a diffuse two-dimensional frame on its orthogonal complement.

Thus the exact-rank-three grouped obstruction is reduced to a finite-heavy **one-weak-direction** normal form. No rotation of the independent physical coordinates is performed.

A second result gives a source-valid obstruction to the tempting next shortcut: even for three independent cap-one coordinates, every positive moment of the conditional `L^infinity` norm of the transverse pair given one scalar linear projection can be arbitrarily large. Hence the one-weak chamber must be paid jointly; conditional-pair-sup moments cannot be the compiler.

Arbitrary additional nonzero spectrum remains a separate debt to the full target.

## 2. Source-pinned premises actually used

### 2.1 Previous B11 strong-pair theorem

Source:

`yspennstate/math-open-problems@cfd6217faa10f4e19f4f35228593699c91fb9489`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260922T170957Z-account01-B11-QFORM-r11/REPORT.md`

For exact rank three, every physical pair of spectral area `G>0` satisfies the alternative

`||p_Q||_infinity <79.55 G^(-1/3)`

or

`||p_Q||_infinity <=256 G^(-1/2)`.

The proof combines the cross-dominated saddle estimate with the independently reviewed scalar-pivot theorem and retains the opposite-sign logarithmic singularity explicitly.

### 2.2 Orientation-free diffuse quadratic Fourier lemma

Source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

Its Lemma 3.1 is stated for arbitrary rank `r`: if `U^T U=I_r`, every physical row leverage of `U` is at most `1/2`, `M` is invertible symmetric, and `b` is any original-coordinate linear coefficient, then for

`F=(U^T X)^T M(U^T X)+b^T X`

one has

`|phi_F(t)| <= min(1, e^(r/2) pi^(r/2) |det M|^(-1/2)|t|^(-r/2)).`        (2.1)

The arbitrary affine term is important because conditioning on a set of original coordinates generates such a term.

### 2.3 Assigned partner account02/B11

Latest completed assigned-partner handoff used here:

`scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B11/20260922T155024Z-b11-qform-87d73745.md`

Canonical partner proof:

`yspennstate/math-open-problems@d56d97c85ced819f45ddad0987deaa5eb4b53cdc`

For independent cap-one variables, `sum b_k^2=1`, `Y=sum b_kX_k`,

`Q=2aX_0X_1+dY^2`

obeys

`||p_Q||_infinity <10.551 |a|^(-2/3)|d|^(-1/3).`             (2.2)

This is applied in Section 6 to an actual endpoint of the new normal form. It is not used outside its independence hypotheses.

## 3. Heavy/low frame decomposition

Set

`H={i: c_i>1/4}`, `L=H^c`,

and define the low-frame operator

`F=sum_{i in L} r_i r_i^T=R_L^T R_L`.

Since `sum_i c_i=tr(R^T R)=3`, the strict threshold gives

`|H|<=11`.                                                     (3.1)

Let

`0<=mu_1<=mu_2<=mu_3<=1`

be the eigenvalues of `F`.

The heavy-frame operator is

`G=I_3-F=sum_{i in H} r_i r_i^T`.

We split according to `mu_1` and `mu_2`.

## 4. Three-direction diffuse low frame: a `6e` continuous bound

### Theorem 4.1
If `mu_1>=1/2`, then the full exact-rank-three quadratic form has a continuous density satisfying

`||p_Q||_infinity <=6e`.                                     (4.1)

### Proof
Condition on all heavy physical coordinates `X_H`. The remaining conditional polynomial in the independent coordinates `X_L` has the form

`Q_L=X_L^T R_L Lambda R_L^T X_L+b^T X_L+c`,                 (4.2)

where `b,c` depend on the conditioned values. Put

`U=R_L F^(-1/2)`, `M=F^(1/2) Lambda F^(1/2)`.

Then `U^T U=I_3` and

`Q_L=(U^T X_L)^T M(U^T X_L)+b^T X_L+c`.

For each `i in L`,

`||U_i||^2=r_i^T F^(-1)r_i <=2||r_i||^2<=1/2`,              (4.3)

because `F>=I/2` and `c_i<=1/4`. Thus (2.1) with `r=3` applies uniformly in the induced affine term:

`|phi_{Q_L}(t)| <= min(1,K|t|^(-3/2))`,

`K=e^(3/2)pi^(3/2)|det M|^(-1/2)`.

The majorant is integrable and

`int_R min(1,K|t|^(-3/2)) dt =6K^(2/3)`.

Fourier inversion therefore yields

`||p_{Q_L}||_infinity <=(3/pi)K^(2/3)=3e|det M|^(-1/3).`     (4.4)

Now

`|det M|=det(F)|det Lambda| >=(1/2)^3*1=1/8`,

so (4.4) gives `||p_{Q_L}||_infinity<=6e`, uniformly in `X_H`. Averaging conditional densities preserves the same essential supremum.

Each conditional density is continuous. The uniform `6e` bound provides a dominating integrand when averaging over `X_H`, so dominated convergence proves continuity of the unconditional density. QED.

This branch is genuinely rotated and does not use independence of the spectral coordinates.

## 5. Two weak low directions force a strong physical pair

### Theorem 5.1
If `mu_2<1/2`, then some heavy physical pair satisfies

`G_ij=||r_i cross r_j||^2 >1/220`,                            (5.1)

and consequently the previous B11 theorem gives

`||p_Q||_infinity <3800`.                                    (5.2)

### Proof
The eigenvalues of `G=I-F` are `1-mu_3,1-mu_2,1-mu_1`. If `mu_2<1/2`, its two largest eigenvalues are both strictly bigger than `1/2`. Hence the second elementary symmetric polynomial obeys

`e_2(G)>1/4`.                                                 (5.3)

Cauchy--Binet gives the exact identity

`e_2(G)=sum_{i<j, i,j in H} det([[<r_i,r_i>,<r_i,r_j>],[<r_j,r_i>,<r_j,r_j>]])`

`       =sum_{i<j, i,j in H} ||r_i cross r_j||^2.`           (5.4)

By (3.1) there are at most `C(11,2)=55` terms, so (5.3)--(5.4) imply (5.1).

Apply the previous strong-pair alternative with `G>1/220`. The cross-dominated bound is less than `79.55*220^(1/3)<481`, while the scalar-pivot alternative is at most

`256 sqrt(220)<3798`.

Thus the safe universal bound `<3800` holds. QED.

This converts what looked like a many-small-pair configuration into a finite strong pair whenever two spectral directions are simultaneously missing from the low diffuse part.

## 6. The only remaining exact-rank-three chamber: one weak direction

Combining Theorems 4.1 and 5.1, the only branch not already covered is

`mu_1<1/2<=mu_2<=mu_3`.                                      (6.1)

Let `z` be a unit eigenvector of `F` for `mu_1`, and let `E=z^perp`. Then

`z^T G z=1-mu_1>1/2`.                                       (6.2)

Thus the at-most-eleven heavy physical coordinates carry more than half of the weak spectral direction.

On the transverse plane `E`, the low-frame operator has eigenvalues `mu_2,mu_3>=1/2`. For `i in L`, write `s_i=P_E r_i` and normalize the transverse low frame by `F_E^(-1/2)`. Its physical row leverages satisfy

`s_i^T F_E^(-1)s_i <=2||s_i||^2<=2c_i<=1/2`.                (6.3)

Hence the remaining two spectral directions are diffuse after an allowed **spectral-space** normalization, while all concentration has been localized to one spectral direction carried by at most eleven original independent coordinates.

This is the promised product-preserving normal form:

> **ONE-WEAK-DIRECTION NORMAL FORM.** Every exact-rank-three indefinite target is already uniformly controlled unless a set of at most eleven original coordinates carries more than half of one spectral direction and the complementary original coordinates form a leverage-`<=1/2` normalized frame on the transverse two-dimensional spectral plane.

No physical rotation was used. The original coordinate product law is intact.

### Actual application of the assigned partner result

A clean endpoint of (6.1) is the separated null-saddle/bank geometry from account02/B11: two heavy original coordinates form the saddle `2aX_0X_1`, while a disjoint normalized low bank forms `dY^2`, `Y=sum b_kX_k`, `sum b_k^2=1`. If `|a|,|d|>=1`, (2.2) gives the actual inequality

`||p_Q||_infinity <10.551`.                                  (6.4)

Any additional **independent additive** remainder may then be convolved without increasing the supremum. Equation (6.4) is the precise scope in which the partner theorem pays the one-weak endpoint. It is not extended to overlapping residual projections by conditioning.

This endpoint retains the required control example: deleting `dY^2` leaves the opposite-sign rank-two saddle, whose centered-uniform density has a logarithmic singularity. The third independent bank square turns the parabolic kernel into an integrable layer-cake profile, exactly as in the partner proof.

## 7. A source-valid obstruction: scalar linear conditioning does not bound transverse pair moments

A tempting next step after (6.1) would be to condition on the weak scalar projection and hope for a universal positive moment of the conditional `L^infinity` density of the transverse pair. That statement is false, already in dimension three.

### Proposition 7.1 — QFORM-SCALAR-LINEAR-CONDITIONAL-PAIR-MOMENT-FALSE-v1
For every `alpha in (0,1)` there exist three independent real random variables with densities bounded by one and an orthogonal map

`(X_1,X_2,X_3) -> (U,W,V)`

such that

`E ||p_{(W,V)|U}||_infinity^alpha`

is arbitrarily large.

### Proof
Fix an integer `N>=2` and define three measurable sets of Lebesgue measure one:

`E_1=union_{a=0}^{N-1}[10a,10a+1/N]`,

`E_2=union_{b=0}^{N-1}[10Nb,10Nb+1/N]`,

`E_3=union_{c=0}^{N-1}[10N^2c,10N^2c+1/N]`.

Let `X_j` have density `1_{E_j}`. These variables are independent and all density caps equal one.

Choose any orthogonal matrix whose first row is `(1,1,1)/sqrt(3)` and call the transformed coordinates `(U,W,V)`. Orthogonal change of variables preserves volume, so the joint density `g(u,w,v)` is still an indicator, hence takes only the values zero and one.

The product support consists of `N^3` boxes of side `1/N`. Their `U`-centers are proportional to

`a+Nb+N^2c`,

so the corresponding `U`-projection intervals are disjoint: distinct centers are separated by `10/sqrt(3)`, whereas each projected interval has length `sqrt(3)/N`.

Let `r` be the density of `(Y_1+Y_2+Y_3)/sqrt(3)` for iid `Y_j~Unif[0,1]`. On the support interval associated with a box indexed by `(a,b,c)`,

`p_U(u)=N^(-2) r(N(u-u_{abc})).`                             (7.1)

Thus for every `q in (0,1)`, with `C_q=int r(s)^q ds in (0,infinity)`, disjointness gives

`int p_U(u)^q du
 =N^3 * N^(-2q) * N^(-1) C_q
 =C_q N^(2-2q).`                                             (7.2)

For almost every `u` with `p_U(u)>0`, the conditional pair density is

`p_{(W,V)|U=u}(w,v)=g(u,w,v)/p_U(u)`.

Because `g` is an indicator and the section is nonempty,

`||p_{(W,V)|U=u}||_infinity=1/p_U(u)`.                       (7.3)

Combining (7.2)--(7.3),

`E ||p_{(W,V)|U}||_infinity^alpha
 =int p_U(u)^(1-alpha)du
 =C_{1-alpha} N^(2alpha) ->infinity.`                        (7.4)

In particular the exponent `alpha=2/3` grows like `N^(4/3)`. QED.

This is not a counterexample to the quadratic-form conjecture. It refutes only the proposed scalar-linear conditional pair-sup bridge. The product geometry must be used before or jointly with the indefinite curved trace.

## 8. Compact conditional end-to-end argument and first missing implication

For the exact-rank-three indefinite target, the present proof graph is now:

- if `mu_1>=1/2`, Theorem 4.1 gives the continuous bound `6e`;
- if `mu_2<1/2`, Theorem 5.1 plus the previous B11 strong-pair result gives `<3800`;
- otherwise `mu_1<1/2<=mu_2`, and Section 6 gives the one-weak-direction normal form.

Therefore the first local missing implication is

`QFORM-ONE-WEAK-DIRECTION-JOINT-SHEAR-v1`:

> For an exact-rank-three indefinite form in the normal form (6.1)--(6.3), prove a dimension-free small-ball/density bound by coupling the finite heavy weak-direction coordinates with the diffuse transverse two-dimensional low frame **before** taking conditional suprema. A valid route may use the translation-uniform rank-two half-Riesz kernel, a product-preserving shear, or grouped bank aggregation. It may not assume post-rotation independence or a positive conditional-pair-sup moment, the latter being refuted by Proposition 7.1.

If this implication is proved, the exact-rank-three indefinite problem is closed by the trichotomy above. The owner's full theorem still additionally requires a stable passage allowing arbitrary extra spectral components; no such passage is claimed here.

## 9. Status and continuity

Outcome: `ESSENTIAL_STEP_APPLIED`. Full QFORM is **OPEN**.

Continuity is proved in the full-low-frame branch `mu_1>=1/2`, because the uniform conditional characteristic-function majorant is integrable. The previous strong-pair branch and the partner bank theorem are used only for essential boundedness unless their cited sources separately prove continuity. No continuity claim is made for the unresolved one-weak branch or for the unrestricted target.

The rank-two opposite-sign logarithmic example remains a mandatory control and is not erased by any claim in this report.
