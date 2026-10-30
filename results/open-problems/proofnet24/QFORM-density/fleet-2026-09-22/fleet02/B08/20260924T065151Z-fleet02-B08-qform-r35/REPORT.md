SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-24T06:51:51.649816Z.
attacking: the rank-two balanced-crossing cancellation survivor: transfer lost crossing rank into actual same-bank child spectral multiplicity, then split those child windows into localized versus diffuse physical frames.

# fleet02/B08 r35 — cross-rank / child-count transfer

Status: **NEW SUPPORTING STRUCTURAL THEOREM + QUANTIFIED LOCALIZED/DIFFUSE ROUTER + EXACTLY-THREE-LARGE-EIGENVALUE STRESS FAMILY / FULL QFORM OPEN**.

Execution status: `WITHOUT_VERIFIED_BRAIN`. Authenticated repository retrieval occurred, but no verified native brain receiver was available in this run.

## First unpaid implication

`QFORM-BILATERAL-CHILD-CROSS-COMPILER-v1`.

After the r34 diffuse-top-three balanced cut and its marginal-free third-compound payment, an unpaid state has a literal original-coordinate crossing `B=A[S,T]` with

` s_3(B) < theta_* L,    theta_* = 0.05512604949999305,`

while the selected three-eigenvector frame is balanced on both banks. The new theorem below shows that the lost third crossing direction cannot disappear: it reappears as **actual principal-block spectral curvature on both banks**. More precisely, with

` kappa_* = sqrt(3/5)-theta_* = 0.7194706197414904,`

an unpaid state is now in one of two explicit chambers:

1. `s_2(B) >= theta_* L`: the literal crossing has two target-scale singular directions, and **each** same-bank principal block has an eigenvalue of modulus `> kappa_* L`.
2. `s_2(B) < theta_* L`: **each** same-bank principal block has at least two eigenvalues of modulus `> kappa_* L`.

In either chamber, for the corresponding child spectral window, either some original physical row has Euclidean norm `> (kappa_*/4)L = 0.1798676549353726 L`, or that child window has physical leverage at most `1/16` row-by-row. Thus the still-unpaid hybrid is no longer “rank-two crossing plus arbitrary same-bank curvature”: it is a rank-two/two-child or rank-one/two-by-two-child configuration with an explicit original-coordinate localization alternative.

The next compiler must use these bilateral child resources without assuming that an already-localized physical coordinate interacts with the crossing. The stress family below shows that such a localized coordinate can be completely disconnected.

## Theorem: balanced cross rank forces bilateral child spectral multiplicity

### `QFORM-BALANCED-CROSS-RANK-TO-CHILD-COUNT-v1`

Let `A` be real symmetric. Let `U in R^{n x 3}` have orthonormal columns and

` A U = U Lambda,    min_j |Lambda_jj| >= L. `

Let `S,T` be a partition of the original physical coordinates and assume

` alpha I_3 <= U_S^T U_S <= beta I_3,`
` alpha I_3 <= U_T^T U_T <= beta I_3,`

for numbers `0<alpha<=beta`. Write

` H_S=A[S,S],   H_T=A[T,T],   B=A[S,T].`

For `q in {1,2,3}`, if

` s_q(B) <= delta L,`

then each of `H_S,H_T` has at least `4-q` eigenvalues (counted with multiplicity) of modulus at least

` (sqrt(alpha/beta)-delta)L. `

Equivalently,

` s_{4-q}(H_S), s_{4-q}(H_T) >= (sqrt(alpha/beta)-delta)L,`

where singular values are in decreasing order. This is an **actual principal-block spectral gate**; no rotated independence is asserted or used.

### Proof

Let `R_{q-1}(B)` be the span of the first `q-1` right singular vectors of `B` (empty when `q=1`). Define

` W_T={a in R^3 : U_T a is perpendicular to R_{q-1}(B)}. `

The condition imposes at most `q-1` linear equations on `a`, hence

` dim W_T >= 3-(q-1)=4-q. `

Because `U_T^T U_T >= alpha I`, the map `a -> U_T a` is injective. For every `a in W_T`, the singular-value variational characterization gives

` ||B U_T a|| <= s_q(B)||U_T a|| <= delta L sqrt(beta)||a||. `

Restricting the eigen-equation `AU=U Lambda` to the `S` rows yields

` H_S U_S a + B U_T a = U_S Lambda a. `

Therefore

` ||H_S U_S a||`
` >= ||U_S Lambda a||-||B U_T a||`
` >= sqrt(alpha)L||a||-delta L sqrt(beta)||a||. `

Since `||U_S a||<=sqrt(beta)||a||`, every nonzero vector in the `(4-q)`-dimensional space `U_S W_T` satisfies

