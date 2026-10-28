SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B13, 2026-09-23T01:30:40Z.
attacking: extremal product laws; force a bad no-pivot finite-grid product witness to contain a constant-energy physical star split into arbitrarily many genuine independent product banks, while simultaneously applying the newest account02/B13 entropic pair-Schur theorem on every useful third-volume cut.

# account01/B13 auto13 — high-window multibank star + entropic pair-Schur counterexample normal form

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T013040Z-account01-B13-qform-auto13`  
Assignment: Extremal product laws  
Status: **ESSENTIAL_STEP_APPLIED / PROVED TARGET-LEVEL COUNTEREXAMPLE NORMAL FORM / FULL QFORM OPEN / CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Exact scope and source pins

The full owner target is unchanged. For arbitrary finite `n`, arbitrary independent real coordinates with densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one universal finite essential density bound for `Q=X^T A X`, or produce a genuine counterexample. No support, moment, iid, sign, log-concavity, interval-support, bounded-fragment, or post-rotation-independence hypothesis is added below.


The completed inputs actually used are:

1. **Designated partner account02/B13 r15**, canonical
   `yspennstate/math-open-problems@d59fc91cdb6c772a0b3c73ba5b90fb62e10e3bf`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T000555Z-account02-B13-productset-r15-482fba/REPORT.md`.
   Its exact finite-mixture/extreme-product reduction plus full-to-no-pivot reduction imply: if full QFORM is false, then for every fixed no-pivot scale `tau>0` the strict no-`tau` product-indicator slab constant is infinite. Its displayed theorem takes `tau=m^-4` and a particular threshold `C3 m`; below I use the same proved selection with the larger threshold `256m`.

2. **Newest completed designated-partner account02/B13 four-hub theorem**, source
   `yspennstate/math-open-problems@ac50e5d5f2c3030c4bd87d5188117d92ceaf55a1`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T013927Z-account02-B13-fourhub-r12/REPORT.md`.
   Its Theorem 4.1 says that for any disjoint physical cross block `M` with third-volume
   `Z=e_3(M^T M)>0`, either the full ambient form obeys
   `||p_Q||_infinity <= 48 sqrt(e/5) Z^(-1/6)`,
   or one genuine physical row-column pair `(i,j)` carries more than `31/512` of `Z`; for a nonzero edge `a=M_ij`, the entire residual Schur two-volume satisfies
   `a^2 e_2(S_* S_*^T)>31 Z/512`, while for `a=0` the corresponding whole cofactor-bank currency exceeds `31 Z/512`.

3. **Conditioned spectral-window branch**, source
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
   with a later target-level application in
   `yspennstate/math-open-problems@ac50e5d5f2c3030c4bd87d5188117d92ceaf55a1`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T154341Z-account03-B20-QFORM-r12/REPORT.md`.
   In the special case `H=empty`, if `P=1_{|A|>=1/64}` satisfies `max_i P_ii<=1/32`, then the full target form has a continuous density bounded by
   `96 sqrt(3e/2)<194`.

4. **Product projection bound** used in its source-valid original-coordinate form:
   for independent cap-one coordinates and nonzero coefficient vector `v`,
   `||p_(v^T X)||_infinity <= sqrt(2)/||v||_2`.
   A source-pinned use appears in `yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7` and in the later B03 aggregate-square report. Only disjoint original-coordinate banks are combined here.

The full theorem remains OPEN. The continuity conclusion remains separately OPEN.

## 2. Threshold amplification of the partner extreme-product normal form

The partner r15 proof uses that, under failure of full QFORM, the strict no-`tau` slab constant is infinite for each fixed `tau>0`. Therefore its finite-grid product-indicator selection is not tied to the numerical threshold `C3m` used there.

Fix an integer `m>=2` and put

`tau_m=m^-4`.

Under failure of full QFORM, choose the same rational finite-grid product-indicator witness as in r15, but with

`|{x in P_m : x^T A_m x in J_m}| / |J_m| > 256 m`.              (2.1)

Here `P_m=prod_k E_{m,k}`, every `|E_{m,k}|=1`, and `A_m` is rational symmetric with `s_3(A_m)>1`. The strict no-pivot inequalities give

