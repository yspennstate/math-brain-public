SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-24T09:28:09Z.
attacking: partner account03/B06 r56 global-null endpoint by product-preserving sparse-kernel deletion, with a sharp spectral-loss calculation and a real pinned-Theorem-A density payment.

# account02/B06 — sparse-kernel product deletion and sharp factor-three quotient

Programme: `QFORM-DENSITY-3EIG-20260922`. Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.


Sources actually consumed:

- designated partner account03/B06 r56, canonical commit `24fd6e4552117b2dd56c62db304883d5360b59f2`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T090040Z-account03-B06-qform-r56/REPORT.md`;
- pinned owner-required source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`;
- in particular the completed localized three-dimensional Theorem A from `COUNTEREXAMPLE_SEARCH.md`: if a three-coordinate quadratic matrix has all eigenvalue magnitudes at least `sigma`, then for arbitrary independent cap-one inputs (linear shifts allowed) its output density is at most `6 sqrt(pi)/sigma`.

## 1. First unpaid implication

Partner r56 proves that every **exact singular** localized three-hub face is either already density-paid by a product-preserving receiver or yields an actual global null vector supported on the three literal hub coordinates. Its stated next debt is to use this global-null certificate without replacing the hub triple by a dependent two-dimensional rotated quotient.

The new point here is that no dependent quotient is needed. One can delete a small original-coordinate bank by conditioning and an exact shear. The same operation preserves three large singular values up to a sharp factor at most three.

## 2. `QFORM-SPARSE-KERNEL-PRODUCT-DELETION-v1`

Let `A=A^T` be an `n x n` real symmetric matrix and let `K subset ker A` be a `d`-dimensional kernel subspace supported on one set `H` of **literal original coordinates**, with

`1 <= d <= |H| = m <= 3`.

Let `W` be an `n x d` matrix with orthonormal columns spanning `K`. Then there is a subset `L subset H`, `|L|=d`, with complement `R`, such that, writing

`C=A_RR`,

one has all of the following.

### (i) Exact source-preserving shear factorisation

After ordering coordinates as `L,R`, define

`T = W_R W_L^{-1}`,  `P=[-T  I_R]`.

Then

`A=P^T C P`.

Consequently for every fixed value `x_L` of the original coordinates in `L`,

`x^T A x = (x_R-Tx_L)^T C (x_R-Tx_L)`.

Thus conditioning on `X_L=x_L` leaves the coordinates of `X_R-Tx_L` independent, with exactly the original one-dimensional densities translated by deterministic constants. Every density cap `<=1` is preserved. No spectral rotation and no conditional projection-density bound are used.

### (ii) Quantitative three-spectrum preservation

The coordinate set `L` can be chosen so that

`sigma_min(W_L)^2 >= 1/binom(m,d)`.

For that choice,

`||P||_op^2 = 1/sigma_min(W_L)^2 <= binom(m,d) <=3`.

Therefore for every singular-value index `k`,

`s_k(C) >= s_k(A)/binom(m,d)`.

In particular, if `A` has at least three eigenvalues of modulus at least one, then `C` has at least three eigenvalues of modulus at least

`1/binom(m,d) >= 1/3`.

This is a one-step product-preserving reduction from a sparse-kernel target to the same rough-input target in fewer original coordinates, with a universal spectral-scale loss no worse than three.

## 3. Proof

Because the columns of `W` are orthonormal and vanish outside `H`, Cauchy--Binet gives

`sum_{L subset H, |L|=d} det(W_L)^2 = det(W_H^T W_H)=det(W^T W)=1`.

Hence some `L` satisfies

`det(W_L)^2 >= 1/binom(m,d)`.

Every singular value of a row submatrix of an orthonormal-column matrix is at most one. Therefore

`det(W_L)^2 = product_j sigma_j(W_L)^2 <= sigma_min(W_L)^2`,

which proves the selection bound.

Now order coordinates as `L,R` and write

`A=[[A_LL,B^T],[B,C]]`, `W=[W_L;W_R]`.

The equation `AW=0` gives

`B W_L + C W_R=0`,

so, since `W_L` is invertible,

`B=-C W_R W_L^{-1}=-CT`.

The upper block equation gives

`A_LL W_L + B^T W_R=0`,

hence

`A_LL=T^T C T`.

Therefore

`A=[[T^TCT,-T^TC],[-CT,C]]=P^T C P`,

with `P=[-T I]`, proving the exact shear representation.

For the norm, orthonormality gives

`W_L^T W_L + W_R^T W_R=I_d`.

Thus

`T^T T = W_L^{-T}(I-W_L^T W_L)W_L^{-1}`,

so

`1+||T||^2 = ||W_L^{-1}||^2 = 1/sigma_min(W_L)^2`.

Since `P P^T=I+TT^T`,

`||P||^2=1/sigma_min(W_L)^2 <= binom(m,d)`.

Finally the standard singular-value product inequality gives

`s_k(A)=s_k(P^T C P) <= ||P||^2 s_k(C)`.

This proves the spectrum statement. Because `A` and `C` are symmetric, singular values are absolute eigenvalue magnitudes.

## 4. Direct application to partner r56

