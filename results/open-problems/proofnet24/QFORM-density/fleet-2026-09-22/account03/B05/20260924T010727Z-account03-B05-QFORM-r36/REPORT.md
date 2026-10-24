SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T01:07:27Z.
attacking: QFORM-NEAR-DOUBLEZERO-GENERAL-HYPERBOLA-v1 — extend the exact coordinate-hyperbola receiver to a punctured collar of general indefinite scalar pairs without conditioning the dependent residual.

# account03/B05 r36 — a uniform rough-input hyperbola receiver on a nonzero-diagonal collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea / equivalent interval bound preserving arbitrary original-coordinate product densities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING PRODUCT-PRESERVING INTERVAL THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Full-target continuity: **OPEN**. The theorem below proves absolute continuity and an essential density bound; continuity is not claimed.

## 1. Scope, fresh sources, and the first missing implication

Fresh owner control was reread before publication at `yspennstate/math-research-brain@de64e09a8455761a19bf2f16c5c5472621751fdb`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live correction inbox was reread. In particular this run does not use arbitrary-joint rank-three coarea, conditional caps for conjugate projections, post-rotation independence, pointwise quadratic van-der-Corput decay, a fiber supremum, or a claim that small coefficients make a small random error.

Immediate predecessor:

- `yspennstate/math-open-problems@3b26570e5ee8a21471acba644e9b20483cbb2118`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T234035Z-account03-B05-QFORM-r35/REPORT.md`.

Fresh complementary coarea input:

- account02/B05, `QFORM-COORD-HYPERBOLA-SCHUR-SQUARE-v1`, current source path
  `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260924T002222Z-account02-B05-QFORM-auto11/REPORT.md`.

That theorem pays the exact double-zero scalar pair `[[0,c],[c,0]]` by averaging the true product logarithmic kernel against the Schur square before taking a supremum. The first natural question is whether the same mechanism survives when the two diagonal entries are small but nonzero. The answer is yes on a fixed, scale-invariant collar.

Fresh designated partner account04/B05:

- `yspennstate/math-open-problems@3b2896d107b17c889b09ce366c957fd901e9a1fc`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`.

Its theorem gives the exact full-line interval bound `pi/sqrt(|det C|)` for an actual definite original-coordinate two-by-two block. Section 8 applies it to the literal-scalar endpoint, at the same scalar-pair boundary treated hyperbolically below.

## 2. The collar theorem

### Theorem `QFORM-NEAR-DOUBLEZERO-GENERAL-HYPERBOLA-v1`

Let `(S,E)` be an arbitrary real random pair, and suppose the marginal density of `S` is bounded by `sqrt(2)`. Let `Y,Z` be mutually independent, independent of `(S,E)`, and have densities bounded by `sqrt(2)`. Let `F=F(S,E)` and `G=G(S,E)` be arbitrary measurable real functions. Let

`B=[[a,c],[c,d]]`

be real symmetric and indefinite, and put

`D=|det B|=c^2-ad>0`.

Assume the scale-free near-double-zero collar

`max(|a|,|d|) <= sqrt(D)/5`.                                        (2.1)

For `L!=0`, deterministic `s0,q0`, define

`Q=L(S-s0)^2
   +a(Y+F)^2+2c(Y+F)(Z+G)+d(Z+G)^2+q0`.                            (2.2)

Then every finite interval `I` satisfies

`boxed:
 P(Q in I) <= 128 (D |L|)^(-1/3) |I|.
`                                                                       (2.3)

Consequently `Q` is absolutely continuous and

`boxed:
 ||p_Q||_(infinity,ess) <=128 (D |L|)^(-1/3).
`                                                                       (2.4)

No continuity of the density is asserted.

The theorem is deliberately stated with arbitrary `F(S,E),G(S,E)`: the dependent residual coordinate of the first product-projection bank may remain inside both translated hyperbolic factors. The theorem does **not** permit an additional arbitrary additive function of `E`; Section 9 explains why this is the remaining affine-null-direction issue in higher-rank conditioning.

## 3. Exact factorization of every pair in the collar

The collar implies `c!=0`. Define

`kappa = c + sign(c) sqrt(D)`,                                     (3.1)
`alpha = d/kappa`, `beta = a/kappa`,                               (3.2)
`delta = 1-alpha beta`.                                             (3.3)

Since `D=c^2-ad`, `kappa` is a root of

`kappa^2-2c kappa+ad=0`.                                            (3.4)

Therefore, for all real `y,z`,

