# account02/B20 QFORM r14 — half-barrier nested-resource amplification

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** `20260922T172846Z-account02-B20-QFORM-r14`  
**Assignment:** proof closure and keeper / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_REDUCTION_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source scope

The target is the following unrestricted statement. For every finite `n`, every independent real random vector `X=(X_1,...,X_n)` whose one-dimensional densities satisfy `0<=f_i<=1`, and every real symmetric matrix `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample. No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, or post-rotation independence assumption is added. Continuity is tracked separately.

Fresh brain control at the beginning of this run was `yspennstate/math-research-brain@21e06f5d694bec5935bf2b6601792a52fca7cae8`; a later freshness read before this report saw `b5c391bc423b118ed74e7e1b37a11222f153cce1`. The active OWNER CONTROL is revision `2026-09-22.8`, with QFORM as the sole target.

The newest completed designated partner result actually consumed is account03/B20 run `20260922T165009Z-account03-B20-QFORM-r13`, canonical mathematics

`yspennstate/math-open-problems@06ef7346c08f41c3fac240e1acdeb1b42dc2995d`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T165009Z-account03-B20-QFORM-r13/REPORT.md`.

Its theorem `QFORM-NESTED-CUT-THREE-RESOURCE-v1` turns a lower bound on `s_2(A-diag A)` into an original-coordinate two-direction cross bank, or a rank-one outer bank plus either a physical pivot or a nested cross bank. I use its exact random-cut/Eckart--Young mechanism below with the newest stronger threshold rather than merely quoting its older constants.

The second current input is account03/B19 run `20260922T170047Z-account03-B19-QFORM-r15`, canonical mathematics `yspennstate/math-open-problems@539d1d9953c616bf0e1ab2dafeef55102f89c2b9`. It proves, under the full owner quantifiers,

` s_2(A-diag A) <= 499/1000  =>  ||p_Q||_infinity < 84. `

Thus every still-unpaid matrix satisfies the strict complementary inequality

` s_2(A-diag A) > 499/1000. `                                      (1.1)

The current orientation-free rank-two affine half-Riesz theorem at `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a` remains available for later analytic payment, but this report does not extend it to arbitrary higher-rank remainders.

Corrections retained throughout: no law-uniform pointwise quadratic-phase decay; no dimension-free naive fiber supremum; no independence after spectral rotation; no generic conditional-density cap surrogate; no one-good-minor inference; no bare bounded-3D-density/coarea implication for indefinite traces; and no same-square absorption of arbitrary same-bank curvature.

## 2. Strongest conditional end-to-end argument

Let `H=A-diag(A)`.

1. If `s_2(H)<=499/1000`, account03/B19 already gives `||p_Q||_infinity<84`.
2. Therefore every unresolved target candidate obeys (1.1).
3. The theorem in Section 3 below applies the designated account03/B20 mechanism at this stronger threshold and forces one of three **quantitatively macroscopic, source-realizable original-coordinate packets** with constants much larger than the previous `3/160`-scale packet.
4. On any such packet, the designated partner's high-window conditioning/whitening expression remains applicable. If `P=1_{|A|>=1/64}=UU^T`, then for a conditioned physical bank `G`,

   `S_G=I-U_G^T U_G`,

   and, whenever `S_G>=I/2`, every unconditioned row satisfies

   `u_i^T S_G^{-1}u_i <= 2 P_ii`.                              (2.1)

   Consequently, if all residual `P_ii<=1/64`, the whitened leverage is at most `1/32`, and the already-paid partner/B20 diffuse branch closes with a continuous density `<194`. Hence any packet that remains unpaid must obey the partner's corresponding localization alternatives on both sides.
5. The first unpaid universal implication is therefore no longer extraction of a resource. It is the analytic payment of the strong packets in Section 5 while retaining arbitrary self blocks and all original-coordinate dependence provenance.

A proof of that final packet-payment implication, together with the already-paid `s_2(H)<=499/1000` branch, would close the full target. This report proves the resource implication but not the final payment.

