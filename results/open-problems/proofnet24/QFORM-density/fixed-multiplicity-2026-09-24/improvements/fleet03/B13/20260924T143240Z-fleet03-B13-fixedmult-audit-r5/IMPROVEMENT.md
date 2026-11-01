# fleet03/B13 r5 — strong-cross / weak-self local receiver obstruction and updated extremal-product compiler

Run: `20260924T143240Z-fleet03-B13-fixedmult-audit-r5`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Current frontier consumed

The complete fixed-multiplicity baseline was reread in this invocation. I found no new fatal defect; the seventeen-direction theorem remains PASS in this worker's audit. The harmless product-projection wording point remains exactly as previously recorded: after rows with `b_i=0` are omitted one may write `sum_{b_i>0}(1-b_i)<=d`, or keep the displayed equality before omitting those rows.

The current stronger source-backed result is the nine-direction theorem with canonical `C_0` density and height `<2582 K^2/s` (fleet03/B14 sharpening and fleet03/B15 continuity closure). Multiplicity eight remains open.

For the eight-direction endpoint I use the new fleet03/B15 strong-cross collapse. In the normalized terminal no-pivot branch it produces a literal physical pair `H` with

```
det(C C^T) >= gamma_* := delta_*^2/2 = 0.36494426588270207...,
||B||_op < beta_* := 0.1104987562112089...,
B=A[H,H],   C=A[H,H^c].
```

If `B=0`, the exact-zero two-anchor receiver closes the branch with height `<8.766532`. The unresolved case is `0<||B||_op<beta_*`. If `B` is invertible, the global `s_8(A)>=1` hypothesis additionally gives six unit Schur directions by the principal-pivot Schur count. The question is whether those six directions are genuinely necessary or whether the local strong-cross/weak-self pair data alone already force bounded density.

They are genuinely necessary.

## 2. Theorem — `QFORM-STRONGCROSS-WEAKSELF-NEEDS-SCHUR-SPECTRUM-v1`

Let `eta=1/100` and let `gamma_* = delta_*^2/2` be the terminal eight-direction cross-Gram constant above. There exists an explicit real symmetric matrix `A` and independent cap-one coordinate laws such that:

1. `A` has no `eta` scalar or principal-pair pivot;
2. a literal physical pair `H` has
   `||A[H,H]||_op=1/20<beta_*` and
   `det(A[H,H^c] A[H,H^c]^T)=14641/40000=0.366025>gamma_*`;
3. `A[H,H]` is invertible and indefinite;
4. the Schur complement of that pair is exactly zero;
5. `X^T A X` has a density with infinite essential supremum.

Hence **no local receiver whose hypotheses are only no-pivot + weak pair self-curvature + the B15 strong cross-Gram floor can prove a uniform density bound.** A valid multiplicity-eight closure must use the additional spectral provenance supplied by `s_8(A)>=1` (equivalently, after an invertible pair pivot, the six surviving Schur directions) or another hypothesis of comparable strength.

### Construction

Take `m=243`, put `c=1/20`, and split `2m` physical coordinates into two banks

`P={p_1,...,p_m}`, `R={r_1,...,r_m}`.

Let `J_m` be the all-ones `m x m` matrix and define

```
A = c [ 0    J_m
        J_m   0  ].
```

This matrix is symmetric and has rank two. Its only nonzero eigenvalues are `+cm` and `-cm`, i.e.

`+243/20` and `-243/20`.

Every diagonal entry is zero. Every off-diagonal entry is either zero or `c`, so every principal two-by-two determinant is either zero or `-c^2=-1/400`. Since `1/400<1/100`, the matrix has no `eta`-pivot.

Choose

`H={p_1,r_1}`.

Then

```
B=A[H,H]=c [0 1; 1 0],
```

so `||B||_op=c=1/20` and `|det B|=c^2=1/400<eta`.

Let `C=A[H,H^c]`. The first row of `C` has value `c` on the `m-1` coordinates `r_2,...,r_m` and zero elsewhere; the second row has value `c` on `p_2,...,p_m` and zero elsewhere. Their supports are disjoint. Consequently

```
C C^T = c^2 (m-1) I_2
      = (121/200) I_2,
```

and therefore

```
det(C C^T)=(121/200)^2=14641/40000=0.366025
            >0.36494426588270207...=gamma_*.
```

Since `rank A=rank B=2` and `B` is invertible, block Gaussian elimination gives

`rank A = rank B + rank(A/B)`;

hence the Schur complement `A/B` is exactly zero. This is the precise feature excluded by the true multiplicity-eight hypothesis, which would instead force six surviving unit Schur directions.

