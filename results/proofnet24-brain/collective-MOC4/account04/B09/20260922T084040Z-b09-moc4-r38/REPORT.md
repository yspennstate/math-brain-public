# account04/B09 MOC4 report — sharp one-third aligned-external cap on the genuine zero face

Run: `20260922T084040Z-b09-moc4-r38`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / not proved / not disproved**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Scope and fresh source state

Target: for every complex normal `4 x 4` pair `A,B` with spectra `a_i,b_i`, prove

`det(A+B) in conv{ prod_i (a_i+b_{sigma(i)}) : sigma in S_4 }`,

including singular and repeated spectra. This report concerns only the `n=4` target.

At invocation start I resolved `yspennstate/math-research-brain` main at
`155e49dfac91e21183ba89e61cf4321780a0a47f` and read `AGENTS.md`, the complete
revision `2026-09-22.2`; B09 remains assigned to MOC4 and older installation/benchmark
work remains stopped.

Latest complete team-lead report consumed:

- account03/B07 `20260922T074824Z-account03-B07-MOC4-r13`, report blob
  `7724d19f793eb934c5fcc2b469bb9d0a108da4eb` in `yspennstate/math-open-problems`;
- named result `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`: on a mixed-Schur pair boundary the
  pair-null vector is a full-Hessian null vector and the fourth-order Lyapunov-Schmidt
  gate acquires a nonnegative cross-Schur reserve. The lead leaves the generic MSQR
  and NDI cross-root closures open.

Required named OTHER-account partner consumed and applied:

- account01/B07 `20260922T070244Z-b07-moc4-r11`, report blob
  `711db07255ac0f3edc3562039d0b8d6f6e0e6d92`;
- named result `MOC4-EXTERNAL-SPINOR-HELLINGER-HOLE-v1` and its exact structured stress
  datum. It proves a general spinor metric hole around Drury external extremes, and gives
  an exact spectral support direction with a unique external value above the permutation
  maximum by `232716479/4000000000` while every other outer vertex is at most the endpoint
  maximum. This makes nonlinear same-unitary payment genuinely necessary.

Additional source pieces applied:

- account04/B07 `MOC4-SPIN6-COFACTOR-DEFICIT-v1`, blob
  `c28a23fd9a1234da762ac85a870870f1bba0092f`: in any Bogoliubov gauge the anti-linear
  block has singular values `(sqrt(lambda),sqrt(lambda),0)` and exact cofactor-deficit
  identities;
- account03/B09 `MOC4-SAXL-EXTERNAL-FACET-CLOSURE-v1`: the normalized positive-Saxl
  outer base has 24 Weyl vertices and 48 Drury external vertices with exact
  `P/R/D` coordinates;
- account01/B08 `MOC4-ZERO-FACE-COMMON-LIFT-FACET-NOGO-v1`, blob
  `f9708f0fe50da3eab74caca821d5d96737491062`: a true rational zero-entry orthogonal
  matrix can violate a facet of the pointwise common-compound permutation-lift polytope,
  so the zero-face proof cannot assume a universal common lift;
- account02/B07 `MOC4-MSQR-LS-SATURATION-MANIFOLD-v1` handoff at 08:23Z: exact pair-LS
  saturation integrates to an equality circle; double mixed saturation reduces to the
  existing zero-face obligation.

## 2. Conditional end-to-end location of the present step

Fix a support direction. If a positive-gap counterexample exists, the existing open-gap
argument permits generic spectra while preserving the same witness and direction; compactness
gives a genuine global maximizing unitary. The newest lead then splits the generic maximizer
into the MSQR and NDI branches. Several saturation mechanisms in the campaign reduce special
MSQR configurations to an equal-support zero-entry representative. On such a zero face, the
Saxl outer polytope contains only 18 Weyl vertices plus 12 external vertices aligned with the
zero singleton. The 18 Weyl vertices are target-safe. Therefore the exact zero-face
representation obstruction is to pay any support carried by those 12 aligned external
vertices, without assuming the now-refuted pointwise common-compound lift.

The first step below gives a **sharp same-unitary cap on the coefficient of each individual
aligned external vertex**. It uses both complementary channels, not merely a metric distance
of the anti-linear spinor block.

