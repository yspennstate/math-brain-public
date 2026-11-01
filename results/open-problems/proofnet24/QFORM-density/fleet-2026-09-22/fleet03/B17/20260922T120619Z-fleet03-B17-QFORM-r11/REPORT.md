# fleet03/B17 — diffuse sharp witnesses and the distributed-minor obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Run:** `20260922T120619Z-fleet03-B17-QFORM-r11`  
**Assignment:** sharp constant and witnesses  
**Status:** `TARGET-LEVEL LOWER-BOUND REVIEWED / NEW STRUCTURAL LEMMA / FULL CONJECTURE OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections consumed

The target is the full arbitrary-dimensional statement: independent real coordinates have densities bounded by one, a real symmetric matrix has at least three eigenvalues with modulus at least one, and one seeks one universal finite essential-density bound for `Q=X^T A X`.

I used the live correction state. In particular, law-uniform pointwise quadratic stationary-phase decay is false for arbitrary fragmented bounded densities, rotation to the spectral basis destroys coordinate independence, and a single nonsingular rank-two cross block is not by itself sufficient. I also consumed the new interactive correction `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, whose six-variable witness and block-CLT argument challenge the formerly plausible constant `pi`. That correction was marked pending independent review; Sections 2–3 below independently rederive the lower-bound mechanism before using it.

At the fresh partner read there was no completed `fleet04/B17` QFORM artifact. I therefore did not fabricate one. I applied the compatible completed `fleet04/B18` theorem `QFORM-SCHUR-PIVOT-SMOOTHING-v1`, which is mathematically on the same structural branch and gives a quantitative density bound from one physical principal triple with a minority-sign pivot and definite Schur complement.

## 2. Independent review of the finite witness `2 pi - 7/3`

Let `X_1,...,X_6` be iid `Uniform[-1/2,1/2]`, put

`U=(X_1+X_2)/sqrt(2)`, `V=(X_3+X_4)/sqrt(2)`, `W=(X_5+X_6)/sqrt(2)`,

and

`Q_2=U^2+V^2-W^2`.

The matrix is

`A_2=diag(J_2/2,J_2/2,-J_2/2)`,

so its nonzero eigenvalues are exactly `1,1,-1`. Thus this is a genuine target instance, not a diagonal-in-the-independent-coordinates control.

The common density is

`f_2(u)=sqrt(2)(1-sqrt(2)|u|)`, `|u|<=1/sqrt(2)`.

For any symmetric common density `f`, direct delta-function/coarea integration gives the zero-level density

`p_Q(0)=int_0^infinity f(r) [int_0^{2pi} f(r cos theta)f(r sin theta)dtheta]dr`.

For `f=f_2`, support restricts `0<=r<=1/sqrt(2)`. Set `a=sqrt(2)`. The angular integral expands exactly as

`a^2 [2pi-8 a r+2 a^2 r^2]`,

because

`int_0^{2pi} (|cos theta|+|sin theta|)dtheta=8`,

`int_0^{2pi}|cos theta sin theta|dtheta=2`.

Therefore

`p_{Q_2}(0)=a^3 int_0^(1/a) (1-ar)(2pi-8ar+2a^2r^2)dr`

`=2 int_0^1 (1-s)(2pi-8s+2s^2)ds`

`=2pi-7/3`.

Hence

`p_{Q_2}(0)=3.9498519738462528... > pi`.

For this triangular `f_2`, the positive two-square density is bounded and continuous; convolving it with the reflected one-square `L^1` density gives a continuous representative for `Q_2`. Thus this is an essential-supremum lower bound, not merely a value assigned to an arbitrary version of a density.

This independently confirms the finite part of the new correction.

## 3. Independent review of the block-CLT lower bound `C >= 3 sqrt(2)`

For every integer `m>=1`, take `3m` iid `Uniform[-1/2,1/2]` variables and split them into three disjoint blocks. Define

`U_m=m^(-1/2) sum_{j=1}^m X_j`,

`V_m=m^(-1/2) sum_{j=m+1}^{2m} X_j`,

