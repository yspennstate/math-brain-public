# fleet03/B12 — signed Schur spectral-count reduction and no-blowup extra-eigenvalue recurrence

Run: `20260922T164418Z-qform-eigenvalue-r13`

Status: `ESSENTIAL_SUPPORTING_REDUCTION / FULL_TARGET_OPEN`

Execution: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval was used; no authenticated native brain receiver-context retrieval occurred.

## Source state


Assignment: additional eigenvalue control. Exact target remains the universal bounded-density conjecture for independent coordinate laws with density cap one and symmetric `A` with at least three eigenvalues of modulus at least one.

Consumed completed fleet04 result actually applied: fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`. The designated partner location fleet04/B12 still has no current QFORM handoff or canonical QFORM run visible at the fresh source read, so no result was fabricated on its behalf.

Also incorporated the latest fleet02/B07 handoff only as structural context: `QFORM-Q0-RIDGE-FOUR-HEAVY-DPP-v1`, canonical `yspennstate/math-open-problems@5f319d96212a5828ec74a6ea3e3c87d67290628a`; full QFORM remains open there as well.

## 1. Exact signed Schur spectral-count theorem

Let

`A = [[a, b^T],[b,C]]`

be a real symmetric matrix in one **original physical coordinate**, with `a != 0`, and let

`S = C - b b^T/a`, `u=b/a`, `q=||u||_2`.

Set

`D = diag(a,S)`, `L = [[1,0],[u,I]]`.

Then exactly

`A = L D L^T`, hence `D=L^{-1} A L^{-T}`.

The largest singular value of the shear is

`||L|| = (sqrt(q^2+4)+q)/2`,

so define

`alpha(q) = ||L||^{-2} = 4/(sqrt(q^2+4)+q)^2`.

For `ell>0`, write

`N_+(M;ell)=#{ eigenvalues of M >= ell }`,

`N_-(M;ell)=#{ eigenvalues of M <= -ell }`.

### Theorem 1 (signed count survives Schur elimination)

For every `ell>0`,

`N_+(S; alpha(q) ell) >= N_+(A;ell) - 1_{a>0}`,

`N_-(S; alpha(q) ell) >= N_-(A;ell) - 1_{a<0}`.

Consequently,

`N_+(S;alpha ell)+N_-(S;alpha ell) >= N_+(A;ell)+N_-(A;ell)-1`.

In particular, if `A` has `m` eigenvalues of modulus at least `ell`, then `S` has at least `m-1` eigenvalues of modulus at least `alpha(q) ell`, regardless of all other eigenvalues, their sizes, or their signs.

### Proof

Suppose `lambda_k(A)>=ell`, and let `E` be the span of the top `k` eigenvectors of `A`. For `x in E`, put `y=L^T x`. Then

`y^T D y = x^T A x >= ell ||x||^2`,

while `||y|| <= ||L|| ||x||`. Therefore on the `k`-dimensional subspace `L^T E`,

`y^T D y >= alpha(q) ell ||y||^2`.

Courant-Fischer gives `lambda_k(D)>=alpha(q)ell`. Since `D` is the block diagonal matrix `diag(a,S)`, the scalar block can consume at most one positive threshold eigenvalue, and only when `a>0`. This proves the positive-count inequality. Apply the same argument to `-A` for the negative-count inequality. No rotation of the input law occurs anywhere in the argument. QED.

### Sign-sensitive exact-three corollary

If the guaranteed large signs are `(2 positive,1 negative)` and `a<0`, then `S` retains **two positive** eigenvalues at least `alpha(q)ell`. If `a>0`, then `S` retains at least one positive eigenvalue `>=alpha(q)ell` and one negative eigenvalue `<=-alpha(q)ell`. The reflected statement holds for `(1 positive,2 negative)`.

Thus the sign of a physical Schur pivot determines which exact-three topology survives; arbitrary added spectrum remains present rather than being discarded.

## 2. Heavy-row pivot-or-cross dichotomy with exact constants

Use the completed B12 spectral-window reduction from `yspennstate/math-open-problems@2bd58d21cf8eda48d6451469ceaf5fb8dc19bf5`.

At spectral scale `ell`, if the projection onto `|lambda(A)|>=ell/39` fails the leverage gate `max_i P_ii <=1/32`, then some physical coordinate satisfies

`r_i := ||A e_i||_2 > rho ell`,

where

`rho = 1/(39 sqrt(32)) = 1/(156 sqrt(2))`.

Write `r_i^2=a^2+||b||^2`. Split at the scale-free threshold `|a| = r_i/2`.

### Diagonal-heavy branch

If `|a| >= r_i/2`, then

`q=||b||/|a| <= sqrt(3)`

and hence

`alpha(q) >= alpha_0 := 4/(sqrt(7)+sqrt(3))^2 = 0.20871215252207995...`.

Also

`|a| >= rho ell/2`,

so the scale-invariant Schur product obeys

`alpha(q)|a| >= c_0 ell`,

with

`c_0 := alpha_0 rho/2 = 0.0004730185203987298...`.

### Diagonal-light branch

If `|a| < r_i/2`, then

`||b|| > (sqrt(3)/2) r_i > gamma_0 ell`,

where

`gamma_0 := sqrt(3) rho/2 = 0.003925464331383298...`.

