# MOC4 account03/B20 r11 — exact scalar slack reformulation of the mixed assignment inequality

**Programme:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** Marcus–de Oliveira for complex normal `4 x 4` pairs (`MOC4`)  
**Outcome:** `ESSENTIAL_REDUCTION_PLUS_CONDITIONAL_THEOREM`; full MOC4 remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Inputs actually consumed

This run uses the source-exact MOC4 target in the collective `TARGETS.md` and three completed campaign artifacts:

1. `account03/B09`, `20260921T235010Z-b09-moc4-r01`: the middle exterior-power layer is compressed into a `3 x 3` doubly stochastic complement-pair matrix `R=(r_{alpha beta})` and a signed matrix `D=(d_{alpha beta})`, with `|d| <= r`; its earlier relaxation left a parity defect.
2. `account01/B07`, `20260922T000420Z-b07-moc4-r1`: the decisive exact identity `D = (H P H^T)_{mean-zero block}`, where `P=(|u_ij|^2)`, absorbs the signed middle-layer term into the one-point transport and reduces the full support problem to one mixed `(P,R)` assignment inequality.
3. `account01/B09`, `20260921T234628Z-b09-bench-v11`: an exact rational orthogonal example refutes every proof that insists final convex weights preserve the one-point marginals `P`, even though the determinant itself remains inside the 24-point Marcus–de Oliveira hull.

The result below does **not** reintroduce a forbidden marginal lift. It converts the remaining mixed inequality into one scalar nonnegative-slack inequality and proves a spectral combinatorial regime of that inequality for every unitary.

## 2. Starting point: the exact mixed assignment inequality

Fix spectra `a=(a_1,...,a_4)`, `b=(b_1,...,b_4)` and a support direction `eta`. After diagonalization, let

`P_ij = |u_ij|^2`.

Use the three complementary pair classes represented by `12,13,14`. Let `R=(r_{alpha beta})` and `D=(d_{alpha beta})` be the exact complement-pair variables from the previous reports. The account01/B07 reduction gives real coefficient arrays `C in R^{4 x 4}` and `X in R^{3 x 3}` such that, after removing an endpoint constant independent of `U`,

\[
F(U)=\langle P,C\rangle+\frac12\langle R,X\rangle. \tag{1}
\]

Let

\[
H=\frac12\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
\]

The exact identity of account01/B07 is

\[
HPH^T=\begin{pmatrix}1&0\\0&D\end{pmatrix}. \tag{2}
\]

Put `G` equal to the lower `3 x 3` block of `H C H^T`, and let `kappa=(H C H^T)_{00}`. Orthogonal invariance of the Frobenius pairing gives

\[
\langle P,C\rangle=\kappa+\langle D,G\rangle. \tag{3}
\]

Thus the only `U`-dependent quantity to control is

\[
\boxed{F_0(U)=\langle D,G\rangle+\frac12\langle R,X\rangle.} \tag{4}
\]

For a permutation matrix `P_sigma`, its mean-zero Hadamard block `D_sigma` is a signed `3 x 3` permutation matrix. Its underlying unsigned permutation is the induced permutation `rho_sigma in S_3` of the three complementary pair classes, and

\[
R_\sigma=|D_\sigma|. \tag{5}
\]

For every fixed `rho in S_3`, the four lifts in `S_4` have exactly the four even sign triples

\[
(+,+,+),(+,-,-),(-,+,-),(-,-,+). \tag{6}
\]

This is the only parity fact needed below.

## 3. New exact scalar-slack identity

Define

\[
K_{\alpha\beta}=|G_{\alpha\beta}|+\frac12 X_{\alpha\beta}. \tag{7}
\]

For `G_{alpha beta}=0`, set `sgn(G_{alpha beta})=0`. Define the **orientation/minor slack**

\[
S(U)=\sum_{\alpha,\beta}|G_{\alpha\beta}|
\bigl(r_{\alpha\beta}-\operatorname{sgn}(G_{\alpha\beta})d_{\alpha\beta}\bigr). \tag{8}
\]

Because `|d_{alpha beta}| <= r_{alpha beta}`, every summand is nonnegative. More concretely, if

\[
r=q_{S,T}+q_{S,T^c},\qquad d=q_{S,T}-q_{S,T^c},
\]

then

\[
r-d=2q_{S,T^c},\qquad r+d=2q_{S,T}. \tag{9}
\]

