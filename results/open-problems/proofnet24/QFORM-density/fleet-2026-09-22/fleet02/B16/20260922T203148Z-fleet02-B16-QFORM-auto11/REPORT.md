SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-22T20:31:48Z.
attacking: weighted unnormalized projection disintegration—can the partner's ambiguity-kernel L2 budget be assembled by a many-coordinate mixed Brascamp--Lieb estimate without normalizing fibers?

# fleet02/B16 — mixed ambiguity/section-mass BL barrier, and the grouped-bank curved payment that escapes it

**Run:** `20260922T203148Z-fleet02-B16-QFORM-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Method:** complementary constructions/source-valid counterexamples  
**Status:** `NEW_CONDITIONAL_LEMMA + REFUTED_INTERMEDIATE_MECHANISM + TARGET-VALID FAMILY PAID / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full target remains open: arbitrary independent real coordinates with densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, support, log-concavity, rotation-independence, or conditional-density-cap assumption is introduced.


## 1. Completed designated partner actually applied

I use fleet03/B16 run `20260922T195823Z-fleet03-B16-QFORM-r15`, canonical report

`yspennstate/math-open-problems@c6601cc34ac9ca1f485f8c20dc4a28c909580817:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260922T195823Z-fleet03-B16-QFORM-r15/REPORT.md`,

with correction event `QFORM-SYMMETRIC-THREE-AMBIGUITY-BL-FAIL-v1` at `yspennstate/math-research-brain@255dc04085fefae8cfd62c607f10dbc40db9994d`.

For every cap-one probability density `f`, define

`k_f(u,v)=1/2 f((v+u)/2)f((v-u)/2)`,

`K_f(u,xi)=int exp(i xi v) k_f(u,v) dv`,

`q_f(u)=K_f(u,0)=int f(x)f(x-u)dx`.

The partner proves

`0<=q_f<=1`, `int q_f=1`, `|K_f|<=q_f`, and `int int |K_f|^p <= pi` for every `p>=2`; in particular `||K_f||_2^2<=pi`. For independent `X_j` and symmetric `A`, quadratic decoupling is the exact unnormalized identity

`|phi_A(t)|^2 = int_(R^n) prod_j K_j(u_j,t(Au)_j) du`.             (1.1)

The partner also proves that selecting only three symmetric physical maps gives an infinite codimension-one BL constant. The first unpaid implication attacked here is the natural repair it left open: keep the `q_j` fiber masses and distribute only a fractional amount of each coordinate through the two-dimensional ambiguity map.

## 2. Mixed ambiguity/section-mass BL interface

For `0<=theta_j<=1`, put

`P_j u = u_j`,

`L_j u = (u_j,(Au)_j) in R^2`,

and `Theta=sum_j theta_j`.

Since `|K_j|<=q_j`, pointwise

`|K_j(u_j,t(Au)_j)| <= |K_j(u_j,t(Au)_j)|^(theta_j) q_j(u_j)^(1-theta_j)`.  (2.1)

Let `B_theta(A)` denote the Brascamp--Lieb constant of the datum consisting of

* map `L_j:R^n->R^2` with exponent `theta_j/2`, and
* map `P_j:R^n->R` with exponent `1-theta_j`.

The scaling identity is automatic:

`sum_j [2(theta_j/2)+(1-theta_j)] = n`.                         (2.2)

### Lemma 2.1 — `QFORM-MIXED-AMBIGUITY-BL-SUFFICIENT-v1`

If `B_theta(A)<infinity`, then for every `t!=0`,

`|phi_A(t)|^2 <= B_theta(A) pi^(Theta/2) |t|^(-Theta/2)`,          (2.3)

hence

`|phi_A(t)| <= B_theta(A)^(1/2) pi^(Theta/4) |t|^(-Theta/4)`.     (2.4)

If, in addition, `Theta>4`, then `phi_A in L^1(R)` and