## 3. Canonical aligned external coordinates

By row/column relabeling and an even-even gauge, put the zero singleton at `(0,0)` and take
an aligned external vertex with

`tau=id`, `rho_tau=id`, `rho'=C=(1,2,0)`.

For Drury's external coordinate formulas,

`P_ext=(J_4-I_4)/3`,
`D_ext=-I_3/3`,
`R_ext=I_3/3 + 2 C/3`.

Writing the conformal and anti-conformal mass matrices

`q^+=(R+D)/2`, `q^-=(R-D)/2`,

gives exactly

`q^+_0 = C/3`,
`q^-_0 = (I+C)/3`.                                           (3.1)

Here `C` is the `3 x 3` permutation matrix of the 3-cycle. In particular `q^+_0` has
three positive entries, all equal to `1/3`, on one perfect matching.

## 4. Zero-face cofactor rigidity specialized to lambda=1

For a genuine point on this zero face, the selected anti-linear block `N` has

`||N||_F^2 = 2(1-P_00)=2`.

The Spin(6) singular-value theorem therefore has `lambda=1`: `N` is a rank-two partial
isometry. If

`r_alpha=sum_beta |n_{alpha beta}|^2`,
`c_beta=sum_alpha |n_{alpha beta}|^2`,

then the companion conformal block `M` is rank one and the prior exact zero-face cofactor
identity gives

`q^+_{alpha beta}=|m_{alpha beta}|^2=(1-r_alpha)(1-c_beta)`.   (4.1)

Set

`p_alpha=1-r_alpha`, `s_beta=1-c_beta`.

Because `sum r=sum c=2`, both `p` and `s` are probability vectors. Thus every genuine
zero-face point satisfies the exact factorization

`q^+ = p s^T`.                                                (4.2)

No simple-spectrum, nonzero-minor, invertibility, or genericity hypothesis is used here.

## 5. New theorem: sharp one-third coefficient cap

### `MOC4-ZERO-FACE-ALIGNED-EXTERNAL-ONE-THIRD-CAP-v1`

Take any normalized 72-vertex Saxl outer decomposition of a genuine zero-face point.
Fix one of the 12 external vertices aligned with that zero singleton, and let `lambda_0`
be its coefficient. Then

`boxed(lambda_0 <= 1/3)`.                                    (5.1)

The constant `1/3` is sharp even on the genuine Spin(6) locus.

### Proof

Normalize by symmetry to (3.1). Let the matching of `q^+_0=C/3` be
`beta=C(alpha)`. Every outer coordinate has nonnegative `q^+` entries. Hence, in any
convex outer decomposition,

`q^+_{alpha,C(alpha)} >= lambda_0/3`                           (5.2)

for each of the three rows. For a genuine zero-face point, (4.2) turns this into

`lambda_0 <= 3 p_alpha s_{C(alpha)}`                           (5.3)

for every `alpha`. Therefore

`lambda_0 <= 3 min_alpha p_alpha s_{C(alpha)}`.                (5.4)

But Cauchy-Schwarz gives

`sum_alpha sqrt(p_alpha s_{C(alpha)}) <= sqrt(sum p * sum s)=1`.

At least one of the three square roots is therefore at most `1/3`, so

`min_alpha p_alpha s_{C(alpha)} <= 1/9`.

Insert this into (5.4) to obtain `lambda_0<=1/3`. Relabeling proves the same statement
for every aligned external vertex. QED.

This is not a generic outer-polytope constant: the factorization (4.2) is the genuine
same-unitary zero-face input.

## 6. Sharpness and a decisive refutation of an anti-linear-only payment

The one-third constant cannot be improved using only the zero-face structural class.
Take

`N=(I-C)/sqrt(3)`, `M=J/3`.

Then, after clearing `sqrt(3)`,

`(I-C)(I-C)^T = 3I-J`,
`M M^T=J/3`,
`M(I-C)^T+(I-C)M^T=0`.

Thus the real Bogoliubov map `z -> Mz+N conjugate(z)` is orthogonal. On the constant
line, `M` acts as the identity and `N` vanishes; on its orthogonal real two-plane,
`M=0` and `(I-C)/sqrt(3)` has determinant one. Hence the real determinant is `+1`, so
this is a genuine `SO(6)` point and therefore has an `SU(4)` spin preimage.

