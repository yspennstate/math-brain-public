# Bent markers separate worst-coordinate and favorable-coordinate restriction defects

Status: proved below and self-checked; novelty **UNVERIFIED**. This is a sharper
analysis of the family in `SHANNON_POTENTIAL_BARRIER_2026-09-18.md`. It neither
proves nor disproves a constant-factor favorable-coordinate theorem and does not
solve FEI. **This intermediate note is superseded for the general restriction
question by `SYMMETRIC_MOD8_RESTRICTION_BARRIER_2026-09-18.md`, which does
disprove every constant-factor favorable-coordinate and aggregate inequality.**

All logarithms are base two unless `ln` is written. For an indicator `A`, let

    W_c(A)=U(A)+c Q_A,

where `U` is the complement-invariant logarithmic potential and `Q_A` is the
singleton Fourier-square mass defined in the preceding note. The unequal-NAND
potential is `V=W_{2/ln2}`.

## 1. Result

For the bent-marker indicator `A` on `m+1` bits from the preceding note, put

    epsilon=2^(-m/2),       delta=epsilon^2,

where `m` is positive and even. Write

    D_i=W_c(A)-[W_c(A_{i=0})+W_c(A_{i=1})]/2.          (1)

For every fixed real `c`, all `m` data coordinates have the same defect

    D_data=[(m+2)/(8 ln2)] epsilon+O_c(m^2 epsilon^2), (2)

whereas the selector coordinate has

    D_sel=[1/4+1/(2 ln2)+o(1)]m epsilon^2.             (3)

Consequently, for every fixed `c` and all sufficiently large even `m`,

    D_i>0 for every coordinate i.                              (4)

Thus the local obstruction is not confined to the marked selector: this
family eventually has no nonincreasing coordinate at all.

On the other hand, the Boolean influences are exactly

    Inf_sel(1-2A)=epsilon^2,
    Inf_data(1-2A)=1/2+epsilon^2.                      (5)

Therefore

    D_sel/Inf_sel=[1/4+1/(2 ln2)+o(1)]m -> infinity,
    D_data/Inf_data=[(m+2)/(4 ln2)]epsilon
                       +O_c(m^2 epsilon^2) -> 0.       (6)

The same example hence exhibits an unbounded worst-coordinate ratio while
its best-coordinate ratio tends to zero. Its aggregate ratio also tends to
zero:

    [sum_i D_i]/[sum_i Inf_i]
       =[(m+2)/(4 ln2)]epsilon+O_c(m^2 epsilon^2).      (7)

This cleanly separates three possible restriction statements:

1. a uniform inequality for every coordinate is false by (3);
2. a zero-charge descent coordinate is false by (4);
3. a constant-charge favorable coordinate, or an aggregate inequality, is
   **not** refuted by this family, by (6)--(7).

## 2. Construction recalled

Let

    g(x)=(-1)^(x_1x_2+...+x_(m-1)x_m)

and let `g'` be obtained by flipping `g(0)=1`. Let the selector function `F`
have restrictions `g,g'`, and put `A=(1-F)/2`. The selector analysis is
exactly the proof of (3) in the preceding note. It remains to analyze a data
coordinate, say `x_1`.

Write

    h(y)=(-1)^(x_3x_4+...+x_(m-1)x_m),

so `g(x)=(-1)^(x_1x_2)h(y)`. By symmetry the calculation for `x_1` applies to
every data coordinate.

## 3. The easy data restriction

When `x_1=1`, the marker point is absent and

    F_{x_1=1}=(-1)^(x_2)h(y),

independently of the selector. Its nonzero Fourier coefficients have common
magnitude `2 epsilon` and their supports all contain `x_2`. Hence the
nonconstant indicator coefficients have common square `epsilon^2`; the only
singleton among them is `{x_2}`. All internal positive spectral edges have
equal endpoint masses. It follows exactly that

    W_c(A_{x_1=1})=h_2(epsilon^2)+c epsilon^2
                   =(m+c)epsilon^2,                    (8)

