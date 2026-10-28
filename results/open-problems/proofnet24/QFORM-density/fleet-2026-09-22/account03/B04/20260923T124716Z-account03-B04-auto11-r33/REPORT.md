SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T12:47:16Z.
attacking: two-hub dilution by a finite mixture of lower compound determinant laws in original product coordinates.

# account03/B04 r33 — multi-compound product-Fourier mixture and an exact two-heavy-coordinate rescue

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport only  
**Full QFORM:** OPEN  
**Continuity:** proved on the new theorem branch because the resulting characteristic function is in `L^1`; not proved for the full target.

## 1. Dependencies actually applied and corrections respected

Two completed supporting arguments are used at equations.

1. The sharp fractional three-volume product-Fourier argument at
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
   I use its one-sided original-coordinate Weyl differencing and its sharp Hausdorff--Young estimate, especially the scalar factor

   `|| |psi_i(2t .)|^q ||_(1/alpha_i)
       <= (pi/|t|)^alpha_i
          (alpha_i/q)^(alpha_i/2)
          (1-alpha_i/q)^(-(q-alpha_i)/2)`.

2. account03/B02's completed `QFORM-WEIGHTED-MIXED32-FOURIER-L1-v1` at
   `yspennstate/math-open-problems@ff8ec2ee90d4846f39e728e1ca20d50c717cc894:proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T085705Z-account03-B02-qform-r25/REPORT.md`.
   Its weighted AM--GM interpolation between a 3-minor family and a 2-minor family is generalized below to finitely many fractionally allocated compound families. The two-family disjoint specialization of the theorem below reproduces B02's exact constant.

The designated partner is `account04/B04`. Fresh direct lookups of both the shared current-QFORM handoff directory and the canonical math archive returned no completed current-QFORM result for that slot. I therefore do not invent partner consumption; account03/B02 is the completed peer result actually applied.

Consumed corrections: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; rotation does not preserve independence; bounded projection density alone does not control an indefinite quadratic pushforward; naive spectral-fiber suprema can lose dimension; and a single heavy physical edge does not absorb arbitrary same-bank curvature. None of those false interfaces is used here.

## 2. New theorem — `QFORM-MULTI-COMPOUND-FOURIER-MIXTURE-v1`

Let `I,J` be disjoint sets of ORIGINAL independent coordinates and let

`B=A[I,J]`.

All same-bank quadratic terms, outside variables/couplings, affine terms, and additional spectrum are arbitrary. For finitely many labels `l`, choose a compound order `k_l` and a nonnegative allocation `c_l(S,T)` supported on physical `k_l x k_l` minors. Require the pointwise no-double-counting condition

`sum_l c_l(S,T) <= 1`                                           (2.1)

for every square-minor term `(S,T)` in the determinant expansion, with absent orders interpreted as allocation zero. Define the allocated determinant currencies

`Z_l = sum_{|S|=|T|=k_l} c_l(S,T) det(B[S,T])^2 > 0`.           (2.2)

Normalize

`w_l(S,T)=c_l(S,T)det(B[S,T])^2/Z_l`.

Let

`alpha_i^(l)=P_l(i in S)`,  `beta_j^(l)=P_l(j in T)`.

Choose weights `theta_l>0`, `sum_l theta_l=1`, and put

`alpha_i=sum_l theta_l alpha_i^(l)`,
`beta_j =sum_l theta_l beta_j^(l)`,
`s       =sum_l theta_l k_l`.                                   (2.3)

Then `sum_i alpha_i=sum_j beta_j=s`.

### Theorem

If

`1 <= q < s/2`                                                   (2.4)

and every mixed row marginal obeys

`alpha_i <= q/2`,                                                (2.5)

