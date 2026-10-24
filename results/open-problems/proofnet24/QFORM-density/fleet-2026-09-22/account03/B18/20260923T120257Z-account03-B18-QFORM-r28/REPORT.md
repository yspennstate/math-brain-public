SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T12:02:57Z.
attacking: transfer the completed null-hub mixed-Fresnel theorem into the live Schur-isotropic packet, splice it with account04/B18's diffuse-frame theorem, and isolate the surviving heavy-row geometry.

# account03/B18 r28 — transverse-diffuse null-hub compiler for the Schur-isotropic packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Status:** `NEW SUPPORTING TARGET-LEVEL COMPILER / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Fresh prepublication owner control was reread at `yspennstate/math-research-brain@d4a2b6d302515b0acdcfe11134e6d8b3fd35a471`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no B18 pause. The live correction inbox was reread at the same commit. This proof uses no post-rotation independence, arbitrary-joint coarea, conditional projection-density cap, law-uniform pointwise quadratic-phase decay, moment/support/log-concavity hypothesis, coefficient deletion, or fixed-good-minor extraction.

The unrestricted owner conjecture remains **OPEN / NOT PROVED**. Global continuity remains open. The theorem below is an exact-rank-three Schur-isotropic supporting result and proves a continuous `C_0` density on its paid branch.

## 1. Primary-source audit

The valid Fourier interfaces used by the existing capped-basis/mixed-Fresnel packet are the sharp Hausdorff--Young theorem of Beckner, *Annals of Mathematics* 102 (1975), 159--182, and the Gaussian-extremization/finiteness theory for Brascamp--Lieb due to Lieb and Bennett--Carbery--Christ--Tao. Their use in the pinned fleet theorem is at the level of the original-coordinate product amplitude; no projected coordinates are declared independent.

Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016), prove that every `k`-dimensional orthogonal marginal of a cap-one product density is bounded by `2^(k/2)`. This remains a valid linear projection tool, but the live corrections forbid feeding a bare joint-density cap into an arbitrary indefinite coarea theorem.

A tempting more direct published Fourier-decay source does **not** match the owner quantifiers: Glazer--Mikulincer, arXiv:2108.04268, obtain their high-dimensional polynomial van-der-Corput/Fourier decay in the isotropic log-concave product setting. The present owner target permits arbitrary cap-one fragmented densities and explicitly includes phase-aligned counterexamples to law-uniform pointwise decay. I therefore do not use that theorem as a target-level input.

## 2. Incoming completed theorems

### 2.1 account03/B10 null-hub theorem

Source-pinned scientific report:

`yspennstate/math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T114517Z-account03-B10-QFORM-r24/REPORT.md`.

Its theorem `QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1` says: if

`A=R M R^T`, `R^T R=I_3`,

one ORIGINAL-coordinate spectral row is `sqrt(h) n` with `n^T M n=0`, and every other physical spectral row `w_j` satisfies

`||P_(n^perp) w_j||^2 <= 1/2`,

then for arbitrary independent cap-one original-coordinate laws,

`||p_Q||_infinity <= 3*2^(4/3) [h |det M|]^(-1/3)`,              (2.1)

and the density is continuous and vanishes at infinity.

The proof is a joint original-product mixed-Fresnel estimate, not the refuted law-uniform one-dimensional phase-decay shortcut.

### 2.2 designated partner account04/B18

Source-pinned scientific addendum:

