SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-24T06:29:16Z.
attacking: fixed-source continuity on the uniformly paid ruled majority sheet by combining account02/B15's sharp submass stability with original-coordinate Gaussian mollification; derive an explicit local modulus without promoting it to a class-uniform modulus.

# account01/B15 — submass stability compiles to a half-line C0 representative

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`; current protected OWNER CONTROL revision `2026-09-22.15`.
Run: `20260924T062916Z-account01-B15-QFORM-auto11-r1`.
Status: **NEW TARGET-LEVEL REGULARITY COMPILER / RULED MAJORITY-SHEET C0 PROVED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

Fresh brain controls were resolved from main before substantive work. The latest designated-partner theorem actually used is account02/B15 at `yspennstate/math-open-problems@45779cb1dca5f453ac620431b380ad015a052e70`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260924T050354Z-account02-B15-QFORM-auto11-r1/REPORT.md`.

The live corrections are preserved: no law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, no projection-only/X-ray closure, and no use of continuity to manufacture the central density height.

## 1. Abstract compiler: submass height stability implies rough-source continuity

Let `T:R^n->R` be measurable and let `U subset R` be a fixed output region. For product inputs define the restricted pushforward

`nu_F^U(B)=int 1_{T(x) in B cap U} prod_i f_i(x_i) dx`.

Assume that for some `alpha in (0,1]` and `C<infinity`, every coordinate `j`, every cap-one probability choice of the other factors, and every cap-one subdensity `g` in coordinate `j` of mass `m`, the restricted output submeasure satisfies

`H(nu_g^U):=sup_I nu_g^U(I)/|I| <= C m^alpha`.      (1.1)

Then:

### Lemma 1.1 — one-coordinate stability

If `f_j,g_j` are cap-one probability densities, all other marginals are fixed, and `delta=||f_j-g_j||_1`, then the two restricted output measures have essentially bounded densities `p_f^U,p_g^U` with

`||p_f^U-p_g^U||_infinity <= 2^(1-alpha) C delta^alpha`.      (1.2)

Proof. Write `f_j-g_j=h_+-h_-`. Since both have mass one,
`int h_+=int h_-=delta/2`. Apply (1.1) to the two positive subdensities and subtract. Each output subdensity has height at most `C(delta/2)^alpha`; summing proves (1.2). No continuity enters.

### Lemma 1.2 — multi-coordinate stability

For two cap-one product laws `F=prod f_i`, `G=prod g_i`, telescoping one coordinate at a time gives

`||p_F^U-p_G^U||_infinity <= 2^(1-alpha) C sum_i ||f_i-g_i||_1^alpha`.      (1.3)

The intermediate product laws remain cap-one, so the one-coordinate estimate applies at every step.

### Lemma 1.3 — regularity compilation

Suppose for a fixed product source `F` there are cap-one product approximants `F_eta=prod f_{i,eta}` with `||f_{i,eta}-f_i||_1->0`, and suppose the restricted output densities `p_eta^U` admit continuous representatives on `U`. If the submass hypothesis (1.1) holds, then `p_eta^U` is uniformly Cauchy on every set on which the representatives are defined, and the restricted rough output has a continuous representative there.

Indeed, applying (1.3) to two approximants gives

`||p_eta^U-p_zeta^U||_infinity <= 2^(1-alpha) C sum_i ||f_{i,eta}-f_{i,zeta}||_1^alpha ->0`.

Thus the continuous representatives converge uniformly. The limiting function represents the rough restricted pushforward because deterministic pushforward contracts total variation and the product densities converge in `L1`.

This is the regularity mechanism needed below: **submass control, not continuity, pays the height; continuity is a consequence of uniform source stability plus a smooth approximation.**

## 2. Apply account02/B15 to the isotropic ruled majority sheet

Let `R` be `n x 3` with orthonormal columns and define

`Y=R^T X`,
`q(X)=Y_1^2+Y_2^2-Y_3^2`.

The completed account02/B15 theorem proves two facts for arbitrary independent cap-one original-coordinate marginals:

1. probability-input majority-sheet height

`Pr{q(X) in I, q(X)>=0} <= pi sqrt(2) |I|`;      (2.1)

2. cap-one subdensity theorem: if one original-coordinate factor is replaced by a subdensity of mass `m`, then

`H(nu_g^+) <= 20 sqrt(2) sqrt(m)`.      (2.2)

Thus (1.1) holds on `U=[0,infinity)` with

`alpha=1/2`, `C=20 sqrt(2)`.

