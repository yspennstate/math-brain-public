SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T07:42:52Z.
attacking: the k=1 near-null physical-core scale debt; test whether the three-large-eigenvalue hypothesis can force the rank-one random-slope resource, and if not replace that false forcing step by a determinant-balanced two-hub/Pluecker payment on a genuine diffuse target family.

# fleet03/B09 r26 — near-null core scale forcing is false; determinant-balanced Pluecker bypass

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **REFUTED INTERMEDIATE SCALE-FORCING MECHANISM / NEW TWO-FRAME STRUCTURAL LEMMA / PEER THEOREM APPLIED TO A STRICT-N3 DIFFUSE FAMILY / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. This report attacks the first structural debt left by fleet03/B09 r25: whether the target spectral hypothesis can force a universal lower bound on the rank-one physical-pair resource `|sigma| ||H n||` after a quantitative two-row wedge has been extracted. It cannot. I give an explicit target-valid family for which that resource tends to zero while the aggregate cross wedge stays exactly one, every physical coefficient tends to zero, and even every physical `2 x 2` principal determinant tends to zero. The same family is nevertheless paid uniformly by the completed determinant-balanced two-hub theorem of fleet02/B09. Thus the correct next mechanism is not reciprocal near-null-core payment; it is an augmented-frame Pluecker/ridge/localization routing.

No Gaussian, moment, compact-support, connected-support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is used. The positive density estimate below applies to every admissible independent cap-one input law. No probability squaring occurs, and the final interval bound is linear in interval length.

## 1. Fresh sources and exact missing implication


The predecessor fleet03/B09 r25 is

`yspennstate/math-open-problems@195447da931f086720afaa12ac902ed7d33dd32e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T061516Z-fleet03-B09-QFORM-r25/REPORT.md`.

For a nonzero rank-one physical pair core `E=sigma r r^T`, internal null direction `n`, and full complementary coupling matrix `H`, it proved

`||p_Q||_infinity
 <=4*2^(3/4)*e^(1/4) (|sigma| ||H n||_2)^(-1/2)`              (1.1)

whenever `H n !=0`. It also combined the completed fleet02/B09 k=1 torsion theorem with the wedge identity to obtain, at `eta=1/16`,

`||p_Q||_infinity
 <46.212 [M_T/(|sigma| |Theta|)]^(1/2)`,                       (1.2)

where `M_T=||H_T r||` and `Theta` is the coefficient-space torsion. The explicit unresolved implication was to force a universal-scale paid resource or route simultaneous near-null degeneration elsewhere.

The completed compatible B09 peer theorem used positively below is fleet02/B09 r13,

`QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`,

canonical source

`yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T064043Z-fleet02-B09-QFORM-r13/REPORT.md`.

For two literal physical hubs, leaf bank `I`,

`A_II=D+sum_(j=1)^r lambda_j v_j v_j^T`,

actual cross columns `c_1,c_2`, augmented deterministic frame

`W=[v_1,...,v_r,c_1,c_2]`, `G=W^T W>0`,

and determinant-weighted disjoint-basis mass `rho` of the whitened frame `U=W G^(-1/2)`, it proves the **core-independent** bound

`||p_Q||_infinity
 <= C_r [rho det(G) prod_j |lambda_j|]^(-1/(r+4)),`            (1.3)

where

`C_r=((r+4)/(r+2)) exp((r+2)/(r+4))`.                          (1.4)

The actual physical `2 x 2` hub core is arbitrary. The theorem yields a continuous density and the same coefficient times `|L|` for every interval `L`.

The designated `fleet04/B09` current-QFORM memory/handoff directory was absent at the fresh canonical check. I therefore do not fabricate a designated-partner theorem and do not wait; the completed compatible fleet02/B09 theorem is applied at an actual inequality in Section 5.

## 2. Counterexample family to core-resource forcing

Fix an integer `k>=2` and set

`m=k^4`.                                                         (2.1)

Use two literal physical hub coordinates `h_1,h_2` and three mutually disjoint leaf banks `I_a,I_b,I_c`, each of cardinality `m`. Let

`a=m^(-1/2) 1_(I_a)`,
`b=m^(-1/2) 1_(I_b)`,
`c=m^(-1/2) 1_(I_c)`,                                          (2.2)

regarded as orthonormal vectors in the full leaf coordinate space. Define the symmetric matrix

