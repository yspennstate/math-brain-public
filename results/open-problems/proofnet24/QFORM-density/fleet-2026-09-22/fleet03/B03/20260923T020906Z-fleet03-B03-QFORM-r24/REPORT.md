SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T02:09:06Z.
attacking: decoupled time integral — interpolate the exact hub/screen independent-copy identity with the newest q-dependent Hausdorff--Young/Brascamp--Lieb mechanism, removing the old leverage-1/2 gate in higher screen rank.

# QFORM-HUB-SCREEN-FRACTIONAL-BL-v1

## Status

**SUPPORTING THEOREM PROVED / LINEAR SMALL-BALL SCALING ON A STRICTLY LARGER HUB-SCREEN CLASS / FULL QFORM OPEN.**

This run extends fleet03/B03 r23's dependence-safe low-rank-screen theorem.  It keeps every sum/difference dependence inside the exact hub ambiguity function, keeps all random variables in original coordinates, permits arbitrary same-bank quadratic curvature and arbitrary dense cross twist on the unused block, and replaces the r23 shared-side leverage hypothesis `max ell_i<=1/2` by an interpolated condition `q>=2 max ell_i`.  The newest q-dependent Hausdorff--Young/Brascamp--Lieb calculation from the volume-stability package is used at an actual equation below, rather than merely cited.

The resulting direct Fourier estimate has three concrete gains:

1. rank-one screens now close whenever the maximum augmented-frame leverage is `<2/3`, rather than only `<=1/2`;
2. rank-two screens close whenever the maximum leverage is `<1`;
3. every screen rank `r>=3` closes with `q=2` **without any leverage restriction at all**.

In each direct-closing case the density is continuous and vanishes at infinity.  The full three-large-eigenvalue conjecture remains open because the bare spectral hypothesis does not yet force one of these quantitative augmented-screen certificates.  Full-target continuity therefore also remains open.

## 1. Fresh sources and live corrections

Fresh owner control was re-read immediately before publication from

`yspennstate/math-research-brain@618ab66f5561589cb61db7e49c8debdc465d7b97`,


The required newest mathematical package is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its Section 5 proves the q-dependent Hausdorff--Young/Brascamp--Lieb mechanism: a row exponent `alpha_i` may be paid whenever `alpha_i<=q/2`, because the scalar Fourier exponent `q/alpha_i` is then at least two.  I apply exactly that interpolation principle to the translated augmented screen frame below.

The exact hub ambiguity identity and projection/BL inputs are from

`yspennstate/math-open-problems@f68817886312b904e2cf86ccbfb14f4f130229f3:proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/hub_decoupling/REPORT.md`.

The immediate predecessor is

`yspennstate/math-open-problems@9655d21c63995f50f815155ccb013c9224f83910:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T005518Z-fleet03-B03-QFORM-r23/LOWRANK_SUPPLEMENT.md`.

The live correction inbox was refreshed at the same control snapshot.  In particular I retain the prohibitions on conditional sum/difference density caps, law-uniform scalar pointwise decay, arbitrary-joint rank-three coarea, one-good-minor extraction, and local collision payment before aggregation.  The new `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1` correction is consistent with the present proof: the screen packet is aggregated before the time norm is taken.  The `QFORM-MIXED-SKELETON-DETERMINANT-ONLY-L1-FALSE-v1` correction is also irrelevant to the stated theorem because no arbitrary same-bank curvature is discarded.

Execution status is `WITHOUT_VERIFIED_BRAIN`: authenticated repository reads/writes occurred, but separate native learned-memory receiver use was not verified.

## 2. Setup

Let the original independent cap-one coordinates be split as

`{h} disjoint_union I disjoint_union J_V disjoint_union J_L disjoint_union K`.

Condition on `X_K`; this changes only affine/constant terms in the active variables.  Let `w=(A_hj)_(j!=h)` be the physical hub row and suppose the original-coordinate screen block factors as

`A[I,J_L]=U V^T`,

where `U` is `|I| x r`, `V` is `|J_L| x r`, and both have rank `r>=1`.  There is **no restriction** on `A[I,J_V]`, any self block, the hub diagonal, outside couplings, affine terms, signs, moments, supports, or connectedness.

Define

`P_I=[w_I,U]`,       `G_I=P_I^T P_I`,

`G_V=V^T V`,

