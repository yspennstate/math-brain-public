SIGNED IN - working on the quadratic-form bounded-density programme, account fleet03, slot B06, 2026-09-24T14:19:44Z.
attacking: the unresolved multiplicity-eight overlap-one terminal by preserving the shared physical coordinate through the first symmetrization, and proving exactly where the existing disjoint grouped compiler loses the dominant bordered determinant.

# fleet03/B06 auto12 — overlap-one disjointification barrier and paired-source Fourier interface

Run: `20260924T141944Z-fleet03-B06-fixedmult-auto12`  
Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924` (later than, and therefore controlling over, the older slot prompt).  
Baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 0. Current mathematical position

The complete nine-eigenvalue replacement has now received multiple independent source-backed PASS reviews elsewhere in the fleet, with the sharper reviewed bound

`||p_Q||_infinity < 5338 K^2/s` when `s_9(A)>=s>0`.

I do not re-award its global validation status here. The first genuinely unpaid threshold remains eight. The current `s_8` no-pivot terminal has an order-two seed `S|T`, `B=A[S,T]`, and two physical heavy residual coordinates `H={h_1,h_2}`. For each `h in H`,

`det A[S union {h}, T union {h}] = +/- det(B) D_h`,

with `|D_h|>=77/80`, whereas the disjoint border through the other heavy coordinate is

`det A[S union {h_1}, T union {h_2}] = +/- det(B) E_{h_1h_2}`,

with `||E||_F<=3/80`.

The previous B06 run proved that the dominant third-order determinant currency is therefore overlap-one, not disjoint. This run proves that the existing grouped product-Fourier compiler is algebraically *exactly blind* to that currency, and gives the correct source-preserving replacement object.

---

## 1. The existing grouped compiler cannot see one overlap coordinate

### Theorem `QFORM-OVERLAPONE-DISJOINTIFICATION-BLINDNESS-v1`

Let `S,T` be disjoint two-element original-coordinate banks, let `h` be outside them, and assume

`B=A[S,T]`

is invertible. Put

`Delta_h = det A[S union {h}, T union {h}]`.

Consider the already-proved grouped product-Fourier compiler in which the literal coordinate `X_h` is used as a one-dimensional hub.

#### (a) Keeping only the two-column bank `T` can never reach a density exponent

With `J=T`, the hub row is

`m=A[h,T] in R^2`.

If `m!=0`, its row span has dimension one. The two seed rows `A[S,T]` projected orthogonally off `span{m}` therefore live in a space of dimension at most one. Hence the residual order-two volume is identically zero:

`Z_2(C)=0`.

Thus the grouped compiler has at most `(k,ell)=(1,1)`, so `d=k+ell<=2`. Its direct Fourier-inversion density step requires `d>2` and cannot fire. If `m=0`, then `k=0` and again `d<=2`.

In particular, the nonzero overlap determinant `Delta_h` does not alter this dimension count.

#### (b) Adding one fresh physical column recovers only a disjoint determinant

Let `kappa` be a physical coordinate outside `S union T union {h}` and enlarge the column bank to

`J'=T union {kappa}`.

Write

`m=A[h,J'] in R^3`,
`N=A[S,J'] in R^(2x3)`.

Assume `m!=0`, put `S_h=||m||_2`, and let `C` be the two rows of `N` after orthogonal projection onto `m^perp`. Then the exact Gram--Schmidt identity is

`S_h^2 det(CC^T) = det([m;N][m;N]^T) = det([m;N])^2`.

Therefore

`boxed: S_h sqrt(Z_2(C)) = |det A[S union {h}, T union {kappa}]|.`                 (1.1)

The row set `S union {h}` and column set `T union {kappa}` are disjoint. Thus the right side is an ordinary disjoint order-three crossing determinant, not the overlap determinant `Delta_h`.

For the grouped theorem with `(k,ell,d)=(1,2,3)` and a literal cap-one hub (`M_H<=1`), the already-audited density constant specializes to

`3 sqrt(2) exp(5/6) S_h^(-1/3) Z_2(C)^(-1/6)`.

Using (1.1), all intermediate `S_h` dependence cancels exactly:

`boxed: ||p_Q||_infinity <= 3 sqrt(2) exp(5/6)
        |det A[S union {h},T union {kappa}]|^(-1/3)`                              (1.2)

whenever that grouped branch is otherwise applicable. Numerically the front constant is

`3 sqrt(2) exp(5/6) = 9.762213934782446...`.

So adjoining a fresh column does not partially spend the overlap currency: after the exact singular-value/volume cancellation, the analytic payment depends **only** on the disjoint three-minor.

### Proof

