SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-23T21:48:57Z.
attacking: the fresh finite-core pairwise-weak branch; retune the physical-pair Schur compiler to a much smaller universal scale and use the new determinant-only physical-triple receiver to force every unpaid H-side self block into a quantitative rank-at-most-two carrier.

# account03/B20 r39 — pairwise-weak finite-core closure to a rank-two self carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: proof closure and keeper / SYNTHESIS  
Status: **NEW TARGET-LEVEL STRUCTURAL CLOSURE + EXPLICIT PAYMENTS / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Continuity: full-target continuity remains OPEN. The new payments below inherit only essential boundedness from the invoked physical-pair / physical-triple receivers.

## 1. Fresh source boundary

Fresh brain control at login resolved to `yspennstate/math-research-brain@21c31d31d8f7a2084e5f8a4cfa2f2616e564b2c9`; owner control remains revision `2026-09-22.15`, QFORM-only.

The immediate assembly input is account03/B19 r42:

`yspennstate/math-open-problems@dfe442ee899867f5677e5ced85a196eca922fe64`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T210457Z-account03-B19-QFORM-r42/REPORT.md`.

Its live finite-core state has ORIGINAL-coordinate banks `H,L`,

`|H|<=124`,                                                     (1.1)

and a physical cross collar

`C=A[H,L]`,
`C=C_2+R_C`,
`rank(C_2)<=2`,
`||R_C||_op<1/64`.                                               (1.2)

Its strong-pair compiler already shows that a quantitatively invertible physical pair either pays the full law or drives `A[H,H]` close to rank two. The remaining collective branch was that every physical principal pair is weak at the chosen threshold.

The second fresh input is account03/B06 r45, `QFORM-PHYSICAL-TRIPLE-DETERMINANT-RECEIVER-v1`:

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T211904Z-account03-B06-qform-r45/REPORT.md`.

For three literal independent original coordinates with invertible symmetric coefficient matrix `M`, arbitrary affine leakage and all outside coordinates conditioned, it proves

`||p_Q||_infinity < 102 |det M|^(-1/3)`.                        (1.3)

No post-rotation independence, moment/support assumption, arbitrary-joint coarea, pointwise quadratic-phase decay, fiber-supremum step, or deletion of a small random quadratic tail is used below.

## 2. Retuned strong-pair branch

Set

`kappa=2^(-20)`,
`eta=2^(-40)`,
`delta=eta^2=2^(-80)`.                                          (2.1)

Suppose a literal physical pair `T subset H` has

`sigma_min(A[T,T])>=kappa`.                                      (2.2)

If it is definite, conditioning every other original coordinate and using the two-dimensional definite-pair receiver gives

`||p_Q||_infinity <= pi/kappa = pi 2^20 < 3.295e6`.             (2.3)

If it is indefinite, put `B=A[T,T]`, `D=|det B|`. Then

`D>=kappa^2`, hence `D kappa>=kappa^3=2^(-60)`.                 (2.4)

Apply r42 Theorem 3.1 to the exact physical Schur complement. If some remaining core coordinate has Schur diagonal at least `eta`,

`||p_Q||_infinity
 <=8 2^(1/4) (D kappa eta)^(-1/4)
 <=8 2^(1/4) 2^25
 <3.193e8`.                                                       (2.5)

If some remaining physical core pair has Schur determinant at least `delta`,

`||p_Q||_infinity
 <=64 (D kappa)^(-1/4) delta^(-1/8)
 <=64 2^15 2^10
 =2^31
 =2147483648`.                                                    (2.6)

If neither gate fires, every diagonal entry of the core Schur block `S_H` has modulus `<eta`, and every off-diagonal entry obeys

`|(S_H)_{ij}|^2
 <=|(S_H)_{ii}(S_H)_{jj}|+|det S_H[{i,j}]|
 <2 eta^2`,                                                       (2.7)

so, because `|H\T|<=122`,

`||S_H||_op
 <[1+121 sqrt(2)] eta
 =1.5654208351e-10`.                                              (2.8)

The exact pair completion therefore writes

`A[H,H]=L_H+E_H`,
`rank(L_H)<=2`,
`||E_H||_op<1.566e-10`.                                          (2.9)