`P_J=[V,w_(J_L)]`,   `G_J=P_J^T P_J`.

Assume `G_I` and `G_J` are invertible.  For each physical row `i in I`, let

`ell_i=(P_I)_(i,*) G_I^(-1) (P_I)_(i,*)^T`,

and write

`h_I=max_i ell_i`.

Fix a real parameter

`1<=q<=2`,     `q>=2 h_I`.                                           (2.1)

Put

`k=r+1`,       `N=q+2k=q+2r+2`,

and define the factorization-invariant packet

`Omega_(r,q)
   = det(G_I) det(G_J)^(q/2) det(G_V)^((2-q)/2)`.                    (2.2)

## 3. The theorem

### Theorem 3.1 (fractional-BL augmented-screen estimate)

Under the setup above, for every `t!=0`,

`|phi_Q(t)|^2 <= D_(r,q) |t|^(-beta_q)`,                             (3.1)

where

`beta_q = 1/2 + (r+1)/q = N/(2q)`,                                  (3.2)

and

`D_(r,q)
 = 2^(1/4+r/(2q)) pi^(beta_q) (e/q)^((r+1)/(2q))
   det(G_I)^(-1/(2q)) det(G_J)^(-1/4)
   det(G_V)^(1/4-1/(2q)).`                                           (3.3)

Therefore `phi_Q in L^2` for every admissible `r,q`, and the law has an `L^2` density satisfying

`boxed(
 ||p_Q||_2^2
 <= L_(r,q) Omega_(r,q)^(-1/N)
 )`,                                                                  (3.4)

with

`L_(r,q)
 = [N/(2(r+1)-q)]
   2^((q+2r)/(2N)) (e/q)^((r+1)/N).`                                 (3.5)

If in addition

`q < 2(r+1)/3`,                                                       (3.6)

then `phi_Q in L^1`, so `Q` has a continuous `C_0` density and

`boxed(
 ||p_Q||_infinity
 <= C_(r,q) Omega_(r,q)^(-1/N)
 )`,                                                                  (3.7)

where

`C_(r,q)
 = [N/(2(r+1)-3q)]
   2^((q+2r)/(2N)) (e/q)^((r+1)/N).`                                 (3.8)

Consequently every interval `B` obeys

`P(Q in B) <= C_(r,q) Omega_(r,q)^(-1/N) |B|`.                       (3.9)

Finally, without the extra condition (3.6), the half-order potential is always finite:

`boxed(
 sup_s E|Q-s|^(-1/2)
 <= H_(r,q) Omega_(r,q)^(-1/(2N))
 )`,                                                                  (3.10)

where

`H_(r,q)
 = [2 sqrt(2) N/(2(r+1)-q)]
   2^((q+2r)/(4N)) (e/q)^((r+1)/(2N)).`                              (3.11)

The half-Riesz statement is a translation-uniform integrated-time estimate and does not assert an `L^infinity` density at the logarithmic direct-Fourier endpoint.

## 4. Exact independent-copy geometry

Use Proposition 4.1 of the hub-decoupling source.  Duplicate the hub and `J_0=J_V union J_L`, keep `I` shared, and for each duplicated original coordinate retain its actual difference variable `W=X-X'`.  Across distinct physical coordinates the `W_j` are independent cap-one probability densities, but no sum/difference pair from the same coordinate is ever declared independent.

For the hub copies put

`X_h=mu+sigma/2`,       `X_h'=mu-sigma/2`,

`F_sigma(mu)=f_h(mu+sigma/2)f_h(mu-sigma/2)`.

The ambiguity transform satisfies

`int_R |Fhat_sigma(s)|^2 ds <= 2 pi g_h(sigma)`,                     (4.1)

where `g_h` is the hub-difference density, `0<=g_h<=1`, `int g_h=1`.

The exact source reduction gives

`|phi_Q(t)|^2
 <= int d sigma E_W [
      |Psi_I(2t( sigma w_I + A[I,J_V]W_V + U V^T W_L ))|
      |Fhat_sigma(2t(<w_(J_V),W_V>+<w_(J_L),W_L>+a sigma))|
    ]`.                                                               (4.2)

Every same-bank quadratic phase allowed in the theorem is already accounted for in this exact reduction.  The dense block `A[I,J_V]` is retained; it will become only a translation after the correct screen variables are kept.

## 5. The joint screen projection and the ambiguity L2 payment