In every r56 exact-global-null branch there is a nonzero null vector `w` supported on the literal three-hub bank. Take `K=span{w}`. Then `d=1`, `m<=3`, and some literal hub coordinate `h` satisfies `|w_h|^2>=1/3`.

Writing `C=A_{-h,-h}`, the theorem gives the particularly transparent formula

`A=R_h^T C R_h`,

where `R_h` subtracts `(w_{-h}/w_h) x_h` from the remaining coordinates, and

`s_3(C) >= |w_h|^2 s_3(A) >= 1/3`.

Conditioning on **that original coordinate** `X_h=t` turns the full quadratic output into the quadratic form with matrix `C` evaluated on independently translated remaining coordinates. This pays the exact product-provenance part of r56's `GLOBALNULL-PRODUCT-QUOTIENT` debt: the quotient need not be represented by a dependent two-dimensional projection of the hub triple.

What remains is analytic/global rather than a provenance problem: for arbitrary remaining dimension one still needs a universal bound for a matrix with three eigenvalues at scale `1/3`. Thus this lemma is a structural compiler, not the full theorem.

## 5. A real target inequality from the pinned completed result

The reduction becomes a complete target-level payment in dimension four. Let `n=4`, suppose `A` has at least three eigenvalues of modulus at least one, and suppose `A` has a nonzero null vector supported on at most three original coordinates. Since rank `A>=3`, the relevant supported kernel is one-dimensional. Choose `h` as above.

Then `C=A_{-h,-h}` is `3 x 3` and every eigenvalue of `C` has modulus at least `1/3`. For every conditioning value `X_h=t`, the translated remaining variables are independent with density caps at most one. The completed pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A therefore gives

`||p_{Q | X_h=t}||_infinity <= 6 sqrt(pi)/(1/3)=18 sqrt(pi)`.

Averaging the **actual conditional densities** rather than taking a curved spectral-fiber supremum gives

`boxed(||p_Q||_infinity <= 18 sqrt(pi) = 31.904169... )`.

This is a genuine QFORM-target branch with arbitrary independent cap-one laws and no support, moment, log-concavity, or continuity assumptions.

## 6. Sharpness of the factor three and obstruction to a stronger compiler

The factor three in the sparse-null spectral transfer is sharp. Consider

`A_* = [[2/3,-1/3,-1/3,0],[-1/3,2/3,-1/3,0],[-1/3,-1/3,2/3,0],[0,0,0,1]]`.

This is the orthogonal projection onto the sum-zero plane of the first three coordinates, direct-summed with the fourth coordinate. Hence

`spec(A_*)={1,1,1,0}`

and

`w=(1,1,1,0)/sqrt(3)`

is a literal three-coordinate-supported null vector. Deleting **any** one of the first three coordinates leaves

`C_*=[[2/3,-1/3,0],[-1/3,2/3,0],[0,0,1]]`

up to permutation, with

`spec(C_*)={1,1,1/3}`.

Therefore no argument that only chooses one coordinate from the support of the sparse null vector can improve the universal spectral retention factor `1/3`.

This example is not a QFORM counterexample. It is itself an exact target matrix, and the preceding pinned-Theorem-A application gives `||p_{X^T A_* X}||_infinity <=18 sqrt(pi)` for every independent cap-one input law.

## 7. Why this differs from the forbidden post-rotation quotient

A natural but dangerous formulation of the r56 null branch is: project the three hub variables orthogonally to the null direction, obtain a two-dimensional random vector, and then try to use that projected vector as if its coordinates were independent. They are not.

The present compiler instead conditions on `d` literal original coordinates and uses the identity `A=P^T C P`. For each conditioning value the remaining random coordinates are exactly independent translations of original coordinates. All weights are therefore retained by ordinary Fubini averaging. The only cost is the deterministic spectral factor `binom(m,d)<=3`, which is sharp.

## 8. First unpaid implication after this run

`QFORM-R56-NEARSINGULAR-SCALE-STABLE-COMPILER-v1`:

Use the exact singular compiler of partner r56 together with the present sparse-kernel deletion to handle the transition where the three-hub block has small but nonzero determinant. The required statement must aggregate the kernel-area / determinant-minor bank before any reciprocal hub determinant and must not treat a small matrix perturbation as a small random quadratic perturbation on arbitrary unbounded inputs.

A second, now sharply isolated, assembly issue is to prevent repeated factor-three spectral losses if sparse-kernel deletion is invoked recursively on changing hub triples. The present theorem removes the product-provenance obstruction in one shot for any kernel subspace supported on a fixed three-coordinate bank, but it does not by itself prove a dimension-independent global recursion.

## 9. Checks and status

A fixed-seed diagnostic tested 3,000 random supported-kernel factorizations (`m=3`, `d=1,2`, ambient dimensions 5,7,9). Maximum `||AW||_F` was `5.95e-16`; the norm and singular-value inequalities held in every case. These are sanity checks only; Sections 2--3 are exact algebra.

**Full QFORM:** OPEN.  
**New result:** proved supporting structural lemma plus complete four-dimensional target payment.  
**Continuity:** not asserted.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.
