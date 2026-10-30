# fleet02/B04 — square-assisted two-direction spectral-window routing

**Run:** `20260922T164653Z-d0a9bbf0`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`; later owner control revision `2026-09-22.8` applied  
**Assignment:** Product Fourier rearrangement / complementary constructions and source-valid counterexamples  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full target remains `OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and first unpaid implication

The target is unchanged: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `X^T A X`, with no moment, support, sign, diagonal-basis, or post-rotation-independence assumptions, or produce a target-valid counterexample.

The previous B04 run reduced the diffuse branch to the completed `1/39` spectral-window theorem and obtained the heavy-coordinate alternative

`max(|A_ii|, ||A[i,i^c]||_2) >= 1/312`.

Its first unpaid implication was `QFORM-RIDGE-SQUARE-OR-HEAVY-BANK-ROUTING-v2`: route such a heavy physical coordinate into a square-assisted residual certificate or an aggregate bank mechanism.

This run closes a quantitative part of that implication. A square-dominant heavy coordinate automatically transfers **two** target-scale spectral directions into its Schur residual. If those two directions are diffuse at the corresponding `1/39` residual window, the previous square-assisted `L^(3/2)` ridge theorem applies with an explicit universal constant. If that residual window is heavy, it produces a second quantitative physical-coordinate certificate. Thus the unresolved heavy branch is reduced to bank-dominance / opposite-sign residual geometry rather than an arbitrary Schur residual.

## 2. Source-pinned dependencies and corrections

1. **Named partner fleet03/B04.** Canonical report
   `yspennstate/math-open-problems@093c15486c794a2e8b23978ca7b289feabf999a7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260922T154859Z-r13/REPORT.md`.
   I use its independently checked MSS spectral-window passage and ridge-perturbation estimate. For a high spectral subspace with row leverage at most `epsilon`, a two-part MSS partition has both partial frame operators at least

   `delta(epsilon)=1/2-sqrt(2 epsilon)-epsilon`.

   If the discarded tail has operator norm at most `tau`, then a physical cross block inherits the corresponding high singular directions up to `tau`, and its ridge leverage obeys the partner's perturbation inequality.

