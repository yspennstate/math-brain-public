SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T18:51:32Z.
attacking: close the canonical projected-compound marginal gate by an exact base-times-height promotion identity; keep the random variables in original product coordinates and test the resulting bound on a dense rotated indefinite form.

# account01/B04 r17 — canonical compound promotion removes the grouped-crossing marginal gate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `SUPPORTING_THEOREM_PROVED / MARGINAL_GATE_REMOVED_FOR_CANONICAL_GROUPED_CROSSING / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Continuity in the new branch: **proved (`C_0`)**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not proved** here. No random variable is rotated. No law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea estimate, worst conditional density cap, moment hypothesis, compact support, connected support, Gaussianity or log-concavity is used.

## 1. Pinned inputs and source boundary

Fresh owner control remains revision `2026-09-22.15`, with QFORM as the sole research target and the full conjecture still open.

The analytic grouped-crossing receiver is the checked source

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The exact subset-entropy refinement used below is the preceding account01/B04 result

`QFORM-GROUPED-CROSSING-EXACT-SUBSET-ENTROPY-v1`,

`yspennstate/math-open-problems@13f0b0b271b4e230cb5493e887ed5ec7dd65f63b`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T181304Z-account01-B04-QFORM-auto11-r16/REPORT.md`.

For a two-physical-hub endpoint with an arbitrary one-volume residual, including failure of the one-volume marginal gate, I use the completed account03/B19 theorem

`QFORM-R2-PHYSICAL-TWOROW-TRANSVERSE-COMPILER-v1`,

`yspennstate/math-open-problems@f09b670173440c4c511985c9a89baf38f97e82c1`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T183023Z-account03-B19-QFORM-r38/REPORT.md`.

The designated account02/B04 result actually applied below is

`QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`,

`yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260923T111930Z-qform/REPORT.md`.

The newer account02/B04 heavy-row report at `beaf7fe9fb87fb81a13a35d5237793eb3b0dde14` was also read. Its exact `L^{-1/3}` hub certificate is compared in Section 7; nothing from it is silently promoted to a general theorem.

## 2. New exact entropy identity for fixed-cardinality subset laws

Let `w` be any probability distribution on the `ell`-subsets `S` of a finite physical row set. Put

`alpha_i=P_w(i in S)`,

and define the exact subset factor appearing in the weighted product-Fourier proof by

`F_ell(w)^2 = exp( H(w) + sum_i alpha_i log alpha_i )`.          (2.1)

As usual `0 log 0=0`.

Choose, conditionally on `S`, a uniformly random ordering `(I_1,...,I_ell)` of the elements of `S`. Every ordered-coordinate marginal is

`p_i=P(I_r=i)=alpha_i/ell`.                                      (2.2)

Let

`TC(I_1,...,I_ell)=sum_(r=1)^ell H(I_r)-H(I_1,...,I_ell)>=0`     (2.3)

be total correlation. Since

`H(I_1,...,I_ell)=H(w)+log(ell!)`,                               (2.4)

and

`ell H(p)=-sum_i alpha_i log alpha_i + ell log ell`,             (2.5)

we obtain the exact identity

`boxed:
 H(w)+sum_i alpha_i log alpha_i
 = ell log ell - log(ell!) - TC(I_1,...,I_ell).`                 (2.6)

Therefore

`boxed:
 F_ell(w)^2 = (ell^ell/ell!) exp(-TC),
 F_ell(w) <= sqrt(ell^ell/ell!).}`                               (2.7)

This is strictly sharper than the generic entropy-subadditivity relaxation `F_ell<=exp(ell/2)`. For `ell=1`, `F_1=1`. For `ell=2`,

`boxed: F_2(w)^2=2 exp(-I(I_1;I_2)) <=2.`                        (2.8)

The upper bound is asymptotically sharp: for the uniform law on all two-subsets of an `m`-point set, `F_2(w)^2=2(m-1)/m ->2`.

## 3. Exact promotion identity for canonical compound volume

Use the grouped-crossing notation. Thus `X_H` and `X'` are independent original-coordinate banks; `W=U^T X_H` has density cap `M_H`; and

`Q=F(X_H)+2<W,M X'+beta>+R(X')`.                                (3.1)

Split the light original coordinates into `I,J`. Assume `M_J` has row rank `k` and singular-value product

`S = product_(a=1)^k s_a(M_J)>0`.                               (3.2)

Let `Pi` denote orthogonal projection in coefficient space onto `row(M_J)`, and put

