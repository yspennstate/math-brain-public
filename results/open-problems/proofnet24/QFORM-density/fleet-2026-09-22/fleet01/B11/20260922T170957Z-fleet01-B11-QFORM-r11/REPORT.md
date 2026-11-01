# fleet01/B11 — cross-dominated indefinite pair and strong-pair closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T170957Z-fleet01-B11-QFORM-r11`  
Assignment: indefinite signatures  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Conditional end-to-end position

The full target remains the arbitrary-dimensional three-large-eigenvalue conjecture. The current rank-two affine half-Riesz theorem controls an exact-rank-three branch once one has a quantitatively nonzero original-coordinate scalar pivot, while the zero-pair cubic-bank theorem controls a special zero-diagonal pair. The local outer-pivot gap is therefore the genuinely indefinite physical pair with small diagonals and a strong cross term.

This report proves that gap in a robust neighborhood of the zero-pair geometry. In exact rank three, any physical spectral-area pair `G_ij` above a fixed threshold is now controlled: either one diagonal is quantitatively large and the reviewed scalar-pivot theorem applies, or both diagonals are small relative to the cross term and the new theorem below applies. The remaining exact-rank-three obstruction is consequently the many-small-`G_ij` / grouped-bank chamber; arbitrary additional spectrum remains a separate global debt.

The rank-two opposite-sign logarithmic singularity is preserved explicitly. The third direction pays it by a square-trace estimate whose level sets have length `O(sqrt(epsilon))`.

## 2. Source-pinned premises actually applied

1. **Assigned partner fleet02/B11 scalar projection theorem.** The completed partner chain used in fleet02/B11 run `20260922T155024Z-b11-qform-87d73745`, canonical report `yspennstate/math-open-problems@d56d97c85ced819f45ddad0987deaa5eb4b53cdc`, includes the completed fleet02/B11 one-dimensional projection result `20260922T135203Z-b11-qform-6080e0b3`: for independent cap-one coordinates and a unit coefficient vector `d`, the linear projection `L=d.X` has density cap

`||p_L||_infinity <= sqrt(e)`.

This cap is used numerically in Theorem 5.1 below.

