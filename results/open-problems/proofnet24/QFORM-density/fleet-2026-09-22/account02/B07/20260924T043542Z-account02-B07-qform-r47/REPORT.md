SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T04:35:42Z.
attacking: the r46 balanced kernel-star residual — transfer every pair-disjoint kernel-star third volume back to literal physical E0 before inversion, then identify the true overlap-dense/hub debt.

# account02/B07 r47 — matching kernel-star exterior compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: coordinate minor selection / complementary constructions and source-valid counterexamples.
Execution: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.
Status: **NEW MATCHING EXTERIOR DOMINATION + DIMENSION-FREE RANK-1/RANK-2 MATCHING DICHOTOMY + EXACT BOUNDED-CORE OBSTRUCTION / FULL QFORM OPEN / CONTINUITY OPEN**.

No moment, support, iid, log-concavity, diagonal-basis, post-rotation independence, or coefficient truncation is used. Every coordinate set below is a literal original-coordinate set.

## 1. Fresh source state and first unpaid implication


Latest completed designated partner is account03/B07 r46:

`yspennstate/math-open-problems@d9203dc7bed31e59ffcee1db8286dbdb0d8e9c51`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T033639Z-account03-B07-qform-r46/REPORT.md`.

The incoming exact rank-one shared-pair packet is, for physical pairs `K subset H`,

`sum_K lambda_K^2 L_K^2 R_K^2 > 1/512`,

where `B_K=A[K,K]=lambda_K u_K u_K^T`, `v_K` is a unit kernel vector,

`L_K^2=sum_{r in I}(v_K^T A[K,r])^2`,
`R_K^2=sum_{c in J}(v_K^T A[K,c])^2`,
`S_K=||A[K,K^c]^T v_K||_2 >= sqrt(L_K^2+R_K^2)`.

The completed physical-pair receiver pays if `|lambda_K|S_K>=2^-10`; if no pair pays, r46 proves the normalized residual currency

`E_bal := sum_K q_K^2 > 2048`,
`q_K := L_K R_K/S_K`.

The immediate first unpaid implication is now sharpened to

`QFORM-R46-OVERLAPGRAPH-TO-HUB-OR-MATCHING-v1`:

> Under the actual upstream condition `E0<1/4`, convert `E_bal>2048` either into (i) a pairwise-disjoint matching carrying definite balanced energy, which the theorem below forces into a dimension-free rank-one/rank-two kernel-star carrier, or (ii) an overlap-dense rank-one-pair graph whose principal-pair consistency produces a literal physical hub/diagonal carrier. No maximum tiny minor may be inverted.

The point of this run is that branch (i) is now closed structurally; only the overlap-graph-to-physical-hub step remains there.

The upstream source is account03/B07 r40:

`yspennstate/math-open-problems@c21a61aa6390c0be6ed68027341207e44c1bbb07`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T224121Z-account03-B07-qform-r40/REPORT.md`.

It defines

`E0=sum_{|S|=|T|=3, S intersect T=empty} det A[S,T]^2`

and pays the full law before the overlap analysis whenever `E0>=1/4`. Therefore the genuinely unpaid overlap-two chamber has `E0<1/4`.

## 2. Literal physical transfer of a matching of kernel stars

Let `Mcal={K_1,...,K_m}` be any family of pairwise-disjoint rank-one physical pairs from the r46 packet. Put

`L0 := I union J`,

which is disjoint from the physical pair bank `H`, and define the actual kernel-star row

`w_a := v_{K_a}^T A[K_a,L0] in R^{L0}`.

Let `W` be the `m x |L0|` matrix whose rows are `w_a`.

### Theorem 2.1 — `QFORM-MATCHING-KERNELSTAR-EXTERIOR-DOMINATION-v1`

For every such pairwise-disjoint family,

`boxed: e_3(W^T W) <= E0.`

In particular, in the genuinely unpaid r40/r46 chamber,

`boxed: e_3(W^T W) < 1/4.`

### Proof

Let `H_M=union_a K_a` and `M=A[H_M,L0]`. Define the `m x |H_M|` matrix `V` whose row `a` is supported on the two physical coordinates of `K_a` and equals the unit vector `v_{K_a}` there. Pair-disjointness gives

`V V^T = I_m`,

and by construction

`W=V M`.

Fix three distinct pair indices `R={a,b,c}` and three physical leaf columns `T subset L0`. Cauchy--Binet gives

`det W[R,T]
 = sum_{S subset H_R, |S|=3} det V[R,S] det M[S,T]`,

where `H_R=K_a union K_b union K_c`. A nonzero coefficient chooses exactly one physical endpoint from each pair. Moreover

`sum_S det V[R,S]^2 = det(V_R V_R^T)=1`.

Cauchy--Schwarz therefore yields

`|det W[R,T]|^2 <= sum_S |det A[S,T]|^2`,

with every contributing `S` disjoint from `T` because `H` and `L0` are disjoint.

Now sum over all three-row sets `R` and all three-column sets `T`. Because the pairs in `Mcal` are mutually disjoint, a physical row triple `S` choosing one endpoint from three pairs determines its three pair indices uniquely, so the right-hand terms are not multiply counted across `R`. Hence

