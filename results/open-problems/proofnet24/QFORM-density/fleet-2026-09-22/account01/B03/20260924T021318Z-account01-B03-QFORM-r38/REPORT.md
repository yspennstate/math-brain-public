SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-24T02:13:18Z.
attacking: the exact double-zero-diagonal localized overlap-two endpoint; replace the crude hyperbola half-power envelope by a two-regime product-density estimate, average it against the dependence-safe one-volume half-Frostman residual, and cancel the vanishing physical pair coefficient against the anchored third-minor packet.

# account01/B03 r38 — exact zero-pivot overlap-two payment by critical hyperbola averaging

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Classification: **NEW TARGET-LEVEL SUBBRANCH PAYMENT / LINEAR SMALL-BALL SCALING / DESIGNATED-PARTNER IDENTITY APPLIED / FULL QFORM OPEN**

The unrestricted conjecture remains **OPEN**. The theorem below closes the literal double-zero-diagonal endpoint of the current localized overlap-two packet. It proves absolute continuity and an essentially bounded density in that branch. Continuity is **not** claimed from this argument.

No Gaussianity, moments, compact support, connected support, log-concavity, post-rotation independence, pointwise van-der-Corput decay, conditional cap for a conjugate sum/difference variable, arbitrary-joint coarea estimate, or one-good-minor hypothesis is used.

## 1. Fresh source boundary

Fresh main control remains OWNER CONTROL revision `2026-09-22.15`, all eighty existing slots QFORM-only. The current owner continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. The full target and full continuity claim remain open in `CURRENT_RESEARCH.md` / `CLAIMS.json`.

The analytic input from this worker is the completed one-volume theorem

`QFORM-ROW-MARGINAL-FREE-1VOLUME-HALFFROSTMAN-v1`

at

`yspennstate/math-open-problems@6882d64088e54bc7f979ae8eb4a5ea9d06d1896f`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T185317Z-account01-B03-QFORM-r31/REPORT.md`.

For a literal original-coordinate cut `L|R` of a product-law quadratic remainder with cross block `M`, put

`Z_1=||M||_F^2`.

It proves, with no row-marginal hypothesis,

`P(|T-s|<rho) <= min(1,H_1 Z_1^(-1/4) sqrt(rho))`                 (1.1)

uniformly in `s,rho`, where

`H_1=sqrt(2e) Gamma(1/4)=8.453631522124516...`.                   (1.2)

Its proof is based on the dependence-safe whole-copy Cauchy--Schwarz/Fourier argument; it does not condition one of `X-X'` and `X+X'` on the other.

The current global structural funnel is source-pinned in account03/B20 r42. After the already-paid macroscopic physical diagonal, principal-triple and disjoint-`E_3` exits, one live branch is a literal physical pair `S` with

`J_2(S)>=1/144`                                                   (1.3)

and both physical diagonals small. Here

`J_2(S)=sum_{|I|=|J|=3, I cap J=S} det A[I,J]^2`.                 (1.4)

The exact `A_hh=0` pair endpoint is not paid by the older nonzero scalar-pivot bound.

The newest completed designated partner account02/B03 report used below is

`yspennstate/math-open-problems@1af51417c2d6a42394faa853627b8bb38d5f4d75`.

It proves a rank-two anchored-volume identity and, separately, a second-crossing instability example showing that finite whole-copy half-Riesz/time energy alone does not imply a bounded one-copy density. I apply the identity to the actual live overlap-one packet in Section 7 and respect the instability warning throughout.

## 2. A sharp-enough universal product-density envelope

The early r37 calculation used only

`p_{UV}(w)<=2|w|^(-1/2)`,

which is too wasteful near zero to cancel a small hyperbolic coefficient against the current overlap-two currency. The missing fact is that cap-one product laws have only logarithmic density growth near zero, uniformly over arbitrarily fragmented and translated supports.

### Lemma 2.1 — `QFORM-PRODUCT-LOG-HALFPOWER-ENVELOPE-v1`

Let `U,V` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. For `W=UV`, its density exists away from zero and satisfies, for every `w!=0`,

`boxed:
 p_W(w) <= min{ 4+2 log_+(1/|w|), 2 |w|^(-1/2) }.