then the full ambient quadratic-plus-affine form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= [e s/((s-2q)sqrt(q))]
    [prod_l theta_l^(theta_l)]^(1/(2s))
    prod_l Z_l^[-theta_l/(2s)].`                                (2.6)

The same conclusion holds when (2.5) is instead satisfied by every mixed column marginal, after transposing `B`.

### 2.1 Determinant interpolation across finitely many compound orders

Put positive Gaussian parameters `d_i` on row maps and `e_j` on coordinate maps. The exact diagonal-plus-PSD expansion is

`det(D_J+B^T D_I B)
 = sum_{S,T: |S|=|T|} det(B[S,T])^2
     prod_{i in S} d_i prod_{j notin T} e_j`.                   (2.7)

For each allocated family set

`A_l=sum_{S,T} c_l(S,T)det(B[S,T])^2
               prod_{i in S}d_i prod_{j notin T}e_j`.

Condition (2.1) and positivity of every determinant-expansion term imply the crucial inequality

`det(D_J+B^T D_I B) >= sum_l A_l`.                              (2.8)

There is therefore no hidden double counting when different same-order families overlap.

Weighted AM--GM under `w_l` gives

`A_l
 >= Z_l prod_i d_i^(alpha_i^(l))
        prod_j e_j^(1-beta_j^(l)).`                             (2.9)

Weighted AM--GM once more gives

`sum_l A_l
 >= C_theta prod_l A_l^(theta_l)`,
`C_theta=prod_l theta_l^(-theta_l)`.                            (2.10)

Combining (2.8)-(2.10),

`det(D_J+B^T D_I B)
 >= C_theta [prod_l Z_l^(theta_l)]
    prod_i d_i^(alpha_i)
    prod_j e_j^(1-beta_j).`                                    (2.11)

Lieb's Gaussian characterization of the Brascamp--Lieb constant therefore yields

`BL
 <= C_theta^(-1/2)
    prod_l Z_l^(-theta_l/2)
    prod_i alpha_i^(-alpha_i/2)
    prod_j (1-beta_j)^(-(1-beta_j)/2).`                         (2.12)

Endpoint exponents are interpreted by the same continuous omission convention as in the cited three-volume proof.

### 2.2 Original-coordinate Fourier estimate

Condition all outside ORIGINAL coordinates. One-sided Weyl differencing in bank `J`, exactly as in the cited volume theorem, gives

`|phi_Q(t)|^2 <= E_D prod_i |psi_i(2t(BD)_i)|`,                 (2.13)

where `D=X_J-X'_J` has independent coordinate densities of mass one and cap at most one. There is no spectral rotation of the random variables and no assertion that a sum/difference pair is independent.

Let `F_t(D)=prod_i |psi_i(2t(BD)_i)|`. Jensen gives

`E F_t <= (E F_t^q)^(1/q)`.

Under (2.5), `q/alpha_i>=2`. Apply the sharp Hausdorff--Young inequality exactly as in the cited peer proofs. Inserting the resulting one-dimensional norms in (2.12), the powers of `alpha_i` cancel. The inequalities

`-(1-x)log(1-x)<=x`

and `sum alpha=sum beta=s` give the two entropy factors `<=e^(s/2)` each. Hence

`boxed:
 E F_t^q
 <= C_theta^(-1/2)e^s q^(-s/2)
    (pi/|t|)^s
    prod_l Z_l^(-theta_l/2).`                                  (2.14)

From (2.13)-(2.14),

`|phi_Q(t)| <= min(1,K |t|^-b)`,
`b=s/(2q)>1`.                                                   (2.15)

The exact scalar integral

`integral_R min(1,K|t|^-b) dt = 2b K^(1/b)/(b-1)`              (2.16)

and Fourier inversion yield (2.6). In particular `phi_Q in L^1`, so the density is continuous and vanishes at infinity.

### 2.3 Consistency checks

For a single `k=3` family with allocation one, `s=3` and (2.6) reduces to

`3e/[(3-2q)sqrt(q)] Z_3^(-1/6)`,

which is exactly the cited fractional three-volume theorem.

For two disjoint allocated families of orders `3` and `2` with weights `theta,1-theta`, `s=2+theta`; (2.6) reduces exactly to account03/B02's weighted mixed-`3+2` constant. Thus the new formula is a finite-family extension of already completed product-Fourier machinery, not a change of analytic interface.

## 3. A two-heavy-coordinate target where pure `E3` and every one-hub `3+2` gate fail

Define a `6 x 3` matrix `U` by the rows

