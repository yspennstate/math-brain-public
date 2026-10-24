# Fresh-correction addendum — affine hyperbolic L2 packet

A new correction appeared after the main report was archived:

`QFORM-O1-PIVOT-SCALE-FROM-MASS-FALSE-v1`, brain commit `b217c7e6427570220a79b3d7a409a1a9d41f76dc`, canonical math-open-problems report `41ed0a3af4b1aec79c036031a00066b0f49a9a45`.

It correctly refutes any inference that O1 determinant mass forces a non-negligible scalar diagonal pivot. The main report did not make that inference: its O1 formula explicitly retains the factor `|d|^(-1/4)` and names the near-zero pivot as unpaid. The correction instead suggests an inverse-free hyperbolic packet. The following new theorem supplies exactly such an integrated-Fourier resource.

## Theorem `QFORM-AFFINE-HYPERBOLIC-L2-v1`

Let `X,U` be independent real random variables. Assume `X` has a probability density `f` with `0<=f<=1`, and `U` has probability density `g` with `||g||_infinity<=M`. Let `a!=0` and let `h:R->R` be arbitrary measurable. Put

`T = 2a XU + h(X)`.                                                   (A.1)

Then `T` has an `L^2` density and

`||p_T||_2 <= 2 sqrt(M/|a|)`.                                        (A.2)

Equivalently, for the Fourier convention `phi_T(t)=E exp(itT)`,

`||phi_T||_2 <= 2 sqrt(2pi M/|a|)`.                                  (A.3)

### Proof

Condition on `X=x`. Away from the null set `x=0`, the conditional density is

`p_x(z) = [1/(2|a x|)] g((z-h(x))/(2a x))`.

Therefore

`||p_x||_2 = (2|a x|)^(-1/2)||g||_2`.

Minkowski gives

`||p_T||_2
 <= ||g||_2 / sqrt(2|a|) * int f(x)|x|^(-1/2) dx`.                 (A.4)

Since `f<=1` and `int f=1`, the bathtub/rearrangement bound for the symmetric decreasing kernel `|x|^(-1/2)` is

`int f(x)|x|^(-1/2) dx
 <= int_{-1/2}^{1/2}|x|^(-1/2)dx
 =2sqrt(2)`.                                                          (A.5)

Also `||g||_2^2<=||g||_infinity||g||_1<=M`. Substitution in (A.4) yields (A.2), and Plancherel yields (A.3). No pointwise oscillatory estimate is used, and the arbitrary affine/self term `h(X)` costs nothing.

## Two independent hyperbolic packets give full `L1_t`

If

`T_1=2a XU+h(X)`, `T_2=2b VW+k(V)`

are built from disjoint independent coordinate banks and the two aggregate variables have density caps `M_1,M_2`, then for any further independent additive term `N`,

`Q=T_1+T_2+N`

satisfies by Cauchy--Schwarz and `|phi_N|<=1`

`||phi_Q||_1
 <= ||phi_T1||_2 ||phi_T2||_2
 <= 8pi sqrt(M_1 M_2/(|ab|)).`                                      (A.6)

Hence Fourier inversion gives a continuous density vanishing at infinity and

`||p_Q||_infinity <=4 sqrt(M_1 M_2/(|ab|)).`                         (A.7)

This is a genuine uniform **integrated characteristic-function estimate without pointwise decay**.

## Apply to the fresh O1 counterexample family

The correction uses the symmetric five-coordinate matrix with

`A_00=epsilon`, `A_01=A_03=A_24=1`,

all other upper-triangular entries zero. Thus

`Q = epsilon X_0^2 +2X_0(X_1+X_3)+2X_2X_4`.                          (A.8)

Let `U=X_1+X_3`. Because convolution with a probability density does not increase the `L^infinity` cap,

`||p_U||_infinity<=1`.

The first packet in (A.8) is (A.1) with `a=1`, `h(x)=epsilon x^2`, `M=1`; the second is (A.1) with `a=1`, `h=0`, `M=1`. They use disjoint original-coordinate banks. Consequently, for **every real epsilon** and every independent cap-one input law,

`||phi_Q||_1 <=8pi`,
`||p_Q||_infinity <=4`,                                              (A.9)

and the output density is continuous and vanishes at infinity.

Thus the fresh correction is a genuine refutation of scalar-pivot extraction but not an obstruction to integrated Fourier smoothing: its entire counterexample family is uniformly paid by two physical hyperbolic packets, including the singular endpoint `epsilon=0`.

## Updated first unpaid implication

For O1 mass near a zero scalar pivot, the correct target is now an **aggregate two-hyperbolic-packet extraction** retaining disjoint original-coordinate banks, not a lower bound on the scalar pivot. The theorem above completely pays any such extraction once the two aggregate linear variables have dimension-free density caps. What remains is the structural extraction from general O1/O2 overlap mass; conditional projected caps or post-rotation independence remain forbidden.