Set

`Z=V^T W_L in R^r`,       `Y=<w_(J_L),W_L>`.

The product projection theorem used in the hub source gives

`||p_Z||_infinity <= 2^(r/2) det(G_V)^(-1/2)`,                       (5.1)

`||p_(Z,Y)||_infinity <= 2^((r+1)/2) det(G_J)^(-1/2)`.               (5.2)

Fix `sigma,W_V,z`, absorbing all their harmless affine shifts into `C`.  Cauchy--Schwarz in the **actual joint density** `p(z,y)` gives

`int p(z,y)|Fhat_sigma(2t(y+C))|dy
 <= p_Z(z)^(1/2)
    [int p(z,y)|Fhat_sigma(2t(y+C))|^2dy]^(1/2).`

By (5.2), `s=2t(y+C)`, and (4.1),

`boxed(
 int p(z,y)|Fhat_sigma(2t(y+C))|dy
 <= 2^((r+1)/4) pi^(1/2)|t|^(-1/2)
    det(G_J)^(-1/4) p_Z(z)^(1/2) g_h(sigma)^(1/2).
 )`                                                                    (5.3)

This is the key dependence-safe form.  Unlike the refuted conditional-cap route, it never normalizes `Y|Z`; the true factors `p_Z(z)^(1/2)` and `g_h(sigma)^(1/2)` remain to be paid jointly with the shared-bank Fourier product.

## 6. New q-dependent translated frame estimate

This is where the newest volume-stability/Hausdorff--Young result is applied.

### Lemma 6.1

For every translation `beta in R^I`, under (2.1),

`boxed(
 int_(R^k) |Psi_I(P_I xi+beta)|^q dxi
 <= [2 pi sqrt(e/q)]^k det(G_I)^(-1/2).
 )`                                                                    (6.1)

#### Proof

Normalize the frame by `G_I^(-1/2)`.  Its rows become `sqrt(ell_i) u_i`, with `u_i` unit whenever `ell_i>0`, and

`sum_i ell_i u_i u_i^T = I_k`,      `sum_i ell_i=k`.                 (6.2)

Geometric Brascamp--Lieb gives

`int prod_i |psi_i(sqrt(ell_i)<u_i,x>+beta_i)|^q dx
 <= prod_i [ ell_i^(-1/2)
              int |psi_i(s)|^(q/ell_i) ds ]^(ell_i).`                (6.3)

Because `q>=2 ell_i`, every scalar exponent `p_i'=q/ell_i` is at least two.  Apply the sharp Hausdorff--Young estimate exactly as in the newest volume-stability report.  Since `f_i<=1` is a probability density,

`int |psi_i(s)|^(q/ell_i) ds
 <= 2 pi (q/(q-ell_i))^((q-ell_i)/(2 ell_i))
          (q/ell_i)^(-1/2).`                                        (6.4)

Multiplication by `ell_i^(-1/2)` cancels the square root of `ell_i`, so (6.3) is at most

`(2 pi/sqrt(q))^k
 prod_i (1-ell_i/q)^(-(q-ell_i)/2).`                                 (6.5)

For `x in[0,1]`, `-(1-x)log(1-x)<=x`.  With `x_i=ell_i/q`,

`log product <= (q/2) sum_i x_i = k/2`.                              (6.6)

This proves `(2 pi sqrt(e/q))^k`.  Restoring the linear change of variables contributes `det(G_I)^(-1/2)`.  Translation never changes the scalar Fourier norms.  Rows of zero leverage are omitted by continuity.  QED.

After scaling by `2t`, (6.1) gives

`||Psi_I(2t(P_I xi+beta))||_(L^q(dxi))
 <= [pi sqrt(e/q)]^(k/q)|t|^(-k/q)
    det(G_I)^(-1/(2q)).`                                             (6.7)

## 7. Hölder closes the dependent product

After (5.3), write `xi=(sigma,z) in R x R^r`.  The only remaining weight is

`w_0(xi)=[g_h(sigma)p_Z(z)]^(1/2)`.

Let `q'` be conjugate to `q`.  Since `1<=q<=2`, `q'>=2`.  Using `g_h<=1`, mass one, and (5.1),

`||w_0||_(q')
 <= ||p_Z||_infinity^(1/q-1/2)
 <= [2^(r/2)det(G_V)^(-1/2)]^(1/q-1/2).`                            (7.1)

