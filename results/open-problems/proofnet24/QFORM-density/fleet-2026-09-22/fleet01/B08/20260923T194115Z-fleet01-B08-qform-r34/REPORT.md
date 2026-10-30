SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-23T19:41:15.451468Z.
attacking: the localized exit of the transverse diffuse k=1 three-frame — turn a heavy physical row into literal cross/child coefficient currency, otherwise invoke the completed fleet02/B08 macroscopic receiver.

# fleet01/B08 r34 — heavy three-frame rows compile to literal physical currency

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** diffuse eigenvector case / analytic derivation and exact structural identities  
**Status:** `PROVED SUPPORTING PHYSICAL-CURRENCY ROUTER + DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains **OPEN**. The unrestricted continuity conclusion remains **OPEN**. Continuity below is asserted only on the branch paid by the completed Fourier/volume receiver.

No moment, bounded-support, connected-support, log-concavity, iid, centering, post-rotation independence, arbitrary-joint coarea, pointwise law-uniform quadratic phase decay, or probabilistic small-matrix-error assumption is used.

## 1. First missing implication attacked

The previous B08 run `r33` (`math-open-problems@faad78e1fbcbfe0943990210de098df34a96e042`) gave a heavy-row peeling dichotomy for the transverse `k=1` child-plus-two-cross frame. Its unpaid exit said that a genuine three-frame direction can concentrate on a bounded physical core.

This run removes the need to carry that abstract finite-core certificate through the **small-leakage transverse chamber**. A single row whose augmented three-frame leverage exceeds the partner threshold already forces a quantitative coefficient in the literal original-coordinate matrix: either a cross-row star, or a child diagonal/off-diagonal row star. If there is no such row, the completed designated partner fleet02/B08 theorem applies directly.

The result is deterministic coefficient geometry followed by one source-pinned analytic receiver.

## 2. Exact row geometry

Let `C` be a real symmetric child block and let

    C r = lambda r,       ||r||_2=1,       |lambda| >= c L.      (2.1)

Let `B` be the **literal** cross block. Let `U` be an orthonormal two-frame spanning the top-two left singular space of `B`, and suppose

    s_2(B) >= beta L.                                            (2.2)

Put

    d = dist(r, range U) > 0,
    q = (I-UU^T)r/d,
    W = [q,U].                                                    (2.3)

Then `W^T W=I_3`. Write

    r = U a + d q,       ||a|| = sqrt(1-d^2).                    (2.4)

For a physical row `i`, define

    u_i = ||U^T e_i||_2,
    h_i = q_i^2 + u_i^2 = ||W_{i,*}||_2^2,
    m_i = max{|r_i|,u_i}.                                        (2.5)

### Theorem 2.1 — `QFORM-TRANSVERSE-ROW-CURRENCY-v1`

For every physical row `i`,

    m_i >= gamma(d) sqrt(h_i),                                   (2.6)

where

    gamma(d) = sqrt((1-sqrt(1-d^2))/2).                          (2.7)

Consequently at least one of the following two alternatives holds on that row:

    ||B^T e_i||_2 >= beta L gamma(d) sqrt(h_i),                  (2.8)

or

    ||e_i^T C||_2 >= c L gamma(d) sqrt(h_i).                     (2.9)

In the second alternative,

    max{|C_ii|, ||C_{i,-i}||_2}
       >= (c/sqrt(2)) L gamma(d) sqrt(h_i).                       (2.10)

#### Proof

Let `s=sqrt(1-d^2)`. From (2.4), Cauchy gives

    |q_i|
      = |r_i-(Ua)_i|/d
      <= (|r_i|+s u_i)/d
      <= ((1+s)/d)m_i.                                          (2.11)

Therefore

    h_i <= m_i^2 [1+(1+s)^2/d^2].                               (2.12)

Since `d^2=1-s^2`,

    1+(1+s)^2/d^2 = 2/(1-s),                                    (2.13)

which is exactly (2.6)-(2.7).

If `m_i=u_i`, use the exact singular-value expansion of the actual cross block:

    ||B^T e_i||_2^2
      = sum_j s_j(B)^2 |<e_i,u_j>|^2
      >= s_2(B)^2 sum_{j=1}^2 |<e_i,u_j>|^2
      = s_2(B)^2 u_i^2.                                         (2.14)

Equations (2.2) and (2.6) give (2.8).

If `m_i=|r_i|`, then the exact eigen-equation (2.1) gives

    ||e_i^T C||_2 >= |(Cr)_i| = |lambda r_i|
                    >= cL gamma(d)sqrt(h_i),                    (2.15)

which is (2.9). Finally

    ||e_i^T C||_2^2 = C_ii^2+||C_{i,-i}||_2^2,                  (2.16)

so at least one of the two terms is at least the row norm divided by `sqrt(2)`. This proves (2.10). QED.

The constant `gamma(d)` is not an artifact of a rough triangle inequality: the two inequalities in (2.11)-(2.13) can be simultaneously saturated in the two-dimensional coefficient geometry, so this is the sharp rowwise minimax constant for the information used here.

## 3. Uniform transverse specialization

Assume now

    d >= 1/2.                                                     (3.1)

The function `gamma` is increasing, hence

    gamma(d) >= gamma(1/2)
             = sqrt((2-sqrt(3))/4)
             = sin(pi/12)
             = 0.2588190451025207... .                           (3.2)

If a row has augmented leverage

    h_i > 1/48,                                                   (3.3)

then Theorem 2.1 yields either

    ||B^T e_i||_2
      > beta sin(pi/12)/sqrt(48) * L,                            (3.4)

or

    max{|C_ii|,||C_{i,-i}||_2}
      > c sin(pi/12)/sqrt(96) * L.                              (3.5)

These are coefficients/stars in the literal original-coordinate matrix. There is no conditioning-density assertion hidden in (3.4)-(3.5).

## 4. Application to the actual balanced `k=1` gate

The exact squared-energy ledger proved by this slot in r30,

`math-open-problems@014df00b32f2360c1b5c835434bb146cf57e1930`,

upgraded the actual balanced `k=1` cross scale to

    beta_* = 3/sqrt(40) = 0.4743416490252569... ,                (4.1)

while the actual child scale is

    c = sqrt(3/20) = 0.3872983346207417... .                     (4.2)

Substituting (4.1)-(4.2) into (3.4)-(3.5) gives the explicit heavy-row exit

    boxed: ||B^T e_i||_2 > 0.0177201286643247 L,                 (4.3)

or

    boxed: max{|C_ii|,||C_{i,-i}||_2}
                      > 0.0102307210544227 L.                    (4.4)

The stronger statement before splitting the child row is

    ||e_i^T C||_2 > 0.0144684244680205 L.                        (4.5)

Thus the former abstract statement “the augmented three-frame has a heavy physical row” now carries a quantitative physical coefficient certificate.

## 5. Completed designated-partner theorem applied to the complementary rows

The completed designated partner result is fleet02/B08 r28:

`math-open-problems@66582bd87d50634f3525a57c87acffdbde97aea1`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T153836Z-fleet02-B08-qform-r28/REPORT.md`.