`|A_ii|<m^-4`,
`|A_ii A_jj-A_ij^2|<m^-4` for `i!=j`,                           (2.2)

hence

`|A_ij|^2 < mu_m:=m^-4+m^-8` for every `i!=j`.                  (2.3)

This is still the exact product-indicator class: no interval, centered-uniform, support-radius or fragment-count restriction is introduced.

The larger threshold (2.1) is useful because every already-paid branch with a bound of order at most `O(m)` is now automatically excluded on this witness.

## 3. New theorem: every escaping witness has a constant-energy multibank star

### Theorem 3.1 — `QFORM-NOPIVOT-HIGHWINDOW-MULTIBANK-STAR-v1`

Assume full QFORM is false and choose the witness above. Let

`P=1_{|A_m|>=1/64}`.

For every `m>=5` there is an original physical coordinate `i=i(m)` such that

`P_ii>1/32`                                                       (3.1)

and its off-diagonal row energy

`W_i:=sum_(j!=i) A_ij^2`

satisfies

`boxed: W_i>2^-18=1/262144.`                                     (3.2)

Consequently

`boxed:
 #{j!=i:A_ij!=0}
 > m^4/[2^18(1+m^-4)].
}`                                                                  (3.3)

In particular the counterexample normal form has **quartic** physical degree growth along one row, strengthening the preceding global `n_m=Omega(m^2)` conclusion.

Moreover fix any integer `K>=2`. For all sufficiently large `m` satisfying

`mu_m=m^-4+m^-8 <= 2^-19/K`,                                     (3.4)

the coordinates `j!=i` can be partitioned into `K` disjoint original-coordinate banks

`G_1 union ... union G_K={1,...,n}\{i}`

such that, with

`b_a=(A_ij)_(j in G_a)`,

one has for every `a=1,...,K`

`boxed: ||b_a||_2^2 >= 2^-19/K.`                                 (3.5)

The normalized largest physical coefficient in each bank obeys

`boxed:
 max_(j in G_a) A_ij^2/||b_a||_2^2
 <= 2^19 K (m^-4+m^-8) ->0.
}`                                                                  (3.6)

Thus for each fixed `K`, the escaping witness contains `K` **genuinely independent, asymptotically diffuse product banks of uniformly nonzero coupling energy** attached to one original coordinate.

### Proof

If every diagonal of `P` were at most `1/32`, the completed spectral-window branch with `H=empty` would give

`||p_(X^T A_m X)||_infinity <194`.

That would force every interval slab ratio to be `<194`, contradicting (2.1), already for `m>=2`. Hence (3.1).

Write an orthonormal eigenbasis `u_l` of `A_m`. Then

`||A_m e_i||_2^2
 =sum_l lambda_l^2 |u_l(i)|^2
 >=(1/64)^2 P_ii
 >1/(4096*32)=2^-17`.                                             (3.7)

Since the diagonal term contributes only `A_ii^2<m^-8`,

`W_i=||A_m e_i||_2^2-A_ii^2 >2^-17-m^-8`.                        (3.8)

For `m>=5`, `m^-8<2^-18`, proving (3.2).

Every nonzero summand in `W_i` is at most `mu_m` by (2.3), so

`#{j!=i:A_ij!=0} > 2^-18/mu_m
 =m^4/[2^18(1+m^-4)]`,                                            (3.9)

which is (3.3).

For the bank decomposition, put weights `w_j=A_ij^2`, total `W=sum w_j>2^-18`, and threshold

`t=2^-19/K`.

Under (3.4), each `w_j<=t`, while `W>2Kt`. Greedily collect unused coordinates until the running weight first reaches `t`; because each atom is at most `t`, each completed bank uses less than `2t`. After `K-1` such banks, the total used mass is less than `2(K-1)t`, leaving more than `2t`, so a `K`th bank can also be completed. Assign every remaining coordinate arbitrarily among the `K` banks. This proves (3.5). Equation (3.6) follows immediately from `A_ij^2<=mu_m` and (3.5). QED.

For a clean numerical specialization, `K=3` is available once `m>=36`; and the normalized coefficient leverage in every bank is at most `1/32` once `m>=85`.

