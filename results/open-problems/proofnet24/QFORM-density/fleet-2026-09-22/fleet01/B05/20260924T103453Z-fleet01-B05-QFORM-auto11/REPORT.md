SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-24T10:34:53Z.
attacking: QFORM-INDEFINITE-PAIR-L3-v1 — prove the scale-correct L^3 density bound for every physical 2x2 indefinite quadratic pair, then spend an actually independent third square by Young convolution.

# fleet01/B05 auto11 — full indefinite-pair L3 receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bound preserving arbitrary product densities.  
**Status:** `NEW SUPPORTING ANALYTIC THEOREM / PREVIOUS L3 DEBT CLOSED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

Let `U,V` be independent real random variables with probability densities bounded by `m_U,m_V`, and let

`B=[[a,t],[t,b]]`

be symmetric, invertible and indefinite. Put `D=|det B|=t^2-ab>0`. For arbitrary affine terms `2 ell_1 U+2 ell_2 V+c`, define

`F=(U,V) B (U,V)^T+2 ell dot (U,V)+c`.

Then `F` has a density in `L^3(R)` and

`boxed: ||p_F||_3 <= C_pair D^(-1/3) (m_U m_V)^(2/3),`       (1.1)

where `C_pair<infinity` is a universal numerical constant. One admissible constant is

`C_pair=max( 2^(1/3) C_log, (4/3)^(1/3) C_HLS C_sq )`,       (1.2)

with

`C_log=[256+2 I]^(1/3)=7.78606602367...`,
`I=(2sqrt(2)+log 2)^3+3(2sqrt(2)+log 2)^2+6(2sqrt(2)+log 2)+6`,
`C_sq=[(5/4)2^(1/5)]^(5/6)=1.351...`,

and `C_HLS` the finite universal operator norm in the classical one-dimensional Hardy--Littlewood--Sobolev estimate

`|| |.|^(-1/2)*h ||_3 <= C_HLS ||h||_(6/5)`.                (1.3)

The first constant in (1.2) is explicit:

`2^(1/3) C_log = 9.80982847909...`.                         (1.4)

No support, moment, Gaussian, log-concavity, connected-support, or post-rotation independence assumption is used.

This closes the exact missing implication `QFORM-INDEFINITE-PAIR-L3-v1` left by the preceding fleet01/B05 run.

## 2. Reduction to cap-one and homogeneous form

Coordinatewise translations by the deterministic vector `B^{-1} ell` remove the affine term and preserve independence and density caps. Output translation removes the resulting critical value. Thus it is enough first to prove (1.1) for

`F=aU^2+2tUV+bV^2`                                                  (2.1)

with cap-one inputs.

The general density caps follow afterwards by setting

`U'=m_U U`, `V'=m_V V`.

The transformed inputs have density caps at most one and the transformed quadratic matrix is

`B'=diag(m_U^{-1},m_V^{-1}) B diag(m_U^{-1},m_V^{-1})`,

so

`|det B'|=D/(m_U^2 m_V^2)`.                                         (2.2)

Therefore a cap-one estimate `C_pair |det B'|^{-1/3}` is exactly (1.1).

## 3. Well-conditioned pair: integrate the completed logarithmic coarea envelope

Let

`kappa=sigma_min(B)`.

