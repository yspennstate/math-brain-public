# fleet01/B04 — effective-dimension-three ridge interpolation

**Run:** `20260922T171055Z-fleet01-B04-QFORM-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`; fresh owner control revision `2026-09-22.8`  
**Assignment:** Product Fourier rearrangement  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and conditional end-to-end route

The target remains open: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or produce a target-valid counterexample. Continuity is a separate requested conclusion.

This run changes mechanism from the preceding B04 local-face/fractional-potential arguments. It attacks the current full-matrix third-compound O0 branch directly through the **free exponent `q` in the regularized product-Fourier ridge inequality**.

The compact route is now:

1. fleet03/B07's third-compound identity reduces every target matrix to one of four aggregate overlap classes O0/O1/O2/O3;
2. in O0 there is an original-coordinate cross block `B` with
   `E_3(B)=e_3(s_1(B)^2,s_2(B)^2,...) >=1/256`;
3. the present theorem calibrates the ridge effective dimension to exactly three and pays the O0 branch whenever its maximum physical ridge leverage is `<3/4`, with an explicit continuous-density bound;
4. hence the unpaid O0 geometry has a genuinely high-leverage packet at effective dimension three, rather than merely the former `>1/2` gate failure;
5. the designated fleet02/B04 square-assisted theorem independently pays a square-dominant/diffuse-residual subbranch of this heavy geometry with an explicit bound `<812.564`;
6. what remains is the product-preserving payment of the `>=3/4` ridge-heavy packet and the O1/O2/O3 aggregate overlap classes.

No pointwise law-uniform quadratic-phase decay, post-rotation independence, fiber supremum, conditional projection cap, fixed-good-minor assertion, or finite-fragment localization is used.

## 2. Source-pinned completed inputs actually used

### 2.1 Full-form ridge theorem

Interactive canonical proof:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For any original-coordinate cross block `B=A[I,J]`, `gamma>0`, define

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`,
`theta=tr K_gamma`,
`D=det(I+BB^T/gamma^2)`.

If `1<=q<=2`, `max_i (K_gamma)_ii<=q/2`, and `theta>2q`, then the **full** quadratic form, retaining arbitrary self blocks and all outside couplings, has a continuous density satisfying

`||p_Q||_infinity
 <= e/(sqrt(2q) gamma) * theta/(theta-2q) * D^(-1/(2theta)).`   (2.1)

This is the product-space integrated Fourier input used below.

### 2.2 Third-compound O0 aggregate

fleet03/B07 canonical proof:

`yspennstate/math-open-problems@685929d9daee92a164dbf6ba6f9305d2e6550826`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T163733Z-fleet03-B07-qform-r12/REPORT.md`.

It proves

`sum_{|S|=|T|=3} det(A[S,T])^2=||wedge^3 A||_HS^2>=1`

and, in the O0 overlap class, produces an original-coordinate cross block `B` with

`E:=e_3(s_1(B)^2,s_2(B)^2,...)>=1/256`.                 (2.2)

Its previous O0 payment fixed `theta=8/3,q=1`, hence required `max diag K<=1/2`. The present argument removes that fixed choice.

### 2.3 Designated partner fleet02/B04

Latest completed partner handoff points to

