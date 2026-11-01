SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-24T10:37:41Z.
attacking: a two-sided star-aware balanced cut in the diffuse carrier survivor, forcing bilateral rank-two carrier alignment or paying the full form through literal third-compound crossings; then convert both carrier footprints into original-bank crossing energy using fleet02/B08 r36.

# fleet01/B08 r49 — two-sided star-aware cut and bilateral rank-two carrier forcing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING END-TO-END BRANCH + BILATERAL PRODUCT-SAFE CARRIER REDUCTION / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains **OPEN**. Full-target continuity remains **OPEN**. This report keeps the random variables in the original independent coordinates, assumes no moments, compact support, connected support, Gaussianity, log-concavity or iid structure, and does not discard complementary spectrum as a small random perturbation.

## 1. Fresh scope and source pins


The immediate own inputs are:

- r47, `yspennstate/math-open-problems@dad5d50a92be318854c9c0ae4409242e84a7753d`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260924T090807Z-fleet01-B08-qform-r47/REPORT.md`;
- r48, `yspennstate/math-open-problems@6aeabdd6343abdea18945673eafbb3ed9fa42fe5`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260924T094957Z-fleet01-B08-qform-r48/REPORT.md`.

The completed designated-partner inputs actually used are:

- fleet02/B08 r35, `yspennstate/math-open-problems@087cf5aa5cfcee4eb6ae243facb9e0fcf2391e29`, which supplies the row-aware selected-three deletion crossing scale and the marginal-free physical third-compound receiver;
- fleet02/B08 r36, `yspennstate/math-open-problems@e54144ba53a8a8039f1d704faf4342d859afb20f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/fleet02-B08-20260924T094502Z-r36/REPORT.md`, which converts a carrier footprint on three disjoint original-coordinate banks into three literal target-scale crossing-energy directions. Its exact arithmetic checks are at `@26422be5c2a10a666dfc7480c9e37a203718c146`.

## 2. Inherited diffuse edge-capped chamber

We work inside the still-unpaid edge-capped diffuse state reached in r47/r48. There is a genuine selected eigentriple

`A_3=U Lambda U^T`, `U^T U=I_3`, `min_j |lambda_j|>=L`,          (2.1)

with

`max_i ||U_i||_2^2 <= 1/48`.                                     (2.2)

There is an ORIGINAL physical coordinate `k` whose row star

`b=A[k,-k]`, `B=||b||_2`                                         (2.3)

obeys

`B > rho L`, `rho=0.0006247538095703261`,                        (2.4)

and, after the already-paid scalar and fixed-edge branches,

`||b||_infinity < rho L/16 < B/16`.                              (2.5)

For a physical cut `S union T=[n]` with `k in S`, write

`D=A[S\{k},T]`,
`z=A[k,T]`,
`y=A[S\{k},k]`.                                                   (2.6)

The fleet02/B08 r35 selected-three deletion calculation applies whenever both selected-frame restricted Grams are at least `3I_3/10`. It supplies the scale

`c0=sqrt(67/800)=0.28939592256975566...`,
`sigma=c0/2=0.14469796128487783... .`                             (2.7)

When `s_2(D)<sigma L`, the complementary spectral crossing has two singular directions above `sigma L`; r48 converts that to two extra genuine eigenvalues of `A`, hence five eigenvalues at scale `sigma L`, and therefore an inductive dimension-drop exit. The primitive branch is `s_2(D)>=sigma L`.

## 3. New theorem: one cut keeps BOTH star halves and the three-frame balanced

### Theorem 3.1 — `QFORM-EDGE-CAPPED-TWOSIDED-STAR-AWARE-THREEFRAME-CUT-v1`

Let `U in R^(n x 3)` satisfy `U^T U=I_3` and

`max_i ||U_i||_2^2 <=1/48`.                                      (3.1)

Fix an original coordinate `k`. Let `b=(b_i)_(i!=k)` satisfy

`B=||b||_2>0`, `||b||_infinity<B/16`.                            (3.2)

Then there is an ORIGINAL-coordinate partition `S union T=[n]`, `k in S`, such that