2. **Own preceding square-assisted theorem.** Canonical report
   `yspennstate/math-open-problems@b129377880c18fe011dd4513282f2e0b60e412e0`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T155815Z-qform-r11b/REPORT.md`.
   It proves `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1`: for

   `Q=a(X+m(Y))^2+R(Y)`,

   with one untouched original coordinate `X`, and a residual physical cross block `B`, define

   `K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`,
   `theta=tr K_gamma`,
   `D=det(I+BB^T/gamma^2)`.

   If `max diag K_gamma<=1/2` and `theta>4/3`, then

   `||p_Q||_inf <= 8*3^(-5/8)*sqrt(e)*sqrt(3theta/(3theta-4))*D^(-1/(4theta))/sqrt(|a| gamma)`.

   This theorem is based on the source-pinned free-regularizer Fourier envelope and the named partner's dependence-safe square smoothing; it does not assert independence after rotation.

3. **Live corrections respected.** Law-uniform pointwise Fresnel decay is false; unrestricted fiber suprema lose dimension; rotated spectral coordinates are not independent; one good cross minor / one good Schur rank-two extraction / a universal good small principal block are not forced. The current owner message's conditional-projection route is treated as a proposed route, not as a proved conditional-density statement; the live fiberwise-trace correction requires product aggregation before or jointly with curved tracing.

No refuted premise is used below.

## 3. New theorem: `QFORM-SQUARE-ASSISTED-TWO-DIRECTION-WINDOW39-v1`

Let `X` be one original coordinate with density at most one, independent of the remaining original coordinates `Y`. Let

`Q=a(X+m(Y))^2+Y^T S Y`,

where `a!=0`, `m` is measurable and finite a.s., and `S` is real symmetric. Fix `s>0`. Assume:

1. `S` has at least two eigenvalues `mu` with `|mu|>=s`;
2. if `P` is the spectral projection of `S` onto `|mu|>=s/39`, then
   `max_j P_jj<=1/32`.

Then `Q` has an essentially bounded density satisfying

`||p_Q||_inf <= C_2 / sqrt(|a| s)`,

where

`C_2 = 8*3^(-5/8)*sqrt(e)*(3/sqrt(2))*7^(-7/24)*sqrt(1248*sqrt(6)/241)`

and

`C_2 = 28.431014463217576... < 28.432`.

Arbitrary further eigenvalues of `S`, of either sign and arbitrarily small magnitude, are retained. No spectral-coordinate independence is assumed.

### Proof

Apply the partner's MSS construction to the high spectral subspace of `S`. With

`epsilon=1/32`,

`delta=1/2-sqrt(2epsilon)-epsilon=7/32`.

The resulting original-coordinate partition `I,J` gives a high-part cross block `B_0` whose second singular value satisfies

`s_2(B_0) >= (7/32)s`,

because the high spectral operator contains at least two eigenvalues of modulus at least `s`. The tail has operator norm less than or equal to `s/39`; hence the full physical cross block `B=S[I,J]` satisfies

`s_2(B) >= sigma := s(7/32-1/39)= (241/1248)s`.          (3.1)

The range projection of `B_0` has every diagonal at most

`epsilon/delta = 1/7`.                                      (3.2)

Choose

`gamma=sigma/sqrt(6)`.                                      (3.3)

The partner's ridge-perturbation estimate yields

`sqrt((K_gamma)_jj)
 <= 1/sqrt(7) + (s/39)/gamma
 = 1/sqrt(7)+32sqrt(6)/241`,

so

`max_j (K_gamma)_jj
 <= (1/sqrt(7)+32sqrt(6)/241)^2
 =0.49450138484491557... < 1/2`.                             (3.4)

Because `B` has two singular values at least `sigma`, the associated ridge variables

`x_r=s_r(B)^2/gamma^2`

satisfy `x_1,x_2>=6`. Therefore

`theta=sum_r x_r/(1+x_r) >= 12/7 >4/3`.                     (3.5)

Thus the preceding square-assisted ridge theorem applies. We retain the determinant factor instead of replacing it by the coarse `log D>=theta` estimate. Put

`h(x)=log(1+x)-x/(1+x)`.

Then `h` is increasing on `[0,infinity)`, so from `x_1,x_2>=6`,

`log D-theta = sum_r h(x_r) >= 2h(6)`,

where

`h(6)=log 7-6/7`.                                           (3.6)

Consequently

`D^(-1/(4theta))
 <= exp[-1/4-h(6)/(2theta)]`.                               (3.7)

For `theta>4/3`, the logarithmic derivative of

`F(theta)=sqrt(3theta/(3theta-4))*exp[-h(6)/(2theta)]`

is

`F'(theta)/F(theta)
 = -2/[theta(3theta-4)] + h(6)/(2theta^2) <0`,              (3.8)

because `3h(6)<4`. Hence the largest value allowed by (3.5) occurs at `theta=12/7`. At that endpoint,

`sqrt(3theta/(3theta-4)) = 3/sqrt(2)`,

and the `exp(-1/4)` in (3.7) cancels the `exp(+1/4)` contained in

`exp[-7h(6)/24] = 7^(-7/24) exp(1/4)`.

Therefore

`sqrt(3theta/(3theta-4))*D^(-1/(4theta))
 <= (3/sqrt(2))*7^(-7/24).`                                (3.9)

Insert (3.3) and `sigma=(241/1248)s` into the square-assisted ridge inequality. This gives exactly

`||p_Q||_inf
 <= C_2 / sqrt(|a|s)`

with the displayed `C_2`. QED.

## 4. New structural routing from one square-dominant heavy coordinate

Write the full target matrix around an original coordinate `i` as

`A=[[a,b^T],[b,C]]`,

and suppose

`a!=0`, `||b||_2<=|a|`.                                      (4.1)

Complete the square in the **original** coordinate:

`X^TAX = a(X_i+a^(-1)b^T Y)^2 + Y^T S Y`,

`S=C-bb^T/a`.                                                (4.2)

Define the shear

`T=[[1,a^(-1)b^T],[0,I]]`.

Then

`A=T^T diag(a,S) T`.                                        (4.3)

Let `r=||b||_2/|a|<=1`. The exact squared operator norm of this shear is

`||T||^2 = 1+r^2/2+(r/2)sqrt(r^2+4)
          <= (3+sqrt(5))/2 =: M_*`.                         (4.4)

Since the target hypothesis is `s_3(A)>=1`, the singular-value inequality

`s_3(A)<=||T||^2 s_3(diag(a,S))`

implies

`s_3(diag(a,S)) >= s_* := 1/M_* = (3-sqrt(5))/2
                    =0.38196601125010515... .`              (4.5)

The scalar block `a` can account for at most one of these three singular directions. Therefore `S` has at least two eigenvalues of modulus at least `s_*`.

Now apply Theorem 3 with `s=s_*`. If the residual spectral projection

`P_S=1_{|S|>=s_*/39}`

has maximum diagonal at most `1/32`, then

`||p_(X^TAX)||_inf <= C_2/sqrt(|a|s_*)`.                    (4.6)

Combine this with the preceding heavy-coordinate consequence of the partner `1/39` theorem: outside the already-closed diffuse original window there is an `i` with

`max(|a|,||b||_2)>=1/312`.                                  (4.7)

Hence, in the **square-dominant** branch

`|a|>=1/312`, `||b||_2<=|a|`,                               (4.8)

and with diffuse residual two-direction window,

`||p_(X^TAX)||_inf
 <= C_2 sqrt(312/s_*)
 =812.563468990244... <813`.                                (4.9)

This is a genuine target-level branch: all other spectral components and all arbitrary input laws remain present.

## 5. If the residual window is heavy, a second physical certificate is forced

Still under (4.8), suppose instead that some residual coordinate `j` has

`(P_S)_jj>1/32`.

Then, by the spectral theorem,

`||S e_j||_2^2
 >= (s_*/39)^2 (P_S)_jj
 > (s_*/39)^2/32`.                                          (5.1)

Write `c=S_jj` and `d=S[j,j^c]`. Since

`||S e_j||_2^2=c^2+||d||_2^2`,

(5.1) implies

`max(|c|,||d||_2) >= s_*/312
 =0.0012242500360580293... .`                               (5.2)

Thus failure of the new diffuse-residual branch cannot remain amorphous: it produces a second heavy original coordinate **inside the Schur residual**.

There is one immediate closure. If `|c|>=s_*/312` and `ac>0`, then the original physical `2x2` principal block on coordinates `{i,j}` has determinant

`det A[{i,j}] = a S_jj = ac >0`.                             (5.3)

It is therefore definite. Conditioning on all other original coordinates preserves independence and the density caps of the two selected coordinates; completing the induced affine terms and integrating elliptical shells gives the standard bound

`||p_(X^TAX)||_inf <= pi/sqrt(|ac|)
 <= pi*312/sqrt(s_*)
 =1585.959552002361... <1586`.                              (5.4)

No Young convolution with a dependent residual is used: (5.4) is a conditional-in-the-other-original-coordinates bound uniform in those coordinates.

So after the partner diffuse-window theorem, this run reduces the remaining matrices to the following explicit alternatives:

- an initial heavy coordinate is **bank-dominant**, `||b||>|a|`;
- or a square-dominant coordinate has a heavy Schur residual coordinate whose **off-diagonal residual bank** dominates;
- or that residual scalar is heavy but has sign opposite to the first square.

This is `QFORM-TWO-STAGE-HEAVY-ROUTING-v1`. These are the next unresolved cases; the full theorem is not claimed.

## 6. Explicit genuinely rotated indefinite example

Let `H` be a normalized real `64x64` Walsh-Hadamard matrix with columns `h_1,...,h_64`. On the 64 residual original coordinates define

`S = 2 h_1 h_1^T - 2 h_2 h_2^T
     + (1/50) sum_{k=3}^{64} (-1)^k h_k h_k^T`.             (6.1)

This is full rank, indefinite, and genuinely rotated in the original product coordinates. Its only eigenvalues of modulus at least `2/39` are `+2,-2`, so

`P= h_1h_1^T+h_2h_2^T`,

and every diagonal of `P` equals

`2/64=1/32`.                                                 (6.2)

Add one fresh original coordinate `X` and define

`Q = 2(X+0.1<h_1,Y>)^2 + Y^T S Y`.                          (6.3)

The unperturbed matrix `diag(2,S)` has three singular values equal to `2`. The square shift changes it by an operator of norm

`0.1^2+0.1 sqrt(0.1^2+4)
 =0.2102498439450079...`,                                    (6.4)

so Weyl's singular-value inequality gives

`s_3(A)>=1.7897501560549922>1`.                              (6.5)

Thus (6.3) is inside the exact target. Theorem 3 with `a=s=2` yields

`boxed: ||p_Q||_inf <= C_2/2
       =14.215507231608788... <14.216.`                      (6.6)

This example has only two target-scale residual directions; the final smoothing is supplied by the untouched original square rather than by falsely treating spectral coordinates as independent.

## 7. Exact computation used

```python
import math

