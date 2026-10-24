# account02/B17 — multiplicity-nine recertification and an exact no-pivot counterexample to the robust-pair-only `s_8` shortcut

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`. Current master observed before this run's writes: `0aa54bd634644b2922e9faecd003692d7f29e61e`, carrying the same manuscript blob.

Status of this note:

- complete fixed-multiplicity threshold certified here: **9**;
- new result: **exact source-valid no-pivot counterexample to any `s_8` receiver that discards the remaining Schur spectrum after extracting a robust two-anchor cross pair**;
- multiplicity 8 remains **OPEN**;
- unrestricted three-eigenvalue QFORM remains **OPEN**.

The counterexample is not a counterexample to the eight-eigenvalue theorem: it has only two nonzero spectral directions. Its point is to prove that the newly extracted robust pair cannot by itself replace the missing global spectral currency.

## 1. Complete threshold-nine replacement, recertified

This worker's preceding immutable B17 proof established the following theorem; I rechecked all branch hypotheses and constants against the pinned baseline during the present full audit. A genuinely separate account02/B18 reconstruction now also records PASS, but the argument below is stated so that the present threshold claim has a closed dependency map rather than resting on that verdict.

### Theorem `QFORM-FIXED-MULTIPLICITY-9-v1`

Let `X_1,...,X_n` be independent real random variables with densities bounded by `K<infinity`. Let `A=A^T`, `b` and `c` be arbitrary. If

` s_9(A)>=s>0,`

then `Q=X^TAX+b^TX+c` has an essentially bounded density with

`boxed: ||p_Q||_infinity <= 6010 K^2/s.`

No support, moment, iid, log-concavity, signature, exact-rank, leverage, diagonal-basis, or post-rotation-independence hypothesis is introduced.

### New analytic receivers used by the replacement

For a literal physical crossing matrix `B`, put `E_r(B)=e_r(BB^T)`, the sum of squared `r x r` row minors.

The grouped product-Fourier compiler is obtained by keeping every promoted heavy row as a literal original-coordinate variable, applying Plancherel to the complex pushforward in that physical row bank, duplicating only a disjoint literal product bank, and using determinant-squared Holder weights on the remaining crossing rows. If the determinant-subset marginals are `alpha_i<=1/2`, scalar Fourier powers are legal at exponent `1/alpha_i>=2`. The entropy identity

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`

follows by uniformly ordering the sampled `ell`-subset and applying entropy subadditivity. This yields a `|t|^{-(k+ell)/2}` envelope for `k` promoted rows and an `ell`-row residual determinant packet. Heavy marginals are promoted and exact Gram--Schmidt/base-times-height identities preserve the determinant mass.

The resulting marginal-free terminal estimates are

`boxed: ||p_R||_infinity <= C_3 E_3(B)^(-1/6),`

