# fleet01/B08 improvement — exact interpolation normal form and a sharper theorem constant

Run: `20260924T123752Z-fleet01-B08-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript: baseline `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This note contains two rigorous improvements and one rigorous barrier statement. It does **not** lower the 17-eigenvalue hypothesis.

## 1. Exact normal form behind `rank R<=3r`

Let `S,T` be a sampled disjoint seed of size `r`, let `L` be its complement, and write

```
A = [ C    B    G
      B^T  F    H
      G^T  H^T  J ],        B=A[S,T] invertible.
```

For the manuscript's nonsymmetric interpolant

```
P=A[:,T]B^{-1}A[S,:],
```

one has exactly

```
P[S,:]=A[S,:],
P[:,T]=A[:,T],
P[L,L]=H^T B^{-1}G.
```

After defining `D,E,R` exactly as in `lem:completion`, the matrix `R` is

```
R = [ C    B    G
      B^T  F    H
      G^T  H^T  H^T B^{-1}G ].                 (1)
```

Permute the columns of (1) to `T,S,L`. The leading `S x T` block becomes `B`. Since `B` is invertible, rank additivity under block Gaussian elimination gives

```
rank R = r + rank K,                             (2)
```

where

```
K = [ U  V
      W  0 ],                                    (3)

U=B^T-FB^{-1}C,
V=H-FB^{-1}G,
W=G^T-H^TB^{-1}C.
```

The first block row of `K` has only `r` rows and the first block column has only `r` columns, so

```
rank K <= 2r,
rank R <= 3r.                                    (4)
```

Meanwhile (1) gives separately

```
R[L,L]=H^TB^{-1}G,
rank R[L,L] <= r.                                (5)
```

Equations (2)–(5) are an exact structural refinement of the manuscript's support proof. They identify the only two extra global-rank currencies as the row defect `V` and column defect `W`.

### Sharpness

Take `delta=1/200` and the direct sum of `r` copies of

```
delta * [0 1 1
         1 0 1
         1 1 1].
```

Choose the first, second and third coordinate of each copy in `S,T,L` respectively. Then

```
B=delta I_r,
C=F=0,
G=H=delta I_r,
J=delta I_r=H^TB^{-1}G.
```

Hence the manuscript completion has `D=E=0` and `R=A`. Every `3 x 3` block has determinant `delta^3`, so

```
rank R=3r,
rank R[L,L]=r.
```

There is no `eta=1/100` pivot: diagonal entries are `0,0,delta`, and every principal `2 x 2` determinant has modulus at most `delta^2=1/40000<eta`. Thus the two rank bounds are simultaneously sharp even inside the local no-pivot entry class. A multiplicity improvement cannot come from replacing `3r` by `2r` on support grounds alone.

For `r=1`, (2) reduces to the exact identity

```
det R = ((b g-c h)(b h-f g))/b,
```

which exhibits the two independent defects `V` and `W` explicitly.

## 2. Why the same pipeline stops at order four

The manuscript's no-pivot spectral-to-volume lemma gives order `k` crossing volume from `4k-3` large singular values. For `k=4`, this would use 13 large directions. But the regularized determinant estimate gives only

```
|phi_Q(t)| <= min(1,(u/|t|)^(k/4))
            = min(1,u/|t|).                     (6)
```

The absolute integral of (6) diverges logarithmically. Therefore the manuscript's Fourier-inversion step cannot turn order-four volume into a uniform density bound. This is an actual endpoint obstruction in the present dependency chain, not a reason to assert that 13 is impossible.

The exact normal form above suggests a concrete successor: prove quantitative control of `V` and `W` from additional same-index bordered information and then convert that information into an extra disjoint crossing direction. Alternatively, establish a new endpoint receiver that turns the order-four determinant bound into Lipschitz small-ball control without assuming smoothness, moments, support connectedness or rotated independence.

## 3. Stronger final constant with no new hypothesis

The manuscript keeps the round bounds `H(Q)<=600`, `sup_a E|Q-a|^{-1/2}<=601`, then `6010<10000` in the main scalar-pivot branch. The displayed proof itself yields a better value.

Recall

```
L0 = 4+4 log 16.
```

For the scalar-pivot branch of `prop:pivot-H`, with `eta=1/100`,

```
H(Q)
 <= eta^{-1/2}(8+3L0)
 = 10(8+3(4+4 log16))
 = 200+120 log16.                               (7)
```

The full negative half moment differs from its truncated version by at most one, so the nine-eigenvalue result may be sharpened to

```
sup_a E|Q-a|^{-1/2}
 <= 201+120 log16.                               (8)
```

At a scalar pivot in the main theorem, another factor `eta^{-1/2}=10` gives

```
||p_Q||_infinity
 <= 2010+1200 log16
 = 5337.106466687737...                          (9)
```

in the normalized case. The other manuscript branches remain below `2400`. Scaling exactly as in `thm:main` therefore gives the strengthened theorem

```
s_17(A)>=s>0
  => ||p_(X^TAX+b^TX+c)||_infinity
     <= (2010+1200 log16) K^2/s
     < 5338 K^2/s.                               (10)
```

This preserves every theorem hypothesis and all affine terms. It is a **constant improvement**, not a multiplicity improvement.

## Status

- Exact nonsymmetric interpolation normal form: **PROVED**.
- Simultaneous sharpness of global/restricted rank bounds inside the no-pivot entry class: **PROVED**.
- Reduction `17 -> 13` by the existing order-four Fourier route: **NOT PROVED; endpoint `1/|t|` is nonintegrable**.
- Constant `10000 -> 5338` under the same `s_17` hypothesis: **PROVED from existing manuscript estimates**.