Thus every state containing a `kappa`-strong physical pair either has an explicit universal density payment or is already an extremely tight rank-two self carrier.

## 3. New theorem: the pairwise-weak branch is rank-one after a physical-triple gate

### Theorem 3.1 — `QFORM-FINITECORE-PAIRWISEWEAK-TO-RANK1-v1`

Let `B=B^T` be an `m x m` real symmetric matrix with `m<=124`. Assume

`sigma_min(B[{i,j},{i,j}])<kappa=2^(-20)`                        (3.1)

for every physical pair `i!=j`.

Put

`tau=kappa^3=2^(-60)`.                                           (3.2)

Then one of the following holds:

1. some literal physical principal triple `S={r,i,j}` satisfies

   `|det B[S,S]|>=tau`;                                          (3.3)

2. there is a symmetric matrix `L` of rank at most one such that

   `||B-L||_op
    <(3+122 sqrt(10)) kappa
    =0.0003707865472226546`.                                    (3.4)

Moreover, in case (3.3), if `B=A[H,H]` is a physical principal block of the ambient QFORM matrix, the full law has an essentially bounded density

`||p_Q||_infinity
 <102 tau^(-1/3)
 =102 kappa^(-1)
 =106954752`.                                                     (3.5)

#### Proof

Let

`R=max_i |B_ii|`                                                 (3.6)

and choose `r` with `|B_rr|=R`.

### Case 1: `R<kappa`

For any pair `i!=j`, write `b=B_ij`. The off-diagonal matrix

`[[0,b],[b,0]]`

has both singular values `|b|`, while the diagonal perturbation has operator norm at most `R`. Weyl's singular-value perturbation inequality gives

`sigma_min(B[{i,j}]) >= |b|-R`.                                  (3.7)

By (3.1), `|b|<R+kappa<2kappa`. Thus every row sum is less than

`kappa+2(m-1)kappa <=(2m-1)kappa`,                              (3.8)

so

`||B||_op<(2m-1)kappa<=247 kappa
 =0.00023555755615234375`.                                      (3.9)

Take `L=0`; this is stronger than (3.4).

### Case 2: `R>=kappa`

Write the pivoted matrix as

`B=[[a,b^T],[b,G]]`,
`|a|=R`,                                                         (3.10)

and let

`S=G-bb^T/a`                                                     (3.11)

be the exact scalar Schur complement.

Fix an index `i!=r`. By (3.7) applied with the maximal diagonal bound `R`, (3.1) implies

`|B_ri|<R+kappa`.                                                 (3.12)

Therefore the operator norm of the physical pair `{r,i}` is bounded by its maximum row sum:

`||B[{r,i}]||_op <R+(R+kappa)=2R+kappa`.                         (3.13)

Since the product of the two singular values is the determinant magnitude,

`|a B_ii-B_ri^2|
 <kappa(2R+kappa)`.                                              (3.14)

Dividing by `|a|=R>=kappa` gives the uniform scalar-Schur diagonal estimate

`|S_ii|<2kappa+kappa^2/R<=3kappa`.                               (3.15)

Now take distinct `i,j!=r`. The exact principal Schur identity is

`det B[{r,i,j},{r,i,j}]=a det S[{i,j},{i,j}]`.                   (3.16)

If (3.3) fails for every such triple, then, using `|a|=R>=kappa`,

`|det S[{i,j}]|<tau/R<=kappa^2`.                                (3.17)

Hence

`|S_ij|^2
 =|S_ii S_jj-det S[{i,j}]|
 <=|S_ii S_jj|+|det S[{i,j}]|
 <9kappa^2+kappa^2
 =10kappa^2`.                                                     (3.18)

Thus `|S_ij|<sqrt(10)kappa`, and the maximum absolute row sum gives

`||S||_op
 <3kappa+(m-2)sqrt(10)kappa
 <=(3+122sqrt(10))kappa`.                                       (3.19)

Finally define the exact pivot-completion matrix

`L=(1/a) vv^T`,
`v=(a,b^T)^T`.                                                    (3.20)

Then `rank(L)<=1` and

`B-L=diag(0,S)`,                                                  (3.21)

so (3.19) proves (3.4).