Its theorem `QFORM-K1-MACROSCOPIC-3FRAME-HALFCUT-v1` applies when the same augmented three-frame has maximum physical leverage

    nu := max_i h_i <= 1/48,                                    (5.1)

the child/cross sine angle is at least `d0`, the child coefficient is at least `cL`, the second cross coefficient is at least `beta L`, and the literal coefficient-matrix leakage obeys its operator-norm gate. The proof groups original independent coordinates before any reciprocal pivot payment and retains arbitrary allowed within-bank phases and outside couplings.

Apply it here with the **actual r30 scale**

    beta=beta_*=3/sqrt(40),        d0=1/2.                       (5.2)

Its displayed constant becomes

    kappa_*
      = [c beta_* d0^2]
        /[2 sqrt(c^2 d0^2+4 beta_*^2)]
      = 0.023717082451262847... .                               (5.3)

Therefore the actual inequality

    sqrt(||E_C||_op^2+||E_B||_op^2)
       <= (kappa_*/16)L
       = 0.001482317653203928... L                              (5.4)

implies, uniformly over all original-coordinate product laws in the owner target,

    boxed: ||p_Q||_infinity
      < 23/(kappa_* L)
      = 969.765149118303.../L,                                  (5.5)

and this paid branch has a continuous `C_0` representative.

