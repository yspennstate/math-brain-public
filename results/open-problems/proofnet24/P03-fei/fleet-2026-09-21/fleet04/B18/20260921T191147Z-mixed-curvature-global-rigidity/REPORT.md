# B18 FEI proof integration — mixed-derivative curvature conservation and global zero-defect rigidity

**Run:** `20260921T191147Z-b18-fei-r13`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** universal Boolean source theorems plus a solved exact endpoint of the current depth-stability programme. No novelty or publication-priority claim.

## 0. Fresh state and the implication attacked

This run starts from the current September-21 FEI programme after the numerical target correction: the external balanced monotone seed already gives a lower bound above `6.52`, the earlier proposed cancellation constant below `2.324` is refuted, and unrestricted FEI remains open.

The compatible inputs used are:

1. fleet04/B18 `20260921T184125Z-transverse-near-subcube-elimination`: a low-depth derivative row whose support is within relative error `1/16` of a coordinate subcube has its restriction-entropy decrement paid by the transverse folded influences of the subcube coordinates; its global aggregation was left conditional on a bounded-incidence/nonreuse selector;
2. fleet03/B18 `20260921T185340Z-signed-flag-curvature`: for an oriented Boolean derivative row the signed translation curvature decomposes exactly as support disagreement plus four times opposite-sign overlap, and the unsigned support bank alone can miss a parity/orientation mode;
3. fleet02/B13 `20260921T180326Z-sign-stability-defect`: the derivative depth defect has the exact four-bank decomposition and equality forces sign purity together with the inherited B12 support rigidity;
4. fleet02/B12's depth-rigidity endpoint: equality in the sharp derivative-Palm depth bound forces a constant-sign coordinate-subcube derivative;
5. fleet02 interactive `20260921T174421Z-centered-critical-budget`: median-character folding and the primitive centered critical-core reduction.

The fresh fleet02/B18 affine-mask/compiler work is a different branch: it removes product-noise assumptions from the compiler-mask payment. This report does not duplicate that branch.

The missing source implication attacked here is:

> Can the overlap of the transverse coordinate sets from different low-depth derivative rows be controlled by an intrinsic Boolean bank, without assuming a bounded-incidence selector?

Yes. Commutation of mixed Boolean derivatives gives an exact **column conservation law**. It turns transverse-set congestion into the target derivative row's spectral depth. At the exact zero-depth endpoint this conservation is much more rigid: if every folded derivative row is an extremizer, the entire Boolean function is a one-point defect (up to character/sign and irrelevant variables), and hence satisfies FEI with constant strictly below `4`.

---

## 1. Setup

Let
\[
f:\mathbb F_2^n\to\{-1,+1\}.
\]
After multiplying by a median character, assume every relevant coordinate has folded influence
\[
0<j_i=\operatorname{Inf}_i(f)\le\frac12.
\]
This gauge preserves spectral entropy and changes ordinary influence to the centered quantity `J`; hence an `H <= C J` estimate is sufficient for FEI with the same constant.

For each coordinate `i`, on the quotient cube with `x_i=0`, write
\[
g_i(y)=D_i f(y)=\frac{f(0,y)-f(1,y)}2\in\{0,\pm1\},
\qquad
E_i=\{y:g_i(y)\ne0\}.
\]
For a residual coordinate `k != i`, put
\[
p_{ik}
=
\Pr_y[1_{E_i}(y)\ne1_{E_i}(y+e_k)],
\]
\[
o_{ik}
=
\Pr_y[g_i(y)=-g_i(y+e_k)\ne0],
\]
and
\[
\kappa_{ik}
=
\mathbb E_y\bigl(g_i(y)-g_i(y+e_k)\bigr)^2.
\]
With
\[
D_k u(x)=\frac{u(x)-u(x+e_k)}2,
\]
define the derivative-row depth energy
\[
d_i=\sum_{k\ne i}\|D_k g_i\|_2^2.
\]
The normalized depth defect is
\[
\delta_i
=
\frac{d_i}{j_i}
-\frac12\log_2\frac1{j_i}
\ge0.
\]

For the entropy side write
\[
\mathcal R_i
=
H(f)-\frac{H(f^{i=0})+H(f^{i=1})}{2}.
\]
The inherited concave restriction theorem gives
\[
\mathcal R_i\le\Psi(j_i),
\qquad
\Psi(t)
=
h_2(t)+1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right),
\]
and
\[
\Psi(t)\le t\left(\log_2\frac1t+\frac3{\ln2}\right).
\tag{1.1}
\]

---

## 2. PROVED: exact mixed-derivative curvature conservation

### Theorem B18-MIXED-CURVATURE-CONSERVATION-01

