SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-22T23:52:09Z.
attacking: newest no-pivot N3 synthesis: force an original-coordinate cross-energy certificate, then split it into a paid diffuse three-volume branch or three sharply quantified low-rank/anchored survivors.

# account03/B19 QFORM r21 — a physical no-pivot cross-volume compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed at start: revision `2026-09-22.15`  
Assignment: `Universal proof assembly`  
Classification: **ESSENTIAL_STEP_APPLIED / TARGET-LEVEL N3 REDUCTION / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN** (`full_brain_connected=false`)

## 1. Exact target and current source boundary

The target is unchanged. For arbitrary independent real coordinates `X_i` with probability densities `0<=f_i<=1` and an arbitrary real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove one universal finite bound on the essential supremum of the density of `Q=X^TAX`, or give a valid counterexample. No Gaussian, moment, compact-support, log-concavity, connected-support, diagonal-basis, or post-rotation independence hypothesis is introduced.

The newest owner-requested Claude synthesis is the package

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/`.

Its relevant global reduction is `N3(tau,C0)`: it is enough to prove the target under one fixed no-pivot threshold `tau>0`, namely

`|A_ii|<tau`,
`|A_ii A_jj-A_ij^2|<tau` for every `i!=j`,

while retaining `s_3(A)>=1`. Once this class has a universal bound, the full conjecture follows by the proved pivot reduction/Gaussian-padding argument. The source still marks `N3` OPEN.

I attack `N3` directly below with the fixed value

`tau = 2^(-20)`.

This is legitimate because the source reduction needs only one fixed positive threshold. Choosing it very small is useful: a no-pivot survivor must then carry its three-eigenvalue spectral mass through many tiny original-coordinate coefficients.

Live corrections are retained throughout. In particular, there is no pointwise quadratic-phase decay claim, no arbitrary-joint rank-three coarea step, no use of a worst conditional fiber density, no selection of spectral coordinates as independent random variables, and no deletion of a small matrix coefficient on the ground that the inputs are bounded (they are not).

## 2. Inputs from completed workers

### 2.1 Weighted three-volume D' theorem

From account03/B12 r20, `QFORM-LOCAL-FOOTPRINT-HYBRID-STABILITY-v1` and its proved weighted D' lemma:

for a physical cross block `M=A[I,J]`, let `w_(S,T)` be any probability law on nonzero physical `3x3` minors, with row marginal

`alpha_i=P_w(i in S)`.

If `max_i alpha_i<=h<3/4`, then, with

`Z_w(M)=exp(H(w)+E_w log |det M[S,T]|^2)`,

the full ambient quadratic form, including arbitrary self blocks, outside couplings and affine terms, has a continuous density satisfying

`||p_Q||_infinity <= C(h) Z_w(M)^(-1/6)`

with

`C(2/3)=9 sqrt(3e)`.

The proof works in original-coordinate product geometry and does not rotate independence.

### 2.2 E3 tail identity

The algebra used independently in account01/B20 auto11 is

`3 E_3(M) >= E_2(M) dist_F(M,{rank<=2})^2`,

where `E_k(M)=e_k(MM^T)`. I reprove it below so the present implication does not depend on an unreviewed numerical threshold from that report.

### 2.3 Designated partner account04/B19

The designated partner's completed `QFORM-FINITE-UNION-CORE-v1` says that, for every measurable output map, the interval concentration supremum over all independent cap-one densities equals its supremum over product indicators of bounded finite unions of intervals of total length one. Thus any interval inequality proved on that core transfers to the entire admissible class with no loss in its constant.

I apply it below to the actual diffuse-three-volume inequality

`P{Q in I} <= 576 sqrt(3e) |I|`.

The weighted D' proof already works for arbitrary product laws, so this partner application is logically redundant but mathematically genuine: it independently verifies that no compact-support or finite-union restriction changes the target constant on this branch.

## 3. No-pivot immediately gives tiny physical entries

Fix `tau=2^(-20)` and suppose `A` is in `N3(tau)`.

For `i!=j`,

`A_ij^2`
` <= |A_ii A_jj-A_ij^2|+|A_ii A_jj|`
` < tau+tau^2`
` < 10^(-6)`.

Hence

`boxed: |A_ij|<10^(-3) for every i!=j.`                         (3.1)

This uses the actual original-coordinate entries; it is not a statement in an eigenbasis.

## 4. A physical random cut carries constant Frobenius energy

Write

`D=diag(A)`, `H=A-D`.

Since `||D||_op<tau` and `s_3(A)>=1`, Weyl's singular-value inequality gives

`s_3(H) >= 1-tau`.

Therefore

`||H||_F^2 >= 3(1-tau)^2`.                                      (4.1)

Choose a uniformly random bipartition `[n]=L disjoint_union R`, and let

`B=A[L,R]=H[L,R]`.

Each unordered off-diagonal pair crosses the cut with probability `1/2`, while `||H||_F^2` counts each unordered pair twice. Thus

`E ||B||_F^2 = ||H||_F^2/4`.

Consequently there exists a deterministic **physical** bipartition for which

`W:=||B||_F^2`
` >= 3(1-tau)^2/4`
` = 3(1-2^(-20))^2/4`
` > 2/3`.                                                        (4.2)

No law of `X` has been used. This is a matrix consequence of the target spectral hypothesis plus the no-pivot diagonal bound.

From now on fix such a cut.

Let

`lambda_1>=lambda_2>=...>=0`

be the squared singular values of `B`; then

`W=sum_r lambda_r`.

Put

`E_2=sum_(p<q) lambda_p lambda_q`,
`E_3=sum_(p<q<r) lambda_p lambda_q lambda_r`.

I use the thresholds

`delta_2=2^(-20)`,
`delta_3=2^(-36)`.

## 5. First branch: small E2 forces a very tight rank-one tube

Assume

`E_2<=2^(-20)`.                                                  (5.1)

### Lemma 5.1

The best rank-one approximation `B_1=sigma_1 u v^T` satisfies

`boxed: ||B-B_1||_F < 1/590,}`                                  (5.2)

`boxed: sigma_1>4/5,}`                                          (5.3)

and at least one of its two unit singular vectors is diffuse in the explicit sense

`boxed: min{||u||_infinity^2,||v||_infinity^2}<1/296.}`         (5.4)

#### Proof

If `lambda_1<W/2`, then

`sum_r lambda_r^2 <= lambda_1 W < W^2/2`,

so

`E_2=(W^2-sum lambda_r^2)/2 > W^2/4 >1/9`,

contradicting (5.1). Hence `lambda_1>=W/2`.

Set

`T_1=sum_(r>=2)lambda_r=W-lambda_1`.

Because `E_2>=lambda_1 T_1`,

`T_1<=2E_2/W <3*2^(-20)`.

Therefore

`||B-B_1||_F=sqrt(T_1)`
` <sqrt(3)*2^(-10)`
` <1/590`,

which proves (5.2). Also

`sigma_1^2=lambda_1=W-T_1`
` >2/3-3*2^(-20)>16/25`,

which proves (5.3).

By (3.1), every physical entry of `B` is smaller than `1/1000`, while every entry of `B-B_1` is bounded by its Frobenius norm. Hence

`sigma_1 |u_i v_j|`
` <= |B_ij|+|(B-B_1)_ij|`
` <1/1000+1/590`.

Using `sigma_1>4/5`,

`|u_i v_j|`
` < (5/4)(1/1000+1/590)`
` <1/296`

for every `i,j`. Taking maxima gives

`||u||_infinity ||v||_infinity<1/296`,

so one factor has square smaller than `1/296`. QED.

### Lemma 5.2 — the third spectral direction is forced into a same-side block

Write

`S=diag(A[L,L],A[R,R])`,

and put the symmetric rank-two cross skeleton

`K=[[0,B_1],[B_1^T,0]]`.

Then

`boxed: max{||A[L,L]||_op,||A[R,R]||_op}>589/590.}`             (5.5)

#### Proof

Let

`R_1=[[0,B-B_1],[(B-B_1)^T,0]]`.

Then `A=S+K+R_1`, `rank K<=2`, and

`||R_1||_op=||B-B_1||_op<=||B-B_1||_F<1/590`.

Since subtracting a rank-two matrix cannot eliminate the third singular value,

`||A-K||_op>=s_3(A)>=1`.

But `A-K=S+R_1`, hence

`||S||_op>=1-||R_1||_op>589/590`.

Because `S` is block diagonal, (5.5) follows. QED.

Thus the low-`E_2` no-pivot survivor is not an amorphous dense matrix. It is a `1/590` physical Frobenius tube around a rank-one cross bank, one of whose two aggregate singular directions has coordinate leverage below `1/296`, while one actual same-side block still has operator norm above `589/590`.

This is a new concrete target for the hub/grouped-square compilers.

## 6. Second branch: positive E2 but tiny E3 forces a rank-two tube

Assume now

`E_2>2^(-20)`                                                     (6.1)

and

`E_3<2^(-36)`.                                                    (6.2)

Set

`T_2=sum_(r>=3)lambda_r=dist_F(B,{rank<=2})^2`.

For every pair `p<q`, removing `lambda_p,lambda_q` leaves at least the tail obtained by removing the two largest terms, so

`sum_(r notin {p,q}) lambda_r >= T_2`.

Therefore

`3E_3`
` =sum_(p<q) lambda_p lambda_q sum_(r notin {p,q})lambda_r`
` >=T_2 E_2`.

Using (6.1)-(6.2),

`T_2<3*2^(-16)`.

Hence

`boxed: dist_F(B,{rank<=2})<sqrt(3)*2^(-8)<1/147.}`             (6.3)

This is again a physical-coordinate statement. It does not delete the `1/147` tail from the quadratic form; that would be illegal under unrestricted supports. It identifies the exact stability interface that a valid grouped/ridge theorem has to absorb.

## 7. Third branch: substantial E3 is either paid or becomes a high-cardinality anchored packet

Assume

`E_3>=2^(-36)`.                                                   (7.1)

Cauchy--Binet gives

`E_3=sum_(|S|=|T|=3) det(B[S,T])^2`.

Define the genuine physical squared-minor probability law

`w_(S,T)=det(B[S,T])^2/E_3`.

Let

`alpha_i=P_w(i in S)`,
`beta_j=P_w(j in T)`.

### 7.1 Diffuse orientation: a complete density payment

If

`max_i alpha_i<=2/3`,

apply the weighted D' theorem with `h=2/3`. For the canonical squared-minor weights,

`H(w)+E_w log |det B[S,T]|^2 = log E_3`,

so

`Z_w(B)=E_3`.

Thus

`||p_Q||_infinity`
` <=9 sqrt(3e) E_3^(-1/6)`
` <=9 sqrt(3e) 2^6`
` =576 sqrt(3e)`
` <1645`.                                                        (7.2)

The same conclusion holds if instead `max_j beta_j<=2/3`, by transposing the cross block.

This branch has a **continuous** density because the D' characteristic-function envelope is integrable uniformly over the outside original-coordinate conditioning.

Actual designated-partner application: on the bounded finite-union product core the same argument gives

`P{Q in I}<=576 sqrt(3e)|I|`                                    (7.3)

for every interval `I`. `account04/B19`'s `QFORM-FINITE-UNION-CORE-v1` transfers (7.3), with the **same constant**, to every independent cap-one product law. Thus compact support is not being added silently in (7.2).

### 7.2 Concentrated row and column orientations

The only unclosed `E_3` case is therefore

`max_i alpha_i>2/3`

and

`max_j beta_j>2/3`.

Choose physical anchors `i_* in L`, `j_* in R` attaining these failures. Then, under the same minor law,

`P(i_* in S and j_* in T)`
` >=alpha_(i_*)+beta_(j_*)-1`
` >1/3`.

Consequently the total squared determinant mass of physical `3x3` minors containing both anchors is

`>E_3/3`.

Independently two-colour every non-anchor row and every non-anchor column. For each anchored triple, its two non-anchor rows split across the two row colours with probability `1/2`, and its two non-anchor columns split across the two column colours with probability `1/2`. Hence some deterministic four-bank colouring retains anchored mass

`boxed: P_anchor > E_3/12 >= 2^(-36)/12.}`                       (7.4)

This reproduces the useful nested-anchor mechanism directly at the new no-pivot source boundary.

### 7.3 No-pivot makes the anchored packet genuinely high-cardinality

Because `L` and `R` are disjoint, every entry of every `3x3` minor of `B` is an off-diagonal entry of `A`. By (3.1), each has magnitude `<1/1000`.

Hadamard therefore gives, for every such minor,

`|det B[S,T]|^2`
` < ((sqrt(3)/1000)^3)^2`
` =27*10^(-18)`.                                                 (7.5)

Combining (7.4)-(7.5), an anchored packet cannot be carried by one or a few anomalous minors. The number `N_anchor` of nonzero physical minors in the retained packet satisfies

`N_anchor`
` > [2^(-36)/12]/[27*10^(-18)]`
` = 10^18/(324*2^36)`
` =44913.3186...`.

Thus

`boxed: N_anchor>=44914.}`                                      (7.6)

This is a genuinely nonlocal original-coordinate obstruction. Any remaining proof in this branch has at least 44,914 distinct anchored physical three-minor witnesses available; it is not permitted to collapse them to a single inverse determinant and pay a catastrophic reciprocal atom.

## 8. Conditional end-to-end proof assembly

The newest Claude reduction says that proving `N3(tau,C0)` for any fixed `tau>0` proves the full QFORM conjecture. Taking `tau=2^(-20)`, Sections 3--7 show that every `N3` matrix has a physical cut satisfying exactly one of the following source-valid alternatives.

### P0 — paid diffuse three-volume branch

`E_3>=2^(-36)` and one orientation has volume marginal at most `2/3`.

Then

`boxed: ||p_Q||_infinity<1645,}`

and `p_Q` has a continuous representative.

### R1 — rank-one cross tube plus almost-unit same-side curvature

`E_2<=2^(-20)`, with

`dist_F(B,rank<=1)<1/590`,
`σ_1(B)>4/5`,
`min(||u||_infinity^2,||v||_infinity^2)<1/296`,

and

`max(||A[L,L]||_op,||A[R,R]||_op)>589/590`.

### R2 — rank-two cross tube with genuine two-volume

`E_2>2^(-20)`, `E_3<2^(-36)`, and

`dist_F(B,rank<=2)<1/147`.

The lower bound on `E_2` is retained and must not be discarded in the next step.

### R3 — high-cardinality anchored three-volume packet

`E_3>=2^(-36)`, both volume orientations are concentrated, and there are physical anchors plus a four-bank colouring carrying squared-minor mass at least

`2^(-36)/12`

across at least

`44914`

distinct nonzero anchored `3x3` minors.

All three unpaid states also retain the original no-pivot inequalities and the entry bound `|A_ij|<10^(-3)`.

Therefore the global `N3` debt is reduced to paying **R1, R2, and R3**. This is materially narrower than the prior statement “prove N3”: R1 is an almost rank-one hub/grouped-square geometry, R2 is an almost rank-two cross geometry with fixed `E_2`, and R3 is an explicitly nonlocal anchored-volume geometry with a huge number of witnesses. No spectral rotation of the input law occurred in obtaining any of them.

## 9. First unpaid implication after this run

`QFORM-N3-LOWRANK-OR-ANCHORED-PAYMENT-v1`:

prove a dimension-free density estimate in each of the three states R1--R3, preferably by mechanisms already completed elsewhere:

- R1: combine the one-side `1/296` diffuse rank-one bank and the `>589/590` same-side operator curvature with the grouped-square / third-square hyperbolic absorption machinery, while retaining arbitrary two-sided self blocks;
- R2: use the fixed `E_2>2^(-20)` before inversion, via the new `k=2` weighted-Riesz theorem or a stable grouped rank-two compiler; do not delete the `1/147` tail pointwise;
- R3: spend the full `>=44914` anchored-minor packet through weighted Brascamp--Lieb or an anchor recursion; do not select a single minor.

The full theorem is not yet proved because none of these three remaining implications is currently available at the required arbitrary-self-block scope.

## 10. Continuity and status

- Paid P0 branch: continuous density, bound `<1645`.
- R1/R2/R3: no density conclusion is claimed here; they are structural reductions.
- Full target: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuous representative: **OPEN**.

## 11. Arithmetic checks

The accompanying checker verifies the exact threshold inequalities, the `1/590`, `1/296`, `1/147`, `<1645`, and `44914` constants. These checks support arithmetic only; the proof is the analytic argument above.
