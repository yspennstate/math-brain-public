SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T17:20:58Z.
attacking: integrated Fourier estimate — compress the degree-4 Fourier-gate failure into literal scalar/residual-volume or two-star/residual-volume currency without selecting a reciprocal minor.

# Early mathematical checkpoint

Full target status: OPEN. Target-wide universal unweighted `int_R |phi_Q(t)| dt` status: OPEN / not refuted here.

Fresh control source at startup: `yspennstate/math-research-brain@5979a2d02580b5ba175f2a208321546a5d390935`, OWNER CONTROL revision `2026-09-22.15`, current continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.

Designated partner actually used: account02/B02, `yspennstate/math-open-problems@221e2d8972267cfffbb61e119d118f5011f8a265`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T153854Z-account02-B02-qform-fa558934/CHECKPOINT.md`. Its completed degree-4 gate gives: if a physical cross block `B` fails the `q=3/2` fourth-volume row-marginal gate in both orientations, there are a physical row `i` and column `j` such that the joint incident fourth-volume satisfies

`J4(i,j) > E4(B)/2`.

## New dimension-free compression lemma

Reorder this physical row and column first and write, entirely in ORIGINAL coordinate banks,

`B = [[b, r^T], [c, M]]`.

Let `J4` denote the sum of squared `4x4` minors containing the distinguished row and column. Then

`J4^(1/2) <= |b| E3(M)^(1/2) + ||r||_2 ||c||_2 E2(M)^(1/2)`.      (1)

Consequently, on the partner's two-sided degree-4 gate failure,

`max{ b^2 E3(M), ||r||_2^2 ||c||_2^2 E2(M) } > E4(B)/8`.          (2)

This has no dimension factor and no reciprocal pivot.

### Proof of (1)

Let `V` and `W` be the residual column and row Euclidean spaces. The matrix coefficients of the operator from `wedge^3 V` to `wedge^3 W` whose Hilbert--Schmidt norm squared is `J4` are

`det [[b, r_T^T],[c_S,M_ST]]`,  `|S|=|T|=3`.

Expanding along the distinguished row/column identifies this exterior operator, up to an irrelevant sign convention, as

`T = b (wedge^3 M) - (c wedge .) (wedge^2 M) i_r`,

where `i_r : wedge^3 V -> wedge^2 V` is contraction by `r` and `c wedge . : wedge^2 W -> wedge^3 W` is exterior multiplication by `c`. Therefore

`||T||_HS <= |b| ||wedge^3 M||_HS + ||c wedge .||_op ||wedge^2 M||_HS ||i_r||_op`
`          = |b| E3(M)^(1/2) + ||c||_2 E2(M)^(1/2) ||r||_2`,

which is (1), using `||wedge^k M||_HS^2 = E_k(M)`. Then `(a+b)^2 <= 2(a^2+b^2) <= 4 max(a^2,b^2)` and `J4>E4(B)/2` yield (2).

Two useful endpoints are exact/simpler. If `b=0`, (1) gives

`J4 <= ||r||^2 ||c||^2 E2(M)`.

If `b != 0`, every incident minor also has the exact Schur formula

`det B[{i} union S,{j} union T] = b det(M_ST - c_S r_T^T/b)`,

so for the full scalar Schur residual `S_b=M-cr^T/b`,

`J4 = b^2 E3(S_b)`.

The non-divisive inequality (2) is preferable near `b=0` and respects the live correction against selecting a single good cross minor.

## Fourier significance and remaining gap

The first resource in (2) is exactly a scalar physical coefficient times an aggregate residual third volume; the second is a two-star packet times aggregate residual second volume. Both are homogeneous of total matrix degree eight, matching `E4(B)`. They are literal physical-coordinate quantities, so no post-rotation independence is asserted.

Simple geometric-mean interpolation of the scalar `|t|^{-1/2}` Plancherel endpoint with the residual degree-3 sharp-HY tail is only critical: with degree-3 HY parameter `q>=1`, the determinant-cancelling weights give time exponent `2/(q+1)<=1`. Thus (2) is not by itself an unweighted-L1 closure. A further smoothing source (or phase-sensitive cancellation) is genuinely required at this star boundary. The next calculation is to test the two resources against the newer projected-crossing/grouped-hub receiver without dropping its row-marginal and rank hypotheses.