where

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`,

and

`boxed: sup_a E|R-a|^(-1/2) <= C_2 E_2(B)^(-1/8),`

where

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

The order-two statement is only a half-potential theorem; the generic order-two `|t|^-1` endpoint is not falsely promoted to an `L^infinity` density theorem.

### Normalized branch proof

Set `K=s=1`, `eta=1/100`, `kappa=80^-2`.

**No physical pivot.** The audited baseline spectral-to-volume theorem at order three applies because `4*3-3=9`:

`V_3(A)>=kappa^3`.

A fair literal coordinate cut gives

`E_3(B)>=4^-3 kappa^3`,

so `E_3(B)^(-1/6)<=160`. Hence

`||p_Q||_infinity <=160 C_3=2370.934026...<2400`.

**Scalar pivot.** If `|A_hh|>=eta`, the scalar Schur complement retains at least eight unit-scale directions. If it itself has a pivot, the audited baseline pivot theorem gives truncated half-potential at most `600`; the outside-unit tail adds at most one. If it has no pivot, then in particular it has five unit-scale directions, so the order-two baseline structural theorem and fair cut give

`E_2>=4^-2 kappa^2`.

Therefore

`sup_a E|R-a|^-1/2 <= C_2 sqrt(160)=152.9919...<153`.

In either scalar subbranch the full half-potential is `<=601`; the square profile costs `eta^-1/2=10`, hence

`||p_Q||_infinity<=6010`.

**Definite pair pivot.** Direct conditioning gives

`||p_Q||_infinity<=pi/sqrt(eta)=10 pi<32`.

**Indefinite pair pivot.** The pair Schur complement retains at least seven unit-scale directions and therefore has norm at least one. The audited hyperbolic envelope plus quarter-power logarithmic-potential estimate gives `<251`.

These four alternatives exhaust the normalized problem. Scaling by `Y=KX` and `A/s` gives the stated `6010 K^2/s` theorem.

### Closed dependency map

`baseline Fourier/Gaussian/Riesz`
` -> geometric BL -> product projection -> scalar Fourier powers`
` -> grouped physical-product compiler`
` -> marginal-free E_3 density and E_2 half-potential`
` -> baseline order-3 spectral volume + fair cut (no-pivot s_9)`
` -> baseline Schur count + order-2 spectral volume (scalar pivot)`
` -> baseline pair-pivot kernels`
` -> normalized theorem -> K,s scaling`.

Thus **9** is a complete replacement threshold. Nothing below is claimed complete in this note.

## 2. Current `s_8` structural collar and the tempting shortcut

The newest proved terminal analysis for the no-pivot `s_8(A)>=1` chamber says: either the disjoint third volume is already large (paid by the `E_3` density receiver), or there is a literal two-coordinate pair `H` for which

`det(A[H,H^c] A[H,H^c]^T) >= 0.3649442658...`,

while

`|A_hh|<10^-2`, `|det A[H,H]|<10^-2`.

The same pair carries a dimension-free good-seed mass. If its self-block is exactly zero, a direct two-anchor affine receiver gives a continuous density `<5.318`. If the self-block is invertible, the order-two Schur half-potential pays the moving logarithmic singularity; the existing route leaves the nonlogarithmic term `6 |det A[H,H]|^-1/2`.

A very tempting shortcut is therefore:

> once a robust cross pair has been extracted, forget the remaining spectrum and prove a determinant-free two-anchor receiver from only (i) ambient no-pivot, (ii) a uniformly nondegenerate outside cross map, and (iii) a tiny/self-near-zero pair block.

The next theorem shows this shortcut is **false**, even with independent unit uniforms and even when the entire finite matrix has no manuscript `eta`-pivot.

## 3. New exact counterexample: robust cross + no pivot + arbitrarily small indefinite self block can still have infinite output density

### Theorem `QFORM-NOPIVOT-ROBUST-PAIR-ONLY-RECEIVER-FALSE-v1`

Fix `eta=1/100`. For every `0<epsilon<eta`, choose an integer

`m > max(50,10/epsilon)`.

There is a real symmetric `(2+2m) x (2+2m)` matrix `A_(epsilon,m)` with the following properties:

1. **No manuscript `eta`-pivot:** every physical diagonal entry has modulus `<eta` and every physical principal `2 x 2` determinant has modulus `<eta`.
2. For the literal pair `H={1,2}`, the self block is

   `K=epsilon diag(1,-1)`,

   hence `|det K|=epsilon^2 ->0`.
3. The outside cross block `C=A[H,H^c]` is maximally robust:

   `CC^T=I_2`, so `det(CC^T)=1`.
4. `rank A_(epsilon,m)=2`; its Schur complement after pivoting on `K` is exactly zero.
5. For iid original physical inputs `Unif[-1/2,1/2]` (all densities exactly one on their supports), the quadratic form `X^T A_(epsilon,m) X` has an **unbounded** density; indeed its density diverges logarithmically at zero.

Consequently there is no finite bound for this local receiver class depending only on the robust-cross determinant, the no-pivot constant and an upper bound on `||K||`. In particular, one cannot interpolate the exact-zero two-anchor theorem through small nonzero indefinite `K` without also spending the ambient Schur/spectral information.

### Construction

Let

`J=diag(1,-1)`, `K=epsilon J`, `a=(2m)^(-1/2)`.

Let `C` be the `2 x 2m` matrix whose first `m` columns are

`a(1,1)^T`

and whose last `m` columns are

`a(1,-1)^T`.

Then

`CC^T = m a^2 [[1,1],[1,1]] + m a^2 [[1,-1],[-1,1]] = I_2`.

Define

`R=C^T K^-1 C`

and

`A_(epsilon,m) = [[K,C],[C^T,R]].`

Because the Schur complement of `K` is exactly zero,

`rank A_(epsilon,m)=rank K=2`.

Equivalently, with `T=[I_2, K^-1 C]`,

`A_(epsilon,m)=T^T K T`.

Thus the matrix has one positive and one negative nonzero eigenvalue and all remaining eigenvalues zero. This is why the example is a shortcut counterexample rather than an `s_8` QFORM counterexample.

### Exact no-pivot check

Every outside column `c_j` is null for the indefinite form `J`:

`c_j^T J c_j=0`.

Hence every outside diagonal entry of `R` is zero. The two anchor diagonal entries are `+epsilon` and `-epsilon`, both below `eta`.

There are only three kinds of principal `2 x 2` determinants.

**Anchor--anchor:**

`det K = -epsilon^2`, so `|det K|=epsilon^2<eta`.

**Anchor--outside:** since the outside diagonal is zero,

`|det A[{h,j},{h,j}]| = |C_hj|^2 = a^2=1/(2m)<eta`.

**Outside--outside:** if the two columns belong to the same sign family, `R_jk=0`. If they belong to opposite families,

`|R_jk|=(1/epsilon)|c_j^T J c_k|=1/(epsilon m)`.

Therefore the principal determinant has modulus either zero or

`1/(epsilon^2 m^2)<eta`

by `m>10/epsilon`.

So the **entire matrix** is in the manuscript no-pivot chamber despite its robust cross pair.

### Exact logarithmic density blowup

Split the independent input vector as `X=(U,Y)`, where `U in R^2` consists of the anchor coordinates and `Y in R^(2m)` the outside coordinates. Then

`Q = U^T K U +2 U^T C Y +Y^T C^T K^-1 C Y`

completes exactly to

`boxed: Q=(U+K^-1 C Y)^T K (U+K^-1 C Y).`

Write

`W=U+K^-1 C Y=(W_1,W_2)`.

The vector `W` has an absolutely continuous density `g`: it is the convolution of the uniform square density of `U` with the law of the independent linear image `K^-1 C Y`.

More is true: `g` is bounded **below by a positive constant on a neighborhood of the origin**. Indeed, put

`delta=epsilon/(8 a m)>0`

and consider the event

`E={|Y_j|<=delta for every j}`.

Since `delta<1/2`,

`P(E)=(2 delta)^(2m)>0`.

On `E`, each coordinate of `K^-1 C Y` has absolute value at most

`(a/epsilon) sum_j |Y_j| <= (a/epsilon)(2m delta)=1/4`.

Therefore, for every `w` with `||w||_infinity<=1/4`, whenever `E` occurs we have

`w-K^-1 C Y in [-1/2,1/2]^2`,

where the anchor density equals one. Hence

`g(w)>=c_(epsilon,m):=P(E)>0`

throughout that square.

Now set

`u=W_1-W_2`, `v=W_1+W_2`.

The Jacobian is `dw_1 dw_2=(1/2) du dv`, and

`Q=epsilon (W_1^2-W_2^2)=epsilon u v`.

Whenever `|u|,|v|<=1/4`, both `|W_1|,|W_2|<=1/4`, so the `(u,v)` joint density is at least `c_(epsilon,m)/2`.

For `0<z<epsilon/64`, the density of `Q` therefore satisfies the explicit lower bound

`p_Q(z)
 >= (c_(epsilon,m)/(2 epsilon))
    int_(4z/epsilon)^(1/4) du/u
 = (c_(epsilon,m)/(2 epsilon)) log(epsilon/(16z)).`

The right side tends to infinity as `z downarrow0`. Thus

`boxed: ||p_Q||_infinity=+infinity.`

This is an essential blowup, not merely a value assigned at one exceptional point.

## 4. What the counterexample rules out — and what it does not

It rules out all arguments of the form

`robust literal pair cross + no eta-pivot + tiny pair self-block`
` -> universal density bound`,

when the rest of the quadratic matrix is discarded or allowed to be arbitrary. The failure persists for every nonzero `epsilon`, however small, whereas the exact-zero pair theorem is valid. Thus the exact-zero receiver is **not perturbatively stable as a local theorem**.

The example also identifies the missing currency exactly. Its pair Schur complement is zero. In a genuine target matrix with `s_8(A)>=1`, pivoting on an invertible two-coordinate block loses at most two spectral directions, so the Schur complement retains at least six unit-scale directions. Any successful near-singular `s_8` argument must spend those directions, or an equivalent good-seed/overlap currency. The determinant-singular `6 D^-1/2` term cannot simply be deleted from the current hyperbolic estimate using the robust cross determinant alone.

The example does **not** disprove multiplicity eight: it has rank two. It also does not disprove QFORM. It is a counterexample to a proof shortcut, exactly in the account02 adversarial sense requested by the owner objective.

## 5. Precise remaining threshold-eight obligation

Combining the proved terminal collar with the robust-anchor extraction, the only unpaid no-pivot `s_8` chamber has a literal pair `H` satisfying a fixed cross determinant lower bound and small self block, plus genuine ambient spectral provenance. The exact-zero self-block subcase is already bounded. For invertible near-singular self blocks the logarithmic critical-value singularity is already paid by the order-two Schur half-potential, but the nonlogarithmic determinant term remains; rank-one singular nonzero self blocks are also unresolved.

The new counterexample proves that the next receiver must be **Schur-aware**. A valid route must combine the pair cross geometry with at least one of:

- the six large directions in the pair Schur complement forced by `s_8`;
- the same-pair good-seed determinant mass retained by the collar construction;
- an equivalent product-preserving third-curvature mechanism.

A receiver that depends only on `det(CC^T)` and the small pair block is impossible.

Therefore the lowest complete theorem certified in this run remains

`boxed: multiplicity 9, constant 6010 K^2/s.`

Multiplicity 8 remains open. The unrestricted three-eigenvalue theorem remains open.