`||p_Q||_infinity <= 1/pi + B_theta(A)^(1/2) pi^(Theta/4-1)/(Theta/4-1)`.  (2.5)

#### Proof

Write `F_j=|K_j|^2` and `G_j=q_j`. By the partner theorem, `int F_j<=pi` and `int G_j=1`. Apply BL to (2.1). To expose the `t` scaling, keep the fixed map `L_j` and replace `F_j(x,y)` by `F_j(x,ty)`, whose `L1(R^2)` norm is `|t|^-1 int F_j`. Therefore

`|phi_A(t)|^2 <= B_theta(A) prod_j (pi |t|^-1)^(theta_j/2) = B_theta(A) pi^(Theta/2)|t|^(-Theta/2)`.

Taking square roots proves (2.4). Since `|phi_A(t)|<=1` for `|t|<=1`, integrate (2.4) over `|t|>=1`; the tail is finite exactly when `Theta/4>1`, giving (2.5) by Fourier inversion. QED.

This is a source-valid sufficient interface: it never divides by `q_j`, never asserts independence after rotation, and preserves the actual product-source weights.

## 3. Exact target-family obstruction at the critical exponent

For every integer `m>=2`, define

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`,               (3.1)

where `J_m` is the all-ones matrix. Its nonzero spectrum is exactly `{1,1,-1}`, so every `A_m` lies in the target class.

Partition the coordinates into the singleton `{0}`, a positive bank `B_+` of size `m`, and a negative bank `B_-` of size `m`.

### Theorem 3.1 — `QFORM-MIXED-AMBIGUITY-BL-BANK-BARRIER-v1`

For `A=A_m`, if the mixed BL datum of Section 2 has finite constant, then necessarily

`theta_0=0`, `sum_(j in B_+) theta_j <=2`, `sum_(j in B_-) theta_j<=2`.  (3.2)

Consequently

`Theta<=4`.                                                        (3.3)

Therefore the entire class of absolute mixed `q_j`/ambiguity-`L2` BL assemblies from Lemma 2.1 reaches at best the borderline

`|phi_A(t)| <= const |t|^-1`,                                      (3.4)

and cannot prove a uniform `L1_t` characteristic-function estimate even on this exact rank-three target family.

#### Proof

A finite BL constant obeys the standard necessary subspace inequalities

`dim V <= sum_j (theta_j/2) dim L_j(V) + sum_j (1-theta_j) dim P_j(V)` for every linear subspace `V`.  (3.5)

First take `V_0=span(e_0)`. Because `A_m` is block diagonal, every map outside coordinate `0` vanishes on `V_0`, while `dim P_0(V_0)=dim L_0(V_0)=1`. Thus (3.5) gives

`1 <= (1-theta_0)+theta_0/2 = 1-theta_0/2`,

so `theta_0=0`.

Next let

`V_+={u:supp(u) subset B_+, sum_(j in B_+)u_j=0}`.

Then `dim V_+=m-1`. On this subspace `(A_m u)_j=0` for every `j in B_+`; hence for each such `j`, `P_j(V_+)` and `L_j(V_+)` are both one-dimensional. All maps outside the positive bank vanish. Therefore

`m-1 <= sum_(j in B_+) [(1-theta_j)+theta_j/2] = m-(1/2)sum_(j in B_+)theta_j`,

which yields `sum_(B_+)theta_j<=2`. The same mean-zero subspace in `B_-` gives the negative-bank bound. Summing proves (3.3). Combining with (2.4) gives (3.4). QED.

### Why `p>2` ambiguity budgets do not rescue this absolute BL interpolation

The partner supplies `int|K|^p<=pi` for every `p>=2`, but if one splits

`|K| <= |K|^theta q^(1-theta)`

and feeds the first factor through an `L^p(R^2)` norm, its BL exponent is `theta/p`; the per-coordinate scaling contribution becomes

`2 theta/p + (1-theta) <=1`,

with equality for a nonzero ambiguity share only at `p=2`. Replacing the `L1` norm of `q` by any `L^r`, `r>1`, decreases scaling further. Hence the `p=2`, `q in L1` mixed datum is already the scale-maximal absolute-norm version of this repair.

This is a genuine mechanism obstruction, not a counterexample to QFORM.

## 4. The same family is uniformly paid by grouping product coordinates before curvature

The obstruction above says the source coordinates cannot be charged one-by-one through an absolute BL norm. It does **not** say the family has large output density.

Write, for independent cap-one input coordinates,

`Y_+ = m^(-1/2) sum_(j in B_+) X_j`,

`Y_- = m^(-1/2) sum_(j in B_-) X_j`.

Then

`Q_m = X_0^2 + Y_+^2 - Y_-^2`.                                    (4.1)

Because the three source groups are disjoint, `X_0,Y_+,Y_-` are genuinely independent. The standard Ball--Rogozin one-dimensional product-projection theorem gives

`||p_(Y_+)||_infinity <= sqrt(2)`                                 (4.2)

(and likewise for `Y_-`). A completed source-pinned use of exactly this theorem is fleet03/B06, `yspennstate/math-open-problems@99f0eb89b7b1ad3ef3f225460fb08d4d22c19a75:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T172229Z-fleet03-B06-qform-r14/REPORT.md`.

If a scalar `U` has density at most `M`, then for `s>0`

`p_(U^2)(s) = [p_U(sqrt(s))+p_U(-sqrt(s))]/(2sqrt(s)) <= M/sqrt(s)`.  (4.3)

Thus

`p_(X_0^2)(s)<=s^-1/2`, `p_(Y_+^2)(s)<=sqrt(2)s^-1/2`.              (4.4)

Their convolution satisfies, for every `r>0`,

`p_(X_0^2+Y_+^2)(r) <= sqrt(2) int_0^r [s(r-s)]^-1/2 ds = pi sqrt(2)`.  (4.5)

Finally `-Y_-^2` is independent, so convolution with its probability law cannot increase an `L-infinity` norm. Hence

`boxed(||p_(Q_m)||_infinity <= pi sqrt(2) = 4.442882938158366...)`   (4.6)

for every `m>=2` and every independent cap-one source law.

### Corollary 4.1 — `QFORM-DISJOINT-BANK-CURVED-PROJECTION-v1`

The harmonic bank family that blocks the mixed ambiguity/section-mass BL route is nevertheless uniformly controlled once the entire positive bank is first aggregated through the actual bounded-density product projection and only then sent through the curved square map. This uses genuine source-group independence only where it actually exists; it does not pretend arbitrary spectral coordinates are independent.

## 5. What changed and next unpaid implication

The designated partner's unnormalized ambiguity kernel remains the correct primitive: it avoids the divergent normalized-fiber moments. This run proves, however, that the most natural fractional repair—interpolating each original coordinate between its one-dimensional section mass `q_j` and its two-dimensional ambiguity `L2` norm and then applying one absolute Brascamp--Lieb inequality—hits the exact `Theta=4` square-root threshold on a target-valid rank-three bank family.

The family itself is paid by a grouped projection theorem with constant `pi sqrt(2)`. Therefore the next source-valid bridge must **group source coordinates before the absolute multilinear payment**, or retain cancellation across the grouped bank. A viable successor should replace coordinatewise reciprocal/BL charging by a bank-level object whose norm is controlled by product projection (Ball--Rogozin / weighted affine-fiber BL) and which still couples to the quadratic phase before taking absolute values.

A precise next obligation is:

`QFORM-GROUPED-AMBIGUITY-BANK-BRIDGE-v1`: build an unnormalized ambiguity or oscillatory estimate for a normalized product projection `Y=w.X_I` as a whole, stable under conditioning on disjoint original-coordinate banks, and prove a three-large-eigenvalue structural synthesis that supplies enough grouped banks or an independent full-matrix exit. It must retain arbitrary extra spectrum and cannot normalize thin fibers.

Full QFORM and full continuity remain OPEN.
