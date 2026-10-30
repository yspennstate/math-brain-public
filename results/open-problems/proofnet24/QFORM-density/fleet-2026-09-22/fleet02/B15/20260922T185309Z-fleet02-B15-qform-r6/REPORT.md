# QFORM fleet02/B15 — scalar-weighted conditional-height moment is false

**Run:** `20260922T185309Z-fleet02-B15-qform-r6`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `REFUTED_INTERMEDIATE_MECHANISM / SOURCE-VALID PRODUCT COUNTEREXAMPLE / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication

The preceding B15 run `20260922T180430Z-fleet02-B15-qform-r5` refuted the worst-level scalar-conditioning gate `sup_b ||rho_{123|Q'=b}||_infinity^(2/3)<infinity`, but its corner singularity was integrable against the scalar-level law. The natural repaired obligation was

`E ||rho_{123|Q'}||_infinity^(2/3) <= C0`.                     (1.1)

This report gives a fixed-matrix cap-one independent product family for which the left side grows at least as `(M/2)^(2/3)`. Thus (1.1) is false. The failure is not caused by a degenerate eigenspace: the matrix below has simple spectrum and exactly three eigenvalues of modulus at least one.

## 2. Fixed target matrix

Let

`H=(1/2)*[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]`.

Then `H` is orthogonal. Put `D=diag(1,2,-3,1/2)` and `A=H D H^T`. Explicitly,

`A=(1/8)*[[1,11,-9,5],[11,1,5,-9],[-9,5,1,11],[5,-9,11,1]]`.

The eigenvalues are exactly `1,2,-3,1/2`; hence exactly three have absolute value at least one, the spectrum is simple, `det A=-3`, and every physical entry is nonzero. For `Y=H^T X`,

`Q=X^TAX=Y1^2+2Y2^2-3Y3^2+(1/2)Y4^2 = Q3+Q'`,

where `Q'=Y4^2/2`. Because the three large eigenvalues are simple and the fourth is strictly smaller in modulus, the large-three/small-remainder split is canonical up to signs.

## 3. Independent cap-one fragmented source

For each integer `M>=1`, let

`E_M = union_{j=1}^M [10j,10j+1/M]`.

Take independent coordinates with densities

`f_1=1_{E_M}`, `f_2=f_3=f_4=1_[0,1]`.

Every marginal is a probability density bounded by one. The physical joint density is `1_{P_M}` for `P_M=E_M x [0,1]^3`, a set of four-dimensional volume one.

The fourth spectral coordinate is

`Y4=(X1-X2-X3+X4)/2`.

Let `Z=(-X2-X3+X4)/2`, supported on `[-1,1/2]`. Conditional on `X1` lying in its `j`th component, write `X1=10j+U_M` with `U_M` uniform on `[0,1/M]`. Hence

`Y4 = 5j + U_M/2 + Z`.

Let `g_M` be the normalized density of `U_M/2+Z`. Its support has length `3/2+1/(2M)<2`. The shifts `5j` are separated by five, so the `M` translated supports are pairwise disjoint. Therefore the density `p_4` of `Y4` is exactly

`p_4(s)=(1/M) sum_{j=1}^M g_M(s-5j)`                         (3.1)

with disjoint summands. Every support lies in `(0,infinity)` because `Y4>=5j-1>=4`. Thus `s -> b=s^2/2` is one-to-one on the entire support.

## 4. Uniform component bound and Renyi lower bound

The variable `X4/2` has density `2*1_[0,1/2]`. Since `Z=X4/2-(X2+X3)/2` is its convolution with a probability law,

`||p_Z||_infinity<=2`.

Convolution with the probability density of `U_M/2` gives

`||g_M||_infinity<=2`.                                       (4.1)

Because `g_M` is a probability density,

`1=int g_M=int g_M^(1/3)g_M^(2/3)<=2^(2/3) int g_M^(1/3)`,

so

`int g_M^(1/3)>=2^(-2/3)`.                                  (4.2)

By the disjoint decomposition (3.1),

`int p_4(s)^(1/3) ds`
` = M*(1/M)^(1/3) int g_M^(1/3)`
` >= (M/2)^(2/3)`.                                           (4.3)

The divergence is entirely source-valid fragmentation: the scalar spectral marginal consists of `M` disjoint translated packets, each carrying mass `1/M`.

## 5. Exact conditional-density identity

Because `H` is orthogonal and the physical joint density is `1_{P_M}`, the spectral vector `Y` has density `rho_Y(y)=1_{S_M}(y)`, where `S_M=H^T P_M`. For almost every `s` with `p_4(s)>0`, the section

`S_M(s)={z in R^3:(z,s) in S_M}`

has three-dimensional volume `p_4(s)`, and a regular conditional density is

`rho_{123|Y4=s}(z)=1_{S_M(s)}(z)/p_4(s)`.

Hence

`||rho_{123|Y4=s}||_infinity=1/p_4(s)`                       (5.1)

for almost every such `s`. Since `Y4>0` almost surely, conditioning on `Q'=Y4^2/2` is equivalent to conditioning on `Y4`. Therefore

`E ||rho_{123|Q'}||_infinity^(2/3)`
` = int p_4(s)[1/p_4(s)]^(2/3) ds`
` = int p_4(s)^(1/3) ds`
` >= (M/2)^(2/3) -> infinity`.                               (5.2)

This is an exact analytic counterexample to (1.1). No asymptotic approximation, moment assumption, rotation-independence assumption, or histogram is used.

## 6. Partner result applied: the actual output stays bounded

The assigned compatible partner result actually applied is fleet03/B15 run `20260922T162724Z-fleet03-B15-r13`, canonical report

`yspennstate/math-open-problems@4813f09ed4f518a1ee172b77a0f1d315989a84e1:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T162724Z-fleet03-B15-r13/REPORT.md`.

That report proves, at worker-candidate scope, that for every fixed symmetric matrix of rank at least three and every cap-one independent product input, `X^TAX` has a density in `C_0(R)` with a finite bound depending only on the fixed matrix. Our `A` is fixed and invertible. Consequently one finite `C_A` controls the whole fragmented family:

`||p_Q||_infinity<=C_A`, `p_Q in C_0(R)`                     (6.1)

uniformly in `M`, while the scalar-conditioned positive moment in (5.2) diverges at least as `M^(2/3)`.

Thus the repaired conditional-height expectation can be arbitrarily worse than the actual output height even for one fixed algebraically generic target matrix. This separates the failed proof interface from the conjecture itself.

## 7. Exact mechanism failure and surviving target

The mixture identity

`p_Q(t)=int p_{Q'}(b) p_{Q3|Q'=b}(t-b) db`                   (7.1)

is valid. The damaging relaxation is moving the output supremum inside the scalar mixture:

`sup_t int p_{Q'}(b)p_{Q3|b}(t-b)db`
` <= int p_{Q'}(b) sup_u p_{Q3|b}(u) db`.                    (7.2)

The fragmented construction makes the right side of conditional-height surrogates diverge, although the left side stays bounded for this fixed `A`. The disjoint scalar packets carry distinct output translations; taking conditional suprema before mixing discards precisely that shift information.

Therefore the first surviving scalar-conditioning obligation is translation-aware: estimate the pointwise mixture in (7.1) before taking `sup_t`, or retain an overlap/packing statistic for the shifted conditional profiles. Neither `sup_b` conditional height nor `E` of a positive conditional-height moment can be a universal bridge.

This is compatible with the live correction `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`, which refutes positive moments after conditioning on the full complement vector. The present construction refutes the scalar-conditioned `2/3` moment itself, on a fixed exact target matrix with a one-dimensional spectral remainder.

## 8. Implication ledger

Under the exact target hypotheses:

1. absolute continuity and fixed-instance regularity remain separate from the universal height problem;
2. the fleet03/B15 fixed-matrix `C_0` theorem supplies bounded continuous output for this family;
3. universal essential boundedness remains OPEN;
4. the scalar worst-level gate is false (preceding B15 run);
5. the scalar-weighted conditional `2/3`-height moment is also false (this run);
6. the next mechanism must retain scalar output translations/overlap before taking a supremum.

No full-QFORM counterexample is claimed.