`yspennstate/math-open-problems@f5f62136676a5334d5b00a7a25081b8436be9bf4`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260922T164653Z-d0a9bbf0/REPORT.md`.

Its theorem `QFORM-SQUARE-ASSISTED-TWO-DIRECTION-WINDOW39-v1` states that if

`Q=a(X+m(Y))^2+Y^T S Y`,

`X` is an untouched original cap-one coordinate, `S` has two eigenvalues of modulus at least `s`, and the physical leverage of the spectral projection onto `|mu|>=s/39` is at most `1/32`, then

`||p_Q||_infinity <=28.4310144633/sqrt(|a|s)`.            (2.3)

I apply (2.3) quantitatively in Section 6; it is not merely cited.

## 3. Elementary-symmetric concentration at effective dimension three

### Lemma 3.1

If `0<=k_j<=1` and `sum_j k_j=3`, then

`e_3(k_1,k_2,... )>=1`.                                    (3.1)

More generally, for `2<=tau<=3`, `sum k_j=tau` implies `e_3(k)>=tau-2`.

### Proof

Fix all variables except a pair `x,y`, and fix `x+y`. Writing the remaining variables as `z`,

`e_3(x,y,z)=xy sum z_j +(x+y)e_2(z)+e_3(z)`.

The coefficient of `xy` is nonnegative. For fixed `x+y` with `x,y in[0,1]`, `xy` is minimized by moving one member of the pair to `0` or `1`. Repeating this concentration operation leaves at most one fractional coordinate. For total mass `tau in[2,3]`, the extremal vector is, up to permutation,

`(1,1,tau-2,0,0,...)`,

whose third elementary symmetric polynomial is `tau-2`. This proves the claim. `QED`

## 4. Main theorem — adaptive ridge payment at effective dimension three

### Theorem 4.1 — `QFORM-O0-EFFECTIVE3-ADAPTIVE-Q-v1`

Let `B` be an original-coordinate cross block of a full quadratic form and put

`E=e_3(s_1(B)^2,s_2(B)^2,...)>0`.

Thus `rank B>=3`. Define the effective-dimension-three scale as follows.

* If `rank B>3`, let `gamma_*>0` be the unique number satisfying
  `tr K_{gamma_*}=3`.
* If `rank B=3`, interpret `gamma_*=0` as the limit `gamma downarrow0`, so `K_*` is the orthogonal projection onto `range(B)` and has trace three.

Set

`ell_*=max_i (K_*)_ii`.                                     (4.1)

If

`ell_*<3/4`,                                                  (4.2)

then the full quadratic form has a continuous density. With

`q_*=max(1,2 ell_*)`,                                        (4.3)

one has the explicit bound

`boxed(
 ||p_Q||_infinity
 <= [3e/(sqrt(2q_*) (3-2q_*))] E^(-1/6).
)`                                                            (4.4)

In particular,

* if `ell_*<=1/2`, then `||p_Q||_infinity <=(3e/sqrt2)E^(-1/6)`;
* if `ell_*<=2/3`, then
  `||p_Q||_infinity <=9e sqrt(3/8) E^(-1/6)`.

### Proof when `rank B>3`

At `gamma=gamma_*`, write

`x_j=s_j(B)^2/gamma^2`,
`k_j=x_j/(1+x_j)`.

Then `sum k_j=theta=3`. By Lemma 3.1,

`e_3(k)>=1`.                                                 (4.5)

Because `x_j>=k_j` coordinatewise,

`E/gamma^6=e_3(x)>=e_3(k)>=1`.                              (4.6)

Also

`D=product_j(1+x_j)>=e_3(x)=E/gamma^6`.                    (4.7)

Condition (4.2) gives `q_*<3/2`. The definition (4.3) gives `1<=q_*<3/2` and

`max diag K<=q_*/2`, `3>2q_*`,

so (2.1) applies at `theta=3`:

`||p_Q||_infinity
 <= e/(sqrt(2q_*)gamma) * 3/(3-2q_*) * D^(-1/6).`          (4.8)

Using (4.7),

`gamma^(-1)D^(-1/6)
 <=gamma^(-1)(E/gamma^6)^(-1/6)
 =E^(-1/6).`                                                 (4.9)

Substitution proves (4.4).

### Rank exactly three

Now `K_gamma` increases to the range projection `K_*` as `gamma downarrow0`, hence every physical diagonal of `K_gamma` is at most `ell_*`. Since `q_*<3/2`, for all sufficiently small positive `gamma`,

`theta(gamma)>2q_*`, `max diag K_gamma<=q_*/2`.

Apply (2.1) and let `gamma downarrow0`. Here

`D(gamma)=E gamma^(-6)(1+o(1))`,
`theta(gamma)->3`.

Therefore

`gamma^(-1)D(gamma)^(-1/(2theta(gamma))) -> E^(-1/6)`

(the extra exponent is `gamma^(3/theta-1)` and tends to one), while

`theta/(theta-2q_*) ->3/(3-2q_*)`.

Taking the infimum over sufficiently small `gamma` proves the same bound. The ridge theorem already supplies continuity for each such positive `gamma`; thus the conclusion is a continuous density. `QED`

## 5. Target-level consequence for the O0 overlap class

In fleet03/B07's O0 branch, (2.2) gives `E>=1/256`, hence

`E^(-1/6)<=256^(1/6)=2^(4/3)`.                              (5.1)

Theorem 4.1 therefore yields the following explicit payments:

`ell_*<=1/2  => ||p_Q||_infinity <14.531`,                  (5.2)

and

`ell_*<=2/3  => ||p_Q||_infinity <37.751`.                  (5.3)

More importantly, the theorem pays **every** O0 form with `ell_*<3/4`, with the parameterized constant (4.4). Thus the O0 branch formerly described only as “ridge gate fails, some leverage >1/2” can now be replaced by the sharper residual condition

`boxed( ell_*>=3/4 at effective dimension three. )`          (5.4)

Since `tr K_*=3`, there are at most four physical rows with leverage at least `3/4`. Hence the remaining O0 obstruction is a bounded-size high-leverage packet, not an arbitrary diffuse bank.

For finite `gamma_*` there is also the exact row-deletion determinant identity

`D_{-i}=D(1-(K_*)_ii)`,                                     (5.5)

obtained from the matrix determinant lemma. Thus a surviving heavy row with leverage at least `3/4` carries at least three quarters of the regularized determinant inclusion weight. This identity is recorded for the next grouped-coordinate conditioning step; it is not used to claim closure.

## 6. Actual application of the designated fleet02/B04 result

The partner report also proves, in the target's square-dominant heavy-coordinate branch, that

`|a|>=1/312`, `||b||_2<=|a|`

forces the Schur residual to have two eigenvalues of modulus at least

`s_*=(3-sqrt(5))/2=0.3819660112...`.

If that residual's `s_*/39` spectral window has physical projection leverage at most `1/32`, apply the partner theorem (2.3) with `s=s_*` and the worst permitted `|a|=1/312`:

`||p_Q||_infinity
 <=28.4310144633/sqrt((1/312)*(3-sqrt(5))/2)
 =812.56346899... <812.564.`                                 (6.1)

This is an actual quantitative partner inequality retaining arbitrary further residual eigenvalues and their signs. It does **not** assert that every `ell_*>=3/4` O0 survivor is square-dominant; rather, any survivor that is square-dominant and has the partner's diffuse residual window is already paid. Therefore the next O0 work may restrict to ridge-heavy packets that also evade this square-assisted exit.

## 7. Genuinely rotated indefinite explicit example

Let

`U=I_5-(2/5)11^T`.

This is a dense orthogonal Householder matrix: diagonal entries are `3/5`, off-diagonal entries are `-2/5`. Define the `10 x10` symmetric matrix

`A=[[0,U],[U,0]]`.

All ten eigenvalues are `+1` or `-1`, so this is an indefinite genuinely non-diagonal target matrix with far more than three eigenvalues of modulus one. Take the physical cross block `B=U`. Then

`E=e_3(1,1,1,1,1)=10`.

At effective dimension three,

`gamma_*^2=2/3`, `K_*=(3/5)I_5`, `ell_*=3/5`, `q_*=6/5`,

and

`D=(5/2)^5`.

Theorem 4.1 gives the aggregate estimate

`||p_Q||_infinity <5.978`                                   (7.1)

for every independent cap-one product input. Keeping the exact determinant in (2.1) instead of the coarse `D>=E/gamma^6` improves this same example to

`boxed( ||p_Q||_infinity <5.008 ).`                          (7.2)

The density is continuous by the ridge theorem. No rotation of the input law or post-rotation independence is used.

## 8. First unpaid implication

The new first O0 implication is

`QFORM-O0-THREEQUARTER-HEAVY-PACKET-v1`:

at the effective-dimension-three scale, assume `E_3(B)>=1/256` and `max diag K>=3/4`; exploit the fact that at most four original-coordinate rows can be this heavy, together with (5.5), to condition/group those rows and transfer a fixed fraction of the determinant/third-compound currency into either

1. a square-assisted partner branch,
2. a rank-two conditioned residual paid by existing half-Riesz/grouped-row theorems,
3. or O1/O2/O3 aggregate overlap currency,

without selecting a reciprocal tiny local minor.

The O1/O2/O3 classes remain separately unpaid in the full synthesis. Consequently **the full QFORM conjecture remains open**. The present O0 paid branch proves continuity; no full continuity conclusion is claimed.

## 9. Integrity/status

All arguments stay in original product coordinates or invoke source-pinned product-space Fourier theorems that retain arbitrary self blocks/outside couplings. The live correction inbox was refreshed immediately before publication. This report does not rely on a refuted intermediate statement. No scheduler, notification, email, Drive, public-release, paid-model/API, remote-workflow, account-authentication, or permission mutation is part of this run.