`boxed: U_S^T U_S >=3I_3/10,   U_T^T U_T>=3I_3/10,`              (3.3)

and simultaneously

`boxed: ||b_T||_2^2 >=(2/5)B^2,`
`boxed: ||b_(S\{k})||_2^2 >=(2/5)B^2.`                            (3.4)

#### Proof

For every `i!=k`, choose independently `xi_i in {0,1}` with mean `1/2`, put `T={i!=k:xi_i=1}`, and force `k in S`. Write `u_i=U_i^T` and

`G_T=sum_(i!=k) xi_i u_i u_i^T`.                                 (3.5)

Then

`E G_T=(I-u_k u_k^T)/2`,                                         (3.6)

whose least eigenvalue is at least `47/96` by (3.1). Put

`delta=47/96-3/10=91/480`.                                       (3.7)

If `||G_T-EG_T||_op<=delta`, then `G_T>=3I/10`. Also

`G_T <= I/2+(91/480)I <7I/10`,                                  (3.8)

so `G_S=I-G_T>=3I/10`.

By independence and centering,

`E||G_T-EG_T||_F^2
 =(1/4) sum_(i!=k)||u_i||_2^4
 <=(1/4)(1/48) sum_i||u_i||_2^2
 =1/64.`                                                         (3.9)

Hence

`P(frame bad) <= (1/64)(480/91)^2=3600/8281.`                    (3.10)

For the star let

`Z=sum_(i!=k) xi_i b_i^2`.                                       (3.11)

Then `EZ=B^2/2`, and by (3.2)

`Var Z=(1/4)sum_i b_i^4 <B^4/1024.`                              (3.12)

Both star halves satisfy (3.4) whenever

`|Z-B^2/2|<=B^2/10`.                                              (3.13)

Chebyshev gives

`P(star bad) < (B^4/1024)/(B^4/100)=25/256.`                     (3.14)

Finally

`3600/8281+25/256
 =1128625/2119936
 =0.5323863550... <1.`                                            (3.15)

Thus a cut satisfying both (3.3) and (3.4) exists. QED.

The improvement over r47 is structural: the same physical cut now preserves a macroscopic part of the star on **both** sides, which lets us test both the right and the left singular carrier of the same literal child crossing `D`.

## 4. Actual QFORM application: nonalignment on either side pays the full form

Apply Theorem 3.1 to the actual star (2.3). By (2.4), the selected cut satisfies

`||z||_2, ||y||_2 >=sqrt(2/5)B >sqrt(2/5) rho L`.                (4.1)

Both selected-frame Grams satisfy the r35 gate, so the partner deletion calculation applies to this exact cut.

### Branch A: `s_2(D)<sigma L`

The fleet02/B08 r35 inequality gives two complementary crossing singular directions at scale `sigma L`. By r48's deterministic spectral-complement theorem, `A` then has at least five genuine eigenvalues of modulus at least `sigma L`. Under dimension induction, the existing hereditary five-large-eigenvalue reduction gives

`||p_Q||_infinity <= C/(sigma L)
 =sqrt(3200/67) C/L
 <6.911 C/L.`                                                     (4.2)

This is an inductive essential-bound exit; continuity is not newly asserted on this branch.

### Branch B: `s_2(D)>=sigma L`

Let `V=V_2(D)` and `W=U_2(D)` be top-two right and left singular subspaces. The right augmented crossing is the literal physical block

`M_R=A[S,T]=[ z^T ; D ]`.                                        (4.3)

The exterior identity from the completed partner source yields

`e_3(M_R M_R^T)
 >=s_1(D)^2 s_2(D)^2 dist(z,V)^2.`                               (4.4)

There is an exactly symmetric left augmented literal crossing

`M_L=A[S\{k},{k} union T]=[ y , D ]`.                             (4.5)

Applying the same identity to `M_L^T=[y^T;D^T]` gives

`e_3(M_L M_L^T)
 >=s_1(D)^2 s_2(D)^2 dist(y,W)^2.`                               (4.6)

Therefore if either