## 3. Parameterized theorem: amplify the partner's nested cut at any off-diagonal threshold

### Theorem `QFORM-HALF-BARRIER-NESTED-RESOURCE-v1`

Let `A` be real symmetric with `s_3(A)>=1`, let `H=A-diag(A)`, and suppose

` s_2(H) > tau `

for some `0<tau<1`. Put

` beta=tau/4`, `alpha=(1-beta)/2`, `gamma=(1-beta)/4`.

Then there is a partition of the original physical coordinates into `L disjoint_union R`, with `C=A[L,R]`, for which at least one of the following holds:

**(T2) two-direction cross bank**

` s_2(C) >= beta. `                                             (3.1)

**(P1) outer bank plus physical pivot**

` s_1(C) > beta `                                               (3.2)

and one side `S in {L,R}` contains an original coordinate `i` such that

` |A_ii| >= alpha. `                                           (3.3)

**(N1) outer bank plus nested bank**

` s_1(C) > beta `                                               (3.4)

and one side `S in {L,R}` has a physical partition `S=S_1 disjoint_union S_2` such that

` s_1(A[S_1,S_2]) > gamma. `                                   (3.5)

All banks are sets of original coordinates. No transformed random coordinates are introduced.

### Proof

Take independent Rademacher signs `epsilon_i` and `D=diag(epsilon)`. Define

`M=(H-DHD)/2`.

If `L={i:epsilon_i=1}` and `R={i:epsilon_i=-1}`, then, after merely reordering physical coordinates,

` M = [[0,C],[C^T,0]],  C=H[L,R]=A[L,R]. `

The nonzero singular values of `M` are those of `C`, each repeated twice. Hence

` ||M||_(4) = 2(s_1(C)+s_2(C)), `                              (3.6)

where `||.||_(4)` is the Ky--Fan four norm. Also `E M=H/2`. Convexity of the Ky--Fan norm yields

`E ||M||_(4) >= ||H/2||_(4)
                = (1/2) sum_{j=1}^4 s_j(H).`

Therefore some physical cut satisfies

` s_1(C)+s_2(C) >= (1/4) sum_{j=1}^4 s_j(H)
                  >= (s_1(H)+s_2(H))/4
                  > tau/2. `                                  (3.7)

If `s_2(C)>=tau/4=beta`, (T2) holds. Assume not. Then (3.7) gives

` s_1(C) > tau/2-tau/4 = beta. `                              (3.8)

Let `sigma=s_1(C)`, choose a top singular pair `u,v`, and write

` C=sigma u v^T+E,  ||E||=s_2(C)<beta. `

Insert the symmetric rank-two matrix carried by this singular pair,

`K=[[0,sigma u v^T],[sigma v u^T,0]].`

Since `rank K<=2` and `s_3(A)>=1`, the spectral-norm Eckart--Young inequality gives

` ||A-K||_op >= 1. `                                           (3.9)

Let `B=diag(A_LL,A_RR)`. Then

`(A-K)-B=[[0,E],[E^T,0]]`,

so `||(A-K)-B||_op=||E||<beta`. Combining this with (3.9),

` max(||A_LL||_op,||A_RR||_op)=||B||_op > 1-beta. `            (3.10)

Choose a side `S` with `||A_SS||_op>1-beta`. If some physical diagonal entry in that side has magnitude at least

`(1-beta)/2=alpha`,

then (3.8) gives (P1).

Otherwise every diagonal entry of `A_SS` has magnitude `<alpha`. Put

`J=A_SS-diag(A_SS)`.

Then

` ||J||_op >= ||A_SS||_op-||diag(A_SS)||_op
             > (1-beta)-alpha
             = (1-beta)/2. `                                  (3.11)

Apply an independent Rademacher cut **inside the same original-coordinate side `S`**. For `D_eta=diag(eta)` on `S`, set

`N=(J-D_eta J D_eta)/2`.

