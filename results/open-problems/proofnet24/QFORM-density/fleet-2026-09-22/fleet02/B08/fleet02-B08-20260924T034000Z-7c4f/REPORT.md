SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-24T03:40:00.072482Z.
attacking: rank-one resonant hub alignment and the nonzero near-rank-one tangent-shear survivor; force an explicit original-coordinate spectral gate or a source-valid obstruction.

# fleet02/B08 r32 — singular-hub half-potential closure and the punctured near-singular survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / complementary constructions and source-valid counterexamples  
Designated partner: `fleet03/B08`  
Status: **NEW SUPPORTING SINGULAR-HUB THEOREM + QUANTIFIED PUNCTURED HYBRID ROUTER + TARGET-VALID HALF-POTENTIAL OBSTRUCTION / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains **OPEN**. Essential boundedness is the target below. Continuity is asserted only where an integrable characteristic-function majorant or an independently completed theorem supplies it. No moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation independence assumption is introduced.

## 1. First unpaid implication after this run

The first B08 debt is now

`QFORM-PUNCTURED-SINGULAR-HUB-HALFRIESZ-COMPILER-v1`:

> In the inherited two-physical-hub diffuse-arm state, after the actual `L/64` physical-pair gate and the r31 carrier-volume / real-shear / localized-hub gates, consume the **nonzero** near-singular hub Schur coefficient
> 
> `0 < |det B/B_pp| < 0.031747 L`,
> 
> while retaining arbitrary remaining quadratic curvature, all induced affine terms, the resonant/aligned rank-one carrier geometry, and arbitrary original-coordinate cap-one product sources. The exact endpoint `det B=0` is paid in this run. A successful compiler must not infer the nonzero case from the zero case by deleting a small quadratic term.

In the branch inherited from r31 this punctured state also carries the actual hub pivot

`|B_pp| > 4031 L/8192`,

the diffuse two-row arm gate `s_2(M)>=L/8`, and—after the earlier localized-hub half-potential gate—the carrier alignment

`r_q^2 < 512/4031`, `r_p^2 > 3519/4031`.

The newest fleet03/B08 deletion-spill router further removes raw third-child spectral loss whenever the deleted coordinate is diffuse in the selected top-three parent frame; Section 6 states the resulting localized alternatives.

## 2. Fresh source boundary


The required fixed source was read at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

including

- `RESULTS.md`,
- `FOURIER_ROUTE_REPORT.md`,
- `COUNTEREXAMPLE_SEARCH.md`.

The completed fixed-source result used in the new theorem is the square-peel Lemma 4.2 in `FOURIER_ROUTE_REPORT.md`:

`D(Q) <= |a|^(-1/2) H_{1/2}(S)`

for an ORIGINAL scalar pivot `a!=0` and its exact Schur remainder `S`. The same source supplies the product-projection/Fourier framework and the warning that a small matrix coefficient cannot be discarded as a small random perturbation under arbitrary supports.

A later source refresh found the newest compatible designated partner

`fleet03/B08 r49`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260924T032039Z-fleet03-B08-qform-diffuse-r49/REPORT.md`,
contained in `math-open-problems@209e9a8756cdab08ef8fb12c49d1d46934742b9c`.

Its immediate predecessor r48 remains the analytic tangent-shear input for the invertible-carrier branch; r49 supersedes r48's raw deletion-child spectral-loss terminal branch.

## 3. New theorem: a singular physical hub block gives a full-ambient half-potential receiver

Consider two ORIGINAL physical coordinates `p,q` and all remaining original coordinates `L`. Write the quadratic matrix in block form

`A = [[a,c,u^T],[c,b,v^T],[u,v,C]]`,

where `a!=0`, `u,v` are physical arm rows, and `C` is completely arbitrary symmetric curvature on the remaining coordinates. Arbitrary affine terms are allowed throughout.

Assume only

`det [[a,c],[c,b]] = ab-c^2 = 0`.

Define the exact Schur arm

`g = v-(c/a)u`.

### Theorem `QFORM-SINGULAR-HUB-STAR-HALFRIESZ-v1`

If `g!=0`, then for every independent original-coordinate source with one-dimensional densities bounded by one,

`boxed:
 ||p_Q||_infinity <= 2^(11/4) ( |a| ||g||_2 )^(-1/2).