Its masses are

`|N|^2=(I+C)/3=q^-_0`,
`|M|^2=J/9`.                                                   (6.1)

So the genuine point has **exactly the same anti-linear mass matrix as the external
vertex**. Therefore any proposed zero-face argument that tries to obtain a positive distance
from the aligned external face using `q^-` alone is false. The missing payment lives in the
companion channel and in the cross-gauge/spectral structure.

For this sharp point, the full two-channel `L1` distance from the external vertex is exactly

`||q^- - q^-_0||_1 + ||q^+ - q^+_0||_1 = 0 + 4/3 = 4/3`.      (6.2)

Moreover the exact verifier exhibits an outer decomposition with coefficient exactly `1/3`
on the chosen external vertex:

- weight `1/9` on Weyl permutations `(1,3,0,2)`, `(2,3,1,0)`, `(3,0,1,2)`;
- weight `1/3` on the chosen external `(tau=id,rho'=(1,2,0))`;
- weight `1/3` on the external `(tau=(0,2,3,1),rho'=id)`.

It reproduces both `q^+=J/9` and `q^-=(I+C)/3` exactly. Thus (5.1) is sharp, not merely
a loose estimate.

This is a source-valid **candidate refutation** only of the stronger anti-linear-only
external-hole mechanism; it is not a counterexample to MOC4.

## 7. Full-channel L1 hole (secondary exact corollary)

The same argument yields a robust metric statement useful for support payment.
For every genuine zero-face point and aligned external vertex,

`||q^- - q^-_0||_1 + ||q^+ - q^+_0||_1 >= 4/3`.              (7.1)

To prove it, put `t_alpha=s_{C(alpha)}` and
`delta=max(TV(p,u),TV(t,u))`, where `u=(1/3,1/3,1/3)`.
The row/column marginals of `q^-` give

`||q^- - q^-_0||_1 >= 2 delta`.                               (7.2)

Because `q^+=p s^T` and `q^+_0` is the uniform measure on one matching,

`||q^+-q^+_0||_1 = 2(1-S)`,
`S=sum_alpha min(p_alpha t_alpha,1/3)`.                        (7.3)

Let `m=(p+t)/2`. Since `p_alpha t_alpha<=m_alpha^2`,

`S <= sum min(m_alpha^2,1/3)`.

For every probability vector `m` on three points,

`sum min(m_alpha^2,1/3) <= 1/3 + TV(m,u)`.                    (7.4)

If all `m_alpha<=1/sqrt(3)`, this is
`sum m_alpha^2<=1/3+TV(m,u)`; writing deviations from `1/3`, the squared positive
deviations sum at most `delta_m^2` and the squared negative deviations at most
`delta_m/3`, hence at most `delta_m` in total because `delta_m<=2/3`.
If one coordinate `x>1/sqrt(3)`, the capped term is `1/3` and the other two squares are
at most `(1-x)^2 <= x-1/3 <= TV(m,u)`.
Finally `TV(m,u)<=delta`. Thus `S<=1/3+delta`, and (7.3) gives
`||q^+-q^+_0||_1>=4/3-2delta`. Combine with (7.2) to get (7.1).
The sharp construction in Section 6 attains equality.

## 8. Direct application to the assigned partner's exact stress datum

The account01/B07 stress direction has a unique external outer maximizer with

`M = 3654300159/1000000000`,
`E_0 = 2969983423/800000000`,
`E_0-M = 232716479/4000000000 > 0`,

and every other one of the 71 outer vertices is at most `M`.
If a zero-entry branch is not aligned with this unique bad external, that external is absent
from the 30 allowed zero-face vertices and the finite outer bound is already target-safe.
If it is aligned, theorem (5.1) gives the exact improved zero-face outer estimate

`h <= (1/3) E_0 + (2/3) M`

whenever only the single bad external is above `M`. Hence the residual outer excess is at most

`(E_0-M)/3 = 232716479/12000000000`.                           (8.1)

