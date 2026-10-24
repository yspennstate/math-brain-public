# B12 FEI — four-generation AND bootstrap closes the complementary-data MUX midline

**Status:** `ESSENTIAL_STEP_APPLIED / NONUNATE_MUX_SLICE_CLOSED / FULL_FEI_OPEN`.

Full unrestricted uniform-cube Fourier entropy-influence remains **OPEN / NOT PROVED**. This report proves the live fixed candidate on one exact infinite, genuinely unequal-data MUX slice. It is not a finite-sample extrapolation and is not promoted to full FEI.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository controls and mathematical source files were read directly. No native authenticated mathematical-brain receiver/context was used.

## 0. Live target and last-three comparison

Fresh owner control revision `2026-09-22.2` supersedes the older B12 harmonic-row wording for substantive work and directs all FEI workers to the all-gate inequality

\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\tag{0.1}
\]

for every Boolean gate and every product bias. The gate-reformulation continuation proves that a finite symmetric nonnegative `Gamma` satisfying (0.1) is equivalent to full FEI.

The last three completed own B12 mechanisms before this run were:

1. `20260922T035404Z-balanced-bent-local-obstruction/REPORT.md`, blob `606cbb7078cb2fc76d8e749a84f2dcab4a4061ab`: a genuine bent/two-point selector refuted every finite **pointwise local** restriction payment; descendant slack must be used nonlocally.
2. `20260922T025438Z-gate-margin-falsification/REPORT.md`, blob `bf37b4fd5ceae2c40e2b59266e2701fed8ff2780`: exact `G10` and the shared-graft family refuted AND/read-once extremality for the old potential.
3. `20260922T013941Z-shared-graft-tail/REPORT.md`: proved an infinite source-valid balanced-gate tail and the lower floor `C_FEI>6.5218509495457`.

So this run does not reopen rank/l1, sign-free profiles, ordinary depth, fixed-relative near-subcube, or the now-refuted pointwise-local payment. It implements the missing nonlocal idea on the same all-gate target: **bootstrap a lower bound on the potential through four certified descendant AND constraints before paying one unequal-data MUX node.**

The FLEET_RULES moves used are: #18 translate the gate into exact biased Fourier coordinates; #19 turn the descendant bootstrap into a finite exact interval algorithm; #30 descend one dyadic scale at a time until the source tail dominates.

## 1. Completed other-account results consumed and applied

### 1.1 account01/B18: live candidate and common-data closure

Consumed:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`, blob `6deb28dc6f2e8f36da01fdc7ac24f600f7553a5c`.

It fixes

\[
C^\dagger=6.521851214,
\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\tag{1.1}
\]

and

\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\tag{1.2}
\]

It proves the exact common-data MUX/addressing star inequality and records the source-bound h96 lower envelope: on `0<u<=1/2`, with `x=log_2(1/u)` and `Gamma_0(u)=uG(x)`,

\[
\boxed{G(x)-4.9096x>2.22.}
\tag{1.3}
\]

The underlying committed h96 output records global wobble minimum `2.22922`, so (1.3) has a large displayed buffer. This run imports (1.3) as the completed source premise; it does not claim to independently recertify the binary h96 array.

### 1.2 account04/B12: the remaining center frontier is non-unate

Consumed:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T041709Z-arity5-unate-tube/REPORT.md`, blob `dbcdec2298fa2a7ae97c3250b7c04a68c29ef64d`.

It proves every balanced essential unate five-input gate obeys

\[
{H(G)\over I(G)-1}
\le {44\over5}-{9\over5}\log_2 3
=5.9470674987\ldots<6,
\tag{1.4}
\]

so any five-input center falsifier for the live `C^dagger` must be non-unate. This is used here to avoid another monotone/unate center search: the MUX is the canonical non-unate selector gate, and account01/B18 had explicitly left the **unequal-data** MUX as its nearest unclosed extension.

A contemporaneous account03/B12 run produced arithmetic diagnostics for this same unequal-data direction but had no completed report at the scientific revision read here; it is not counted as the required completed peer theorem.

## 2. Exact biased spectrum of one-bit MUX

Let

\[
M(a,x_0,x_1)=(1-a)x_0+a x_1
\]

with independent Bernoulli biases

\[
\Pr[a=1]=t,\qquad \Pr[x_0=1]=q_0,\qquad \Pr[x_1=1]=q_1.
\]

Use the standard normalized biased basis and the `{-1,+1}` output `f=1-2M`. Put

\[
r=(1-t)q_0+tq_1.
\]

A direct expansion gives exactly six possibly nonzero squared Fourier masses:

\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_a&=V_t(q_1-q_0)^2,\\
w_0&=(1-t)^2V_{q_0},\\
w_1&=t^2V_{q_1},\\
w_{a0}&=t(1-t)V_{q_0},\\
w_{a1}&=t(1-t)V_{q_1}.
\end{aligned}
\tag{2.1}
\]

