# r40 prepublication addendum

Fresh control was re-resolved at `yspennstate/math-research-brain@0c48916e7fa8d6f99936add18a6e2a8868499dbe`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live correction inbox was reread and no newer correction invalidating the arguments in `REPORT.md` was found.

## 1. Notation correction

In equation (3.1) of `REPORT.md`, the string `nu_J=beta_J v_J` is a typographical spelling of

`u_J=beta_J v_J`.

There is no additional variable `nu_J`. The proof and matrix (3.10) use `u_J,u_K` throughout.

## 2. Completing the transverse square does not change the three currencies

The cross-star decomposition in Section 2 was written using the original orthonormal pair `(v,w)`, while Theorem 3.1 uses `z=w+(gamma/delta)v`. This is harmless and exact. On each bank, adding the same global multiple `lambda v` to `w`:

- leaves every Pluecker coefficient `v_j w_k-v_k w_j` unchanged;
- leaves the least-squares residual energies `d_J,d_K` unchanged;
- adds `lambda` to both regression slopes, hence leaves the slope gap `alpha_J-alpha_K` unchanged.

Therefore equation (2.7) decomposes the same cross-star mass into exactly the currencies used after completion of the square.

## 3. Partner scope clarification and exact-source application

Account04/B05's published theorem is stated for an **actual original-coordinate** definite physical pair. Section 4's grouped `(Y,Z)` formula is a direct corollary of its elementary two-independent-variable proof, because `Y` and `Z` are genuinely independent disjoint-bank variables, but it should not be confused with the literal statement of the published theorem.

An application inside the theorem's exact published scope is also available on the present Witt packet: if any literal original-coordinate principal pair `C=A[{j,k},{j,k}]` is definite and

`|det C|>=1/16`,

then account04/B05 gives directly

`||p_Q||_(infinity,ess) <= pi/sqrt(|det C|) <=4pi<12.567`,

with all other original coordinates conditioned and with all outside couplings retained. Thus the designated partner result is applied without any extension of its stated source scope.

## 4. Source for the bank linear-density cap

The bound used in (3.12) is the `k=1` case of the product-marginal theorem of Galyna Livshyts, Grigoris Paouris and Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949: for a product probability density `prod f_i` with `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal is bounded by `2^(k/2)`. Hence a unit-norm linear form has density cap `sqrt(2)`, and scaling gives `sqrt(2/s)` and `sqrt(2/(1-s))` for the two bank sums.

## 5. Status

`QFORM-WITT-BANK-GAP-COAREA-v1` remains a scoped supporting theorem. It does not pay nonzero within-bank residual components of the shared-shear direction. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains OPEN. Execution remains `WITHOUT_VERIFIED_BRAIN`.
