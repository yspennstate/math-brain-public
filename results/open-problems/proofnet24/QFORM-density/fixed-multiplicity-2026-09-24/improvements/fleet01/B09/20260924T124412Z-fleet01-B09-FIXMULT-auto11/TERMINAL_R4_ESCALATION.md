# QFORM-S16-TERMINAL-R4-DETERMINANT-ESCALATION-v1

Run: `20260924T124412Z-fleet01-B09-FIXMULT-auto11`
Baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Status: **new supporting structural theorem; not a 16-eigenvalue density theorem**.

## Statement

Use the manuscript constants

\[
\eta=10^{-2},\qquad \kappa=80^{-2}.
\]

Let `A=A^T` have no `eta`-pivot and satisfy `s_16(A)>=1`. Let `S,T` be disjoint four-sets with

\[
B=A_{S,T}
\]

invertible. Put `L=[n]\setminus(S\cup T)` and form the manuscript interpolation

\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot},
\qquad
E_{L,L}=\operatorname{off}(A_{L,L}-P_{L,L}),
\]

with all other entries of `E` zero. Assume

\[
\|E\|_F\le\frac1{16}.
\]

Then there exists a four-set `H subset L` such that `P_{H,H}` is quantitatively invertible. Define

\[
a:=\sqrt{\eta+\eta^2}=\frac{\sqrt{101}}{100},
\]

and

\[
\delta:=\frac{371}{400}-3\left(a+\frac1{16}\right)
=\frac{74-3\sqrt{101}}{100}
=0.438503731366\ldots>0.
\]

Then

\[
\boxed{\sigma_{\min}(P_{H,H})\ge\delta},
\qquad
\boxed{|\det P_{H,H}|\ge\delta^4}.
\]

Writing

\[
C=A_{H,T},\qquad G=A_{S,H},
\]

one has the exact factorization

\[
P_{H,H}=CB^{-1}G
\]

and hence

\[
\boxed{|\det C|\,|\det G|\ge\delta^4|\det B|}.
\]

Because all entries joining disjoint coordinate banks have modulus `<a`, Hadamard gives

\[
|\det C|,|\det G|\le M:=(2a)^4
=0.00163216.
\]

Consequently

\[
\boxed{|\det B|\le \frac{M^2}{\delta^4}
=7.2049718338\times10^{-5}},
\]

and at least one of the two alternative disjoint four-by-four physical minors satisfies

\[
\boxed{
\max\{|\det A_{H,T}|,|\det A_{S,H}|\}
\ge\delta^2\sqrt{|\det A_{S,T}|}
\ge R\,|\det A_{S,T}|
}
\]

with the universal escalation factor

\[
\boxed{R:=\frac{\delta^4}{M}=22.6532460869\ldots>22.65.}
\]

Thus an order-four seed with completion residual at most `1/16` cannot be a maximal-magnitude disjoint order-four seed. Iterating the implication along successively larger determinants must eventually reach a seed whose completion residual exceeds `1/16`.

## Proof

The manuscript completion for `r=4` writes

\[
A=D+R_0+E,
\]

where

\[
\operatorname{rank}R_0\le12,
\qquad
(R_0)_{L,L}=P_{L,L},
\qquad
\operatorname{rank}(R_0)_{L,L}\le4,
\qquad
D|_{S\cup T}=0,
\]

and `E` has zero diagonal. Since `s_16(A)>=1` and `||E||<=||E||_F<=1/16`, nonsymmetric singular-value perturbation gives

\[
s_{16}(D+R_0)=s_{16}(A-E)\ge\frac{15}{16}.
\]

The global rank bound `rank R_0<=12` therefore yields

\[
s_4(D)\ge\frac{15}{16}.
\]

Hence at least four diagonal entries of `D` have modulus at least `15/16`. Since `D` vanishes on `S union T`, choose four such coordinates in `L` and call the set `H`.

For `i in H`, zero diagonal of `E` and the no-pivot bound `|A_ii|<eta=1/100` imply