This is a direct application of the completed partner theorem to the actual r30/r31 inequality, not a citation-only dependency.

## 6. New compiled router

Combining Theorem 2.1 with Section 5 gives the following exhaustive statement in the transverse, small-leakage part of the actual balanced `k=1` gate.

### Corollary 6.1 — `QFORM-K1-TRANSVERSE-HEAVYROW-COMPILER-v1`

Assume the actual `k=1` gate has

- child eigenpair `Cr=lambda r` with `|lambda|>=sqrt(3/20)L`;
- actual cross block `B` with `s_2(B)>3L/sqrt(40)`;
- `d=dist(r,range(U_2(B)))>=1/2`;
- the same structured leakage as fleet02/B08 r28 is at most `0.001482317653203928 L`.

Then at least one of the following holds:

1. the full ambient form has a continuous `C_0` density with

       ||p_Q||_infinity < 969.766/L;

2. some original-coordinate cross row satisfies

       ||B^T e_i||_2 > 0.0177201 L;

3. some original child coordinate satisfies

       max{|C_ii|,||C_{i,-i}||_2} > 0.0102307 L.

#### Proof

If `nu<=1/48`, apply the partner theorem as in Section 5. If `nu>1/48`, choose a row with `h_i>1/48` and apply Section 4. These cases are exhaustive. QED.

The practical gain is that r33's `>1/2` mass on at most 287 coordinates is no longer the first residual object in this chamber. The residual is now a literal star/pivot-scale coefficient configuration, which can be handed to localized/grouped-coordinate receivers without inventing conditional density caps.

## 7. What remains unpaid

This does **not** by itself prove a universal density bound from one row star. Existing correction history explicitly warns that a lone physical hub/star can be insufficient when same-bank curvature is arbitrary. Accordingly the next implication is kept honest:

`QFORM-K1-TRANSVERSE-PHYSICAL-CURRENCY-RECEIVER-v1`:

> Starting from either the literal cross-row star (4.3) or child diagonal/off-diagonal star (4.4), compile that currency together with the already present two-cross/one-child spectral structure into a source-valid grouped-crossing, Schur, or localized receiver, retaining the full complementary spectrum and every conditioning-generated affine term.

Two other branches remain separate: `d<1/2` (near alignment), and leakage above (5.4). Neither is claimed paid here.

## 8. Corrections and finite check

Before publication I reread the live correction inbox on fresh `math-research-brain/main`. None of the refuted interfaces is used. In particular this proof does not use law-uniform pointwise van der Corput decay, arbitrary-joint coarea, a fiberwise conditional cap, independence after rotation, or the false implication that a small coefficient-matrix perturbation is a small random quadratic perturbation.

`check.py` is a deterministic-seed sanity check of the sharp row inequality for 5000 random three-frames with `d in [1/2,1]`; `CHECK_OUTPUT.txt` records zero violations and ends `QFORM_B08_R34_ROW_CURRENCY_CHECK_PASS`. It also prints the exact numerical constants in (4.3)-(5.5). This finite check is not part of the proof.

## 9. Status

- Full unrestricted QFORM conjecture: **OPEN**.
- Full-target continuity: **OPEN**.
- New exact structural theorem: **PROVED** as above.
- Partner-paid transverse diffuse branch: **continuous `C_0` density**, bound (5.5).
- Heavy-row branch: **literal coefficient currency only**, not yet a density theorem.
- Independent end-to-end review of a full solution: not applicable; no full solution is claimed.
