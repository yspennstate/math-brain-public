SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-22T21:20:21Z.
attacking: low-cross-rank/full-leverage residual routing via product-space Fourier rearrangement and grouped-coordinate half-Riesz smoothing.

# fleet02/B04 — orthogonal-leakage separation and a sharp counterexample to uniform rank-three cross extraction

Status: `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_TARGET_OPEN`.

## Scope and live corrections

Target: independent real coordinates with densities at most one, arbitrary real symmetric A, and at least three eigenvalues of modulus at least one. No moments, support restrictions, diagonal-basis independence, or post-rotation independence are used. The report preserves the live corrections: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive conditional projected-density moments are false; and one fixed good physical minor/cross-rank certificate is not forced by the target hypothesis.

Named partner used: fleet03/B04 r18, `QFORM-ONE-ZERO-TRIPLE-v1`, canonical source `yspennstate/math-open-problems@b49aee1e303aee7191caea8f380bea12bab7641b`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260922T205156Z-r18/REPORT.md`. It states: if one original-coordinate 3x3 principal block B is invertible and one selected diagonal entry is zero, then arbitrary outside spectrum/couplings are allowed and

`||p_(X^TAX)||_infinity <= 3*2^(2/3) |det B|^(-1/3)`.

## 1. New structural lemma: orthogonal leakage can be separated from transverse determinant mass

### `QFORM-ORTHOGONAL-LEAKAGE-SEPARATION-v1`

Let `v_1,...,v_m in R^2` span R^2, put `S=sum_i v_i v_i^T`, and let nonzero `eta in R^m` satisfy

`sum_i eta_i v_i = 0`.

Then there is a partition `[m]=L disjoint_union T` such that

`(sum_(i in L) eta_i^2) * det(sum_(j in T) v_j v_j^T) >= ||eta||_2^2 det(S)/24`.   (1)

In particular, since each normalized factor is at most one,

`sum_(i in L) eta_i^2 >= ||eta||_2^2/24`,

and

`det(sum_(j in T) v_j v_j^T) >= det(S)/24`.   (2)

The partition is by original-coordinate indices, so the two packets are genuinely independent under the product input law.

### Proof

Normalize by replacing `v_i` with `S^(-1/2)v_i` and `eta` with `eta/||eta||`; then `sum v_i v_i^T=I_2`, `sum eta_i^2=1`, and `sum eta_i v_i=0`.

Let `a_i=eta_i^2` and `ell_i=||v_i||^2`. If `V` is the matrix with rows `v_i`, then `P=VV^T` is a rank-two orthogonal projection and `eta` is orthogonal to its range. Hence `P+eta eta^T` is a rank-three orthogonal projection. Put `d_i=ell_i+a_i`, its diagonal entries. Thus `0<=d_i<=1` and `sum_i d_i=3`.

Order `a_(1)>=a_(2)>=...` and put `s=a_(1)+a_(2)+a_(3)<=1`. Since `0<=d_i<=1` and `sum d_i=3`, the rearrangement bound gives

`sum_i a_i d_i <= s`.

Also `sum_i a_i^2 >= s^2/3`. Therefore

`sum_i a_i ell_i = sum_i a_i d_i-sum_i a_i^2 <= s-s^2/3 <= 2/3`,

so

`sum_i a_i(1-ell_i) >= 1/3`.   (3)

Now choose a random fair partition: each i enters L with probability 1/2 independently, and T is the complement. Put

`A_L=sum_(i in L)a_i`, `D_T=det(sum_(j in T)v_jv_j^T)`.

By two-dimensional Cauchy-Binet,

`D_T=sum_(j<k; j,k in T) w_jk`, where `w_jk=det(v_j,v_k)^2`.

Only triples of distinct indices contribute to `E[A_L D_T]`, each with probability 1/8. For fixed i,

`sum_(j<k; j,k!=i) w_jk = det(I_2-v_iv_i^T)=1-ell_i`.

Hence by (3)

`E[A_LD_T]=(1/8)sum_i a_i(1-ell_i)>=1/24`.

Some partition satisfies the same lower bound. Undoing the normalization gives (1). QED.

### Application to the partner frontier

In fleet03/B04 r18, each residual bank G has transverse vectors `v_i=(beta_i,gamma_i)` and leakage decomposition

`alpha_G=p_G beta_G+q_G gamma_G+eta_G`, with `eta_G` orthogonal to both transverse coefficient columns.

Whenever `eta_G!=0`, (1) gives a genuine original-coordinate split inside G that retains at least `1/24` of the leakage energy and at least `1/24` of the transverse determinant. Thus the remaining two-bank overlap problem is not a lack-of-independent-packets problem: independent scalar-leakage and transverse-determinant packets can always be manufactured quantitatively. The unpaid analytic issue is that the discarded coefficient components still contaminate the selected packets inside the full quadratic polynomial; a valid splice must absorb that contamination before paying reciprocal local coefficients.

## 2. Counterexample to the stronger shortcut “both leakages nonzero force a quantitative rank-three cross cut”

The following exact target family shows that the tempting next shortcut is false even with perfectly conditioned transverse banks.

Let

`M=[[0,1,0],[1,0,0],[0,0,1]]`,

so the nonzero spectrum is `{1,1,-1}`. Put `h=1/2`, `a=1/(2sqrt(2))`,

`beta=a(1,1,-1,-1)`,
`gamma=a(1,-1,1,-1)`,
`u=(1,1,1,1)/2`.

For `0<eps<1/2`, set

`p=sqrt(1/2-2eps^2)`,
`alpha_J=p beta+eps u`,
`alpha_K=-p beta+eps u`.

Take one heavy row `r_0=(1/sqrt(2),0,0)`, four J-rows `(alpha_J_i,beta_i,gamma_i)`, and four K-rows `(alpha_K_i,beta_i,gamma_i)`. Let R be the resulting 9x3 matrix and `A_eps=R M R^T`.

The columns of R are orthonormal: the transverse banks each satisfy

`S_J=S_K=(1/2)I_2`,

both orthogonal leakages are nonzero with

`eta_J=eps u`, `eta_K=eps u`,

and the longitudinal norm identity is `h+p^2+2eps^2=1`. Thus `A_eps` has nonzero eigenvalues exactly `{1,1,-1}` and is an exact target-valid rotated indefinite form.

In the orthonormal bank bases `(u,beta/||beta||,gamma/||gamma||)`, the J-K physical cross block is unitarily equivalent to

`[[0,eps/sqrt(2),0],[eps/sqrt(2),0,0],[0,0,1/2]]`.

Therefore its three nonzero singular values are exactly

`1/2, eps/sqrt(2), eps/sqrt(2)`.   (4)

Both leakage vectors are nonzero for every eps>0, while the second and third cross singular values tend to zero. Hence the inference

> nonzero orthogonal leakage in both B19 banks => a universal rank-three cross-singular-value certificate

is false. Record this shortcut as `CANDIDATE_REFUTED`; it is not a counterexample to QFORM.

## 3. Named partner applied to an actual inequality

The heavy coordinate has `A_00=0`. Choose the first two J coordinates. Their transverse rows are `(a,a)` and `(a,-a)`, so the squared Pluecker determinant is `1/16`. Since `h=1/2` and `det M=-1`, the corresponding physical 3x3 principal block satisfies exactly

`det A_{0,1,2}=-1/32`.

Applying fleet03/B04 r18 `QFORM-ONE-ZERO-TRIPLE-v1` gives, uniformly for every eps in `(0,1/2)` and every admissible independent cap-one input law,

`||p_(X^T A_eps X)||_infinity <= 3*2^(2/3)*32^(1/3)`

`=3*2^(7/3)=15.119052598738476...`.   (5)

Thus the same family that kills a uniform rank-three cross-cut route remains uniformly controlled by the source-pinned partner theorem.

At `eps=1/10`, the form is genuinely rotated and indefinite; the checker records cross singular values `(0.5,0.0707106781,0.0707106781)` and the exact target spectrum `{1,1,-1}` up to floating error.

## 4. First unpaid implication

`QFORM-LEAKAGE-PACKET-CONTAMINATION-SPLICE-v1`: use the quantitative packet separation (1) inside one or both B19 banks to prove a product-space/rearrangement estimate that tolerates the residual transverse coefficients on the leakage packet and residual leakage coefficients on the transverse packet. The stronger attempt to replace this by a uniform rank-three J-K cross certificate is invalid by (4). A successful next theorem must aggregate before taking any reciprocal small singular value.

No full-proof claim is made.
