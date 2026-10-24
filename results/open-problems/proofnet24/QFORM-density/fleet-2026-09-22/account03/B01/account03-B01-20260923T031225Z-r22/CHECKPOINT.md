SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T03:12:25Z.
attacking: optimized signed-Fejer closure for the robust grouped 2+1 near-null branch, using the sharp two-dimensional product-projection cap and a scale-normalized split.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T031225Z-r22`  
Status: supporting quantitative improvement; full QFORM remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source-pinned setup

Use account03/B19 r21, canonical predecessor `yspennstate/math-open-problems@207a77337f6b3587233055160a27b317b2491342`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T010143Z-account03-B19-QFORM-r21/REPORT.md`. Its robust grouped `1+2` packet produces a genuinely independent cap-one scalar `X_0`, a two-dimensional orthogonal projection `Z=U^T X_G` of a disjoint original-product bank, and an active symmetric matrix

`B=[[a,b^T],[b,C]]`

with

`s:=s_min(B)>1/12`, `D:=|det B|>1/12`.

The receiver is an orthogonal two-dimensional marginal of a cap-one product density, so the checked Livshyts--Paouris--Pivovarov marginal theorem gives the sharper joint cap

`M_2<=2`

(r21 used the weaker internal cap `e`).

Account03/B19 r21 proves the scale-correct transverse resource: whenever `r:=|a|/s<1`, after rotating only inside the receiver plane,

`P>= (1-r)D`.

Apply account01/B16 `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1`, canonical `yspennstate/math-open-problems@8d262d18e5581cd02b8ea8be5102aa2a6d30ddd7`, to obtain

`||p_Q||_inf <= 103680^(1/3) M_2^(2/3) (DP)^(-1/6)`
`             <= N_0 (1-r)^(-1/6)`,

where, using `M_2<=2` and `D>1/12`,

`N_0=103680^(1/3) 2^(2/3) 12^(1/3)`.

For `a!=0`, apply `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, canonical `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, exactly as in r21. It gives

`||p_Q||_inf <=16 sqrt(30)|a|^(-1/4)D^(-1/4)`
`             <=F_0 r^(-1/4)`,

where

`F_0=16 sqrt(30) sqrt(12)=96 sqrt(10)`.

Thus for `0<r<1` the best available bound is the minimum of an increasing near-null envelope and a decreasing scalar-Schur envelope. At `r=0` the near-null envelope applies, and for `r>=1` the scalar-Schur envelope applies.

## Exact rational split

Take

`r_0=4849/5000=0.9698`.

For `0<=r<=r_0`, monotonicity gives

`||p_Q||_inf <= N_0(1-r_0)^(-1/6) <306`.

The inequality is exact after taking sixth powers. Since

`N_0^3=103680*4*12=4,976,640`

and `1-r_0=151/5000`, it reduces to

`4,976,640^2 * 5000 < 306^6 *151`,

namely

`123834728448000000 <123966832950161856`.

For `r>=r_0`, monotonicity gives

`||p_Q||_inf <=96 sqrt(10) r_0^(-1/4)<306`.

After fourth powers this is exactly

`96^4*100*5000 <306^4*4849`,

namely

`42467328000000 <42514579705104`.

Therefore the whole robust grouped `1+2` packet is paid by the clean uniform constant

`||p_Q||_inf <306`.

This improves r21's `<362` constant without changing its structural hypotheses. The new ingredient is the sharp two-dimensional orthogonal-product marginal cap `2` plus a scale-normalized optimized split. Continuity is not inferred: the near-null source theorem establishes essential boundedness, not a continuous representative.

The designated partner account04/B01 signed-Fejer theorem will be applied in the final report to the actual `<306` inequality.