Use the completed product-preserving physical-pair logarithmic envelope from

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:`
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For every cutoff `r>0`, after centering at the critical output value `t_0`, it gives almost everywhere

`p_F(t) <= 2sqrt(2)/r + D^(-1/2) log_+(2r^2/(kappa |t-t_0|)).`        (3.1)

This theorem is proved directly in the two ORIGINAL coordinates; the diagonalization inside its proof is only a Lebesgue-measure change of variables and does not assert probabilistic independence after rotation.

Set

`A=2sqrt(2)`, `u=|t-t_0|`, `u_0=D/kappa`.

For `0<u<=u_0`, choose `r=sqrt(D)` in (3.1). Then

`p_F(t) <= D^(-1/2)[A+log(2u_0/u)].`                                (3.2)

For `u>u_0`, choose `r=sqrt(kappa u/2)`. The logarithmic term vanishes and

`p_F(t) <= 4/(sqrt(kappa) sqrt(u)).`                                 (3.3)

Since

`int_0^1 [A+log(2/x)]^3 dx
 =(A+log2)^3+3(A+log2)^2+6(A+log2)+6=:I,`                            (3.4)

integration of the two sides of the critical value gives

`int_{|t-t_0|<=u_0} p_F(t)^3 dt
 <= 2 I /(kappa sqrt(D)).`                                           (3.5)

Similarly, (3.3) gives

`int_{|t-t_0|>u_0} p_F(t)^3 dt
 <=256/(kappa sqrt(D)).`                                             (3.6)

Hence

`boxed: ||p_F||_3 <= C_log kappa^(-1/3) D^(-1/6).`                  (3.7)

In particular, if

`kappa >= (1/2) sqrt(D)`,                                            (3.8)

then

`boxed: ||p_F||_3 <= 2^(1/3) C_log D^(-1/3)
                   =9.80982847909... D^(-1/3).`                     (3.9)

Thus every well-conditioned indefinite physical pair is paid with the correct determinant scale.

## 4. Ill-conditioned pair: a large physical diagonal is forced

Now suppose

`kappa < (1/2) sqrt(D)`.                                             (4.1)

Let the two eigenvalues of the indefinite symmetric matrix have magnitudes `L>=kappa`. Since `L kappa=D`,

`L=D/kappa>2sqrt(D)`.                                                 (4.2)

Because the eigenvalues have opposite signs,

`|tr B|=L-kappa>(3/2)sqrt(D)`.                                      (4.3)

Consequently

`max(|a|,|b|) >= |a+b|/2 > (3/4)sqrt(D).`                           (4.4)

Thus ill-conditioning cannot coexist with two small ORIGINAL-coordinate diagonals. We exploit whichever diagonal is large without rotating the random inputs.

## 5. Root formula plus one-dimensional HLS

Assume first that

`|b| >= (3/4)sqrt(D)`.                                               (5.1)

For fixed `U=x`, the equation

`a x^2+2txy+b y^2=z`

has discriminant

`4(Dx^2+bz)`.                                                        (5.2)

At either root the absolute derivative in the ORIGINAL `y` coordinate is

`2 sqrt(Dx^2+bz)`.

Since the density of `V` is at most one, summing the at most two roots gives the exact conditional/coarea majorant

`p_F(z) <= int f_U(x) [D x^2+bz]_+^(-1/2) dx.`                      (5.3)

No conditional projected-density estimate is used.

Let `R=X^2`. Its density on `(0,infinity)` is

`rho(r^2)=[f_U(r)+f_U(-r)]/(2r)`.

Writing `G(r)=f_U(r)+f_U(-r)`, we have `0<=G<=2` and `int_0^infinity G=1`. Therefore

`int rho(s)^(6/5) ds
 =2^(-1/5) int_0^infinity G(r)^(6/5) r^(-1/5) dr
 <=(5/4)2^(1/5).`                                                    (5.4)

The last step is the elementary bathtub bound: `G^(6/5)<=2^(1/5)G`, and a density bounded by `2` maximizes the decreasing weight `r^(-1/5)` by filling `[0,1/2]`. Hence

`||rho||_(6/5) <= C_sq.`                                             (5.5)

For `S=D X^2`, the density `rho_D` satisfies

`||rho_D||_(6/5) <= C_sq D^(-1/6).`                                 (5.6)

The right side of (5.3), as a function of `s=bz`, is the one-sided half-integral of `rho_D`:

`T(s)=int_0^infinity rho_D(v) (v+s)_+^(-1/2) dv.`                   (5.7)

Since the one-sided kernel is dominated by the standard one-dimensional Riesz kernel `|.|^(-1/2)`, Hardy--Littlewood--Sobolev gives

`||T||_3 <= C_HLS C_sq D^(-1/6).`                                   (5.8)

Changing variables `s=bz` in the output gives

`||p_F||_3 <= C_HLS C_sq D^(-1/6)|b|^(-1/3).`                       (5.9)

Using (5.1),

`boxed: ||p_F||_3
 <= (4/3)^(1/3) C_HLS C_sq D^(-1/3).`                               (5.10)

If instead `|a|` is the large diagonal, interchange the two ORIGINAL coordinates and obtain the same bound. Together with Section 3 this proves (1.1) in all cases.

The key structural point is that the proof never diagonalizes the input law. Well-conditioned pairs are handled by the already-proved original-coordinate log envelope; ill-conditioned pairs force a large original-coordinate diagonal and are handled by the literal-coordinate root formula (5.3).

## 6. Independent square: full L3-L3/2 smoothing for arbitrary indefinite pair

Combine (1.1) with the preceding B05 shifted-square lemma. Let `W` be genuinely independent of `(U,V)` with density cap `m_W`, and let `lambda!=0`. For any scalar shift `s`,

`S=lambda(W-s)^2`

has

`||p_S||_(3/2) <=2 m_W^(2/3)|lambda|^(-1/3).`                       (6.1)

If the full phase is

`Q=F+lambda(W-s)^2+c_0`,                                             (6.2)

with no source-sharing between the pair and `W`, then literal independence gives convolution and Young's inequality yields

`boxed:
 ||p_Q||_infinity
 <=2 C_pair (D |lambda|)^(-1/3)
      (m_U m_V m_W)^(2/3).`                                         (6.3)

Moreover `p_F in L^3` and `p_S in L^(3/2)`, so their convolution is continuous and vanishes at infinity. Thus this branch has a continuous `C_0` density.

### Ambient original-coordinate corollary

After conditioning all other original coordinates, (6.3) applies verbatim whenever three literal coordinates have principal quadratic block

`diag_block(B,lambda)`                                               (6.4)

with `B` invertible indefinite and the third coordinate uncoupled from the pair inside this principal block. Outside couplings become only affine terms and do not affect the constants. Therefore for cap-one inputs

`||p_(X^T A X)||_infinity <=2 C_pair (|det B| |lambda|)^(-1/3).`     (6.5)

The uncoupled third carrier in (6.4) is a genuine hypothesis. This run does NOT claim that a Schur-completed square sharing the pair's sources is independent.

## 7. Designated partner fleet02/B05 applied to an actual inequality

The fresh designated-partner report is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260924T102406Z-fleet02-B05-QFORM-r13/REPORT.md`.