`e_3(W^T W)
 = sum_R sum_T |det W[R,T]|^2
 <= sum_{S subset H_M,T subset L0, |S|=|T|=3}|det A[S,T]|^2
 <= E0`.

This proves the theorem. Notice that the vectors `v_K` were used only as deterministic coefficients in an exterior-algebra identity; no rotated random coordinates and no post-rotation independence are introduced. QED.

This is the desired aggregate-before-inversion transfer: a genuine third volume in the kernel-star family is automatically a literal original-coordinate disjoint third-volume packet already paid upstream.

## 3. Dimension-free low-rank consequence on every energetic matching

Write the squared singular values of `W` as

`x_1 >= x_2 >= ... >= 0`,

and put

`E2(W)=e_2(W^T W)`,
`tau_2=sum_{j>=3}x_j=inf_{rank R<=2}||W-R||_F^2`.

The elementary compound identity

`3 e_3(x)
 = sum_{i<j}x_i x_j sum_{k notin {i,j}}x_k`

and

`sum_{k notin {i,j}}x_k >= sum_{k>=3}x_k=tau_2`

imply

`boxed: tau_2 E2(W) <= 3 e_3(W^T W).`

Therefore, in the unpaid `E0<1/4` chamber,

`boxed:
 E2(W)>=zeta >0
 ==>
 inf_{rank R<=2}||W-R||_F^2 < 3/(4 zeta).
}`

There is also an exact relation to the r46 normalized energy. Since

`||w_K||_2^2=L_K^2+R_K^2`

and `S_K>=sqrt(L_K^2+R_K^2)`, AM--GM gives

`q_K^2=L_K^2 R_K^2/S_K^2
 <= L_K^2 R_K^2/(L_K^2+R_K^2)
 <= (L_K^2+R_K^2)/4
 =||w_K||_2^2/4`.

Thus if a pairwise-disjoint matching `Mcal` carries normalized residual energy

`mu=sum_{K in Mcal} q_K^2`,

then

`boxed: ||W||_F^2 >= 4 mu.`

A convenient fully quantitative rank-one/rank-two fork follows. Let `T=||W||_F^2`. If `mu>1/4`, use the threshold `zeta=mu`.

* If `E2(W)>mu`, then the previous estimate gives

  `inf_{rank R<=2}||W-R||_F^2 < 3/(4mu)`.

* If `E2(W)<=mu`, then `mu<T^2/4` because `T>=4mu` and `mu>1/4`. If `x_1<T/2`, one has `sum_j x_j^2 <= x_1 T<T^2/2`, whence `E2=(T^2-sum x_j^2)/2>T^2/4`, contradiction. Hence `x_1>=T/2`. Writing `tau_1=T-x_1`,

  `E2 >= x_1 tau_1 >= (T/2)tau_1`,

  so

  `tau_1 <= 2E2/T <= 2mu/T <=1/2`.

Therefore:

`boxed:
 mu>1/4
 ==>
 [dist_F^2(W,rank<=1)<=1/2]
 OR
 [dist_F^2(W,rank<=2)<3/(4mu)].
}`

This is dimension-free. It does not assert that the low-rank kernel-star coordinates are independent variables; the remaining receiver must still coordinateize or otherwise consume this literal physical linear-combination structure.

## 4. Exact bounded-dimensional spectral arithmetic — and its limit

Suppose a physical coordinate set `C`, `|C|=m`, captures a determinant packet of total squared weight

`P_C = sum_{(S,T) in packet, S union T subset C} det A[S,T]^2`.

Since all those physical minors are terms in the Cauchy--Binet expansion of `e_3(A[C,C]^2)`, one has

`e_3(A[C,C]^2)>=P_C`.

If the singular values of the symmetric physical principal block are `s_1>=s_2>=s_3>=...`, then

`e_3(A[C,C]^2)
 <= binom(m,3) s_1^2 s_2^2 s_3^2`.

Hence the exact aggregate, no-single-minor lower bound is

`boxed:
 s_3(A[C,C])
 >= sqrt(P_C)/(sqrt(binom(m,3)) s_1(A[C,C]) s_2(A[C,C])).
}`

Thus bounded support plus an upper control of the top two physical scales genuinely closes the spectral-core extraction. Bounded cardinality and determinant mass alone do **not** do so: the denominator is real, not a proof artefact. For example `diag(R,R,R^-2)` has determinant one but third singular value `R^-2`; adjoining a disjoint scalar `1` makes the full matrix a valid three-large-eigenvalue target while this bounded physical determinant core remains arbitrarily ill-conditioned. The full QFORM law is not challenged by this example (it is diagonal and already paid); it refutes only the unconditional bounded-core inference.

## 5. Exact target-class stress for the r46 normalized energy

The same issue appears diffusely and more directly in the r46 currency. For integers `N>=6`, `M>=1`, construct `N` mutually disjoint blocks. In block `a` use physical coordinates

`u_a, z_a, I_a (|I_a|=M), J_a (|J_a|=M)`.

Put