Hence `S(U)` is exactly twice a weighted mass of the complementary `2 x 2` minors in the orientation disfavored by the sign of `G`; it is not an abstract relaxation error.

Entrywise,

\[
Gd+\frac12Xr
=\left(|G|+\frac12X\right)r-|G|(r-\operatorname{sgn}(G)d).
\]

Therefore

\[
\boxed{F_0(U)=\langle R,K\rangle-S(U).} \tag{10}
\]

Since `R` is doubly stochastic, put

\[
K_\rho=\sum_{\alpha=1}^3K_{\alpha,\rho(\alpha)},\qquad
K_* =\max_{\rho\in S_3}K_\rho,
\]

and define the **assignment slack**

\[
A(U)=K_*-\langle R,K\rangle\ge0. \tag{11}
\]

Then

\[
\boxed{F_0(U)=K_*-A(U)-S(U).} \tag{12}
\]

Now compute the best actual `S_4` lift above a fixed `rho`. Set

\[
\delta_\rho=
\begin{cases}
0,&\prod_\alpha G_{\alpha,\rho(\alpha)}\ge0,\\
2\min_\alpha |G_{\alpha,\rho(\alpha)}|,&\prod_\alpha G_{\alpha,\rho(\alpha)}<0.
\end{cases} \tag{13}
\]

The even-sign rule (6) gives exactly

\[
\max_{\sigma:\rho_\sigma=\rho}
\left(\langle D_\sigma,G\rangle+\frac12\langle R_\sigma,X\rangle\right)
=K_\rho-\delta_\rho. \tag{14}
\]

Thus the complete permutation support value is

\[
V_* =\max_{\rho\in S_3}(K_\rho-\delta_\rho). \tag{15}
\]

Define the **effective parity deficit**

\[
\Delta=K_*-V_*\ge0. \tag{16}
\]

Combining (12) and (15) yields the main exact reduction:

\[
\boxed{
F_0(U)\le V_*
\quad\Longleftrightarrow\quad
A(U)+S(U)\ge\Delta.
} \tag{17}
\]

So the remaining support inequality is no longer a mixed `4 x 4`/`3 x 3` assignment statement. It is exactly the assertion that two manifestly nonnegative unitary slacks — Birkhoff assignment slack `A` and wrong-orientation minor mass `S` — pay the finite spectral parity deficit `Delta`.

Immediate consequence: if some maximizer of `K_rho` has nonnegative selected `G`-product, then `Delta=0`, and the support inequality follows automatically for **every** unitary.

## 4. New universal conditional theorem for a unique bad optimizer

Assume `K_rho` has a unique maximizing permutation `rho_0` and

\[
\prod_\alpha G_{\alpha,\rho_0(\alpha)}<0.
\]

Write

\[
m=\min_\alpha |G_{\alpha,\rho_0(\alpha)}|>0. \tag{18}
\]

For `tau != rho_0`, let

\[
q(\tau)=3-\#\{\alpha:\tau(\alpha)=\rho_0(\alpha)\}\in\{2,3\},
\]

and define the normalized competing-assignment gap

\[
\kappa=\min_{\tau\ne\rho_0}
\frac{K_*-K_\tau}{q(\tau)}. \tag{19}
\]

### Theorem

If

\[
\boxed{\kappa\ge m,} \tag{20}
\]

then the MOC4 support inequality in this direction holds for every unitary `U`.

### Proof

Take any Birkhoff decomposition

\[
R=\sum_{\tau\in S_3}\mu_\tau P_\tau.
\]

Let

\[
E_R=\sum_\alpha(1-r_{\alpha,\rho_0(\alpha)}).
\]

Then

\[
E_R=\sum_\tau\mu_\tau q(\tau),
\]

and, by (19),

\[
A(U)=\sum_\tau\mu_\tau(K_*-K_\tau)\ge\kappa E_R. \tag{21}
\]

Let

\[
s_\alpha=\operatorname{sgn}(G_{\alpha,\rho_0(\alpha)}).
\]

The sign triple `s` has odd parity. Since `D` is the mean-zero Hadamard block of a doubly stochastic `P`, it lies in the convex hull of the 24 signed permutation blocks `D_sigma`. Along any fixed `rho_0`, every vertex contributes either zero/one matched entries or, when all three entries match, an even sign triple. Therefore the odd-sign functional satisfies

\[
\sum_\alpha s_\alpha d_{\alpha,\rho_0(\alpha)}\le1. \tag{22}
\]

Keeping only the three `rho_0` cells in (8) and using `|G|>=m` there,

