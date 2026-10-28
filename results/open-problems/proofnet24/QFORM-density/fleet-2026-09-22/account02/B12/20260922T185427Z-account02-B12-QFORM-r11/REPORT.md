SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B12, 2026-09-22T18:54:27Z.
attacking: lossless singular-value inheritance through physical Schur elimination, then a dimension-free recurrence showing arbitrarily many additional large eigenvalues do not worsen a solved terminal branch.

# account02/B12 — lossless Schur peeling for arbitrary additional large eigenvalues

Run: `20260922T185427Z-account02-B12-QFORM-r11`  
Assignment: **Additional eigenvalue control**  
Status: `ESSENTIAL_SUPPORTING_REDUCTION / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

The full target remains open: for independent real coordinates with densities at most one and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal density bound for `X^T A X`, or give a valid counterexample. No rotation-independence assumption is used below.

## 1. Fresh sources and completed inputs actually used


The designated same-role partner result was read in full from account03/B12:

* account03/B12 `QFORM-SIGNED-SCHUR-EXTRA-EIGENVALUE-RECURRENCE`, canonical `yspennstate/math-open-problems@c10963494049ba2708f33e8533198ac38fc2ba31`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T164418Z-qform-eigenvalue-r13/REPORT.md`. It proves signed Schur spectral-count inheritance at the degraded scale `alpha(q) ell` and, on the high-leverage diagonal-heavy branch, the fixed-point recurrence constant `8456.328510410563...`.

I also read the complete dependent square-smoothing theorem used by that partner:

* account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`. If `R` has density cap `M`, and conditionally on `R=r` the scalar `V_r` has density cap one, then `R+aV_R^2` has density cap at most `2 sqrt(M/|a|)`.

A concurrent account03/B09 report records the already-known scalar singular-value inheritance as an input. The result below therefore does not claim novelty for that scalar inequality itself; the new B12 contribution is the exact block form, its use to remove the partner's `alpha(q)` loss from absolute-eigenvalue peeling, and the resulting tunable no-blowup recurrence for arbitrary extra large eigenvalues.

Corrections respected: no arbitrary-joint coarea `2/3` premise, no worst normalized scalar fiber, no post-rotation independence, no fixed good minor, no conditional-cap-as-independence substitution, and no pointwise law-uniform Fresnel decay.

## 2. Lossless block-Schur singular-value inheritance

Let a real symmetric matrix be partitioned in **original coordinates** as

`A = [[B,E],[E^T,C]]`,

where `B` is an invertible `r x r` physical principal block. Define its Schur complement

`S = C - E^T B^(-1) E`.

Write singular values in decreasing order as `s_1 >= s_2 >= ...`.

### Theorem 2.1 — `QFORM-SCHUR-SINGULAR-INHERITANCE-BLOCK-v1`

For every `j=1,...,n-r`,

`boxed:  s_j(S) >= s_(j+r)(A).`

In particular, if `A` has at least `m` eigenvalues of modulus at least `ell` and `m>r`, then `S` has at least `m-r` eigenvalues of modulus at least **the same scale `ell`**. There is no condition-number, shear, sign, or row-norm loss.

### Proof

Set

`U = [[B],[E^T]]`, an `n x r` matrix.

Then exactly

`U B^(-1) U^T = [[B,E],[E^T,E^T B^(-1)E]]`.

Hence

`A = diag(0_r,S) + U B^(-1) U^T`.                                      (2.1)

The second term has rank at most `r`. The standard rank-`r` singular-value inequality gives

`s_(j+r)(D+R) <= s_j(D)` whenever `rank(R)<=r`.

Apply it to `D=diag(0_r,S)` and `R=U B^(-1)U^T`. The nonzero singular values of `D` are exactly those of `S`, so

`s_(j+r)(A) <= s_j(S)`,

as claimed. QED.

### Scalar corollary

For a nonzero physical scalar pivot

`A=[[a,b^T],[b,C]]`, `S=C-bb^T/a`,

one has

`boxed: s_j(S)>=s_(j+1)(A).`                                            (2.2)

Thus if `A` has `m` eigenvalues of modulus at least `ell`, every nonzero scalar Schur elimination leaves `m-1` eigenvalues of modulus at least `ell` in the residual, irrespective of `q=||b||/|a|`.

This is deliberately an **unsigned** theorem. The partner account03/B12 signed theorem remains useful when one must know which sign survives; its `alpha(q)` loss is the price of retaining signed threshold counts. For the owner's target, whose hypothesis counts `|lambda|`, the scale loss is unnecessary during extra-eigenvalue peeling.

The factor one is sharp: for block diagonal `A=diag(B,S)`, equality can occur in the interlacing bound.

## 3. Source-valid square smoothing after one lossless peel

Take the scalar case in original coordinates. Completing the physical variable gives

`X^T A X = a ( X_i + b^T X_-i/a )^2 + X_-i^T S X_-i`.                 (3.1)

No spectral rotation of the product law occurs. Conditional on the Schur remainder, the shifted scalar variable is a mixture of translations of the original `X_i` density and therefore still has density cap one. Account04/B18 applies exactly.

Suppose the residual law has density cap

`||p_S||_infinity <= B/ell`,                                           (3.2)

and the physical pivot obeys

`|a| >= delta ell`, `delta>0`.                                         (3.3)

Then

`||p_A||_infinity <= (2/ell) sqrt(B/delta).`                            (3.4)

Define

`T_delta(B)=2 sqrt(B/delta)` and `F_delta=4/delta`.

Then `T_delta(B)=sqrt(F_delta B)` and exactly

`T_delta^k(B)=F_delta^(1-2^(-k)) B^(2^(-k)) <= max(F_delta,B)`.          (3.5)

Thus **any number of heavy physical scalar peels costs only one fixed constant**, not a product of constants.

## 4. Arbitrarily many additional large eigenvalues can be stripped without spectral-scale decay

Consider a chain of original-coordinate scalar Schur complements

`A^(0)=A, A^(1),...,A^(k)`

with pivots `a_0,...,a_(k-1)` satisfying

`|a_j|>=delta ell` for every `j`.

If `A` initially has at least `k+3` eigenvalues of modulus at least `ell`, Theorem 2.1 gives inductively

`A^(j)` has at least `k+3-j` eigenvalues of modulus at least `ell`.       (4.1)

Hence the terminal residual `A^(k)` is still inside the three-large-eigenvalue target at the **original scale**, with every unpeeled smaller/larger eigenvalue and every sign retained in the actual residual matrix.

If a terminal theorem gives

`||p_(A^(k))||_infinity <= B_terminal/ell`,

then repeated dependent square smoothing gives

`boxed:
 ||p_A||_infinity <= max(B_terminal,4/delta)/ell.
