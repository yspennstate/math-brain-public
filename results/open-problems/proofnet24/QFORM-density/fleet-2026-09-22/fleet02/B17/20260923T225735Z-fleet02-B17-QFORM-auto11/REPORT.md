# QFORM B17: global tip maximality for the first-order optimal three-bank witness

Run: `20260923T225735Z-fleet02-B17-QFORM-auto11`  
Status: `PROVED_SUPPORTING_SHARP_WITNESS_THEOREM`; unrestricted QFORM remains OPEN; full-target continuity remains OPEN; `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The latest compatible fleet03/B17 report (`20260923T221053Z-fleet03-B17-QFORM-auto11`) solves the first-order cone-tip optimization for the exact three-bank uniform family. It leaves open whether an off-tip output level can beat the cone tip. This report proves:

**Theorem (QFORM-THREEBANK-GLOBAL-TIP-OPTIMAL-v1).** Let

- `J = diag(1,1,-1)`,
- `O in O(3)`, `B = O^T J O`,
- `m_1,m_2,m_3 >= 2`,
- `X_{jk}` independent `Unif[-1/2,1/2]`,
- `Y_j = m_j^{-1/2} sum_{k=1}^{m_j} X_{jk}`,
- `Q = Y^T B Y`.

Then:

1. for every `O` and every `m_j`, the one-sheet side satisfies

   `ess sup_{s>=0} p_Q(s) <= p_Q(0)`;

2. if the negative eigenvector is aligned with a bank, say `B=J` after a permutation of the bank labels, then also

   `p_Q(-r) <= p_Q(0)` for every `r>0`,

   and consequently

   `||p_Q||_infty = p_Q(0)`.

Thus the latest partner's first-order optimal cone-tip orientation (negative axis aligned with the smallest bank) is not merely tip-optimal: its **actual global density norm is attained at the cone tip**. For non-aligned rotations, any off-tip escape in this family is now confined to the minority-sign/two-sheet side `s<0`.

This is a theorem about this exact source-valid family, not a proof of unrestricted QFORM.

## 2. Physical source and exact spectrum

Let `R` be the `N x 3` synthesis matrix, `N=m_1+m_2+m_3`, whose rows in bank `j` equal `e_j/sqrt(m_j)`. Then

`R^T R = I_3`.

Define the physical matrix

`A = R B R^T`.

Because `R` is an isometry from `R^3` onto its range, the nonzero spectrum of `A` is exactly the spectrum of `B`, hence

`spec_nonzero(A) = {1,1,-1}`.

In the aligned case the statement is even more explicit:

`A = diag(J_{m_1}/m_1, J_{m_2}/m_2, -J_{m_3}/m_3)`

(up to permutation), where `J_m` is the all-ones matrix. Each physical input density is exactly one on a unit interval. There is no post-rotation independence assumption: the only independent aggregated coordinates are the three bank sums, which depend on disjoint original coordinate sets.

## 3. Log-concavity of the three-bank source

Write `g_j` for the density of `Y_j`. The unit-interval density is even and log-concave in the extended-value sense. Convolution and non-singular scaling preserve log-concavity, hence every `g_j` is even and log-concave. Therefore

`rho(y) = g_1(y_1) g_2(y_2) g_3(y_3)`

is centrally symmetric and log-concave on `R^3`.

In spectral coordinates `z=Oy`,

`rho_O(z)=rho(O^T z)`

remains centrally symmetric and log-concave. This observation does not assert independence of the coordinates of `z`.

## 4. Pinned-source theorem applied to a real inequality

The required pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem C,

proves the exact ruled-level-set identity for `q(z)=z_1^2+z_2^2-z_3^2` on the one-sheet side. For `s>0`, with

`e_theta=(cos theta,sin theta,0)`,  
`w_theta=(-sin theta,cos theta,1)`,

one has

`delta(q-s) dz = (1/2) dtheta dt`

on the ruling `z=sqrt(s)e_theta+t w_theta`. Equivalently,

`p_Q(s) = (pi/sqrt(2)) avg_theta rho_theta(sqrt(s)e_theta)`,

where `rho_theta` is the two-dimensional marginal of `rho_O` obtained by integrating along the ruling direction.

Now apply Prekopa to `rho_O`: every `rho_theta` is log-concave. It is also centrally symmetric. Hence, for every `x`,

`rho_theta(0) >= sqrt(rho_theta(x) rho_theta(-x)) = rho_theta(x)`.

Substitution into the exact pinned identity gives the genuine sharp-witness obstruction

`p_Q(s) <= (pi/sqrt(2)) avg_theta rho_theta(0) = p_Q(0),   s>0`.

Thus **no positive off-tip peak can occur anywhere in the partner's finite three-bank uniform family, regardless of rotation or unequal bank sizes**. The generic pinned bound `pi sqrt(2)` is not sharp enough to prove the candidate constant `3sqrt(2)`; the exact ruling plus the special log-concave source structure is what pays this implication. Failure of the generic constant is therefore a proof-constant limitation, not a QFORM counterexample.

## 5. The aligned two-sheet side

Now take the bank-aligned signature

`Q = Y_1^2 + Y_2^2 - Y_3^2`.

Set

`W=Y_1^2+Y_2^2`, `V=Y_3^2`.

These variables are independent because they use disjoint original coordinate banks. Let `a` and `b` be their densities. Since `g_3` is even and nonincreasing on `[0,infinity)`, for `v>0`

`b(v)=g_3(sqrt(v))/sqrt(v)`

is nonincreasing. Therefore for every `r>0`,

`p_Q(-r)=integral_0^infinity a(u)b(u+r)du`

`          <= integral_0^infinity a(u)b(u)du`

`          = p_Q(0)`.

The cone-tip integral is finite: by polar coarea,

`a(u) <= pi ||g_1||_infty ||g_2||_infty`,

while `b(u)=O(u^{-1/2})` at the origin. Hence the comparison is legitimate.

Combining this direct two-sheet inequality with Section 4 proves the global bound

`||p_Q||_infty <= p_Q(0)`.

For `m_j>=2`, each `g_j` is continuous and compactly supported. The displayed convolution formulas then give a continuous representative of the aligned output density at zero (dominated convergence; `b` is integrable and `a(u)b(u)` is integrable at zero). Hence equality holds:

`||p_Q||_infty = p_Q(0)`.

This scoped continuity statement is not being promoted to the unrestricted target.

## 6. Application to the latest fleet03/B17 optimization

The partner report writes `u_j=O_{3j}^2` and proves the first-order cone-tip expansion

`p_Q(0)/(3sqrt(2)) = 1 - sum_j h_4(u_j)/(20m_j) + O((sum_j 1/m_j)^2)`,

where

`h_4(u)=(57+6u-39u^2)/32`.

Because `h_4` is strictly concave, the partner proves that for fixed bank sizes the smallest first-order deficit occurs at a simplex vertex: the negative spectral axis is aligned with the smallest bank. If bank `k` is the negative bank, the deficit is

`D_1 = [24/m_k + 57/m_i + 57/m_j]/640`.

At fixed total dimension `N=m_1+m_2+m_3`, Cauchy-Schwarz gives

`24/m_k+57/m_i+57/m_j >= (sqrt(24)+2sqrt(57))^2/N`,

with equality in the continuous allocation at

`m_k:m_i:m_j = sqrt(24):sqrt(57):sqrt(57)`.

Thus

`K_* = (sqrt(24)+2sqrt(57))^2/640`

`    = 63/160 + 3sqrt(38)/80`

`    = 0.6249155251113366...`.

Choose integer bank sizes within `O(1)` of these proportions. Since this orientation is aligned, the theorem above upgrades the partner's cone-tip expansion to an expansion for the **actual global density norm**:

`||p_Q||_infty = 3sqrt(2) [1 - K_*/N + O(N^-2)]`.

Consequently the exact source-valid global witness sequence approaches `3sqrt(2)` from below at the first-order optimal cone-tip rate. In particular any universal target constant must satisfy `C_* >= 3sqrt(2)`.

The new information is the global-maximality statement, not the already-known lower obstruction itself.

## 7. Fully explicit rational near-optimal global witness

For an especially concrete finite sequence, let `q>=1` and take

`m_-=13q`, `m_+=20q`, `m_+'=20q`, `N=53q`,