For every distinct pair `i,k`,
\[
\boxed{\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik}.}
\tag{2.1}
\]
Consequently, for every fixed target coordinate `k`,
\[
\boxed{
\sum_{i\ne k}\bigl(p_{ik}+4o_{ik}\bigr)=4d_k,
}
\tag{2.2}
\]
and therefore
\[
\boxed{
\sum_{i\ne k}p_{ik}\le4d_k,
\qquad
\sum_{i\ne k}o_{ik}\le d_k.
}
\tag{2.3}
\]

### Proof

Fix all coordinates except `i,k` and abbreviate the four Boolean values by
\[
a=f(0,0),\quad
b=f(1,0),\quad
c=f(0,1),\quad
d=f(1,1).
\]
The change of the `i`-derivative row in direction `k` is
\[
g_i(x_k=0)-g_i(x_k=1)
=
\frac{a-b-c+d}{2}.
\]
The change of the `k`-derivative row in direction `i` is the same scalar:
\[
g_k(x_i=0)-g_k(x_i=1)
=
\frac{a-c-b+d}{2}.
\]
Hence mixed derivatives commute pointwise and
\[
\kappa_{ik}=\kappa_{ki}.
\]

For two values `u,v in {0,±1}`, the elementary identity
\[
(u-v)^2
=
1_{\{u^2\ne v^2\}}
+
4\,1_{\{u=-v\ne0\}}
\]
gives
\[
\kappa_{ik}=p_{ik}+4o_{ik}.
\]
Finally,
\[
\kappa_{ki}
=
4\|D_i g_k\|_2^2.
\]
Summing over `i != k` gives (2.2), and dropping nonnegative terms gives (2.3). QED.

### Interpretation

The previous bounded-incidence quantity counted how many low-depth transverse sets `F_i` hit a fixed coordinate `k`. Equation (2.2) says that the **actual Boolean support-boundary load into `k` cannot accumulate arbitrarily**: including its missing orientation correction, it is exactly the derivative depth energy of row `k`.

This is an integrability constraint. An arbitrary family of near-subcubes does not satisfy it; genuine Boolean derivative rows do because they come from one common potential `f`.

---

## 3. PROVED: the bounded-incidence hypothesis can be replaced by a depth bank

Suppose a derivative row `i` is in the robust near-subcube regime of the preceding B18 report. Thus there is a coordinate subcube
\[
Q_i=\{x_{F_i}=a_i\},
\qquad
s_i=\mu(Q_i)=2^{-|F_i|},
\]
such that
\[
\varepsilon_i=\mu(E_i\triangle Q_i)\le\rho j_i,
\qquad
\rho\le\frac1{16}.
\]
For each `k in F_i`, the coordinate boundary of a subcube and Lipschitzness under symmetric difference give
\[
p_{ik}
=
I_k(E_i)
\ge2(s_i-\varepsilon_i).
\tag{3.1}
\]
Also
\[
|s_i-j_i|\le\varepsilon_i.
\tag{3.2}
\]

Let
\[
L_i=\log_2(1/j_i),
\qquad
r_i=|F_i|=\log_2(1/s_i).
\]
From (3.1)-(3.2),
\[
\sum_{k\in F_i}p_{ik}
\ge
2j_i(1-2\rho)
\left(
L_i-\log_2(1+\rho)
\right).
\tag{3.3}
\]
Combining this with (1.1) yields:

### Theorem B18-ROBUST-ROW-TO-CURVATURE-02

For every such robust row,
\[
\boxed{
\mathcal R_i
\le
C_\rho\sum_{k\in F_i}p_{ik},
}
\tag{3.4}
\]
where one may take
\[
C_\rho
=
\frac{
1+3/\ln2
}{
2(1-2\rho)
\left(1-\log_2(1+\rho)\right)
}.
\tag{3.5}
\]
At the inherited threshold `rho=1/16`,
\[
C_{1/16}<3.337.
\tag{3.6}
\]

Indeed the ratio
\[
\frac{L+3/\ln2}{
2(1-2\rho)(L-\log_2(1+\rho))
}
\]
is decreasing for `L>=1`, so its maximum is at `L=1`.

Now let `G` be **any** set of robust pivots at one Boolean state. No bounded-incidence assumption is imposed. Summing (3.4), using only `F_i subseteq [n]\{i}`, and then applying (2.3),
\[
\begin{aligned}
\sum_{i\in G}\mathcal R_i
&\le
C_\rho
\sum_{i\in G}\sum_{k\in F_i}p_{ik}\\
&\le
C_\rho
\sum_k\sum_{i\ne k}p_{ik}\\
&\le
4C_\rho\sum_k d_k.
\end{aligned}
\]
Thus:

### Corollary B18-NO-INCIDENCE-DEPTH-PAYMENT-03

