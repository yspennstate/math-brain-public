# fleet02/B06 — curved fiber integration: definite-pair coarea, a delocalized adversary, and determinant-mass repair

**Run:** `b06-20260922T113045Z-d47192d10a82`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** fleet02/B06, `Curved fiber integration` / pathway `GEOMETRY`  
**Classification:** `ESSENTIAL_STEP_APPLIED` plus local `CANDIDATE_REFUTED`; **full target OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 0. Control and corrections consumed

The later owner order supersedes the earlier FEI assignment. The target is: for independent real `X_i` with densities `f_i<=1` and real symmetric `A` having at least three eigenvalues of magnitude at least `1`, prove that `Q=X^TAX` has an essentially bounded density with one universal dimension-free constant.

Fresh control before final publication was `yspennstate/math-research-brain@60757c672067bfb966846b7fabfab6d34b80e60c`, with B06 assignment blob `2232129fa7f54afbd24ee9798bb7fa25187cb9db`. I consumed the current required corrections:

- `QFORM-POINTWISE-DECAY-FALSE`: no law-uniform pointwise Fresnel power decay over arbitrary densities `<=1`;
- `QFORM-FIBER-SUP-DIMENSION-LOSS`: integrating an unrestricted spectral-fiber supremum can lose a factor growing with dimension;
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: diagonalizing `A` destroys coordinate independence, so rotated-coordinate convolution arguments are invalid without additional product-structure control.

The correction inbox was empty at the publication snapshot.

The named partner fleet03/B06 had no completed handoff at the fresh programme snapshot, so I did not wait or fabricate a dependency. I instead consumed and applied the exact OTHER-account source fleet03/B17 run `fleet03-B17-20260922T112131Z`, commit `c64fcff680b0a252a3c92002c60eedba02bbb9ec`, report blob `570781af62598117e1014e1edd6831b958bf00c4`. That report proves the exact same-sign two-square bound `pi/sqrt(|lambda_1lambda_2|)` in aligned independent coordinates and refutes the proposed law-uniform pointwise Fresnel decay. I use its two-dimensional geometry as a premise, not as a claim of mine.

## 1. Curved-fiber lemma that survives arbitrary outside coupling

The simplest source-valid weighted replacement is to keep the entire ellipse geometry inside a physical two-coordinate fiber rather than replacing it by a fiber maximum.

### Theorem 1 — `QFORM-DEFINITE-PHYSICAL-PAIR-v1`

Let `X_1,...,X_n` be independent with densities at most `1`, and let `Q(X)=X^TAX`. Suppose that for physical coordinates `i!=j` the full principal block

`B=A[{i,j},{i,j}]`

is positive definite or negative definite. Then `Q(X)` has a density and

`||p_Q||_infinity <= pi/sqrt(det B)`.

No assumption is made on the entries coupling these two coordinates to the remaining `n-2` coordinates.

### Proof

Condition on all variables except `X_i,X_j`. For every fixed outside vector `w`, writing `z=(X_i,X_j)`,

`Q_w(z)=z^T B z + b(w)^T z + c(w)`.

The conditional joint density of `z` is exactly `h(z)=f_i(z_1)f_j(z_2)`, hence `0<=h<=1` and `int h=1`. If `B>0`, complete the square and make the linear change `y=B^{1/2}(z-z_0)`. Translation preserves the pointwise density bound and `dz=(det B)^(-1/2)dy`. At every output level `s`, the conditional pushforward density is at most

`(det B)^(-1/2) int_{R^2} delta(s-|y|^2)dy = pi/sqrt(det B)`,

because in polar coordinates `int delta(s-r^2) r dr dtheta=pi`. The negative-definite case follows after changing the sign of the quadratic polynomial. The bound is uniform in `w`; averaging the conditional laws preserves the same `L^infinity` bound. `QED`

This genuinely retains the curved fiber. It permits a nonzero cross term between the selected physical coordinates and arbitrary linear terms induced by all outside coordinates. It strictly extends the already-closed aligned diagonal subcase.

## 2. The tempting finite-coordinate reduction is false

A natural attempt to finish from Theorem 1 is to claim that three large eigenvalues force a uniformly definite principal block on a bounded number of original coordinates. This is false, even in exact rank three.

### Construction — `QFORM-HADAMARD-DELOCALIZED-v1`

Let `n=2^k`, `k>=3`, let `H_n` be the Sylvester Hadamard matrix, and let `u_1,u_2,u_3` be its first three normalized columns. Put

`U=[u_1 u_2 u_3]`, `D=diag(1,1,-1)`, and `A=UDU^T`.

Since `U^TU=I_3`,

`spec(A)=(1,1,-1,0,...,0)`.

So the target's three-large-eigenvalue hypothesis is satisfied exactly. Every row of `U` has squared norm `3/n`. For any physical coordinate set `S` with `|S|=m`,

`A_SS=U_S D U_S^T`,

hence

`||A_SS||op <= ||U_S||op^2 <= ||U_S||F^2 = 3m/n`.

Thus for every fixed `m`, **every** `m`-coordinate compression has operator norm tending to zero with `n`. No dimension-independent number of physical coordinates can be guaranteed to retain constant-size curvature.

The failure is sharper for pairs. The selected Hadamard rows have the form `(1,s_i,t_i)/sqrt(n)`, with `s_i,t_i in {+1,-1}`. Therefore

`A_ii=1/n`,

`A_ij=(1+s_i s_j-t_i t_j)/n in {-1/n,1/n,3/n}`,

so for every `i!=j`,

`det A[{i,j}] = 1/n^2-A_ij^2 <=0`.

There is not a single definite physical `2x2` principal block, although the whole matrix has two positive unit eigenvalues and one negative unit eigenvalue.

