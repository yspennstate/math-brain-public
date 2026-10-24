SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T23:16:52Z.
attacking: the grouped-rank-two endpoint logarithm by using an untouched physical kernel coordinate before any rotated-fiber endpoint estimate.

# account03/B09 r43 — physical-kernel endpoint removes the rank-two logarithm

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism  
Run: `20260923T231652Z-account03-B09-QFORM-r43`  
Status: **NEW SUPPORTING THEOREM, PENDING INDEPENDENT REVIEW; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and source state

The owner target remains: independent ORIGINAL-coordinate real random variables with scalar probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, log-concavity, iid, diagonal-basis, or post-rotation independence assumption is introduced.

The immediate predecessor is account03/B09 r42,

`yspennstate/math-open-problems@6642b95f1b9f447bdb961c5cbebe5b7d003faa20`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T215045Z-account03-B09-QFORM-r42/REPORT.md`.

For a physical triple `L`, an arbitrary-width disjoint right bank `J`, `rank C=2` for `C=A[L,J]`, unit `n in ker(C^T)`, `a=Pn`, `Delta=sigma_1(C)sigma_2(C)`, it proved the adaptive family

`||p_Q||_infinity <= C_p Delta^(-p/[2(p+1)]) ||a||^(-1/(p+1)), p>2`,

and, with the exact overlap currency

`V=Delta^2 ||a||^2`, `R=||a||^2/Delta`,

the logarithmic endpoint

`||p_Q||_infinity <=8.824 V^(-1/6)(1+log_+ R)^(1/3)`.

The unresolved issue was the logarithm as `p downarrow2`. The r42 stress family had `n=e_3`, `Delta=epsilon`, `a=epsilon^(-1)e_1`, so `V=1` but `R=epsilon^(-3)`. This run changes mechanism: when the rank-two cross bank has an **actual physical zero row**, the untouched physical coordinate lets one spend either a true linear slope or a true scalar square before any rotated conditional-density step.

Analytic inputs used at their exact stated scopes:

1. r42 and its r41 grouped right-bank factorization/Plancherel estimate.
2. The outer-square half-Riesz peel and rank-two crossing estimate recorded in account03/B12 r40, source `yspennstate/math-open-problems@23fbe7b2134155c764dff7eba9ad8540883befb0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T194742Z-qform-eigenvalue-r40/REPORT.md`.
3. Designated partner account04/B09 physical-cross theorem, source `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

Nothing below uses law-uniform pointwise van-der-Corput decay, an arbitrary-joint coarea bound, a conditional cap after rotating independent variables, deletion of a small quadratic term, or a universally large physical minor.

## 2. Physical-kernel normal form

Let `L={1,2,3}` and `J` be disjoint sets of ORIGINAL coordinates. Condition on every original coordinate outside `L union J`; this only creates affine terms. Write

`Q=Y^T P Y+2Y^T C Z+G(Z)+ell^T Y+const`,                         (2.1)

where `Y=(X_1,X_2,X_3)`, `Z=X_J`, the three coordinates of `Y` remain mutually independent and independent of `Z`, and `G` is an arbitrary quadratic-affine polynomial on the whole right bank.

Assume

`rank C=2`,                                                       (2.2)

and, after a permutation of the three ORIGINAL left coordinates,

`C^T e_3=0`.                                                      (2.3)

Thus the common rank-two kernel is literally the physical coordinate direction

`n=e_3`.                                                          (2.4)

Let

`Delta=sigma_1(C)sigma_2(C)>0`,                                  (2.5)

and write the third physical column of `P` as

`a=P e_3=(p_1,p_2,d)^T`.                                         (2.6)

Set

`A0=||a||_2`, `p_infty=max(|p_1|,|p_2|)`,
`V=Delta^2 A0^2`, `R=A0^2/Delta`.                                (2.7)

The branch below assumes `A0>0`; `A0=0` is outside this supporting theorem.

Because the kernel is physical, no rotation of the left random variables is needed. Put

`U=(X_1,X_2)`, `X=X_3`.                                          (2.8)