If the triple gate (3.3) fires, the three coordinates are literal independent source coordinates after conditioning all others. Apply the determinant-only physical-triple theorem (1.3), giving (3.5). QED.

## 4. Combined finite-core consequence

Apply Sections 2-3 with `B=A[H,H]`. There is an explicit full-law payment bounded by

`C_core=2^31`                                                     (4.1)

on every branch where a strong pair or a determinant-large triple fires. Otherwise there is a symmetric rank-at-most-two matrix `L_H` such that

`boxed:
 ||A[H,H]-L_H||_op
 <epsilon_H:=0.0003707865472226546.}`                            (4.2)

Combining with the live physical cross collar (1.2), define

`K=[[L_H,C_2],[C_2^T,0]]`.                                      (4.3)

Since `rank(L_H)<=2` and the symmetric off-diagonal block generated by a rank-two `C_2` has rank at most four,

`rank(K)<=6`.                                                     (4.4)

Writing

`A=diag(0_H,A[L,L])+K+E`,                                       (4.5)

one has

`||E||_op
 <=||A[H,H]-L_H||_op
   +||[[0,R_C],[R_C^T,0]]||_op
 <epsilon_H+1/64
 =0.015995786547222654`.                                        (4.6)

This closes the pairwise-weak collective branch left open in r42: **every unpaid finite-core state now has all H-side self curvature and H-L crossing compressed into one rank-at-most-six deterministic carrier, modulo an explicit operator error below 0.016.** The error is NOT discarded from the random quadratic polynomial.

Because the original target has `s_3(A)>=1`, Weyl also gives the deterministic spectral certificate

`s_3(diag(0_H,A[L,L])+K)
 >1-0.01599578655
 >0.9840042`.                                                     (4.7)

This does not by itself pay the law, but it identifies the next exact analytic interface: a rank-six carrier over an arbitrary product-coordinate base, with a retained nonzero coefficient error below `0.016` and three near-unit singular directions.

## 5. Designated partner account04/B20 applied at an actual inequality

The completed designated partner report is

`yspennstate/math-open-problems@9d07c5d5c69c885509db66cb1093acdeff8bcb64`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T181642Z-account04-B20-QFORM-r11/REPORT.md`.

Its exact three-color theorem states that for a normalized exact-rank-three direction with maximum atom `eta_h<1/3`, three disjoint original-coordinate banks can be chosen with

`W_1W_2W_3 >=(1-3 eta_h)/27`.                                   (5.1)

On the live diffuse-normal inequality `eta_h<1/64`, this gives

`boxed: W_1W_2W_3>61/1728.}`                                    (5.2)

The corresponding three bank projections are genuinely independent and have joint density cap

`e^(3/2) sqrt(27/(1-3 eta_h))
 <e^(3/2)sqrt(1728/61)
 =23.8533112123...<23.854`.                                      (5.3)

This is recorded only at its proved scope. It is not substituted for a curved quadratic pushforward and is not used to erase the rank-six error in (4.6).

## 6. First remaining implication

The first remaining finite-core closure edge is now

`QFORM-FINITECORE-RANK6-CARRIER-WITH-RETAINED-ERROR-PAYMENT-v1`:

> Starting from (4.5)-(4.7), pay a symmetric rank-at-most-six carrier over the arbitrary `L`-bank base while retaining the coefficient error `||E||_op<0.015996`, arbitrary same-bank curvature on `L`, all outside couplings, signs, affine terms, fragmented/unbounded cap-one laws and arbitrary additional spectrum; or route it source-preservingly to an already-paid physical pair, triple, grouped-crossing, ridge, or exact-rank-three receiver.

The small deterministic operator error cannot be dropped as a small random error because the input laws have no moments. A valid next step must spend it algebraically or absorb it inside a receiver that keeps the original product coordinates.

## 7. Status

- Full unrestricted QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- New theorem: `QFORM-FINITECORE-PAIRWISEWEAK-TO-RANK1-v1`.
- New combined compiler: every unpaid finite-core state is reduced to a rank-at-most-six carrier with retained coefficient error `<0.015996`.
- Largest explicit new/retuned payment constant used in this compiler: `2^31`.
- Full-target continuity: **OPEN**. No new continuity claim is made for the physical-pair/triple payment branches used here.
- Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
