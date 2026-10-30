# fleet03/B05 — span-aligned block Pluecker aggregation

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T161113Z-fleet03-B05-QFORM-r11`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / MECHANISM STRESS FAMILY / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory receiver use.

## 1. Scope and first unpaid implication

The owner target remains the full statement for every dimension, every independent real coordinate family with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one. This report proves a new exact-rank-three heavy-isotropic coarea theorem. It does **not** prove the full conjecture or the requested continuity conclusion.

Live corrections consumed include the failure of law-uniform pointwise quadratic-phase decay, loss from unrestricted fiber suprema, loss of independence after spectral rotation, insufficiency of a single cross minor, insufficiency of conditional-density caps in place of genuine independence, and the failure of fixed local rank-two extraction. None of those mechanisms is used below.

The preceding fleet03/B05 report proved `QFORM-PAIR-SECTIONAL-COAREA-v1`: if `U` is genuinely independent of a possibly dependent pair `(V,Z)`, `||p_U||_infinity<=M_U`, `||p_(V,Z)||_infinity<=M_2`, and

`W=2aUV+H(V)+b(Z+theta(V))^2`,

then

`||p_W||_infinity <= 3*2^(2/3) M_U^(2/3) M_2^(2/3) |a|^(-2/3)|b|^(-1/3)`.  (1.1)

Its selected-coordinate application paid `|Delta_jk|^(-2/3)` even though the total pair-Pluecker mass equals one. Fleet02/B05 then proved `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1`: every two-dimensional orthonormal projection of an arbitrary product law with scalar density caps one has joint density at most `e`, and used (1.1) to close the aggregate **zero-leakage** branch. Source: `yspennstate/math-open-problems@e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T155206Z-b05-qform-779c4c9b/REPORT.md`.

The first unpaid coarea implication was therefore to aggregate pair-Pluecker mass while retaining the true hidden leakage. The theorem below does this exactly on every block on which the leakage lies in the span of the two transverse coefficient vectors. It identifies the precise extra obstruction as a **third Pluecker / span-defect mass**.

The designated partner remains `fleet04/B05`. Fresh current-QFORM memory/handoff checks found no completed artifact for that slot, so no theorem is falsely attributed to it. The completed fleet02/B05 coarea result above is applied directly and source-pinned. The previously completed fleet04/B18 Schur-pivot theorem remains a compatible comparison route, but is not needed for the proof below.

## 2. General two-dimensional aggregate density after whitening

Let `X=(X_j)_{j in L}` have independent scalar probability densities bounded by one. Let `y,z in R^L`, and put

`G_L = [[||y||^2, <y,z>],[<y,z>,||z||^2]]`,
`D_L = det G_L`.

Assume `D_L>0`. Let `M` be the `2 x |L|` matrix with rows `y,z`. Then

`M_0 = G_L^(-1/2) M`

has orthonormal rows. By the completed fleet02/B05 theorem, `M_0 X` has density at most `e`. Since

`(y.X,z.X)^T = G_L^(1/2) (M_0 X)`,

the ordinary output change of variables gives

`boxed{ ||p_(y.X,z.X)||_infinity <= e D_L^(-1/2). }`                    (2.1)

This is an actual application of completed peer mathematics. No input-coordinate rotation is performed; whitening occurs only in the two-dimensional output.

Cauchy--Binet gives the exact identity

`D_L = sum_{j<k, j,k in L} (y_j z_k-y_k z_j)^2`.                         (2.2)

Thus (2.1) pays the **total** pair-Pluecker mass on the block rather than its largest individual minor.

## 3. Heavy-isotropic normal form

Use the exact-rank-three heavy-isotropic state from the preceding B05/B10 work. Let

`A=U Lambda U^T`, `U^T U=I_3`, `|det Lambda|>=1`,

and let one physical row be `u_i=sqrt(c)e`, with `c>1/2` and `e^T Lambda e=0`. In an orthonormal spectral basis `(e,f,g)`, write

`Lambda=[[0,B,0],[B,r,sigma0],[0,sigma0,tau]]`,

so

`B^2 |tau|=|det Lambda|>=1`.                                             (3.1)

For residual physical rows write

`u_j=s_j e+y_j f+z_j g`.

Then

`sum s_j^2=1-c`, `sum y_j^2=sum z_j^2=1`,
`<s,y>=<s,z>=<y,z>=0`.                                                   (3.2)

With

`T=sum s_jX_j`, `Y=sum y_jX_j`, `Z=sum z_jX_j`,

completion of the spectral `Z` square gives

`Q=2B(sqrt(c)X_i+T)Y + A_0 Y^2 + tau(Z+kappa Y)^2`                       (3.3)

for fixed real `A_0,kappa`.

## 4. Main theorem: aggregate Pluecker payment on a span-aligned block

### Theorem 4.1 — `QFORM-SPAN-ALIGNED-PLUCKER-AGGREGATION-v1`

Let `L` be any subset of the residual original coordinates and `K=L^c`. Write `s_L,y_L,z_L` for the coefficient restrictions. Assume

1. `D_L=det Gram(y_L,z_L)>0`; and
2. the leakage on `L` is exactly transverse-span aligned:

` s_L = alpha y_L + beta z_L `                                          (4.1)

for some real `alpha,beta`.

Then the full quadratic form (3.3) has an essentially bounded density satisfying

`boxed{ ||p_Q||_infinity
 <= 3*2^(2/3) e^(2/3) c^(-1/3) D_L^(-1/3)
    |det Lambda|^(-1/3). }`                                             (4.2)

In particular, because `c>1/2` and `|det Lambda|>=1`,

`boxed{ ||p_Q||_infinity < 6 e^(2/3) D_L^(-1/3). }`                     (4.3)

Numerically `6 e^(2/3)=11.6864042463...`.

#### Proof

Condition on every residual coordinate in `K`; keep `X_i` and all coordinates in `L` unconditioned. Because the original coordinates are independent, after this conditioning `X_i` remains independent of the `L`-bank and has the same density cap. Let the conditioned contributions from `K` be constants `t_0,y_0,z_0`. Put

`V = y_L.X_L + y_0`,
`R = z_L.X_L + z_0`,
`U_0 = sqrt(c) X_i`.

By (4.1),

`s_L.X_L = alpha (V-y_0) + beta (R-z_0)`,

so the total leakage is

`T = alpha V + beta R + gamma`                                         (4.4)

for a conditioned constant `gamma`.

Substitute (4.4) into (3.3). Terms `2B(alpha V+gamma)V` depend only on `V` and are absorbed into a new scalar function `H(V)`. The sole extra mixed term is

`2B beta V R`.

Since `tau!=0`, this term is absorbed exactly into the existing square:

`tau(R+kappa V)^2 + 2B beta V R
 = tau(R+(kappa+B beta/tau)V)^2 + H_1(V)`                               (4.5)

for an explicit quadratic `H_1`. Therefore the conditional form is exactly

`Q = 2B U_0 V + H_2(V)
      + tau(R+theta(V))^2`.                                             (4.6)

Here `U_0` is genuinely independent of `(V,R)` and

`||p_U0||_infinity <= c^(-1/2)`.                                       (4.7)

Translations do not change the joint density cap, and (2.1) gives

`||p_(V,R)||_infinity <= e D_L^(-1/2)`.                                 (4.8)

Apply `QFORM-PAIR-SECTIONAL-COAREA-v1`, equation (1.1), with

`M_U=c^(-1/2)`, `M_2=eD_L^(-1/2)`, `a=B`, `b=tau`.

This yields, uniformly in all conditioned values,

`||p_(Q | X_K)||_infinity
 <=3*2^(2/3)e^(2/3)c^(-1/3)D_L^(-1/3)
   |B|^(-2/3)|tau|^(-1/3)`.

By (3.1), the final two factors equal `|det Lambda|^(-1/3)`. Mixing the conditional laws over `X_K` preserves the same bound. This proves (4.2), and (4.3) follows from `c>1/2`, `|det Lambda|>=1`. QED.

### What this resolves

For `|L|=2`, condition (4.1) is automatic whenever `D_L>0`, and (4.2) reduces to the preceding selected-pair theorem up to the universal two-dimensional projection constant. More importantly, for larger `L`, equation (2.2) shows that (4.2) aggregates **all** pair minors inside `L` before reciprocal payment. If `D_L>=delta>0`, the entire block is paid with a universal `O(delta^(-1/3))` constant even when every individual `|Delta_jk|` is tiny.

The fleet02/B05 no-leakage theorem is the special case `L=all residual coordinates`, `alpha=beta=0`, `D_L=1`. Theorem 4.1 therefore strictly identifies the algebraic feature that allowed that aggregate proof: zero leakage is not essential; **span-aligned leakage is sufficient**.

## 5. Exact third-Pluecker obstruction

The span condition has a coordinate-free exact defect. Define the three-vector Gram determinant

`E_L = det Gram(s_L,y_L,z_L)`.                                          (5.1)

When `D_L>0`, the Schur-complement identity gives

`boxed{ E_L/D_L
 = ||s_L - Proj_span{y_L,z_L} s_L||^2. }`                         (5.2)

Hence Theorem 4.1 applies exactly when `E_L=0`.

Cauchy--Binet gives

`E_L = sum_{j<k<ell in L}
        det([[s_j,s_k,s_ell],
             [y_j,y_k,y_ell],
             [z_j,z_k,z_ell]])^2`.                                     (5.3)

Thus the first unpaid coarea quantity is no longer merely the pair-Pluecker mass `D_L`. It is the **simultaneous pair/triple Pluecker geometry `(D_L,E_L)`**. Pair mass can be aggregated dimension-freely whenever the triple defect vanishes; the hard branch is genuine overlapping three-projection provenance `E_L>0`.

Because the owner assumptions impose no moments or support bounds, a small coefficient-space value of `E_L/D_L` cannot simply be declared a small random perturbation: variables with density at most one may live on arbitrarily large scales. A nonzero defect therefore requires a real third-bank smoothing/aggregation argument, not a tail-free perturbation assertion.

## 6. Target-valid stress family: pair mass one but no large exact aligned block

The new theorem is useful but not automatic. The following exact frame shows why the third-Pluecker defect is a genuine remaining mechanism barrier.

Fix `m>=4` and set

`theta_j=2 pi j/m`,
`y_j=sqrt(2/m) cos(theta_j)`,
`z_j=sqrt(2/m) sin(theta_j)`, `j=0,...,m-1`.

Then `y,z` are orthonormal and

`Delta_jk = y_j z_k-y_k z_j
          = (2/m) sin(theta_k-theta_j)`,                                (6.1)

so

`sum_{j<k} Delta_jk^2=1`,
`max_{j<k}|Delta_jk| <=2/m`.                                            (6.2)

Let `H={v in R^m:<v,y>=<v,z>=0}`. For each coordinate triple `I={i,j,k}`, define the vector `w_I` supported on `I` by

`(w_I)_i=Delta_jk`, `(w_I)_j=-Delta_ik`, `(w_I)_k=Delta_ij`.

Then `w_I` is orthogonal to both `y` and `z`, and

`det([[v_i,v_j,v_k],[y_i,y_j,y_k],[z_i,z_j,z_k]])=<v,w_I>`.            (6.3)

For three distinct regular-polygon indices the three planar vectors `(y_r,z_r)` cannot all lie on one line through the origin, so `w_I!=0`. Therefore, inside `H`, each equation `<v,w_I>=0` is one proper hyperplane. A finite union of proper hyperplanes cannot cover the real vector space `H`. Choose a unit `s' in H` outside all of them.