eps=1/32
delta=7/32
tail_ratio=1/39
sigma_ratio=delta-tail_ratio
gamma_ratio=sigma_ratio/math.sqrt(6)
ridge_lev=(1/math.sqrt(7)+tail_ratio/gamma_ratio)**2
theta0=12/7
h6=math.log(7)-6/7
base=8*3**(-5/8)*math.sqrt(math.e)
det_theta_factor=(3/math.sqrt(2))*7**(-7/24)
C2=base*det_theta_factor/math.sqrt(gamma_ratio)

M1=(3+math.sqrt(5))/2
s0=1/M1
square_branch=C2*math.sqrt(312/s0)
residual_heavy=s0/312
definite_pair=math.pi*312/math.sqrt(s0)

example_bound=C2/math.sqrt(2*2)
coupling=0.1**2+0.1*math.sqrt(0.1**2+4)
spectral_lower=2-coupling

print('delta',delta)
print('sigma_ratio',sigma_ratio)
print('gamma_ratio',gamma_ratio)
print('ridge_leverage_bound',ridge_lev)
print('theta0',theta0)
print('h6',h6)
print('base',base)
print('det_theta_factor',det_theta_factor)
print('C2',C2)
print('M1',M1)
print('s0',s0)
print('square_branch_bound',square_branch)
print('residual_heavy_threshold',residual_heavy)
print('definite_pair_bound',definite_pair)
print('example_bound',example_bound)
print('coupling_perturbation_norm',coupling)
print('example_s3_lower',spectral_lower)