`dist(z,V)>=||z||/2`                                              (4.7)

or

`dist(y,W)>=||y||/2`,                                             (4.8)

then, using (4.1) and `s_1(D)>=s_2(D)>=sigma L`, the corresponding literal crossing satisfies

`e_3(M M^T)^(1/6) >= kappa_bi L`,                                (4.9)

where

`kappa_bi
 =[sigma^2 (sqrt(2/5) rho/2)]^(1/3)
 =0.016052570248452247... .`                                     (4.10)

The completed fleet02/B08 marginal-free third-compound receiver therefore pays the **entire ambient form**, retaining all same-side curvature and all outside couplings:

`boxed: ||p_Q||_infinity
 <=6^(4/3)/(kappa_bi L)
 <679.189/L,`
`boxed: p_Q in C_0(R).`                                          (4.11)

Consequently every still-unpaid primitive Branch-B state must satisfy the new **bilateral relative alignment tube**

`boxed: dist(z,V_2(D))<||z||/2,`
`boxed: dist(y,U_2(D))<||y||/2.`                                  (4.12)

This is a genuine strengthening: the same rank-two child crossing must simultaneously absorb the physical star arriving from its row side and the physical star arriving from its column side.

## 5. Bilateral carrier footprints on disjoint original-coordinate banks

We now turn (4.12) into product-safe physical-bank structure.

Consider either side, with star vector `q` equal to `z` or `y`, norm `Q=||q||`. Equation (3.4) and the global edge cap imply

`max_i q_i^2/Q^2
 < (B^2/256)/[(2/5)B^2]
 =5/512.`                                                        (5.1)

Partition the physical coordinates on that side greedily into four nonempty banks, cutting at cumulative squared-mass thresholds `jQ^2/4`. Each overshoot is at most one maximal coordinate weight, hence every bank `J_r` satisfies

`||q_(J_r)||_2^2
 >(1/4-5/512)Q^2
 =(123/512)Q^2.`                                                  (5.2)

Thus

`||q_(J_r)||_2>aQ`, `a=sqrt(123/512)=sqrt(246)/32=0.4901370981... .` (5.3)

Let `P` be the orthogonal projection onto the corresponding top-two carrier plane and write

`v=Pq`, `e=(I-P)q`.                                                (5.4)

By (4.12), `||e||<Q/2`. Call a bank bad if

`||v_(J_r)||<=Q/8`.                                               (5.5)

On a bad bank,

`||e_(J_r)||
 >=||q_(J_r)||-||v_(J_r)||
 >(a-1/8)Q.`                                                      (5.6)

If two banks were bad, disjoint support would give

`||e||^2
 >2(a-1/8)^2Q^2
 =[(131-4sqrt(246))/256]Q^2
 =0.2666502009...Q^2
 >Q^2/4`,                                                        (5.7)

contradicting `||e||<Q/2`. The strict last inequality is equivalent to

`67>4sqrt(246)`,                                                  (5.8)

and follows after squaring from `4489>3936`.

Hence on **each side** at least three of four pairwise-disjoint original-coordinate banks satisfy

`||v_(J_r)||>Q/8`.                                                (5.9)

Normalize `u=v/||v||`. Since `||v||<=Q`,

`boxed: ||u_(J_r)||>1/8`                                         (5.10)

on at least three disjoint banks.

We have therefore proved:

### Theorem 5.1 — `QFORM-BILATERAL-R2-CARRIER-THREEBANK-FOOTPRINT-v1`

Every still-unpaid Branch-B state has

- a unit `u_R in V_2(D)` visiting at least three disjoint original-coordinate banks `K_1,K_2,K_3 subset T` with `||u_R|_(K_j)||>1/8`;
- a unit `u_L in U_2(D)` visiting at least three disjoint original-coordinate banks `H_1,H_2,H_3 subset S\{k}` with `||u_L|_(H_i)||>1/8`.

All six banks are source-level physical banks. No independence is claimed for the rotated scalar coordinates `u_R^T X` or `u_L^T X`.

## 6. Actual application of the newest designated-partner r36 theorem