`C=(A_R)_[I,J](I-Pi)`.                                          (3.3)

Fix `ell>=1` and assume

`Z_ell=e_ell(CC^T)>0`.                                           (3.4)

For each physical `ell`-subset `E subset I`, let

`D_E=det(C_E C_E^T)`,

and use the canonical compound-volume law

`nu(E)=D_E/Z_ell`.                                                (3.5)

Its physical row marginals are

`alpha_i=P_nu(i in E)`.                                          (3.6)

Suppose `alpha_h>0` for one physical row `h in I`. Move the **original scalar coordinate** `X_h` from the light bank to the hub bank. Let `c_h` be row `h` of `C`. The enlarged hub-to-`J` crossing matrix is obtained by stacking the physical row `(A_R)_{h,J}` below `M_J`. The base-times-height determinant identity gives its singular-value product

`boxed: S_+ = S ||c_h||_2.`                                      (3.7)

After this promotion, the remaining projected crossing rows are

`C_+ = C_[I\{h},*](I-Pi_{c_h})`                                 (3.8)

inside `row(M_J)^perp`. Put

`Z_(ell-1)^+ = e_(ell-1)(C_+ C_+^T)`, with `Z_0^+=1`.             (3.9)

For every `(ell-1)`-set `T subset I\{h}`, another base-times-height identity gives

`det(C_[{h} union T] C_[{h} union T]^T)
 = ||c_h||_2^2 det((C_+)_T (C_+)_T^T)`.                         (3.10)

Summing (3.10) over `T` and using (3.5)-(3.6) yields the exact compound-currency recursion

`boxed:
 ||c_h||_2^2 Z_(ell-1)^+ = alpha_h Z_ell,`                       (3.11)

and therefore

`boxed:
 S_+^2 Z_(ell-1)^+ = alpha_h S^2 Z_ell.`                         (3.12)

No small singular value is selected or inverted. One projected smoothing direction is converted into one **physical original-coordinate hub direction**, the total smoothing count is unchanged, and the only currency loss is the actual canonical inclusion probability `alpha_h`.

The hub density cap does not worsen: `(W,X_h)` has joint density at most `M_H`, because `X_h` is an independent original coordinate with density at most one.

## 4. Main theorem — canonical grouped crossing with no row-marginal assumption

Set

`d=k+ell>2`,

and define

`a_r=r^r/r!` for `r>=1`, `a_0=1`.                                (4.1)

### Theorem `QFORM-CANONICAL-COMPOUND-PROMOTION-v1`

In the setup (3.1)-(3.4), **no row-marginal hypothesis is required**. The full quadratic form has a continuous density in `C_0(R)` and

`boxed:
 ||p_Q||_infinity
 <= [d/(d-2)]
    2^((k+3ell)/(2d))
    (ell^ell/ell!)^(1/(2d))
    M_H^(1/d)
    (S^2 Z_ell)^(-1/(2d)).`                                     (4.2)

The same right side multiplied by `2pi` bounds `integral_R |phi_Q(t)|dt`.

#### Proof

Run the following finite deterministic promotion algorithm.

At stage `j`, the hub dimension is `k_j`, the residual compound order is `ell_j`, and

`k_j+ell_j=d`.                                                    (4.3)

Initially `(k_0,ell_0)=(k,ell)`. If `ell_j>=1` and every canonical `ell_j`-volume row marginal is at most `1/2`, stop. Otherwise choose a row with

`alpha_j>1/2`                                                     (4.4)

and promote that original coordinate by Section 3. Then

`k_(j+1)=k_j+1`, `ell_(j+1)=ell_j-1`,                            (4.5)

and the determinant currency satisfies exactly

`S_(j+1)^2 Z_(ell_j-1)^(j+1)
 =alpha_j S_j^2 Z_(ell_j)^j`.                                   (4.6)

The process terminates after at most `ell` promotions. Write `p` for the number of promotions and `r=ell-p` for the terminal residual order.

If `r>=1`, the terminal canonical volume law has every row marginal at most `1/2`. Apply the exact-subset-entropy grouped-crossing theorem. Because the law is canonical, its determinant/entropy currency is exactly `Z_r`, while (2.7) gives

`F_r <= a_r^(1/2)`.                                               (4.7)

Thus

`||p_Q||_infinity
 <=[d/(d-2)]
   2^((k+p+3r)/(2d))
   a_r^(1/(2d))
   M_H^(1/d)
   (S_p^2 Z_r)^(-1/(2d)).`                                      (4.8)

