SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-22T21:38:56Z.
attacking: cross-block bilinear smoothing through product-projection L2 control, and the critical rank-two-cross plus independent-square closure.

# account01/B16 — cross-bank L2 bilinear smoothing and the rank-two-plus-square bridge

Status: `ESSENTIAL_STEP_APPLIED`; full QFORM OPEN / NOT PROVED. Full continuity remains separate. Execution: `WITHOUT_VERIFIED_BRAIN`.

Fresh control source at start: `yspennstate/math-research-brain@f80b78e724a1afd0074252838dbdd818e6bbe22b`, OWNER CONTROL revision `2026-09-22.15`; refreshed before publication on fresh main with the same QFORM-exclusive owner control. Assignment: projection-product interaction.

Live corrections consumed: arbitrary-joint 3D coarea is false; positive conditional projection-density moments are false; projected spectral coordinates are not independent after rotation; normalized thin-fiber and conditional-cap shortcuts are invalid; coordinatewise mixed ambiguity/BL reaches only the critical exponent on the harmonic-bank obstruction. None of those false interfaces is used below.

Dependencies actually applied:

1. Own previous source-product theorem `QFORM-GROUPED-L2-FRESNEL-v1`, canonical report `yspennstate/math-open-problems@e4c589aa572f7d140c78a832af2d554eed97fde4:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260922T211047Z-account01-B16-QFORM-r16/REPORT.md`, which records the actual bounded-density projection theorem in dimensions 1,2,3 and the source-grouping principle.
2. Designated partner account02/B16 `20260922T203148Z-account02-B16-QFORM-auto11`, canonical report `yspennstate/math-open-problems@484069f14f49a3303befbe62863d950e67c809e1:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T203148Z-account02-B16-QFORM-auto11/REPORT.md`. In particular, its grouped-bank step applies Ball--Rogozin to a normalized source projection and obtains `||p_L||_infinity<=sqrt(2)`; its mixed-ambiguity theorem shows why a coordinatewise absolute payment can stall exactly at `|t|^-1`.

The point of this run is to turn that critical `|t|^-1` rank-two cross-bank decay into a uniform half-Riesz bound, and then spend one genuinely independent square bank to reach a bounded density. This is a nonlinear product-preserving synthesis, not a conditional spectral-density argument.

## 1. Complex projection lemma for a physical source bank

Let `X_I` be a block of original independent coordinates with joint product density `rho_I`. Let `E` be a Euclidean subspace of `R^I`, and let `H_I:R^I->R` be arbitrary measurable. For fixed real `t`, define the complex measure

`mu_(I,t)(B)=E[1_{P_E X_I in B} exp(i t H_I(X_I))]`.

If the positive projection `P_E X_I` has density `rho_E`, then `mu_(I,t)` has density `a_(I,t)` satisfying

`|a_(I,t)(u)|<=rho_E(u)` almost everywhere.

Hence, if `||rho_E||_infinity<=M_E`,

`||a_(I,t)||_1<=1`,
`||a_(I,t)||_2<=M_E^(1/2)`.

This is simply disintegration before absolute value. It preserves all dependence within the physical bank and does not assert independence after an orthogonal rotation.

## 2. Rank-r cross-bank Fourier theorem

Split the original coordinates into two disjoint source banks `I,J`. Let

`R=H_I(X_I)+H_J(X_J)+2 X_I^T C X_J`,

where `H_I,H_J` are arbitrary measurable real functions and `C:R^J->R^I` is a real matrix of exact rank `r>=1`.

Put

`E=range(C) subset R^I`,
`F=range(C^T) subset R^J`.

Let the nonzero singular values of `C:F->E` be `sigma_1,...,sigma_r`, and set

`Delta_r(C)=prod_(k=1)^r sigma_k`.

Assume the positive projection densities of `P_E X_I` and `P_F X_J` satisfy caps `M_E,M_F`.

### Theorem 2.1 — `QFORM-CROSSBANK-L2-FOURIER-v1`

For every `t!=0`,

`|phi_R(t)| <= pi^(r/2) (M_E M_F)^(1/2) Delta_r(C)^(-1/2) |t|^(-r/2)`.      (2.1)

If `r>2`, then `R` has a bounded continuous density and

`||p_R||_infinity <= [r/(r-2)] (M_E M_F)^(1/r) Delta_r(C)^(-1/r)`.          (2.2)

### Proof

For fixed `t`, use Section 1 to push the two complex bank measures onto `E` and `F`, obtaining densities `a_t,b_t` with

`||a_t||_2<=M_E^(1/2)`, `||b_t||_2<=M_F^(1/2)`.

Because the two original source banks are genuinely independent and because the bilinear term only sees `P_E X_I` and `P_F X_J`,

