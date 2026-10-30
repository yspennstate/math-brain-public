SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-22T22:10:41Z.
attacking: universal proof assembly at the heavy-null two-bank residue; compress the partner partition into a nondegenerate mixed null-triple/symplectic-area packet and pay its rank-two analytic currency before any reciprocal atom selection.

# fleet01/B19 r11 — heavy-null mixed symplectic packet and half-Riesz payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control used:** revision `2026-09-22.15` at fresh-control refresh; QFORM is the sole research target.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL+ANALYTIC PAYMENT / FULL TARGET OPEN`.

The full theorem remains OPEN: for independent original-coordinate real inputs with densities bounded by one and symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound on the density of `X^T A X`. Continuity remains separate.

This report preserves the live corrections. It does not use post-rotation independence, the refuted arbitrary-joint rank-three coarea bound, a positive conditional projection-density moment, law-uniform one-dimensional pointwise quadratic-phase decay, a worst-fiber supremum, a fixed-good-minor assertion, or perturbative deletion of small curvature under unrestricted fragmented supports.

## 1. Source-pinned current inputs

### 1.1 Assigned partner fleet02/B19 r19

Use the completed partner report

`yspennstate/math-open-problems@718ed012b3271daaab97d01e459c400c877aee0d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260922T210733Z-fleet02-B19-qform-r19/REPORT.md`.

In the compressed exact-rank-three heavy-null state it has

`A = U M U^T`, `U^T U = I_3`, `D:=|det M|>=1/2`,

with a distinguished original coordinate `0` whose row is

`u_0=sqrt(c) r`, `c>=7/9`, `r^T M r=0`.

In an orthonormal spectral basis `(r,e,w)`, every complementary row is

`u_j=(alpha_j,v_j)`, `v_j=(beta_j,gamma_j) in R^2`.

The partner consumes fleet03/B19's two-bank partition and supplies disjoint original-coordinate banks `J,K` such that

`S_J:=sum_(j in J) v_j v_j^T`, `S_K:=sum_(k in K) v_k v_k^T`,

`S_J+S_K=I_2`,

`det(S_J) det(S_K) >= 1/640`.                                  (1.1)

The same partner proves the exact-span endpoint and every leakage residual bounded away from zero, leaving only the positive-near-zero leakage interpolation as its local analytic debt.

### 1.2 Fresh structural peer fleet03/B10 r19

Use

`yspennstate/math-open-problems@bb2a985a44425ae3cbfd222da9c42fee8486cf51`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260922T214631Z-fleet03-B10-QFORM-r19/REPORT.md`.

It proves the exact slope-gap identity and four-stratum exterior-volume decomposition, and in particular converts the near-span state into a constant aggregate O3 principal-triple packet without dividing by the small leakage residuals. Its remaining analytic debt is aggregate-before-inversion payment of that diffuse packet.

### 1.3 Rank-two analytic peer fleet03/B06 r17

Use

`yspennstate/math-open-problems@898bf19622a52a515c2034b27ae5f98dd0e21f75`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T194649Z-fleet03-B06-qform-r17/REPORT.md`.

If disjoint original-coordinate banks have exact rank-two cross block `C`, with nonzero singular product `Pi_2(C)`, then for arbitrary same-bank quadratic-affine phases

`R=F(X_J)+2 X_J^T C X_K+G(X_K)`

has an `L^3` density satisfying

`||p_R||_3 <= (3e)^(2/3) Pi_2(C)^(-1/3)`.                       (1.2)

This theorem keeps arbitrary same-bank self curvature; it is not a zero-self statement.

## 2. New theorem: a universal symplectic cross packet is already present

Let

`Omega=[[0,1],[-1,0]]`,

and let `V_J,V_K` be the matrices whose rows are `v_j^T`, `v_k^T`. Define the rectangular original-bank matrix

`C_perp := V_J Omega V_K^T`.                                    (2.1)

Thus

`(C_perp)_(j,k)=det(v_j,v_k)=beta_j gamma_k-gamma_j beta_k`.    (2.2)

