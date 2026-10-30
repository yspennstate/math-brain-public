# fleet02/B08 r3 — rank-sharp completion family and the multiplicity-eight saturation packet

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T143645Z-fleet02-B08-fixedmult-audit-r3`  
Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **proved structural improvement / counterexample to stronger rank bookkeeping; no multiplicity-eight L-infinity theorem claimed.**

## 1. A stronger exact sharpness family

Fix `r>=1` and `0<delta<1/10`. Partition the coordinates into three `r`-sets `S,T,L`, and put

```text
A = [ 0          delta^2 I   delta I
      delta^2 I  0           delta I
      delta I    delta I     0       ].
```

This is symmetric. The sampled seed is

```text
B=A[S,T]=delta^2 I_r.
```

The manuscript interpolation is therefore exactly

```text
P=A[:,T] B^{-1} A[S,:]
 = [ 0  delta^2 I  delta I
     0  0          0
     0  delta I    I ].
```

On `L x L`, `A-P=-I_r` is diagonal, hence the completion of Lemma 6.2 has

```text
F=0,   E=0,   D=diag(0_S,0_T,-I_L),
R=A-D
 = [ 0          delta^2 I  delta I
     delta^2 I  0          delta I
     delta I    delta I     I       ].
```

For one three-coordinate component,

```text
P_0 = [0 delta^2 delta; 0 0 0; 0 delta 1],
R_0 = [0 delta^2 delta; delta^2 0 delta; delta delta 1].
```

Direct determinants give `det(R_0)=delta^4` and `rank(P_0)=1`; also `rank(R_0-P_0)=2`. Therefore block additivity gives the simultaneous exact equalities

```text
rank P                 = r,
rank(R-P)              = 2r,
rank R                 = 3r,
rank R[L,L]            = r.
```

Moreover the rows-`T` support part of `R-P` has rank exactly `r`, and after removing those rows the remaining columns-`S` support part also has rank exactly `r`. Thus *each individual rank charge* in the manuscript support proof is sharp. Here `R` is already symmetric and `E=0`; symmetry or near-symmetry of the final corrected matrix cannot by itself lower the global `3r` coefficient.

The family is genuinely no-pivot: every diagonal entry of `A` is zero, and every principal two-coordinate determinant is `-a_ij^2`, whose modulus is at most `delta^2<1/100=eta`.

There is a further exact volume obstruction. After permuting coordinates, `A` is a direct sum of `r` three-coordinate components. For a disjoint square minor, each component must contribute the same number of selected rows and selected columns. Since the row and column sets are disjoint inside a three-coordinate component, that common number is at most one. Hence every disjoint minor of order `r+1` vanishes:

```text
V_{r+1}(A)=0.
```

So the package `E=0`, exact symmetry of `R`, target-scale diagonal `D`, sharp global/restricted ranks, and zero next disjoint volume is algebraically compatible. This is a counterexample to any attempt to improve the threshold by rank/support bookkeeping alone. It is **not** a counterexample to a spectral theorem: the displayed `A` has only `3r` nonzero eigenvalues and, for small `delta`, its singular values are small.

For the current threshold-eight problem the specialization `r=2` is particularly relevant: it has `V_3(A)=0`, `rank R=6`, `rank R[L,L]=2`, and two unit diagonal entries in `D`, while remaining no-pivot. Thus any proof of `s_8 => V_3>0` must genuinely use the two extra spectral directions; the completion pattern alone does not force order-three volume.

## 2. Robust saturation packet forced by a hypothetical unpaid s8 state

Normalize `K=s=1`, and keep the baseline constants

```text
eta=1/100,   kappa=1/80^2.
```

Assume

```text
A=A^T,  A has no eta-pivot,  s_8(A)>=1,  V_3(A)<kappa^3.
```

Apply exactly the manuscript telescoping/sampling/completion argument. It produces a seed order `r<=2` with

```text
||E|| <= ||E||_F < (r+1)/80,
rank R <= 3r,
rank R[L,L] <= r,
A=D+R+E,
D=0 on the seed,
diag(E)=0.
```

The case `r<=1` is already impossible by the manuscript diagonal-dominance contradiction because `8>=4r+1`. Hence necessarily

```text
r=2,   ||E||_F<3/80,   rank R<=6,   rank R[L,L]<=2.             (2.1)
```

The no-pivot estimate can be kept sharper than the manuscript's convenient `1/7`:

```text
|A_ij|^2 < eta+eta^2=101/10000,
so |A_ij| < sqrt(101)/100 < 11/100.                              (2.2)
```

### At most two D-sites can be >=3/10

Suppose three indices `H subset L` satisfied `|D_ii|>=3/10`. Since `|A_ii|<1/100` and `E_ii=0`,

```text
|R_ii|>29/100.
```

For each row of the `3 x 3` block `R[H,H]`, the two off-diagonal `A` entries contribute less than `22/100`, while Cauchy-Schwarz and (2.1) give

```text
sum_{j in H, j!=i}|E_ij| <= sqrt(2)||E||_F < 3sqrt(2)/80 < 9/160.
```

Therefore

```text
sum_{j!=i}|R_ij| < 11/50+9/160 = 221/800 < 232/800 = 29/100.
```

Strict row diagonal dominance would make `R[H,H]` invertible, contradicting `rank R[L,L]<=2`. Thus at most two diagonal entries of `D` have modulus at least `3/10`.

Let `H` be the set of those entries, `h=|H|<=2`, let `D_H` retain only them, and put `D_0=D-D_H`. Then `||D_0||<3/10`. Since

```text
s_8(D+R)=s_8(A-E)>1-3/80=77/80,
```

singular-value perturbation gives

```text
s_8(D_H+R)>77/80-3/10=53/80.                                   (2.3)
```

But `rank(D_H+R)<=h+6<=8`. The positive eighth singular value in (2.3) forces equality throughout:

```text
h=2,
rank R=6,
rank(D_H+R)=8.                                                   (2.4)
```

Applying the rank-four-shift inequality here with the actual rank-two matrix `D_H` gives

```text
s_6(R) >= s_8(D_H+R) > 53/80.                                  (2.5)
```

### The restricted carrier is exactly rank two and quantitatively nondegenerate

On the two-site set `H`, again `|R_ii|>29/100`. There is only one off-diagonal competitor per row, and

```text
|R_ij| <= |A_ij|+|E_ij| < 11/100+3/80 = 59/400.
```

Hence the row-dominance margin is strictly larger than

```text
29/100-59/400 = 57/400.                                        (2.6)
```

Thus `R[H,H]=P[H,H]` is invertible. Consequently

```text
rank R[L,L]=rank P=2.                                           (2.7)
```

The max-coordinate proof of diagonal dominance also gives, for every `x in R^2`,

```text
||P[H,H]x||_2 > (57/400)||x||_infinity >= (57/(400 sqrt(2)))||x||_2,
```

so

```text
s_2(P) >= s_2(P[H,H]) > 57/(400 sqrt(2)) > 1/10.                (2.8)
```

### Exact rank saturation plus near-symmetric spectral collar

Because `A,D` are symmetric,

```text
R-R^T=E^T-E.
```

Let `R_s=(R+R^T)/2`. Then

```text
||R_s-R|| < 3/80.                                               (2.9)
```

Combining (2.5) with (2.9), while `rank R=6`, yields

```text
s_6(R_s)>53/80-3/80=5/8,
s_7(R_s)<3/80.                                                   (2.10)
```

Since `R_s` is symmetric, it therefore has six genuine eigenvalues of modulus greater than `5/8`, while every remaining eigenvalue has modulus below `3/80`.

Finally (2.4) is equality in the rank sum `rank(D_H+R)<=rank D_H+rank R`. Hence both the column spaces and the row spaces are direct sums:

```text
Col(R) intersect span{e_h:h in H} = {0},
Row(R) intersect span{e_h:h in H} = {0}.                         (2.11)
```

## 3. Consequence for the threshold frontier

The multiplicity-nine replacement proof is compatible with the baseline rank mechanism because its no-pivot branch uses order three, for which the manuscript count is exactly `4*3-3=9`.

At multiplicity eight, an unpaid state cannot be treated as an arbitrary one-direction-short failure. The interpolation argument forces the very rigid packet (2.1)--(2.11): exactly two large diagonal sites, exact global rank six, exact restricted rank two, a well-conditioned restricted interpolation core, and a symmetric rank-six spectral cluster separated from the remaining spectrum.

The exact family in Section 1 shows that the algebraic rank/support part of this packet can be saturated with `V_3=0`; therefore a true multiplicity-eight L-infinity proof must use additional spectral/analytic information beyond a generic improvement of `rank R<=3r` or `rank R[L,L]<=r`.

This artifact does **not** claim the multiplicity-eight bounded-density theorem and does not address unrestricted three-eigenvalue QFORM.