where `h_2(t)=-t log t`.

## 4. The marked data restriction

When `x_1=0`, the base function is `h(y)`, independent of `x_2`, and the
one-point marker remains in the branch with selector one. Put

    d=m-2,             M=2^(m-2),
    z_+=epsilon^2(1-epsilon)^2,
    z_-=epsilon^2(1+epsilon)^2,
    y_0=epsilon^4,
    n_+=(M+sqrt(M))/2, n_-=(M-sqrt(M))/2.              (9)

In the selector-free spectral layer, sets not containing `x_2` have masses
`z_+` or `z_-` according to the Walsh sign of `h`; sets containing `x_2` have
mass `y_0`. The selector layer has constant mass `y_0`.

There are `dM/4` sign-changing edges in the `y` directions. Both the `x_2`
direction and the selector direction contribute the same large-to-small edge
sum; in either direction the edge at the empty set is omitted from the
internal sum. The singleton masses are `y_0,y_0` in those two directions and
`z_+` in each of the `d` remaining directions. Consequently the exact formula
is

    W_c(A_{x_1=0})
      =(dM/4) z_+ log(z_-/z_+)
       +2y_0[(n_+-1)log(z_+/y_0)+n_-log(z_-/y_0)]
       +2h_2(y_0)+d h_2(z_+)+c(2y_0+d z_+).            (10)

This formula includes `m=2`, using the usual zero-mass continuity convention.

## 5. Asymptotic data defect

For the unrestricted marker, the exact formula in the preceding note has
leading data-edge term

    (m/16)(1-epsilon)^2
       log[((1+epsilon)/(1-epsilon))^2]
      =[m/(4ln2)]epsilon+O(m epsilon^2).                (11)

Every other term in that full potential is `O_c(m^2 epsilon^2)`: there are
`O(epsilon^-2)` selector edges of mass `O(epsilon^4)` and logarithmic contrast
`O(m)`, while all singleton terms have total size
`O_c(m^2 epsilon^2)`.

In (10), the first term is

    [(m-2)/(4ln2)]epsilon+O(m epsilon^2),               (12)

by the same expansion. Its remaining terms are again
`O_c(m^2 epsilon^2)`, and (8) has that order as well. Subtracting half of
(8) and (10) from (11) yields

    D_data
      ={2m-(m-2)\over 8ln2}epsilon+O_c(m^2 epsilon^2)
      =[(m+2)/(8ln2)]epsilon+O_c(m^2 epsilon^2),

which proves (2). Since `m epsilon -> 0`, the error divided by the positive
leading term tends to zero; hence (4) follows from (2) and (3).

For (5), the selector restrictions differ at one of `2^m` points. In a data
direction the unmarked quadratic bent function has influence `1/2` in each
selector slice. Flipping the marked value changes the formerly agreeing edge
incident to zero into a disagreeing edge, adding exactly `epsilon^2` to the
normalized Boolean influence. Equations (6)--(7) now follow by substitution.

## 6. What this family leaves open

For this family alone, the remaining restriction question would be whether a
universal constant `C` guarantees some coordinate satisfying

    D_i <= C Inf_i,

or a suitable aggregate/block substitute. The bent marker forces `C>0` and
simultaneously shows why controlling the maximum local ratio is unnecessary.
It supplies no counterexample to a finite `C`. The later transitive mod-8
family supplies exactly that counterexample for both coordinate statements;
only a genuinely nonlocal block mechanism could still survive.

`check_favorable_coordinate_separation.py` verifies (8)--(10) against full
Walsh transforms and certifies the sign pattern for the actual unequal-NAND
potential through `m=12`, using exact rational arithmetic and outward rational
logarithm intervals. The all-large-`m` statements are proved above, not
inferred from the finite check. This is a self-check, not an independent audit.