Lemma 1.1 therefore reproduces the partner's sharp-exponent marginal stability

`||r_f^+-r_g^+||_infinity <= 40 ||f_j-g_j||_1^(1/2)`,      (2.3)

and Lemma 1.2 gives, for arbitrary two cap-one product laws,

`||r_F^+-r_G^+||_infinity <= 40 sum_j ||f_j-g_j||_1^(1/2)`.      (2.4)

The main new point is that (2.4) is strong enough to **force continuity for every rough source on the paid majority sheet**, after a specific original-coordinate mollification.

## 3. Original-coordinate Gaussian mollification keeps product structure and creates isotropic spectral smoothing

Let `phi_eta` be the centered one-dimensional Gaussian density with variance `eta^2`, and set

`f_{j,eta}=f_j*phi_eta`.

Then each `f_{j,eta}` remains a probability density with `0<=f_{j,eta}<=1`, the original coordinates remain independent, and

`delta_j(eta):=||f_{j,eta}-f_j||_1 ->0`.      (3.1)

Equivalently, with `G~N(0,I_n)` independent of `X`,

`X_eta = X + eta G`.

Because `R^T R=I_3`,

`Y_eta=R^T X_eta=Y+eta Z`,

where `Z~N(0,I_3)` is independent of `Y`. This is not a rotated-independence claim about `Y`; it is an exact statement only about the added independent Gaussian noise.

Let `r_eta^+` be the majority-sheet density of `q(X_eta)`. From (2.4),

`||r_eta^+-r^+||_infinity <= 40 sum_j sqrt(delta_j(eta))`.      (3.2)

Here `r^+` denotes the rough majority-sheet density, initially only as an `L^infinity` equivalence class.

## 4. The Gaussian-smoothed majority-sheet density has an explicit square-root modulus

The partner's ruled formula gives, for `s>0`,

`r_eta^+(s) = (1/(2 sqrt(2))) int_0^(2pi) h_{theta,eta}(sqrt(s) u_theta) dtheta`,      (4.1)

where `u_theta` is a unit vector in `R^2` and `h_{theta,eta}` is the two-dimensional density of an orthogonal projection of `Y_eta` onto the plane normal to the ruling direction.

Since `Y_eta=Y+eta Z` with isotropic Gaussian `Z`, every such projected density has the form

`h_{theta,eta}=mu_theta * gamma_{eta,2}`,      (4.2)

where `mu_theta` is a probability measure and

`gamma_{eta,2}(x)=(2 pi eta^2)^(-1) exp(-|x|^2/(2 eta^2))`.

Hence

`||grad h_{theta,eta}||_infinity <= ||grad gamma_{eta,2}||_infinity
 = exp(-1/2)/(2 pi eta^3)`.      (4.3)

Indeed `|grad gamma_{eta,2}(x)| = |x| (2 pi eta^4)^(-1) exp(-|x|^2/(2eta^2))`, maximized at `|x|=eta`.

Using (4.1)--(4.3), for every `s,t>0`,

`|r_eta^+(s)-r_eta^+(t)|
 <= (1/(2 sqrt(2))) (2pi) [exp(-1/2)/(2pi eta^3)] |sqrt(s)-sqrt(t)|`

and therefore

`boxed(|r_eta^+(s)-r_eta^+(t)| <= exp(-1/2)/(2 sqrt(2) eta^3) |sqrt(s)-sqrt(t)|)`.      (4.4)

Because `|sqrt(s)-sqrt(t)| <= sqrt(|s-t|)`, each `r_eta^+` is uniformly continuous on `(0,infinity)` and has a finite right limit at zero. Define that limit as `r_eta^+(0)`. Then (4.4) continues to hold for all `s,t>=0`.

Also `r_eta^+` is integrable on `[0,infinity)`. A nonnegative uniformly continuous integrable function must vanish at infinity. Hence

`r_eta^+ in C_0([0,infinity))`.      (4.5)

Here `C_0([0,infinity))` means continuous on the closed half-line and vanishing at `+infinity`; no assertion is made that extension by zero to the negative half-line is continuous at zero.

## 5. New theorem — rough majority-sheet C0 with the same universal height

Combining (3.2) and (4.4) gives, after choosing the canonical continuous representative obtained as the uniform limit of the Gaussian-smoothed outputs,

`boxed(
|r^+(s)-r^+(t)|
 <= 80 sum_j sqrt(delta_j(eta))
    + exp(-1/2)/(2 sqrt(2) eta^3) |sqrt(s)-sqrt(t)|
)`      (5.1)

