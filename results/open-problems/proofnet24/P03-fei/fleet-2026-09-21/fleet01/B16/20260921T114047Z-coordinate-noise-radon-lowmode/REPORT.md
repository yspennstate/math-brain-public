# B16 FEI signed transport/noise interpolation: exact coordinate-noise cut bridge and a low-mode obstruction

Date: 21 September 2026  
Fleet scope: fleet01 / B16  
Route: APPROACH 10/13, signed transport/noise interpolation and Boolean correlation constraints  
Execution label: `WITHOUT_VERIFIED_BRAIN`  
Status of unrestricted FEI: **OPEN / NOT PROVED**

## 0. What moved

This run continues the signed route after the fleet01 dimension-free noisy-square bank and the newer Shapley/plaquette + q-flip Radon handoff. It does not audit the settled read-once certificate.

There are two positive exact results and one rigorous obstruction.

1. The physical cut field is not merely analogous to a noisy-square correlation field. Under **one-coordinate noise** it is exactly the normalized nonconstant noisy square:

   \[
   (T_t^{(i)}f)^2=1-(1-t^2)\eta_i,
   \qquad
   \widehat{(T_t^{(i)}f)^2}(U)=-(1-t^2)\widehat\eta_i(U)\quad(U\ne0).
   \]

   Thus the source-side map requested by the previous fleet01 report has norm one after the correct anisotropic change of semigroup.

2. The q-flip frustration profile has an exact Fourier transform with **nonpositive nonconstant coefficients**. Its centered `L2` norm is at most twice the cut energy. Consequently any mean-zero displacement kernel of uniformly bounded `L2` norm is paid linearly by influence (or by `J` after the legitimate character gauge). This is a dimension-free payment theorem directly on the q-flip activity field.

3. However, the actual random-coordinate-order **raw dual-generator entropy kernel** from the Shapley/plaquette handoff fails that bounded-kernel target in a much stronger way than the earlier positive-baseline calculation showed. Even after subtracting its constant mode, every fixed low Walsh mode has multiplier of order `n`; for frequency weight `r`,

   \[
   A_{n,r}=\frac{4n}{(r+1)(r+2)}+O_r(1).
   \]

   A two-variable parity-switch Boolean function embedded with `n-2` dummy coordinates realizes the `r=1` mode, so merely centering the raw baseline still costs asymptotically `2n/3` times the distinguished-coordinate influence. Therefore **mean cancellation is not enough**. The plaquette/terminal/R16 refunds must cancel the low nonconstant displacement modes as well.

This kills the subroute “apply the Radon `L2` payment to the centered generator-entropy baseline.” It does **not** kill the signed Shapley/plaquette route; instead it specifies the exact cancellation that the combined residual kernel must exhibit.

No publication-priority or novelty claim is made.

---

## 1. Exact coordinate-noise realization of the cut field

Let

\[
\eta_i(x)=\frac{1-f(x)f(x^{\oplus i})}{2}\in\{0,1\},
\qquad
\alpha_i=\mathbb E\eta_i=\operatorname{Inf}_i(f).
\tag{1.1}
\]

Let `T_t^{(i)}` noise only coordinate `i` and leave all other coordinates fixed:

\[
T_t^{(i)}f(x)
=\frac{1+t}{2}f(x)+\frac{1-t}{2}f(x^{\oplus i}),
\qquad 0\le t\le1.
\tag{1.2}
\]

### Theorem 1.1 — `B16-COORDINATE-NOISE-CUT-IDENTITY`

For every Boolean `f`, every coordinate `i`, and every `0<=t<=1`,

\[
\boxed{
(T_t^{(i)}f(x))^2
=1-(1-t^2)\eta_i(x).
}
\tag{1.3}
\]

Consequently, if

\[
C_U^{(i)}(t)
:=\widehat{(T_t^{(i)}f)^2}(U),
\]

then

\[
\boxed{
C_0^{(i)}(t)=1-(1-t^2)\alpha_i,
\qquad
C_U^{(i)}(t)=-(1-t^2)\widehat\eta_i(U)\quad(U\ne0).
}
\tag{1.4}
\]

In particular,

\[
\boxed{
\sum_{U\ne0} C_U^{(i)}(t)^2
=(1-t^2)^2\alpha_i(1-\alpha_i).
}
\tag{1.5}
\]

#### Proof

If the `i`-edge at `x` is an agreement edge, then `f(x)=f(x^i)` and `T_t^{(i)}f(x)=f(x)`, so the square is `1`. If it is a disagreement edge, then `f(x^i)=-f(x)` and `T_t^{(i)}f(x)=t f(x)`, so the square is `t^2`. This is exactly (1.3). Fourier expansion gives (1.4). Since `eta_i^2=eta_i`, Parseval gives