Now apply fleet02/B08 r36 Theorem 2.1 to the actual pair `(D,u_R)` from Theorem 5.1. Since

`s_2(D)>=sigma L`                                                 (6.1)

and `u_R in V_2(D)` has three disjoint physical banks of norm `>1/8`, r36 produces unit vectors `w_j^R`, each supported entirely on `K_j`, such that

`boxed: ||D w_j^R||_2 >= (sigma/8)L
       =0.01808724516060973...L,   j=1,2,3.`                      (6.2)

In particular

`boxed: ||D[:,K_j]||_op >=(sigma/8)L,`
`boxed: ||D[:,K_j]||_F >=(sigma/8)L.`                             (6.3)

Apply the same completed partner theorem to `(D^T,u_L)`. Since `s_2(D^T)=s_2(D)` and `u_L in V_2(D^T)`, there are unit vectors `w_i^L`, each supported entirely on the disjoint original-coordinate bank `H_i`, satisfying

`boxed: ||D^T w_i^L||_2 >=(sigma/8)L
       =0.01808724516060973...L,   i=1,2,3,`                      (6.4)

hence

`boxed: ||D[H_i,:]||_op >=(sigma/8)L,`
`boxed: ||D[H_i,:]||_F >=(sigma/8)L.`                             (6.5)

This is an equation-level application of the newest completed designated-partner result. It upgrades a geometric singular-plane footprint to **six literal original-bank crossing-energy certificates**, three source banks on each side of the same rank-two carrier. It does not assert that every pair block `D[H_i,K_j]` is large; that stronger conclusion has not been proved and is not used here.

Because the `H_i` and `K_j` lie in mutually disjoint original-coordinate sets, all six underlying source subvectors are genuinely mutually independent. The carrier directions themselves remain deterministic coefficient vectors, not new independent random coordinates.

## 7. Updated B08 frontier

Inside the edge-capped diffuse chamber the current router is now:

1. `s_2(D)<sigma L`: r48 converts the partner cancellation into a five-large-eigenvalue state and exits by dimension induction with factor `<6.911` relative to the lower-dimensional constant.
2. `s_2(D)>=sigma L`, with either star half relatively nonaligned: the literal third-compound receiver pays the full ambient form continuously by `<679.189/L`.
3. The only primitive survivor is therefore **bilaterally rank-two aligned**. Moreover, both physical sides contain three disjoint original-coordinate banks carrying literal crossing energy at least

   `sigma L/8=0.01808724516060973...L`.

The first unpaid implication is now

`QFORM-SIXBANK-BILATERAL-R2-CARRIER-COMPILER-v1`:

> Consume a literal crossing `D` with `s_2(D)>=sigma L` whose right and left top-two carrier planes each have three disjoint product-source banks carrying the target-scale energies (6.2)-(6.5), while retaining arbitrary same-bank quadratic curvature, arbitrary complementary spectrum and all affine terms. The compiler must be uniform through the punctured third-mode collar exhibited by fleet02/B08 r36; it may not rotate the product law or delete a nonzero residual coefficient tail.

The fleet02/B08 r36 punctured-collar family is an important control: the exact aligned endpoint and a diffuse third-mode estimate separately do not give uniform control as the puncture tends to zero. Thus the next receiver must genuinely use the bilateral bank structure rather than a coefficient-continuity argument.

## 8. Status and integrity

- Full universal bounded density: **OPEN**.
- Full-target continuous density: **OPEN**.
- The new two-sided cut theorem and bilateral footprint theorem are deterministic and unconditional within their stated hypotheses.
- The `<679.189/L` branch is an unconditional full-ambient density payment and gives a continuous `C_0` representative.
- The `s_2(D)<sigma L` branch is an inductive reduction, not a stand-alone unconditional full proof.
- No Monte Carlo or histogram is used as proof; all decimals above are evaluations of exact rational/radical expressions and the inherited fixed constant `rho`.
- No task identity, cadence, enabled/paused state, notification setting, permissions, public visibility, cross-account authentication, paid API/model setting, or installation setting was changed.
- Repository transport is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