`

The estimate is full-ambient: **no assumption at all** is imposed on `C`, including its rank, sign, same-bank spectrum, off-diagonal entries, or size. Conditioning outside the displayed coordinates is harmless because it only creates affine terms. This proof gives essential boundedness; it does not claim continuity.

### Proof

Apply the completed fixed-source square peel to the ORIGINAL coordinate `p`. Exact completion gives

`Q = a (X_p + ell(X_q,X_L))^2 + S(X_q,X_L)`.

The `q^2` coefficient in the Schur remainder is

`b-c^2/a = (ab-c^2)/a = 0`.

Therefore, after absorbing all remaining affine terms into a scalar shift `eta` and an arbitrary measurable remainder `W`, one has the exact form

`S = 2 X_q ( <g,X_L> + eta ) + W(X_L)`.

In the quadratic-form application `W` contains the **entire** Schur light block; it is not assumed diagonal or low rank.

Fix `X_L` and put

`Y=<g,X_L>+eta`.

For every target `s`, the cap-one density of the original coordinate `X_q` implies

`E_q |2Y X_q + W-s|^(-1/2) <= 2 |Y|^(-1/2).`                    (3.1)

Indeed, when `Y!=0`, scaling reduces the integral to

`(2|Y|)^(-1/2) int f_q(x)|x-t|^(-1/2) dx`.

Among probability densities capped by one, the last integral is maximized by the indicator of the unit interval centered at `t`, and equals at most

`int_{-1/2}^{1/2}|x|^(-1/2)dx = 2sqrt(2)`.

This is exactly (3.1). The event `Y=0` has probability zero once `g!=0` because `Y` has a density.

Now use the standard Ball--Rogozin/Livshyts--Paouris--Pivovarov one-dimensional product projection bound. The normalized linear form `(g/||g||).X_L` has density at most `sqrt(2)`, so

`||p_Y||_infinity <= K := sqrt(2)/||g||.`                       (3.2)

A second bathtub argument for the decreasing kernel `|y|^(-1/2)` yields

`E |Y|^(-1/2)
 <= K int_{-1/(2K)}^{1/(2K)} |y|^(-1/2)dy
 = 2 sqrt(2K).`                                                   (3.3)

Combining (3.1)-(3.3), uniformly in `s`,

`H_{1/2}(S)
 <= 4 sqrt(2K)
 <= 2^(11/4) ||g||^(-1/2).`                                     (3.4)

Finally the fixed-source square peel gives

`D(Q)<=|a|^(-1/2)H_{1/2}(S)`,

which is the stated theorem. QED.

### Why this theorem is source-safe

No stochastic coordinate is rotated. The only linear projection is used as a **marginal-density theorem** for `<g,X_L>`; its spectral components are never declared independent. The square completion is in one ORIGINAL physical coordinate. The arbitrary function `W(X_L)` remains inside the argument rather than being deleted or bounded pointwise.

## 4. Application to the live r31 resonant/aligned state

The inherited r31 state is

`A=[[B,M],[M^T,lambda ww^T+D]]`,
`w=M^T r`, `G=MM^T`,

with two ORIGINAL physical hubs, two-row arm `M`, arbitrary physical diagonal `D`, and arbitrary affine terms generated by conditioning.

The live diffuse-arm gates are

`mu=max_j m_j^T G^(-1)m_j <=1/3`,
`s_2(M)>=L/8`.

The earlier actual physical-pair theorem remains

`if some ORIGINAL physical 2x2 principal block has sigma_min>=L/64,
 then ||p_Q||_infinity<619/L.`                                   (4.1)

After the r31 mixed-hub and real-shear gates fail, one obtains an ORIGINAL hub `p` with

`|a|:=|B_pp|>4031L/8192`.                                       (4.2)

Let `q` be the other hub and write

`B=[[a,c],[c,b]]`.

If `det B=0`, the new theorem applies. Its Schur arm is

`g=m_q-(c/a)m_p = (-c/a,1)M`.

Since `s_2(M)` is the least singular value of the two-row arm,

`||g|| >= s_2(M) sqrt(1+(c/a)^2) >= s_2(M) >= L/8.`             (4.3)

Therefore

`||p_Q||_infinity
 <= 2^(11/4)(|a| ||g||)^(-1/2)
 < 27.1247693734 / L.`                                          (4.4)

This pays the **entire exact singular-hub endpoint**, independently of `lambda`, `r`, `D`, and every other coefficient of the remaining block. In particular it is stronger in scope than attempting to use the exact-resonance identity alone.

## 5. What a surviving nonzero hub determinant now looks like

Suppose (4.1) is unpaid and `det B!=0`. Let `s_1(B)>=s_2(B)>0` be the singular values of the symmetric hub block. The r31 selection of `p` gave

`|a| >= (s_1-s_2)/2`,                                           (5.1)

and the resonant branch gave

`s_1(B)>4095L/4096`, while (4.1) forces `s_2(B)<L/64`.           (5.2)

The exact remaining `q^2` coefficient after the ORIGINAL `p` square peel is

`delta_B := det B / a`.

Using `|det B|=s_1s_2`, (5.1)-(5.2) give

`|delta_B|
 <= 2s_1s_2/(s_1-s_2)
 = 2s_2/(1-s_2/s_1)
 < (8190/4031)(L/64)`,

hence

`boxed:
 0 < |delta_B| < 0.0317461548003 L.
