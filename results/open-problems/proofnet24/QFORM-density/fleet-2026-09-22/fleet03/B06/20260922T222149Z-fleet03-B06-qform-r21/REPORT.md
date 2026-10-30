SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B06, 2026-09-22T22:21:49Z.
attacking: the strict-higher-rank bicolooop survivor after the grouped actual-minor reduction, by turning two physically heavy exterior directions into one genuinely large ORIGINAL-coordinate 2x2 cross minor; otherwise isolate a one-sided wedge-diffuse state.

# fleet03/B06 QFORM r21 — wedge-diffuse or a paid physical 2x2 minor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T222149Z-fleet03-B06-qform-r21`  
**Assignment:** Curved fiber integration  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** not proved by the branch theorem below; the paid branch gives an essentially bounded density.

## 1. Exact scope and source-valid inputs

The full target is unchanged: for every finite `n`, every collection of independent real `X_i` with one-dimensional probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `X^T A X`, or produce a target-valid counterexample.

No Gaussian, log-concavity, moment, compact-support, connected-support, or diagonal-basis assumption is introduced. In particular, no spectral rotation is treated as preserving independence. The live corrections are retained: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint rank-three coarea bound, no positive moment of a worst conditional projection-density cap, no unrestricted fiber supremum, no X-ray-only indefinite trace bound, and no small-tail characteristic-function perturbation.

### Input A — fleet03/B08 r22, actual grouped-minor core

Canonical source:

`yspennstate/math-open-problems@c5b2350b76a01283a2503368d013a44beadbbcc6`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T215031Z-fleet03-B08-qform-diffuse-r22/REPORT.md`.

In the only unpaid nonzero-pivot strict-higher-rank bicolooop branch, there are:

* a genuine original-coordinate outer scalar pivot `a!=0`;
* an actual original-coordinate cross block `H` with singular values `h_1>=h_2>=h_3>=...`;
* a scale `gamma>0`;
* top left singular vectors `u_1,u_2` and top right singular vectors `v_1,v_2`;
* physical anchor indices `j,r` such that

`L_j:=u_1(j)^2+u_2(j)^2 > 6221/6450`,                            (1.1)

`R_r:=v_1(r)^2+v_2(r)^2 > 6221/6450`,                            (1.2)

`h_3/h_2 < 3/200`,                                                (1.3)

and

`h_1 h_2 > (4/5) gamma^2`.                                       (1.4)

The same report identifies the actual physical double-incident minor matrix

`M_H(k,s)=det H[{j,k},{r,s}]`, `k!=j`, `s!=r`,                    (1.5)

and proves `||M_H||_op>(3/4)gamma^2`. More precisely, its exterior-square decomposition gives a rank-one leading term plus a remainder with operator norm at most `h_1 h_3`. The present run spends that more precise decomposition.

### Input B — exact rank-two conditional grouped theorem

Canonical source:

`yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

For a rank-exactly-two ORIGINAL-coordinate cross block `C` and fixed physical row/column `j,r`, with

`Delta_jr(C)=sum_(k!=j,s!=r) det C[{j,k},{r,s}]^2`,

it proves, uniformly under conditioning on all outside ORIGINAL coordinates,

`||p_R||_3 <= 3^(2/3) 2^(1/3) Delta_jr(C)^(-1/6)`.                (1.6)

All same-side quadratic terms, affine terms, and outside couplings are retained. For a physical `2 x 2` cross block with determinant `d!=0`, (1.6) reduces to

`||p_R||_3 <= 3^(2/3) 2^(1/3) |d|^(-1/3)`.                       (1.7)

### Input C — compatible completed fleet04 square theorem actually applied

The designated partner `fleet04/B06` has a current QFORM run start but no completed current-QFORM canonical report/handoff at the final source check, so no partner theorem or PASS is fabricated.

The compatible completed fleet04 result actually applied is fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its proof supplies, after the genuine original-coordinate scalar completion,

`p_Q(t) <= |a|^(-1/2) int_0^infinity
 p_R(t-sgn(a)u) u^(-1/2) du`.                                      (1.8)

This inequality does not assume independence between the residual value and the translated square variable.

## 2. The top-two exterior directions incident to the anchors

Define, for `k!=j`,

`p_k = [u_1(j)u_2(k)-u_2(j)u_1(k)]/sqrt(L_j)`,                    (2.1)

and for `s!=r`,

`q_s = [v_1(r)v_2(s)-v_2(r)v_1(s)]/sqrt(R_r)`.                    (2.2)

The standard two-frame identity gives

`sum_(k!=j) p_k^2=1`, `sum_(s!=r) q_s^2=1`.                       (2.3)

