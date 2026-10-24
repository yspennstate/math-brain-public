# account02/B15 — universal likelihood-shell compiler for the exact I-projection KL

**Run:** `20260922T110507Z-account02-B15-sparse-suspension-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / UNIVERSAL_LOG_KL_COMPILER / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Exact target, predecessor, and movement

The active owner programme is `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`. The exact account02/B15 assignment is **Sparse-suspension logarithmic compiler**.

The canonical Path-B source identity is the account02/B15 I-projection theorem

\[
R_\Gamma(G;p)
=
B_{\rm inf}^\Gamma(G;p)+K_{\rm occ}(G;p),
\qquad
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r),
\tag{0.1}
\]

where `P=w^+` is the actual nonempty biased spectral law, `r_i=P(i\in S)`, `Q_r` is the unique maximum-entropy conditional-product law with those occurrence marginals, and

\[
\mu:=\sum_i r_i=\mathbb E_P|S|\ge1.
\tag{0.2}
\]

At a balanced uniform source this becomes

\[
H(f)=H_{\max}(r)-K_{\rm occ}(f),
\qquad
\mu=I(f).
\tag{0.3}
\]

The immediately preceding account02/B15 report `20260922T103316Z-account02-B15-r11` proved a two-log-bin compiler with loss at most `2[I(F)-1]` on every character suspension, exact degree/magnitude-cell compilers on the sparse defect and recursive-majority stress families, and left the universal obligation

\[
K_{\rm occ}(f)-\widetilde K(f)\le L[I(f)-1]
\tag{0.4}
\]

for all balanced Boolean sources.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.

**MECHANISM CHANGE:** `separate floor bins for -log P and -log Q on the suspension face -> one global quantized log-likelihood-ratio shell after the full I-projection, with singleton atoms retained exactly`.

**TARGET-LEVEL CHANGE:** (0.4) is now proved for **every nonempty spectral source**, at arbitrary product bias, with `L=1` for unit-width shells and more generally with arbitrary loss coefficient `delta>0`. The hierarchy KL is not paid repeatedly: one first forms the exact global likelihood ratio and quantizes only its total.

This is still not FEI closure. The remaining universal inequality is now a lower bound on an explicit one-dimensional signed likelihood-shell KL.

## 1. Named completed partner result actually consumed

The latest compatible **completed** account03/B15 result available at the fresh scientific head is

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T092409Z-complement-packet-kl-gap/REPORT.md`

at immutable source commit `2c1afb444c3a4fa2cbee12f73fd8c19c44af9e56`.

It proves, on the balanced `c<1` branch of the exact I-projection,

\[
K_{\rm occ}
\ge
\frac{d^2}{L^2\ln2},
\tag{1.1}
\]

with its source-defined complement-packet quantities `d,L`, and explicitly warns that one packet can be exponentially small.

I use (1.1) below inside the new compiler, obtaining a retained-shell lower bound with only one excess-influence surcharge. On the sparse character-suspension face the deterministic fresh coordinate forces `c=1`, so the partner theorem is exactly inapplicable there; the likelihood-shell mechanism supplies the missing logarithmic branch instead.

The other source-exact inputs used are:

* `IPROJ`, account02/B15 `20260922T0829Z-influence-iprojection-kl`, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`;
* `HIERARCHY`, account04/B15 `20260922T091017Z-iprojection-composition-transfer`, commit `2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`;
* `L2_BARRIER`, account04/B15 `20260922T093820Z-full-convolution-energy-obstruction`, commit `7ec649dfb3d1ab2f92855f2069590fca2ac956dd`;
* `LOWLEVEL_BARRIER`, account03/B18 `20260922T100641Z-lowlevel-projection-barrier`, commit `bff0d7b6c21485f386841c42582eb04f32705046`.

The last two are design constraints: neither an unweighted quadratic compression nor a fixed/sub-half-depth labelled projection may replace the rare-event logarithm.

## 2. One-dimensional likelihood-shell lemma

Let `P<<Q` be probability laws on a finite set `Omega`. Let `A` be a set of atoms to retain individually. Fix `delta>0`, and for every `x notin A` with `P(x)>0` write

\[
\ell(x)=\log_2\frac{P(x)}{Q(x)},
\qquad
b_\delta(x)=\left\lfloor\frac{\ell(x)}{\delta}\right\rfloor.
\tag{2.1}
\]

Let `sigma(x)` be any additional source label; in the Fourier application it is the actual Fourier sign. Define `Z_delta` by

* keeping each `x in A` as its own label;
* placing all `P(x)=0` atoms in a separate zero-source label;
* otherwise recording `(sigma(x),b_delta(x))`.

Put

\[
K_\delta(P,Q):=
D_{\rm KL,2}\bigl((Z_\delta)_\#P\Vert(Z_\delta)_\#Q\bigr).
\tag{2.2}
\]

### Lemma 2.1 — likelihood-shell loss

\[
\boxed{
0\le D_{\rm KL,2}(P\Vert Q)-K_\delta(P,Q)
\le \delta\,P(A^c).
}
\tag{2.3}
\]

#### Proof

KL chain rule gives

\[
D(P\Vert Q)
=
D(P_Z\Vert Q_Z)
+
\sum_zP_Z(z)D(P(\cdot\mid z)\Vert Q(\cdot\mid z)).
\tag{2.4}
\]

Singleton fibres from `A` and zero-source fibres contribute no conditional KL.

On every remaining positive-mass fibre, all likelihood ratios

\[
L(x)=P(x)/Q(x)
\]

lie in one interval `[2^{j\delta},2^{(j+1)\delta})`. The cell ratio

\[
\bar L_z=\frac{P_Z(z)}{Q_Z(z)}
\]

is a `Q(\cdot|z)`-weighted average of those `L(x)`, hence lies in the same interval. Therefore

\[
\frac{P(x\mid z)}{Q(x\mid z)}
=\frac{L(x)}{\bar L_z}<2^\delta,
\]

and the conditional divergence on that cell is at most `delta` bits. Summing over the non-singleton positive-source cells proves (2.3). `QED`.

Compared with the preceding two-bin lemma, quantizing the **single log likelihood ratio** halves the worst-case per-cell loss from two bits to one bit when `delta=1`.

## 3. Universal nonempty-spectrum compiler

Return to the exact nonempty spectral law `P=w^+` of an arbitrary nonconstant Boolean gate at product bias, and let `Q_r` be its exact occurrence I-projection.

Take

\[
A=\{S:|S|=1\}.
\tag{3.1}
\]

Because `P` is supported on nonempty sets,

\[
\mu-1
=
\mathbb E_P(|S|-1)
=
\sum_{|S|\ge2}(|S|-1)P(S),
\tag{3.2}
\]

so

\[
\boxed{
P(|S|\ge2)\le\mu-1.
}
\tag{3.3}
\]

Define `K_shell,delta` from Lemma 2.1, retaining every singleton with its original coordinate identity and on all higher sets retaining the actual Fourier sign plus

\[
\left\lfloor
\delta^{-1}\log_2\frac{P(S)}{Q_r(S)}
\right\rfloor.
\tag{3.4}
\]

### Theorem 3.1 — `B-UNIVERSAL-LIKELIHOOD-SHELL-COMPILER-v1`

For every such nonempty spectral source,

\[
\boxed{
0\le
K_{\rm occ}-K_{\rm shell,\delta}
\le
\delta\,P(|S|\ge2)
\le
\delta(\mu-1).
}
\tag{3.5}
\]

In particular, at unit resolution,

\[
\boxed{
K_{\rm occ}-K_{\rm shell,1}\le\mu-1.
}
\tag{3.6}
\]

This theorem is distribution-theoretic once the exact source `P` and exact I-projection `Q_r` are fixed; Booleanity is retained through the fact that `P` is the actual signed Fourier source, and the sign label is preserved rather than erased.

For the physical gate normalization,

\[
r_i=\frac{\operatorname{It}_i(G;p)}{v},
\qquad
v=V_{p_{\rm out}},
\]

hence

\[
v(\mu-1)=\sum_i\operatorname{It}_i(G;p)-v.
\tag{3.7}
\]

Therefore the omitted negative relative entropy has the explicit physical payment

\[
\boxed{
0\le
v(K_{\rm occ}-K_{\rm shell,\delta})
\le
\delta\left(\sum_i\operatorname{It}_i-v\right).
}
\tag{3.8}
\]

No projection integrality, valuation depth, `l1/rank` bound or unweighted `L2` statistic enters (3.8).

The exact gate remainder is now

\[
\boxed{
R_\Gamma
=
B_{\rm inf}^\Gamma
+
K_{\rm shell,\delta}
+
L_\delta,
\qquad
0\le L_\delta\le\delta(\mu-1).
}
\tag{3.9}
\]

So the conditional KL lost by the compiler is paid once by the physical excess occurrence count.

## 4. Balanced FEI form and exact remaining implication

For a balanced uniform Boolean function,

\[
\mu=I(f),
\qquad
H(f)=H_{\max}(r)-K_{\rm occ}.
\]

Theorem 3.1 gives

\[
\boxed{
H_{\max}(r)-K_{\rm shell,\delta}
-\delta[I(f)-1]
\le H(f)
\le
H_{\max}(r)-K_{\rm shell,\delta}.
}
\tag{4.1}
\]

Consequently, a proof of

\[
\boxed{
K_{\rm shell,\delta}(f)
\ge
H_{\max}(r)-C[I(f)-1]
}
\tag{4.2}
\]

for one finite `C` proves FEI with the same `C`.

Conversely, FEI with constant `C_0` would imply (4.2) with `C=C_0+delta`. Thus, for existence of a finite dimension-independent constant, the full balanced target is equivalent up to the arbitrarily chosen additive shell width `delta` to the **one-dimensional shell-KL payment** (4.2).

This is the first still-unpaid Shannon implication after the compiler. The progress in this run is not (4.2), but the universal source-exact reduction of the entire residual KL to that scalar statistic with a proved influence surcharge.

## 5. Sparse one-point suspensions: the unit shell is exact

For

\[
p=2^{1-m},
\qquad
g_m(x)=1-2{\bf1}_{\{x=0\}},
\qquad
F_m(y,x)=y\,g_m(x),
\tag{5.1}
\]

the old-coordinate factor has

\[
P(\varnothing)=(1-p)^2,
\qquad
P(T)=p^2\quad(T\ne\varnothing),
\tag{5.2}
\]

while its I-projection is iid `Bernoulli(p)`,

\[
Q(T)=p^{|T|}(1-p)^{m-|T|}.
\tag{5.3}
\]

The full-spectrum singleton `{y}` corresponds to `T=emptyset` and is retained exactly. For `k=|T|\ge1`,

\[
\ell_k
=
\log_2\frac{p^2}{p^k(1-p)^{m-k}},
\tag{5.4}
\]

and

\[
\ell_{k+1}-\ell_k
=
\log_2\frac{1-p}{p}.
\tag{5.5}
\]

For `m>=3`, this gap is at least `log_2 3>1`, so unit likelihood shells distinguish every degree exactly. For `m=2`, the relevant conditional likelihood ratios are equal and the merger is itself lossless. Hence

\[
\boxed{
K_{\rm shell,1}(F_m)=K_{\rm occ}(F_m)
\quad\text{for every }m\ge2.
}
\tag{5.6}
\]

Thus the compiler preserves the inherited rare-event scale

\[
\frac{K_{\rm shell,1}(F_m)}{mp}
=
m-5+\frac1{\ln2}+o(1),
\tag{5.7}
\]

whereas the completed unweighted-convolution `L2` statistic is only `4mp+o(mp)`.

Combining (5.6) with the already-proved sparse entropy bound `H(g_m)<4mp` gives

\[
B_{\rm inf}^{4}(F_m)+K_{\rm shell,1}(F_m)
=
4mp-H(g_m)>0.
\tag{5.8}
\]

So the named adversarial sparse family is paid at center four by the new universal shell statistic without any special-purpose degree label.

## 6. Exact hierarchy transport: quantize once after summing all KL pieces

The completed account04/B15 hierarchy theorem gives, for a disjoint composition

\[
F=G(f_1,\ldots,f_s),
\]

the exact source/reference factorizations

\[
P_F(T,(S_i))
=
P_0(T)\prod_{i\in T}P_i(S_i),
\tag{6.1}
\]

\[
Q_s(T,(S_i))
=
Q_A(T)\prod_{i\in T}Q_i^{(\zeta)}(S_i).
\tag{6.2}
\]

Therefore the **pointwise global log likelihood** is exactly additive:

\[
\boxed{
\ell_F
=
\log_2\frac{P_0(T)}{Q_A(T)}
+
\sum_{i\in T}
\log_2\frac{P_i(S_i)}{Q_i^{(\zeta)}(S_i)}.
}
\tag{6.3}
\]

Its expectation is the full hierarchy ledger

\[
K_{\rm occ}(F)
=
K_{\rm occ}(G)
+\sum_i\alpha_iK_{\rm occ}(f_i)
+C_{\rm hier},
\qquad C_{\rm hier}\ge0.
\tag{6.4}
\]

The new compiler applies the floor **after** forming the total (6.3). Hence Theorem 3.1 gives

\[
\boxed{
K_{\rm shell,\delta}(F)
\ge
K_{\rm occ}(G)
+\sum_i\alpha_iK_{\rm occ}(f_i)
+C_{\rm hier}
-\delta[\mu_F-1].
}
\tag{6.5}
\]

All hierarchy/reference-mismatch KL is therefore retained before the single global surcharge. No level of a composition tree spends the same negative information credit again.

This is the requested composition-compatible form of the compiler; recursively quantizing each component separately is unnecessary and can accumulate avoidable losses.

## 7. Applying the completed account03/B15 complement-packet theorem

On the partner's balanced `c<1` branch, combine (1.1) with Theorem 3.1:

\[
\boxed{
K_{\rm shell,\delta}
\ge
\frac{d^2}{L^2\ln2}
-\delta[I(f)-1].
}
\tag{7.1}
\]

Thus the partner's signed Boolean complement-convolution gap survives inside the compiled statistic up to one explicitly priced excess-influence surcharge. In any region where

\[
\frac{d^2}{L^2\ln2}
>
\delta[I(f)-1]+[-B_{\rm inf}]_+,
\tag{7.2}
\]

the shell statistic alone pays the common residual.

The partner already proves that one complement packet may be exponentially small, so (7.1) is not claimed as universal closure. Its role here is exact: a source-valid Boolean KL payment can be inserted into the compiler without dropping the remaining negative relative entropy.

## 8. Mandatory recursive-majority preflight

The completed account03/B18 barrier proves that fixed or sub-half-depth labelled KL projections recover a vanishing fraction of the dependence payment on depth-`m` recursive ternary majority `M_m`.

The likelihood-shell compiler is different. The source identities are

\[
I(M_m)=\mu_m=(3/2)^m,
\qquad
H(M_m)=4(\mu_m-1),
\tag{8.1}
\]

and therefore

\[
K_{\rm occ}(M_m)
=
H_{\max}(r^{(m)})-4(\mu_m-1).
\tag{8.2}
\]

At unit resolution, Theorem 3.1 gives

\[
K_{\rm shell,1}(M_m)
\ge
H_{\max}(r^{(m)})-5(\mu_m-1).
\tag{8.3}
\]

Equivalently,

\[
\boxed{
B_{\rm inf}^{5}(M_m)
+
K_{\rm shell,1}(M_m)
\ge0
}
\tag{8.4}
\]

for **every depth**. More generally the `delta`-shell compiler pays this family at center `4+delta`.

Thus the compiler passes the mandatory recursive-majority preflight analytically. It does not keep a bounded set of low Fourier levels and one tail; it keeps all scales through the quantized total log likelihood, while losing at most one excess-influence bit in expectation.

## 9. Deterministic checks on genuine Boolean sources

The adjacent standard-library checker verifies the formulas on four source tests.

1. The heterogeneous four-bit composition-prime witness with raw Walsh vector `(0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0)`, occurrence marginals `(1/4,1/4,1/4,3/4)`, has `K_occ=0.8012879378504625`; the signed unit-shell compiler is exact to floating error.

2. The actual three-bit `OR(literal,AND)` hierarchy witness has `K_occ=0.13252104900749184`, `K_shell,1=0.12973245974808612`, and loss `0.002788589259405727`, far below both its higher-order mass `4/15` and its excess occurrence count `1/3`.

3. For sparse suspensions `2<=m<=30`, the maximum numerical discrepancy `|K_occ-K_shell,1|` is `1.11e-16`.

4. For recursive majority through depth four, the checker reconstructs the exact `(support size, Fourier exponent)` class recurrence. The largest observed shell loss divided by `I-1` is `0.0034868362560871446`, and the compiled center-five residual is positive in every checked depth.

The executed checker ends with `PASS`. These computations are falsification/implementation checks only; Lemma 2.1 and Theorems 3.1, 5.6, 6.5 and 8.4 are analytic.

## 10. Exact remaining obligation and recipient handoff

The sparse-suspension compiler subproblem is now solved more strongly than requested:

* the loss is **zero** on the one-point suspension family;
* it is at most `delta[I(F)-1]` on every balanced Boolean source;
* at arbitrary bias the physical loss is at most `delta(sum_i It_i-v)`;
* hierarchy KL is retained and charged only once globally.

The full FEI problem remains **OPEN**. The next exact Path-B implication is

\[
\boxed{
K_{\rm shell,1}(f)
\ge
H_{\max}(r)-C[I(f)-1]
}
\tag{10.1}
\]

for some finite universal `C`, or a genuine Boolean family refuting that shell payment. The statistic in (10.1) consists only of exact singleton identities, actual Fourier sign, and the integer shell of the exact likelihood ratio `P/Q_r`; no fixed-depth tail merger is present.

The recipient `account04/B17` should use (3.5)/(3.8) in its cross-path suspension transport: its canonical suspension KL can be replaced by `K_shell,1` at a cost of at most the physical excess occurrence count, while preserving its branch/reference-mismatch credits. In the critical-core gauge this gives a one-bit influence surcharge rather than discarding the dependence KL.

No novelty or publication-priority claim is made. Full unrestricted FEI is not proved.

## 11. Immutable source pins

* `yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04`: `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.
* `yspennstate/math-open-problems@2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`: `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`.
* `yspennstate/math-open-problems@2c1afb444c3a4fa2cbee12f73fd8c19c44af9e56`: `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T092409Z-complement-packet-kl-gap/REPORT.md`.
* `yspennstate/math-open-problems@7ec649dfb3d1ab2f92855f2069590fca2ac956dd`: `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md`.
* `yspennstate/math-open-problems@bff0d7b6c21485f386841c42582eb04f32705046`: `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`.
* Immediate predecessor: `yspennstate/math-open-problems@ad83138c850372d14d0dcacaa76a50a2fe79bcaf`: `proofnet24/P03-fei/fleet-2026-09-22/account02/B15/20260922T103316Z-account02-B15-r11/REPORT.md`.

Fresh scientific master observed before publication: `98dfb2962c57951bfefe163d447c0c5aebc643cf`.
