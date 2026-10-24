# account04/B17 FEI handoff — biased Booleanity quadratic-form KL gap

**Status:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_BOOLEANITY_KL_CREDIT`; full FEI remains `OPEN / NOT PROVED`; execution `WITHOUT_VERIFIED_BRAIN`.

**Source-bound scientific artifact:** `yspennstate/math-open-problems`, report commit `603b35e74227d1c2d8ee34c0c527c439c686e30b`, path `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`, report blob `f7a069e0e44ab05ff574807e72973c131c960ca8`. Checker commit `d84e26b7648faf722bbe8d51eba305d1c4204203`, blob `3738068f99d66feab2b0de91f5c2c92fe31df23a`; captured PASS output commit `872cad552b22c1b243f07936b32d721ae51b179d`, blob `dbd9369fbf384fd60ca4c346a17b66c3c8adb190`.

**Named newest compatible other-account B15 consumed:** account03/B15 `20260922T085625Z-product-equality-rigidity`, scientific creation commit `84c69136ca6b008badb76f15bf1071d029c927aa`. It proves `K_occ=0` on the balanced uniform slice iff the gate is character-times-bent, hence decomposable/dictator. Also retained account02/B15's exact arbitrary-potential I-projection identity `R_Gamma=B_inf^Gamma+K_occ` from commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`. The obsolete fixed `Gamma^dagger` is not revived.

## New theorem

For a nonconstant Boolean gate at arbitrary interior product bias, write its full biased Fourier coefficient vector as `a`, output variance `v=V_q`, actual nonempty spectral law `P`, and account02/B15 maximum-entropy matched-marginal law `Q_r`. In the normalized one-bit basis, `phi_i^2=1+kappa_i phi_i` with `kappa_i=(1-2p_i)/sqrt(p_i(1-p_i))`. For every nonempty `U`, the exact Boolean equation is

`a^T M_U a = 0`,

where `M_U` is the tensor product of `I_2` off `U` and `[[0,1],[1,kappa_i]]` on `U`, with exact operator norm

`L_U = product_{i in U} sqrt(max(p_i,1-p_i)/min(p_i,1-p_i))`.

Keep the true signed empty coefficient and replace the nonempty magnitudes by `sqrt(v Q_r(S))`. Define `g_U` to be the minimum absolute value of `b^T M_U b` over all sign choices on those nonempty magnitudes. Then

`K_occ >= g_U^2 / (4 v L_U^2 ln 2)`

for every nonempty `U`, hence

`K_occ >= (1/(4 v ln 2)) max_U g_U^2/L_U^2`.

Proof: choose the actual Fourier signs, compare the candidate vector `b` to `a`, use the Boolean quadratic equation and operator norm to get `g_U <= 2 L_U ||a-b||_2`, then use `||a-b||_2^2 = v * Hellinger^2(P,Q_r)` and `D_2(P||Q_r) >= Hellinger^2/ln 2`. This preserves the entire B15 KL credit and works off-centre; it is not a relaxed spectral argument.

## Adversarial failure and replacement

At the balanced uniform `c<1` B15 endpoint, taking `U` to be the full active set gives the quantitative strengthening `K_occ >= d^2/ln2`, with `d=c^{-1} product_i sqrt(t_i(1-t_i))`.

But this **single-equation** replacement is not influence-relative. For the exact balanced Boolean family obtained by flipping two opposite-sign distance-two vertices of a dictator, with `q_k=2^(2-k)`, one has exactly

`r=(1-q_k,q_k,...,q_k)`, `I-1=(k-2)q_k`, and the I-projection root satisfies `c>=1/2`. Hence `d<=q_k^((k-1)/2)`, so the full-active certificate divided by `I-1` is at most `q_k^(k-2)/((k-2)ln2) -> 0`. This falsifies using only the B15 full-active parity equation as a dimension-free payment mechanism.

The genuinely different replacement is the **all-equations Booleanity bank** `max_U g_U^2/L_U^2`. On the exact `k=5` two-flip source the full-active lower certificate is `0.00003112386407223417...`, while the best Boolean equation gives `0.01157360325406454267...`, about `371.86x` larger. On an exact Boolean `MAJ_3` at rational biases `(3/8,2/5,1/3)`, the biased theorem gives a positive lower certificate `0.0015668153390476566...` against actual `K_occ=0.4748676582334332495...`.

**Next exact obligation:** for the next repaired symmetric potential, compare this all-equations Booleanity bank directly to `[-B_inf^Gamma]_+`, or construct an actual gate/bias where it is still too small. A stronger possible continuation is a joint coercivity estimate combining several `U` equations instead of taking only their maximum. No such universal joint estimate is claimed here.