## 4. Product-law consequence: a genuine K-dimensional rectangle certificate

For the product-indicator witness define

`S_a=sum_(j in G_a) A_ij X_j`, `a=1,...,K`.                       (4.1)

The banks are disjoint sets of **original independent coordinates**, hence `S_1,...,S_K` are mutually independent and are also independent of `X_i`. No rotated variable has been declared independent.

The product-projection estimate and (3.5) give

`||p_(S_a)||_infinity
 <= sqrt(2)/||b_a||_2
 <=1024 sqrt(K).`                                                 (4.2)

Therefore the joint vector `(S_1,...,S_K)` has product density bounded by

`(1024 sqrt(K))^K`.                                                (4.3)

Equivalently, for arbitrary intervals `I_1,...,I_K`, the extreme-product geometry obeys

`boxed:
 |{x in P_m : S_a(x) in I_a for every a=1,...,K}|
 <= (1024 sqrt(K))^K prod_(a=1)^K |I_a|.
}`                                                                  (4.4)

This is uniform in translations, support radius, gaps and fragment count of every `E_{m,j}`. It is a direct geometric inequality on the actual product-indicator witness, not a statement about a rotated joint density.

The original quadratic form can be written exactly as

`Q=A_ii X_i^2 + 2 X_i sum_(a=1)^K S_a + Q_(i^c)(X_(i^c)).`         (4.5)

Equation (4.4) is **not** falsely promoted to a density bound for (4.5): `Q_(i^c)` can have arbitrary same-bank quadratic curvature and can be strongly dependent on each `S_a`. The mixed-hub correction explicitly shows why one must aggregate such curvature before a local collision or reciprocal-coefficient payment.

## 5. Applying the newest account02/B13 theorem to every useful third-volume cut

The new multibank star is simultaneous with a second, independent structural constraint coming from the newest designated-partner account02/B13 theorem.

Let `I,J` be any disjoint original-coordinate sets and put

`M=A_m[I,J]`,
`Z=e_3(M^T M)`.

Assume

`s_3(M)>=1/m`.                                                     (5.1)

Then

`Z>=s_3(M)^6>=m^-6`.                                               (5.2)

The paid branch of account02/B13 r12 would give the actual ambient inequality

`||p_Q||_infinity
 <=48 sqrt(e/5) Z^(-1/6)
 <=48 sqrt(e/5) m
 <35.392 m`.                                                       (5.3)

But the selected extreme-product witness has slab ratio `>256m`, so (5.3) is impossible. Therefore **every** cut satisfying (5.1) lies in the partner's pair-Schur/cofactor branch.

Thus there is a genuine physical pair `(r,c) in I x J` carrying

`Z_rc>31 Z/512`.                                                   (5.4)

If the physical edge `a=A_rc` is nonzero, the entire residual Schur cross bank

`S_*=N-c_vec r_vec^T/a`

obeys

`boxed:
 a^2 e_2(S_*S_*^T)>31 Z/512 >=31/(512 m^6).
}`                                                                  (5.5)

Using the strict no-`m^-4` pair condition,

`a^2<m^-4(1+m^-4)`,                                               (5.6)

so

`boxed:
 e_2(S_*S_*^T)
 >31/[512 m^2(1+m^-4)]
 >31/(1024m^2).
}`                                                                  (5.7)

If instead `a=0`, the partner's whole cofactor-bank currency satisfies

`boxed: H_rc>31 Z/512 >=31/(512m^6).}`                            (5.8)

This is the requested actual application of the designated partner result to an inequality: the `35.392m` paid slab estimate is directly contradicted by the selected `>256m` extreme-product slab, forcing the pair-Schur/cofactor alternative on every useful third-volume cut.

For completeness, the r15 `D_5` theorem also improves on this amplified witness. With

`C5=5 sqrt(2e)=11.6582199...`,

the ratio `>256m` forces, for every disjoint cross block,

`boxed: s_5(M)<C5/(256m)<0.04554/m.}`                            (5.9)

So an escaping witness is simultaneously high-window/star-diffuse, pair-Schur anchored on each useful third-volume cut, and uniformly very close to cross rank at most four.

## 6. Why the newest corrections do not invalidate this theorem