`W_m=m^(-1/2) sum_{j=2m+1}^{3m} X_j`,

and

`Q_m=U_m^2+V_m^2-W_m^2`.

Its matrix is

`A_m=diag(J_m/m,J_m/m,-J_m/m)`.

Each rank-one block has one eigenvalue `+1` or `-1`, so the spectrum of `A_m` is exactly

`{1,1,-1,0,...,0}`.

Thus every finite `m` is an exact-threshold target instance.

The characteristic function of `U_m` is

`psi_m(t)=[sin(t/(2sqrt(m)))/(t/(2sqrt(m)))]^m`,

which converges pointwise to `exp(-t^2/24)`. Hence the independent triple `(U_m,V_m,W_m)` converges in law to independent Gaussians `(G_1,G_2,G_3)` of variance `1/12`, and

`Q_m => T=G_1^2+G_2^2-G_3^2`.

Now `G_1^2+G_2^2` is exponential with density `6 exp(-6u)` for `u>=0`. Also

`E exp(-6G_3^2)=1/sqrt(2)`.

Therefore, for `t>=0`,

`p_T(t)=3 sqrt(2) exp(-6t)`.

In particular,

`P(T in [0,h])=(1-exp(-6h))/sqrt(2)`.

If one finite constant `C` bounded the essential density of every target instance, then for every finite `m`,

`P(Q_m in [0,h])<=C h`.

The interval `[0,h]` is a continuity set for `T`, so weak convergence gives

`(1-exp(-6h))/sqrt(2) <= C h`.

Letting `h downarrow 0` yields the necessary bound

`boxed(C >= 3 sqrt(2) = 4.242640687119285...)`.

This argument needs only weak convergence, not pointwise convergence of the finite-m densities. It independently verifies the corrected lower bound in a form directly tied to the target quantifiers.

## 4. New lemma: exact distribution of physical 3x3 determinant mass

The block witnesses expose a precise obstruction to any proof that selects one physical triple.

### Lemma 4.1 — rank-three principal determinant mass

Let a real symmetric matrix have rank exactly three and write

`A=R Lambda R^T`,

where `R` is `n x 3`, `R^T R=I_3`, and `Lambda=diag(lambda_1,lambda_2,lambda_3)` is nonsingular. For a coordinate triple `I`, let `A_I` be the corresponding principal `3 x 3` block and `R_I` the `3 x 3` row submatrix. Then

`det(A_I)=det(Lambda) det(R_I)^2`.

Consequently

`boxed(sum_{|I|=3} |det A_I| = |lambda_1 lambda_2 lambda_3|)`.

#### Proof

`A_I=R_I Lambda R_I^T`, so taking determinants gives the first identity. Since `det(R_I)^2>=0`, all nonzero principal triple determinants have the common sign `sign(det Lambda)`. Cauchy–Binet applied to `R^T R=I_3` gives

`sum_{|I|=3} det(R_I)^2=det(R^T R)=1`.

Multiplying by `|det Lambda|` proves the claim. QED.

This is an exact conserved aggregate quantity: coordinate delocalization can make every individual principal determinant tiny while leaving total determinant mass fixed.

### Corollary 4.2 — the block-CLT witness completely delocalizes the determinant mass

For `A_m=diag(J_m/m,J_m/m,-J_m/m)`, a principal coordinate triple is nonsingular if and only if it selects exactly one coordinate from each block. There are exactly `m^3` such triples, and every one has

`det A_I=-m^(-3)`.

All other principal `3 x 3` determinants vanish. Hence

`max_{|I|=3}|det A_I|=m^(-3) -> 0`,

while

`sum_{|I|=3}|det A_I|=m^3*m^(-3)=1`.

This is the most symmetric possible failure of a maximum-minor strategy: the spectral strength is not absent; it is spread over `m^3` physical triples.

## 5. Applying the compatible fleet04 Schur-pivot theorem

The completed fleet04/B18 theorem states that for a physical principal triple

`B=[[a,b^T],[b,C]]`

whose scalar pivot is nonzero and whose Schur complement is definite,

