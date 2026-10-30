# QFORM-FIXED-MULTIPLICITY-17-PARAMETER-RETUNING-2100-v1

**Status:** proved improvement of the numerical constant for the same 17-eigenvalue theorem; **no multiplicity reduction and no `s_3` claim**.

Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

The baseline chose `eta=1/100`, `kappa=1/80^2` for convenient arithmetic and then rounded the final constant to `10000`. The proof has substantial slack. Retuning only those two deterministic thresholds gives the following stronger theorem with every matrix/law/affine hypothesis unchanged.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K`. Let `A=A^T`, `b` arbitrary and `c` arbitrary. If

\[
s_{17}(A)\ge s>0,
\]

then `X^TAX+b^TX+c` has a density and

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
<2100\,\frac{K^2}{s}.}
\]

No iid, moment, support, sign, rank, definiteness, smoothness, leverage or exact-spectrum assumption is added.

## 1. New normalized parameters

As in the manuscript, reduce first to `K=s=1`. Replace only equation `(1.2)` by

\[
\boxed{
\eta=\frac9{352},\qquad
\sqrt\kappa=\frac4{307},\qquad
\kappa=\frac{16}{94249}.}
\tag{1}
\]

A useful feature is that

\[
\eta+\eta^2
=\frac{9}{352}\frac{361}{352}
=\left(\frac{57}{352}\right)^2.
\tag{2}
\]

Hence, if there is no `eta`-pivot, the manuscript's principal `2x2` determinant argument gives exactly

\[
|a_{ii}|<\frac9{352},
\qquad
|a_{ij}|<q:=\frac{57}{352}\quad(i\ne j).
\tag{3}
\]

All analytic lemmas in the manuscript are parameter-independent. The only point requiring a new proof is the spectral-to-volume proposition with these larger thresholds.

## 2. Retuned spectral-to-volume proposition

### Claim
For `1<=k<=5`, if `A=A^T` has no `eta`-pivot and `s_{4k-3}(A)>=1`, then

\[
V_k(A)\ge\kappa^k
\tag{4}
\]

with the parameters in (1).

### Proof
Assume `V_k<kappa^k`. Exactly as in the manuscript's telescoping argument, there exists `0<=r<=k-1` with `V_r>0` and

\[
V_{r+1}<\kappa V_r.
\tag{5}
\]

If `r=0`, then

\[
\|\operatorname{off}A\|_F<\sqrt\kappa=\frac4{307},
\]

and therefore

\[
\|A\|
\le\|\operatorname{diag}A\|+\|\operatorname{off}A\|_F
<\frac9{352}+\frac4{307}<1,
\]

contradicting `s_{4k-3}(A)>=1`.

Now let `1<=r<=4`. The volume-sampled interpolation and completion lemmas of the manuscript give

\[
A=D+R+E,
\qquad
\operatorname{rank}R\le3r,
\qquad
\operatorname{rank}R_{L,L}\le r,
\]

with `D=0` on the `2r` seed coordinates and

\[
\varepsilon:=\|E\|_F
\le(r+1)\sqrt{V_{r+1}/V_r}
<(r+1)\frac4{307}.
\tag{6}
\]

Put `m=4k-3`. Since `r<=k-1`, `m>=4r+1`. The manuscript's singular-value rank inequality therefore forces at least `r+1` diagonal entries of `D`, all in `L`, to have modulus at least `1-epsilon`. Choose such an `(r+1)`-set `H subset L`.

For `i in H`, because `E_ii=0`,

\[
|R_{ii}|>1-\varepsilon-\eta.
\tag{7}
\]

For distinct `i,j in H`, (3) and `|E_ij|<=epsilon` give

\[
|R_{ij}|<q+\varepsilon.
\tag{8}
\]

Thus strict row diagonal dominance follows provided

\[
1-\eta-rq>(r+1)\varepsilon.
\]

By (6), it is enough that

\[
1-\eta-rq>\frac{4(r+1)^2}{307}.
\tag{9}
\]

The left side decreases with `r` and the right side increases, so only `r=4` needs checking. There (9) is the exact rational inequality

\[
\frac{115}{352}>rac{100}{307},
\]

because

\[
115\cdot307-100\cdot352=105>0.
\tag{10}
\]

Hence `R_{H,H}` is invertible and has rank `r+1`, contradicting `rank R_{L,L}<=r`. This proves (4). QED.

The argument is the manuscript's full nonsymmetric interpolation argument, not a new spectral truncation. All random variables remain in original coordinates.

## 3. Retuned no-pivot analytic constants

The random-coordinate-cut identity is unchanged. From (4), for `k=3` or `5`, some physical cut has

\[
Z_k^{-1/(2k)}
\le2\kappa^{-1/2}
=2\frac{307}{4}
=\frac{307}{2}.
\tag{11}
\]

Therefore the manuscript's order-five receiver gives

\[
\boxed{
\|p_Q\|_\infty
\le5e\frac{307}{2}
=\frac{1535e}{2}
=2086.281303\ldots .}
\tag{12}
\]

The order-three Riesz receiver gives the full half-potential bound

\[
\boxed{
\sup_a\mathbb E|Q-a|^{-1/2}
\le12\sqrt{\frac e2\frac{307}{2}}
=6\sqrt{307e}.}
\tag{13}
\]

## 4. Retuned pivot half-potentials

Put

\[
L_0=4+4\log16,
\qquad
C_{\rm sq}:=8+3L_0=20+12\log16.
\tag{14}
\]

The scalar-pivot proof in the manuscript now gives the truncated half-potential

\[
H(Q)\le\eta^{-1/2}C_{\rm sq}
=\frac{4\sqrt{22}}3(20+12\log16).
\tag{15}
\]

The definite-pair branch gives

\[
H(Q)\le4\pi\eta^{-1/2},
\tag{16}
\]

and the indefinite-pair branch gives

\[
H(Q)
\le\eta^{-1/2}(32+4\log16)+4/e.
\tag{17}
\]

Combining (13), (15)–(17) exactly as in Proposition `prop:nine`, every quadratic form with `s_9>=1` has full half-potential at most one plus the maximum of those four quantities.

## 5. Main scalar-pivot branch is below 2100

At a main scalar pivot, multiplication by `eta^{-1/2}=4sqrt(22)/3` converts the four possible nine-direction half-potential bounds into the following density bounds (including the outer `+1` tail):

\[
C_1
=\frac{352}{9}(20+12\log16)+\frac{4\sqrt{22}}3,
\tag{18}
\]

\[
C_2
=\frac{1408\pi}{9}+\frac{4\sqrt{22}}3,
\tag{19}
\]

\[
C_3
=\frac{352}{9}(32+4\log16)
+\frac{4\sqrt{22}}3\left(1+\frac4e\right),
\tag{20}
\]

and

\[
C_4
=8\sqrt{6754e}+\frac{4\sqrt{22}}3.
\tag{21}
\]

Each is `<2100`. For an entirely elementary verification, `pi<4`, `sqrt(22)<19/4`, and `e<3` make (19) and (21) much smaller than 2100. Also `e>2`. Finally

\[
\log16=4\log2<2.8,
\tag{22}
\]

because

\[
e^{0.7}>1+0.7+0.7^2/2+0.7^3/6>2.
\]

Using (22),

\[
C_1
<\frac{352}{9}(53.6)+\frac{19}{3}
<2100,
\tag{23}
\]

and (20) is even smaller (less than 1710 under the same crude bounds). Numerically, the actual dominant scalar-pivot value in (18) is

\[
C_1=2089.744416873\ldots .
\tag{24}
\]

## 6. The other main branches

The no-pivot branch is (12). To check it is `<2100` without decimal assumptions, the exponential series gives

\[
e
<\sum_{n=0}^7\frac1{n!}+\frac1{8!}\sum_{j=0}^\infty9^{-j}
=\frac{685}{252}+\frac1{35840}
<2.719.
\tag{25}
\]

Hence

\[
\frac{1535e}{2}<2087<2100.
\tag{26}
\]

A definite main pair has density at most

\[
\pi\eta^{-1/2}=\frac{4\pi\sqrt{22}}3<26.
\tag{27}
\]

For an indefinite main pair, the manuscript's log-potential argument gives

\[
\eta^{-1/2}(10+5\log16)+1/e<151
\tag{28}
\]

using (22), `sqrt(22)<19/4`, and `e>2`.

Thus every normalized main branch is `<2100`.

## 7. Scaling

For general density cap `K` and spectral scale `s`, make exactly the manuscript substitution

\[
Y=KX,
\qquad
\widetilde Q
=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\qquad
Q=(s/K^2)\widetilde Q.
\]

The coordinate densities of `Y` are bounded by one and `s_17(A/s)>=1`. Applying the normalized estimate and scaling the scalar output density proves

\[
\boxed{
\|p_Q\|_\infty<2100\,K^2/s.}
\]

This completes the stronger same-threshold theorem.

## 8. Multiplicity status

This retuning does **not** lower seventeen. The algebra still encounters `r=4`, for which the current interpolation contradiction needs `m>=4r+1=17`; analytically, the direct crossing determinant receiver still gives only the nonintegrable `|t|^{-1}` endpoint at order four. I read the current `s_16` improvements (carrier-orthogonal same-bank modes, mixed four-plus-one exterior energy, and the exact leverage/self-coordinate traps). They substantially narrow the endpoint but do not yet give a product-preserving fifth direction in every case. Therefore no `s_16` theorem is asserted here.