If `r=0`, all smoothing directions have been promoted to the hub. Apply the exact-rank crossing theorem to the resulting `d`-dimensional hub-to-`J` crossing. The product-law projection density on the `J` side is at most `2^(d/2)`, so the same formula (4.8) holds with `a_0=1`, `Z_0=1`.

Iterating (4.6) gives

`S_p^2 Z_r = S^2 Z_ell product_(j=0)^(p-1) alpha_j`.             (4.9)

Every promoted row obeys `alpha_j>1/2`, so

`(product alpha_j)^(-1) <2^p`.                                  (4.10)

Also

`k+p+3r = k+3ell-2p`.                                           (4.11)

Finally `a_r<=a_ell` for `0<=r<=ell`, because

`a_(m+1)/a_m=(1+1/m)^m>1` for `m>=1`.                           (4.12)

Combining (4.8)-(4.12),

`2^(k+3ell-2p) a_r (product alpha_j)^(-1)
 <=2^(k+3ell-p) a_r
 <=2^(k+3ell) a_ell`,                                           (4.13)

which is exactly (4.2) after taking the `1/(2d)` power.

Both terminal receivers give an integrable characteristic-function bound `min(1,K|t|^(-d/2))`, because `d>2`. Hence `phi_Q in L^1` and the density has a continuous representative vanishing at infinity. QED.

### Important scope

This theorem removes the **canonical row-marginal gate once a grouped hub / projected-compound packet has already been produced**. It does not prove that the bare three-large-eigenvalue hypothesis always yields target-scale `S^2 Z_ell`. The global routing problem remains open.

## 5. One-hub / second-compound corollary

Take one physical original-coordinate hub (`k=1`) and a projected second-compound packet (`ell=2`). Then `d=3`, `M_H<=1`, and (4.2) becomes

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3) (S^2 Z_2)^(-1/6)
 =7.559526299369239... (S^2 Z_2)^(-1/6).}`                       (5.1)

There is **no** row-marginal condition.

A sharper branchwise statement follows from the proof. If the canonical pair law has maximum marginal `alpha_*<=1/2`, then (5.1) follows directly from the exact entropy identity. If some row `h` has `alpha_h>1/2`, one promotion gives

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6) alpha_h^(-1/6)
   (S^2 Z_2)^(-1/6)
 <6 (S^2 Z_2)^(-1/6).}`                                        (5.2)

Thus the dangerous near-coloop regime is actually **easier** after physical promotion; the former fractional `q->2` blow-up is not structural.

In star-volume language, if `B` is the physical cross block with distinguished hub row `b_0`, then

`S^2 Z_2
 =sum_(i<j, i,j!=0)
   det(B_[{0,i,j}] B_[{0,i,j}]^T)`.                             (5.3)

Hence (5.1) is a direct bound in terms of the entire third-volume **star** through one physical hub, without selecting one tiny local minor.

## 6. Explicit fully dense rotated indefinite target

Let

`r=(1,1,1,1)/2`,
`u=(1,1,-1,-1)/2`,
`v=(1,-1,1,-1)/2`.                                               (6.1)

These are mutually orthonormal and every physical coordinate of each vector is nonzero. Define the `5 x 4` cross block

`B = [ r ; 2u ; u ; v ; v ]`,                                   (6.2)

and the fully dense symmetric matrix

`A_* = [[J_5/100, B],
        [B^T,     J_4/100]].`                                    (6.3)

Every entry of `A_*` is nonzero. Moreover

`B^T B = r r^T +5 u u^T+2 v v^T`,                               (6.4)

so the nonzero singular values of `B` are exactly

`sqrt(5), sqrt(2), 1`.                                           (6.5)

The zero-self-block matrix has nonzero spectrum

`{+sqrt(5),-sqrt(5),+sqrt(2),-sqrt(2),+1,-1}`.                  (6.6)

The same-bank perturbation in (6.3) has operator norm

`max(||J_5/100||op,||J_4/100||op)=1/20`.                        (6.7)

By Weyl, four eigenvalues of `A_*` have modulus at least

`sqrt(2)-1/20>1`.                                                (6.8)

Thus (6.3) is genuinely rotated, indefinite, fully dense in the physical product coordinates, and satisfies the owner's exact spectral hypothesis.

Use the first left original coordinate, whose cross row is `r`, as the hub. Then `S=1`, and after projecting off `r` the residual rows are