Three late corrections are particularly relevant.

1. `QFORM-R-ROBUST-TWODIR-FREE-IMPLICATION-FALSE-v1` shows that low-order aggregate currencies alone do not force one physical cross block with a universal lower bound on `sigma_1 sigma_2`. Nothing above makes that inference. Equation (5.7) retains the **whole** Schur `e_2` aggregate.

2. `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1` gives a mixed-hub star-plus-rank-one family where every local pair collision deteriorates although the full aggregated form is uniformly paid. The multibank conclusion (3.5)-(4.4) is deliberately an **aggregation-before-collision** statement. It does not select one star edge.

3. `QFORM-MIXED-SKELETON-DETERMINANT-ONLY-L1-FALSE-v1` shows that a nonzero mixed skeleton determinant does not by itself provide the missing third time-integrability direction once same-bank curvature is ignored. No determinant-only L1 claim is made here.

The earlier corrections concerning pointwise quadratic oscillatory decay, post-rotation independence, conditional projection caps, bounded-support continuity and fixed-fragment extremality are likewise not used.

## 7. New counterexample normal form and first unpaid implication

Combining Sections 2--5 gives the following sharper target-level normal form.

### Corollary 7.1 — `QFORM-NOPIVOT-MULTIBANK-PAIR-SCHUR-NORMAL-FORM-v1`

If full QFORM is false, then for every fixed `K>=2` and all sufficiently large `m` there is a rational finite-grid product-indicator witness with slab ratio `>256m`, `s_3(A)>1`, strict no-`m^-4` physical pivots, and all of the following simultaneously:

- one original coordinate has off-diagonal row energy `>2^-18` and degree `Omega(m^4)`;
- its star couplings split into `K` disjoint genuine product banks, each with squared coupling norm at least `2^-19/K`, and each bank becomes coefficient-diffuse as `m->infinity`;
- the corresponding bank projections satisfy the translation/fragment-uniform rectangle inequality (4.4);
- every disjoint cross block has `s_5<0.04554/m`;
- every cross block with `s_3>=1/m` is forced into one physical pair carrying the whole quantitative Schur `e_2` currency (5.5)-(5.7), or the zero-edge cofactor currency (5.8).

This is stronger than the preceding max-volume skeleton alone: it identifies a **constant-energy probabilistic product resource** inside the escaping witness, not merely a low-cross-rank matrix approximation.

The first unpaid implication is now

`QFORM-N3-MULTIBANK-STAR-PAIR-SCHUR-GLUING-v1`:

> Starting from the same extreme-product witness, combine the constant-energy multibank star (4.5) with the forced aggregate Schur/cofactor resource on useful cuts **before** any local reciprocal coefficient, collision, or absolute Fourier payment. Route the resulting packet to one of the completed aggregate mechanisms (mixed-hub/Fresnel, rank-two-cross plus aggregate square, product plus two squares, D'/D5, ridge), or prove a new grouped-bank estimate for the remaining genuinely entangled in-bank curvature.

A valid closure must keep the original product-coordinate provenance. The bank-density estimate alone is not enough because the same-bank quadratic remainder can correlate with the bank projection; this is exactly where the latest mixed-hub correction bites.

## 8. Verification notes

The constants are elementary:

`48 sqrt(e/5)=35.3918672374591...`,
`96 sqrt(3e/2)=193.849240381844...`,
`5 sqrt(2e)=11.6582199079856...`.

For the bank threshold, (3.4) is first satisfied at `m=36` for `K=3`, `m=39` for `K=4`, and `m=46` for `K=8`. The stronger sufficient condition making the normalized maximum coefficient at most `1/32` is first satisfied at `m=85,91,108` respectively.

The proof is analytic. These numerical checks only corroborate the displayed constants and integer thresholds.

## 9. Status

Full QFORM essential boundedness remains **OPEN / NOT PROVED**. Full-target continuity remains **OPEN**. This run proves a stricter target-level counterexample normal form and an exact product-set rectangle certificate, and consumes the newest account02/B13 result at the inequality level. No public release, email, notification change, scheduler mutation, new task, paid API/model call, cross-account authentication, or permission expansion was performed. Repository synchronization is recorded separately from native brain ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.