`phi_R(t)=int_E int_F a_t(u)b_t(v) exp(2 i t <u,Cv>) du dv`.

Use the Fourier convention `hat b(xi)=int_F exp(i<xi,v>)b(v)dv`. Then

`phi_R(t)=int_E a_t(u) hat b_t(2t C^T u)du`.

Cauchy--Schwarz, the invertibility of `C:F->E`, and Plancherel give

`|phi_R(t)|
 <= ||a_t||_2 [int_E |hat b_t(2t C^T u)|^2 du]^(1/2)
 = ||a_t||_2 (2|t|)^(-r/2) Delta_r(C)^(-1/2) ||hat b_t||_2
 <= pi^(r/2) (M_E M_F)^(1/2) Delta_r(C)^(-1/2)|t|^(-r/2)`.

This proves (2.1).

Write the coefficient in (2.1) as `K`. Since `|phi_R(t)|<=1`, for `r>2`

`int_R |phi_R(t)|dt
 <= int_R min(1,K|t|^(-r/2))dt
 = 2 [r/(r-2)] K^(2/r)`.

Fourier inversion yields a bounded continuous density and

`||p_R||_infinity
 <= (1/(2pi))*2[r/(r-2)]K^(2/r)
 = [r/(r-2)](M_E M_F)^(1/r)Delta_r(C)^(-1/r)`.

QED.

### Rank-three universal corollary

For `r=3`, the actual bounded-density product-projection theorem supplies

`M_E,M_F <= 2^(3/2)`

for arbitrary cap-one original coordinate laws. Therefore any physical split whose actual cross block has exact rank three satisfies

`boxed(||p_R||_infinity <= 6 Delta_3(C)^(-1/3))`,                  (2.3)

with a continuous density, regardless of the two arbitrary self-bank phases `H_I,H_J`.

This is strictly more flexible than the preceding grouped-Fresnel theorem in one direction: it uses the **actual cross block** `C` and permits completely arbitrary self-bank quadratic/linear terms. No selected spectral decomposition has to survive inside each self block.

For an exact-rank-three spectral form `A=U Lambda U^T`, if a split has frame operators

`S_I=U_I^T U_I`, `S_J=I-S_I`,

then its cross block `C=U_I Lambda U_J^T` has

`Delta_3(C)=|det Lambda| sqrt(det S_I det S_J)`.                  (2.4)

Thus if `S_I,S_J >= alpha I_3` and `|det Lambda|>=1`, (2.3) gives `||p_Q||_infinity<=6/alpha`, agreeing with the previous grouped-Fresnel constant but now through a direct cross-bank oscillatory payment.

## 3. Critical rank two gives a uniform half-Riesz potential

The partner account02/B16 obstruction identifies `|t|^-1` as the exact critical decay where plain Fourier inversion fails. At rank two, (2.1) gives precisely that decay, but the critical estimate is still strong enough after weighting by `|t|^-1/2`.

Assume now `rank(C)=2`, and put

`Delta_2(C)=sigma_1 sigma_2`.

Then

`|phi_R(t)| <= K |t|^-1`,
`K=pi (M_E M_F)^(1/2) Delta_2(C)^(-1/2)`.                        (3.1)

### Theorem 3.1 — `QFORM-CROSSBANK-HALF-RIESZ-v1`

For every real `a`,

`E |R-a|^(-1/2)
 <= 4 sqrt(2) (M_E M_F)^(1/4) Delta_2(C)^(-1/4)`.                 (3.2)

### Proof

In the distributional Fourier convention above,

`widehat(|x|^-1/2)(t)=sqrt(2pi)|t|^-1/2`.

The right side of

`(1/sqrt(2pi)) int_R |t|^-1/2 |phi_R(t)|dt`

is finite because of (3.1), so standard Riesz-potential regularization (truncate the kernel at zero and infinity, apply Fourier inversion, then pass monotonically/dominatedly to the limit) gives

`E|R-a|^-1/2
 <= (1/sqrt(2pi)) int_R |t|^-1/2 min(1,K/|t|)dt`.

The integral is exact:

`int_R |t|^-1/2 min(1,K/|t|)dt = 8 sqrt(K)`.

Substituting (3.1) gives

`E|R-a|^-1/2
 <= 8/sqrt(2pi) * sqrt(pi) (M_E M_F)^(1/4)Delta_2(C)^(-1/4)
 =4sqrt(2)(M_E M_F)^(1/4)Delta_2(C)^(-1/4)`.

QED.

Using the two-dimensional product-projection theorem `M_E,M_F<=2`, this simplifies to the source-universal grouped estimate

`boxed(sup_a E|R-a|^-1/2 <= 8 Delta_2(C)^(-1/4))`.               (3.3)