For each fixed `W_V`, the dense term `A[I,J_V]W_V` is merely a translation in (6.7).  Hölder in the actual variables `(sigma,z)`, followed by averaging `W_V`, therefore combines (5.3), (6.7), and (7.1) into (3.1)-(3.3).

No positivity, independence, or bounded conditional density has been added beyond what the original product law actually supplies.

## 8. Inversion, L2 collision, and half-Riesz integration

From (3.1),

`|phi_Q(t)| <= min(1, D_(r,q)^(1/2)|t|^(-b_q))`,

`b_q=beta_q/2=N/(4q)`.                                               (8.1)

For `b>1`,

`int_R min(1,B|t|^-b)dt = [2b/(b-1)]B^(1/b)`.                       (8.2)

Condition `b_q>1` is exactly (3.6).  Substituting (3.3) into (8.2) and Fourier inversion gives (3.7)-(3.8): the power of `pi` becomes exactly one and cancels the inversion factor, while the determinant powers combine as `Omega_(r,q)^(-1/N)`.

For the L2 statement, `beta_q>1` for every `r>=1`, `q<=2`, and

`int_R |phi_Q(t)|^2dt
 <= [2 beta_q/(beta_q-1)]D_(r,q)^(1/beta_q).`                        (8.3)

Plancherel gives (3.4)-(3.5).

For the half-order potential, the standard positive regularization of the Riesz kernel yields

`sup_s E|Q-s|^(-1/2)
 <= (2pi)^(-1/2) int_R |t|^(-1/2)|phi_Q(t)|dt.`                     (8.4)

For every `b>1/2`,

`int_R |t|^(-1/2)min(1,B|t|^-b)dt
 = [4b/(b-1/2)]B^(1/(2b)).`                                         (8.5)

Here `b_q>=3/4`, so (8.4)-(8.5) prove (3.10)-(3.11).

## 9. Factorization invariance

The screen factorization is not unique.  For `S in GL(r)`, replace

`U -> U S`,      `V -> V S^(-T)`.

Then

`det G_I -> det(S)^2 det G_I`,

`det G_V -> det(S)^(-2) det G_V`,

`det G_J -> det(S)^(-2) det G_J`.

The exponent of `det S` in (2.2) is

`2 - q - (2-q)=0`.

Thus `Omega_(r,q)` is a physical certificate of the augmented screen packet, not an artifact of the chosen factorization.

## 10. Concrete corollaries

### 10.1 Rank one

Here `k=2`.  Direct L1 inversion needs `q<4/3`.  Since the smallest admissible choice is `q=max(1,2h_I)`, every

`h_I<2/3`                                                               (10.1)

closes.  At the old range `h_I<=1/2`, choose `q=1`; the sharpened constant is

`C_(1,1)=9.183258210955094...`,                                      (10.2)

improving the previous r23 prefactor `10.7177346...` at the same invariant scale.

For the strict-N3 balanced mixed-hub witness paid in r23,

`det G_I=1/4`, `det G_J=1/4`, `det G_V=1/2`,

so `Omega_(1,1)=1/(8 sqrt(2))`.  The new bound is

`||p_Q||_infinity <=14.918246976412703...`,                           (10.3)

again with a continuous density.  This is a control family, not an exhaustive N3 theorem.

### 10.2 Rank two

Here `k=3`, and direct inversion needs only `q<2`.  Therefore every

`h_I<1`                                                               (10.4)

closes.  For example, at `h_I<=1/2`, `q=1` gives

`C_(2,1)=4.587897478510473...`.                                      (10.5)

At `h_I<=3/4`, `q=3/2` gives

`C_(2,3/2)=8.177658276764104...`.                                    (10.6)

At the exact coloop endpoint `h_I=1`, only `q=2` is admissible and direct L1 inversion is logarithmically critical.  The new half-Riesz estimate remains finite:

`boxed(
 sup_s E|Q-s|^(-1/2)
 <= 4 sqrt(2) e^(3/16)
    [det(G_I)det(G_J)]^(-1/16)
 )`,                                                                  (10.7)

whose prefactor is `6.823468712303328...`.  This is a useful translation-uniform endpoint for a further genuine square transducer, but it is not by itself an `L^infinity` theorem.

### 10.3 Rank at least three: no leverage gate