`                                                                  (2.1)

The same bounds hold uniformly for `(U+a)(V+b)` for arbitrary deterministic translations `a,b`.

#### Proof

For `w!=0`, the standard product change of variables gives

`p_W(w)=int_R f(u)g(w/u) du/|u|`.                                 (2.2)

Put `r=|w|`. For each compatible sign quadrant reduce to subprobability densities `F,G` on `(0,infinity)`, still bounded by one, and consider

`I(r)=int_0^infinity F(u)G(r/u) du/u`.                             (2.3)

If `0<r<1`, split `(0,r)`, `[r,1]`, `(1,infinity)`.

On `(0,r)`, substitute `v=r/u`; then `v>1` and

`int_0^r F(u)G(r/u)du/u
 =int_1^infinity F(r/v)G(v)dv/v
 <=int_1^infinity G(v)dv <=1`.                                    (2.4)

On `[r,1]`, use only `F,G<=1`:

`int_r^1 ... <=int_r^1 du/u=log(1/r)`.                            (2.5)

On `(1,infinity)`,

`int_1^infinity F(u)G(r/u)du/u<=int_1^infinity F(u)du<=1`.        (2.6)

Thus one compatible sign quadrant contributes at most `2+log(1/r)`. There are two such quadrants, so

`p_W(w)<=4+2log(1/r)` for `r<1`.                                  (2.7)

If `r>=1`, split at `u=1`. On `(0,1)`, the same substitution gives at most `1/r<=1`; on `(1,infinity)` the contribution is at most one. Each sign quadrant is therefore at most two, yielding `p_W(w)<=4`.

For the half-power envelope, split (2.2) at `|u|=sqrt(r)`. On `|u|>=sqrt(r)`, use `g<=1` and `int f=1` to obtain at most `r^(-1/2)`. On `|u|<sqrt(r)`, substitute `v=w/u`; then `|v|>sqrt(r)` and use `f<=1`, `int g=1` to obtain another `r^(-1/2)`. This proves (2.1). Translations preserve independence and density caps. QED.

### Scaled hyperbola

Let `mu!=0`, `m=|mu|`, and

`Z=2 mu (U+a)(V+b)`.

Writing `L=2m`, Lemma 2.1 gives the uniform translated conditional envelope

`p_Z(y) <= m^(-1)[2+log(L/|y|)]`,        `0<|y|<L`,                (2.8)

and

`p_Z(y) <= sqrt(2)m^(-1/2)|y|^(-1/2)`,  `|y|>=L`.                (2.9)

No support location or moment enters.

## 3. Critical averaging against a square-root small-ball residual

### Theorem 3.1 — `QFORM-HYPERBOLA-HALFFROSTMAN-COMPILER-v1`

Let `X,Y` be independent cap-one variables, independent of an arbitrary environment `E`. Let `a(E),b(E),R(E)` be arbitrary measurable real functions. Let `mu!=0`, `m=|mu|`, and

`Q=2mu [X+a(E)][Y+b(E)] + R(E)`.                                  (3.1)

Assume that the residual obeys the translation-uniform square-root concentration estimate

`sup_s P(|R-s|<rho) <= min(1,H sqrt(rho))`                         (3.2)

for every `rho>0`. Define

`A_*=H sqrt(2m)`.                                                  (3.3)

Then `Q` is absolutely continuous and

`boxed:
 ||p_Q||_infinity <=
   (A_*/m)[5+log(1/A_*)],                 A_*<=1,
   m^(-1)[5+2log A_*],                    A_*>=1.
}`                                                                  (3.4)

In particular the estimate is uniform in the random translations `a(E),b(E)`.

#### Proof

Condition on `E`. Given the environment, `X+a(E)` and `Y+b(E)` remain independent cap-one variables, so (2.8)--(2.9) apply. For a target point `q` put

`Y_0=|R-q|`, `L=2m`.

Averaging the conditional density gives

`p_Q(q)
 <=m^(-1) E[(2+log(L/Y_0)) 1_(Y_0<L)]
   +sqrt(2)m^(-1/2) E[Y_0^(-1/2)1_(Y_0>=L)].`                    (3.5)

For the logarithmic term, layer cake and (3.2) give

`E log(L/Y_0)_+
 =int_0^infinity P(Y_0<L e^(-u))du
 <=int_0^infinity min(1,A_* e^(-u/2))du`.                         (3.6)

Thus

`E log(L/Y_0)_+ <= 2A_*`,                              `A_*<=1`,  (3.7)

and

`E log(L/Y_0)_+ <= 2+2log A_*`,                        `A_*>=1`.  (3.8)

Also `P(Y_0<L)<=min(1,A_*)`.

For the far half-power term use, for `y>=L`,

`y^(-1/2)=(1/2)int_y^infinity r^(-3/2)dr`.                         (3.9)

Tonelli and (3.2) imply

`E[Y_0^(-1/2)1_(Y_0>=L)]
 <=(1/2)int_L^infinity min(1,H sqrt(r)) r^(-3/2)dr`.               (3.10)

If `A_*<=1`, the threshold is `H^(-2)>=L`, and (3.10) equals at most

`H[1+log(1/A_*)]`.                                                 (3.11)

If `A_*>=1`, it is at most

`L^(-1/2)`.                                                        (3.12)

Since `H=A_*/sqrt(2m)` and `L=2m`, substitution into (3.5) gives exactly (3.4):

- for `A_*<=1`, the near part is at most `4A_*/m` and the far part at most `(A_*/m)[1+log(1/A_*)]`;
- for `A_*>=1`, the near part is at most `m^(-1)[4+2log A_*]` and the far part at most `m^(-1)`.

Absolute continuity follows by mixing the conditional product densities; `P(X+a(E)=0)=P(Y+b(E)=0)=0` for every fixed environment. QED.

The key point is that the logarithmic near-zero singularity and the half-power far tail are spent against the *same* square-root concentration law. Neither the crude `|y|^(-1/2)` estimate alone nor the whole-copy collision integral alone gives this cancellation.

## 4. Exact double-zero overlap-two payment

Let `S={h_1,h_2}` be a literal physical pair and suppose

`A[S,S]=[[0,mu],[mu,0]]`, `mu!=0`.                                (4.1)

Let `K=S^c`. Since the pair block is invertible, complete it exactly. Writing `X_S=(X_h1,X_h2)`, the full ambient quadratic form becomes

`Q=2mu [X_h1+a(X_K)][X_h2+b(X_K)] + R(X_K)`,                      (4.2)

where `R` is the quadratic form of the Schur complement

`S_A=A[K,K]-A[K,S]A[S,S]^(-1)A[S,K]`.                            (4.3)

The two peeled physical coordinates remain genuinely independent of the environment `X_K`.

Define the localized overlap-two third-minor mass

`J_2(S)=sum_(i!=j, i,j in K) det A[S union {i},S union {j}]^2`.   (4.4)

The block determinant identity gives, for every `i,j in K`,

`det A[S union {i},S union {j}]
 =det A[S,S] (S_A)_(ij)
 =-mu^2 (S_A)_(ij)`.                                              (4.5)

Because `J_2(S)` uses `i!=j`,

`boxed:
 J_2(S)=mu^4 sum_(i!=j)(S_A)_(ij)^2.}`                            (4.6)

Randomly put every coordinate of `K` into one of two disjoint literal banks `L,R` with probability one half. Then

`E ||(S_A)_[L,R]||_F^2
 =1/4 sum_(i!=j)(S_A)_(ij)^2
 =J_2(S)/(4mu^4).`                                                (4.7)

Hence some actual original-coordinate cut satisfies

`Z_1:=||(S_A)_[L,R]||_F^2 >= J_2(S)/(4mu^4).`                     (4.8)

Apply the completed one-volume theorem (1.1) to the **full Schur remainder** `R`, retaining all same-bank quadratic curvature. It gives (3.2) with

`H <= H_1 Z_1^(-1/4)
   <= sqrt(2) H_1 m J_2(S)^(-1/4)`.                               (4.9)

Consequently

`A_* =H sqrt(2m)
 <= x:=2 H_1 m^(3/2) J_2(S)^(-1/4).`                              (4.10)

The right side of Theorem 3.1 is monotone in `A_*` at fixed `m`, so it is enough to substitute `x`.

Solve (4.10)'s defining equality for `m`:

`m=x^(2/3) J_2(S)^(1/6) (2H_1)^(-2/3)`.                          (4.11)

If `x<=1`, Theorem 3.1 gives

`||p_Q||_infinity
 <=(2H_1)^(2/3) J_2(S)^(-1/6)
    x^(1/3)[5+log(1/x)].`                                        (4.12)

The scalar factor is increasing on `(0,1]`, because its derivative has sign `2-log x>0`; its maximum is five at `x=1`.

If `x>=1`,

`||p_Q||_infinity
 <=(2H_1)^(2/3) J_2(S)^(-1/6)
    x^(-2/3)[5+2log x].`                                         (4.13)

This scalar factor is decreasing on `[1,infinity)`, because its derivative has sign `-4(1+log x)<0`; its maximum is again five at `x=1`.

Therefore the small/large hyperbola scales glue with **complete cancellation of `mu`**:

### Theorem 4.1 — `QFORM-ZERODIAG-OVERLAP2-PAYMENT-v1`

Under (4.1), for the full ambient form and arbitrary independent cap-one input laws,

`boxed:
 ||p_Q||_infinity
 <= C_02 J_2(S)^(-1/6),
 C_02=5(2H_1)^(2/3)=32.93711407877257... .}`                      (4.14)

Thus every interval `I` obeys the genuine linear small-ball estimate

`boxed:
 P(Q in I)<=C_02 J_2(S)^(-1/6)|I|.}`                              (4.15)

For the live global packet `J_2(S)>=1/144`,

`boxed:
 ||p_Q||_infinity <=75.40716718914965... .}`                      (4.16)

This closes the **exact double-zero-diagonal** endpoint of the current localized overlap-two branch with a dimension-free universal constant.

Continuity is not proved by this mixture argument. Absolute continuity and essential boundedness are proved.

## 5. Dependence-safe whole-copy integral

The independent-copy identity is retained only in its legitimate whole-variable form:

`|phi_Q(t)|^2=E exp(it(Q-Q'))`,                                   (5.1)

where `Q'` is an independent copy of the entire scalar `Q`. At no point is `X_i-X_i'` conditionally re-capped given `X_i+X_i'`, and the two are never declared independent.

The one-volume concentration input (1.1) was itself obtained by a dependence-safe whole-copy Fourier/Cauchy--Schwarz argument. Once (4.14) is known, one also gets the a posteriori integrated whole-copy estimate

`int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <=4+2pi ||p_Q||_infinity
 <=4+2pi C_02 J_2(S)^(-1/6).`                                    (5.2)

Indeed `||p_Q||_2^2<=||p_Q||_infinity`, Plancherel gives `int|phi_Q|^2=2pi||p_Q||_2^2`, the contribution of `|t|<=1` is at most `4`, and `|t|^(-1/2)<=1` outside. At the live threshold `J_2=1/144`, (5.2) is at most

`477.79720493889965...`.                                          (5.3)

Equation (5.2) is recorded as a whole-copy energy consequence, **not** as the argument proving bounded density. The partner counterexample below shows why that distinction is necessary.

## 6. Why this is not contradicted by the second-crossing instability

The designated partner account02/B03 constructed a rank-two product-law form `T_epsilon` with an unbounded logarithmic output density while

`int |t|^(-1/2)|phi_(T_epsilon)(t)|^2dt<infinity`.

Therefore a finite weighted collision integral alone cannot be promoted to an `L^infinity` conclusion. The present proof does something strictly stronger: it derives a translation-uniform square-root concentration law for the Schur **residual**, keeps the exact near-zero logarithmic product kernel of the peeled hyperbola, and averages the two at the one-copy level. That is the step that recovers linear small-ball scaling.

## 7. Designated partner rank-two identity applied to the live overlap-one packet

The newest account02/B03 theorem also supplies an exact identity for a literal anchored block

`M=[[b,r^T],[c,N]]`                                                (7.1)

when `rank N=2`. If

`N=s_1 u_1 v_1^T+s_2 u_2 v_2^T`, `s_1,s_2>0`,                    (7.2)

and

`c=c_1u_1+c_2u_2+c_perp`,
`r=r_1v_1+r_2v_2+r_perp`,                                        (7.3)

then the partner proves

`J_sep = tau^2
 +||r_perp||^2(s_1^2 c_2^2+s_2^2 c_1^2)
 +||c_perp||^2(s_1^2 r_2^2+s_2^2 r_1^2)
 +(s_1^2+s_2^2)||c_perp||^2||r_perp||^2`,                        (7.4)

where

`tau=s_1s_2[b-r^T N^+ c]`.                                       (7.5)

Apply this completed partner identity to the **actual live one-anchor packet** from the global funnel, for which `J_sep>=1/2304`. The four terms in (7.4) are nonnegative. Therefore one of them is at least `1/9216`, and hence

`boxed:
 max{
  |tau|,
  ||r_perp|| sqrt(s_1^2 c_2^2+s_2^2 c_1^2),
  ||c_perp|| sqrt(s_1^2 r_2^2+s_2^2 r_1^2),
  sqrt(s_1^2+s_2^2)||c_perp||||r_perp||
 }
 >=1/96.}`                                                       (7.6)

This is a concrete source-valid inequality on the remaining rank-two overlap-one branch. It is useful because the partner's instability example also shows that one cannot simply perturb the exact-rank-one triangle theorem by a tiny second crossing: the anchored currency in (7.4), rather than the triangle product alone, must be spent.

I do **not** claim (7.6) already pays all four rank-two subcases. It is the sharpened next interface after the exact double-zero overlap-two payment above.

## 8. What remains

The global structural compiler currently leaves localized overlap-two and overlap-one packets after the already-paid diagonal/principal-triple/disjoint-cross exits.

This run pays overlap-two when the two shared physical diagonal entries are **exactly zero**. The remaining overlap-two collar has one or both shared diagonals nonzero but arbitrarily small; an older scalar-pivot theorem pays every fixed nonzero pivot but loses a negative power as that pivot tends to zero. The next useful step is a uniform interpolation between Theorem 4.1 and the nonzero-pivot compiler, or a direct determinant/trace version that treats the entire indefinite physical pair without a small-diagonal discontinuity.

For overlap-one, exact rank one is already paid by the three-group triangle theorem; in rank two, (7.6) is the current source-valid decomposition of the anchored currency. The partner's second-crossing instability rules out treating the second singular direction as a harmless perturbation.

Thus the unrestricted QFORM conjecture and unrestricted continuity claim remain **OPEN**.

## 9. Numerical constants and deterministic checks

Using

`H_1=sqrt(2e)Gamma(1/4)=8.453631522124516...`,

one obtains

`C_02=5(2H_1)^(2/3)=32.93711407877257...`,

and at `J_2=1/144`,

`C_02*144^(1/6)=75.40716718914965...`.

The a posteriori whole-copy weighted integral bound at that threshold is

`4+2pi*75.40716718914965...=477.79720493889965...`.

These are deterministic arithmetic checks only; no Monte Carlo or numerical histogram is used as evidence for the theorem.