\[
|(R_0)_{ii}|
=|A_{ii}-D_{ii}|
\ge\frac{15}{16}-\frac1{100}
=\frac{371}{400}.
\]

For distinct `i,j in H`, the no-pivot condition gives

\[
|A_{ij}|^2<\eta+\eta^2,
\qquad |A_{ij}|<a=\frac{\sqrt{101}}{100},
\]

while `|E_ij|<=||E||_F<=1/16`. Therefore

\[
|(R_0)_{ij}|=|A_{ij}-E_{ij}|<a+\frac1{16}.
\]

Because `|H|=4`, every row and every column of `(R_0)_{H,H}=P_{H,H}` has diagonal modulus at least `371/400` and total off-diagonal modulus strictly less than `3(a+1/16)`. The strict row and column diagonal-dominance gap is precisely `delta`.

For completeness, row diagonal dominance gives the inverse norm estimate directly. If `Px=y` and `|x_i|=||x||_infty`, then

\[
\delta |x_i|\le |y_i|\le||y||_infty,
\]

so

\[
||P^{-1}||_\infty\le\delta^{-1}.
\]

Apply the same argument to `P^T` to get `||P^{-1}||_1<=delta^{-1}`. Hence

\[
||P^{-1}||_2
\le\sqrt{||P^{-1}||_1||P^{-1}||_\infty}
\le\delta^{-1}.
\]

Thus `sigma_min(P)>=delta`, and the product of the four singular values gives `|det P|>=delta^4`.

The interpolation identity gives

\[
P_{H,H}=A_{H,T}B^{-1}A_{S,H}=CB^{-1}G,
\]

so determinant multiplicativity proves

\[
|\det C|\,|\det G|=|\det P_{H,H}|\,|\det B|
\ge\delta^4|\det B|.
\]

Because `H,T,S` are pairwise disjoint, every entry of `C` and `G` is off-diagonal in the original matrix. Each is strictly smaller than `a` in modulus. Every row therefore has Euclidean norm `<2a`, and Hadamard yields

\[
|\det C|,|\det G|\le(2a)^4=M.
\]

The product lower bound and the two upper bounds give

\[
|\det B|\le M^2/\delta^4.
\]

Also

\[
\max(|\det C|,|\det G|)
\ge\sqrt{|\det C|\,|\det G|}
\ge\delta^2\sqrt{|\det B|}.
\]

Finally `|det B|<=M^2/delta^4` implies

\[
\frac{\delta^2}{\sqrt{|\det B|}}
\ge\frac{\delta^4}{M}=R,
\]

which proves the escalation inequality.

## Exact relation to the 17 -> 16 obstruction

The baseline proof needs five large complement diagonal directions in the terminal `r=4` chamber to contradict `rank P_{L,L}<=4`; `s_16` forces only four. The theorem above extracts what the saturated case still gives: not merely invertibility of the three-bank maps, but a quantitative determinant gain by a factor `>22.65` to another physical disjoint order-four seed whenever the current seed has small completion residual.

This is stronger than the qualitative statement that `A_{H,T}` and `A_{S,H}` are invertible.

However, **this does not yet close the 16-eigenvalue theorem.** The volume-sampling argument guarantees a low-residual seed in determinant-squared average. The larger seed produced above can have residual `>1/16`; converting that event into a dimension-free lower bound for `V_5/V_4`, or back into an `O(|I|)` density receiver, still needs an additional aggregate argument. A single high-residual seed can carry arbitrarily small determinant-squared weight relative to `V_4` in high dimension. Therefore no multiplicity reduction is claimed.

## Interaction with the order-four analytic endpoint

A separate completed worker result proves an integrable order-four Fourier envelope under a diffuse row- or column-leverage condition. The present theorem addresses the complementary algebraic `r=4` saturation but does not force such a leverage condition. A plausible next step is therefore a dimension-free trichotomy for the terminal seed:

1. diffuse leverage -> the existing order-four endpoint receiver;
2. low completion residual -> determinant escalation as above;
3. high completion residual -> aggregate fifth-volume or a direct shared-coordinate receiver.

Only item 2 is proved here.
