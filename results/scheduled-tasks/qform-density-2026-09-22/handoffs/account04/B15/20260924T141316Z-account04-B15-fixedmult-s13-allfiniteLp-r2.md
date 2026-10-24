# account04/B15 handoff — sharpened all-finite-Lp theorem at thirteen eigenvalues

Run: `20260924T141316Z-account04-B15-fixedmult-s13-allfiniteLp-r2`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`

## Source pins

- Pinned manuscript commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- Manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- Manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- New mathematics commit: `a67db2543e806eb1580b95062afc957155350f34`
- New mathematics path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account04/B15/20260924T141316Z-account04-B15-fixedmult-s13-allfiniteLp-r2/THIRTEEN_EIGENVALUE_ALL_FINITE_LP_SHARP.md`

## Proved result

For independent real coordinate densities bounded by (K), arbitrary affine terms, and (s_{13}(A)ge s>0), the quadratic polynomial has a density in every finite (L^p), (p>1). For (2le p<infty),
[
 |p_Q|_p
 le
 left(rac{K^2}{s}ight)^{1-1/p}
 igl(max{3810,160sqrt{2e},p}igr)^{1-1/p}.
]
For (1<ple2),
[
 |p_Q|_p
 le
 left(rac{3810K^2}{s}ight)^{1-1/p}.
]

The proof combines the sharpened graph determinant
[
 |phi_Q(t)|ledet!left(I+rac{t^2}{2pi^2e}M^TMight)^{-1/8}
]
with the order-four physical cut and the audited (3810) pivot bound. The rough-law density passage is justified by Gaussian convolution, uniform Hausdorff--Young bounds, weak (L^p) compactness, and uniqueness of the limiting measure.

## Exact endpoint

The normalized no-pivot branch has
[
 |phi_Q(t)|lemin{1,u/|t|},qquad ule160pisqrt{2e},
]
hence
[
 |p_Q|_ple(160sqrt{2e},p)^{1-1/p}.
]
This gives an (O(hlog(1/h))) interval bound, not the (O(h)) bound needed for (L^infty). The completed bounded-density threshold remains below the original manuscript threshold in newer candidate work, but this report makes no claim beyond the rigorously sourced thirteen-eigenvalue finite-(L^p) theorem. The unrestricted three-eigenvalue conjecture remains open.

## Next use

The (O(p)) family is useful currency for convolution or mixed-hub receivers. Any endpoint improvement must exploit cancellation or a compatible second crossing before absolute values; the critical (1/|t|) envelope alone cannot prove bounded density.