assert ridge_lev < 0.5
assert theta0 > 4/3
assert C2 < 28.432
assert square_branch < 813
assert example_bound < 14.216
assert spectral_lower > 1
```

Output:

```text
delta 0.21875
sigma_ratio 0.19310897435897437
gamma_ratio 0.07883640865528126
ridge_leverage_bound 0.49450138484491557
theta0 1.7142857142857142
h6 1.0887672919124562
base 6.637987706199633
det_theta_factor 1.202594819158655
C2 28.431014463217576
M1 2.618033988749895
s0 0.38196601125010515
square_branch_bound 812.563468990244
residual_heavy_threshold 0.0012242500360580293
definite_pair_bound 1585.9595520023609
example_bound 14.215507231608788
coupling_perturbation_norm 0.2102498439450079
example_s3_lower 1.7897501560549922
```

## 8. Conditional end-to-end route and exact remaining gap

A compact source-valid route is now:

1. If the `|A|>=1/39` spectral window has maximum coordinate leverage at most `1/32`, the named partner theorem gives a continuous density `<35.27`.
2. Otherwise a physical coordinate has `max(|a|,||b||)>=1/312`.
3. If it is square-dominant, the shear identity forces two Schur-residual directions at scale `s_*=(3-sqrt(5))/2`.
4. If their residual `1/39` window is diffuse, Theorem 3 gives density `<813`.
5. If that residual window is heavy, (5.2) forces a second physical residual certificate; a same-sign heavy scalar closes by the definite-pair estimate `<1586`.

The first unpaid implication is therefore the **two-stage bank/opposite-sign aggregation**: starting from either (i) an initial bank-dominant row, or (ii) a square-dominant row followed by a residual bank-dominant or opposite-sign heavy coordinate, extract a product-preserving grouped-coordinate packet that supplies the missing smoothing without paying a vanishing local minor. The live singleton-plus-two-banks and Pluecker-support counterexamples rule out the obvious local-minor shortcuts.

Status: `ESSENTIAL_STEP_APPLIED`. This is not a full proof and has not received two independent end-to-end reviews.