Let

`M_0 = h_1 h_2 sqrt(L_j R_r) p q^T`.                              (2.4)

From the exterior-square singular expansion used in Input A,

`M_H=M_0+E`, `||E||_op <= h_1 h_3`.                               (2.5)

This is stronger than merely knowing the total determinant-bank norm. It identifies the only way that an individual physical minor can fail to inherit the large top-two exterior currency: at least one of the two incident exterior directions must be spread over physical coordinates.

## 3. New dichotomy: wedge diffuse, or one physical minor is uniformly large

### Theorem 3.1 — `QFORM-BICOLOOP-WEDGE-DIFFUSE-OR-PHYSICAL-MINOR-v1`

In the strict-higher-rank state of Input A, one of the following alternatives holds.

**(D) Wedge-diffuse alternative.** On at least one side,

`max_(k!=j) p_k^2 <= 1/2`

or

`max_(s!=r) q_s^2 <= 1/2`.                                         (3.1)

**(P) Paid physical-minor alternative.** There are physical indices `k!=j`, `s!=r` for which

`boxed(
 |det H[{j,k},{r,s}]|
 > (2411/6450) gamma^2
 >0.373798 gamma^2.
)`                                                                   (3.2)

The statement uses the ACTUAL original-coordinate cross block `H`, not the normalized matrix `Z`, and does not require the anchor entry `H_jr` to be nonzero.

### Proof

Suppose (D) fails. Then there are `k!=j`, `s!=r` such that

`|p_k|>1/sqrt(2)`, `|q_s|>1/sqrt(2)`,

so

`|p_k q_s|>1/2`.                                                     (3.3)

By (2.4)-(2.5),

`|M_H(k,s)|
 >= h_1 h_2 sqrt(L_jR_r)|p_kq_s|-||E||_op`

`> h_1h_2 [ (1/2)(6221/6450) - 3/200 ]`.                          (3.4)

Using (1.4),

`|M_H(k,s)|
 > (4/5) gamma^2 [ 6221/12900 - 3/200 ]`

`= (2411/6450) gamma^2`.                                          (3.5)

Since `M_H(k,s)` is exactly `det H[{j,k},{r,s}]`, this proves (P). QED.

### 3.2 Geometry of the wedge-diffuse survivor

The alternative (D) has a useful coordinate interpretation. On the left, choose an orthonormal basis `s,p` for the top-two left singular plane so that

`s_j=sqrt(L_j)`, `p_j=0`,                                         (3.6)

and the residual coordinates of `p` are exactly (2.1), up to an irrelevant sign. Then

`sum_(k!=j)s_k^2=1-L_j <229/6450`.                                (3.7)

Hence if the left side of (D) holds, for every `k!=j` the top-two-plane leverage obeys

`u_1(k)^2+u_2(k)^2=s_k^2+p_k^2`

`< 1/2 +229/6450`

`=1727/3225`

`<0.535504`.                                                       (3.8)

The symmetric statement holds on the right. Thus failure of the physical-minor payment forces a genuine one-sided diffuse *second top-two direction after removing the near-coloop anchor*. This is substantially narrower than the previous generic “small higher-rank tail” description.

## 4. The physical-minor branch is analytically paid without selecting a spectral fiber

Assume branch (P), and write

`d=det H[{j,k},{r,s}]`,

so by (3.2)

`|d| > c_0 gamma^2`, `c_0=2411/6450`.                              (4.1)

Condition on every residual ORIGINAL coordinate except the four coordinates indexed by `{j,k}` on the left and `{r,s}` on the right. The surviving four variables remain independent with their original one-dimensional density caps at most one. All couplings to the conditioned coordinates become affine terms. The surviving cross block is the physical `2 x 2` matrix

`C=H[{j,k},{r,s}]`,

which has rank exactly two because `d!=0`.

Input B therefore applies uniformly in the conditioning. Since the only double-incident determinant in this `2 x 2` block is `d`, (1.7) gives the conditional estimate

`||p_(R|outside)||_3
 <=3^(2/3)2^(1/3)|d|^(-1/3)`.                                    (4.2)

Averaging the conditional densities and using Minkowski preserves the same `L^3` bound:

`boxed(
 ||p_R||_3
 <=3^(2/3)2^(1/3)c_0^(-1/3) gamma^(-2/3).
)`                                                                  (4.3)

This is exactly where original-coordinate product structure is used. No general rotation is declared independent, and no conditional spectral-density cap is introduced.

## 5. Actual fleet04 square-kernel application

Starting from the completed fleet04/B18 inequality (1.8), let

`M=||p_R||_3`.

For any `U>0`, Holder with exponents `3` and `3/2` on `[0,U]` gives