For the induced partition `S=S_1 disjoint_union S_2`, `N` is the symmetric cross-only matrix whose operator norm is `s_1(A[S_1,S_2])`, and `E N=J/2`. Convexity of the operator norm gives a cut with

` s_1(A[S_1,S_2]) = ||N||_op >= ||J||_op/2
                    > (1-beta)/4=gamma. `                     (3.12)

Together with (3.8), this is (N1). QED.

### Why `beta=tau/4` is the natural balanced choice

The partner proof in fact permits any split threshold `delta in (0,tau/2)`: either `s_2(C)>=delta`, or `s_1(C)>tau/2-delta`, while the pivot/nested lower bounds become `(1-delta)/2` and `(1-delta)/4`. The weakest of the two outer cross-direction guarantees is maximized by balancing

`delta=tau/2-delta`,

namely `delta=tau/4`. Thus the constants above are not an arbitrary rescaling of the older theorem; they are the balanced constants supplied by exactly the same source-valid mechanism at the current sharp off-diagonal barrier.

## 4. Current numerical specialization

By account03/B19, every unresolved target form has `tau=499/1000` available strictly. Therefore set

` beta = 499/4000 = 0.12475,`

` alpha = 3501/8000 = 0.437625,`

` gamma = 3501/16000 = 0.2188125.`

Every unresolved target form consequently has one of:

1. `s_2(A[L,R])>=499/4000`;
2. `s_1(A[L,R])>499/4000` and a physical pivot `|A_ii|>=3501/8000` on one side;
3. `s_1(A[L,R])>499/4000` and a nested physical cross bank with `s_1>3501/16000`.

This is a substantial quantitative amplification of the designated partner's earlier `3/160`, `9/160`, `157/320`, `157/640` resource scales.

## 5. Aggregate source-realizable packet corollaries

These forms can be converted into aggregate currencies without selecting a single tiny minor.

### 5.1 Two-direction alternative: a four-bank determinant packet

For a real matrix `C`, Cauchy--Binet gives

`e_2(CC^T)=sum_{|I|=2,|J|=2} det(C[I,J])^2
          =sum_{p<q}s_p(C)^2 s_q(C)^2.`                        (5.1)

Under (T2), `s_1(C),s_2(C)>=beta`, so

`e_2(CC^T)>=beta^4.`                                           (5.2)

Independently two-color the physical rows `L` and physical columns `R`. Any fixed unordered row pair is separated with probability `1/2`, and independently any fixed column pair is separated with probability `1/2`. Therefore some deterministic partitions

`L=L_1 disjoint_union L_2`, `R=R_1 disjoint_union R_2`

retain at least one quarter of (5.1):

`sum_{i in L_1,j in L_2}
 sum_{a in R_1,b in R_2} det C[{i,j},{a,b}]^2
 >= beta^4/4.`                                                 (5.3)

At `beta=499/4000`, the exact lower bound is

` beta^4/4 = 62001498001 / 1024000000000000
            > 6.05 * 10^(-5). `                               (5.4)

Thus the live two-direction branch carries a fixed original-coordinate four-bank `2x2` determinant packet.

### 5.2 Pivot alternative: macroscopic square plus macroscopic outer bank

Since Frobenius norm dominates operator norm, (P1) gives

` ||A[L,R]||_F^2 > beta^2 = 249001/16000000`                   (5.5)

along with

` |A_ii| >= 3501/8000.`                                       (5.6)

The coordinate `i` is physical, so its source law remains independent of every disjoint physical bank before any conditioning.

### 5.3 Nested alternative: two disjoint-scale cross energies

The outer bank obeys (5.5), while the nested physical partition satisfies

` ||A[S_1,S_2]||_F^2 > gamma^2
   = 12257001/256000000. `                                    (5.7)

If `T` is the opposite side of the outer cut, then `S_1,S_2,T` are three pairwise disjoint original-coordinate banks. This is exactly the product provenance needed by any subsequent grouped-bank analytic argument.