This is a derived transverse/symplectic operator, not the physical cross block `A[J,K]`; that distinction is essential.

### Theorem 2.1 — `QFORM-HEAVYNULL-SYMPLECTIC-PACKET-v1`

Under the partner hypotheses (1.1), `C_perp` has exact rank two and

`boxed:
 Pi_2(C_perp)
 = sqrt(det S_J det S_K)
 >= 1/sqrt(640).
`                                                                    (2.3)

Moreover both nonzero singular values satisfy

`boxed: s_2(C_perp)>=1/sqrt(640).`                                (2.4)

Finally

`boxed:
 ||C_perp||_F^2
 >= 2/sqrt(640).
`                                                                    (2.5)

#### Proof

Because `S_J,S_K` are positive definite, `V_J,V_K` each have column rank two, so `C_perp` has rank two. Cauchy--Binet on the exact rank-two factorization gives

`Pi_2(C_perp)^2
 = det(V_J^T V_J) det(Omega)^2 det(V_K^T V_K)
 = det(S_J)det(S_K)`,                                              (2.6)

which proves (2.3).

Since `S_J<=I_2` and `S_K<=I_2`, both `||V_J||_op` and `||V_K||_op` are at most one, hence

`s_1(C_perp)<=1`.                                                  (2.7)

Therefore

`s_2(C_perp)=Pi_2(C_perp)/s_1(C_perp)>=1/sqrt(640)`,             (2.8)

proving (2.4). Finally

`||C_perp||_F^2=s_1^2+s_2^2>=2s_1s_2=2Pi_2(C_perp)`,             (2.9)

and (2.3) gives (2.5). QED.

### Equivalent trace identity

For later use,

`||C_perp||_F^2
 = tr(S_J)tr(S_K)-tr(S_JS_K)`.                                  (2.10)

If `lambda_1,lambda_2` are the eigenvalues of `S_J`, this is

`lambda_1(1-lambda_2)+lambda_2(1-lambda_1)`.

The AM--GM lower bound in (2.5) is therefore sharp at the level of determinant-product information.

## 3. New target-matrix consequence: a constant mixed null principal-triple bank

For every `j in J,k in K`, exact-rank-three principal-minor factorization gives

`det A[{0,j,k},{0,j,k}]
 = det(M) det(u_0,u_j,u_k)^2`.                                   (3.1)

Because `u_0=sqrt(c)r` and `v_j,v_k` are the coordinates orthogonal to `r`,

`det(u_0,u_j,u_k)^2
 = c det(v_j,v_k)^2`.                                           (3.2)

Hence

`|det A[{0,j,k}]|
 = D c |(C_perp)_(j,k)|^2`.                                     (3.3)

Summing (3.3) and applying Theorem 2.1 gives the exact aggregate identity and universal lower bound

`boxed:
 sum_(j in J,k in K) |det A[{0,j,k}]|
 = D c ||C_perp||_F^2
 >= 2Dc/sqrt(640)
 >= 7/(9 sqrt(640))
 = 0.03074436614... .
`                                                                    (3.4)

### Corollary 3.1 — `QFORM-HEAVYNULL-MIXED-O3-BANK-v1`

Every compressed heavy-null state carrying the assigned B19 two-bank partition has a constant principal-triple determinant packet specifically on triples

`{0,j,k}`, `j in J`, `k in K`,

with one coordinate from each of the three mutually independent source groups `{0}`, `J`, `K`. No near-span assumption is required.

This is stronger structurally than merely knowing that some O3 packet exists: its composition is fixed to the null pivot plus one coordinate from each independent transverse bank. It also holds before deciding whether the longitudinal leakage residuals vanish, are small, or are large.

It does **not** imply that one physical triple has a dimension-free determinant; the mass may be arbitrarily diffuse over `j,k`.

## 4. Analytic payment of the whole symplectic packet before atom selection