This is a factor-three reduction of the **entire** external excess, much stronger on the
zero face than the partner's general det-only metric exclusion. It still does not close this
stress direction because the runner-up is exactly `M`; coefficient exclusion alone cannot
remove a positive excess unless the bad coefficient is forced to zero or the required
companion vertices carry a quantified sub-`M` deficit.

The sharpness example explains exactly why that final directional payment must use more than
an individual coefficient cap: a genuine zero-face point can attain the `1/3` cap, but doing
so forces additional external/Weyl companions. On the partner stress datum, the explicit sharp
cap-saturating decomposition is in fact far below `M` because one forced companion external has
large negative support. Turning that phenomenon into a universal support-weighted inequality is
the remaining step rather than another metric constant.

## 9. Integration with the newest zero-face common-lift no-go

Account01/B08 now gives an exact true zero-entry orthogonal matrix that has no positive
common-compound permutation law. The present theorem does **not** assume such a law. It uses only:

1. the valid normalized Saxl outer decomposition (which always exists for the positive minor
   functional);
2. nonnegativity of its channel coordinates;
3. the genuine zero-face cofactor factorization `q^+=p s^T`.

Thus the one-third cap survives the B08 no-go and is compatible with its surviving target
`MOC4-ZERO-FACE-SPECTRAL-ROOF-v1`. In fact (5.1) identifies an exact nonlinear restriction that
any proof of that spectral roof can exploit.

## 10. First remaining implication

The exact next zero-face implication is now narrower:

`MOC4-ZERO-FACE-SPECTRAL-DIRECTIONAL-PAYMENT-v1`:

> For an actual spectral coefficient array and a genuine zero-entry global support maximizer,
> combine `q^+=p s^T`, the gauge-conjugate cofactor/hexagon identities, strict row/column pair
> reserves, and the weighted degree-two Birkhoff roof so that every aligned external excess is
> accompanied by enough sub-`M` support deficit to cancel it. The individual external coefficient
> is already sharply capped at `1/3`; no proof may assume it is smaller in general.

On the lead's generic interior branch, `MOC4-MSQR-CROSS-RESERVE-PAYMENT-v1` and
`MOC4-NDI-CROSS-ROOT-CLOSURE` remain open. This run does not silently replace those with the
zero-face result.

## 11. Exact verification

`verify_zero_face_external_hole.py` uses only Python standard-library exact `Fraction` arithmetic
for the `P/R/D` coordinates and all rational assertions. It verifies:

- the canonical aligned external formulas `q^+_0=C/3`, `q^-_0=(I+C)/3`;
- the scaled exact Bogoliubov identities for the sharp genuine point;
- exact full-channel distance `4/3` with zero anti-linear distance;
- all 30 zero-face allowed outer vertices (18 Weyl + 12 aligned external);
- exact outer-channel diameter `6` as a secondary check;
- the exact sharp outer decomposition attaining external coefficient `1/3`;
- an exact denominator-12 rational grid check of the analytic L1 lemma, whose minimum is `4/3` at uniform `p=s`;
- the partner stress residual factor `1/3`, namely `232716479/12000000000`.

Recorded stdout is in `verify_zero_face_external_hole.out`.

## 12. Failure / non-claims

- No full proof of MOC4 is claimed.
- No MOC4 counterexample is claimed.
- The sharp `SO(6)` construction refutes only an **anti-linear-only** external-hole mechanism;
  its full two-channel data are not the external vertex.
- The one-third cap is sharp, so merely improving that scalar constant cannot close the universal
  zero-face problem.
- The partner stress direction is narrowed but not closed by coefficient capping alone.
- No common positive permutation/compound lift is assumed.
- No literature-search miss is used as novelty evidence.
- Singular/repeated spectra remain part of the target; the new zero-face theorem itself has no
  spectral-gap denominator and is valid without genericity.

## Verdict

`ESSENTIAL_STEP_APPLIED`.

The run proves a sharp same-unitary `1/3` cap on every individual aligned Drury external
coefficient on a genuine zero face, gives an exact genuine Spin(6) saturator, and shows that the
anti-linear mass can coincide **exactly** with an external vertex—so any successful proof must use
the companion channel/cross-gauge spectral structure. This materially sharpens the remaining
zero-face spectral-payment obligation while preserving the open status of MOC4.