The cross term involves `U` and `Z` only.

Factor the two-row cross matrix as in r41,

`C_[1,2],J=L_0 R_0^T`, `R_0^T R_0=I_2`, `det L_0=Delta`.         (2.9)

For the genuine projection `V_R=R_0^T Z`, the reviewed projection theorem gives density cap at most two. Pushing the complex measure `exp(itG(Z))dP_Z` onto `V_R` gives a complex density `b_t` with

`||b_t||_2<=sqrt(2)`.                                             (2.10)

Exactly as in r41, if

`F_u(t)=f_1(u_1)f_2(u_2) int f_3(x)
 exp(it[d x^2+2(p_1u_1+p_2u_2)x+beta x]) dx`                    (2.11)

(up to an irrelevant unit-modulus `u`-phase), and

`A(t)^2=int_R2 |F_u(t)|^2 du`,                                   (2.12)

then two-dimensional bilinear Plancherel gives

`boxed:
 |phi_Q(t)| <= pi sqrt(2) Delta^(-1/2)|t|^(-1) A(t).`            (2.13)

All same-bank quadratic terms remain inside unit-modulus phases.

## 3. New physical-slope endpoint

The key gain is that in the physical-kernel case the left density in (2.11) is still the exact product `f_1 f_2 f_3`, rather than a merely bounded rotated joint density.

### Lemma 3.1 — physical-slope `L^2` budget

If `p_infty>0`, then for every `t!=0`,

`boxed:
 A(t)^2 <= pi/(|t| p_infty).`                                    (3.1)

### Proof

Assume without loss of generality `p_infty=|p_1|>0`. Define

`g_t(x)=f_3(x) exp(it d x^2)`                                    (3.2)

and use the angular Fourier convention

`hat g_t(xi)=int g_t(x)e^{i xi x} dx`.                            (3.3)

For fixed `u_2`, the inner integral in (2.11) is

`hat g_t(2t p_1u_1+2t p_2u_2+t beta)`.                           (3.4)

Therefore, using only `f_1^2<=1`,

`int f_1(u_1)^2 |hat g_t(2t p_1u_1+c)|^2 du_1
 <= [1/(2|t p_1|)] int |hat g_t(xi)|^2 dxi`.                    (3.5)

Plancherel and `f_3<=1`, `int f_3=1`, give

`int |hat g_t|^2=2pi int f_3^2 <=2pi`.                           (3.6)

Hence (3.5) is at most `pi/(|t p_1|)`. Finally

`int f_2(u_2)^2 du_2<=1`,                                        (3.7)

which proves (3.1). The quadratic chirp `exp(itd x^2)` is kept exactly; it costs nothing because it has modulus one in (3.6). QED.

Combining (2.13) and (3.1),

`|phi_Q(t)|
 <= pi^(3/2) sqrt(2)
    Delta^(-1/2)p_infty^(-1/2)|t|^(-3/2).`                       (3.8)

Together with `|phi_Q(t)|<=1`, the majorant is integrable. If

`B=pi^(3/2)sqrt(2) Delta^(-1/2)p_infty^(-1/2)`,                  (3.9)

then

`(1/(2pi)) int_R min(1,B|t|^(-3/2)) dt
 = (3/pi) B^(2/3)`.                                               (3.10)

Thus:

### Theorem 3.2 — physical-slope receiver