Although `C_perp` is not the physical cross block of `Q`, it is itself an honest exact-rank-two matrix between the original-coordinate banks `J,K`. Therefore the completed rank-two theorem (1.2) applies to the following entire auxiliary family.

### Theorem 4.1 — `QFORM-SYMPLECTIC-AREA-L3-v1`

For arbitrary real quadratic-affine functions `F` on the `J` coordinates and `G` on the `K` coordinates, set

`R=F(X_J)+2 X_J^T C_perp X_K+G(X_K)`.                           (4.1)

Then for all independent cap-one input laws,

`boxed:
 ||p_R||_3
 <= (3e)^(2/3) Pi_2(C_perp)^(-1/3)
 <= (3e)^(2/3) 640^(1/6)
 < 11.894.
`                                                                    (4.2)

All same-bank self terms and affine shifts are allowed.

This is an actual application of completed peer mathematics to the partner's quantitative packet: the partner's determinant-product inequality (1.1) supplies the nondegenerate `Pi_2`, and the B06 theorem pays the full diffuse operator at once. No `j,k` atom is selected.

## 5. New fractional-trace consequence: uniform half-Riesz currency

The `L^3` bound has exactly enough integrability to produce the half-Riesz quantity that appears in scalar-square and Schur transducers.

### Lemma 5.1

If a probability density `p` satisfies `||p||_3<=M`, then

`boxed:
 sup_t int_R p(x)|x-t|^(-1/2) dx
 <= 4(4/3)^(3/4) M^(3/4).
`                                                                    (5.1)

#### Proof

For `rho>0`, Holder on `|x-t|<=rho` gives

`int_(|x-t|<=rho) p(x)|x-t|^(-1/2)dx
 <= M (int_(-rho)^rho |u|^(-3/4)du)^(2/3)
 =4M rho^(1/6).`                                                   (5.2)

The complement contributes at most `rho^(-1/2)`. Thus

`H_(1/2)<=4M rho^(1/6)+rho^(-1/2)`.                              (5.3)

The minimizer satisfies `rho^(2/3)=3/(4M)`; at that point the first term is three times the second, yielding (5.1). QED.

Combining Lemma 5.1 with Theorem 4.1 gives

### Theorem 5.2 — `QFORM-SYMPLECTIC-AREA-HALFRIESZ-v1`

For every `R` in (4.1),

`boxed:
 H_(1/2)(R)
 :=sup_t E|R-t|^(-1/2)
 <=4(4/3)^(3/4) sqrt(3e) Pi_2(C_perp)^(-1/4)
 <=31.787.
`                                                                    (5.4)

Again this is uniform in dimension, arbitrary same-bank self curvature, arbitrary signs, and all cap-one input laws.

The important point is conceptual: **the diffuse mixed null-triple packet already carries a uniformly paid half-Riesz resource.** The outstanding issue is no longer reciprocal payment of its atoms.

## 6. A general mixed-exterior compressor

The same rank-three geometry gives a useful source-valid compressor for the mixed stratum isolated by fleet03/B10.

Let arbitrary row families `u_i in R^3`, `i in J union K`, satisfy

`sum_(i in J)u_i u_i^T <= I_3` and `sum_(k in K)u_k u_k^T<=I_3`,

and define

`E_21=sum_(i<j in J,k in K) det(u_i,u_j,u_k)^2`.

Form the matrix `T` from `R^K` to pair-space `R^(J choose 2)` by

`T_({i,j}),k=det(u_i,u_j,u_k)`.                                  (6.1)

Then `rank(T)<=3`, `||T||_F^2=E_21`; hence a unit `z in R^K` exists with

`||Tz||_2^2>=E_21/3`.                                           (6.2)

Set `a=sum_k z_k u_k`. Since

`||Tz||^2=a^T adj(G_J)a`, `G_J=sum_(i in J)u_i u_i^T<=I`,       (6.3)

and `adj(G_J)<=I`, one has

`||a||^2>=E_21/3`.                                              (6.4)

Choose an orthonormal basis `b,d` of `a^perp`. With