Their sum is one. Hence the biased influences are

\[
\operatorname{It}_a=V_t d,
\quad d=q_0+q_1-2q_0q_1,
\quad
\operatorname{It}_0=(1-t)V_{q_0},
\quad
\operatorname{It}_1=tV_{q_1}.
\tag{2.2}
\]

All signs and the actual Boolean source are retained; no arbitrary-row replacement occurs.

## 3. Complementary data at balanced address: exact scalar reduction

Set

\[
t={1\over2},\qquad q_0=q,\qquad q_1=1-q,\qquad 0<q\le {1\over2},
\]

and write `V=V_q`. Then `r=1/2`, `d=1-V/2`, and (2.1) becomes

\[
\boxed{0,\ 1-V,\ V/4,\ V/4,\ V/4,\ V/4.}
\tag{3.1}
\]

Therefore

\[
\widetilde H_M=h_2(V)+2V.
\tag{3.2}
\]

Because `Gamma` is symmetric, the two data terms in (0.1) combine. For any symmetric `Gamma` with center `C=Gamma(1/2)`, the all-gate slack on this line is exactly

\[
\boxed{
D_\Gamma\!\left(M;{1\over2},q,1-q\right)
=\Gamma(q)-V_q\left({C\over2}+2\right).
}
\tag{3.3}
\]

Thus for the live candidate define

\[
B:={C^\dagger\over2}+2=5.260925607,
\qquad
F(q):=\Gamma^\dagger(q)-V_q B.
\tag{3.4}
\]

The entire complementary-data midline is closed exactly if `F(q)>=0` on `(0,1/2]`.

## 4. The descendant AND recursion

The already-certified AND inequality at input biases `(q,1/2)` has spectral masses

\[
(1-q)^2,\quad q(1-q),\quad q^2,\quad q(1-q),
\]

which form the product distribution of two Bernoulli-`q` bits. Hence its spectral entropy is exactly `2h_2(q)`. Its gate inequality is

\[
\Gamma^\dagger(q/2)+2h_2(q)
\le {1\over2}\bigl(\Gamma^\dagger(q)+h_2(V_q)\bigr)+qC^\dagger.
\tag{4.1}
\]

Rearranging gives

\[
\Gamma^\dagger(q)
\ge 2\Gamma^\dagger(q/2)
+4h_2(q)-h_2(V_q)-2qC^\dagger.
\tag{4.2}
\]

Since

\[
2V_{q/2}-V_q=2q^2,
\]

(4.2) becomes the exact lower recursion

\[
\boxed{
F(q)\ge2F(q/2)+R(q),
}
\tag{4.3}
\]

where

\[
R(q):=4h_2(q)-h_2(V_q)-2qC^\dagger+2q^2B.
\tag{4.4}
\]

Four iterations yield

\[
F(q)\ge16F(q/16)
+R(q)+2R(q/2)+4R(q/4)+8R(q/8).
\tag{4.5}
\]

This is the nonlocal step absent from the preceding pointwise-local restriction attempt: a possibly adverse present-scale term is allowed to borrow from four already-certified smaller-scale AND constraints before the MUX charge is assessed. No MUX influence or information credit is counted twice; (4.5) is a derived functional lower bound on `Gamma^dagger`.

## 5. Source tail closes the fifth scale

From (1.1)--(1.3), with

\[
\alpha=4.9096,
\qquad
K:=4B-a^\dagger=20.775497572,
\]

we obtain for every `0<u<=1/2`

\[
\begin{aligned}
F(u)
&>u\left[
\alpha\log_2{1\over u}+2.22
-K(1-u)
\right].
\end{aligned}
\tag{5.1}
\]

Putting `u=q/16`, equations (4.5) and (5.1) imply

\[
F(q)>\mathcal L(q),
\tag{5.2}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal L(q)
={}&q\left[
\alpha\log_2{16\over q}+2.22-K(1-q/16)
\right]\\
&+R(q)+2R(q/2)+4R(q/4)+8R(q/8).
\end{aligned}}
\tag{5.3}
\]

It remains only to prove the one-variable inequality `L(q)>0`.

## 6. Analytic tiny-q branch

For `0<z<=1/4`, use the standard entropy bounds

\[
h_2(z)\ge z\log_2(1/z),
\qquad
h_2(x)\le x\log_2(e/x).
\]

Since `V_z<=4z<=1` and `x log_2(e/x)` is increasing on `(0,1)`, while `e<4`,

\[
h_2(V_z)
\le4z\log_2{e\over4z}
<4z\log_2{1\over z}
\le4h_2(z).
\tag{6.1}
\]

Thus the entropy part of every `R(q/2^j)` is nonnegative. If `0<q<=2^{-11}`, then `log_2(16/q)>=15`, so after dropping the positive quadratic terms,

\[
\begin{aligned}
\mathcal L(q)
&\ge q\,[15\alpha+2.22-K-8C^\dagger]\\
&=q\,{728423179\over250000000}\\
&=2.913692716\,q>0.
\end{aligned}
\tag{6.2}
\]

