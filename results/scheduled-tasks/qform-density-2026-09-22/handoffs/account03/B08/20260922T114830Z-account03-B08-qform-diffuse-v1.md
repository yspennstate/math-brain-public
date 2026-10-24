# account03/B08 handoff — diffuse spectral-frame theorem

Outcome: `ESSENTIAL_STEP_APPLIED`; full `QFORM-DENSITY` target remains OPEN; execution `WITHOUT_VERIFIED_BRAIN`.

Canonical science report: `yspennstate/math-open-problems`, commit `9dcddd0bf3fbcb8e0b3396e0a4d883924d3f4ada`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T114830Z-account03-B08-qform-diffuse-v1/REPORT.md`, blob `022e24d4e6470665c48d7bfb1a3ad5c7963f664a`.

## Fresh control and corrections

The later owner control `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`, superseded the incoming FEI prompt. Required route corrections were observed: law-uniform pointwise one-variable Fresnel decay is false; unrestricted spectral-fiber suprema can lose dimension; diagonalizing `A` destroys coordinate independence. A later inbox event `QFORM-CROSSMINOR-ALONE-FALSE` was also consumed before this handoff; it concerns a different two-block pivot claim and does not challenge the theorem below.

The named partner account04/B08 had no completed current-QFORM handoff on the fresh reads used in this run; no partner theorem was fabricated or assumed. I instead applied the completed other-account result account02/B06, report commit `6902eb62f21a7c833ca27dcca69f34d50e711a7d`, which supplies the exact Sylvester-Hadamard rank-three delocalized adversary to finite-coordinate localization.

## Main proved result

Let `R in R^{n x r}` have orthonormal columns, `r>=3`, and row leverages `c_i=||R_{i,*}||^2<=1/2`. Let `Lambda` be real symmetric invertible. For independent `X_i` with densities `f_i<=1`, and **arbitrary measurable coordinatewise potentials** `V_i`, set

`Y=(R^T X)^T Lambda (R^T X)+sum_i V_i(X_i)`.

Then

`|phi_Y(t)| <= min(1,(pi e)^(r/2)|det Lambda|^(-1/2)|t|^(-r/2))`

and `Y` has a bounded continuous density satisfying

`||p_Y||_infinity <= e r/(r-2) |det Lambda|^(-1/r)`.

Hence if all eigenvalues represented by `Lambda` have magnitude at least `1`, the bound is at most `3e`.

The proof is a nontruncated Fourier–Brascamp–Lieb argument. Sharp Hausdorff–Young gives, for every complex `g` with `|g|<=1`, `||g||_1<=1` and every `p>=2`,

`int |hat g|^p <= 2 pi sqrt(e/p)`.

Writing each nonzero row as `v_i=sqrt(c_i)u_i`, the identity `sum c_i u_i u_i^T=I_r` and rank-one geometric Brascamp–Lieb with exponent `p_i=1/c_i>=2` yield

`int_{R^r} prod_i |hat g_i(<v_i,xi>)| dxi <= (2 pi sqrt(e))^r`.

An `r`-dimensional Fresnel representation of the low-rank quadratic phase then gives the displayed `|t|^{-r/2}` bound. No pointwise decay of an individual input characteristic function is used.

## Applied peer result

For account02/B06's exact family `A=U diag(1,1,-1)U^T` with three normalized Sylvester-Hadamard columns and `n=2^k>=8`, every row leverage is `3/n<=3/8<1/2`. The new theorem therefore proves for every admissible product law

`|phi_Q(t)| <= (pi e)^(3/2)|t|^(-3/2)` and `||p_Q||_infinity<=3e`,

with a continuous representative. Thus the family that defeats every fixed-size physical-coordinate curvature localization is nevertheless target-safe by a genuinely global diffuse-frame mechanism.

## Nontrivial extension

If a set `H` of localized coordinates is conditioned on, write `L=H^c`, `M=R_L^T R_L`, and `W=R_L M^(-1/2)`. Whenever `M>0` and every row of `W` has squared norm at most `1/2`, the same argument gives the uniform conditional and unconditional bound

`e r/(r-2) (det M)^(-1/r)|det Lambda|^(-1/r)`.

This quantitatively complements localized-coordinate conditioning and requires no moment assumptions.

## First unpaid implication

`QFORM-DIFFUSE-OFFDIAGONAL-REMAINDER-v1`: for a general target matrix, selecting diffuse large eigenvectors leaves an orthogonal spectral remainder `C` whose phase `exp(i t X^T C X)` is not coordinatewise-factorized. Extend the diffuse theorem to this arbitrary off-diagonal remainder, or find a different product-preserving payment. This is the exact remaining gap between the proved diffuse theorem and the full conjecture.