` ||H_S x||/||x|| >= (sqrt(alpha/beta)-delta)L. `

The min-max formula for singular values gives the claimed lower bound for `s_{4-q}(H_S)`. Because `H_S` is symmetric, these singular values are absolute eigenvalues. The `T` statement is identical after using the first `q-1` **left** singular vectors of `B` and the `T`-row eigen-equation

` B^T U_S a + H_T U_T a = U_T Lambda a. `

This proves the theorem. `square`

## The r34 balanced cut: numerical specialization and localized/diffuse split

The r34 balanced physical cut has

` alpha=3/8, beta=5/8 `

and, after failure of the benchmark `197.7780678260685/L`,

` s_3(B)<theta_* L,`
` theta_*=6^(4/3)/197.7780678260685`
`        =0.05512604949999305. `

Hence

` kappa_* = sqrt((3/8)/(5/8))-theta_*`
`         = sqrt(3/5)-theta_*`
`         = 0.7194706197414904. `

The theorem gives the full hierarchy

` s_3(B)<theta_*L  =>  s_1(H_S),s_1(H_T)>kappa_*L,`
` s_2(B)<theta_*L  =>  s_2(H_S),s_2(H_T)>kappa_*L,`
` s_1(B)<theta_*L  =>  s_3(H_S),s_3(H_T)>kappa_*L. `

Now take on either bank any `d=4-q` orthonormal eigenvectors belonging to eigenvalues of modulus `>kappa_*L`, and let `P` be their physical spectral projection. Spectral decomposition gives, for every physical row `i`,

` ||H[i,*]||_2^2 = ||H e_i||_2^2`
`                 >= kappa_*^2 L^2 P_ii. `

Therefore

` P_ii>1/16  =>  ||H[i,*]||_2 > (kappa_*/4)L`
`                         = 0.1798676549353726 L. `

Otherwise `max_i P_ii<=1/16`, which is exactly a quantitative diffuse physical-frame certificate. In the `s_2(B)<theta_*L` chamber this yields a two-dimensional diffuse child frame on **both** banks unless a strong physical row is already present.

This threshold deliberately matches the `1/16` child-frame leverage gate in the newest completed fleet03/B08 theorem read in this run (`20260924T061920Z-fleet03-B08-qform-diffuse-r51`). That partner theorem is a one-hub/two-child result. If a product-safe physical hub/principal subsystem is additionally produced while retaining a third singular value at scale

` L_p = kappa_* L / sqrt(47/48) = 0.7270842774794581 L, `

then its child hypothesis `s_2(C)>=sqrt(47/48)L_p` is automatic and the partner transverse branch would pay `<93.296/L_p <128.316/L`, or else return its double-rank-two alignment/localization alternatives. What is **not** proved here is that such a hub can always be extracted while retaining that third spectral scale. That is the precise interface debt; the theorem above is hub-free and valid before any local inversion.

## Exactly-three-large-eigenvalue double-cancellation stress family

### `QFORM-EXACT3-WALSH-DOUBLE-CANCELLATION-STRESS-v1`

This family realizes the difficult `s_2(B)<theta_*L` chamber with bilateral diffuse two-child curvature and a completely disconnected localized coordinate.

Let `m=2^q>=1024`. Identify the `m` coordinates with `F_2^q`. Write `w_a` for the normalized Walsh character

` w_a(x)=(-1)^{a dot x}/sqrt(m). `

Take

` chi(x)=(-1)^{e_1 dot x}`  (an unnormalized sign character),
` u_1=w_0,   u_2=w_{e_2},   u_3=w_{e_3},`
` v_2=chi .* u_2=w_{e_1+e_2},`
` v_3=chi .* u_3=w_{e_1+e_3}. `

These five normalized Walsh vectors are orthonormal. Add one separate original coordinate `z`. For `alpha_0=0.9`, set

` A_m = L(u_1u_1^T+u_2u_2^T+u_3u_3^T)`
`       + alpha_0 L(v_2v_2^T+v_3v_3^T)`
`       + (L/2)e_z e_z^T. `

Its nonzero spectrum is exactly

` {L,L,L,0.9L,0.9L,0.5L}. `

Thus it has **exactly three** eigenvalues of modulus at least `L`.

Let `S_0={x:chi(x)=+1}` and `T={x:chi(x)=-1}`, and put the isolated coordinate `z` into `S=S_0 union {z}`. For the selected top-three frame `U=[u_1,u_2,u_3]`,

` U_S^T U_S=U_T^T U_T=(1/2)I_3, `

and the physical top-three row leverage is `3/m<1/48`.

