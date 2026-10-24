# B17 FEI creative run — a sharp shared-MUX sensitivity-boundary charge

**Run:** `B17-20260921T140528Z-r31`  
**Status:** PARTIAL. Full Friedgut--Kalai Fourier entropy--influence conjecture remains **OPEN / NOT PROVED**.  
**Research label:** `WITHOUT_VERIFIED_BRAIN`.  
**Route:** APPROACH 3/7/14 — sensitivity coupling + shared-variable composition + coding entropy.  
**Fresh scientific base:** `yspennstate/math-open-problems` master `0c4dd6b8aa64f08f8f150a428519982b642b8100`.  
**Continuation point:** account01/B17 `B17-20260921T124026Z-r30`, the disjoint-branch MUX theorem.  
**No audit:** no read-once certificate or settled exhaustive sweep was rerun.

## 1. The question left by the previous B17 run

Let `x` be a fresh selector and let `g,h` be Boolean functions, now allowed to share variables. Put

\[
F(x,y)=\frac{g(y)+h(y)}2+x\,\frac{g(y)-h(y)}2.
\]

The preceding B17 run proved a dimension-free linear selector charge when the two branches have disjoint residual
variables. The next question was whether the same kind of charge survives shared variables.

Write

\[
p_T=\widehat g(T)^2,\qquad q_T=\widehat h(T)^2,\qquad
j=\Pr[g\ne h]=\frac{1-\langle g,h\rangle}{2}.
\]

The exact influence identity still holds with arbitrary overlap:

\[
I(F)=\frac{I(g)+I(h)}2+j. \tag{1}
\]

Define the exact extra entropy charge

\[
M(g,h):=H(F)-\frac{H(g)+H(h)}2. \tag{2}
\]

The main result of this run is a sharp universal upper bound on `M` in terms of the *boundary of the branch
disagreement set*. This gives a precise coupling between spectral entropy and the sensitivity structure.

## 2. Exact information decomposition

For each Fourier coordinate `T`, the two MUX coefficients are

\[
\widehat F(T)=\frac{\widehat g(T)+\widehat h(T)}2,\qquad
\widehat F(T\cup\{x\})=\frac{\widehat g(T)-\widehat h(T)}2. \tag{3}
\]

Let

\[
m_T=\frac{p_T+q_T}{2}.
\]

If `X` records whether the spectral sample of `F` contains the selector `x`, then its `T`-marginal is exactly
`m=(p+q)/2` and `Pr[X=1]=j`. Therefore the chain rule gives the exact identity

\[
\boxed{
M(g,h)=\operatorname{JS}(p,q)+H(X\mid T),
} \tag{4}
\]

where `JS` is the Jensen--Shannon divergence in bits. Hence

\[
H(X\mid T)\le h_2(j). \tag{5}
\]

This separates the shared-variable obstruction into a distinguishability term between the two squared Fourier
spectra and the description length of the selector membership bit.

## 3. A Fourier-Hellinger lemma

### Lemma 3.1

For probability vectors `p,q`,

\[
\operatorname{JS}(p,q)
\le \frac{1-\sum_T\sqrt{p_Tq_T}}{\ln 2}. \tag{6}
\]

For `p_T=\widehat g(T)^2`, `q_T=\widehat h(T)^2` this implies

\[
\boxed{
\operatorname{JS}(p,q)
\le \frac{2\min(j,1-j)}{\ln 2}.
} \tag{7}
\]

### Proof

For one coordinate write `m=(p+q)/2` and `theta=p/(p+q)`. Its JS contribution is
`m[1-h_2(theta)]`. The elementary scalar inequality

\[
1-h_2(\theta)
\le \frac{1-2\sqrt{\theta(1-\theta)}}{\ln 2} \tag{8}
\]

follows by putting `theta=(1+z)/2`: after multiplication by `ln 2` the difference between the right and left sides
has derivative

\[
\frac{z}{\sqrt{1-z^2}}-\operatorname{atanh}z\ge0,
\]

because the derivative of this last expression is
`(1-\sqrt{1-z^2})/(1-z^2)^{3/2}>=0`, and equality holds at `z=0`. Summing (8) proves (6).

Now

\[
\sum_T\sqrt{p_Tq_T}
=\sum_T|\widehat g(T)\widehat h(T)|
\ge\left|\sum_T\widehat g(T)\widehat h(T)\right|
=|\langle g,h\rangle|
=|1-2j|.
\]

Thus `1-BC <= 1-|1-2j|=2 min(j,1-j)`, proving (7). QED.

Combining (4), (5), and (7) already gives the universal nonlinear shared-MUX charge