Part (a) is dimension counting after orthogonal projection in `R^2`. For part (b), Gram--Schmidt the first row `m` of the `3x3` matrix `[m;N]`. Row operations orthogonal to `m` do not change its determinant magnitude. The Gram determinant of the transformed rows is

`||m||^2 det(CC^T)`.

Because the matrix is square, that Gram determinant is also `det([m;N])^2`. This proves (1.1). Substitution into the audited `(1,2)` grouped compiler gives

`S_h^(-1/3) Z_2^(-1/6)
 = (S_h sqrt(Z_2))^(-1/3)`,

which is (1.2). QED.

### Terminal `s_8` consequence

Take `h=h_1` and `kappa=h_2` in the terminal state. The bordered-minor identity gives

`det A[S union {h_1},T union {h_2}]
 = +/- det(B) E_{h_1h_2}`,

whereas

`det A[S union {h_1},T union {h_1}]
 = +/- det(B) D_{h_1}`

and `|D_{h_1}|>=77/80`.

Hence the disjointified grouped compiler replaces the large quantity `det(B)D_h` by the potentially tiny quantity `det(B)E_{h_1h_2}`. The previous exact terminal estimate even gives

`|det(B)E_{h_1h_2}|^2+|det(B)E_{h_2h_1}|^2
 <= (9/6400)|det B|^2`.

This is not a constant-tuning issue. It proves that a direct reuse of the current disjoint `(k,ell)=(1,2)` compiler cannot spend the certified overlap-one curvature.

---

## 2. Exact source-preserving replacement after one symmetrization

The natural repair is not to duplicate the physical coordinate into two falsely independent banks. It is to keep the two-copy source block generated by the first legitimate symmetrization.

### Theorem `QFORM-PAIRED-SYMMETRIZATION-SOURCE-BLOCK-v1`

Let

`Q(X)=X^T A X+b^T X+c`,

where `A=A^T` and the original `X_i` are independent with probability densities `0<=f_i<=1`. Let `X'` be an independent copy and set coordinatewise

`U=X-X'`, `V=X+X'`.

Then, exactly,

`boxed: |phi_Q(t)|^2
 = integral exp(i t [U^T A V+b^T U]) prod_i G_i(U_i,V_i) dU dV`,                (2.1)

where

`G_i(u,v)= (1/2) f_i((v+u)/2) f_i((v-u)/2)`.                                   (2.2)

For every coordinate `i`, `G_i` is a probability density on `R^2` and satisfies

`0<=G_i<=1/2`,                                                                   (2.3)

and every one-dimensional slice is a subprobability of cap at most `1/2`:

`int G_i(u,v) dv <=1` for every `u`,
`int G_i(u,v) du <=1` for every `v`.                                             (2.4)

Moreover its partial Fourier transform in the second variable has the exact global energy budget

`boxed: integral_R integral_R |hat G_{i,u}(xi)|^2 dxi du
       = pi ||f_i||_2^4 <= pi.`                                                  (2.5)

Here `hat G_{i,u}(xi)=integral exp(i xi v)G_i(u,v)dv` under the manuscript Fourier convention.

Now fix disjoint two-sets `S,T` and one physical coordinate `h` outside them. Condition in (2.1) on every variable except

`U_{S union {h}}` and `V_{T union {h}}`.

For `s in S`, `V_s` is exterior and the surviving factor `G_s(U_s,V_s)` is a one-dimensional subdensity satisfying (2.4). For `t in T`, `U_t` is exterior and `G_t(U_t,V_t)` is likewise a subdensity. The common physical coordinate contributes the **unsplit two-dimensional factor**

`G_h(U_h,V_h)`.

The phase in these six selected variables has bilinear coefficient matrix exactly

`boxed: M_h=A[S union {h},T union {h}]`,                                        (2.6)

and every interaction with conditioned exterior variables is only affine in the selected variables.

Thus the overlap determinant

`det M_h = det A[S union {h},T union {h}]`

survives literally in the bilinear phase after symmetrization, while original product provenance survives as four one-dimensional slice subdensities plus the single paired source block `G_h`. No rotation-induced independence is asserted.

### Proof

Since `X'` is independent,

`|phi_Q(t)|^2=E exp(i t[Q(X)-Q(X')])`.

With `X=(V+U)/2` and `X'=(V-U)/2`, symmetry of `A` gives

`Q(X)-Q(X')=U^T A V+b^T U`.

The Jacobian of `(x,x')->(u,v)` is `2` in each coordinate, hence (2.1)-(2.2). The change of variables also proves total mass one and the cap `1/2`.

For fixed `u`, write `x=(v+u)/2`; then

`int G_i(u,v)dv = integral f_i(x)f_i(x-u)dx <=1`,

and the other slice is identical. For the `L^2` norm, the inverse change `(u,v)=(x-x',x+x')` has Jacobian `2`, so