`A_k = k^(-1) e_(h1)e_(h1)^T
      + k (e_(h1) a^T + a e_(h1)^T)
      + k^(-1) (e_(h2) b^T + b e_(h2)^T)
      + c c^T.`                                                 (2.3)

Every displayed vector is supported on original physical coordinates; (2.3) is not a spectral change of random variables.

The physical hub core is

`E_k = diag(k^(-1),0)`.                                         (2.4)

Hence `E_k` has rank one. In its own physical basis we may take

`r=e_(h1)`, `n=e_(h2)`, `sigma=k^(-1)`.                         (2.5)

The hub-to-leaf coupling matrix `H_k` has columns

`H_k r = k a`, `H_k n = k^(-1) b`.                              (2.6)

Therefore

`||H_k r||=k`, `||H_k n||=k^(-1)`,                              (2.7)

and the two-row aggregate wedge is exactly

`Delta(H_k)=det(H_k^T H_k)=k^2*k^(-2)=1`.                       (2.8)

But the r25 rank-one random-slope resource is

`|sigma| ||H_k n|| = k^(-2) ->0`.                               (2.9)

Thus **a unit aggregate wedge plus the target spectral hypothesis cannot force a positive universal lower bound on the rank-one core resource**. In particular, (1.1) can become arbitrarily weak on a perfectly target-valid family even though the cross rows remain quantitatively two-dimensional.

This does not refute (1.1); it refutes only the proposed next structural step of forcing its denominator away from zero.

## 3. Exact target spectrum and diffuse local geometry

The active invariant subspace is

`span{e_(h1), e_(h2), a, b, c}`.                                (3.1)

In the orthonormal basis ordered as `(e_(h1),a,e_(h2),b,c)`, the nonzero part of `A_k` is the orthogonal direct sum

`[[k^(-1), k], [k,0]]
 direct_sum
 [[0,k^(-1)],[k^(-1),0]]
 direct_sum
 [1].`                                                          (3.2)

Hence the nonzero spectrum is exactly

`lambda_+(k)=(k^(-1)+sqrt(k^(-2)+4k^2))/2`,
`lambda_-(k)=(k^(-1)-sqrt(k^(-2)+4k^2))/2`,
`+k^(-1)`, `-k^(-1)`, `1`.                                     (3.3)

For `k>=2`,

`lambda_+(k)>=k>=2`,                                            (3.4)

and

`|lambda_-(k)|
 =(sqrt(k^(-2)+4k^2)-k^(-1))/2
 >= k-(2k)^(-1)
 >=7/4>1`.                                                      (3.5)

Together with the eigenvalue `1`, every `A_k` satisfies the exact target hypothesis with at least three eigenvalues of modulus at least one.

At the same time, every physical coefficient is small. Since `sqrt(m)=k^2`, the only nonzero coefficient scales are

`A_(h1,h1)=k^(-1)`,
`A_(h1,j)=k/sqrt(m)=k^(-1)` for `j in I_a`,
`A_(h2,j)=k^(-1)/sqrt(m)=k^(-3)` for `j in I_b`,
`A_(i,j)=m^(-1)=k^(-4)` for `i,j in I_c`.                       (3.6)

Thus

`max_(i,j)|A_ij|=k^(-1)->0`.                                   (3.7)

In particular every physical `2 x 2` principal determinant has magnitude at most `k^(-2)`: the largest one is the hub-one / `I_a` determinant `-k^(-2)`. Every physical `3 x 3` determinant tends to zero as well; the crude Leibniz bound is

`|det A_S| <= 6 k^(-3)` for every `|S|=3`.                      (3.8)

For `k>=129`,

`max_i |A_ii|<1/128`,
`max_(i<j)|det A_{ {i,j} }|<1/128`.                             (3.9)

Thus the family lies inside the standard strict-N3 local no-pivot chamber while the rank-one core resource (2.9) vanishes. The obstruction is genuinely diffuse/anisotropic, not a hidden large physical coefficient.

### Consequence `QFORM-K1-CORE-RESOURCE-FORCING-ALONE-FALSE-v1`

There is no universal `c>0` such that the three-large-eigenvalue hypothesis, even together with a unit two-row aggregate wedge, implies

`|sigma| ||H n|| >= c`                                         (3.10)