This is a bank-level fractional-trace estimate: the two original-coordinate groups may each contain arbitrarily many coordinates and arbitrary internal quadratic phases.

## 4. Spending one genuinely independent square bank

Let a third disjoint original-coordinate bank `K` produce a scalar random variable `L` independent of `(X_I,X_J)`, with density cap

`||p_L||_infinity<=M_3`.

Let `s=s(X_I,X_J)` be an arbitrary measurable real translation and let `gamma!=0`. Define

`Q=R + gamma [L+s(X_I,X_J)]^2`.                                  (4.1)

The translation is allowed to depend arbitrarily on the first two banks; only the innovation `L` itself must come from a disjoint source bank.

Conditioned on the first two banks, the variable `gamma(L+s)^2` has a density bounded by

`M_3 |gamma|^-1/2 |u|^-1/2`

on the appropriate sign half-line. Therefore `Q` has a density satisfying

`p_Q(t) <= M_3 |gamma|^-1/2 E|t-R|^-1/2`.

Combining with Theorem 3.1 gives:

### Theorem 4.1 — `QFORM-RANK2-CROSSBANK-TRANSLATED-SQUARE-v1`

`boxed(||p_Q||_infinity
 <= 4sqrt(2) M_3 |gamma|^-1/2
    (M_E M_F)^(1/4) Delta_2(C)^(-1/4))`.                          (4.2)

Under the universal source-projection caps `M_E,M_F<=2`,

`||p_Q||_infinity <= 8 M_3 |gamma|^-1/2 Delta_2(C)^(-1/4)`.       (4.3)

Now apply the **completed designated partner account02/B16 grouped-bank result** at an actual inequality: if `L` is a normalized linear projection of an arbitrary disjoint cap-one product bank, the partner's Ball--Rogozin step gives

`M_3<=sqrt(2)`.

Hence

`boxed(||p_Q||_infinity
 <= 8sqrt(2) |gamma|^-1/2 Delta_2(C)^(-1/4))`.                    (4.4)

This is the requested partner application: the partner's exact grouped source-projection cap supplies the final square-bank factor in the rank-two critical Fourier closure.

A concrete target-valid special case is

`Q=2X_1Y_1+2X_2Y_2+Z^2`,

for five independent cap-one scalar inputs. Here `M_E=M_F=M_3=1`, `Delta_2(C)=1`, `gamma=1`, and therefore

`||p_Q||_infinity <=4sqrt(2)`.                                    (4.5)

The coefficient matrix has eigenvalues `{1,1,1,-1,-1}`, so this is a genuine member of the target class, not a lower-rank toy.

If the translation `s` is deterministic (in particular zero), the final square bank is independent of `R`; convolution with its `L1` density and the finite half-Riesz bound gives a continuous density. For arbitrary base-dependent `s`, (4.2) proves essential boundedness; continuity is not claimed here.

## 5. What this pays and what remains

This run creates two complementary bank-level exits:

1. **rank-three physical cross bank:** direct `L2 x L2` bilinear Fourier smoothing gives a bounded continuous density, with the quantitative cost `6 Delta_3(C)^(-1/3)` under the universal projection theorem;
2. **rank-two physical cross bank plus one disjoint square innovation:** the critical `|t|^-1` decay is converted to a uniform half-Riesz potential and the third bank pays the missing half power, yielding (4.4).

These results directly address the `QFORM-GROUPED-L2-FRESNEL-CROSSBLOCK-v1` gap from the preceding B16 run. They preserve original-coordinate product provenance and never normalize a thin conditional spectral fiber.

The designated partner's harmonic family

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`

is the complementary zero-cross endpoint: account02/B16 already proves `||p_Qm||_infinity<=pi sqrt(2)` by grouping each rank-one bank before the curved square map, while its coordinatewise mixed-BL route is forced to the critical exponent. Together, these results show that rank 0/1 bank geometry and rank 2/3 cross-bank geometry can all be paid by product-preserving mechanisms in substantial structured cases.

The full conjecture is still OPEN. The first unpaid structural implication is now:

`QFORM-PRODUCT-PARTITION-TRICHOTOMY-v1`: from the bare assumption that `A` has at least three eigenvalues of modulus at least one, produce a physical partition that forces at least one quantitatively nondegenerate branch among

(a) a rank-three cross block with `Delta_3(C)` bounded below;
(b) a rank-two cross block with `Delta_2(C)` bounded below plus a disjoint square innovation of coefficient bounded below;
(c) a grouped rank-one-bank/same-sign-square configuration of the type paid by account02/B16;
(d) one of the already-proved ridge-window / physical-pair / heavy-pivot exits.

No such exhaustive partition theorem is proved here. Small cross singular values and overlapping high-leverage frames remain the genuine global obstacle. Full QFORM and full continuity therefore remain OPEN.