`intint G_i(u,v)^2 du dv
 = (1/2)(integral f_i(x)^2 dx)^2
 = (1/2)||f_i||_2^4 <=1/2`.

Plancherel in `v` gives (2.5).

Finally, because `S,T,{h}` are physically disjoint except for the intentionally shared `h` on the row/column side, fixing all complementary `U,V` variables leaves the selected part of `U^TAV` equal to

`U_{S union {h}}^T A[S union {h},T union {h}] V_{T union {h}}`

plus affine and constant terms. This proves (2.6). QED.

---

## 3. Why (2.1) is the correct next curved-fiber interface

The live correction set forbids normalizing a conjugate sum/difference slice and then claiming a uniform conditional density cap. The construction above never does that. The slice factors are kept as **subdensities**, and the only global statement about the shared `(U_h,V_h)` source is the exact `L^2` energy (2.5).

It also removes a problem in the naive triangular-shear attack. In the original variables, translating the two seed banks by multiples of `X_h` causes the arbitrary same-bank quadratic phases to create additional `X_h^2` terms. In the difference variables (2.1), the entire quadratic polynomial is globally bilinear `U^TAV`; there are no hidden same-side quadratic phases to expand. The price is precisely the paired factor `G_h`, which must not be split into independent `U_h` and `V_h` laws.

This identifies a clean missing analytic statement:

`QFORM-OVERLAP-PAIREDBLOCK-CURVED-RECEIVER-v1`:

> bound the scalar small-ball probability or an integrated Fourier norm for the conditional six-variable block in (2.6), using the four cap-one subdensity slices together with the exact paired energy (2.5), with a bound that depends on the overlap determinant before any disjointification.

A pointwise rough quadratic-phase estimate is not an admissible substitute. Direct interval/small-ball integration or a block Brascamp--Lieb estimate that keeps `G_h` intact is the natural next mechanism.

---

## 4. Designated fleet04/B06 result: actual inequality and exact scope

The current completed designated partner result is fleet04/B06

`QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`

at `yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`.

It proves that for a diffuse original-product two-frame `(L,V)`, with shared transverse statistic of the exact tangential form

`B=alpha L+gamma V+B_R`,

one may complete the square and apply a determinant-one output shear. On the region outside the shifted fold,

`|V-v_*|>r`,

the two-output density satisfies

`boxed: ||g_r||_infinity <= 4/(|lambda| r).`                                    (4.1)

I apply (4.1) at the actual working radius `r=1/64`. On every shear-flat subbranch of the proposed overlap receiver in which the exposed curved coefficient obeys `|lambda|>=1`, this gives the concrete inequality

`boxed: ||g_{1/64}||_infinity <=256.`                                            (4.2)

Therefore the zero-normal/tangential face of a future paired-block decomposition needs no new argument once it has been reduced to a diffuse two-frame in the partner theorem's exact source-separated scope. The present `s_8` overlap certificate does **not** by itself guarantee that reduction, so (4.2) is not promoted to a proof of multiplicity eight. Positive normal paired-block mass remains the genuinely new part.

---

## 5. Deterministic diagnostic

I independently checked identity (1.1) on 10,000 fixed-seed random real `3x3` matrices. For each matrix, the first row was treated as `m`, the other two as `N`, and `C` was obtained by orthogonal projection onto `m^perp`. There were zero violations at tolerance `1e-10`; the largest normalized floating discrepancy between

`||m|| sqrt(det(CC^T))`

and

`|det([m;N])|`

was `1.18e-11`. This is only a regression diagnostic; the proof is the exact Gram determinant calculation above.

---

## 6. Status and next exact obligation

- Nine-eigenvalue fixed-multiplicity theorem: multiple independent PASS reviews exist elsewhere; this run does not change its release status.
- `QFORM-OVERLAPONE-DISJOINTIFICATION-BLINDNESS-v1`: **PROVED**.
- `QFORM-PAIRED-SYMMETRIZATION-SOURCE-BLOCK-v1`: **PROVED**.
- Multiplicity eight: **OPEN**.
- Full three-eigenvalue conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Global continuity: **OPEN** outside scopes where an integrable characteristic-function envelope is already proved.

The next B06 obligation is now narrower than “find an overlap receiver”: prove a dimension-free block inequality for the exact conditional source in (2.6), using the four one-dimensional subdensity factors and the paired source budget (2.5). Any proof that first replaces the shared coordinate by a fresh disjoint column is provably forced back to the small `E`-border by (1.1), and therefore cannot use the dominant `D_h` currency.

No scheduler/task identity, enabled/paused state, email/push setting, permission, public-release state, installation, paid API/model call, or cross-account authentication was changed.