`lambda_N=N^(-1/2)`,
`A[u_a,u_a]=lambda_N`,
`A[z_a,ell]=A[ell,z_a]=c_M=(2M)^(-1/2)` for every `ell in I_a union J_a`,

and all other coefficients in that block zero; different blocks do not couple.

For the physical pair `K_a={u_a,z_a}`,

`B_{K_a}=diag(lambda_N,0)`,
`v_{K_a}=e_{z_a}`,
`L_a^2=R_a^2=1/2`,
`S_a=1`.

Thus each exact r40 bordered packet contributes

`lambda_N^2 L_a^2 R_a^2 =1/(4N)`,

so the total packet is

`sum_a lambda_N^2L_a^2R_a^2=1/4>1/512`,

while the r46 normalized residual is

`boxed: sum_a(L_aR_a/S_a)^2=N/4 -> infinity.`

Also `|lambda_N|S_a=N^-1/2`, so for `N>2^20` every individual pair is below the r46 `2^-10` analytic threshold.

The spectrum of each block is

`{+1,-1,lambda_N,0,...,0}`,

because the physical `z_a` star has Euclidean edge norm one. Hence the complete symmetric matrix is in the exact owner target for every `N>=2`.

Nevertheless every fixed-cardinality physical principal core degenerates. If `|C|<=L`, then in each block the restricted star has operator norm at most `sqrt(L/(2M))`, while the isolated `u_a` scale is `N^-1/2`. Therefore

`boxed:
 s_3(A[C,C])
 <= ||A[C,C]||_op
 <= max(N^-1/2,sqrt(L/(2M))).
}`

Taking `M=N` sends the right side to zero for every fixed `L`, even though the normalized r46 energy diverges. Thus

`QFORM-R46-BALANCED-ENERGY-IMPLIES-BOUNDED-PHYSICAL-CORE`

is false as a standalone structural implication.

Crucially, this is **not** an actual unpaid r40 survivor. It exposes exactly why the upstream disjoint-volume condition must be retained. Let `H_z={z_1,...,z_N}` and let `L_all=union_a(I_a union J_a)`. The physical cross block `A[H_z,L_all]` has `N` orthonormal rows, each of norm one. Consequently

`boxed:
 Z_3=e_3(A[H_z,L_all]A[H_z,L_all]^T)=binom(N,3).
}`

Equivalently, for every triple of blocks the total squared physical disjoint-minor mass is exactly one, so already

`E0>=binom(N,3)`.

The construction is therefore excluded from the actual overlap chamber `E0<1/4`: its failure of bounded-core extraction is paid by aggregate physical volume, not by a hidden good minor.

## 6. Required application of the pinned e5 result

The pinned completed source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

proves Theorem D: for a physical cross block with third volume `Z_3` and row-volume marginals at most `1/2`,

`||p_Q||_infinity <= 6 sqrt(e) Z_3^(-1/6)`,

with arbitrary same-bank quadratic curvature and affine terms retained.

Apply it to the exact stress family above. Every nonzero volume sample chooses three of the `N` hub rows symmetrically, hence each physical row marginal is

`alpha_a=3/N<=1/2` for `N>=6`.

With `Z_3=binom(N,3)`, the completed pinned theorem gives the real full-ambient estimate

`boxed:
 ||p_Q||_infinity
 <= 6 sqrt(e) binom(N,3)^(-1/6)
 <= 6.004270
}`

(the last inequality is the worst endpoint `N=6`). Thus the exact family is not a QFORM counterexample. It is paid for the correct determinant-aggregation reason.

The same conclusion can be seen even more locally from the pinned Theorem H: two literal hubs `z_1,z_2` with all their leaves have Gram matrix `I_2` and leaf leverage `1/(2M)<=1/2`, giving `|phi(t)|<=4pi^2|t|^-2` and hence `||p_Q||_infinity<=4`. I record Theorem D as the required e5 application because it uses exactly the physical third-volume currency relevant to this slot.

## 7. What is now closed and what is not

Closed this run:

1. A pairwise-disjoint matching of r46 kernel-star pairs cannot hide a genuine third exterior direction from the upstream physical disjoint-volume packet: `e3(W^TW)<=E0` exactly.
2. In the actual unpaid `E0<1/4` chamber, every energetic matching has a dimension-free rank-one/rank-two spectral carrier as quantified above.
3. Bounded physical support plus determinant mass converts to an actual `s3` lower bound with the exact `s1 s2` denominator; no single minor is selected. The denominator cannot be deleted universally.
4. The natural many-disjoint-star attempt to make the r46 balanced energy diverge while destroying bounded cores is source-valid but automatically creates huge physical `E0` and is paid by the pinned e5 Theorem D.

Not closed: a large total `E_bal>2048` need not a priori place a fixed amount of weight on a pairwise-disjoint matching. The remaining difficult state is therefore an overlap-dense graph of rank-one physical pairs, together with the algebraic consistency conditions `det A[K,K]=0` on every contributing edge. The next useful proof should turn that overlap density into a literal physical hub/diagonal carrier, or prove that a definite-energy matching exists. It must preserve the small nonzero `lambda_K`, all outside curvature, and all extra spectrum.

Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.