`p_i=b dot u_i`, `q_i=d dot u_i`,

one has

`det [[||p||^2,p dot q],[p dot q,||q||^2]]
 =sum_(i<j)(p_iq_j-q_ip_j)^2
 =||Tz||^2/||a||^2
 >=E_21/3`,                                                      (6.5)

where the last inequality uses `||a||<=1`.

Thus a mixed O3 packet of mass `E_21` always compresses to a two-dimensional aggregate on one bank whose coefficient-Gram determinant is at least `E_21/3`, together with a unit coefficient aggregate on the other bank. This does not yet solve the hidden-fiber problem, but it proves that diffuseness of the physical triples does **not** destroy all low-dimensional aggregate geometry.

For the B10 threshold `E_21>=1/128`, the two-dimensional Gram determinant in (6.5) is at least `1/384`, so its product-projection density cap is at most `2 sqrt(384)<39.192`.

## 7. Compact conditional end-to-end proof map after this run

The current route can be stated without pretending the theorem is finished.

1. Existing global reductions pay the low-offdiagonal, ridge-diffuse, quantitative physical-pair, exact cross-rank at least three, and several scalar-Schur branches.
2. In the exact-rank-three heavy-null residual, assigned partner fleet02/B19 r19 pays the exact-span endpoint and every leakage residual bounded away from zero. Its only local gap is the simultaneous positive-near-zero leakage regime.
3. Fresh fleet03/B10 r19 removes the structural singularity in that regime: its slope-gap/exterior decomposition forces constant aggregate principal-triple mass without any reciprocal leakage factor.
4. **New here:** the same B19 partition in fact supplies, for every heavy-null state, the more structured packet (3.4): null pivot `0` plus one coordinate from each independent bank `J,K`. The associated transverse symplectic operator has exact rank two, `Pi_2>=1/sqrt(640)`, and its whole diffuse operator is analytically paid in `L^3` and half-Riesz norm by (4.2),(5.4).

Therefore the first essential missing implication has narrowed to the following product-preserving transducer.

### `QFORM-HEAVYNULL-SYMPLECTIC-TRACE-TRANSDUCER-v1` — OPEN

In the canonical heavy-null exact-rank-three phase

`Q=2s RY+dY^2+2gYZ+fZ^2`,

with `s^2|f|=|det M|>=1/2`, distinguished independent null scalar `X_0`, and the partner's disjoint `J,K` partition, convert the uniform half-Riesz payment of the derived symplectic area operator

`C_perp=(det(v_j,v_k))_(j in J,k in K)`, `Pi_2(C_perp)>=1/sqrt(640)`,

into an `L^infinity` density bound for the **actual** quadratic form `Q`, while retaining the longitudinal hidden-fiber variables and arbitrary same-bank curvature. Equivalently, prove a dependence-safe trace/comparison inequality that spends (5.4) without replacing the product-linear source by a receiver-only bounded joint/conditional density.

This is narrower than generic `O3 aggregate payment`: the available packet already has an exact null pivot, two disjoint independent banks, a fixed rank-two symplectic operator, and a universal half-Riesz constant `<31.787`.

A tempting but invalid shortcut is to identify `C_perp` with `A[J,K]`; they are different matrices. The next proof must expose `C_perp` through a valid Schur/trace/decoupling identity or derive an equivalent paid operator from the actual phase. This report makes no such unsupported identification.

## 8. Outcome

- `QFORM-HEAVYNULL-SYMPLECTIC-PACKET-v1`: **PROVED**.
- `QFORM-HEAVYNULL-MIXED-O3-BANK-v1`: **PROVED**.
- `QFORM-SYMPLECTIC-AREA-L3-v1`: **PROVED by applying completed fleet03/B06 mathematics to the partner packet**.
- `QFORM-SYMPLECTIC-AREA-HALFRIESZ-v1`: **PROVED**.
- full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- continuity: **not proved by the new branch**.

No email, public release, new task, cross-account authentication, paid/remote compute, permission expansion, scheduler mutation, or notification change was performed.
