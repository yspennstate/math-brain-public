SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-24T02:05:27Z.

# fleet01/B20 — r43 exterior-cross E3 or common-plane collar

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **ESSENTIAL_STEP_APPLIED / R43-EXTERIOR-CROSS-COMPILER / FULL-QFORM-OPEN**.
Full-target continuity remains **OPEN**. Execution remains `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-valid premises

Fresh owner control remained revision `2026-09-22.15`, QFORM-exclusive. The full target is still OPEN. Live corrections consumed include: no law-uniform pointwise quadratic oscillatory decay; no worst-fibre dimension-free cap; no arbitrary-joint rank-three coarea shortcut; no post-rotation independence; and no deletion of nonzero coefficient tails.

The newest completed designated partner is fleet02/B20 `20260924T011328Z-fleet02-B20-QFORM-auto11`, canonical report commit `math-open-problems@7320b73d2b8e9548653c01a9a97515e337f3cc3d`. Let `M=A[I,J]` be its literal disjoint original-coordinate cross block, with singular values `s1>=s2>=...`, `x_r=s_r^2`, and

`E2(M)>4/9`, `E3(M)<delta:=2^-18`.

The partner proves, in the branch `s2<1/8`, with `T2=sum_(r>=3)x_r`, the split:

(A) if `x2>=T2`, then

`p:=s1*s2 > p0:=0.47133956521232195...`;

(B) if `x2<T2`, then

`s1>s_*:=113.7464246960848...` and `dist_F(M,rank<=1)<0.005860183`.

It also proves the global third-mode separation

`max{||A[I,I]||op,||A[J,J]||op,||A[K,K]||op,||A[I,K]||op,||A[J,K]||op}>7/40`,

where `K=(I union J)^c`.

The already-completed literal physical `E3` receiver pays any cross block `B` with `e3(BB^T)>=2^-18` by a universal bound (`<=82.760672` in the partner normalization). I only use this exact fixed-threshold scope below.

## 2. Exterior augmentation identity

Let `H=A[I,K]` and form the literal physical cross block

`B=A[I,J union K]=[M H]`.

Let `u1,u2` be the top two left singular vectors of `M`, and `P2` the orthogonal projection onto their span. Since

`BB^T=MM^T+HH^T`

and

`MM^T >= s1^2 u1u1^T+s2^2 u2u2^T`

in Loewner order, monotonicity of eigenvalues under positive-semidefinite addition gives

`e3(BB^T) >= e3(s1^2 u1u1^T+s2^2 u2u2^T+HH^T)`.

Expanding the third exterior power (equivalently Cauchy--Binet after using the deterministic singular frame) and keeping only triples containing both top singular columns yields the exact positive sub-sum

`e3(BB^T) >= (s1*s2)^2 ||(I-P2)H||_F^2`.                 (2.1)

This is deterministic coefficient geometry only. No projected random variable is asserted independent.

Likewise, using only the top singular vector `u1` and putting `P1=u1u1^T`, `H_perp=(I-P1)H`, one has

`e3(BB^T) >= s1^2 e2(H_perp H_perp^T)`.                 (2.2)

All tails of `M` and all coefficients of `H` remain in the random quadratic form; (2.1)-(2.2) merely keep positive exterior-volume sub-sums.

The same statements hold with `I,J` interchanged and `H=A[J,K]`, using the right singular vectors of `M`.

## 3. The concentrated-second-direction branch becomes a common two-plane collar

Assume partner branch (A): `x2>=T2`, hence `s1*s2>p0`.

If

`||(I-P2)H||_F >= d2:=2^-9/p0`,

then by (2.1)

`e3(BB^T) > p0^2 d2^2 = 2^-18`,

so the physical E3 receiver pays the full ambient law.

Numerically,

`d2=0.004143774773331803...`.

Therefore every unpaid state in this subbranch with a strong exterior crossing `||H||op>7/40` must satisfy

`boxed: ||(I-P2)H||_F < 0.004143775`,                  (3.1)

and consequently

`||P2 H||op >= ||H||op-||(I-P2)H||op
             > 7/40-d2
             =0.170856225226668...`.                   (3.2)

Thus a `>7/40` exterior resource cannot point in an arbitrary new left direction: unless E3 already pays, it lies within Frobenius distance `0.004144` of the same physical two-plane supporting the two multiplicatively strong directions of `M`, while retaining a `>0.170856` aligned arm.

This is the requested actual application of the fleet02/B20 inequality `s1*s2>0.4713395652`.

## 4. The ultra-giant rank-one branch becomes rank-one aligned or rank-two transverse

Assume partner branch (B): `x2<T2`, hence `s1>s_*`.

If the augmented physical block `B=[M H]` remains unpaid, then (2.2) and `e3(BB^T)<2^-18` imply

`e2(H_perp H_perp^T) < eps_*:=2^-18/s_*^2
                     =2.94838755e-10`.                (4.1)

This has a useful deterministic consequence. Put

`S=||H_perp||_F^2`

and let `z1>=z2>=...` be the squared singular values of `H_perp`, with `T=sum_(r>=2) z_r`.

### 4a. Small transverse mass

If `S<1/256`, then

`boxed: ||H-P1H||_F<1/16`.                              (4.2)

If also `||H||op>7/40`, then

`boxed: ||P1H||op>7/40-1/16=9/80`.                     (4.3)

So the exterior arm is quantitatively aligned with the same physical hub direction `u1` as the ultra-giant crossing.

### 4b. Nontrivial transverse mass

Assume `S>=1/256`. If `T>S/2`, then `z1=S-T<S/2`; since every `z_r<=z1`,

`sum z_r^2 <= z1 S < S^2/2`,

hence

`e2(H_perp H_perp^T)
 =(S^2-sum z_r^2)/2
 >S^2/4 >=2^-18`,

contradicting (4.1). Therefore `T<=S/2`, so `z1>=S/2` and

`e2(H_perp H_perp^T)>=z1 T>=(S/2)T`.

Using (4.1) and `S>=1/256`,

`T < 512 eps_* = 2^-9/s_*^2`.

Thus

`boxed: dist_F(H_perp,rank<=1)<2^(-9/2)/s_*
       <0.000388533`.                                    (4.4)

Since `H=P1H+H_perp`, approximating `H_perp` by its best rank-one matrix gives

`boxed: dist_F(H,rank<=2)<0.000388533`.                  (4.5)

Moreover `z1>=S/2` gives a genuine transverse singular arm

`s1(H_perp)>=sqrt(S/2)>=1/(16 sqrt(2))
             =0.0441941738...`.                          (4.6)

Hence the ultra-giant branch has a sharp physical alternative: the exterior crossing is within `1/16` of the original hub line, or it is within `3.89e-4` of rank two and contains a transverse arm of size at least `0.04419`.

## 5. New theorem

### `QFORM-R43-EXTERIOR-CROSS-E3-OR-COMMONPLANE-COLLAR-v1`

In the fleet02/B20 r43 giant-near-rank-one packet `s2(M)<1/8`, suppose the guaranteed `>7/40` third-mode resource of partner Theorem 5.1 is one of the literal exterior crossings `A[I,K]` or `A[J,K]`.

Then either the full QFORM law is already paid by a literal physical cross block with `e3>=2^-18`, or:

1. in the `x2>=T2` branch, that exterior crossing lies within Frobenius distance `<0.004143775` of the same top-two singular plane of `M` and retains aligned operator norm `>0.170856225`; or
2. in the `x2<T2` ultra-giant branch, it is either within Frobenius distance `<1/16` of the top hub line (with aligned arm `>9/80`), or it is within Frobenius distance `<0.000388533` of rank at most two and contains a transverse arm `>=1/(16sqrt2)`.

The statement is symmetric between the `I` and `J` sides.

## 6. Remaining interface

The fleet02/B20 five-way third-mode separation is therefore no longer broad on its two exterior-crossing alternatives. The first genuinely unpaid r43 interface is now

`QFORM-R43-SAMEBANK-OR-ALIGNED-EXTERIOR-COLLAR-PAYMENT-v1`:

- either the fixed `>7/40` resource is one of the same-bank blocks `A[I,I]`, `A[J,J]`, `A[K,K]`; or
- the exterior resource is forced into the explicit common one/two-plane collars above.

The next useful closure step is a Schur/grouped-coordinate receiver for these aligned collars, or a physical cut of the strong same-bank block that preserves enough of the existing hub/two-plane currency. One must retain the residual crossing and all same-bank curvature rather than deleting them.

No claim of a full proof or counterexample is made. Full QFORM remains OPEN; full continuity remains OPEN.
