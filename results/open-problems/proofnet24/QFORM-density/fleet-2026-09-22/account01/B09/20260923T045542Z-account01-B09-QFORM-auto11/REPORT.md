SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T04:55:42Z.
attacking: the remaining exact global clique-factor N3 branch; turn the target spectral gap into a quantitative mixed-hub Gram determinant, apply account02/B09 Pluecker smoothing without rotating the product law, and localize the only surviving small-disjointness branch onto at most three physical leaves.

# account01/B09 auto11 — exact clique: no-heavy closure and unique-heavy finite-core reduction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T045542Z-account01-B09-QFORM-auto11`  
Assignment: Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL-ANALYTIC CLOSURE / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report closes the entire exact clique-factor branch of the strict `N3(1/128)` chamber whenever no clique coordinate is individually heavy, and reduces the remaining exact-clique branch to one unique heavy clique coordinate together with a quantitatively transverse hub direction and, if the account02/B09 smoothing certificate fails, a mixed direction localized to at most three physical leaves.

The proof stays in original physical coordinates. It does not use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint 3D coarea, positive moments of conditional projection heights, deletion of an overlapping square, or a fixed-minor lower bound.

## 1. Source-pinned inputs


The immediate B09 predecessor is

`yspennstate/math-open-problems@96594eeaba7df69cc9414fd77ef8119fda034867`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T041440Z-account01-B09-QFORM-auto11/REPORT.md`.

It proves: inside strict `N3(1/128)`, the exact global cut-rank-one leaf classification has no triangle survivor, its global star branch is completely paid, and exact hub/clique alignment is impossible. Thus the only exact global cut-rank-one B09 survivor entering this run is a nonaligned clique-factor leaf block.

The designated partner input is the latest completed account02/B09 theorem

`QFORM-MIXED-HUB-PLUCKER-SMOOTHING-v1`,

canonical source

`yspennstate/math-open-problems@c5a57d1be0dc69e47bcb9fb52d5eaac77f4833c6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T041423Z-account02-B09-QFORM-auto11/REPORT.md`.

For one physical hub `h`, leaf bank `I`, arbitrary outside bank and

`A_II=D+lambda vv^T`,

put `c=A[I,h]`, `W=[v,c]`, `G=W^T W`, and whiten `W` to a two-column orthonormal frame `U`. If `rho` is the probability that two iid Pluecker-distributed physical two-coordinate bases of `U` are disjoint, then, whenever `rho>0`,

`||p_Q||_infinity <= 3 exp(2/3) [rho |lambda| det(G)]^(-1/3)`.   (1.1)

The density is continuous and every interval `J` obeys the same coefficient times `|J|`. The same report proves the basis-free lower bound

`rho >= 1-sum_i ell_i^2`,                                    (1.2)

where `ell_i` are the row leverages of `U`, and the failure certificate: if `rho<r`, some unit active mixed direction in `range(W)` has coordinate energy outside a physical two-coordinate set at most `sqrt(r)`.

## 2. Strict N3 constants and normalized exact clique model

Set

`tau=1/128`,
`eta=sqrt(tau+tau^2)=sqrt(129)/128`,
`delta=tau+eta=(1+sqrt(129))/128`,
`q=1-delta=(127-sqrt(129))/128`.

Numerically,

`eta = 0.088732942903129275...`,
`delta = 0.096545442903129275...`,
`q = 0.903454557096870725...`.                               (2.1)

Strict `N3(tau)` means

`|A_ii|<tau`,
`|det A[{i,j},{i,j}]|<tau`

for every physical coordinate and pair, while the target gives `s_3(A)>=1`. Hence

`|A_ij|^2 < tau+tau^2 = eta^2`,

so

`boxed: |A_ij|<eta  (i!=j).`                                 (2.2)

In the exact clique-factor branch, after absorbing the magnitude of the clique coefficient into the clique vector, write the full leaf block as

`A_II = D + s uu^T`,                                         (2.3)

where `s in {+1,-1}`, `D` is diagonal, and for distinct leaves

`A_ij=s u_i u_j`.

The hub-leaf vector is

`c=A[I,h]`,                                                   (2.4)

and `a=A_hh`. Put

`x_i=u_i^2`.

Then (2.2) gives

`x_i x_j<eta^2` for `i!=j`,                                  (2.5)

and

`c_i^2<eta^2`.                                                (2.6)

Consequently at most one clique coordinate can satisfy `x_i>eta`.

The partner invariant in the normalized representation is simply

`P=det([u,c]^T[u,c])`.                                       (2.7)

Indeed this equals the invariant `|lambda|det(G)` in an unnormalized representation.

## 3. No heavy clique coordinate: spectral gap forces a well-conditioned mixed frame

Assume

`x_i<=eta` for every leaf `i`.                                (3.1)

Define the rank-at-most-three core

`R = [[a,c^T],[c,s uu^T]]`.                                  (3.2)

Because

`D_ii=A_ii-sx_i`,

(3.1) and strict N3 give

`||D||_op < tau+eta=delta`.                                  (3.3)

Thus

`A=R+diag(0,D)`

and singular-value perturbation yields

`s_3(R)>=1-delta=q`.                                         (3.4)

Since `rank R<=3`, (3.4) forces `rank R=3` and all three nonzero singular values of `R` to be at least `q`.

Let

`t=||u||^2`,

and decompose

`c=alpha e + beta z`,

where `e=u/||u||`, `z perp e`, `||z||=1`, `beta>0`. On `span{e_h,e,z}`, the core is exactly

`M=[[a,alpha,beta],[alpha,s t,0],[beta,0,0]]`.                (3.5)

Its least singular value is at least `q`.

### 3.1 Three quantitative consequences of `s_min(M)>=q`

First,

`||M e_z||=beta`,

so

`beta>=q`.                                                    (3.6)

Second, for

`y=e-(alpha/beta)z`,

we have `My=s t e`. Hence

`t>=q`.                                                       (3.7)

Third, apply `M^{-1}` to `e_z`. Direct solution gives a third coordinate

`(alpha^2/(s t)-a)/beta^2`.

Since `||M^{-1}||<=1/q`,

`|alpha^2/(s t)-a|<=beta^2/q`,

and therefore, using `|a|<tau`,

`alpha^2/t <= tau+beta^2/q`.                                 (3.8)

Now let

`G=[u,c]^T[u,c]`.

Its determinant is

`det G=t beta^2`,                                             (3.9)

while (3.8) gives

`tr G=t+alpha^2+beta^2
 <= t(1+tau+beta^2/q)+beta^2`.                               (3.10)

For a positive `2x2` matrix, `lambda_min(G)>=det(G)/tr(G)`. Using (3.6)-(3.7) in (3.10),

`boxed:
lambda_min(G)
 >= mu := q^2/(1+tau+2q)
 =0.289986097603086270... .`                                 (3.11)

This is the essential missing implication: the target spectral gap prevents the apparently dangerous mixed frame from becoming arbitrarily ill-conditioned once no individual clique coefficient is heavy.

## 4. Automatic Pluecker diffuseness and complete payment of the no-heavy clique branch

The raw physical row of `[u,c]` at leaf `i` is `(u_i,c_i)`. By (3.1) and (2.6),

`||(u_i,c_i)||^2 <= eta+eta^2`.                              (4.1)

Let `ell_i` be the leverage of this row in the whitened frame. By (3.11),

`ell_i
 <= (eta+eta^2)/mu
 =0.333141756994184640...
 <1/3.`                                                       (4.2)

Because a two-column orthonormal frame has `sum_i ell_i=2`,

`sum_i ell_i^2 <= (max_i ell_i) sum_i ell_i <2/3`.            (4.3)

The account02/B09 determinant-weighted basis inequality (1.2) therefore gives the **uniform** disjoint-basis mass

`boxed: rho>1/3.`                                             (4.4)

Also, since the three nonzero singular values of `R` are at least `q`, its pseudodeterminant obeys

`|pdet R|>=q^3`.                                              (4.5)

But from (3.5),

`|det M|=t beta^2=det G`,                                    (4.6)

so

`boxed: P=det G>=q^3.`                                       (4.7)

Now apply the designated account02/B09 theorem (1.1) with the **actual inequalities** (4.4) and (4.7):

`||p_Q||_infinity
 <=3e^(2/3)(rho P)^(-1/3)
 < [3e^(2/3)/q] 3^(1/3)
 <9.328.`                                                     (4.8)

Thus

`boxed: ||p_Q||_infinity<9.328`,
`boxed: P{Q in J}<9.328 |J|`                                 (4.9)

for every admissible product law on this entire no-heavy exact-clique branch. The partner Fourier envelope is integrable, so the density is **continuous** here.

This is stronger than the preceding B09 frontier: a mixed-frame row of leverage above `1/2` is impossible unless a clique coordinate itself is physically heavy.

## 5. Unique heavy clique coordinate: transversality cannot collapse

It remains to consider the unique index `k` with

`x_k>eta`.                                                    (5.1)

By (2.5), every `j!=k` satisfies

`x_j<eta^2/x_k<eta`.                                         (5.2)

Orthogonally decompose the hub vector as

`c=gamma u+r`,
`r perp u`,
`beta=||r||`.                                                 (5.3)

I claim

`boxed: beta>0.18.`                                          (5.4)

This gives a quantitative nonalignment statement rather than only the qualitative exclusion proved in the previous run.

To prove it, note from the `k`th physical hub edge and (2.6) that

`|gamma| sqrt(x_k)
 <= |c_k|+|r_k|
 < eta+beta`,

hence

`gamma^2 < (eta+beta)^2/eta`.                                (5.5)

Let

`d_k=A_kk-sx_k`

and define

`B=s(u+s gamma e_h)(u+s gamma e_h)^T+d_k e_k e_k^T`.          (5.6)

This matrix has rank at most two. The difference `A-B` consists of:

1. the hub diagonal error `a-s gamma^2`;
2. the hub-leaf cross error `r`;
3. the leaf diagonal errors `D_jj=A_jj-sx_j` for `j!=k`.

By (5.2), the third piece has operator norm `<delta`. The first two pieces together are the arrowhead matrix

`E0=[[a-s gamma^2,r^T],[r,0]]`,

whose exact operator norm is

`||E0||
 = ( |a-s gamma^2| + sqrt(|a-s gamma^2|^2+4 beta^2) )/2`.     (5.7)

Using `|a|<tau` and (5.5), define

`E(beta)=tau+(eta+beta)^2/eta`.

Then

`||A-B||
 < delta + ( E(beta)+sqrt(E(beta)^2+4beta^2) )/2`.            (5.8)

The right side is increasing in `beta`. At `beta=0.18`, direct substitution of the exact constants gives

`delta + ( E(0.18)+sqrt(E(0.18)^2+4(0.18)^2) )/2
 =0.9559327633541367...<1`.                                  (5.9)

Therefore `beta<=0.18` would imply `s_3(A)<=||A-B||<1`, since `rank B<=2`, contradicting the target. This proves (5.4).

Consequently the partner invariant is already at universal scale:

`P=||u||^2 beta^2
 >=x_k beta^2
 > eta(0.18)^2
 =0.00287494735006138... .`                                  (5.10)

So in the heavy-coordinate branch the mixed Gram determinant itself is **not** the remaining obstruction.

## 6. Partner theorem pays all but a finite-core Pluecker-localized survivor

Apply the same designated account02/B09 theorem once more. If

`rho>=1/256`,                                                 (6.1)

then (1.1) and (5.10) give

`||p_Q||_infinity
 <3e^(2/3)[(1/256) eta(0.18)^2]^(-1/3)
 <261`.                                                       (6.2)

Hence every interval obeys

`boxed: P{Q in J}<261 |J|`,                                  (6.3)

and the density is continuous on this subbranch.

If instead

`rho<1/256`,                                                  (6.4)

the exact small-`rho` failure certificate in the partner report produces a physical two-coordinate set `S` and a unit vector `w` in the active mixed plane `span{u,c}` such that

`sum_(i notin S) w_i^2 <= sqrt(rho)<1/16`.                   (6.5)

Let

`F=S union {k}`.

Then `|F|<=3`, the unique physically heavy clique coordinate belongs to `F`, and the same active mixed direction satisfies

`boxed: sum_(i notin F) w_i^2<1/16.`                         (6.6)

Thus the previously vague heavy-row nonalignment survivor has been reduced to an explicit **at-most-three-physical-leaf localization witness** while retaining the universal transverse reserve

`||P_{u^perp}c||>0.18`                                       (6.7)

and the mixed determinant reserve (5.10).

No density conclusion is claimed from (6.6) alone. The next step must elevate this finite set without conditioning away the remaining spectral resource.

## 7. What this run changes

The exact global cut-rank-one chamber in strict `N3(1/128)` now routes as follows.

- Star: already paid, `<4.428`, continuous.
- Triangle: already excluded.
- Exact clique, `max_i u_i^2<=eta`: **paid in this run**, `<9.328`, continuous.
- Exact clique, unique `u_k^2>eta`, `rho>=1/256`: **paid in this run**, `<261`, continuous.
- Exact clique, unique `u_k^2>eta`, `rho<1/256`: the only remaining exact-clique B09 node; it has the quantitative transversality (5.4), determinant reserve (5.10), and a mixed direction with at least `15/16` of its coordinate energy on at most three physical leaves.

The next obligation is therefore

`QFORM-N3-CLIQUE-UNIQUEHEAVY-3LOCAL-ROUTING-v1`:

elevate the at-most-three localized leaves together with the hub and spend either the resulting finite physical core, a two-hub wedge, a grouped slope packet, or a residual diffuse one-dimensional frame, while preserving all same-bank curvature and the third target direction.

## 8. Target status and continuity

This report does **not** prove the unrestricted conjecture and does not give a counterexample. `QFORM-FULL` remains OPEN. It proves continuous bounded densities on the two partner-paid exact-clique subbranches (Sections 4 and 6). No global continuity claim is made.

Execution label remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval and synchronization are not being conflated with a verified native receiver-memory ingestion event.
