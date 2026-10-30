SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T20:09:44Z.
attacking: optimize the first non-Gaussian deficit over all periodic Parseval cube frames, identify near-sharp dense rotated frames, and apply the newest fleet02/B17 global separated-bank barrier to a concrete inequality.

# QFORM B17 — sharp first-order periodic-frame witness constant

Run: `20260923T200944Z-fleet01-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN**  
Continuity: no unrestricted continuity claim.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The full arbitrary-law/arbitrary-matrix target remains **OPEN / NOT PROVED / NOT DISPROVED**. The theorem below sharpens the periodic-diffuse witness analysis only. It respects the live corrections: no generic pointwise Fourier decay, no arbitrary-joint coarea cap, and no post-rotation independence are used.

## 1. Source pins used

The previous B17 Edgeworth theorem is consumed from

`yspennstate/math-open-problems@a1ba664bb0eb87aa086402b959e2503a734c633d:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260922T123638Z-fleet01-B17-qform-diffuse-edgeworth-v1/REPORT.md`.

It proves the following source-valid statement. Let `J=diag(1,1,-1)`, let `v_1,...,v_r in R^3` be a fixed Parseval row pattern,

`sum_j v_j v_j^T = I_3`,

repeat the pattern `m` times with row scale `m^{-1/2}`, and put `A_m=U_m J U_m^T`. For independent physical variables `Unif[-1/2,1/2]`, the physical matrix has exact nonzero spectrum `{1,1,-1}` and, writing

`s(v)=v_1^2+v_2^2`, `t(v)=v_3^2`,

`E_J(v)=(57/32)s(v)^2+(15/4)s(v)t(v)+(3/4)t(v)^2`,

one has

`p_{Q_m}(0)=3 sqrt(2)[1-(20m)^{-1} sum_j E_J(v_j)+O(m^{-2})]`.

The newest designated partner theorem consumed in full is

`yspennstate/math-open-problems@a1ba664bb0eb87aa086402b959e2503a734c633d:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T195641Z-fleet02-B17-QFORM-auto11/REPORT.md`.

It proves a global bound below `3sqrt(2)` for the entire separated architecture `X^2+(a.U)^2-(b.V)^2`, with arbitrary cap-one singleton law and arbitrary unrelated centered-cube leverage profiles.

## 2. New sharp anisotropic lower bound for the Edgeworth penalty

Put

`a=57/32`, `b=15/4`, `c=3/4`.

The key point is that the mixed coefficient is larger than the geometric-mean threshold:

`b^2=225/16 > 4ac=171/32`.

Therefore, for every `s,t>=0`,

`a s^2+b st+c t^2 >= (sqrt(a)s+sqrt(c)t)^2`.

Apply this to every row. Parseval gives

`sum_j s(v_j)=2`, `sum_j t(v_j)=1`.

Hence Cauchy gives the exact universal pattern inequality

`sum_j E_J(v_j)`
` >= sum_j (sqrt(a)s_j+sqrt(c)t_j)^2`
` >= r^{-1}(2sqrt(a)+sqrt(c))^2`
` = (63+2sqrt(342))/(8r)`.

Thus, with total physical dimension `n=rm`, every fixed periodic Parseval cube frame satisfies

`p_{Q_m}(0)`
` <= 3sqrt(2)[1-c_*/n+O(n^{-2})]`,

where

`boxed(c_*=(63+2sqrt(342))/160=0.62491552511133661688...)`.

This strictly sharpens the earlier general coefficient `27/80=0.3375` by a factor about `1.8516`.

This is a witness-side asymptotic statement, not a universal upper bound on `||p_Q||_infty` for arbitrary product laws.

## 3. The constant c_* is asymptotically sharp over row patterns

The inequality is not an artifact of Cauchy. Split the `r` pattern rows into `k` positive-plane rows and `q=r-k` negative-axis rows. For `k>=3`, let the positive rows be

`v_j=sqrt(2/k)(cos(2pi j/k), sin(2pi j/k),0)`, `1<=j<=k`,

which form an equal-norm Parseval frame of the positive plane. Take each of the remaining `q` rows to be `e_3/sqrt(q)`. Then the full pattern is Parseval and has

`sum_j E_J(v_j)=57/(8k)+3/[4(r-k)]`.

Writing `k=lambda r`, the continuous minimizer is

`lambda_* = sqrt(38)/(sqrt(38)+2)`,

or equivalently `k/(r-k)->sqrt(38)/2`. Along integer pairs with this ratio,

`r sum_j E_J(v_j) -> (sqrt(57/8)+sqrt(3/4))^2`
` = (63+2sqrt(342))/8`.

Therefore `c_*` is the **sharp asymptotic first-order coefficient** over all fixed Parseval row patterns.

The extremizing geometry is informative: the fastest periodic approach to the Gaussian obstruction segregates row energy between the two-dimensional positive spectral subspace and the one-dimensional negative subspace in the ratio above. A row that carries both signs pays the strictly excessive mixed coefficient `15/4`.

## 4. A four-row near-sharp pattern

The smallest especially clean near-extremizer has `r=4`, `k=3`:

`v_1=(sqrt(2/3),0,0)`,
`v_2=(-1/sqrt(6),1/sqrt(2),0)`,
`v_3=(-1/sqrt(6),-1/sqrt(2),0)`,
`v_4=(0,0,1)`.

Then `sum v_jv_j^T=I_3` and

`sum E_J(v_j)=25/8`.

Since `n=4m`,

`p_{Q_m}(0)=3sqrt(2)[1-5/(8n)+O(n^{-2})]`.

The coefficient `5/8=0.625` misses the sharp `c_*` by only

`(37-2sqrt(342))/160 = 0.00008447488866338...`.

So a four-row pattern is already within about `1.35e-4` relative error of the best possible first-order periodic-frame rate.

## 5. Exact fully dense rotated stress family

The preceding four-row pattern has structural zeros. To show that the near-sharp mechanism survives genuine physical coupling, rotate the spectral row pattern by the exact rational orthogonal matrix

`O=(1/5007) [[4994,-298,203],[302,4997,-94],[-197,106,5002]]`.

The checker verifies `O^T O=I_3`. Let `w_j=O v_j`, let `W` be the `4x3` matrix with rows `w_j^T`, and set

`A_*=W J W^T`.

Then `W^T W=I_3`, `A_*^3=A_*`, `tr A_*=1`, and `tr A_*^2=3`; hence

`spec(A_*)={1,1,-1,0}`.

Every one of the sixteen entries of `A_*` is nonzero; the smallest absolute entry is

`0.0021833954346771398...`.

Now repeat each row `w_j/sqrt(m)` exactly `m` times. The resulting `4m x 4m` physical matrix is dense entrywise and has exact nonzero spectrum `{1,1,-1}` for every `m`.

For this exact rotated pattern,

`sum_j E_J(w_j)=1554220767867635/496598405422144`
`=3.1297337061451832379...`.

Therefore, with `n=4m`,

`boxed(p_{Q_m}(0)=3sqrt(2)[1-c_dense/n+O(n^{-2})])`,

where

`c_dense=310844153573527/496598405422144`
`=0.62594674122903664757...`.

Thus a genuinely dense exact-spectrum product-cube family approaches the source-valid obstruction `3sqrt(2)` with a first-order coefficient only `0.0010312161...` above the sharp periodic-frame coefficient `c_*`.

More generally, density is not a true obstruction to sharpness: for the segregated near-minimizing patterns in Section 3, a generic orthogonal rotation arbitrarily close to the identity makes all finitely many physical `J`-inner products nonzero while changing the quartic coefficient continuously. Hence `c_*` is also the infimum of the first-order coefficient over **fully dense** periodic patterns in the two-limit sense `r->infinity` followed by a generic rotation tending to the identity.

## 6. Actual application of the newest fleet02/B17 theorem

Take independent centered unit intervals `U_1,U_2,U_3,V_1,V_2,V_3`, an independent arbitrary random variable `X` with density `0<=f<=1`, and set

`S=(U_1+U_2+U_3)/sqrt(3)`,
`T=(2V_1+V_2+2V_3)/3`.

The corresponding physical matrix

`A_sep=diag(1, aa^T, -bb^T)`,

with `a=(1,1,1)/sqrt(3)` and `b=(2,1,2)/3`, has exact nonzero spectrum `{1,1,-1}`. Applying the completed partner theorem gives the actual global inequality

`boxed(||p_{X^2+S^2-T^2}||_infty <= K_sep)`,

where

`K_sep=2sqrt(2) asin(4/5)+sqrt(5)(pi/2-asin(4/5))`
`=4.0616991701014631769... < 3sqrt(2)`.

The certified gap is

`3sqrt(2)-K_sep=0.1809415170178219695...`.

This interacts nontrivially with the new dense family: its cone-tip value tends to `3sqrt(2)`, so for all sufficiently large `m` it exceeds `K_sep`. Thus the near-sharp periodic mechanism cannot be represented by, or uniformly reduced to, the separated one-heavy plus two opposite rank-one cube-bank architecture covered by the partner theorem. Shared diffuse sign geometry is genuinely needed to reach the sharp lower-obstruction scale.

## 7. Sharp-constant consequence

The strongest source-valid universal lower obstruction remains

`boxed(C_univ >= 3sqrt(2))`.

This run does not raise that lower bound. What it adds is a sharp quantitative constraint on how finite periodic product-cube witnesses can approach it:

- every fixed periodic Parseval frame approaches from below with first relative deficit at least `c_*/n`;
- `c_*=(63+2sqrt(342))/160` is asymptotically optimal over row patterns;
- a four-row pattern already attains `5/(8n)`;
- fully dense exact rotated patterns can be made arbitrarily close to the same sharp coefficient;
- the partner's entire separated one-heavy architecture stays a fixed global distance below `3sqrt(2)`.

So a proof of a sharp `3sqrt(2)` upper bound, if true, cannot hope for a dimension-free stability gap away from diffuse dense frames: there are exact dense target matrices whose cone-tip density loses only `~0.625/n` relatively. Conversely, a counterexample above `3sqrt(2)` cannot arise as the first Edgeworth perturbation of any fixed periodic cube frame, because the optimized first correction has a strictly negative sign.

## 8. Verification and remaining gap

`CHECK.py` verifies the sharp coefficient algebra, the near-sharp four-row Parseval frame, the rational orthogonal rotation, exact spectrum identities, entrywise density of `A_*`, the exact dense coefficient, and the partner-constant comparison. It returns

`QFORM_B17_SHARP_PERIODIC_FRAME_CHECK_PASS`.

Remaining witness frontier: nonperiodic/mesoscopic frames whose pattern changes with dimension, rough non-uniform cap-one laws, intermediate-leverage shared-coordinate structures, off-zero modes, or extra active spectrum. Nothing here proves `C_univ=3sqrt(2)` or unrestricted continuity.
