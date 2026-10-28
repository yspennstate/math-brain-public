# account02/B06 — quadratic-form bounded-density: physical-block adversary and determinant-mass repair

**Run:** `b06-20260922T113045Z-d47192d10a82`  
**Classification:** `ESSENTIAL_STEP_APPLIED` + local `CANDIDATE_REFUTED`; **full target OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target and source pins

The active target is:

> There is a universal constant `C` such that whenever `X_1,...,X_n` are independent real random variables with densities bounded by `1`, and `Q(x)=x^T A x` has at least three eigenvalues with absolute value at least `1`, the law of `Q(X)` is absolutely continuous with density bounded by `C`.

Control was initially resolved at brain commit `995e9b1aa5c019d6dc4a0c7fc282ea6ee8629607` and refreshed before publication at `805f03e66f360052064cc12df16a974bc7d6762c`; the README blob at the refresh is `66a4971fdf4f06635581f4bee32796394d6ce103`. No later stop was present at publication time.

The named OTHER-account result consumed and used here is account03/B17 run `account03-B17-20260922T112131Z`, exact source commit

`c64fcff680b0a252a3c92002c60eedba02bbb9ec`,

report blob

`570781af62598117e1014e1edd6831b958bf00c4`.

That report proves two facts which I do not re-derive as fleet novelty:

1. the proposed law-uniform pointwise Fresnel decay is false;
2. if two independent physical coordinates already appear as a same-sign diagonal pair with coefficients `lambda_1,lambda_2`, then the sum of their squares has density at most `pi/sqrt(|lambda_1 lambda_2|)`.

The same report closes the full coordinate-diagonal branch with `C=pi`. The arbitrary rotated-eigenbasis case remains open.

A bounded literature check during this run found Rudelson--Vershynin's linear-image small-ball theorem and Hanson--Wright-type quadratic concentration under substantially stronger tail assumptions. Neither result is used below as a premise, and no novelty claim is inferred from the search.

## 2. First positive repair: any definite physical 2x2 principal block is enough

The account03/B17 `pi` lemma extends beyond a zero cross coefficient.

### Theorem 2.1 — `QFORM-DEFINITE-PHYSICAL-PAIR-v1`

Let `X_1,...,X_n` be independent real random variables with densities bounded by `1`, and let `Q(X)=X^T A X`, with `A` real symmetric. Suppose that for some distinct physical coordinates `i,j`, the principal block

`B=A[{i,j},{i,j}]`

is positive definite or negative definite. Then `Q(X)` has a density and

`||p_Q||_infinity <= pi / sqrt(det B)`.

Here `det B>0` for either sign of definiteness. In particular, if `det B>=1`, the universal bound `pi` follows immediately.

### Proof

Condition on all variables other than `X_i,X_j`. For each fixed outside value `w`, write `z=(X_i,X_j)`. The conditional polynomial has the form

`Q_w(z)=z^T B z + b(w)^T z + c(w)`.

The conditional joint density of `z` is

`h(z)=f_i(z_1) f_j(z_2)`,

so `0<=h<=1` and `int h=1`.

Assume first `B>0`. Completing the square translates `z` and changes only the output center. Let `y=B^{1/2}(z-z_0)`. Translation preserves the pointwise density bound and `dz=(det B)^(-1/2)dy`. At every positive level `s`, the pushforward density is bounded by replacing the translated input density by `1`:

`p_{Q_w}(s) <= (det B)^(-1/2) int_{R^2} delta(s-|y|^2) dy`.

In polar coordinates,

`int delta(s-r^2) r dr dtheta = pi`,

so

`||p_{Q_w}||_infinity <= pi/sqrt(det B)`.

If `B<0`, apply the same argument to `-Q_w`. The bound is uniform in `w`. Averaging the conditional laws over the outside coordinates is a mixture, and a mixture of densities bounded by the same constant remains bounded by that constant. This proves the theorem. `QED`

### Why this matters

The theorem allows an arbitrary cross term `2A_ij X_i X_j` and arbitrary coupling of both selected coordinates to every outside variable. It therefore strictly enlarges the already-closed coordinate-diagonal route. A natural next reduction would be to hope that the three-large-eigenvalue hypothesis forces one such physical pair with determinant bounded below by a universal constant. The next section shows that this hope is false in a very strong exact sense.

## 3. Exact adversary to every fixed-size physical-coordinate reduction

### Candidate refuted — `QFORM-FINITE-PHYSICAL-BLOCK-v0`

A tempting statement is:

> if `A` has at least three eigenvalues of magnitude at least `1`, then some bounded-size set of original independent coordinates carries an `O(1)` amount of that curvature; in particular one might hope for a uniformly definite physical `2x2` principal block or, more generally, an `m x m` principal compression with an eigenvalue bounded below independently of `n`, for a fixed `m`.

This is false.

### Construction — Sylvester-Hadamard delocalization

Let `n=2^k`, `k>=3`, and let `H_n` be the Sylvester Hadamard matrix. Let `u_1,u_2,u_3` be its first three columns normalized by `1/sqrt(n)`, and put

`U=[u_1 u_2 u_3]`,

`D=diag(1,1,-1)`,

`A=U D U^T`.

Because `U^T U=I_3`, the spectrum of `A` is exactly

`1, 1, -1, 0, ..., 0`.

Thus the owner's three-large-eigenvalue hypothesis is met at equality.

Every row of `U` has squared norm exactly `3/n`. If `S` is any set of `m` physical coordinates, then

`A_SS=U_S D U_S^T`,

and therefore

`||A_SS||_op <= ||U_S||_op^2 <= ||U_S||_F^2 = 3m/n`.

Consequently, for every fixed `m`, every `m`-coordinate compression has vanishing operator norm as `n->infinity`. In particular, when `n>3m`, no such compression has even one eigenvalue of magnitude `1`.

This rules out any proof which first tries to localize the spectral hypothesis into a dimension-independent number of original coordinates while retaining constant-size curvature.

### Stronger failure for physical pairs

For these first three Hadamard columns, each row of `U` is `(1,s_i,t_i)/sqrt(n)` with `s_i,t_i in {+1,-1}`. Hence

`A_ii = 1/n`,

and for `i!=j`,

`A_ij = [1+s_i s_j-t_i t_j]/n in {-1/n,1/n,3/n}`.

Thus every `2x2` physical principal determinant is

`det A[{i,j}] = 1/n^2 - A_ij^2 <= 0`.

So **there is not a single definite physical `2x2` principal block at all**, even though the full matrix has two positive eigenvalues `+1,+1` and one negative eigenvalue `-1`.

The finite checker at `n=16` verifies this exactly, without floating point. Writing `A=M/16`, it finds 88 pair determinants with numerator `0` and 32 with numerator `-8`; all 120 are nonpositive. It also verifies `M^3=16^2 M`, `tr(A)=1`, and `tr(A^2)=3`, which certify the spectrum `+1,+1,-1,0,...,0` for this symmetric matrix.

This is a refutation of the reduction step, **not** of the bounded-density conjecture.

## 4. Repair: the curvature is not lost; it is spread as determinant mass

The adversary suggests the right invariant. The same-sign spectral pair may be completely delocalized across physical coordinates, but it carries an exact Cauchy--Binet determinant budget.

### Lemma 4.1 — `QFORM-SAMESIGN-DETERMINANT-MASS-v1`

Let `r_1,r_2` be orthonormal eigenvectors of `A` with same-sign eigenvalues `lambda_1,lambda_2`. Put

`R=[r_1 r_2]`

and let

`P=R diag(lambda_1,lambda_2) R^T`

be just this rank-two same-sign spectral component. For a physical coordinate pair `S={i,j}`, let `P_S` denote the `2x2` principal block. Then

`det(P_S)=lambda_1 lambda_2 det(R_S)^2 >=0`,

and exactly

`sum_{|S|=2} det(P_S) = lambda_1 lambda_2`.

In particular, if `|lambda_1|,|lambda_2|>=1`, the total physical determinant mass is at least `1`.

### Proof

For a pair `S`,

`P_S=R_S diag(lambda_1,lambda_2) R_S^T`,

so multiplicativity of the `2x2` determinant gives

`det(P_S)=lambda_1 lambda_2 det(R_S)^2`.

Since the signs agree, `lambda_1 lambda_2>0`. By Cauchy--Binet,

`sum_{|S|=2} det(R_S)^2 = det(R^T R)=1`,

because the two columns of `R` are orthonormal. Summing proves the identity. `QED`

### Exact behavior in the Hadamard adversary

For the positive rank-two component

`P=u_1u_1^T+u_2u_2^T`,

the `n=16` exact checker finds 64 physical pairs with determinant numerator `4` and 56 with determinant `0`; after division by `16^2`, their total is exactly `1`, as Lemma 4.1 requires.

So the same-sign curvature survives in the original coordinates, but only as a **distributed mass over many pairs**. In the fully delocalized family each useful minor is of order `n^-2`; there need not be a single pair of constant determinant.