`                                                                              (4.2)

This is the promised additional-eigenvalue stability statement. It does not assume that the quadratic remainder is independent of the completed square. The only independence used is the original coordinate independence needed for the conditional translate cap in account04/B18.

## 5. Apply the designated partner's high-leverage dichotomy: remove the `alpha(q)` loss

The completed account03/B12 partner theorem supplies the following source-valid branch at scale `ell`. If the `1/39` diffuse spectral-window gate fails, some physical row has

`r_i:=||A e_i|| > rho ell`,

with

`rho=1/(156 sqrt(2)).`                                                  (5.1)

Write that row as `(a,b)` so that `r_i^2=a^2+||b||^2`.

For any free threshold `theta in (0,1)`, there is an exhaustive original-coordinate dichotomy:

* **heavy pivot:** `|a|>=theta r_i`, hence `|a|>theta rho ell`;
* **cross dominated:** `|a|<theta r_i`, hence
  `||b||>sqrt(1-theta^2) rho ell`.

On the heavy branch use `delta=theta rho` in (4.2). Therefore arbitrarily many additional large eigenvalues can be peeled with normalized constant

`boxed: F_theta = 4/(theta rho) = 624 sqrt(2)/theta.`                    (5.2)

The cross branch is transferred, without any reciprocal single-entry selection, to the aggregate singleton-versus-rest bank lower bound

`boxed: ||b|| > gamma_theta ell,
 gamma_theta = rho sqrt(1-theta^2).`                                    (5.3)

This one-parameter form is useful to future proof assembly because `theta` can be optimized against the eventual cross-bank payment instead of being frozen before that payment is known.

### Partner's historical split `theta=1/2`

At `theta=1/2`,

`delta=rho/2=1/(312 sqrt(2))`,

so

`F_(1/2)=8/rho=1248 sqrt(2)=1764.9385258416228...`.                     (5.4)

The partner's signed/shear recurrence used

`alpha_0=4/(sqrt(7)+sqrt(3))^2=0.20871215252207995...`

and fixed point

`8/(alpha_0 rho)=8456.328510410563...`.

Thus, when only absolute large-eigenvalue counts are needed, the present lossless Schur argument improves that recursive fixed-point constant by the exact factor

`1/alpha_0=4.79128784747792...`.                                        (5.5)

This comparison does **not** invalidate the partner's signed theorem; it separates two different needs. Signed topology may still require the shear estimate. Extra-eigenvalue peeling for the owner's absolute-value hypothesis does not.

## 6. Conditional end-to-end reduction and first unpaid implication

A compact conditional route is now:

1. Use the proved spectral-window theorem whenever its diffuse gate holds.
2. Otherwise use the partner's heavy-row certificate `r_i>rho ell`.
3. Choose a threshold `theta`.
4. If the row is pivot-heavy and there are more than three guaranteed large eigenvalues, peel it. Theorem 2.1 loses one large direction but **no spectral scale**; account04/B18 maps density constants by `T_delta`, whose arbitrary-depth fixed point is (5.2).
5. Continue until either a proved terminal theorem fires, exactly three large directions remain, or a cross-dominated row (5.3) appears.
6. Therefore arbitrary additional large eigenvalues of either sign are not an independent source of blow-up on the pivot-heavy branch.

The first unpaid implication is now sharply confined to the terminal/exact-three geometry and the cross-dominated aggregate branch. In particular, one still needs a product-preserving estimate for

`||b||>gamma_theta ell`

that does not replace the whole bank by one tiny coefficient or a rotated independent coordinate. The current full-matrix pair theorem pays a uniformly strong physical pair but the singleton-plus-two-banks family shows such a pair need not exist. The recent one-strong-cross half-Riesz branch is another compatible target.

This report does **not** prove full QFORM and does not prove continuity. It proves an exact matrix reduction and a density-stability recurrence which preserve every additional eigenvalue in the physical residual and eliminate recursive scale loss from the diagonal-heavy extra-eigenvalue branch.

## 7. Computational checks

A deterministic checker bundled with this report verifies:

* random scalar and block Schur instances satisfy `s_j(S)>=s_(j+r)(A)`;
* the exact partner constants `rho`, `alpha_0`, old/new fixed points and improvement ratio;
* the closed form `T^k(B)=F^(1-2^-k)B^(2^-k)` numerically across several `k`.

The checker is only arithmetic/testing support; the theorem proof is the rank decomposition (2.1) plus the cited dependent square-smoothing lemma.