If `p_infty>0`, the law of `Q` has a bounded continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <=3*2^(1/3) Delta^(-1/3)p_infty^(-1/3).`                        (3.11)

Equivalently every interval `I` obeys

`P{Q in I}<=3*2^(1/3)(Delta p_infty)^(-1/3)|I|`.                 (3.12)

This is a genuine endpoint estimate: there is no `p>2`, no `epsilon^-1/3`, and no logarithm.

## 4. Complementary scalar-square receiver

If `d!=0`, isolate the untouched original scalar `X=X_3`. Since the third physical cross row is exactly zero, its coefficient contains no right-bank variable:

`Q=d X^2+2X L(U)+R_base(U,Z)`,                                   (4.1)

where `L(U)` is affine in the two physical coordinates `U` (and in already conditioned outside constants) and is independent of `X`. Completing the square gives

`Q=d[X+L(U)/d]^2+R(U,Z)`.                                        (4.2)

Crucially, the residual `U`-to-`Z` cross matrix is still exactly `C_[1,2],J`; the square completion changes only the `U`-side quadratic/affine part.

For this residual, the two-row physical crossing estimate gives

`|phi_R(t)|<=min(1, pi sqrt(2) Delta^(-1/2)|t|^(-1)).`           (4.3)

The source-valid half-Riesz identity is

`H_(1/2)(R)
 <=(2pi)^(-1/2) int_R |t|^(-1/2)|phi_R(t)|dt`.                   (4.4)

Writing `A=pi sqrt(2)Delta^(-1/2)`, the integral in (4.4) is

`2[int_0^A t^(-1/2)dt + A int_A^infinity t^(-3/2)dt]
 =8 sqrt(A)`.                                                     (4.5)

Therefore

`boxed:
 H_(1/2)(R)<=2^(11/4) Delta^(-1/4).`                             (4.6)

The outer-square peel yields

`boxed:
 ||p_Q||_(infinity,ess)
 <=2^(11/4)|d|^(-1/2)Delta^(-1/4).`                              (4.7)

This is an `O(|I|)` interval bound. The cited square-peel theorem establishes essential boundedness here; this report does **not** upgrade this subbranch to continuity.

## 5. Pure overlap bound: the r42 logarithm disappears for a physical kernel

We now combine the new slope endpoint, the scalar-square endpoint, and r42 only in the benign low-anisotropy chamber.

Recall

`V=Delta^2 A0^2`, `R=A0^2/Delta`.                                (5.1)

### Theorem 5.1 — `QFORM-GROUPED-RANK2-PHYSICAL-KERNEL-ENDPOINT-v1`

Under (2.1)-(2.7), with `A0>0`,

`boxed:
 ||p_Q||_(infinity,ess) <=8 V^(-1/6).`                           (5.2)

Consequently

`boxed:
 P{Q in I}<=8 V^(-1/6)|I|`                                      (5.3)

for every interval `I`.

Proof. There are three exhaustive cases.

**Case A: `R<=1`.** Apply r42 with `p=3`:

`||p_Q||_infinity
 <=C_3 V^(-1/6) R^(1/24)
 <=6.871566676 V^(-1/6)<8V^(-1/6)`.                              (5.4)

This branch has a continuous density.

**Case B: `R>1` and `sqrt(p_1^2+p_2^2)>=A0/sqrt(2)`.** Then

`p_infty>=A0/2`.                                                  (5.5)

Using (3.11),

`||p_Q||_infinity
 <=3*2^(1/3) Delta^(-1/3)p_infty^(-1/3)
 <=3*2^(2/3) V^(-1/6)
 =4.762203156... V^(-1/6)<8V^(-1/6)`.                            (5.6)

This branch also has a continuous `C_0` density.

**Case C: `R>1` and `sqrt(p_1^2+p_2^2)<A0/sqrt(2)`.** Then

`|d|>A0/sqrt(2)`.                                                 (5.7)

From (4.7), divided by `V^(-1/6)=Delta^(-1/3)A0^(-1/3)`,

`||p_Q||_(infinity,ess)/V^(-1/6)
 <=2^(11/4) Delta^(1/12)A0^(1/3)|d|^(-1/2)`
`=2^(11/4)(A0/|d|)^(1/2)R^(-1/12)`
`<2^(11/4)2^(1/4)=8`.                                            (5.8)

This closes the final case. QED.

The theorem is homogeneous and pays the exact r41 one-index-overlap currency `V` with the scale-correct exponent `-1/6`, with no anisotropy logarithm.

Continuity statement: Cases A and B are continuous. Case C is only asserted to have an essentially bounded density by the cited outer-square theorem. Hence Theorem 5.1 as a whole establishes essential boundedness, not full continuity.

## 6. The r42 high-anisotropy stress family is uniformly closed

For the r42 five-coordinate family

`P_epsilon=[[0,0,epsilon^(-1)],
            [0,1,0],
            [epsilon^(-1),0,0]]`,

`C_epsilon=[[1,0],[0,epsilon],[0,0]]`,                            (6.1)

we have exactly

`n=e_3`, `Delta=epsilon`, `a=epsilon^(-1)e_1`,
`V=1`, `R=epsilon^(-3)`.                                         (6.2)

The physical-slope endpoint applies with

`p_infty=epsilon^(-1)`.                                          (6.3)

Therefore for every `0<epsilon<1`,

`boxed:
 ||p_Q||_infinity
 <=3*2^(1/3)
 =3.779763149684619... .`                                        (6.4)

This is continuous and uniform as `epsilon downarrow0`, whereas the adaptive r42 estimate grew like `(log R)^(1/3)`. Thus the r42 logarithm is an artifact in this exact physical-kernel high-anisotropy family, not a necessary loss there.

The target-valid spectrum remains the r42 spectrum:

`+/-sqrt(1+epsilon^(-2)), 0,
 [1+sqrt(1+4epsilon^2)]/2,
 [1-sqrt(1+4epsilon^2)]/2`,                                      (6.5)

so at least three eigenvalues have modulus at least one.

## 7. Designated account04/B09 partner applied to an actual inequality

The completed partner theorem states that a literal invertible physical `3x3` cross block `K` gives

`||p_Q||_infinity<=3|det K|^(-1/3)`                              (7.1)

with arbitrary dense same-side curvature and a continuous density.

Apply it to the six-coordinate target-valid matrix

`A_partner=[[0,K],[K,0]]`, `K=diag(1,2,3)`.                      (7.2)

The spectrum is

`{-3,-2,-1,1,2,3}`                                               (7.3)

and `det K=6`. Hence the partner theorem gives the actual final-law inequality

`boxed:
 ||p_Q||_infinity<=3*6^(-1/3)
 =1.650963624447313... ,`                                        (7.4)

and

`P{Q in I}<=3*6^(-1/3)|I|`,                                     (7.5)

with a continuous density.

## 8. What changed and what remains open

The r42 endpoint debt is now strictly smaller. The logarithm has been removed whenever the common kernel of the grouped rank-two physical cross bank is itself an ORIGINAL coordinate direction. This includes the explicit family that proved `R` can be arbitrarily large under the full target spectral hypothesis.

The remaining same-target B09 obstruction is therefore not simply `R>>1`; it is

`QFORM-GROUPED-RANK2-NONPHYSICAL-KERNEL-ENDPOINT-v1`:

> remove the logarithm, or route to an already-paid physical receiver, when the rank-two kernel `n` has support on more than one original coordinate. The next proof should preserve the exact product structure rather than treating the rotated kernel coordinate as independent. A promising route is to exploit a physical coordinate with large `|n_i|` and compare the actual cross row to the two-row quotient before applying the physical-slope/square dichotomy above.

No claim is made that every target matrix contains an exact physical-kernel rank-two packet. Full unrestricted QFORM remains **OPEN**, and full-target continuity remains **OPEN**.

## 9. Deterministic checks

The accompanying checker verifies:

- `3*2^(1/3)=3.779763149684619...`;
- the combined transverse constant `3*2^(2/3)=4.762203155904598...`;
- the scalar combined constant in Case C is exactly `8`;
- the partner value `3*6^(-1/3)=1.650963624447313...`;
- the r42 stress-family spectrum for several `epsilon` values and `V=1` exactly up to floating-point error.

These checks validate arithmetic and algebra only; they are not substitutes for the analytic proof.

## 10. Status

This is a supporting theorem, not a full solution. Independent end-to-end review of the new endpoint argument has not yet been recorded. Repository transport/readback is separate from native learned-memory ingestion; absent a genuine current-run receiver event the execution label remains `WITHOUT_VERIFIED_BRAIN`.