For every `r>=3`, take `q=2`.  Since every row leverage is at most one, (2.1) is automatic.  The `G_V` factor disappears entirely and

`boxed(
 ||p_Q||_infinity
 <= [(r+2)/(r-2)] e^((r+1)/(2(r+2)))
    [det(G_I)det(G_J)]^(-1/[2(r+2)])
 )`.                                                                  (10.8)

This density is continuous and vanishes at infinity.  For `r=3`,

`||p_Q||_infinity
 <= 5 e^(2/5)[det(G_I)det(G_J)]^(-1/10)
 =7.459123488206351... [det(G_I)det(G_J)]^(-1/10).`                  (10.9)

The L2 constant in the same branch is

`||p_Q||_2^2
 <= (5/3)e^(2/5)[det(G_I)det(G_J)]^(-1/10)
 =2.486374496068784... times the invariant power.`                   (10.10)

## 11. Designated partner applied to an actual new inequality

The completed `fleet04/B03` report is

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`.

Its previously advertised weighted-L2 compiler has a known homogeneity/time-weight error and is not used.  Its valid collision lemma is

`P(|Y-Y'|<=epsilon) <= 2 epsilon ||p_Y||_2^2`.                       (11.1)

Applying (11.1) to the **new** L2 estimate (3.4) gives

`boxed(
 P(|Q-Q'|<=epsilon)
 <= 2 L_(r,q) Omega_(r,q)^(-1/N) epsilon.
 )`                                                                  (11.2)

For the leverage-free `r=3,q=2` branch this is

`P(|Q-Q'|<=epsilon)
 <= (10/3)e^(2/5)
    [det(G_I)det(G_J)]^(-1/10) epsilon`

`=4.972748992137568... [det(G_I)det(G_J)]^(-1/10) epsilon.`          (11.3)

This is a literal partner-result application and a linear independent-copy collision estimate derived without splitting any coordinate sum from its difference.

## 12. Checks

The executed checker `check_r24.py` verifies:

- the `beta_q=N/(2q)` exponent identity;
- cancellation of the Fourier `pi` factor;
- every determinant exponent in `Omega_(r,q)`;
- factorization invariance;
- the exact L1 threshold, including the rank-one `q=4/3` and rank-two `q=2` logarithmic endpoints;
- the displayed numerical constants;
- `r=3,q=2`: `C=5e^(2/5)`, `L=(5/3)e^(2/5)`;
- rank-two `q=2` half-Riesz constant `4sqrt(2)e^(3/16)`.

The actual output ends

`QFORM_B03_R24_CHECK_PASS`.

Finite algebra checks are not independent proof review.

## 13. First unpaid implication

The analytic screen payment is now considerably less fragile: rank three and above require no shared-side leverage gate at all, rank two only excludes the exact coloop endpoint for direct inversion, and rank one tolerates leverage up to `2/3`.

The first full-target debt is therefore more sharply structural.  From only three eigenvalues with absolute value at least one, prove an exhaustive **product-preserving aggregate alternative** that either:

1. enters one of the already-paid three-volume/ridge/near-diffuse exits;
2. produces an augmented hub/screen packet with quantitative `Omega_(r,q)` in one of the closing ranges above;
3. enters the separately paid exact-coloop/mixed-hub/grouped-square mechanisms; or
4. supplies a new grouped packet for the genuinely entangled small-total-tail remainder.

The fresh fleet02/B03 correction shows why one must aggregate before local collision payment, and the fresh fleet01/B03 product-plus-two-square result supplies another legitimate grouped exit.  Neither result makes this structural OR automatic.  Known local-minor and single-Schur counterexamples forbid replacing the OR by the assertion that one uniformly good small physical minor exists.

Therefore the unrestricted QFORM conjecture is still **OPEN**.  No counterexample to it is produced here.  Continuity is **PROVED only in the direct-closing branches (3.6)** and remains open for the unrestricted target.

## 14. Execution discipline

No scheduler/task identity, enabled/paused state, cadence, email, push notification, account binding, permission, installation, paid model/API/Codex call, remote workflow, or public-release setting was changed.  Repository transport is not native learned-memory ingestion.  Model self-report is `GPT-5.6 Sol`; configured reasoning effort and provider reasoning-token/thinking-time telemetry were not exposed and are recorded as `UNKNOWN`/`null` in the run receipt.