\[
\sum_{U\ne0}\widehat\eta_i(U)^2
=\alpha_i-\alpha_i^2,
\]

which yields (1.5). `square`

### Corollary 1.2 — the requested source map is an exact isometry

For every `t<1`,

\[
\boxed{
\widehat\eta_i(U)
=-\frac{C_U^{(i)}(t)}{1-t^2},\qquad U\ne0.
}
\tag{1.6}
\]

Thus the cut-Fourier source in the previous fleet01 compiler criterion does not require a lossy abstract operator into noisy-square correlations: after switching from isotropic noise to one-coordinate noise, the map is literally scalar multiplication.

There is also a boundary-derivative form. If `C_U(r_1,...,r_n)` is the anisotropic noisy-square correlation, then for `U ne 0`,

\[
\boxed{
\widehat\eta_i(U)
=\frac12\left.\partial_{\log r_i}C_U(r_1,...,r_n)\right|_{r_1=\cdots=r_n=1}.
}
\tag{1.7}
\]

For `i in U` both sides vanish. For `i notin U`, writing the Boolean convolution as the sum over `i in S` and `i notin S`, terminal Booleanity `C_U(1)=0` makes the two halves opposite, and the derivative picks twice the `i in S` half.

This identity is useful because it preserves the original coordinate geometry exactly; no Hamming-path surrogate is introduced.

---

## 2. Exact Fourier inversion of the q-flip frustration profile

Because `eta_i(x)=eta_i(x^i)`, identify it with a function on

\[
W_i\cong\mathbb F_2^{n-1}.
\]

For `w in W_i`, define the physical two-edge/q-flip frustration probability

\[
p_i(w)
:=\Pr_x[\eta_i(x)\ne\eta_i(x+w)].
\tag{2.1}
\]

The preceding Shapley/Radon handoff proved

\[
p_i(w)=4\sum_{U:\,U\cdot w=1}\widehat\eta_i(U)^2.
\tag{2.2}
\]

Set

\[
E_i:=\sum_{U\ne0}\widehat\eta_i(U)^2
=\alpha_i(1-\alpha_i).
\tag{2.3}
\]

### Theorem 2.1 — `B16-QFLIP-RADON-FOURIER-INVERSION`

With normalized Walsh transform on `W_i`,

\[
\boxed{
\widehat p_i(0)=2E_i,
\qquad
\widehat p_i(U)=-2\widehat\eta_i(U)^2\quad(U\ne0).
}
\tag{2.4}
\]

Equivalently,

\[
\boxed{
p_i(w)=2E_i-2\sum_{U\ne0}\widehat\eta_i(U)^2(-1)^{U\cdot w}.}
\tag{2.5}
\]

Hence every nonconstant Walsh coefficient of the q-flip frustration profile is nonpositive. In particular `p_i` is a conditionally negative-definite function on the displacement group.

#### Proof

Use

\[
1_{\{U\cdot w=1\}}=\frac{1-(-1)^{U\cdot w}}2
\]

in (2.2). Then

\[
p_i(w)=2\sum_{U\ne0}\widehat\eta_i(U)^2
-2\sum_{U\ne0}\widehat\eta_i(U)^2(-1)^{U\cdot w},
\]

which is (2.5), and orthogonality gives (2.4). `square`

Combining (1.4) and (2.2) gives an exact one-coordinate-noise version of the q-flip bridge:

\[
\boxed{
p_i(w)
=\frac4{(1-t^2)^2}
\sum_{U:\,U\cdot w=1} C_U^{(i)}(t)^2,
\qquad t<1.}
\tag{2.6}
\]

So the q-flip activity profile is a Radon transform of the **same** noisy-square field, with no unknown source operator left.

---

## 3. A dimension-free kernel payment directly on q-flip activity

The Fourier inversion immediately yields an `L2` estimate at the correct linear-in-cut scale.

### Theorem 3.1 — `B16-CENTERED-QFLIP-L2-PAYMENT`

For every coordinate `i`,

\[
\boxed{
\|p_i-2E_i\|_{L^2(W_i)}^2
=4\sum_{U\ne0}\widehat\eta_i(U)^4
\le4E_i^2,
}
\tag{3.1}
\]

hence

\[
\boxed{
\|p_i-2E_i\|_2\le2E_i\le2\alpha_i.
}
\tag{3.2}
\]