with the negative eigenvalue on the `13q` bank. Every finite physical matrix has exact nonzero spectrum `{1,1,-1}` and all `53q` physical marginals are unit-interval cap-one laws. The preceding theorem gives

`||p_{Q_q}||_infty = p_{Q_q}(0)`.

Substituting the partner's full second-order cone expansion gives the exact asymptotic coefficients

`p_{Q_q}(0)/(3sqrt(2))`

` = 1 - 981/(83200 q)`

`     - 3190763/(193822720000 q^2)`

`     + O(q^-3)`.

Equivalently, in total dimension `N=53q`,

`||p_{Q_q}||_infty/(3sqrt(2))`

` = 1 - [51993/83200]/N`

`     - [8962853267/193822720000]/N^2`

`     + O(N^-3)`.

Here

`51993/83200 = 0.6249158653846154...`,

only `3.4027e-7` above the continuous optimum `K_*`. This is a completely explicit, globally tip-maximal, finite-dimensional exact-spectrum witness family.

For the second-order substitution, at the aligned orientation the partner formulas give

`c_2(0)=h_6(0)/105+h_8(0)/800 = -4833/327680`,

`c_2(1)= -173/17920`,

`k_44(0,0)=7803/2048`,

`k_44(0,1)=603/128`.

Inserting `(m_1,m_2,m_3)=(20q,20q,13q)` into its formula yields exactly the coefficient above.

## 8. What remains genuinely unpaid

Inside the partner's three-bank uniform architecture:

- the entire one-sheet side is now tip-dominated for **every** rotation and unequal bank allocation;
- the first-order optimal aligned orientation is tip-dominated on **both** signs, hence globally;
- an off-tip escape can remain only on the two-sheet side of a genuinely non-aligned rotation.

Outside this architecture, rough non-log-concave bank laws, surviving non-CLT components, shared macroscopic physical rows, multiscale fragmented sources, and extra active spectrum remain possible sharp-constant mechanisms.

A future valid example with density peak `>3sqrt(2)` would refute the proposed sharp constant, but would **not** refute existence of a larger universal QFORM bound. A genuine counterexample to QFORM must make the best universal constant diverge.

The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction is respected: Section 5 uses the actual aligned independent-bank convolution and monotonicity of the squared negative bank, not a generic X-ray estimate for arbitrary three-dimensional densities.

## 9. Source pins

- owner programme: `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.15`;
- required pinned completed source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `COUNTEREXAMPLE_SEARCH.md` Theorem C and the matching `RESULTS.md` ruling identity;
- latest compatible partner consumed: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T221053Z-fleet03-B17-QFORM-auto11/REPORT.md` (file SHA `63522737e0db4882038e6ad2b1d5b92d26399901`);
- fresh brain control head observed before the run write: `67970aa621c93ae34457405a0f4c46129f6656a2`;
- fresh math head observed immediately before publication work: `cd436a1fad22a288eeee6f5cf0c2b2d7f1632488`.

No full-target theorem or full-target continuity claim is made.
