SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B12, 2026-09-22T19:54:53Z.
attacking: exact stability and failure modes of scalar Schur elimination when one genuinely new spectral eigenvalue is added to a three-large-eigenvalue core.

# fleet02/B12 — exact spectral-spike Schur law and certificate switching

**Programme:** QFORM-DENSITY-3EIG-20260922.  
**Owner control read:** math-research-brain control revision 2026-09-22.15, fresh main read through commit `22ca56c8fd5979d70bd01f5a96ff801da084bc2c` before scientific publication.  
**Assignment:** Additional eigenvalue control.  
**Classification:** `PROVED_SUPPORTING_STABILITY_THEOREM + EXACT_TARGET_CLASS_MECHANISM_BARRIER / FULL_TARGET_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction discipline

The full target remains open: independent real coordinates with densities bounded by one, and an arbitrary symmetric matrix with at least three eigenvalues of absolute value at least one, should give a quadratic-form density bounded by one universal constant.

This report uses only original-coordinate conditioning. It does not rotate the product source and then claim independence; it does not take a worst normalized conditional fiber; and it does not use the corrected-away arbitrary-joint-density coarea claim. The live corrections `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`, and `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` are respected.

The completed named partner result actually applied is fleet03/B12:

- repository `yspennstate/math-open-problems`
- commit `b3c543b40dfaef13468466fa82625303a7719af8`
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`
- theorem `QFORM-TWO-SAMESIGN-THREEBLOCK-v1`.

It states that if one physical original-coordinate principal `3x3` block has two eigenvalues of the same sign and magnitude at least `L`, while the third is arbitrary, then after conditioning all outside original coordinates the full quadratic form has density cap

`||p_Q||_infinity <= C_*/L`,

where

`C_* = 2*pi + 3*sqrt(3) + sqrt((2*pi+3*sqrt(3))^2 + 3*pi^2)`

`    = 24.183038289961516...`.

All outside coefficients and cross couplings are allowed in that theorem.

## 2. A commuting one-eigenvalue addition with an exact scalar-Schur law

Fix `sigma in {+1,-1}`, `0<q<1`, and

`v_q = (sqrt(q), sqrt(1-q), 0, 0)^T`.

Start from the rank-three core

`A_0 = 2 sigma (I_4 - v_q v_q^T)`

and add the genuinely new spectral direction

`tau v_q v_q^T`.

Because `v_q` is exactly the kernel eigenvector of `A_0`, this is a commuting spectral addition, not merely an arbitrary matrix perturbation. The final matrix is

`A_{sigma,q,tau} = 2 sigma I_4 + (tau-2 sigma) v_q v_q^T`,

with exact spectrum

`{2 sigma, 2 sigma, 2 sigma, tau}`.                         (2.1)

Hence for every real `tau` the matrix remains in the QFORM target class: it always has three eigenvalues of modulus `2`.

Use original coordinate 1 as a scalar pivot. Its coefficient is

`a = 2 sigma (1-q) + tau q`.                                 (2.2)

Whenever `a != 0`, direct Schur complementation in the original coordinates gives

`Sc_1(A_{sigma,q,tau})`
`  = diag( 2 sigma tau/a, 2 sigma, 2 sigma ).`                (2.3)

Thus the added eigenvalue is transformed by scalar Schur elimination through the exact fractional-linear map

`tau -> 2 sigma tau / [2 sigma (1-q)+tau q]`.                 (2.4)

The only pole is the genuine physical-pivot cancellation `a=0`.

### Proof

The spectrum in (2.1) follows because `A` acts by `tau` on `v_q` and by `2 sigma` on `v_q^perp`. In coordinates 1 and 2, the matrix has eigenvalues `2 sigma` and `tau`, hence determinant `2 sigma tau`. Its first diagonal pivot is (2.2). The Schur determinant identity therefore gives the remaining one-dimensional Schur eigenvalue `(2 sigma tau)/a`. Coordinates 3 and 4 are untouched eigenvectors with eigenvalue `2 sigma`, proving (2.3). The symbolic checker independently expands the Schur complement and verifies the same identity.

## 3. Positive stability theorem: the full density is uniform for every added eigenvalue

The complementary physical block on coordinates `{2,3,4}` is

`B = 2 sigma I_3 + (tau-2 sigma)(1-q) e_1 e_1^T`.             (3.1)

Its eigenvalues are exactly

`2 sigma, 2 sigma, 2 sigma+(tau-2 sigma)(1-q)`.               (3.2)

So, independently of the sign and magnitude of `tau`, this physical block always has two same-sign eigenvalues of magnitude `2`. Applying the completed fleet03/B12 theorem with `L=2` proves

`||p_{X^T A_{sigma,q,tau} X}||_infinity`
`   <= C_*/2`
`   = 12.091519144980758...`                                  (3.3)

for every independent cap-one product source, every `0<q<1`, every `tau in R`, and both core signs `sigma`.