Therefore, for every mean-zero displacement kernel `k_i:W_i->R`,

\[
\boxed{
\left|\mathbb E_w k_i(w)p_i(w)\right|
\le2E_i\|k_i\|_2.
}
\tag{3.3}
\]

If `sup_i ||k_i||_2 <= K`, then

\[
\boxed{
\sum_i\left|\mathbb E_w k_i(w)p_i(w)\right|
\le2K I(f).
}
\tag{3.4}
\]

After multiplying `f` by a minimizing character `chi_T`, `eta_i` is either unchanged or complemented, so `p_i` and `E_i` are unchanged while the new coordinate influences are `min(alpha_i,1-alpha_i)`. Since

\[
E_i=\alpha_i(1-\alpha_i)\le\min(\alpha_i,1-\alpha_i),
\]

(3.4) improves to

\[
\boxed{
\sum_i\left|\mathbb E_w k_i(w)p_i(w)\right|
\le2K J(f).
}
\tag{3.5}
\]

#### Proof

Parseval and (2.4) give the equality in (3.1). Since the nonnegative numbers `ehat_i(U)^2` sum to `E_i`, their squared sum is at most `E_i^2`. This gives (3.2). For mean-zero `k_i`, the constant `2E_i` is orthogonal to `k_i`; Cauchy-Schwarz gives (3.3), and summation gives (3.4). The gauge statement follows from the complement observation. `square`

### Interpretation

This is stronger than the earlier generic dual-energy criterion in one important respect. The second square root of influence is already present because the physical q-flip activity is **quadratic** in the cut Fourier coefficients. If the fully refunded Shapley residual can be written as a uniformly `L2`-bounded mean-zero displacement kernel against `p_i`, linear payment by `J` follows immediately.

The next question is whether the actual Shapley/plaquette residual kernel has that bounded norm after its exact refunds. The answer for the **raw generator-entropy baseline**, even after centering, is no.

---

## 4. Random-order dual-generator baseline kernel

Use the ordered-min q-flip basis from the Shapley/plaquette handoff, but randomize the physical coordinate order uniformly. Fix an edge direction `i` and write `m=n-1`. For a nonzero displacement `w in W_i` with `k=|w|`, let `K_n(w)` be the expected dual-generator entropy attached to that displacement with the indicator that `i` is the pivot.

If the rank of `i` is `r` and `c=n-r+1`, then the corresponding dual generator is a codimension-`c` subcube defect with entropy `H_c`. Conditional on this rank, all `k` coordinates of `w` must lie among the `c-1` coordinates after `i`. Hence

\[
\boxed{
K_n(w)
=\frac1n\sum_{c=k+1}^n
H_c\frac{\binom{c-1}{k}}{\binom{n-1}{k}},
\qquad w\ne0,
}
\tag{4.1}
\]

and set `K_n(0)=0`.

The previous raw support-load number is exactly

\[
B_n=\frac12\sum_{w\ne0}K_n(w)
=\frac1{2n}\sum_{c=2}^n(2^{c-1}-1)H_c.
\tag{4.2}
\]

To compare this unnormalized displacement sum with Theorem 3.1, put

\[
\mathcal K_n(w):=2^m K_n(w).
\tag{4.3}
\]

Then `E_w mathcal K_n = sum_w K_n = 2B_n`, so the earlier `Theta(n)` positive baseline is the constant Walsh mode of `mathcal K_n`.

A natural hope was that the constant mode was the only bad one and that the plaquette/terminal telescope merely had to center the kernel. The next theorem disproves that hope.

---

## 5. Low Walsh modes of the centered raw baseline still grow linearly

For a frequency `U subset W_i` of size `r`, define the unnormalized Walsh multiplier

\[
A_{n,r}:=\sum_{w\in W_i}K_n(w)(-1)^{U\cdot w}
=\widehat{\mathcal K_n}(U).
\tag{5.1}
\]

By radial symmetry it depends only on `r`.

### Theorem 5.1 — `B16-RAW-BASELINE-LOWMODE-OBSTRUCTION`

For every `1<=r<=n-1`,

\[
\boxed{
A_{n,r}
=\frac1n\sum_{c=2}^n H_c
\left[
2^{c-1}
\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}
-1
\right],
}
\tag{5.2}
\]

where the binomial ratio is zero when `c-1>n-1-r`.

For each fixed `r`, using

\[
H_c=8c2^{-c}+O(2^{-c})
\tag{5.3}
\]

from the subcube-defect entropy formula,