At relative near-subcube error at most `1/16`,
\[
\boxed{
\sum_{i\in G}\mathcal R_i
<
13.348\sum_k d_k.
}
\tag{3.7}
\]

This is a genuine replacement for the **assumed** bounded-incidence selector in the preceding local aggregation theorem. The price is that the receiving bank is derivative depth rather than centered influence.

Using the definition of `delta_k`,
\[
d_k
=
j_k\left(
\frac12\log_2\frac1{j_k}+\delta_k
\right),
\tag{3.8}
\]
so (3.7) identifies the remaining payment exactly as an influence-profile term plus the already isolated B13 depth-defect bank. It does **not** claim that this bank is universally `O(J)`.

### Exact-support improvement

If `E_i=Q_i` exactly, then `j_i=s_i=2^{-r_i}`,
\[
p_{ik}=2j_i\qquad(k\in F_i),
\]
and the previous exact-subcube scalar estimate
\[
\mathcal R_i\le4r_i j_i
\]
gives
\[
\boxed{
\mathcal R_i
\le2\sum_{k\in F_i}p_{ik}.
}
\tag{3.9}
\]
Hence an arbitrary family of exact-subcube rows satisfies
\[
\boxed{
\sum_{i\in G}\mathcal R_i
\le8\sum_k d_k.
}
\tag{3.10}
\]

The next section shows that if **every** row is at the exact depth endpoint, even the bank on the right is unnecessary: Boolean integrability classifies the whole function.

---

## 4. PROVED: all-row zero depth defect forces a one-point phase

### Theorem B18-GLOBAL-ZERO-DEFECT-RIGIDITY-04

Assume the median-character gauge above and delete irrelevant variables. If
\[
\boxed{\delta_i=0\quad\text{for every remaining coordinate }i,}
\tag{4.1}
\]
then there is a point `b in F_2^m` and a sign `sigma in {±1}` such that
\[
\boxed{
f(x)=\sigma\bigl(1-2\,1_{\{x=b\}}\bigr).
}
\tag{4.2}
\]
Equivalently, before the median-character fold, every all-row depth extremizer is a character times a one-point defect, up to sign and irrelevant variables.

### Proof