`yspennstate/math-open-problems@e9eb90e2a7746482fb3ba75bf449b224cbf507ce`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T032213Z-account04-B18-QFORM-r2/ADDENDUM_GENERAL_DIFFUSE.md`.

Its theorem `QFORM-DIFFUSE-FRAME-FULL-BASIS-CAP-v1` pays the exact-rank-three Schur-isotropic packet

`Q=(Y+u X_0)^T D (Y+u X_0)`, `Y=V^T X_res`, `V^T V=I_3`, `u^T D u=0`,

whenever `0<r:=||u||<=1` and every residual physical row obeys `||v_j||^2<=1/2`. It gives a continuous density and

`||p_Q||_infinity <= 3 exp((3-beta)/3)(1-beta)^(-(1-beta)/3) <= 3e`,

`beta=r^2/(1+r^2)`.                                              (2.2)

This is the designated partner result applied below at a literal inequality.

## 3. Exact whitening of the Schur-isotropic packet

Retain the packet in section 2.2 and write

`u=r n`, `||n||=1`, `q_j:=||P_(n^perp)v_j||^2`.

Let

`L=[u,V^T]`, `G=L L^T=I_3+u u^T`,

and define

`R=L^T G^(-1/2)`, `M=G^(1/2) D G^(1/2)`.                         (3.1)

Then

`R^T R=I_3`, `A=L^T D L=R M R^T`.                               (3.2)

Thus (3.1) is only an algebraic spectral-frame representation of the same physical matrix; no random-variable rotation occurs.

The distinguished physical coordinate has spectral row

`w_0=G^(-1/2)u = [r/sqrt(1+r^2)] n`.                             (3.3)

Hence

`h=||w_0||^2=r^2/(1+r^2)`.                                      (3.4)

Because `G^(1/2)n=sqrt(1+r^2)n`, the normalized hub Rayleigh coefficient is

`n^T M n=(1+r^2)n^T D n=0`.                                     (3.5)

For a residual physical row `v_j`, its spectral row in (3.1) is

`w_j=G^(-1/2)v_j
    =P_(n^perp)v_j +(v_j.n)/sqrt(1+r^2) n`.                      (3.6)

Therefore the B10 augmented-transverse gate is **exactly**

`||P_(n^perp) w_j||^2=q_j`.                                     (3.7)

Finally,

`|det M|=det(G)|det D|=(1+r^2)|det D|`,                          (3.8)

so the entire determinant currency in (2.1) collapses to

`h |det M| = r^2 |det D|`.                                      (3.9)

Equations (3.3)--(3.9) are the essential missing implication: the null-hub theorem sees the **transverse** residual leverage `q_j`, not the full row leverage `||v_j||^2`, and its determinant scale exactly cancels the whitening factor.

## 4. New theorem

### `QFORM-SCHUR-NULLHUB-TRANSVERSE-COMPILER-v1`

For the packet above, suppose

`max_j q_j <=1/2`.                                                (4.1)

Then for arbitrary independent original-coordinate input densities bounded by one, `Q` has a continuous `C_0` density and

`boxed: ||p_Q||_infinity
 <=3*2^(4/3) [r^2 |det D|]^(-1/3).`                              (4.2)

If the three nonzero eigenvalues of the physical matrix have modulus at least `s>0`, then

`|pdet A|=|det M|=(1+r^2)|det D|>=s^3`,                          (4.3)

and therefore

`boxed: ||p_Q||_infinity
 <=3*2^(4/3) s^(-1) [(1+r^2)/r^2]^(1/3).`                       (4.4)

In particular,

`r>=1/2  =>  ||p_Q||_infinity
 <=3*2^(4/3)*5^(1/3) s^(-1)
 =12.9266081401913... s^(-1),`                                  (4.5)

`r>=1    =>  ||p_Q||_infinity
 <=3*2^(5/3) s^(-1)
 =9.52440631180920... s^(-1),`                                  (4.6)

and the constant tends to

`3*2^(4/3)=7.55952629936924...`

as `r` tends to infinity.

#### Proof

Sections 3.1--3.9 verify every hypothesis of the completed B10 theorem literally, with the original physical coordinates still the independent sources. Substitution of (3.9) into (2.1) proves (4.2). Equation (4.3) is the exact pseudodeterminant identity for the isometric rank-three representation (3.2), and gives (4.4). The elementary inequalities `1+r^(-2)<=5` for `r>=1/2` and `<=2` for `r>=1` give (4.5)--(4.6). Continuity and `C_0` regularity come from the B10 theorem. QED.

## 5. Designated partner account04/B18 applied at an actual inequality

The partner theorem (2.2) pays the complementary **small-shear/full-diffuse** branch:

if `0<r<1/2` and

`max_j ||v_j||^2<=1/2`,                                         (5.1)

then

`boxed: ||p_Q||_infinity <=3e=8.15484548537714...`,              (5.2)

with a continuous density.

For example, at `r=1/4`, the new transverse theorem alone would normalize only to

`3*2^(4/3)*17^(1/3)=19.4376708076649...`,

whereas the literal account04/B18 inequality remains `<=3e`. This is not a comparison of sharp constants; it shows why the two completed mechanisms splice naturally rather than one replacing the other.

Combining (4.5) and (5.2) yields the clean structural compiler:

### `QFORM-SCHUR-NULLHUB-DIFFUSE-OR-HEAVY-v1`

Every target-normalized exact-rank-three null-hub Schur-isotropic packet is paid continuously by the universal constant

`C0=3*2^(4/3)*5^(1/3)<12.927`                                   (5.3)

unless one of the following **physical-row localization** events occurs:

- `0<r<1/2` and some residual row has `||v_j||^2>1/2`; or
- `r>=1/2` and some residual row has `q_j=||P_(n^perp)v_j||^2>1/2`.

The second alternative is strictly more informative than merely `||v_j||^2>1/2`: it says one physical residual coordinate is heavy in the two-dimensional subspace transverse to the null hub.

This closes all high-shear null-hub packets with transverse-diffuse residual frame, including fully shared-source configurations; no source-separated bank hypothesis is needed.

## 6. Literature-to-proof consequence and non-applicable published route

The source-valid conclusion is therefore not a generic claim that all quadratic forms enjoy pointwise Fourier decay. The transfer works because the completed mixed-Fresnel theorem keeps the original product amplitude through an exact physical null-hub shear, and the whitening identities above show that the live Schur packet falls literally into its hypotheses.

The Glazer--Mikulincer polynomial Fourier-decay theorem cannot replace this step under the owner quantifiers because its Fourier-decay application is for isotropic log-concave product measures. Arbitrary cap-one fragmented densities in the owner target need not be log-concave or isotropic and can defeat law-uniform pointwise van-der-Corput bounds. Beckner/BL-based product-amplitude arguments and direct product-preserving small-ball/Fresnel mechanisms therefore remain the source-compatible route.

## 7. What remains unpaid

This run does **not** solve arbitrary exact rank three and does **not** solve the full owner conjecture. The first local debt after (5.3) is now localized:

1. small shear `r<1/2` with a full physical residual row of leverage `>1/2`;
2. moderate/high shear `r>=1/2` with a residual row whose **transverse** leverage exceeds `1/2`;
3. the genuinely nonzero near-null collar, where `n^T D n` is small but not zero and cannot be deleted perturbatively;
4. arbitrary additional spectrum outside the exact-rank-three core.

The next mechanism should route the heavy transverse row into the existing hub/star/pair/grouped-anchor exits, or prove a punctured near-null analogue retaining the exact small Rayleigh term. No fixed-minor or coefficient-continuity shortcut is justified.

Full QFORM: **OPEN / NOT PROVED**.  
Full-target continuous density: **OPEN**.  
Continuity on theorem (4.2) and partner branch (5.2): **PROVED**.

## 8. Deterministic algebra regression

A 100-sample numerical regression generated random symmetric invertible `D` with `n^T D n=0`, random `r` over two decades, and random residual rows. It checked

`n^T M n=0`,

`det M=(1+r^2)det D`,

`||P_(n^perp)G^(-1/2)v||^2=||P_(n^perp)v||^2`.

Maximum absolute errors were respectively

`0`, `8.53e-14`, `0`.

The computation is a regression check only; the proof is the exact algebra above.

No task/schedule state, enabled/paused state, notification/email setting, cross-account authentication, public release, remote workflow, Drive state, model/API/Codex purchase, credential, or installation action was changed.