\[
\begin{aligned}
S(U)
&\ge m\sum_\alpha
\bigl(r_{\alpha,\rho_0(\alpha)}-s_\alpha d_{\alpha,\rho_0(\alpha)}\bigr)\\
&\ge m\bigl((3-E_R)-1\bigr)
=m(2-E_R). \tag{23}
\end{aligned}
\]

If `E_R<=2`, then from (21), (23), and `kappa>=m`,

\[
A+S\ge \kappa E_R+m(2-E_R)
=2m+(\kappa-m)E_R\ge2m.
\]

If `E_R>=2`, then `A>=\kappa E_R>=2m` and `S>=0`. Thus always

\[
A(U)+S(U)\ge2m. \tag{24}
\]

For the unique bad maximizer, its parity loss is `2m`, while the effective deficit `Delta` can only be smaller because another nonmaximal `rho` may have a better parity-adjusted value. Hence `Delta<=2m`, and (17) proves the support inequality. QED.

### Meaning

A genuinely hard support direction is now forced into a narrow combinatorial regime. If `K` has a unique maximizer, a possible failure requires an odd-parity maximizer **and** a competing assignment closer than `m` per changed pair-class edge (`kappa<m`). Multiple maximizing assignments are the other unresolved regime. This is a stronger localization than merely saying that the one-point and pair assignments may disagree.

## 5. Exact nontrivial check on the shared marginal-lift obstruction

Use the exact rational orthogonal matrix and complex spectra from `account01/B09`:

\[
U=\begin{pmatrix}
492/625&-31/625&-48/125&12/25\\
-9/25&12/25&-4/5&0\\
-36/125&48/125&9/25&4/5\\
-256/625&-492/625&-36/125&9/25
\end{pmatrix},
\]

\[
a=(-2-3i,-2,3+i,-1-2i),\qquad
b=(3,2-i,3-2i,2+3i).
\]

Take the support direction `eta=-4-5i`. Exact rational arithmetic gives

\[
G=\frac12\begin{pmatrix}
755&755&-673\\
-1005&-801&975\\
-345&-345&1083
\end{pmatrix},
\]

\[
X=\begin{pmatrix}
-284&-294&-148\\
-624&-430&-376\\
1110&1100&590
\end{pmatrix}.
\]

The six `K_rho` values are

\[
2515/2,\ 2515/2,\ 2515/2,\ 2515/2,\ 2351/2,\ 2351/2,
\]

while the corresponding parity losses are

\[
755,\ 345,\ 755,\ 345,\ 345,\ 345.
\]

Therefore

\[
K_*=2515/2,\qquad
V_*=1825/2,\qquad
\Delta=345. \tag{25}
\]

For the actual unitary,

\[
A(U)=\frac{2563648}{390625},
\qquad
S(U)=\frac{225456591}{390625},
\]

so

\[
A(U)+S(U)=\frac{228020239}{390625}
=583.73181184\ldots, \tag{26}
\]

and

\[
A(U)+S(U)-\Delta
=\frac{93254614}{390625}
=238.73181184\ldots>0. \tag{27}
\]

Thus the new exact criterion certifies this genuinely positive-deficit support direction on the same unitary/spectra that destroy the natural `P`-marginal convex-lift strategy. The certification uses no final convex weights preserving `P`.

For the specific dual direction used in the account01/B09 marginal-lift obstruction, `eta=8-5i`, the same reduction has `Delta=0`; the support inequality is therefore automatic from (17) even though the stronger marginal-preserving representation fails. This cleanly separates the true hull problem from the refuted lift mechanism.

## 6. What remains

Full MOC4 is still open. The exact remaining universal statement is now:

> For every structured coefficient pair `(G,X)` arising from spectra and a support direction, and every unitary-generated `(R,D)`, prove `A(U)+S(U) >= Delta`.

The next attack should focus only on the residual regimes not covered above:

1. several `K`-maximizing assignments with parity loss; or
2. a unique odd maximizer with `kappa<m`.

The most promising common-unitary input is the row/column Plucker triangle system already derived by account01/B07. If `A` is small, `R` is concentrated on the bad assignment face; the parity inequality (22) then forces signed disagreement in `D`, and the Plucker constraints should force that disagreement to appear as actual wrong-orientation minor mass in `S`. This is now a scalar quantitative target rather than a search for a forbidden common permutation law.

No claim of a full proof, counterexample to MOC4, or worldwide novelty is made.
