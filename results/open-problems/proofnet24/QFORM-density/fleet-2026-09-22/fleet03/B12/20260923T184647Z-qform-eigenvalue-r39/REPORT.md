SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T18:46:47Z.
attacking: seven-mode physical square-energy compiler, converting arbitrary signed added spectrum into a self-core or five-direction cross-ridge exit.

# fleet03/B12 r39 — destructive square-Gram to seven-mode hybrid density compiler

Run: `20260923T184647Z-qform-eigenvalue-r39`

Status: **new supporting theorem proved; designated partner applied at an actual inequality; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

The target is the full arbitrary-dimension statement for independent real coordinates with scalar densities bounded by one and symmetric `A` having at least three eigenvalues of absolute value at least one. No moment, Gaussian, log-concavity, support, iid, diagonal-basis, or post-rotation independence assumption is made below.

Continuity: the cross-ridge exit below has a continuous `C_0` density. The finite-core projected-gradient exit proves absolute continuity and an essential `L^infinity` bound but does not by itself prove continuity. Therefore the combined theorem below is asserted only as an essentially bounded density theorem.

## 1. Source-valid premises actually used

1. **Finite physical-core projected-gradient theorem.** From
   `yspennstate/math-open-problems@7f2c9f4c2dfeb6134d9291eb7e83b62a9cb4b3b0`,
   if an actual `m x m` original-coordinate quadratic block has at least three eigenvalues in absolute value at least `a>0`, then after arbitrary affine terms its output density is bounded by
   `2 sqrt(6 pi m)/a`.
   Conditioning on all outside ORIGINAL coordinates is therefore legitimate and retains independence inside the core.

2. **One-scale ridge theorem.** From
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
   for an actual original-coordinate cross block `B`, with
   `K=B B^T (gamma^2 I+B B^T)^(-1)`, `theta=tr K`, if `1<=q<=2`, `max_i K_ii<=q/2`, and `theta>2q`, then the full ambient form has a continuous `C_0` density and
   `||p||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta/(theta-2q)`.
   Arbitrary self blocks and outside couplings are retained.

3. **Designated partner fleet04/B12 destructive square-Gram theorem.** From
   `yspennstate/math-open-problems@c307f81b3196820aa711a5c47f243feeeeb74781`,
   for an actual carrier `H`, baseline `A0`, arbitrary symmetric addition `D`,
   `G0=(A0^2)[H,H]`, `G=((A0+D)^2)[H,H]`, and destructive defect
   `N_H(A0,D)=[G0-G]_+` with eigenvalues `nu_1>=nu_2>=...`, one has, for `k+r<=|H|`, and after any further symmetric `T` with `||T||_op<=delta`,

   `sqrt(lambda_k(((A0+D+T)^2)[H,H])) >= [sqrt((lambda_(k+r)(G0)-nu_(r+1))_+) - delta]_+`.

   This charges only actual loss of square energy on the physical carrier. `D` may have arbitrary rank, signs and operator norm.

No quadratic remainder is discarded as a small random variable and no convolution independence is asserted after a spectral rotation.

## 2. Deterministic self/cross profile from a physical square-energy carrier

Let `H` be a set of `m` ORIGINAL coordinates and write the final matrix in the physical split `H direct_sum H^c` as

`A = [[C, B], [B^T, D]]`.

The exact physical identity is

`(A^2)[H,H] = C^2 + B B^T`.                                      (2.1)

Let singular values be decreasing. For positive integers `p,q` with `p+q=k+1`, Weyl's eigenvalue inequality for the positive semidefinite matrices `C^2` and `B B^T` gives

`lambda_k(C^2+B B^T) <= lambda_p(C^2)+lambda_q(B B^T)`

and hence

`boxed: s_p(C)^2 + s_q(B)^2 >= lambda_k((A^2)[H,H]).`            (2.2)

This is purely deterministic. In particular, at `k=7`, `p=3`, `q=5`, if

`lambda_7((A^2)[H,H]) >= g^2`,                                  (2.3)

then

`boxed: s_3(C)^2 + s_5(B)^2 >= g^2.`                            (2.4)

This is the first essential implication used below: square energy cannot hide from both a three-mode physical self core and a five-direction actual cross block.

## 3. Five-cross-direction ridge receiver with no leverage hypothesis

Let `b=s_5(B)>0`. Apply the ridge theorem with `q=2` and

`gamma=b/sqrt(12)`.                                               (3.1)

Because `0<=K<=I`, every diagonal entry satisfies

`K_ii<=1=q/2`,                                                    (3.2)

so the leverage gate is automatic. The first five singular values of `B` are at least `b`, hence