`boxed:
 a y^2+2c yz+d z^2
 = kappa (y+alpha z)(z+beta y).
`                                                                       (3.5)

Moreover

`|kappa|=|c|+sqrt(D)`,                                              (3.6)
`delta=2 sqrt(D)/|kappa|`,                                         (3.7)
`boxed: |kappa| delta =2 sqrt(D).`                                 (3.8)

The collar gives

`|ad|<=D/25`, hence

`sqrt(24/25) <= |c|/sqrt(D) <= sqrt(26/25)`.                        (3.9)

Thus

`gamma:=|kappa|/sqrt(D)
 <=1+sqrt(26/25)=2.0198039027...`,                                  (3.10)

and

`|alpha|,|beta|
 <= (1/5)/(1+sqrt(24/25))
 <1/8`.                                                             (3.11)

In particular

`63/64 < delta <65/64`.                                             (3.12)

These inequalities are deterministic matrix identities; no probabilistic approximation has been made.

## 4. A rough kernel for the product of two nearby linear forms

Fix values of `(S,E)`, so that `F,G` are constants. Translate

`y=Y+F`, `z=Z+G`.

Their one-dimensional densities are still bounded by

`M=sqrt(2)`                                                        (4.1)

and remain independent. Put

`u=y+alpha z`, `v=z+beta y`.                                       (4.2)

The linear map `(y,z)->(u,v)` has determinant `delta>0`. For the product `w=uv`, the density formula is

`p_(uv)(w)
 =delta^(-1) int_R
   f((u-alpha w/u)/delta)
   g((w/u-beta u)/delta)
   du/|u|`                                                         (4.3)

for `w!=0`. Write the integral after the factor `delta^(-1)` as `I(w)/delta`, i.e.

`I(w)=int_R f(y(u))g(z(u))du/|u|`.                                 (4.4)

### Lemma 4.1 — two simultaneous envelopes

Under `|alpha|,|beta|<1/8` and `63/64<delta<65/64`,

`boxed:
 I(w) <=23 [1+log_+(1/|w|)],
`                                                                       (4.5)

and

`boxed:
 I(w) <=7 |w|^(-1/2).
`                                                                       (4.6)

#### Proof of the inverse-square-root envelope

Let `r=sqrt(|w|)`. On `|u|>=r`,

`y'(u)=(1+alpha w/u^2)/delta`,

so

`|y'(u)| >=7/(8 delta)`.                                            (4.7)

There are two monotone components, `u>=r` and `u<=-r`. Using `g<=M`, `1/|u|<=1/r`, and the probability mass of `f`,

`int_(|u|>=r) f(y(u))g(z(u))du/|u|
 <= (16 M delta/7) r^(-1).`                                        (4.8)

On `|u|<=r`, make the change `v=w/u`; then `du/|u|=dv/|v|` and `|v|>=r`. In the `v` parameter,

`z(v)=(v-beta w/v)/delta`,

and the same derivative argument gives another `(16 M delta/7)r^(-1)`. Therefore

`I(w)<= (32 M delta/7)|w|^(-1/2)
 <7 |w|^(-1/2)`,                                                    (4.9)

using `M=sqrt(2)` and `delta<65/64`.

#### Proof of the logarithmic envelope

First assume `0<|w|<=1`. On `|u|>=1/2`,

`|alpha w/u^2|<=1/2`, hence `|y'(u)|>=1/(2delta)`.                  (4.10)

Using the two monotone components, `g<=M`, and `1/|u|<=2`, this part is at most

`8 M delta`.                                                        (4.11)

On `|u|<=2|w|`, change again to `v=w/u`; now `|v|>=1/2`, and the symmetric derivative estimate for `z(v)` gives another `8 M delta`.

The only uncovered region can occur when `2|w|<1/2`; there

`2|w|<|u|<1/2`.

Using only `fg<=M^2=2`, its contribution is

`4 log(1/(4|w|))`.                                                   (4.12)

Since

`16 M delta <23`,                                                   (4.13)

we obtain

`I(w)<=23+4 log_+(1/|w|)
      <=23[1+log_+(1/|w|)]`.                                       (4.14)

For `|w|>1`, (4.6) gives `I(w)<=7<23`, so (4.5) also holds. QED.

The two envelopes must be retained together. The logarithmic bound is efficient near the hyperbolic critical value; the half-Riesz tail is efficient away from it.

## 5. Returning to the quadratic pair