for every selected nonzero rank-one physical pair core. This remains false in families for which all physical coefficients and all physical `2 x 2` principal determinants tend to zero.

The correct structural proof therefore has to route anisotropy **before** taking the reciprocal rank-one core resource.

## 4. A two-dimensional Pluecker collision identity

The peer theorem (1.3) suggests a clean structural replacement in the two-cross-column case. I record the exact elementary identity because it turns failure of determinant-balanced smoothing into a concrete physical-row concentration statement.

Let `U in R^(N x 2)` have orthonormal columns. Write its row vectors as `u_i`, define leverages

`ell_i=||u_i||_2^2`,                                            (4.1)

and for every unordered pair `{i,j}` define the Pluecker basis weight

`w_ij=det(u_i,u_j)^2`.                                         (4.2)

By Cauchy--Binet,

`sum_(i<j) w_ij=1`.                                             (4.3)

Let `S,T` be iid random two-element bases distributed according to `w`, and put

`rho=P(S cap T=empty)`.                                         (4.4)

For the determinantal basis law,

`P(i in S)=ell_i`.                                              (4.5)

Therefore

`E |S cap T| = sum_i ell_i^2`.                                 (4.6)

Since two two-element sets can intersect in zero, one, or two elements, and intersection size two is exactly the event `S=T`,

`P(S=T)=sum_(i<j) w_ij^2`.                                     (4.7)

Writing `p_1=P(|S cap T|=1)` and `p_2=P(S=T)`, we have

`1=rho+p_1+p_2`,
`sum_i ell_i^2=p_1+2p_2`.                                      (4.8)

Eliminating `p_1` gives the exact identity

`boxed:
rho = 1-sum_i ell_i^2 + sum_(i<j) w_ij^2.`                    (4.9)

In particular, if `rho<rho_0`, then

`sum_i ell_i^2 > 1-rho_0`.                                    (4.10)

Because `sum_i ell_i=2`,

`boxed:
max_i ell_i > (1-rho_0)/2.`                                   (4.11)

Thus small disjoint-basis mass cannot remain completely diffuse: it forces a literal original physical leaf carrying a definite fraction of the **whitened aggregate two-row cross geometry**.

### Corollary `QFORM-TWOHUB-CROSS-PLUCKER-DICHOTOMY-v1`

Suppose a two-hub packet has a diagonal leaf block and cross matrix `C=[c_1,c_2]` with `G=C^T C>0`. Whiten `U=C G^(-1/2)` and let `rho` be its two-dimensional disjoint-basis mass. For any `0<rho_0<1`, either

1. `rho>=rho_0`, in which case fleet02/B09 r13 gives the **core-independent continuous-density payment**

   `||p_Q||_infinity <=2sqrt(e) [rho_0 det G]^(-1/4)`,          (4.12)

   with the same coefficient times interval length; or

2. there is a physical leaf `i` with

   `c_i^T G^(-1)c_i > (1-rho_0)/2`.                            (4.13)

The second alternative is a finite physical localization certificate, not a density conclusion. It is precisely the object that should be passed to a physical-pair/grouped/ridge exit rather than dividing by a vanishing hub-core determinant.

This lemma is scale invariant: multiplying one cross direction by `R` and the other by `R^(-1)` does not change the whitened geometry. That is exactly the anisotropy that defeats (3.10).

## 5. Apply the completed two-hub theorem to the diffuse counterexample family

The family in Section 2 has an exact leaf decomposition with one same-side curvature direction:

`A_(II)=c c^T`,                                                 (5.1)

so in (1.3) take

`r=1`, `lambda=1`, `v=c`,
`c_1=k a`, `c_2=k^(-1)b`.                                      (5.2)

The augmented frame is

`W=[c,k a,k^(-1)b]`.                                           (5.3)

Since `a,b,c` are orthonormal,

`G=W^T W=diag(1,k^2,k^(-2))`,
`det G=1`.                                                      (5.4)

Whitening removes the cross anisotropy exactly:

`U=W G^(-1/2)=[c,a,b]`.                                        (5.5)

Each column is flat on its own disjoint bank of size `m`. A nonzero three-row Pluecker basis must select exactly one physical coordinate from each of the three banks. Every such basis has weight

`m^(-3)`,                                                       (5.6)

and there are `m^3` of them. Two iid bases are disjoint iff their chosen coordinate differs in each bank. Hence the disjoint-basis mass is **exactly**