`theta >= 5 * b^2/(gamma^2+b^2)
       = 5/(1+1/12)
       = 60/13 > 4 = 2q`.                                       (3.3)

The function `theta/(theta-4)` decreases for `theta>4`, therefore the ridge theorem yields

`||p_Q||_infinity
 <= sqrt(e)/(2 gamma) * (60/13)/(60/13-4)
 = sqrt(e)/(2(b/sqrt(12))) * 15/2
 = boxed: [15 sqrt(3e)]/[2 b].`                                 (3.4)

This branch proves a continuous density vanishing at infinity. The estimate concerns the full ambient quadratic form; same-side quadratic curvature and all outside coefficients remain present.

Define

`D5 = 15 sqrt(3e)/2`.                                             (3.5)

## 4. Seven-mode carrier compiler

### Theorem 4.1 — `QFORM-SEVEN-SQUARE-MODE-HYBRID-COMPILER-v1`

Let `H` be an actual set of `m>=7` original coordinates. If

`lambda_7((A^2)[H,H]) >= g^2 >0`,                                (4.1)

then for every independent cap-one product input,

`boxed:
 ||p_(X^T A X)||_infinity
 <= [24 pi m + 675 e/4]^(1/2) / g.`                              (4.2)

No restriction is imposed on the number, signs, or magnitudes of the other eigenvalues of `A`.

### Proof

Put

`a=s_3(C)`, `b=s_5(B)`.

Equation (2.4) gives

`a^2+b^2>=g^2`.                                                   (4.3)

If `a>0`, condition on all coordinates outside `H`. The conditional form on the `m` independent coordinates in `H` has quadratic matrix exactly `C`; outside variables create only deterministic affine and constant terms. The projected-gradient theorem gives the uniform conditional bound

`||p_Q||_infinity <= A_m/a`,
`A_m=2 sqrt(6 pi m)`.                                            (4.4)

If `b>0`, Section 3 gives independently

`||p_Q||_infinity <= D5/b`.                                      (4.5)

We now use only the Euclidean constraint (4.3). Set

`K_m = sqrt(A_m^2+D5^2)/g`.                                      (4.6)

If both `A_m/a>K_m` and `D5/b>K_m`, then

`a<A_m/K_m`, `b<D5/K_m`,

so

`a^2+b^2 < (A_m^2+D5^2)/K_m^2 = g^2`,

contradicting (4.3). Hence at least one of (4.4), (4.5) is at most `K_m`. Since

`A_m^2=24 pi m`, `D5^2=675e/4`,

(4.2) follows. The argument also covers `a=0` or `b=0` by using the other branch. QED.

This theorem is a compact end-to-end receiver for seven physical square-energy modes. It is stronger than simply proving `s_3(A)>=g`: it uses where the square energy lands in ORIGINAL coordinates and routes it either to a bounded physical core or to an actual product-preserving cross block.

## 5. Arbitrary additional spectrum via destructive square-Gram defect

### Theorem 5.1 — `QFORM-DESTRUCTIVE-GRAM-SEVEN-MODE-STABILITY-v1`

Let `A0,D,T` be real symmetric `n x n` matrices and let `H` be an actual set of `m` original coordinates. Put

`G0=(A0^2)[H,H]`,
`G=((A0+D)^2)[H,H]`,
`N=[G0-G]_+`,

and write `nu_1>=nu_2>=...>=0` for the eigenvalues of `N`. Suppose `7+r<=m`, `||T||_op<=delta`, and define

`g = [sqrt((lambda_(7+r)(G0)-nu_(r+1))_+) - delta]_+`.           (5.1)

If `g>0`, then the full final matrix

`A=A0+D+T`                                                       (5.2)

satisfies

`boxed:
 ||p_(X^T A X)||_infinity
 <= [24 pi m + 675 e/4]^(1/2) / g.`                              (5.3)

In particular, if `rank N<=r`, then

`g >= [sqrt(lambda_(7+r)(G0))-delta]_+`.                         (5.4)

### Proof

Apply the completed fleet04/B12 theorem with `k=7`. It gives

`sqrt(lambda_7((A^2)[H,H])) >= g`.                               (5.5)

Theorem 4.1 then applies directly. QED.

### Interpretation

The addition `D` may contain arbitrarily many smaller eigenvalues, arbitrarily many larger eigenvalues, arbitrary signs, and arbitrary orientation. It may be full rank and have unbounded operator norm. The only quantity charged is the residual spectrum of the **actual destructive square-Gram footprint** on `H`. A second dense tail `T` is charged only through its deterministic coefficient norm `delta`; the random variable `X^T T X` is never approximated or treated as independent.