There is an analogous rank-three identity. If `R` has three orthonormal columns and `Lambda=diag(lambda_1,lambda_2,lambda_3)`, then for the rank-three spectral truncation `T=R Lambda R^T`,

`det(T_S)=det(Lambda) det(R_S)^2`

for every triple `|S|=3`, and

`sum_{|S|=3} det(R_S)^2=1`.

Thus the absolute determinant mass of the rank-three spectral truncation is exactly `|lambda_1 lambda_2 lambda_3|>=1`.

## 5. The important caveat: the full matrix can cancel every useful minor

Lemma 4.1 is a spectral-component identity, not yet a density proof. The remaining spectral components of the full matrix can destroy definiteness of every physical pair. The Hadamard example demonstrates this maximally: the positive rank-two component has total pair-determinant mass exactly `1`, yet after adding the single negative eigencomponent `-u_3u_3^T`, every full physical `2x2` principal determinant becomes nonpositive.

Therefore one may not simply replace `P_S` by `A_S` in Lemma 4.1 and invoke Theorem 2.1. This is the repaired statement that the false finite-block reduction was missing.

The first genuinely unpaid implication is now:

### `QFORM-DISTRIBUTED-MINOR-AGGREGATION-v1`

Use the exact same-sign determinant mass

`sum_{i<j} lambda_1 lambda_2 det(R_{ij})^2 = lambda_1 lambda_2`

inside an anti-concentration or oscillatory-integral argument **before** cancellation by the other eigendirections and without selecting a single physical coordinate pair. The aggregation must retain the original product structure of the `X_i` and remain dimension-free.

A plausible route is a multilinear or decoupled estimate which averages physical-coordinate pair kernels with weights `det(R_{ij})^2`. The point is not to find one large minor; the Hadamard family proves that this can be impossible. The proof has to spend the entire determinant budget collectively.

This aligns with account03/B17's conclusion that the rotated coordinates cannot simply be treated as independent, and with account01/B08's null-cone example showing that an arbitrary rotated joint `L^infinity` density bound forgets too much product structure.

## 6. Compact conditional end-to-end route after this run

A conditional proof skeleton is now:

1. among three large eigenvalues choose a same-sign pair `lambda_1,lambda_2`;
2. if the full matrix has a definite physical `2x2` block of determinant `d`, Theorem 2.1 closes immediately with `C<=pi/sqrt(d)`;
3. otherwise do **not** search for a bounded-size coordinate block: the Hadamard family proves that this localization can fail at every fixed size;
4. instead use Lemma 4.1's normalized determinant-mass measure on coordinate pairs, together with the original product density, to derive a dimension-free small-ball or averaged-frequency estimate for the full quadratic form;
5. once `sup_u P(|Q-u|<=epsilon)<=C epsilon` is obtained uniformly, absolute continuity and the density bound follow by differentiation.

Step 4 is the first essential missing implication. Full target status stays **OPEN**.

## 7. Exact checker and hashes

The checker is finite, deterministic, exact-integer arithmetic, and was executed before archival.

- checker SHA-256: `3837e6b93ab013fec2b47e1bb7825255d3728444fa21b719fb7d9ea16baf0d47`
- output SHA-256: `b47f44694f9827829a2583cd85d08ce569f04e9604835908085fa7cda7783a74`
- status: `PASS`

It verifies the `n=16` Hadamard instance, the exact spectrum certificate, nonpositivity of every full physical pair determinant, and total same-sign rank-two determinant mass `1`.

## 8. Status ledger

**PROVED / source-valid in this run**

- `QFORM-DEFINITE-PHYSICAL-PAIR-v1` with exact constant `pi/sqrt(det B)`.
- `QFORM-SAMESIGN-DETERMINANT-MASS-v1` by Cauchy--Binet.
- exact Hadamard family with spectrum `(+1,+1,-1,0,...)` and `||A_SS||op<=3|S|/n` for every physical coordinate set `S`.
- every physical `2x2` principal block in that family is non-definite.

**REFUTED intermediate claim**

- any dimension-independent finite-physical-coordinate localization which is supposed to preserve constant-size curvature from the three-large-eigenvalue hypothesis.

**NOT refuted**

- the owner's bounded-density conjecture itself.

**OPEN**

- `QFORM-DISTRIBUTED-MINOR-AGGREGATION-v1`, i.e. convert total same-sign spectral determinant mass into target-level anti-concentration while retaining product structure and surviving cancellation from the remaining eigendirections.