Set `c=3/4`, `s=(1/2)s'`. Then

`||s||^2=1-c=1/4`, `<s,y>=<s,z>=0`.                                    (6.4)

Add one heavy physical row `u_0=sqrt(c)e` and residual rows

`u_j=s_j e+y_j f+z_j g`.

Equations (6.4) and orthonormality of `y,z` imply

`sum_j u_j u_j^T + u_0u_0^T=I_3`.

Finally choose

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`,                                    (6.5)

whose eigenvalues are `{1,-1,1}`. The heavy row is isotropic, `e^T Lambda e=0`, and this is a fully valid exact-rank-three owner-target matrix family.

By construction every three-coordinate determinant of `(s,y,z)` is nonzero. Therefore for every block `L` with `|L|>=3`, equation (5.3) gives `E_L>0`: no such block is span aligned. Blocks with `D_L>0` and `E_L=0` can have at most two coordinates, and then (6.2) gives

`D_L=Delta_jk^2 <=4/m^2`.                                               (6.6)

Consequently the certificate (4.3), if used **only** through exact span-aligned blocks, still pays at least the scale `D_L^(-1/3) >= (m/2)^(2/3)` on this target-valid frame, even though the total pair-Pluecker mass is exactly one.

This is not a counterexample to QFORM and not evidence that the true density grows. It is a source-valid counterexample to the stronger structural hope that total pair mass alone must be capturable inside one large exactly aligned block. The next mechanism must spend the third projection rather than wish it away.

## 7. First unpaid implication

The next B05 target is now sharply:

**`QFORM-PAIR-TRIPLE-PLUCKER-COAREA-v1` — OPEN.**  Prove a curved-trace/coarea inequality for the heavy-isotropic product-linear triple `(T,Y,Z)` that pays the pair mass `D_L` while simultaneously using nonzero triple defect `E_L`, without selecting one tiny physical pair and without replacing product provenance by only a joint or conditional density cap.

Equivalent useful formulations include:

- an aggregate three-bank estimate for blocks with `E_L>0` which reduces continuously to Theorem 4.1 when `E_L=0` but does not rely on moment/tail smallness; or
- a structural dichotomy proving that every target frame with no large aligned block enters an already-paid disjoint-bank, ridge-window, Schur, or hyperbolic-square branch.

The regular-polygon-plus-generic-orthogonal-leakage frame in Section 6 is the mandatory stress test for any proposed block-selection statement.

Arbitrary additional spectral directions remain a separate later interaction/truncation debt. Full QFORM is still **OPEN / NOT PROVED**, and this report does not prove continuity of the density.

## 8. Source ledger and delivery scope

- Fresh control programme/revision at run start: `QFORM-DENSITY-3EIG-20260922`, `2026-09-22.5`.
- Previous fleet03/B05 pair-sectional theorem: `yspennstate/math-open-problems@332f29e335274f2b3f81ccf92d62443b928c66cd`.
- Completed fleet02/B05 aggregate two-dimensional projection theorem actually applied in (2.1): `yspennstate/math-open-problems@e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`.
- Designated `fleet04/B05`: no completed current-QFORM artifact found at the source refresh; no partner result fabricated.
- Compatible fleet04 comparison source retained from the preceding run: fleet04/B18, `QFORM-SCHUR-PIVOT-SMOOTHING-v1`, `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`.

Manual allowlist/privacy review of this report found only mathematical statements, public repository coordinates, run identifiers, and nonsecret control hashes. No credentials, signed URLs, private transcripts, personal data, email, Drive, scheduler IDs, or machine paths are included.