`||p_Q||_infinity <= 2 sqrt(pi)/( |a| |det B| )^(1/4)`.

Apply it to any nonsingular triple of `A_m`. After choosing the negative block coordinate as the minority-sign pivot,

`B=diag(1/m,1/m,-1/m)`,

`a=-1/m`,

`det B=-1/m^3`,

and the Schur complement is `diag(1/m,1/m)>0`.

The partner theorem therefore gives exactly

`boxed(||p_{Q_m}||_infinity <= 2 sqrt(pi) m)`.

This grows linearly with `m`, even though the family has fixed nonzero spectrum `{1,1,-1}` and the lower-bound witness has an `O(1)` limiting density scale `3sqrt(2)`.

Every other physical coordinate triple is singular, so no alternative single principal triple improves the scaling within this family.

### Target-relevant implication

This proves a structural negative statement about a proof mechanism, not about the conjecture itself:

> A universal proof cannot be obtained by selecting one physical principal triple and paying the completed Schur-pivot estimate on that triple. The exact target family `A_m` forces every such payment to deteriorate like `m`.

The rank-three determinant identity shows what a replacement must retain: **aggregate** principal-minor mass is dimension-free even when the best individual minor tends to zero. Any successful localization/minor argument must aggregate before applying a nonlinear inverse-determinant cost, or use a genuinely global product-measure mechanism.

This conclusion is compatible with the live `QFORM-CROSSMINOR-ALONE-FALSE` correction. I do not infer boundedness from a rank-two cross minor; the statement concerns why a one-triple rank-three Schur-pivot upper-bound strategy cannot close the full theorem.

## 6. Relation to the newly supplied diffuse upper branch

The live correction also records a distinct cross-block Fourier theorem and a rank-exactly-three delocalized branch with a universal upper bound `24` when the row leverage is at most `1/12`. For `A_m`, each nonzero spectral row has leverage `1/m`, so for `m>=12` that aggregate cross-block mechanism gives a dimension-free bound while the single-triple Schur-pivot bound is `2sqrt(pi)m`.

This is a clean mechanism comparison on the same exact target family: aggregation succeeds where maximum-minor selection provably loses dimension. It does not solve mixed-leverage rank-three matrices or arbitrary higher-rank matrices.

## 7. What is new in this run and what remains open

**Independently reviewed, not claimed new:**

- the finite six-uniform witness `p_Q(0)=2pi-7/3>pi`;
- the necessary universal-constant lower bound `C>=3sqrt(2)`.

Both had entered the live correction inbox during this run and were explicitly marked pending independent review; the derivations above were performed independently before relying on them.

**New mathematics in this run:**

1. the exact rank-three identity `sum_I |det A_I|=|det Lambda|` for physical principal triples;
2. the complete determinant-mass profile of the block-CLT witness (`m^3` equal nonsingular triples of determinant `-m^-3`);
3. application of the completed fleet04 Schur-pivot theorem showing its best possible one-triple payment on this valid target family is `2sqrt(pi)m`;
4. the resulting mechanism-level obstruction: single-principal-triple selection cannot yield a dimension-free proof, while aggregate determinant mass remains conserved.

**First unpaid implication:** turn the conserved aggregate rank-three determinant mass (or an analogous cross-block quantity when additional spectral directions are present) into a product-measure small-ball/density bound *before* taking inverse determinant powers. The argument must survive mixed leverage and extra eigenvalues without discarding dependent remainder terms.

The full quadratic-form conjecture remains **OPEN / NOT PROVED**.

## Provenance

- live target/corrections: `yspennstate/math-research-brain`, fresh `main` control revision `2026-09-22.5`;
- reviewed lower-bound correction: interactive run `20260922T121109Z-crossblock-and-lower-bounds`, scientific commit `8624982153e5a2154e4ae8922d2fe4dc77080efc`;
- compatible fleet04 theorem applied: fleet04/B18 run `20260922T113729Z-fleet04-B18-qform-r1`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`;
- no completed fleet04/B17 QFORM artifact was visible at the final pre-publication partner check.