Thus every spectral-window failure produces, in original coordinates, either a Schur pivot with a **uniform product scale** `alpha|a| >= c_0 ell`, or a singleton-versus-rest cross bank with singular value `||b||>gamma_0 ell`.

This strictly refines the earlier coarse `|A_ii|>1/312 or ||A_-i,i||>1/312` split because the first branch now carries the exact spectral-count survival needed after completing the square.

## 3. Actual application of fleet04/B18: extra large eigenvalues do not blow up the constant

The fleet04/B18 theorem states: if `R` has density cap `M` and, conditionally on `R=r`, the scalar `V` has density cap one, then

`||p_{R+aV^2}||_infinity <= 2 sqrt(M/|a|)`.

For the physical Schur decomposition,

`Q = a (X_i + b^T X_{-i}/a)^2 + X_{-i}^T S X_{-i}`.

Because `X_i` is independent of `X_{-i}` with density cap one, conditioning on the Schur remainder only mixes translates of the `X_i` density, so the required conditional density cap is indeed one. This is a genuine application of the partner theorem to the present inequality, not merely a citation.

Now suppose `A` has `m>=4` eigenvalues of modulus at least `ell`, the spectral-window gate fails, and the heavy row lies in the diagonal-heavy branch. Theorem 1 gives at least `m-1>=3` eigenvalues of `S` of modulus at least

`ell' = alpha(q) ell`.

If a bound

`||p_{X_{-i}^T S X_{-i}}||_infinity <= B/ell'`

is available for that residual instance (from a diffuse-window terminal theorem, or inductively from the same universal three-eigenvalue theorem), then fleet04/B18 gives

`||p_Q||_infinity`

` <= 2 sqrt( (B/ell')/|a| )`

` <= (2/ell) sqrt(B/c_0)`.

Define the normalized recurrence

`T(B)=2 sqrt(B/c_0)`.

Its positive fixed point is

`B_* = 4/c_0 = 8/(alpha_0 rho) = 8456.328510410563...`.

Equivalently `T(B)=sqrt(B_* B)`, and therefore

`T^k(B)=B_*^(1-2^{-k}) B^(2^{-k}) <= max(B_*,B)`.

### Consequence: no constant explosion from arbitrarily many extra large eigenvalues

Along any chain of diagonal-heavy Schur eliminations, each elimination removes at most one guaranteed large eigenvalue and rescales the surviving threshold by `alpha(q)`, but **the normalized density constant never exceeds `max(B_*,B_terminal)`**, independent of the number of additional large eigenvalues.

Hence arbitrary extra large eigenvalues of either sign are not an independent source of constant blow-up on this branch. They can be stripped one at a time until either:

1. a diffuse spectral-window certificate terminates the chain (the existing terminal constant is `<66.546`, hence the outer chain is bounded by `B_*`);
2. exactly three guaranteed large eigenvalues remain, leaving the true base target;
3. a diagonal-light heavy row appears, in which case the unresolved obstruction is transferred to a physical cross bank of size `>gamma_0` times the current spectral scale.

This is the precise additional-eigenvalue reduction obtained in this run.

## 4. Interaction with the newest four-heavy determinant-core result

The fresh fleet02/B07 theorem compresses one q=0 ridge failure to at most four determinant-heavy physical rows. The present theorem gives a complementary rule for any such candidate row once an absolute physical row scale is certified: if its diagonal is at least half its row norm, Schur elimination preserves the large-eigenvalue count quantitatively and costs at most the fixed recurrence above; otherwise the row is necessarily cross-dominated and should be paid by grouped/cross smoothing rather than by another reciprocal principal minor.

No claim is made here that the DPP inclusion-marginal threshold alone already supplies the absolute `rho ell` row scale; that conversion remains a separate obligation.

## 5. What remains unpaid

Full QFORM is still OPEN.

This run removes a specific source of uncertainty: **additional large eigenvalues do not cause an unbounded recursive loss in the diagonal-heavy high-leverage branch.** The surviving target-level debt is now concentrated in the diagonal-light heavy-row/cross-bank branch, especially at the base exact-three level.

For exact three large eigenvalues, Theorem 1 also isolates the sign topology after a physical pivot, but it does not by itself prove a density bound for the resulting two-large-eigenvalue Schur form.

A next useful implication is therefore:

`QFORM-CROSS-DOMINATED-HEAVY-ROW-CLOSURE-v2`: from `||b||>gamma_0 ell` plus the remaining signed Schur spectral information, derive a grouped-coordinate smoothing bound without paying a reciprocal single coefficient/minor. The newest fleet01/B19 one-cross-singular quarter-moment theorem and fleet02/B07 four-heavy DPP reduction are compatible inputs.

Continuity: the present Schur recurrence transfers an `L^infinity` density bound; it does not by itself upgrade continuity. Continuity is inherited only when the terminal residual theorem and the square-smoothing passage are separately justified in a continuity-preserving form. Therefore this report claims essential boundedness only for the recurrence statement.

## 6. Corrections respected

No pointwise law-uniform van-der-Corput/Fresnel estimate is used. No post-rotation independence is assumed. No fiber-sup dimension-free claim, single-good-minor inference, conditional-cap-as-independence substitution, or Monte Carlo evidence is used. All conditioning occurs in original coordinates.