`u0=(2/sqrt(5),0,0)`,
`u1=(0,2/sqrt(5),0)`,

`u2=( 1/(2sqrt(5)),  1/(2sqrt(5)),  1/2)`,
`u3=( 1/(2sqrt(5)), -1/(2sqrt(5)),  1/2)`,
`u4=( 1/(2sqrt(5)),  1/(2sqrt(5)), -1/2)`,
`u5=( 1/(2sqrt(5)), -1/(2sqrt(5)), -1/2)`.

Direct exact arithmetic gives

`U^T U=I_3`.                                                     (3.1)

Set `P=UU^T`. Explicitly,

```
P =
[4/5,  0,    1/5,   1/5,   1/5,   1/5]
[0,    4/5,  1/5,  -1/5,   1/5,  -1/5]
[1/5,  1/5,  7/20,  1/4,  -3/20, -1/4]
[1/5, -1/5,  1/4,   7/20, -1/4,  -3/20]
[1/5,  1/5, -3/20, -1/4,   7/20,  1/4]
[1/5, -1/5, -1/4,  -3/20,  1/4,   7/20].
```

Thus `P^2=P` and `rank(P)=3`. On twelve original independent coordinates define

`A_*=[[0,P],[P,0]]`.                                            (3.2)

Then

`spec(A_*)={+1,+1,+1,-1,-1,-1,0,0,0,0,0,0}`.                  (3.3)

This is a genuinely rotated indefinite target with six eigenvalues of modulus one.

### 3.1 Pure third-volume obstruction

Since `P` is a rank-three projection,

`E3(P)=1`,                                                       (3.4)

and the canonical third-minor inclusion marginals are exactly the diagonal leverages of `P`. Hence

`alpha_0=alpha_1=4/5`.                                          (3.5)

Every pure-third-volume Fourier choice has `q<3/2`, so `q/2<3/4<4/5`; the pure gate is impossible.

### 3.2 Every one-heavy-coordinate mixed `3+2` rescue still fails

Delete physical coordinate `0`. The residual frame Gram is

`diag(1/5,1,1)`,

so the residual squared singular values of `P_{-0,-0}` are

`1/25,1,1`,

and therefore

`E2(P_{-0,-0})=27/25`.                                         (3.6)

Under its canonical squared `2 x 2` minor law, the other heavy coordinate `1` has exact inclusion marginal

`104/135 > 3/4`.                                                (3.7)

The incident third-minor family anchored at `0` gives coordinate `1` marginal `4/5`. Therefore **every** convex mixture of those two one-hub families leaves coordinate `1` with marginal at least `104/135>3/4`. But every admissible weighted `3+2` theorem has average order `<3`, hence `q<s/2<3/2` and so `q/2<3/4`. Thus no one-hub `3+2` mixture can pay this second hub. The same argument holds with `0` and `1` interchanged.

This is an exact obstruction to the preceding run's one-heavy mechanism, not merely a worse numerical constant.

## 4. Three-family lower-compound dilution pays both hubs

Use three **fractionally allocated** determinant families. The half allocations in the two second-order families are essential because those deletion families overlap on minors avoiding both hubs; the no-double-counting condition (2.1) is then exact.

### 4.1 Double-hub third-minor family

Let `F3` consist of all `3 x 3` minors whose row and column triples contain both heavy coordinates `0,1`, with allocation coefficient one. Exact Cauchy--Binet factorization through `P=UU^T` gives

`Z3=256/625`,                                                   (4.1)

with row and column inclusion marginals

`alpha^(3)=beta^(3)=(1,1,1/4,1/4,1/4,1/4)`.                   (4.2)

### 4.2 Two half-allocated residual second-minor families

For `F2^0`, take every `2 x 2` determinant term after deleting row and column `0`, but allocate coefficient `1/2` to each such term. The raw residual volume is

`E2(P_{-0,-0})=27/25`,

so the allocated currency is

`Z2^0=27/50`.                                                   (4.3)

Uniform half allocation leaves the normalized inclusion marginals unchanged:

`alpha^(2,0)=beta^(2,0)
 =(0,104/135,83/270,83/270,83/270,83/270)`.                    (4.4)