This is a genuine arbitrary-added-eigenvalue stability theorem: the fourth eigenvalue may be zero, arbitrarily small, arbitrarily large, same-sign, or opposite-sign. No convolution with the added quadratic term is asserted; the proof switches to a physical block and conditions only original coordinates.

## 4. Small added eigenvalue can make a fixed Schur remainder arbitrarily large

Take `sigma=+1`, `q=1-epsilon`, `0<epsilon<1/2`, and choose

`tau_small = (epsilon^2-2 epsilon)/(1-epsilon)`
`          = -epsilon(2-epsilon)/(1-epsilon)`.                (4.1)

Then the added spectral eigenvalue tends to zero:

`|tau_small| <= 3 epsilon -> 0`,                               (4.2)

while the final physical pivot is

`a = epsilon^2`.                                               (4.3)

Equation (2.3) gives

`Sc_1(A) = diag(s_epsilon,2,2)`,

`s_epsilon = -2(2-epsilon)/[epsilon(1-epsilon)]`,              (4.4)

so

`|s_epsilon| > 4/epsilon -> infinity`.                         (4.5)

For the unperturbed rank-three core `tau=0`, the same pivot has Schur complement `diag(0,2,2)`. Thus an added eigenvalue whose magnitude goes to zero can change this fixed physical Schur remainder by an arbitrarily large operator norm, even though the final matrix always has three eigenvalues exactly equal to `2` and its full output density is uniformly bounded by (3.3).

Quantitatively: for every `eta>0` and `M>0`, choosing

`epsilon < min(1/2, eta/3, 4/M)`

produces `|tau_small|<eta` but

`||Sc_1(A_{+,1-epsilon,tau_small})-Sc_1(A_{+,1-epsilon,0})||_op > M`.   (4.6)

Global sign reflection gives the same construction with a positive small added eigenvalue and three core eigenvalues `-2`.

Therefore **there is no dimension-free fixed-pivot Schur stability modulus depending only on the norm/magnitude of the newly added eigenvalue**. Any small-tail Schur perturbation lemma must retain a physical pivot-gap denominator or switch certificates when the pivot nearly cancels.

## 5. Arbitrarily large added eigenvalue has the same fixed-pivot failure

The phenomenon is not confined to small added eigenvalues. Set `sigma=+1`, `q=epsilon`, `0<epsilon<1/3`, and choose the final pivot to be `a=epsilon`, i.e.

`tau_large = (epsilon-2(1-epsilon))/epsilon`
`          = 3-2/epsilon`.                                    (5.1)

Then

`|tau_large| = 2/epsilon-3 >= 1/epsilon -> infinity`,          (5.2)

but (2.3) gives

`s_epsilon = 2 tau_large/epsilon`
`          = 6/epsilon - 4/epsilon^2`,                         (5.3)

hence, for `epsilon<=1/3`,

`|s_epsilon| >= 2/epsilon^2 -> infinity`.                      (5.4)

Again the full output density stays bounded by `C_*/2`; again global sign reflection realizes a positive arbitrarily large added eigenvalue against a negative three-eigenvalue core.

Thus both smaller and larger extra eigenvalues of either sign can drive one fixed scalar Schur certificate through an arbitrarily bad Möbius pole without creating any target-level density pathology.

## 6. What this changes and what remains unpaid

This report does **not** refute QFORM. It proves the opposite for the entire family (2.1): a uniform density cap survives every value of the extra eigenvalue.

The mechanism-level conclusion is sharp and source-valid:

1. spectral addition itself can be perfectly benign for the full product-law density;
2. a fixed scalar Schur representation can nevertheless become arbitrarily ill-conditioned under an arbitrarily small or arbitrarily large genuinely new eigenvalue;
3. therefore recursive extra-eigenvalue arguments cannot use `||added spectral tail||` alone to control a chosen Schur remainder;
4. near a pivot cancellation, a proof must either retain the exact pivot-gap price or switch to another physical block / aggregate certificate before taking inverse local quantities.

The fleet03/B12 two-same-sign-threeblock theorem supplies exactly such a switch on this stress family. The full target still requires a dimension-free mechanism ensuring an appropriate switch or aggregate payment for an arbitrary symmetric matrix with only three globally large eigenvalues; the live corrections show that no single uniformly good local principal block is forced in general.

## 7. Checker

`check_spectral_spike_schur.py` verifies symbolically:

- the pivot identity (2.2);
- the exact Schur spectrum (2.3);
- the fact that the complementary physical triple always has two eigenvalues exactly `2` in the `sigma=+1` normalization;
- the small-spike formulas (4.1)-(4.4);
- the large-spike formulas (5.1)-(5.3).

The recorded checker output is `PASS`.

## 8. Status

**Target-level movement:** `OPEN -> OPEN`. No universal QFORM constant is proved for arbitrary matrices.  
**Mechanism-level movement:** new exact barrier plus a source-valid stability switch. The fixed-pivot Schur-tail architecture is proved nonuniform even under a commuting one-eigenvalue spectral addition inside the exact target class, while the named partner theorem proves the full density remains uniformly bounded on the same family.