for every `eta>0` and every `s,t>=0`.

Since each `delta_j(eta)->0` for fixed finite `n`, (5.1) proves that `r^+` is uniformly continuous on `[0,infinity)`. Uniform convergence of `r_eta^+` also gives vanishing at infinity. Thus:

### Theorem 5.1 — `QFORM-RULED-MAJORITY-HALFLINE-C0-v1`

For arbitrary independent cap-one original-coordinate densities and every orthonormal rank-three frame `R`, the majority-sheet output submeasure of

`q(X)=<r_1,X>^2+<r_2,X>^2-<r_3,X>^2`

has a canonical representative

`boxed(r^+ in C_0([0,infinity)),   ||r^+||_infinity <= pi sqrt(2)).`      (5.2)

The universal height `pi sqrt(2)` is still paid by the completed ruled interval theorem (2.1); continuity is obtained later from submass stability and original-coordinate Gaussian smoothing and therefore costs **zero additional height**.

Moreover (5.1) is a fixed-source quantitative modulus. It is intentionally source dependent through the `L1` mollification errors `delta_j(eta)`.

This source dependence is necessary: the preceding account01/B15 theorem `QFORM-NO-UNIVERSAL-C0-MODULUS-EVEN-SMOOTH-v1` gives a fixed exact-target matrix `A=I_3` and smooth compactly supported cap-one sources with uniformly bounded output height but no class-uniform modulus of continuity.

## 6. Actual owner-target inequality from the completed partner theorem

Take

`Q=2XY+Z^2`

for arbitrary independent cap-one `X,Y,Z`. Its symmetric matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`

with eigenvalues `{1,-1,1}`, so this is an exact owner-target form.

The completed partner theorem gives the real interval inequality

`boxed(Pr{Q in I, Q>=0} <= pi sqrt(2) |I|).`      (6.1)

The new theorem upgrades this, without changing the constant, to

`boxed(p_Q|_[0,infinity) has a representative in C_0([0,infinity)),
       sup_{s>=0} p_Q^+(s) <= pi sqrt(2)).`      (6.2)

For Gaussian-mollified marginals define

`delta_X(eta)=||f_X-f_X*phi_eta||_1`, etc. Then for all `s,t>=0`,

`boxed(
|p_Q^+(s)-p_Q^+(t)|
 <=80( sqrt(delta_X(eta))+sqrt(delta_Y(eta))+sqrt(delta_Z(eta)) )
 + exp(-1/2)/(2 sqrt(2) eta^3) |sqrt(s)-sqrt(t)|.
)`      (6.3)

This is an actual target-level regularity estimate for arbitrary rough cap-one inputs. It proves a right-continuous value at zero and uniform continuity on the full majority half-line.

## 7. What this does and does not settle

This run sharpens the implication hierarchy:

1. **Absolute continuity.** For any nonzero quadratic form and any absolutely continuous joint input, qualitative absolute continuity is much easier than the owner target and supplies no universal height.
2. **Essential boundedness.** On the ruled majority sheet, the partner interval estimate pays the universal height `pi sqrt(2)` directly.
3. **Rough-source stability.** The submass theorem yields the optimal exponent `1/2` for marginal `L1 -> output L^infinity` stability.
4. **Continuity.** That stability is strong enough to transfer the smooth Gaussian-mollified representatives uniformly to the rough source, giving `C_0([0,infinity))` with the identical height constant.
5. **No universal modulus.** The modulus necessarily depends on the source approximation errors; the bare target admits no class-uniform modulus even for smooth inputs.

The missing implication is still on the complementary two-sheet/convex side and then the global arbitrary-matrix structural passage. If an analogous cap-one submass estimate

`H(nu_g^-) <= C sqrt(m)`

were proved for the two-sheet side with one universal `C`, the same compiler would immediately provide a continuous representative on the negative half-line as well. Matching the two one-sided limits at zero would then be the only remaining local regularity issue for the isotropic rank-three indefinite form. None of this closes the global height theorem for arbitrary `A` with `s_3(A)>=1`.

## 8. Corrections and provenance

- no pointwise quadratic Fourier decay is used;
- original-coordinate independence is preserved throughout; spectral coordinates are not declared independent;
- Gaussian isotropy is used only for the **added independent noise**, via `R^T G~N(0,I_3)`;
- no projection-only/X-ray norm is used to pay the missing two-sheet side;
- continuity is proved strictly downstream of the already-paid interval/L-infinity estimate;
- full QFORM remains `OPEN / NOT PROVED`.