`int_0^U p_R(t-u)u^(-1/2)du
 <=2^(4/3) M U^(1/6)`.                                            (5.1)

Using total mass one on `[U,infinity)` gives

`int_U^infinity p_R(t-u)u^(-1/2)du <=U^(-1/2)`.                  (5.2)

Optimizing (5.1)+(5.2) over `U` yields

`sup_t int_0^infinity p_R(t-u)u^(-1/2)du
 <= (8/3^(3/4)) M^(3/4)`.                                       (5.3)

Substitute (4.3) into (1.8) and (5.3):

`||p_Q||_infinity
 <= [8 2^(1/4)/3^(1/4)]
    c_0^(-1/4) /sqrt(|a|gamma)`.                                (5.4)

The exact arithmetic checker records

`[8 2^(1/4)/3^(1/4)](6450/2411)^(1/4)
 =9.245018792477305...`.

Therefore the heavy-heavy wedge branch satisfies the concrete bound

`boxed(
 ||p_Q||_infinity
 < 9.25 / sqrt(|a| gamma).
)`                                                                  (5.5)

This is an actual application of the completed fleet04 dependence-safe square mechanism to the new physical-minor inequality. It proves absolute continuity and essential boundedness in branch (P). It does not by itself prove continuity.

## 6. What changed relative to r20

The previous B06 mechanism paid the **exact rank-one Schur-minor endpoint** after a weighted preconditioner, but a small nonzero orthogonal tail could not be discarded uniformly. The current argument changes the mechanism:

1. it works with the **actual physical cross block** from fresh fleet03/B08 r22, not with a perturbative characteristic-function comparison;
2. it uses the leading exterior-plane geometry to ask whether the two incident Pluecker directions are physically heavy;
3. if they are, the small higher-rank tail cannot hide the determinant: a single actual physical `2 x 2` minor is forced above `0.373798 gamma^2` and is paid by conditioning on only original coordinates;
4. if they are not, the survivor has the explicit wedge-diffuse leverage bound (3.8), rather than merely “near rank two.”

The theorem also covers the case `H_jr=0`; no Schur division by the anchor cross entry is needed in the paid branch.

## 7. Remaining implication

The new exact local debt is

`QFORM-WEDGE-DIFFUSE-SCHUR-WINDOW-v1`:

> Starting from the surviving bicolooop state and, say, `max_(k!=j)p_k^2<=1/2`, combine the near-coloop anchor with the diffuse second top-two direction in a product-preserving *spectral-window* or grouped-coordinate estimate that retains the nonzero higher-rank tail. The target is an `L^p`, `p>2`, residual density or an equivalent small-ball exponent `>1/2`, followed by the already-valid dependence-safe outer square. The proof may not replace the full range projection by the top-two plane without paying the tiny tail, because the live small-tail continuity correction forbids that shortcut.

The quantitative leverage observation (3.8), `1727/3225<0.536` outside the anchor, is intended currency for such a spectral-window estimate: it is already below the `3/4` leverage threshold corresponding to any fractional-ridge exponent `q<3/2`, but a future proof must make that statement for a weighted window that legitimately includes the nonzero tail rather than for the bare top-two truncation.

The separate global problem of obtaining a universal lower bound for the structural scale `|a|gamma`, and the zero/near-zero outer-pivot sibling, remain outside this local branch theorem.

## 8. Computation and integrity

The deterministic checker in this run verifies:

* `(4/5)[(6221/6450)/2-3/200]=2411/6450=0.3737984496...`;
* the wedge-diffuse outside-anchor top-two leverage cap is exactly `1727/3225=0.5355038759...`;
* the paid-branch square constant is `9.2450187924...<9.25`.

Checker source commit: `672ead726a0c19af06c3c9616a0b69aa701c06b7`.  
Checker output commit: `d7f98864ff2737e07607c77442cbf7eac3150d6e`, terminating `STATUS=PASS`.

These computations only verify exact arithmetic; the proof is the exterior-square decomposition, the source-pinned conditional theorem, and the inequalities above.

## 9. Status

**Proved in this run:** `QFORM-BICOLOOP-WEDGE-DIFFUSE-OR-PHYSICAL-MINOR-v1`, including the paid physical-minor branch (5.5) and the wedge-diffuse leverage sharpening (3.8).

**Not proved:** the full QFORM conjecture; the wedge-diffuse Schur-window implication; a universal lower bound on `|a|gamma`; the zero/near-zero outer-pivot sibling; or continuity.

Repository transport is not native brain ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`. No scheduler, task, notification, email, Drive, public-release, paid-API, Codex, credential, or cross-account action is part of this result.
