SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T22:21:18Z.
attacking: the exact-Schur-match/zero-tail third-curvature endpoint by projecting a same-bank physical crossing off the two-dimensional hub-partner row space, then applying the reviewed grouped-hub projected-crossing theorem.

# Early calculation — projected same-bank curvature at exact common-plane match

Run: `20260923T222118Z-fleet03-B08-qform-diffuse-r44`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Full QFORM remains OPEN.

Use two ORIGINAL hub coordinates H and disjoint original-coordinate light banks J1,J2. Let the hub-to-bank arms be `M1` and `M2`, each with two rows. Consider the common-plane light matrix

`A_LL = M^T R M + diag(S1,S2)`,  `M=[M1 M2]`,

where `S1,S2` are arbitrary symmetric same-bank residuals. In the r45 exact Schur-match/zero-tail endpoint one has `R=B^{-1}`, but the calculation below does not need invertibility or conditioning of B.

Choose a physical subset `K subset J1` such that `M1[:,K]` has rank two. Put `I=(J1\K) union J2`, and let `P_K` be the orthogonal projection in `R^K` onto `row(M1[:,K])`. The `I-K` light crossing is

`A_LL[I,K] = M_I^T R M1[:,K] + [S1[J1\K,K];0]`.

The first summand has every row in `row(M1[:,K])`, hence

`A_LL[I,K](I-P_K) = [S1[J1\K,K](I-P_K);0]`.                  (E.1)

Therefore the arbitrary common-plane edge is annihilated *exactly* by the product-safe projected crossing, leaving only genuine third same-bank curvature.

Define

`A_K = sqrt(det(M1[:,K] M1[:,K]^T))`

and

`F_K = ||S1[J1\K,K](I-P_K)||_F`.

For the reviewed grouped-hub projected-crossing theorem with `k=2`, `ell=1`, the projected first-volume is `Z1=F_K^2`. If `F_K>0` and every physical row `c_i` of the projected crossing satisfies

`||c_i||^2 <= F_K^2/2`,

then, because the two literal hub coordinates have joint density cap one,

`||p_Q||_infinity <= 3*2^(5/6) (A_K F_K)^(-1/3)`.             (E.2)

The source characteristic-function envelope is integrable (`|t|^{-3/2}`), so this branch has a continuous `C_0` density. All internal hub terms, same-side quadratic terms, diagonals and affine terms are retained.

## Rank-one residual specialization

If `S1=lambda q q^T` with `||q||=1`, then

`F_K = |lambda| ||q_{J1\K}|| ||(I-P_K)q_K||`.                  (E.3)

The row-marginal condition becomes

`max_{i in J1\K} q_i^2 <= (1/2)||q_{J1\K}||^2`.               (E.4)

Thus a diffuse rank-one third curvature is paid whenever a balanced piece of its eigenvector survives transverse to the restricted two-arm row space.

## Exact-match Hadamard stress family

Apply this to the target-valid fleet02/B08 stress family: `m=2^d`, `d>=3`; three distinct normalized Sylvester characters `r_a,r_b,q`; `M=[r_a^T;r_b^T]`; `B=diag(epsilon,-epsilon)`; and after exact pair completion `S1=q q^T`, `S2=0` while the pair-Schur cross block is exactly zero.

Choose a nonzero character index `h` different from `a+b`, `a+c`, `b+c`, and let `K={x:chi_h(x)=1}`. Character orthogonality gives exactly

`M_K M_K^T=(1/2)I_2`,
`q_K perpendicular row(M_K)`,
`||q_K||^2=||q_{K^c}||^2=1/2`.

Hence `A_K=1/2`, `F_K=1/2`, and each projected row marginal is `2/m <=1/4`. Equation (E.2) gives

`||p_Q||_infinity <= 3*2^(5/6)*2^(2/3)=6 sqrt(2) <8.486`,      (E.5)

uniformly in `epsilon`, `m`, and all independent cap-one laws. This branch is continuous `C_0`. It directly pays the previously exhibited exact-match family even when the physical hub pair is arbitrarily ill-conditioned and every physical 2x2 principal block lies below the `1/64` gate.

This is not a full solution. The remaining deterministic interface is to force a physical cut with simultaneous two-arm area and transverse projected third-curvature volume, or route failure to an aligned/localized certificate.