`                                                                  (5.3)

This is the quantitatively **punctured** survivor promised in Section 1. The exact endpoint `delta_B=0` is no longer debt.

The previous localized-hub half-potential gate remains active: if the carrier direction in the hub plane is `r=(r_p,r_q)`, then failure of its determinant currency forces

`boxed:
 r_q^2<512/4031,
 r_p^2>3519/4031.
`                                                                  (5.4)

The r31 partner-cancelled-twist gate also remains: any light coordinate with

`|d_j|>=L/128`,
`|d_j+lambda w_j^2|<=|d_j|/2`

is already paid by fleet03/B08 r47 with `<152.219/L`. Thus the residual nonzero `delta_B` state must simultaneously evade that light-twist cancellation mechanism.

## 6. Newest fleet03/B08 r49 applied to the deletion-loss branch

The newest designated partner is fleet03/B08 r49, theorem

`QFORM-DIFFUSE-DELETION-PARTNER-SPILL-ROUTER-v1`.

Let `j` be the same ORIGINAL coordinate used in the r48 tangent-shear/deletion branch, and let `p_j` be its leverage in the selected top-three parent eigenframe. Use the live partner gates

`mu_top=1/48`, `theta=1/64`.

If `p_j>1/48`, then `j` is already an explicit localized top-three spectral coordinate. If instead

`p_j<=1/48`,

r49 gives the following exhaustive actual alternatives for the literal deletion child `C_j`:

1. if `s_3(C_j)>=L/64` and its `L/4096` child spectral window is diffuse, then
   
   `boxed: ||p_Q||_infinity<4096/L`, with a continuous C0 density;

2. if that child window is localized, then some ORIGINAL parent coordinate `k` obeys
   
   `boxed: max(|A_kk|,||A[k,-k]||_2)>L/32768;`

3. if `s_3(C_j)<L/64`, then the parent necessarily has
   
   `boxed: s_4(A)>185L/192;`
   
   if the corresponding parent spectral window is diffuse, then
   
   `boxed: ||p_Q||_infinity<65.658/L`, continuously;
   
   otherwise some ORIGINAL coordinate satisfies
   
   `boxed: max(|A_kk|,||A[k,-k]||_2)>185L/98304
          =0.00188191731770833... L.`

Thus the raw “deletion child loses its third eigenvalue” branch from r48 is no longer terminal in the diffuse selected-three regime. It either pays outright or produces a stronger physical localized witness at the parent scale.

For completeness, the r48 tangent-shear estimate itself remains useful in the invertible aligned-carrier branch. If `R` is invertible, `mu<=1/3`, and a physical twist `d_j` makes `diag(d_j,R)` indefinite, r48 gives

`||p_Q||_infinity
 <=8.653498 [ |d_j det R| det(MM^T) ]^(-1/3).`                  (6.1)

Therefore the inherited 619/L benchmark is already paid whenever

`boxed:
 |d_j det R| det(MM^T)
 >=2.7321412344e-6 L^3.
`                                                                  (6.2)

The remaining invertible-carrier branch must have small tangent-shear currency or fall into the localized alternatives above.

## 7. Target-valid punctured-singular stress family

The exact theorem in Section 3 must **not** be extended to (5.3) by continuity in `delta_B`. The following family makes the obstruction explicit while remaining safely inside the QFORM target and while having no good physical `2x2` principal block.

Fix

`0<delta<1/64`, `m>64/delta`, `n>64`.

Use mutually disjoint original-coordinate banks

- one coordinate `Z`,
- one coordinate `H` and an `m`-coordinate bank `X`,
- an `n`-coordinate bank `Y`.

Let

`g_m=m^(-1/2)(1,...,1)`,
`u_n=n^(-1/2)(1,...,1)`,

and on the `H+X` bank define

`v_delta = sqrt(delta) e_H + delta^(-1/2) g_m`.

Set

`A_{delta,m,n}
 = L [ e_Z e_Z^T + v_delta v_delta^T + u_n u_n^T ]`,            (7.1)

where the three rank-one vectors have disjoint physical supports.

### 7.1 Exact target spectrum

The only nonzero eigenvalues are exactly

`boxed:
 L,
 L(delta+delta^(-1)),
 L.
