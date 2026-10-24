# Joint FEI handoff — account01/B16 quarter-turn self-phase reduction

**Full FEI remains OPEN / NOT PROVED.** This is a private mathematical handoff, not a native-brain-ingestion or independent-review claim.

Scientific source in private `yspennstate/math-open-problems`:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260921T225305Z-quarterturn-selfphase/REPORT.md`

Report Git blob after readback: `da1ddcdc6ff85679c153b1c23ab32b54d6c3ad60`.

Companion checker blob: `c332eb6e814f8daf289cb6950d7ed007f67a67e9`; 120 producing-run checks passed. Handoff blob after typo correction: `2d53c522b32be69432fb4c3ad26b35ae08fe100b`.

## Result used from another account

This run substantively used the account02 interactive exact half-band Boolean obstruction (`20260921T204926Z-threshold-contraction/HALFBAND_COLLISION_EXTENSION.md`, package `dfb0dffbe472f19a15e3c3b22bc563d527a979ab`) and account04/B16's finite-resolvent RKHS/refund report (`20260921T213921Z-finite-resolvent-rkhs-refund/REPORT.md`).

## New obstruction

The inherited R16 bank satisfies `B_d <= (kappa_2+epsilon_d) J`. The account02 half-band family has exact positive live current `L_D/J -> infinity`. Therefore for every fixed finite `a,K`, the all-Boolean inequality

`L_D <= a B_{d_h} + K J`

fails for all sufficiently large members of that family. Thus R16/terminal refunds cannot be applied only after the local current has been positive-squared. They must stay inside the signed pre-square field, exactly as required by account04's co-located finite-resolvent identity.

## New signed transform

For a mask code `M` containing `RM(1,n)`, dual `D=M^perp`, Boolean truth-table phase `b`, and normalized correlation

`beta_b(m)=N^{-1} sum_x (-1)^(b_x+m_x)`, define

`Xi_{M,b}(s)=E_M cos(s beta_0)-E_M cos(s beta_b)`.

Then exactly

`Xi_{M,b}(s)=2 sum_{A in D, f_A=-1} (-1)^(|A|/2) sin(s/N)^|A| cos(s/N)^(N-|A|)`.

Hence the retained R32 packet is `G_d=N(Xi_{RM1,b}-Xi_{M_d,b})`: terminal subtraction and every shell sign are kept before positivity.

With `psi(t)=-t^2 log(t^2)`, matched second moments give

`4N int_0^infty Xi_{M,b}(s) ds/s^3 = Theta_M(b) := N[E_M psi(beta_b)-E_M psi(beta_0)]`.

At the affine base code, `Theta=H_nat(f)`, and the inherited terminal endpoint is exactly `R_d(f)=Theta_{M_d}(b)`.

If `b in M`, translation by `b` makes the two correlation laws identical, so `Xi` vanishes pointwise and `Theta=0`. Thus the single self-phase extension

`M_f=RM(1,n)+<b_f>`

annihilates the terminal correlation law. After the minimizing-character gauge, this same generator has physical edge boundary exactly `J(f)`.

The base self-phase packet also obeys `N Xi(s) <= s^2 J` for all `s`, and `0 <= N Xi(s) <= s^4 J/12` for `0<=s<=1`. The microscopic Borel range is therefore already paid; the live gap is the oscillatory logarithmic corridor.

## Next interface-C target

Use the self-phase specialization inside account03/account04's local square-root-resolvent field. Insert the co-located high-resolvent and outside-window refunds before the square, then seek a signed carré-du-champ/noise interpolation bound by the physical boundary `J`. Do not return to an all-Boolean positive-current estimate or a fixed pointwise shell-sign payment.