By the inherited B12 equality rigidity (equivalently, B13's four nonnegative defect banks together with equality in cube edge isoperimetry), for every remaining coordinate `i`,
\[
g_i
=
\sigma_i\,1_{Q_i},
\tag{4.3}
\]
where `Q_i` is a coordinate subcube. Write
\[
Q_i=\{x_{F_i}=a_i\}.
\]
Because `0<j_i<=1/2`, every `F_i` is nonempty.

Construct a graph on the relevant coordinates by joining `i` to `k` exactly when `k in F_i`.

Mixed derivative commutation from Section 2 gives
\[
D_k g_i=D_i g_k.
\tag{4.4}
\]
If `k notin F_i`, the left side is zero. If `k in F_i`, it is a nonzero constant-sign half-indicator of the subcube obtained by removing the `k` constraint. Therefore (4.4) implies
\[
k\in F_i
\Longleftrightarrow
i\in F_k.
\tag{4.5}
\]
When these equivalent conditions hold, equality of the two nonzero subcube indicators implies
\[
F_i\setminus\{k\}
=
F_k\setminus\{i\},
\tag{4.6}
\]
and their fixed bit patterns agree on the common set.

Thus adjacent vertices have the same closed neighborhood:
\[
\{i\}\cup F_i
=
\{k\}\cup F_k.
\tag{4.7}
\]
Every connected component of the graph is therefore a clique, and for a component `C`,
\[
F_i=C\setminus\{i\}
\qquad(i\in C).
\tag{4.8}
\]
The pattern agreement in (4.6) gives a common point `b_C in F_2^C` such that
\[
Q_i
=
\{x_{C\setminus\{i\}}
=
(b_C)_{C\setminus\{i\}}\}.
\tag{4.9}
\]

There cannot be two nontrivial components. Indeed, for coordinates in different components every cross mixed derivative vanishes. In Walsh language this means no nonzero Fourier coefficient contains coordinates from both components, so
\[
f=c+\sum_C u_C(x_C)
\tag{4.10}
\]
with each `u_C` depending on only one component. A `{±1}`-valued function of the additive form (4.10) cannot have two nonconstant summands: choosing two values of each of two nonconstant summands would produce a `2 x 2` additive rectangle with both row and column differences nonzero, forcing one pair of `{±1}` values to differ by magnitude `4`. Hence exactly one relevant component remains.

Call it `C`, with `|C|=m>=2`. By (4.9), the only sensitive edge in direction `i` is the edge whose other coordinates equal `b_C`. Therefore all sensitive edges are precisely the `m` cube edges incident to `b_C`. The `m`-cube with `b_C` removed is connected. Hence `f` is constant on all points other than `b_C`, and it takes the opposite sign at `b_C`. This is (4.2). QED.

---

## 5. PROVED: the global zero-defect endpoint satisfies FEI with constant < 4

For the one-point phase on `m>=2` relevant variables, set
\[
t=2^{1-m},
\qquad
L=\log_2(1/t)=m-1.
\]
Its Fourier coefficients have magnitudes
\[
|\widehat f(\varnothing)|=1-t,
\qquad
|\widehat f(S)|=t\quad(S\ne\varnothing),
\]
and
\[
I(f)=mt.
\]
Therefore
\[
H(f)
=
\phi((1-t)^2)
+
(2^m-1)t^2\,2L
=
\phi((1-t)^2)
+
(4t-2t^2)L,
\tag{5.1}
\]
where `phi(w)=w log_2(1/w)`.

Since
\[
-\ln(1-t)\le\frac{t}{1-t},
\]
\[
\phi((1-t)^2)
=
-\frac{2(1-t)^2\ln(1-t)}{\ln2}
\le
\frac{2t(1-t)}{\ln2}
<
4t.
\tag{5.2}
\]
Using `(4t-2t^2)L<=4tL`,
\[
\boxed{
H(f)<4t(L+1)=4I(f).
}
\tag{5.3}
\]

Thus:

### Corollary B18-ZERO-DEFECT-FEI-05

Every Boolean function whose median-folded relevant derivative rows all attain the sharp B12 depth endpoint satisfies
\[
\boxed{H(f)<4J(f)\le4I(f).}
\tag{5.4}
\]

This closes the **entire exact equality branch**, not merely one derivative row.

---

## 6. Decisive computation

The accompanying standard-library checker uses exact `Fraction` arithmetic for all cube identities. It exhausts every Boolean truth table through dimension four and checks:

- `kappa_ik = kappa_ki`;
- `kappa_ik = p_ik + 4 o_ik`;
- the column conservation identity;
- after median-character folding, every function whose relevant derivative rows are all constant-sign coordinate-subcube rows is a one-point phase on its relevant variables.

Recorded coverage:

- `394,000` unordered mixed-coordinate/function cases;
- `262,944` column-conservation cases;
- `1,912` all-row endpoint functions after folding;
- `0` classification failures.

It also evaluates the exact one-point spectral formula for `2<=m<=32`; the largest sampled ratio is
`H/I = 3.965168439111353 < 4`.

Checker SHA-256:
`f9506f6b7fadc6307e411eda108bfa0f0a364d8fa184ce2df1b91ebd5a7c28d0`.

Sanitized stdout SHA-256:
`2387da143009125b9f6682a06fb38910de0b17477f71316a11fa5ca5ef018b56`.

The finite calculation is falsification/self-check evidence only. Sections 2--5 are analytic and all-dimensional.

---

## 7. Status ledger and next universal implication

### PROVED

1. Exact mixed signed-curvature symmetry:
   \[
   \kappa_{ik}=\kappa_{ki}.
   \]
2. Exact column conservation:
   \[
   \sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k.
   \]
3. Arbitrary overlap of robust near-subcube transverse sets is paid by the derivative-depth bank; no bounded-incidence hypothesis is needed for this same-state aggregation.
4. All-row zero depth defect globally classifies the function as a character times a one-point defect (up to sign/irrelevant variables).
5. That full equality class satisfies FEI with constant strictly below `4`.

### CONDITIONAL / NOT YET GLOBAL

- The depth-bank aggregate (3.7) is not yet a universal centered-influence payment. Its exact decomposition (3.8) still contains the influence-profile term `sum j_i log(1/j_i)`.
- A quantitative stability theorem converting **small total depth defect** into closeness to the one-point class is not proved here.
- No adaptive restriction tree is constructed here whose total entropy charge is bounded by a universal multiple of `J`.

### REFUTED / PRESERVED WARNINGS

- Same-coordinate payment remains false.
- Unsigned support transport alone misses opposite-sign curvature.
- An arbitrary family of near-subcubes need not have bounded overlap; the new conservation law relies on their being genuine mixed derivatives of one Boolean function.
- The current external lower bound above `6.52` means the global FEI constant cannot be inferred from the `<4` equality endpoint.

### OPEN

**Full unrestricted FEI remains OPEN / NOT PROVED.**

The next source-exact implication is now sharper:

> Prove a quantitative global stability/dichotomy: either the median-folded derivative system has enough total depth defect to pay the residual through the B13 sign/isoperimetric/mixed-axis banks, or the mixed-curvature conservation law forces the whole system close to the one-point phase, where the ratio is below `4`.

This target is strictly stronger than asking for a bounded-incidence selector: the exact endpoint has now been classified, and near-endpoint overlap has an intrinsic Boolean capacity.