\[
\boxed{
M(g,h)\le h_2(j)+\frac{2}{\ln 2}\min(j,1-j).
} \tag{9}
\]

This is the coding form of the result.

## 4. PROVED: sharp sensitivity-boundary payment

Let

\[
D(y)=g(y)h(y)\in\{-1,1\}.
\]

Thus `D=-1` exactly on the branch-disagreement set. Put `q=min(j,1-j)`. Edge isoperimetry on the cube gives

\[
I(D)\ge 2q\log_2\frac1q. \tag{10}
\]

Also

\[
h_2(q)
=q\log_2\frac1q+(1-q)\log_2\frac1{1-q}
\le q\log_2\frac1q+\frac{q}{\ln2}. \tag{11}
\]

Substituting (10)--(11) into (9) proves:

### Theorem 4.1 — shared-MUX sensitivity-boundary theorem

For arbitrary Boolean branches `g,h` on any common ambient cube,

\[
\boxed{
M(g,h)
\le
\frac12 I(gh)
+\frac{3}{\ln 2}\min\{\Pr[g\ne h],\Pr[g=h]\}.
} \tag{12}
\]

Equivalently, for an arbitrary Boolean function `f` and coordinate `i`, let

\[
g=f_{i=+1},\qquad h=f_{i=-1},\qquad
d_i=gh.
\]

Then `Inf_i(f)=Pr[g ne h]` and

\[
\boxed{
H(f)-\frac{H(g)+H(h)}2
\le
\frac12 I(d_i)
+\frac{3}{\ln2}\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
} \tag{13}
\]

Here `d_i` is exactly the sign of the `i`-edge sensitivity indicator: `d_i=-1` on sensitive `i`-fibres.
Consequently `I(d_i)` measures the boundary, across the other coordinates, of the set of sensitive `i`-fibres.
This is a direct spectral-entropy/sensitivity-structure coupling.

The coefficient is

\[
\frac3{\ln2}=4.328085122666891\ldots. \tag{14}
\]

## 5. The coefficient `3/ln 2` is sharp in (12)

The sharpness mechanism is an exact Boolean family, not an abstract point process.

Let `r` be even, `N=2^r`, and on `F_2^r` take the quadratic bent sign

\[
g_r(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{r-1}x_r}.
\]

Its normalized Walsh coefficients all have magnitude

\[
t=N^{-1/2}.
\]

Let `h_r` equal `g_r` everywhere except at `0`, where its sign is flipped. Then

\[
j=\Pr[g_r\ne h_r]=N^{-1}=t^2, \tag{15}
\]

and `D_r=g_rh_r` is the one-point defect. Therefore

\[
I(D_r)=2rj. \tag{16}
\]

Write the bent coefficients as `sigma_T t`, `sigma_T in {+-1}`. Since `g_r(0)=1`,

\[
\sum_T\sigma_T=\sqrt N,
\]

so the counts of the two signs are

\[
n_+=\frac{N+\sqrt N}{2},\qquad
n_-=\frac{N-\sqrt N}{2}. \tag{17}
\]

Flipping the value at zero changes every Fourier coefficient by `-2/N`. With

\[
\phi(s)=s\log_2(1/s)
\]

and

\[
\begin{aligned}
\nu_\sigma(t)
&=
\phi\!\left(t^2(1-\sigma t)^2\right)+\phi(t^4)
-\frac12\phi(t^2)
-\frac12\phi\!\left(t^2(1-2\sigma t)^2\right),
\end{aligned} \tag{18}
\]

the exact charge ratio is

\[
\boxed{
R_r:=\frac{M(g_r,h_r)}j
=
\frac{(1+t)\nu_+(t)+(1-t)\nu_-(t)}{2t^4}.
} \tag{19}
\]

Expanding the four elementary `log(1+-t)` terms at `t=0` gives

\[
R_r
=
r+\frac3{\ln2}
-\frac{19}{6\ln2}\,2^{-r}
+O(2^{-2r}). \tag{20}
\]

In particular

\[
R_r-r\longrightarrow\frac3{\ln2}. \tag{21}
\]

Since `(1/2) I(D_r)/j=r`, no inequality of the form

\[
M(g,h)\le\frac12 I(gh)+C\min(j,1-j)
\]

can hold with `C<3/ln 2`. Thus the coefficient in Theorem 4.1 is best possible.

This family also decisively kills the stronger hoped-for overlap extension

\[
M(g,h)\le C\,\Pr[g\ne h]
\]