By (3.5), the scalar-pair contribution equals `kappa uv`. Its conditional density at a nonzero offset `r` therefore satisfies, by (3.8),

`k(r)
 <= A [1+log_+(R/|r|)],
 A=23/(2 sqrt(D)),
 R=|kappa|`,                                                        (5.1)

and

`k(r)<=B |r|^(-1/2),
 B=7 sqrt(R)/(2 sqrt(D)).`                                          (5.2)

Both inequalities are uniform in the translations `F,G` and hence uniform in the whole environment `(S,E)`.

This is the key gain over conditioning either of the two transformed factors: no conditional density of a conjugate projection is introduced. The two original independent scalar banks are integrated jointly before any reciprocal quantity appears.

## 6. Schur-square small balls

For every real `t` and every `rho>0`, the cap `||p_S||inf<=sqrt(2)` gives

`P(|L(S-s0)^2-t|<rho)
 <=min{1,K sqrt(rho)},
 K=4/sqrt(|L|).`                                                     (6.1)

Indeed, the inverse image of an interval of radius `rho` under the translated square has total length at most `2 sqrt(2rho/|L|)`.

Fix an output point `q` and put

`r=|q-q0-L(S-s0)^2|`,                                               (6.2)
`x=K sqrt(R)=4 sqrt(R/|L|).`                                        (6.3)

The conditional kernel (5.1)-(5.2) is now averaged against the **unconditional marginal law of S**; the arbitrary dependent environment is never conditioned in a way that asks for a cap on `S|E`.

For the near region `r<=R`, layer cake and (6.1) give

`E[1_(r<=R)]<=min(1,x)`,                                            (6.4)

and

`E log_+(R/r)
 <= J(x),`                                                          (6.5)

where

`J(x)=2x`,                `0<x<=1`,
`J(x)=2+2log x`,          `x>=1`.                                   (6.6)

Hence

`N<=A*3x` for `x<=1`,                                                (6.7)

and

`N<=A(3+2log x)` for `x>=1`.                                        (6.8)

For the far region, another layer-cake computation gives

`E[r^(-1/2)1_(r>R)]
 <=R^(-1/2),                         x>=1,`
` <=K[1+log(1/x)],                   0<x<1.`                          (6.9)

Therefore the far contribution obeys the same scale after multiplication by `B`.

## 7. Scale cancellation and the constant 128

Put

`T=(D |L|)^(-1/3)`,                                                 (7.1)
`gamma=R/sqrt(D)`.                                                   (7.2)

From `x=4 sqrt(R/|L|)`,

`A/T
 =23*2^(1/3) gamma^(1/3) x^(-2/3).`                               (7.3)

For `x<=1`, (6.7) yields

`N/T
 <=69*2^(1/3) gamma^(1/3) x^(1/3)
 <=69*2^(1/3) gamma^(1/3).`                                        (7.4)

For `x>=1`, the function

`x^(-2/3)(3+2log x)`                                                (7.5)

is decreasing from `3`, so the same bound holds.

For the far term, (6.9) gives at most

`7*2^(1/3) gamma^(1/3) T`                                          (7.6)

when `x>=1`. For `x<1` the additional scalar factor is

`x^(1/3)[1+log(1/x)]`,                                              (7.7)

whose exact maximum on `(0,1]` is `3 exp(-2/3)`. Thus

`F/T
 <=21*2^(1/3) exp(-2/3) gamma^(1/3).`                              (7.8)

Using (3.10), the total numerical constant is at most

`[69*2^(1/3)+21*2^(1/3)exp(-2/3)]
 [1+sqrt(26/25)]^(1/3)
 =127.0622898016... <128.`                                          (7.9)

This proves (2.3)-(2.4).

The argument directly constructs an integrable mixture density and therefore yields interval domination. It does not rely on an invalid interval-to-Borel promotion of a frozen conditional profile.

## 8. Application to the live ratio packet and the designated partner

In the live homogeneous ratio-packet normal form from account01/B05 r26 and own r35,

`H=[[C,P],[P^T,B]]`,
`C-PB^(-1)P^T=lambda m e1e1^T`,
`mu=|det B||lambda|`,                                               (8.1)

write `(S,R)` for the first product-projection bank and `Y,Z` for the two disjoint scalar product banks. Completing the scalar pair gives exactly

`Q=lambda m S^2
  + [Y+A11 S+A12 R, Z+A21 S+A22 R]
    B
    [Y+A11 S+A12 R, Z+A21 S+A22 R]^T`.                             (8.2)

Thus Theorem 2 applies with