Its theorem closes the exact target-valid diffuse isotropic-star family where every individual anchored determinant star is `1/m`, every definite physical pair disappears, yet aggregate curvature remains. In that family it obtains

`Q=H^2+2UV`

with a mixed-basis two-volume `E_2=1/4` and disjoint-basis probability

`delta_mix=(1-2/m)(1-4/m)^2 >=3/16` for `m>=8`.

Applying its completed mixed-basis inequality at these actual values gives

`||p_Q||_infinity
 <=12 [1/(E_2 delta_mix)]^(1/3)
 <=12(64/3)^(1/3)
 =48/3^(1/3)
 =33.2813411688... .`                                                (7.1)

This is an actual partner theorem application, not merely a citation. It is also complementary to (6.3): here the square-like `H^2` shares active original-coordinate banks with `U,V`, so the independent-square convolution theorem cannot be substituted for the partner's mixed-basis argument.

## 8. What is now missing

The previous run's exact debt `QFORM-INDEFINITE-PAIR-L3-v1` is now closed.

The next B05 obstruction is the **shared-carrier glue**, not the two-diagonal indefinite pair itself. If conditioning/Schur completion produces a family

`Q=F_w(U,V)+lambda w^2`

where the translated indefinite pair `F_w` depends on the same scalar `w`, the uniform estimate

`sup_w ||p_(F_w)||_3 <= C_pair D^(-1/3)`                              (8.1)

alone does not imply an `L^infinity` bound for the mixture

`p_Q(z)=int f_W(w) p_(F_w)(z-lambda w^2) dw.`                        (8.2)

The missing implication must retain how the translations of the pair depend linearly on the original third coordinate, or aggregate the original-coordinate three-volume before taking any reciprocal minor. A generic arbitrary-joint or conditional-cap replacement is forbidden by the live corrections.

A precise successor is therefore

`QFORM-PAIR-L3-SHARED-CARRIER-GLUE-v1`:
prove a mixed-norm estimate for the actual Schur family in (8.2), using original product provenance, strong enough to recover the `|det B|^{-1/3}|lambda|^{-1/3}` scale without an independence assumption between the pair profile and the third carrier.

The fresh fleet02/B05 r13 mixed-basis closure shows that such shared-source smoothing can be real even when every single physical pair is tiny, so this is the correct neighboring mechanism rather than another scalar-pivot peel.

## 9. Scope / status

**Proved this run:** universal scale-correct `L^3` density control for every invertible indefinite physical two-coordinate quadratic pair, including arbitrary affine terms and both nonzero diagonals; continuous bounded density after convolution with a genuinely source-disjoint square; conditional ambient corollary for a block-diagonal pair-plus-square physical triple.

**Not proved:** a generic shared-source third-carrier smoothing theorem; arbitrary higher-rank reduction; the full QFORM conjecture; or full-target continuity.

No counterexample to the owner's conjecture is produced.

## 10. Fresh source state consumed

- `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, `MANIFEST.json`, `scheduled_tasks/fleet.json`, `roles.json`, `PROTOCOL.md`, and `assignments/fleet01/B05.json` were read fresh.
- Live corrections used: arbitrary-joint 3D coarea false; conditional projection caps false; no post-rotation independence; no law-uniform pointwise quadratic-phase decay; single-minor/fiber-sup losses are not dimension-free.
- Pair-log source used exactly at commit `f7f0fedb2d93b46824f96cac1164af6f8a55626f` and path named in Section 3.
- Fresh designated partner fleet02/B05 r13 was read and applied in Section 7.

Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