## 6. Exact application of the newest account03/B20 localization expression

The designated partner's completed r13 report attaches a high-window conditioning test to every physical bank. Let

`P=1_{|A|>=1/64}=UU^T`.

For a physical conditioning set `G`, its exact whitening matrix is

`S_G=I-U_G^T U_G`.                                             (6.1)

If `S_G>=I/2`, then for every unconditioned physical row `u_i`,

`ell_i=u_i^T S_G^{-1}u_i <= 2 P_ii.`                           (6.2)

Thus if all residual `P_ii<=1/64`, then `ell_i<=1/32` and the partner's already-paid diffuse splice applies. Therefore any **unpaid** outer cut `L|R` produced above must satisfy both

` ||U_L^T U_L||_op>1/2  OR  max_{i in R}P_ii>1/64,`            (6.3)

` ||U_R^T U_R||_op>1/2  OR  max_{i in L}P_ii>1/64.`            (6.4)

The same test applies to a nested cut. Equations (6.1)--(6.4) are not qualitative citations: they are the exact partner expression used here to constrain the newly amplified packets.

## 7. What this proves and what it does not

**Proved:** combining the current paid half-offdiagonal branch with the designated partner's exact cut mechanism, every unresolved target matrix carries one of the strong packets (5.3), (5.5)--(5.6), or (5.5)+(5.7), with the localization constraints (6.3)--(6.4) whenever the partner diffuse branch has not already closed it.

**Not proved:** that an arbitrary symmetric self-block contamination can always be paid from these currencies. In particular, one must not replace a grouped bank by independent singular-vector coordinates, condition to a fictitious bounded spectral density, or select one reciprocal minor from aggregate mass.

**Continuity:** continuity is inherited only on the already-paid partner diffuse branch; no continuity claim is made for the residual packets.

**Full target:** still OPEN. No counterexample to the exact target is produced here.

## 8. First unpaid universal implication after this run

`QFORM-STRONG-HALF-BARRIER-PACKET-PAYMENT-v1`:

Under the full target hypotheses, assume `s_2(A-diag A)>499/1000` and one of the exact source-realizable alternatives produced in Sections 4--6 holds. Prove a universal density bound by a dependence-safe analytic estimate, or transfer a fixed amount of the packet into an already-paid ridge/grouped-square/rank-two branch, while retaining arbitrary self blocks and all affine terms induced by conditioning.

A particularly concrete subgoal is the pivot packet:

`|A_ii|>=3501/8000`, `||A[L,R]||_F^2>249001/16000000`,

plus (6.3)--(6.4). The scalar-pivot completion gives an exact half-Riesz demand on its Schur remainder, and the current rank-two affine theorem can pay that demand whenever the packet can be converted, without rotating the source, into a rank-two Schur component of fixed determinant. Establishing that conversion in aggregate form is the next analytic bottleneck.

The nested packet gives the alternative route: three disjoint original-coordinate banks with fixed outer and inner cross energies. A valid proof may aggregate each bank before applying curvature, but it may not assume independence of singular-vector projections inside a bank.

## 9. Before/after and next method

**Before:** the newest partner reduction used the much weaker universal premise `s_2(H)>3/20`, leaving outer cross scales around `3/160`--`9/160` and a nested scale `157/640`.

**After:** the newly paid account03/B19 half-barrier makes every survivor satisfy `s_2(H)>499/1000`; the balanced partner mechanism then forces the uniform outer scale `499/4000`, pivot `3501/8000`, nested scale `3501/16000`, or the four-bank determinant mass (5.4). This is target-level reduction movement, not a restatement of prior bookkeeping.

**Next method:** attack the pivot packet by aggregate Schur-compound identities. Expand the total second compound of the scalar Schur complement and seek a lower bound from the outer Frobenius bank plus the third-eigenvalue condition, with an explicit alternative that routes any rank-one cancellation into the nested/grouped-bank packet. This changes the next analytic object from local minor selection to aggregate Schur compound mass and respects all current corrections.
