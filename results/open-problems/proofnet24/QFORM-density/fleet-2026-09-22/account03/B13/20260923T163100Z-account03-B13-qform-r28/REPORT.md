SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T16:31:00Z.
attacking: replace the noncoercive Euclidean transverse-radius alternative by an exact residual-quadratic pair-count inequality on purified product-set slab witnesses.

# account03/B13 — residual-energy pair counting on extremal product slabs

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.  
Status: **NEW SUPPORTING GEOMETRIC THEOREM / NEW INTERMEDIATE-CURRENCY CORRECTION / FULL QFORM OPEN / FULL CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

The target remains: independent real coordinates with densities `0<=f_i<=1`, symmetric `A`, at least three eigenvalues of modulus at least one, and a dimension/law/matrix-independent density bound. No post-rotation independence, moment, connected-support, compact-support, Gaussian or log-concavity hypothesis is introduced below.

## 1. Fresh source-pinned inputs actually used

### 1.1 Designated partner: exact extremal-product reduction

Source:

`yspennstate/math-open-problems@82f9b7e9372c2434f27fd1f5a65e7148663516a7`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T121154Z-account04-B13-nonattained-bathtub-r1/REPORT.md`.

For every nonnegative measurable kernel `K:R^n->[0,infinity]`, the partner proves

`sup_{0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx
 = sup_{|E_i|=1} int_{prod_i E_i} K(x) dx`.                         (1.1)

No optimizer is required. For bounded slab kernels the right side can be approximated by bounded finite unions of intervals, but there is **no uniform diameter, component count, single-interval, or centered-uniform reduction**.

A short proof, to pin the precise scope used here: freeze every coordinate except `i`; the functional is `int g_i(t) f_i(t) dt` with `g_i>=0`. The bathtub principle replaces `f_i` by the indicator of a measure-one superlevel set of `g_i` without decreasing the value. Starting from an epsilon-maximizer and doing this successively in all coordinates gives an all-indicator product with no loss. Truncate `K` and use monotone convergence for an unbounded nonnegative kernel. This proves (1.1) without a joint attainment assertion.

### 1.2 Exact diffuse retained-range density theorem

Source:

`yspennstate/math-open-problems@9d9e2369ad137664a48b1b7c6d682ddaed62bcad`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T125929Z-account01-B13-qform-auto23/FRESNEL_RANGE_ADDENDUM.md`.

In the form already compiled and proved in my preceding run, if `R` is a real symmetric physical-coordinate matrix of rank `d>=3`, its range projection `P_R` satisfies

`max_j (P_R)_{jj} <= 1/2`,                                        (1.2)

and arbitrary affine coefficients are allowed, then the output

`X^T R X + ell^T X + c`                                           (1.3)

has a continuous density bounded by

`M(R) = [4d/(d-2)] |pdet R|^(-1/d)`.                              (1.4)

The estimate is uniform in `ell,c`. The underlying proof factorizes only in the original independent coordinates; the spectral decomposition is used solely on the deterministic coefficient matrix.

My preceding B13 theorem also checked that disjoint outside original coordinates may be conditioned first, so arbitrary cross couplings become affine coefficients and do not alter (1.4). That source is

`yspennstate/math-open-problems@<preceding-run-commit-as-published>`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T151646Z-account03-B13-qform-r28/REPORT.md`.

The present argument only needs the special case (1.3), so it does not depend on any unproved crossing reduction.

### 1.3 Current continuation/corrections


`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md`

and its `extremal_laws/REPORT.md`. In particular I do not use the open `(SP)` proposal, an arbitrary-joint coarea bound, conditional-density supremum shortcuts, independence after rotation, uniform pointwise quadratic-phase decay, or a uniformly good single minor.

## 2. Why the preceding Euclidean transverse radius is the wrong closing currency

Let `A` be symmetric and split it spectrally at a threshold `tau>0`:

`R = 1_{|A|>=tau} A`,
`E = A-R`.                                                         (2.1)

Then `R E=E R=0`, `||E||_op<tau`, and if `P` is the range projection of `R`, then `E=P^perp E P^perp`.

The preceding B13 result bounded the conditional slab mass in Euclidean balls of the low-spectral variable. That inequality is valid, but **large Euclidean low-spectral radius is not coercive**: exact null directions can be arbitrarily spread without affecting `Q` at all. The repair is to measure the exact residual quadratic error

`q_E(x-z) := (x-z)^T E (x-z)`                                     (2.2)

rather than `||P^perp(x-z)||^2`.

This retains precisely the part of the low-spectral displacement that can alter the quadratic form. It also automatically vanishes on true null directions and respects indefinite cancellation rather than replacing it by an operator-norm upper bound.

## 3. First essential missing implication: exact one-centre residual localization

Assume

`d=rank R >=3`, `max_j P_jj<=1/2`.                                (3.1)

Put

`M := [4d/(d-2)] |pdet R|^(-1/d)`.                                (3.2)

Let `Q(X)=X^TAX`, let `J` be an interval of length `L>0`, and define

`S={Q in J}`, `m=P(S)=rho L`.                                     (3.3)

For an arbitrary deterministic `z in R^n`, define the exact affine model

`Q_z(X) := Q(X) - (X-z)^T E(X-z)`.                                (3.4)

Because `A=R+E`, expansion gives

`Q_z(X)=X^T R X + 2 z^T E X - z^T E z`.                           (3.5)

Thus (1.4) applies uniformly in `z`:

`||p_{Q_z}||_inf <= M`, and `p_{Q_z}` is continuous.               (3.6)

For `delta>=0`, set

`H_z(delta)={ |(X-z)^T E(X-z)| <= delta }`.                        (3.7)

On `S cap H_z(delta)`, equation (3.4) implies

`Q_z in J+[-delta,delta]`,                                        (3.8)

an interval of length `L+2delta`. Hence

`P(S cap H_z(delta)) <= M(L+2delta)`.                              (3.9)

Dividing by `m=rho L` proves:

### Theorem 3.1 — `QFORM-SLAB-RESIDUAL-ONE-CENTRE-v1`

Under (3.1), for every deterministic centre `z` and every `delta>=0`,

`boxed:
 P( |(X-z)^T E(X-z)|<=delta | Q in J )
 <= (M/rho)(1+2delta/L).`                                         (3.10)

This is strictly sharper than the Euclidean transverse-ball estimate in the following sense: since

`|(x-z)^TE(x-z)| <= tau ||P^perp(x-z)||_2^2`,                     (3.11)

every radius-`r` Euclidean low-spectral ball is contained in `H_z(tau r^2)`, so the preceding inequality follows from (3.10). The converse fails maximally when `E` has a nullspace.

No support size or moment appears in (3.10).

## 4. Main new theorem: a two-sample residual-energy pair-count inequality

Let `X'` be an independent copy of `X`. For fixed `x'`, choose

`z=P^perp x'`.                                                     (4.1)

Because `E=P^perp E P^perp`,

`(X-z)^T E(X-z)
 = (X-X')^T E(X-X')`                                              (4.2)

when `X'=x'`. Apply (3.9) to the `X`-variable for this deterministic centre and then integrate only over `x' in S`. We obtain

`P( X in S, X' in S,
    |(X-X')^T E(X-X')|<=delta )
 <= m M(L+2delta).`                                                (4.3)

Since `P(X in S,X' in S)=m^2`, division yields:

### Theorem 4.1 — `QFORM-SLAB-RESIDUAL-ENERGY-PAIR-COUNT-v1`

Under (3.1), for every interval `J` of length `L>0`, every `delta>=0`, and every slab ratio `rho=P(Q in J)/L>0`,

`boxed:
 P( |(X-X')^T E(X-X')|<=delta
    | Q(X) in J, Q(X') in J )
 <= (M/rho)(1+2delta/L).`                                         (4.4)

This is an **actual two-copy geometric small-ball inequality inside the bad slab**. It does not ask for a common fibre centre, a bounded support radius, or finite moments. The two slab points themselves generate the centre.

### Quantile form

For `0<eta<1`, let

`Delta_{E,eta}(S)
 := inf{delta>=0:
       P(|(X-X')^TE(X-X')|<=delta | X,X' in S)>=1-eta}`.           (4.5)

Then (4.4) gives

`boxed:
 Delta_{E,eta}(S)
 >= (L/2) ((1-eta)rho/M - 1)_+ .`                                 (4.6)

If every retained eigenvalue has modulus at least `tau`, then

`|pdet R|^(1/d)>=tau`,
`M <= [4d/(d-2)]/tau <= 12/tau`.                                  (4.7)

Consequently, for the median pair-energy scale (`eta=1/2`),

`boxed:
 Delta_{E,1/2}(S)
 >= (L/2) (tau rho/24 -1)_+ .`                                    (4.8)

Thus a high-ratio slab cannot merely be geographically broad in directions irrelevant to the polynomial: **a positive fraction of pairs of slab points must be separated by a quantitatively large amount of actual residual quadratic action**.

When `E=0`, the left side of (4.4) is one already at `delta=0`, and the theorem immediately gives `rho<=M`. So the exact diffuse retained-range branch closes with no fictitious spread alternative.

## 5. Pure product-set geometric form, and the designated partner applied at the actual inequality

By the account04/B13 theorem (1.1), the slab functional may be tested on unit-measure product sets without loss in the supremum. Let

`B=E_1 x ... x E_n`, `|E_i|=1`,
`S_B={x in B: x^T A x in J}`,                                     (5.1)

and let `|S_B|=rho_B L`. Then (4.3), now interpreted as Lebesgue measure on `B x B`, becomes the geometric additive-energy inequality

`boxed:
 |{(x,y) in S_B x S_B:
     |(x-y)^T E(x-y)|<=delta}|
 <= |S_B| M(L+2delta).`                                           (5.2)

Equivalently,

`|{...}|/|S_B|^2
 <= (M/rho_B)(1+2delta/L).`                                       (5.3)

This is the requested attack on the **resulting geometric sublevel-set problem** after product purification.

The application to arbitrary cap-one laws is literal: if a slab ratio `rho` is approached by admissible densities, (1.1) produces unit-measure product indicators with slab ratios approaching the same `rho`; each such product witness obeys (5.2)-(5.3). Bounded finite-union witnesses may be used by approximation, but neither the number of fragments nor their diameter is controlled. No interval extremality is asserted.

This use of account04/B13 is essential rather than cosmetic: the stress example in Section 6 is itself a fragmented product indicator, and it shows exactly why a bounded-diameter strengthening of the partner theorem would be false.

## 6. New correction: Euclidean transverse radius is noncoercive even on half of the slab mass

### Proposition 6.1 — `QFORM-EUCLIDEAN-TRANSVERSE-RADIUS-NONCOERCIVE-v1`

There is a target-valid family for which the conditional low-spectral Euclidean half-mass radius tends to infinity while the quadratic form and its slab law are completely unchanged and the exact residual `E` is zero.

#### Construction

Take `n=7`. For `k=1,2,3` put

`v_1=(e_1+e_4)/sqrt(2)`,
`v_2=(e_2+e_5)/sqrt(2)`,
`v_3=(e_3+e_6)/sqrt(2)`,                                          (6.1)

and

`A=P=sum_{k=1}^3 v_k v_k^T`.                                     (6.2)

Then `P^2=P`, its spectrum is

`{1,1,1,0,0,0,0}`,                                                (6.3)

and

`diag P=(1/2,1/2,1/2,1/2,1/2,1/2,0)`.                            (6.4)

Hence the high spectral range is exactly at the diffuse leverage gate `max P_jj=1/2`, while at threshold `tau=1` the residual `E=A-R` is exactly zero.

Let `X_1,...,X_6` be any independent cap-one laws, for instance uniforms on `[-1/2,1/2]`. Let `X_7` be uniform on the unit-measure fragmented set

`F_R=[0,1/3] union [R,R+1/3] union [2R,2R+1/3]`,                  (6.5)

with `R>1`. Then

`Q=X^TAX
 = (1/2)[(X_1+X_4)^2+(X_2+X_5)^2+(X_3+X_6)^2]`,               (6.6)

so `Q` is independent of `X_7`. Therefore, conditioned on **any** positive-probability slab `{Q in J}`, the `X_7` law remains uniform on `F_R`.

Any Euclidean ball of radius `r` in the low-spectral subspace projects onto an interval of length at most `2r` in the seventh coordinate. An interval of length `<R-1/3` intersects at most one component of `F_R`, hence carries at most `1/3` of the `X_7` mass. Thus any low-spectral Euclidean ball carrying at least one half of the conditional slab mass must obey

`r >= (R-1/3)/2`.                                                  (6.7)

This diverges with `R`, although `E=0` and the law of `Q` is independent of `R`.

So the preceding Euclidean anti-concentration theorem remains mathematically correct, but the inference

`large conditional low-spectral Euclidean radius => useful unpaid QFORM currency`

is false. The exact residual-energy replacement (4.4) repairs precisely this defect: here `(X-X')^TE(X-X')=0` identically, and (4.4) returns the correct direct payment `rho<=M`.

This proposition is an intermediate-mechanism correction, **not** a counterexample to the QFORM conjecture.

## 7. What this does and does not close

This run closes the defect in the previous B13 obstruction: irrelevant null-space fragmentation can no longer masquerade as useful geometric spread. In the diffuse retained-range branch, every high-ratio product witness now forces a **positive-mass, translation-free, curvature-weighted pair separation** (4.6), not merely a large support radius.

It does **not** yet pay that residual separation. The remaining implication is

`QFORM-RESIDUAL-PAIR-ENERGY-TO-PHYSICAL-CERTIFICATE-v1`:

> Given the purified product-set slab `S_B`, diffuse retained range `R`, and the lower bound (4.6) for the residual quadratic pair energy, convert this positive two-sample energy into either (i) a physical grouped-bank/cross-volume certificate already covered by a completed density theorem, or (ii) a multiscale lowering of the spectral threshold which supplies a new diffuse rank-three retained packet. The conversion must preserve original-coordinate product provenance and may not use moments or same-fibre overlap.

A natural next mechanism is spectral multiscale rather than another radius argument: decompose `E` into dyadic spectral bands and use (4.6) to show that one nonzero band carries positive slab-pair quadratic action. If that band has rank at least three and diffuse physical leverage, it can be promoted into the retained model and paid by the same theorem; the hard survivor is a finite sequence of rank-one/rank-two or high-leverage bands, which should interface with the fleet's hub/pair compilers.

## 8. Status

Full QFORM: **OPEN / not proved / not disproved**.  
Global continuity: **OPEN**.  
Continuity proved here only for each affine model `Q_z`; the pair-count transfer does not by itself prove continuity of the actual full `Q`.

New proved supporting results:

1. `QFORM-SLAB-RESIDUAL-ONE-CENTRE-v1`, equation (3.10).
2. `QFORM-SLAB-RESIDUAL-ENERGY-PAIR-COUNT-v1`, equations (4.4)-(4.8).
3. Pure product-set geometric energy inequality (5.2), after actual application of account04/B13 purification.
4. `QFORM-EUCLIDEAN-TRANSVERSE-RADIUS-NONCOERCIVE-v1`, the exact target-valid stress family (6.1)-(6.7).

No scheduler/task state, cadence, notification setting, email delivery, public release, remote workflow, paid API/model call, Codex execution, or cross-account authentication was changed.