`rho_k=(1-1/m)^3=(1-k^(-4))^3`.                                (5.7)

Apply the completed peer theorem (1.3) with `r=1`. Since `det G=|lambda|=1`,

`boxed:
||p_(X^T A_k X)||_infinity
 <=(5/3)e^(3/5) rho_k^(-1/5)
 =(5/3)e^(3/5)(1-k^(-4))^(-3/5).`                              (5.8)

For `k>=2`, `m>=16`, so

`rho_k>=(15/16)^3`                                              (5.9)

and therefore

`boxed:
||p_(X^T A_k X)||_infinity <3.157.`                            (5.10)

The same number times `|L|` bounds

`P{X^T A_k X in L}`                                             (5.11)

for every interval `L`, and the density is **continuous** on this whole family.

This is the required actual application of a completed other-worker B09 theorem. It is particularly informative because the r25 rank-one payment deteriorates like `k` on exactly the same family:

`(|sigma| ||H n||)^(-1/2)=k`,                                  (5.12)

while the determinant-balanced augmented-frame theorem stays below `3.157`. The loss in (1.1) is therefore a proof-coordinate anisotropy loss, not a real concentration phenomenon in this branch.

## 6. What this changes in the B09 proof map

The r25 next step was phrased as `QFORM-K1-NEARNULL-CORE-SCALE-FORCING-v1`. Section 3 proves that a **core-only** version of that forcing statement is false, even in a strict-N3 diffuse family with a unit aggregate cross wedge. The route must change on this same target.

The viable replacement is

`QFORM-K1-ANISOTROPY-TO-AUGMENTED-PLUCKER-OR-LOCALIZATION-v1`:

> Before paying a reciprocal near-null physical-core scale, form the determinant-balanced augmented coefficient frame consisting of the two hub-to-bank cross directions and whatever exact low-rank same-side curvature is available. If its determinant product and disjoint-basis mass are at universal scale, use the core-independent two-hub theorem. If the disjoint mass is small, use the Pluecker rank-split/high-leverage certificate to produce a literal finite physical core or a disjoint lower-dimensional bank and route that object to an already-paid physical-pair, grouped, ridge, or star mechanism. Only after these aggregate exits fail should one invoke a reciprocal rank-one core resource.

For one same-side curvature direction, the large-disjointness branch is already completely paid by (1.3). The previously proved fleet03/B09 three-dimensional small-disjointness theorem `QFORM-PLUCKER-SMALLRHO-RANKSPLIT-v1` supplies the complementary source-coordinate `k=1,2,3` rank splits. The remaining work is therefore the **finite routing of those small-disjointness outputs**, not a universal lower bound on `|sigma| ||H n||`.

This is a genuine mechanism change triggered by an explicit obstruction, while preserving all earlier valid rank-one random-slope work.

## 7. Scope and continuity

- Full QFORM: **OPEN / not proved / not disproved**.
- New negative result: `QFORM-K1-CORE-RESOURCE-FORCING-ALONE-FALSE-v1` refutes only an intermediate structural forcing step.
- New positive structural lemma: `QFORM-TWOHUB-CROSS-PLUCKER-DICHOTOMY-v1` gives a paid large-disjointness branch and a literal high-leverage physical-leaf certificate otherwise.
- Target-valid diffuse family: for every `k>=2`, all admissible cap-one product laws satisfy the continuous-density bound (5.10); for `k>=129` the matrices also lie in the strict local no-pivot chamber.
- Full-target continuity: **OPEN**.

The designated `fleet04/B09` partner still had no completed current-QFORM artifact at the fresh check. No peer activity is fabricated. The completed fleet02/B09 result is applied quantitatively in (5.8)--(5.10).

## 8. Reproducibility

`CHECK.py` in this immutable run directory verifies the exact nonzero spectrum formula, the number of target-scale eigenvalues for representative `k`, the physical coefficient scale, the vanishing rank-one resource, the exact Pluecker mass, and the numerical constant `<3.157`. These computations are sanity checks; the proof is the algebra above.

Repository transport is not native learned-memory ingestion. Status remains `WITHOUT_VERIFIED_BRAIN`. No task identity, schedule, email/push notification, public release, paid model/API/Codex call, credential, or cross-account authentication state was changed.