2. **Reviewed orientation-free rank-two affine fusion.** `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, with scoped independent review `yspennstate/math-open-problems@3323397511a6c899630825e18d925511e8aee1e9`, proves the exact-rank-three scalar-pivot consequence

`||p_Q||_infinity <= 128 [c_i |A_ii| |det Lambda|]^(-1/4)`

for `A=R Lambda R^T`, `R^T R=I_3`, when `A_ii !=0`, with arbitrary induced original-coordinate affine terms.

3. **Partner control family.** The latest completed assigned partner theorem gives, for `Q=2aX_0X_1+dY^2`, `Y=sum b_kX_k`, `sum b_k^2=1`,

`||p_Q||_infinity < 10.551 |a|^(-2/3)|d|^(-1/3)`.

It will be used as a stress test showing why the remaining many-small-pair chamber must be aggregated rather than paid by one local minor.

## 3. Translation-uniform envelope for a cross-dominated indefinite binary form

Let `U,V` be independent real variables with densities bounded by one. Translations of either density are allowed. Put

`R = p U^2 + 2 a U V + q V^2`,

and assume

`|p| <= |a|/4`, `|q| <= |a|/4`, `a !=0`.

Then

`D := a^2-pq >= (15/16)a^2 >0`.

Define the decreasing envelope

`Phi(u)=4+log(1/u)` for `0<u<=1`,
`Phi(u)=4 u^(-1/2)` for `u>=1`.

### Lemma 3.1
For almost every `s !=0`, uniformly over all translations of the two cap-one densities,

`p_R(s) <= 3 D^(-1/2) Phi(|s|/sqrt(D)).`        (3.1)

### Proof
Split the `(u,v)` plane into

`S_1={|v|<=|u|}`, `S_2={|v|>|u|}`.

On `S_1`, fixing `u`,

`|partial_v R|=2|au+qv| >= (3/2)|a||u|`.

For fixed `u`, the equation `R=s` has at most two roots in `v`. Also, on `S_1`,

`|s| <= (|p|+2|a|+|q|)u^2 <= (5/2)|a|u^2`.

Hence every contributing root has

`|u| >= r := sqrt( 2|s|/(5|a|) )`,

and one-dimensional change of variables gives the `S_1` contribution at most

`(4/(3|a|)) int_{|u|>=r} f(u)/|u| du`.

The same argument on `S_2`, fixing `v`, gives the identical bound with the second density. For any probability density `f<=1`,

`int_{|u|>=r} f(u)/|u| du <= 1+2log(1/r)` if `0<r<1`,
`<=1/r` if `r>=1`.                                           (3.2)

Because `(15/16)a^2<=D<=(17/16)a^2`, if `u_0=|s|/sqrt(D)` then

`r^2 >= (sqrt(15)/10) u_0`.

For `u_0<=1`, (3.2) is at most `4+log(1/u_0)`. For `u_0>=1`, the same estimate (when `r<1`) and `1/r` (when `r>=1`) are both at most `4u_0^(-1/2)`. Summing the two sectors and using

`8/(3|a|) <= (2sqrt(17)/3)D^(-1/2) <3D^(-1/2)`

gives (3.1). QED.

The logarithm in `Phi` is essential: at `p=q=0`, centered uniform inputs give the usual logarithmically divergent density of `2aUV` at zero.

## 4. The square direction integrates the logarithm

### Lemma 4.1 — square-trace estimate
Let `Y` have a probability density bounded by `K`. For every `delta>0`, `kappa!=0`, and `t in R`,

`E Phi(|t-kappa Y^2|/delta) <= 19 K^(2/3) (delta/|kappa|)^(1/3).`   (4.1)

### Proof
Scale `W=KY`, whose density is at most one, and set

`rho=delta K^2/|kappa|`.

It suffices to bound, uniformly in `tau`,

`E Phi(|tau-W^2|/rho) <=19 rho^(1/3)`.

The elementary quadratic-level-set estimate

`Leb{w: |w^2-tau|<=epsilon} <=4 sqrt(epsilon)`                 (4.2)

holds for every real `tau` and `epsilon>0`.

For `0<lambda<=4`, `Phi(u)>lambda` implies `u<(4/lambda)^2`; by (4.2),

`P(Phi(|tau-W^2|/rho)>lambda) <= min(1,16sqrt(rho)/lambda)`.

For `lambda>4`, `Phi(u)>lambda` implies `u<exp(4-lambda)`, so

`P(Phi(|tau-W^2|/rho)>lambda) <= min(1,4e^2 sqrt(rho)e^(-lambda/2))`.

Integrating these layer-cake bounds gives, when `sqrt(rho)<=1/4`,

`E Phi <= sqrt(rho)[24+16log(1/(4sqrt(rho)))] <=19 rho^(1/3)`.

(The last ratio is maximized at `log(1/(4sqrt(rho)))=3/2` and is `<18.4`.) When `sqrt(rho)>=1/4`, the same integrals give

`E Phi <=6+2log(4sqrt(rho)) <=19 rho^(1/3)`.

Rescaling proves (4.1). QED.

This is the precise rank-three gain: the binary saddle contributes a logarithm, while the third square has `O(sqrt(epsilon))` trace-level measure, converting the singularity to the summable one-third power.

## 5. Main theorem: cross-dominated exact-rank-three Schur pair

Let `X=(X_i)` have independent densities bounded by one. Let `A` have exact rank three and representation

`A=R Lambda R^T`, `R^T R=I_3`,

where `Lambda` is invertible of signature `(+,+,-)` or `(+,-,-)`. Choose a physical pair `I={i,j}` and write

`B=A_{I,I}=[[p,a],[a,q]]`.

Assume the cross-dominated inequalities `|p|,|q|<=|a|/4`. Put

`D=a^2-pq>0`,
`G_ij=||r_i cross r_j||^2`,
`P_ij=|det Lambda| G_ij`.

### Theorem 5.1
The quadratic form `Q=X^TAX` has an essentially bounded density and

`||p_Q||_infinity <= 57 e^(1/3) P_ij^(-1/3) <79.55 P_ij^(-1/3).`  (5.1)

### Proof
Partition coordinates into the pair and its complement. Since `B` is invertible and `rank A=3`, its Schur complement has rank one. Completing the square in the two ORIGINAL physical coordinates gives exactly

`Q=(x+h(Z))^T B (x+h(Z)) + kappa L(Z)^2`,                    (5.2)

where `Z` is the collection of remaining independent original coordinates, `h(Z)` is a possibly highly correlated translation, and `L=d.Z` for a unit vector `d`. No independence between `h(Z)` and `L(Z)` is asserted or needed.

Condition on `Z`. Lemma 3.1 is uniform over the translated pair densities, so

`p_Q(t) <= 3D^(-1/2) E Phi(|t-kappa L^2|/sqrt(D)).`

Now apply the completed assigned-partner fleet02/B11 projection inequality

`||p_L||_infinity <= sqrt(e)`

to Lemma 4.1. This gives

`||p_Q||_infinity
 <=57 e^(1/3) D^(-1/2) (sqrt(D)/|kappa|)^(1/3)
 =57 e^(1/3) (D|kappa|)^(-1/3).`                            (5.3)

Finally, exact rank three and Cauchy-Binet give

`D|kappa|
 = sum_{k notin I} |det A_{I union {k}}|
 = |det Lambda| sum_k det(r_i,r_j,r_k)^2
 = |det Lambda| ||r_i cross r_j||^2
 = P_ij`,

because `sum_k r_k r_k^T=I_3`. Substitute into (5.3). QED.

The result is invariant under negating `A`, hence covers both indefinite signatures.

## 6. Strong-pair closure: no local zero/near-zero-pivot exception remains

There is also a useful deterministic compression lemma.

### Lemma 6.1
For any pair of physical rows with `G=G_ij>0`,

`max(|A_ii|,|A_jj|,|A_ij|) >= G/4`.                         (6.1)

### Proof
Let `S=span(r_i,r_j)`. The two singular values of the `2x3` row matrix have squared values `mu_1>=mu_2>0` with

`mu_1 mu_2=G`, `mu_1+mu_2<=2`,

so `mu_2>=G/2`. The compression of `Lambda` to every two-dimensional subspace has operator norm at least one: by Cauchy interlacing, in signature `(2,1)` its largest Ritz value is at least the second positive eigenvalue, and in signature `(1,2)` its smallest Ritz value is at most the second negative eigenvalue in absolute value. Congruence by the row-coordinate matrix therefore yields

`||B||_op >= mu_2 >= G/2`.

A symmetric `2x2` matrix with maximum absolute entry `m` has operator norm at most `2m`, proving (6.1). QED.

### Corollary 6.2
For an exact-rank-three target form and any physical pair with area `G>0`, either

`||p_Q||_infinity <79.55 G^(-1/3)`                         (6.2)

or

`||p_Q||_infinity <=256 G^(-1/2)`.                         (6.3)

Indeed, if both diagonals are at most `|A_ij|/4`, Theorem 5.1 applies and `|det Lambda|>=1`. Otherwise one diagonal has magnitude at least `G/16`: if the largest entry in (6.1) is diagonal this is immediate with `G/4`, while if it is the cross term the failed cross-dominance gives one diagonal `>|A_ij|/4>=G/16`. Its row leverage is at least `G` because `G<=c_i c_j<=c_i`. The independently reviewed scalar-pivot theorem then gives

`128[c_i |A_ii| |det Lambda|]^(-1/4) <=256G^(-1/2)`.

Thus any pair with, for example, `G>=1/4` gives a universal bound `<=512`. The local zero/near-zero diagonal transition is no longer a separate obstruction in exact rank three.

## 7. Assigned-partner stress test and why aggregation is still necessary

Apply the latest completed fleet02/B11 bank family with equal bank coefficients `b_k=1/sqrt(m)`. For each physical saddle-plus-bank-coordinate pair the relevant spectral area is of order `G=1/m`; any one-pair estimate of the form (6.2) grows like

`79.55 m^(1/3)`.

But the partner's completed bank aggregation theorem gives the same full form the uniform estimate

`||p_Q||_infinity <10.551`

in the normalized case. Thus today's theorem pays the entire **strong-pair** chamber but cannot be iterated by simply selecting the best tiny pair. The partner result supplies an actual target-class witness that the remaining proof must aggregate many small pair areas before paying a reciprocal power.

## 8. First essential missing implication

`QFORM-MANY-SMALL-PAIR-GROUPED-COMPILER-v1`:

In an exact-rank-three indefinite Parseval frame, suppose no physical pair has `G_ij` bounded below by a universal constant. Use the identities

`sum_j G_ij = 2 c_i`

and the original product structure to group many small pair areas into one product-preserving bank mechanism, so that either

1. an independent/translation-uniform square bank is exposed and the fleet02/B11 bank theorem or the previous B11 clean-square theorem applies;
2. the frame enters an already certified diffuse/ridge branch; or
3. another grouped physical block carries a dimension-free determinant/regularized-determinant certificate.

The one-local-triple and conditional-cap corrections rule out replacing this grouped step by a selector of one small minor or by post-rotation conditional independence.

Even a complete exact-rank-three closure would still have to be stabilized under arbitrary additional spectral components to prove the owner's full theorem.

## 9. Status and continuity

Outcome: `ESSENTIAL_STEP_APPLIED`. The full conjecture is still OPEN. This report proves essential boundedness in the stated exact-rank-three cross-dominated branch and, together with the reviewed scalar-pivot theorem, closes every exact-rank-three branch containing a quantitatively strong physical pair. It does **not** prove the many-small-pair grouped compiler or the arbitrary-extra-spectrum step.

No separate continuity proof is claimed for Theorem 5.1. The unrestricted continuous-density conclusion remains OPEN.