This covers the singular endpoint analytically; no finite grid is used there.

## 7. Exact rational interval certificate on the compact remainder

For

\[
2^{-11}\le q\le1/2,
\]

`check_complementary_mux.py` supplies a finite **interval proof**, not a point sample. It splits each of the ten dyadic octaves into 128 rational cells, for 1280 cells total. On each cell `[l,u]` it lower-bounds every term of (5.3) in the adverse monotone direction:

* `q log_2(16/q)` is increasing on this range, so use `l`;
* `q(1-q/16)` is increasing, so its negative term uses `u`;
* `h_2(z)` is increasing for `z<=1/2`, so positive entropy terms use the left endpoint;
* `V_z` is increasing, and `h_2` rises to `1/2` then falls, so the negative `h_2(V_z)` term uses the appropriate endpoint, or the exact upper bound `1` if a cell crosses `V_z=1/2`;
* negative linear terms use the right endpoint and positive quadratic terms the left.

Every logarithm at a rational endpoint is enclosed using exact `Fraction` arithmetic and

\[
\ln x
=2\sum_{n=0}^{N-1}{y^{2n+1}\over2n+1}+R_N,
\qquad
0\le R_N\le
{2y^{2N+1}\over(2N+1)(1-y^2)},
\tag{7.1}
\]

after exact power-of-two scaling to `1<=x<=2`, where `0<=y=(x-1)/(x+1)<=1/3`. The checker uses `N=14`. Every cell's lower bound is an exact rational and is asserted strictly positive.

Executed output:

```text
PASS
candidate_C 6.521851214
quadratic_lift_a 0.268204856
B=C/2+2 5.260925607
alpha 4.9096
K 20.775497572
small_branch_constant_exact 728423179/250000000
small_branch_constant_decimal 2.913692716000000
interval_cells 1280
min_interval_lower_decimal 0.016155516990529
min_cell_left 1/2048
min_cell_right 129/262144
ln2_width_upper 1.130e-15
classification exact-rational sign certificate for scalar four-step lower envelope; source Gamma tail premise imported
```

The executed checker SHA-256 is

`4b294a8f68b7fce3d5703a38b0740eb771f4dce69789364141dcf42a9c5ccc57`.

The displayed decimal minimum is diagnostic only; the proof assertion is the exact rational sign on every cell.

## 8. Theorem and quantified remaining implication

### Theorem 8.1 — complementary-data MUX midline

Assuming the completed source-bound h96 premise (1.3) for the fixed `Gamma^dagger`, for every `0<q<1`,

\[
\boxed{
D_{\Gamma^\dagger}\!\left(M;{1\over2},q,1-q\right)>0.
}
\tag{8.1}
\]

The statement for `q>1/2` follows by exchanging the two complementary data labels and symmetry. Boundary values follow by continuity.

This is a genuine unequal-data family: except at `q=1/2`, the two data biases differ, and at `q=1/4` they are the explicit interior pair `(1/4,3/4)`. The proof is source-bound to one actual Boolean gate, preserves the exact six spectral masses and all influence prices, and uses no arbitrary row model.

**FULL-PROBLEM CHANGE:** none. No universal FEI upper bound is proved, and `C_FEI<infinity` remains open. The live fixed candidate is not proved for all gates/biases.

**MECHANISM CHANGE:** yes. Before this run the newest own result showed that every finite pointwise local restriction payment fails on a genuine bent-selector family. After this run, one previously open non-unate unequal-data gate slice is paid by a **four-generation descendant bootstrap plus one source tail payment**. This is the first B12 use in the live all-gate programme of descendant potential slack as an explicit nonlocal amortization rather than a nodewise charge.

**Quantified remaining implication:** prove

\[
D_{\Gamma^\dagger}(P;p)\ge0
\]

for every composition-prime Boolean gate `P` and every interior bias vector, or find an exact Boolean counterexample. Within one-bit MUX, the remaining two-dimensional obstruction is to release the restrictions `t=1/2` and `q_1=1-q_0`; the exact six-mass formula (2.1) is now the starting point. Beyond MUX remain general biased non-unate prime gates. The account04/B12 theorem removes the balanced-uniform unate five-input center from that search, but not the off-center or non-unate sectors.

## 9. Scope / privacy / non-closure

Changed files in this run contain only mathematical derivation, a standard-library checker, and its sanitized output. A manual changed-file review found no credentials, scheduler identifiers, machine paths, email/Drive data, benchmark gold, raw transcripts, unrelated private data, or publication action. No permission, workflow, scheduler, notification, email, Drive, or paid/remote-model change is made here.

This report preserves all predecessor failures. In particular it does **not** revive pointwise local payment, global rank/l1, sign-free profiles, ordinary depth/positive-defect, or fixed-relative near-subcube arguments. Full FEI remains OPEN.