\[
\boxed{
A_{n,r}
=\frac{4n}{(r+1)(r+2)}+O_r(1).
}
\tag{5.4}
\]

In particular,

\[
\boxed{A_{n,1}=\frac23 n+O(1).}
\tag{5.5}
\]

Thus subtracting the constant mode of the random-order generator-entropy kernel does **not** produce a dimension-free `L2` or Fourier-multiplier kernel: its first nonconstant mode is already linear in `n`.

#### Proof of (5.2)

Swap the random-order expectation with the sum over displacements. Conditional on `i` having codimension parameter `c`, the allowed displacements are exactly the nonempty subsets of a uniformly random `(c-1)`-subset `A` of the other `m=n-1` coordinates. For fixed frequency set `U`,

\[
\sum_{\varnothing\ne w\subseteq A}(-1)^{U\cdot w}
=2^{c-1}1_{\{U\cap A=\varnothing\}}-1.
\tag{5.6}
\]

The probability that a uniformly random `(c-1)`-subset `A` avoids a fixed `r`-subset `U` is

\[
\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}.
\]

Average (5.6) over `A`, multiply by `H_c`, then average the rank/codimension uniformly over `c`, giving (5.2).

#### Proof of (5.4)

Equation (5.3) implies

\[
2^{c-1}H_c=4c+O(1)
\tag{5.7}
\]

uniformly after enlarging the absolute constant to absorb finitely many small `c`. Also `sum_c H_c<infinity`, so the `-H_c` contribution in (5.2) is `O(1/n)`.

For fixed `r`, the avoidance ratio in (5.2) is a degree-`r` product which, with `c/n -> x`, converges uniformly away from an `O_r(1/n)` endpoint layer to `(1-x)^r`. Hence the main sum is a Riemann sum:

\[
\frac1n\sum_{c=2}^n
4c\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}
=4n\int_0^1 x(1-x)^r\,dx+O_r(1).
\]

Since

\[
\int_0^1x(1-x)^r\,dx=\frac1{(r+1)(r+2)},
\]

(5.4) follows. `square`

For `r=1` there is also the exact simplification

\[
A_{n,1}
=\frac1n\sum_{c=2}^n H_c
\left[
2^{c-1}\frac{n-c}{n-1}-1
\right].
\tag{5.8}
\]

---

## 6. A Boolean family realizes the bad singleton mode

The low-mode growth above is not an abstract kernel pathology that Boolean cut profiles avoid.

Let `z` be the distinguished coordinate `i`, let `y_1` be one other coordinate, and let the remaining `n-2` coordinates be dummy variables. Define

\[
A(y_1)=\frac{1+y_1}{2},
\qquad
B(y_1)=\frac{1-y_1}{2},
\qquad
f_n(y_1,z,\text{dummies})=A(y_1)+zB(y_1).
\tag{6.1}
\]

This is the two-variable parity-switch/one-corner defect extended trivially to dimension `n`. For the `z` direction,

\[
\eta_z(y)=B(y_1)=\frac{1-y_1}{2},
\qquad
\alpha_z=\frac12,
\qquad
E_z=\frac14.
\tag{6.2}
\]

Its q-flip activity profile is exactly

\[
\boxed{p_z(w)=1_{\{w_1=1\}}=\frac{1-\chi_{\{1\}}(w)}2.}
\tag{6.3}
\]

Therefore, after subtracting the constant mode of the normalized baseline kernel,

\[
\boxed{
\mathbb E_w
\left(\mathcal K_n(w)-\mathbb E\mathcal K_n\right)p_z(w)
=-\frac12A_{n,1}.
}
\tag{6.4}
\]

Since `Inf_z(f_n)=1/2`,

\[
\boxed{
\frac{\left|\mathbb E_w(\mathcal K_n-\mathbb E\mathcal K_n)p_z\right|}
{\operatorname{Inf}_z(f_n)}
=A_{n,1}
=\frac23n+O(1).
}
\tag{6.5}
\]

The whole Boolean function actually depends on only two variables; its Fourier entropy and influence are independent of the number of dummy coordinates. Thus (6.5) is a particularly sharp diagnostic: the `Theta(n)` low-mode loss is an artifact of the **unrefunded representation**, and any valid dimension-free compiler must cancel it exactly enough to restore dummy-variable invariance.

This refutes every attempted closure of the form

\[
\left|\mathbb E_w k_n(w)p_i(w)\right|
\le C\operatorname{Inf}_i(f)
\]

where `k_n` is merely the centered raw generator-entropy kernel from (4.3) and `C` is universal.