### Unbounded output density

Take all `2m` coordinates independent and uniform on `[-1/2,1/2]`; these are probability densities bounded by one. Put

```
U = sum_{j=1}^m X_{p_j},
V = sum_{j=1}^m X_{r_j}.
```

The two sums are independent. Directly from the block form,

`Q=X^T A X = 2c U V = (1/10) U V`.

Let `g_m` be the density of a sum of `m` independent `Unif[-1/2,1/2]` variables. Convolution shows that `g_m` is continuous and strictly positive at zero; hence there are numbers `a,r>0` such that

`g_m(x)>=a` for `|x|<=r`.

For `W=UV` and `w!=0`, the product change of variables gives

`p_W(w)=int_R g_m(u) g_m(w/u) du/|u|`.

If `0<|w|<r^2`, restrict the integral to positive

`|w|/r <= u <= r`.

On this interval both `|u|<=r` and `|w/u|<=r`, so

```
p_W(w) >= a^2 int_{|w|/r}^r du/u
        = a^2 log(r^2/|w|).
```

Thus `p_W(w)->infinity` as `w->0`, and scalar dilation gives

`ess sup p_Q = infinity`.

This is a genuine rough-law counterexample to the **local** receiver, not to the multiplicity-eight theorem: here `rank A=2`, so `s_8(A)=0`.

## 3. Why this matters for the current 8-direction proof

The new B15 strong-cross reduction is valid and useful, but this construction shows exactly what its next receiver must retain. The data

```
no eta-pivot,
||B||_op < 0.111,
det(C C^T) >= 0.3649
```

are insufficient by themselves even when `B` is invertible and indefinite. The missing input is not a constant improvement. In the counterexample the Schur complement is identically zero, whereas under `s_8(A)>=1` Lemma `lem:schur` forces at least six eigenvalues of the Schur complement to have modulus at least one.

Accordingly the next correct endpoint statement should be formulated as a **strong-cross / weak-self / six-Schur-direction receiver**, not as a perturbation of the exact-zero pair theorem and not as a local pair theorem. This also supplies a concrete adversarial test family for any proposed receiver: deleting the six-direction hypothesis must make the theorem fail on the matrix above.

A useful secondary lesson is that the exact-zero closure is not uniformly perturbative in the local pair block without extra spectral information. The family above can be made with arbitrarily small `c>0` by increasing `m` so that `c^2(m-1)>=sqrt(gamma_*)`; every nonzero member still has an unbounded product density while the cross-Gram floor stays fixed.

## 4. Extremal-product law reduction, with designated fleet04/B13 theorem applied

The completed fleet04/B13 no-attainment purification theorem (`math-open-problems@d9f6bcd057b7804ea7ba06fea8dad5f54e357990`) states for every nonnegative measurable kernel `K` that

```
sup_{0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx
 = sup_{|E_i|=1} int_{prod_i E_i} K(x) dx,
```

with no optimizer, interval, centering, bounded-support, or fixed-fragment assertion.

Apply that theorem to the actual current nine-direction interval inequality and the slab kernel

`K_I(x)=1_{ {x^T A x+b^T x+c in I} }`.

The reviewed current theorem gives, after normalization `K=s=1`,

`P{Q in I}<2582 |I|` whenever `s_9(A)>=1`.

Therefore the same sharp current constant is exactly equivalent to the geometric product-set inequality

```
sup_{|E_i|=1}
 |{x in prod_i E_i : x^T A x+b^T x+c in I}|
 <2582 |I|,
```

and conversely this geometric inequality would imply the arbitrary cap-one product-law statement. Bounded finite-union product indicators may be used as epsilon-witnesses by regular approximation, but no single-interval extremality is claimed.

This is the designated fleet04/B13 result applied to an actual current inequality, not merely cited as background.

## 5. Updated regularity and theorem status

The newer fleet03/B15 fixed-instance regularity synthesis gives the current nine-direction theorem a canonical `C_0` representative with the same `<2582 K^2/s` height, including arbitrary affine terms. Thus continuity is solved at multiplicity nine.

Multiplicity eight remains **OPEN**. Its exact-zero strong-cross subchamber is paid; the nonzero weak-self chamber remains open and must use the six Schur spectral directions. The unrestricted three-large-eigenvalue conjecture remains **OPEN / not proved / not disproved**.

No Gaussianity, log-concavity, moment, compact-support assumption (outside the explicit uniform test law in the counterexample), connected-support assumption, diagonal-basis reduction, post-rotation independence, arbitrary-joint coarea bound, or law-uniform pointwise quadratic phase decay is used.