`                                                                  (7.2)

Thus the matrix satisfies the exact target with three eigenvalues of modulus at least `L`.

### 7.2 Every physical pair misses the actual `L/64` gate

Inside either rank-one support every `2x2` principal block is singular. Across different supports the block is diagonal, and the only nonzero one-coordinate diagonal scales besides the `Z` entry are

`delta L`, `L/(delta m)`, `L/n`,

all strictly below `L/64` by construction. Hence every physical `2x2` principal block is singular or has

`sigma_min<L/64`.                                                (7.3)

At the concrete checker point

`delta=1/128`, `m=16384`, `n=128`,

all three nonzero small pair scales equal exactly

`L/128`.

### 7.3 The near-singular half-potential can blow up on a frozen third-resource slice

The physical hub block on `(Z,H)` is

`L diag(1,delta)`,

so it approaches the exact singular block as `delta->0` but remains nonzero. After peeling `Z`, the `H+X` part is

`L [ delta H^2 +2H(g_m.X)+delta^(-1)(g_m.X)^2 ]`

`= L delta [ H + delta^(-1)(g_m.X) ]^2.`                         (7.4)

For the valid product source in which `H,X_i` are uniform on `[-1/2,1/2]`, the scalar

`T=H+delta^(-1)(g_m.X)`

has a continuous density positive at zero. Therefore

`E |L delta T^2|^(-1/2)
 = (Ldelta)^(-1/2) E|T|^(-1)
 = +infinity.`                                                   (7.5)

Consequently, after freezing the disjoint `Y` bank at the zero slice, the half-potential demanded by a naive extension of the Section 3 square-peel receiver is infinite for every `delta>0`, however small. This is a mechanism obstruction to “the nonzero coefficient is close to zero, so delete it.” It is not a counterexample to QFORM.

### 7.4 The same full target family is uniformly bounded

For arbitrary admissible product sources, define the three independent block variables

`Z`,
`V=<v_delta,(H,X)>`,
`U=<u_n,Y>`.

They are independent because they use disjoint ORIGINAL coordinate banks. The normalized linear form `U` has density at most `sqrt(2)`. Therefore

`p_{Z^2}(s)<=s^(-1/2)`,
`p_{U^2}(s)<=sqrt(2)s^(-1/2)`

for `s>0`, and convolution gives

`||p_{Z^2+U^2}||_infinity
 <=sqrt(2) int_0^s [t(s-t)]^(-1/2)dt
 =pi sqrt(2).`

Adding the independent nonnegative variable `V^2` cannot increase the `L^infinity` norm. Scaling by `L` yields the actual universal family bound

`boxed:
 ||p_{X^T A_{delta,m,n} X}||_infinity
 <= pi sqrt(2)/L
 =4.4428829382.../L.
`                                                                  (7.6)

Thus (7.1) is a target-valid **proof-mechanism obstruction**, not a QFORM counterexample. It shows exactly why the punctured near-singular coefficient in (5.3) must be consumed together with the surviving third spectral resource rather than by local perturbation theory.

## 8. Interpretation of the remaining hybrid

The localized/diffuse picture is now narrower than in r31.

- A well-conditioned ORIGINAL physical pair (`sigma_min>=L/64`) is paid by `<619/L`.
- In the weak-pair resonant rank-one carrier chamber, carrier volume and positive real-shear discriminant are paid by the r31 mixed-hub and real-shear compilers.
- Their failure forces the actual macroscopic hub pivot `|a|>4031L/8192` and carrier alignment (5.4).
- **This run pays the entire exact singular hub block `det B=0` by `<27.125/L`, with arbitrary remaining curvature.**
- A surviving nonzero hub block has the explicit tiny Schur coefficient (5.3), but the stress family proves that coefficient cannot be discarded under arbitrary supports.
- In the invertible aligned-carrier branch, r48 pays the nontrivial tangent-shear currency (6.2); r49 turns deletion-child spectral loss into either payment or a concrete ORIGINAL localized witness.

The genuine remaining debt is therefore not “a singular hub” and not “child spectral loss.” It is the **punctured** near-singular hub coefficient coupled to the still-present second/third spectral resources, in a branch that has already accumulated physical localization. A successful next proof should use those resources simultaneously—most plausibly a two-variable product half-Riesz / cancelled-square compiler stable for `0<|delta_B|<0.031747L`—rather than conditioning them away.

## 9. Deterministic checks and status

`CHECKS.py` verifies the scale constants and the stress-family formulas. `CHECKS.txt` terminates

`QFORM_B08_R32_CHECK_PASS`.

The checked values are

- singular-hub live constant: `27.124769373386016`,
- r48 619/L tangent-shear currency threshold: `2.732141234361960e-6`,
- punctured Schur-hub coefficient ceiling: `0.031746154800298 L`,
- r49 fourth-spill scale: `185/192=0.963541666666667`,
- r49 diffuse spill payment: `65.657826813698960/L`,
- concrete stress spectrum at `delta=1/128`: `(L,128.0078125 L,L)`,
- concrete nonzero physical-pair scales: all `L/128`,
- full stress-family density certificate: `pi sqrt(2)/L=4.442882938158366/L`.

The full QFORM conjecture remains OPEN. The exact singular physical-hub endpoint is closed by a new full-ambient essential-density theorem; the nonzero near-singular puncture remains the first B08 debt.