The spectral calculation behind (4.4) is short. The inclusion weights of the three normalized singular directions are

`2/27,26/27,26/27`.

Coordinate `1` lies entirely in one high direction with squared coordinate `4/5`, giving `(26/27)(4/5)=104/135`. Each lower coordinate has squared coordinates

`(1/4,1/20,1/4)`

in the normalized low/high/high singular directions, giving

`(2/27)(1/4)+(26/27)(1/20+1/4)=83/270`.                        (4.5)

Define `F2^1` symmetrically after deleting coordinate `1`, again with coefficient `1/2` per eligible determinant term. Then

`Z2^1=27/50`,                                                   (4.6)

and the first two marginals in (4.4) are swapped.

A second-order minor avoiding both hubs is eligible for both residual families and therefore receives total allocation `1/2+1/2=1`; a minor eligible for only one receives total allocation `1/2`. Thus the pointwise determinant-term allocation never exceeds one, as required in (2.1).

### 4.3 Exact balancing weights

Choose

`theta3=31/166`,
`theta20=theta21=135/332`.                                     (4.7)

They sum to one, and the average compound order is

`s=3 theta3+2 theta20+2 theta21=363/166`.                       (4.8)

The mixed marginals are exactly

`alpha=beta=(1/2,1/2,197/664,197/664,197/664,197/664)`.         (4.9)

Thus the theorem applies at `q=1`, with integrability gap

`s-2=31/166>0`.                                                 (4.10)

Substitution in (2.6) gives

`||p_{X^T A_* X}||_infinity
 <= (363e/31)
    [(31/166)^(31/166)(135/332)^(135/166)]^(83/363)
    (256/625)^(-31/726)
    (27/50)^(-45/242)`
` = 29.198835629278766...`.                                    (4.11)

Therefore, for every twelve independent real inputs with probability densities bounded by one,

`boxed: ||p_{X^T A_* X}||_infinity < 29.199`.                  (4.12)

The density is continuous and vanishes at infinity.

## 5. Interpretation

The useful point is not the numerical constant. This matrix has **two** physical third-volume hubs of leverage `4/5`. Pure third-volume Fourier inversion fails, and deleting either hub leaves the other with residual second-volume marginal `104/135>3/4`, so every one-anchor `3+2` mixture fails as well. A symmetric mixture of one double-hub third-minor packet and two half-allocated lower-order deletion packets simultaneously reduces both hub exponents to exactly `1/2`, while preserving a positive aggregate determinant currency.

This is the first B04 calculation in this sequence that explicitly pays a genuine two-heavy-coordinate obstruction by lower compound orders rather than selecting a small physical minor or switching to a diagonal/local special case.

## 6. What remains open

The theorem in Section 2 is fully general for any supplied finite collection of **fractionally allocated** determinant families, but the bare spectral assumption `s_3(A)>=1` does not yet produce, in every matrix, a collection whose mixed marginals pass the Fourier gate while the weighted geometric determinant currency stays bounded below on a universal scale.

The next structural obligation is therefore sharper:

`QFORM-FINITE-HUB-COMPOUND-COMPILER-v1` — given the finite compound-hub residues already forced by the third/fourth-volume entropy arguments, construct allocated deletion/incident families of orders `3,2,1` (or route their failure to an already-paid physical-pair/star/ridge endpoint) so that all mixed product exponents lie below the Hausdorff--Young threshold while the weighted determinant currency remains dimension-free.

The present two-hub example proves that such a compiler can require more than one lower-compound deletion family. It does not prove the exhaustive compiler or the full QFORM conjecture. Full-target continuity also remains open.

## 7. Deterministic checks, checkpoint correction and provenance

All final matrix identities, spectra, minor currencies, inclusion marginals, balancing weights, allocation constraints, and the final constant were checked by exact rational/symbolic arithmetic and saved in `CHECKS.json`; no Monte Carlo evidence is used.

The early `CHECKPOINT.md` was intentionally written before the exact arithmetic pass. Its first trial currencies and weights were provisional and are superseded by the corrected `CHECKS.json` and this final report. The checkpoint is preserved rather than rewritten so the failed preliminary calculation remains visible.