with a dimension-independent `C`: its left/right ratio grows as `r+3/ln 2+o(1)`. This is **not** a counterexample
to FEI. It is a counterexample only to the proposed local shared-MUX linear charge.

## 6. Controlled-overlap positive result

The previous disjoint-branch theorem can still be extended to a fixed shared core.

Suppose

\[
g=g(z,a),\qquad h=h(z,b),
\]

where the shared block `z` has `r` bits and the residual blocks `a,b` are disjoint. For the common Fourier
coordinates `T subseteq [r]`, write `a_T=hat g(T)`, `b_T=hat h(T)`. Outside the shared block the branch Fourier
supports are disjoint.

The scalar charge

\[
n(a,b)
=
\phi\!\left(\frac{(a+b)^2}{4}\right)
+\phi\!\left(\frac{(a-b)^2}{4}\right)
-\frac12\phi(a^2)-\frac12\phi(b^2) \tag{22}
\]

obeys

\[
n(a,b)\le
L\,\bigl||a|-|b|\bigr|,
\qquad
L=\frac{\gamma+2/e}{2\ln2},\quad
\gamma=\frac{109+73\sqrt{73}}{864}. \tag{23}
\]

Indeed for a fixed ratio of the two squared magnitudes the quotient by `||a|-|b||` increases with their common
scale, so one magnitude can be pushed to `1`; the resulting one-variable bound is exactly the logarithmic estimate
proved in the preceding B17 MUX report.

Let `u(z)=E_a g(z,a)` and `v(z)=E_b h(z,b)`. The exclusive Fourier mass is at most `4j`. Moreover

\[
\sum_{T\subseteq[r]} n(a_T,b_T)
\le L\sum_T|\widehat{u-v}(T)|
\le L\,2^r E|u-v|
\le L\,2^{r+1}j, \tag{24}
\]

using `|u-v|<=1-uv` for `u,v in [-1,1]`. Hence

\[
\boxed{
M(g,h)\le K_r j,\qquad
K_r=4+2^r\,\frac{\gamma+2/e}{\ln2}.
} \tag{25}
\]

For `r=0` this recovers the previous analytic charge `6.28494833349...`; for `r=1` it gives
`8.56989666698...`. This is a genuine fixed-overlap composition theorem, although the bound is intentionally not
claimed sharp. The bent one-point family shows that *some* growth with overlap width is unavoidable for a purely
local `C_r j` charge.

## 7. Numerical stress test of the new sharpness family

The accompanying checker independently builds the bent truth tables and performs normalized FWHTs through `r=12`,
then compares those direct coefficients with (19). It also evaluates the closed form through `r=20`.

Selected values:

| `r` | `M/j` | `r+3/ln 2` |
|---:|---:|---:|
| 2 | 4.8676687468 | 6.3280851227 |
| 4 | 8.0300138475 | 8.3280851227 |
| 6 | 10.2559702353 | 10.3280851227 |
| 8 | 12.3101942894 | 12.3280851227 |
| 12 | 16.3269695829 | 16.3280851227 |
| 16 | 20.3280154116 | 20.3280851227 |
| 20 | 24.3280807634 | 24.3280851227 |

For `r<=12` the direct FWHT and closed formula agree to the displayed floating precision, and the bent flatness
error is zero in binary floating arithmetic for these powers of two. The scaled gap
`2^r[(r+3/ln2)-R_r]` approaches `19/(6 ln2)=4.5685342961...`, matching (20).

These are stress tests; the universal statements (12), (13), and the asymptotic derivation are analytic.

## 8. What this changes in the FEI route

The raw sensitivity-set entropy route was already killed, and the scalar Palm-size relaxation was already killed.
This run identifies a more local object that survives those failures:

\[
d_i(y)=f_{i=+1}(y)f_{i=-1}(y).
\]

The restriction entropy cost is controlled by the *boundary influence of the sensitivity indicator* `d_i`, not by
the entropy of the entire sensitivity set and not by the scalar Palm size alone. The rare bent flip shows that this
boundary term is genuinely necessary and exactly explains the logarithmic rare-event cost.

The next target is therefore not another local `Delta_i H <= C Inf_i` inequality. It is an **amortized coding
theorem for the sensitivity-boundary terms**: find a restriction/coding scheme in which the successive
`I(d_i)/2` charges are paid once, rather than once per coordinate. In two-face language,
`Inf_j(d_i)` is the probability that an `(i,j)` face has odd sign product, so the candidate budget is a signed
higher-face boundary process rather than the previously refuted raw sensitivity-set entropy.

No publication-priority or literature-novelty claim is made here. Full FEI remains OPEN.