`2u, u, v, v`.                                                    (6.9)

Only `u-v` row pairs have nonzero area. Therefore

`Z_2=(4+1)(1+1)=10`.                                             (6.10)

The canonical pair marginal of the heavy row `2u` is

`alpha_h= [4(1+1)]/10 =4/5`.                                    (6.11)

Promote this actual physical row. The two-hub crossing singular product is

`S_+=2`,                                                         (6.12)

and after projecting the remaining rows off `u`, only the two `v` rows survive, so

`Z_1^+=||v||^2+||v||^2=2`.                                      (6.13)

The exact promotion identity is visible numerically:

`S_+^2 Z_1^+ =4*2=8=(4/5)*10=alpha_h S^2 Z_2`.                  (6.14)

The terminal `k=2,ell=1,d=3` receiver therefore gives, for **every** admissible independent cap-one product law,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=3*2^(5/6)*8^(-1/6)
 =3*2^(1/3)
 =3.779763149684619... .}`                                      (6.15)

The characteristic function is in `L^1`; hence this displayed target has a continuous `C_0` density. No histogram or asymptotic approximation enters (6.10)-(6.15).

For comparison, the generic no-marginal corollary (5.1) gives

`3*2^(4/3)*10^(-1/6)=5.150245313595342...`;                     (6.16)

the explicit heavy-row promotion uses the actual `alpha_h=4/5` and is substantially sharper.

## 7. Designated account02/B04 result applied to the same matrix

Condition only the third left original coordinate in (6.2), the row `u`. The retained four-row cross block is

`B_4=[r;2u;v;v]`.                                                (7.1)

Its positive three-row volumes are exactly the two triples

`{r,2u,v_1}` and `{r,2u,v_2}`,                                   (7.2)

each with squared volume `4`. Hence

`E_3(B_4)=8`.                                                     (7.3)

Rows `r` and `2u` are coloops of the supported rank-three row matroid, so the designated account02/B04 theorem `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1` applies in its sharper exact-rank-three/coloop branch. Uniformly in the conditioned coordinate it gives

`boxed:
 ||p_Q||_infinity <=6*8^(-1/6)=3*sqrt(2)
 =4.242640687119286... .}`                                      (7.4)

Averaging over the conditioned original coordinate preserves this bound for the same ambient matrix `A_*`. Equation (6.15) therefore improves this completed designated-partner certificate on the same target-valid matrix by the exact factor

`(3 sqrt(2))/(3*2^(1/3))=2^(1/6)=1.122462048309373...`.         (7.5)

I also checked the newest account02/B04 heavy-row family `M_L=D_L(I-(2/5)11^T)`. Its completed one-hub certificate is

`||p_Q||infinity <=3*2^(5/6)L^(-1/3)`.                           (7.6)

At `L=4096` this is

`0.3340870193026273...`.                                        (7.7)

The generic new no-marginal theorem (5.1), using `S=L`, `Z_2=6`, gives on that exact family

`0.3504957244440252...`;                                        (7.8)

so the partner's exact optimized residual-pair currency is about `4.91%` sharper there. This is a genuine equation-level use of the current partner result, not a status citation.

## 8. What this changes and what remains open

The previous B04 gap `QFORM-FRACTIONAL-PROJECTED-CROSSING-NEARCOLOOP-SPLICE-v1` is **closed for canonical compound-volume laws**: every heavy canonical row can be promoted to a physical hub with exact currency recursion (3.12), and repeated promotion terminates without a near-coloop singularity.

The first remaining implication is now

`QFORM-TARGETSCALE-GROUPED-COMPOUND-EXTRACTION-v1`:

> Starting only from the bare hypothesis that `A` has at least three eigenvalues of modulus at least one, force an original-coordinate grouped packet with `d=k+ell>2` and universal-scale currency `M_H^(-2/d) S^2 Z_ell` (or route its failure into one of the already-paid finite-core rank-one/rank-two, two-source strong-mode, minority-sign pivot, ridge, square-hyperbolic or exact-rank branches), without deleting nonzero tails or assuming post-rotation independence.

The new theorem means that **row-volume marginal imbalance is no longer part of that extraction problem**. What remains is the scale of the aggregate grouped currency itself.

Full unrestricted QFORM: **OPEN / not proved / not disproved**. Full-target continuity: **OPEN**. Continuity is proved on every branch of Theorem 4.2 and on the explicit matrix above. Two independent end-to-end reviews are not requested because no full candidate proof exists yet.