Thus additional eigenvalues that increase the carrier square Gram, or destroy it only in at most `r` directions, are free except for the finite reserve of `r` carrier modes. This is a stability theorem for the final coefficient matrix, not a probabilistic convolution statement.

## 6. Actual partner application: full-rank unbounded signed packet plus rank-three destructive packet

Take `R^20=H direct_sum J` with `|H|=|J|=10`. Let

`A0 = [[0, 2 I_10], [2 I_10, 0]]`.                              (6.1)

Let `J0` be block diagonal with five copies of

`[[0,-1],[1,0]]`,

so `J0^T=-J0` and `J0 J0^T=I_10`. For arbitrary real `t`, define

`D_t = [[0, t J0], [t J0^T, 0]]`.                               (6.2)

`D_t` has ten eigenvalues `+|t|` and ten eigenvalues `-|t|`; its magnitude is completely unrestricted. Put `B_t=A0+D_t`. Then exactly

`(B_t^2)[H,H]
 = (2I_10+tJ0)(2I_10+tJ0)^T
 = (4+t^2) I_10`.                                               (6.3)

Now add an arbitrary symmetric matrix `L`, with no rank, sign, or norm restriction, satisfying only

`rank N_H(B_t,L) <= 3`,                                         (6.4)

and finally any symmetric dense `T` with

`||T||_op <= 1/4`.                                               (6.5)

Set

`A=B_t+L+T`.                                                      (6.6)

Apply the completed fleet04/B12 destructive square-Gram theorem with baseline `B_t`, addition `L`, carrier `H`, `k=7`, `r=3`, and `delta=1/4`. Since `7+3=10`,

`sqrt(lambda_7((A^2)[H,H]))
 >= sqrt(lambda_10((B_t^2)[H,H])) - 1/4
 = sqrt(4+t^2)-1/4
 >= 7/4`.                                                        (6.7)

This is the required equation-level use of the designated partner result.

The new seven-mode compiler therefore gives

`||p_Q||_infinity
 <= [240 pi + 675 e/4]^(1/2) / (7/4)
 = 19.899275305553434...`.                                      (6.8)

This improves the available density control for this enlarged family while permitting:

- a full-rank signed packet `D_t` with arbitrarily large eigenvalues of both signs;
- a further arbitrary-magnitude, potentially full-rank `L`, constrained only by rank at most three of its destructive square-Gram footprint on `H`;
- a final dense symmetric coefficient tail of norm at most `1/4`;
- arbitrary cap-one independent input laws.

No continuity claim is made for the whole family because the proof may exit through the finite-core branch. If it exits through the five-direction cross-ridge branch, that branch has a continuous `C_0` density.

## 7. Rigorous finite consistency check

A deterministic numerical check sampled 10,000 random real symmetric `24 x 24` matrices, used the first ten ORIGINAL coordinates as `H`, and verified

`s_3(A[H,H])^2 + s_5(A[H,H^c])^2
 >= lambda_7((A^2)[H,H])`.                                      (7.1)

There were zero violations at tolerance `1e-9`; the minimum observed margin was `1.909193461459049`. This is only a consistency test of the matrix inequality. The proof is the Weyl argument in Section 2, and no Monte Carlo conclusion about the conjecture is drawn.

## 8. What remains for the full conjecture

The full target is still OPEN. The missing implication is structural:

> starting only from `s_3(A)>=1`, force a bounded ORIGINAL-coordinate carrier with seven square-energy modes at a universal scale, or route failure of such a carrier into one of the already-paid ridge/grouped-crossing/hub/rank-two mechanisms.

The bare three-eigenvalue assumption does not itself provide seven square-energy modes on a bounded carrier, so Theorem 5.1 is a supporting stability theorem rather than a complete proof.

The new result narrows the additional-eigenvalue issue: once seven physical square-energy modes are available, *arbitrary extra signed spectrum is harmless except through its actual destructive carrier footprint*. The remaining difficulty is extracting such product-preserving physical geometry from only three global large eigenvalues.

## 9. Source pins

- Control source read at start: `yspennstate/math-research-brain@fc919bb6362788e5e61ad24963aa37a118ecc720`.
- Designated partner: `yspennstate/math-open-problems@c307f81b3196820aa711a5c47f243feeeeb74781`.
- Finite-core projected-gradient theorem: `yspennstate/math-open-problems@7f2c9f4c2dfeb6134d9291eb7e83b62a9cb4b3b0`.
- One-scale ridge theorem: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`.
- Execution label: `WITHOUT_VERIFIED_BRAIN`.