It does **not** refute the fully signed Shapley/plaquette identity, because that identity includes the curvature bank and terminal Shapley share which were omitted from `mathcal K_n` here.

---

## 7. The corrected closure target

The new exact source identity and the obstruction together sharpen the target.

Let the fully refunded, basis-averaged displacement kernel for physical direction `i` be `R_i(w)`, after combining

- dual-generator entropy,
- the signed Shapley plaquette/cross-ratio bank,
- the terminal Shapley share,
- and the inherited R16/moment credits without double counting.

If the constant part is separately accounted for and

\[
\boxed{
\sup_i\|R_i-\mathbb E R_i\|_{L^2(W_i)}\le K
}
\tag{7.1}
\]

with a universal `K`, then Theorem 3.1 pays the q-flip activity contribution by at most `2KJ(f)`.

A stronger Fourier-multiplier target is

\[
\boxed{
\sup_{i}\sup_{U\ne0}|\widehat R_i(U)|\le K.
}
\tag{7.2}
\]

Because the q-flip Fourier coefficients are `-2 eta_hat_i(U)^2`, (7.2) directly gives

\[
\left|\mathbb E_w(R_i-\mathbb ER_i)p_i\right|
\le2K E_i,
\]

and summing gives `<=2KJ(f)` after the gauge.

The raw baseline fails (7.2) at every fixed low mode by (5.4). Therefore the next signed calculation should not estimate its plaquette/terminal terms as small errors. It should compute their **low Walsh multipliers** and test whether they cancel the explicit profile

\[
\frac{4n}{(r+1)(r+2)}+O_r(1).
\tag{7.3}
\]

The dummy-coordinate family (6.1) is the first exact test: because the underlying function is genuinely two-dimensional, the complete residual must not retain an `n`-dependent singleton multiplier. If the full Shapley/plaquette/terminal combination cancels (5.5), the next task is to prove the cancellation for every fixed `r` and then control the remaining high-frequency band with the fleet01/fleet03 noisy-square fractional-resolvent banks. If the complete residual still has (5.5), this basis-averaged route is dead.

---

## 8. Executed checks

Companion code: `check.py` in this folder.

The locally executed bytes had SHA-256

`2f33decd6698a115ebcc2cd3632415818a75f3295c66379bf042dbde8339e232`.

It returned `PASS` and performed:

- **2,412 exact rational coordinate-noise checks** through all Boolean functions on `n<=3`, at `t=0,1/2,2/3`, verifying (1.4);
- **800 exact rational q-flip Radon/Fourier checks** for every Boolean function at `n=2,3`, including (2.4) and (3.1);
- an independent combinatorial check of the singleton multiplier formula through `n=15`;
- numerical evaluation of the proved multiplier formula at `n=10,20,40,80`.

For `(r=1,2,3)`, the observed `A_{n,r}/n` at `n=80` was

\[
(0.663162411430,\ 0.329497256392,\ 0.195990628116),
\]

against the predicted limits

\[
(2/3,\ 1/3,\ 1/5).
\]

The parity-switch centered-pairing ratio in (6.5), namely `A_{n,1}`, was

\[
5.052044993087,\ 12.517741944303,\ 26.299930950032,\ 53.052992914408
\]

for `n=10,20,40,80`.

The finite checks support the algebraic formulas; the all-dimensional statements above are proved directly and do not depend on enumeration.

---

## 9. Before / after

**Before:** fleet01 had a dimension-free isotropic signed noisy-square bank and an unresolved cut-to-sink operator; the Shapley handoff had an exact q-flip Radon activity identity and an `n+O(1)` raw positive baseline, but did not identify whether centering that baseline was sufficient.

**After:** the cut field is exactly a one-coordinate noisy-square correlation field, the q-flip activity profile has an explicit negative Fourier spectrum and a dimension-free centered-kernel payment, and centering the actual raw baseline is rigorously shown to be insufficient: its fixed low modes grow linearly in ambient dimension and a valid two-variable Boolean function with dummy coordinates realizes the bad singleton mode.

**Status:** `PARTIAL / PROVED LEMMAS + RIGOROUS SUBROUTE OBSTRUCTION / FULL FEI OPEN`.

**Next B16 move:** compute the singleton and low-weight displacement multipliers of the *combined* Shapley curvature plus terminal share on the dummy-extended parity-switch family. The first required cancellation is exactly `A_{n,1}` from (5.8). If it cancels, derive the general fixed-`r` Ward identity forced by dummy-variable invariance and use the fractional noisy-square bank for the high-frequency remainder. If it does not cancel, abandon this random-order q-flip basis route.