On this half-cut, `v_j=u_j` on `S_0` and `v_j=-u_j` on `T` for `j=2,3`. Hence the two `0.9L` modes cancel ninety percent of the `u_2,u_3` crossings. The literal crossing has exactly

` s(B)=(0.5L,0.05L,0.05L,0,...). `

Consequently

` s_2(B)=s_3(B)=0.05L<theta_*L. `

The complementary crossing `(A_m-A_3)[S,T]` has rank two and singular values `0.45L,0.45L`; along each cancelled Walsh direction the signed cancellation is exactly `-0.45L`.

The same-bank principal blocks have, on the Walsh carrier,

` spec_nonzero(H_S|carrier)=spec_nonzero(H_T|carrier)`
`                           ={0.95L,0.95L,0.5L}. `

Thus the two cancelled crossing directions reappear as two `0.95L` child eigenvalues on each bank. Their normalized two-frame has physical row leverage `4/m<=1/256`, far inside the `1/16` diffuse gate. Because this half-cut is exactly `1/2`-balanced, the theorem's sharper exact-balance lower bound is `1-0.05=0.95`, and the family attains it exactly in those two directions.

The isolated coordinate `z` simultaneously has `A_zz=L/2` and spectral-window leverage one, but is completely disconnected from the crossing. Thus a localized row need not interact with the cancellation packet.

Finally, no uniformly conditioned physical pair is available. On two Walsh coordinates every matrix entry has magnitude at most

` (3+2*0.9)L/m = 4.8L/m, `

so every such `2x2` principal block has operator norm at most

` 9.6L/m <= 0.009375L < L/64. `

For a pair containing `z`, the block is diagonal and its smaller diagonal entry is `4.8L/m<=0.0046875L<L/64`.

This is therefore a genuine exactly-three-large-eigenvalue obstruction to any proof that demands a well-conditioned physical pair or demands that the already-localized coordinate couple to the rank-deficient crossing.

## Required pinned-source theorem applied to this real target inequality

The family is **not** a QFORM counterexample. Apply the completed generalized rank-`r` Fresnel--Brascamp--Lieb Theorem F from

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

(`FOURIER_ROUTE_REPORT.md`). It states for

` A=D+R Lambda R^T `

with original-coordinate product sources, a diagonal `D`, rank-`r` frame row leverage at most `1/2`, and nonzero frame eigenvalues `lambda_j`, that

` ||p_Q||_infinity <= [4r/(r-2)] prod_j |lambda_j|^{-1/r},   r>2, `

with the characteristic-function proof giving a continuous `C_0` density.

For the present rank-five diffuse frame

` R=[u_1,u_2,u_3,v_2,v_3], `

all Walsh rows have leverage `5/m<=1/2`, the `z` row has frame leverage zero, and `D=(L/2)e_z e_z^T` is diagonal. The rank-five eigenvalue product is

` L^3(0.9L)^2 = 0.81 L^5. `

Therefore, for every admissible collection of independent densities bounded by one,

` ||p_{X^T A_m X}||_infinity`
` <= (20/3)(0.81L^5)^(-1/5)`
` = (20/3) 0.9^(-2/5) L^(-1)`
` = 6.953632543404217... / L, `

and `p in C_0(R)`.

This is a direct application of a completed theorem from the required fixed source to an actual target-valid obstruction. It shows that **whole-frame diffuse aggregation succeeds exactly where local physical-pair extraction and crossing third-volume both fail**.

## Remaining hybrid after r35

Combining r34 and the new child-count transfer gives a concrete two-way unresolved geometry before any invalid post-rotation step:

- **Genuine rank-two crossing chamber:** `s_2(B)>=theta_*L`, `s_3(B)<theta_*L`, and each bank has at least one `kappa_*L` child eigenmode. Unless a row of norm `>0.1798676549L` appears, these child modes may be taken physically diffuse at leverage `<=1/16`.
- **Rank-one crossing / bilateral-two-child chamber:** `s_2(B)<theta_*L`; each bank has at least two `kappa_*L` child eigenmodes. Unless a row of norm `>0.1798676549L` appears, both two-dimensional child frames are physically diffuse at leverage `<=1/16`.

If even `s_1(B)<theta_*L`, each bank has three eigenvalues of modulus `>kappa_*L`; this is a further child-dominated subcase, not a payment by itself because arbitrary same-bank residual curvature and conditioning-generated affine terms remain.

The fixed-source Walsh example above sits in the second chamber and demonstrates that the localized high-window coordinate can be irrelevant. A successful next proof should aggregate the bilateral diffuse child frames and the remaining crossing at the product-source level **before** selecting a reciprocal physical pivot. No moment, support, log-concavity, diagonal-basis, or post-rotation independence assumption is used here.

Full unrestricted QFORM and global continuity remain **OPEN**.