This is a rigorous falsifier of the local reduction, **not** a counterexample to the target conjecture.

## 3. Repair: replace one large fiber by a determinant-mass measure

The Hadamard family does not destroy same-sign curvature; it distributes it across many tiny physical coordinate pairs. Cauchy--Binet gives the exact invariant.

### Lemma 2 — `QFORM-SAMESIGN-DETERMINANT-MASS-v1`

Let `r_1,r_2` be orthonormal eigenvectors with same-sign eigenvalues `lambda_1,lambda_2`, and write

`R=[r_1 r_2]`,

`P=R diag(lambda_1,lambda_2)R^T`

for this rank-two same-sign spectral component. For every physical pair `S={i,j}`,

`det P_S = lambda_1 lambda_2 det(R_S)^2 >=0`,

and

`sum_{|S|=2} det P_S = lambda_1 lambda_2`.

In particular, if both large eigenvalues have magnitude at least `1`, the total determinant mass is at least `1`.

### Proof

For each pair,

`P_S=R_S diag(lambda_1,lambda_2)R_S^T`,

so `det P_S=lambda_1lambda_2 det(R_S)^2`. By Cauchy--Binet,

`sum_{|S|=2}det(R_S)^2=det(R^TR)=1`.

Summing proves the identity. `QED`

This is the weighted replacement suggested by the B06 geometry assignment: the natural weights are the squared Pluecker coordinates `det(R_S)^2`. They sum to one exactly, so a delocalized eigenspace does not lose total two-dimensional curvature even though no individual physical fiber need carry an `O(1)` share.

For the `n=16` Hadamard checker, the positive rank-two component has 64 pair minors with determinant numerator `4` and 56 zero pair minors; after the `16^2` scaling their total is exactly `1`. Yet adding the third negative eigendirection makes every full `A_S` pair determinant nonpositive. This is the precise cancellation obstruction that a correct weighted argument must survive.

There is an analogous rank-three identity: if `T=R Lambda R^T` is a rank-three spectral truncation with three orthonormal columns in `R`, then for every physical triple `S`,

`det T_S = det(Lambda) det(R_S)^2`,

and `sum_{|S|=3}det(R_S)^2=1`. Thus the absolute three-dimensional determinant mass equals `|det Lambda|`.

## 4. What the repair does and does not prove

Theorem 1 shows that a **full** definite physical pair of determinant `d` immediately gives a target-level density bound `pi/sqrt(d)`. Lemma 2 shows that a same-sign spectral pair always carries total determinant mass at least one over physical pairs. But the Hadamard construction proves these facts cannot be naively combined: the other eigendirections can cancel definiteness of every full physical pair.

Therefore the next implication must use the spectral determinant-mass weights **inside** a product-structure-preserving estimate before the rest of the quadratic form is collapsed to a full physical principal block.

A correct form of the unpaid implication is:

### `QFORM-WEIGHTED-CURVED-FIBER-AGGREGATION-v1`

For a same-sign large eigenpair with Pluecker weights

`w_ij=det(R_{ij})^2`, `sum_{i<j}w_ij=1`,

prove a dimension-free small-ball or averaged-frequency estimate for the full `Q` by aggregating the exact two-dimensional ellipse kernels over pairs with weights `w_ij`, while keeping the original product density active and allowing all remaining spectral components. The estimate must not replace each fiber by its unrestricted supremum and must not assume that one `w_ij` is large.

This is quantitatively narrower than the generic statement “use product structure”: the exact conserved quantity to be spent is now the determinant-mass probability measure `w_ij`.

## 5. Compact conditional end-to-end argument

1. Among any three large eigenvalues choose a same-sign pair.
2. If a full physical definite pair has determinant bounded below, close by Theorem 1.
3. Otherwise do not search for a bounded-size coordinate localization; `QFORM-HADAMARD-DELOCALIZED-v1` rules that mechanism out.
4. Use Lemma 2 to assign a normalized determinant-mass weight to every physical pair.
5. Prove `QFORM-WEIGHTED-CURVED-FIBER-AGGREGATION-v1`. A bound `sup_u P(|Q-u|<=epsilon)<=C epsilon` would imply an essentially bounded density by the standard interval differentiation argument.

Step 5 is the first essential missing implication. No continuity conclusion for the full target is claimed.

## 6. Exact computation

The deterministic exact-integer checker was executed in this run. For `n=16`, writing `A=M/16`, it verifies:

- the first three Hadamard columns are orthogonal;
- `M^3=16^2 M`, `tr(A)=1`, `tr(A^2)=3`, hence the symmetric matrix has eigenvalues exactly `+1,+1,-1,0,...,0`;
- all 120 physical `2x2` principal determinants are nonpositive: 88 have numerator `0`, 32 have numerator `-8`;
- the positive rank-two spectral component has total pair determinant mass exactly `1`.

Checker SHA-256: `5038695df78b17715a960a500a207888a514796de5e97ab68b7188362b9ea002`.  
Output SHA-256: `b47f44694f9827829a2583cd85d08ce569f04e9604835908085fa7cda7783a74`.  
Status: `PASS`.

## 7. Status

**PROVED / supporting:** `QFORM-DEFINITE-PHYSICAL-PAIR-v1`; `QFORM-SAMESIGN-DETERMINANT-MASS-v1`; the rank-three analogue; exact delocalized Hadamard construction and compression bound.

**CANDIDATE_REFUTED:** any claim that the three-large-eigenvalue hypothesis forces constant curvature on a dimension-independent number of original coordinates, including the hoped-for uniformly definite physical pair.

**OPEN:** `QFORM-WEIGHTED-CURVED-FIBER-AGGREGATION-v1` and the full bounded-density conjecture.