`L=lambda m`, `D=|det B|`,                                         (8.3)

whenever `B` is indefinite and

`max(|a|,|d|)<=sqrt(|det B|)/5`.                                    (8.4)

Since

`D|L|=|det B||lambda|m=mu m`,                                      (8.5)

we obtain

`boxed:
 ||p_Q||_(infinity,ess)
 <=128 (mu m)^(-1/3).
`                                                                       (8.6)

For the standard packet mass `m>=3/20`,

`boxed:
 ||p_Q||_(infinity,ess)
 <=128(20/(3mu))^(1/3)
 <240.906 mu^(-1/3).
`                                                                       (8.7)

In particular the hard subbranch `mu>=1` has a numerical bound `<240.906` throughout this entire nonzero-diagonal collar. The estimate is independent of `q_Y,q_Z,q_xi`, of the residual size in `(S,R)`, and of the overlap coefficients `Aij`. It strictly extends the exact double-zero hyperbolic endpoint to a punctured neighborhood.

This application is for the homogeneous packet (or for affine terms that can be removed by an authorized range translation). An arbitrary additive null-direction term generated by higher-rank conditioning is not silently discarded; it is recorded in Section 9.

### Fresh designated partner applied to an actual inequality

The newest completed account04/B05 theorem says that if an **actual original-coordinate** pair has a definite principal block `C`, then

`P(Q in I)<=pi |det C|^(-1/2)|I|`                                  (8.8)

in the cap-one target, even with arbitrary outside couplings and conditioning-generated affine terms.

Apply it at the literal-scalar endpoint of the same packet: if `q_Y=q_Z=1`, then the normalized scalar projections `Y,Z` are, up to signs, two literal independent original coordinates and their physical principal block is exactly `B`. Therefore, whenever this literal block is definite,

`boxed:
 P(Q in I)<=pi |det B|^(-1/2)|I|,
 ||p_Q||_(infinity,ess)<=pi |det B|^(-1/2).
`                                                                       (8.9)

This is the actual use of the designated partner theorem in this run. It is complementary to (8.6): (8.9) pays the convex literal-pair side, while the new theorem pays a scale-invariant hyperbolic collar where the literal-pair area argument would be infinite.

For reference, the earlier completed account04/B05 exact-slope theorem also remains valid: if the first-bank exact slope mass is `m_*`, then

`||p_Q||inf<51.6(mu m_*)^(-1/3)`.                                  (8.10)

Thus a heavy exact first-bank slope remains a separate exit; it is not needed in proving the new collar theorem.

## 9. Exact remaining factor

The new result changes the r35 debt. The exact double-zero scalar face and an entire fixed punctured collar around it are now paid without requiring scalar tails and without conditioning the dependent residual. A genuinely surviving hyperbolic packet must leave the collar:

`max(|a|,|d|)>sqrt(|det B|)/5`,                                     (9.1)

unless another existing slope/crossing/definite-pair exit fires.

There is a second, logically separate issue if the ratio packet is obtained by conditioning a higher-rank complement. Completing the scalar pair can leave an additive affine term in the Schur-null first-bank direction, schematically

`h R`.                                                              (9.2)

Because `S` and `R` are dependent projections of the same original product bank, one cannot condition `R` and preserve a cap for `S`, and an arbitrary function of `R` could destroy the square small-ball argument if treated as an unrestricted environment. The present theorem therefore does not claim to pay (9.2). The next precise coarea obligation is

`QFORM-HYPERBOLA-SCHUR-SQUARE-WITH-PRODUCT-NULL-AFFINE-v1`:

> retain the original-product provenance of `(S,R)` and prove a translation-uniform interval estimate for
> `L S^2+hR+kappa[Y+F(S,R)][Z+G(S,R)]`
> in the same near-double-zero collar, without conditioning `R` or replacing `(S,R)` by an arbitrary joint law.

Alternatively, a structural reduction that shows the relevant higher-rank packet has no such residual affine/null term would close the same debt. This is now the exact missing factor, rather than the nonzero diagonal perturbation itself.

## 10. Scope statement

No Gaussianity, moments, centering, compact support, connected support, log-concavity, or independence after rotation is used. The two scalar banks are genuinely independent original-coordinate product projections; their translated pair is integrated jointly. The first bank is used only through the cap of its one-dimensional projection `S`, while the correlated residual may enter both pair translations arbitrarily.

This is a supporting branch theorem, not a proof of unrestricted QFORM. The full theorem remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains OPEN.
