# B14 — signed-overlap rigidity inside a restriction-critical FEI core

**Run:** 2026-09-21T10:14:23Z, account04/B14  
**Role:** FEI erasure and selector proof  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`  
**Target:** full uniform-cube Fourier entropy-influence conjecture; still **OPEN / NOT PROVED**.  
**Creative moves used:** FLEET_RULES #18 (say it in another language), #25 (count the same thing twice), #2 (attack the negation first).  
**Scope:** new consequences of the exact erasure identity and the restriction-critical-descendant lemma. No novelty claim is made; publication priority is **UNVERIFIED**.

## 1. State consumed and exact live obstruction

I continued from the fresh P03 state on `master`, including the 21 September read-once package, the exact erasure reduction, the recombination-vs-allocation theorem, and the compatible account02/B14 restriction-critical-descendant report (blob `95ae302edfd4be5f47e5ab4677a068d1be57926e`). I did not re-audit their certificates.

For a Boolean function `g:{-1,1}^n->{-1,1}`, write `a_S=\widehat g(S)`, `p_S=a_S^2`,

\[
H(g)=\sum_S p_S\log_2(1/p_S),\qquad I(g)=\sum_S |S|p_S.
\]

For a relevant physical coordinate `i`, put

\[
\alpha_i=\operatorname{Inf}_i(g)=\sum_{T\not\ni i} a_{T\cup\{i\}}^2,
\]

and let `g_+,g_-` be the two restrictions. The recovered exact identity is

\[
\Delta_iH(g)=B_i(g)+JS_i(g),
\tag{1}
\]

where `B_i=H(X_i\mid X_{-i})` for the spectral sample `X`, while the recovered universal bounds give

\[
JS_i\le B_i,
\qquad
JS_i\le c\min\{\alpha_i,1-\alpha_i\},
\qquad c=\frac2{\ln2}.
\tag{2}
\]

The account02/B14 restriction-critical lemma says that for every nonconstant `f` there is a physical restriction descendant `g` maximizing `r=H/I` among its nonconstant descendants and satisfying, for every relevant `i`,

\[
\Delta_iH(g)\ge r(g)\alpha_i.
\tag{3}
\]

Consequently, when `r(g)>4/\ln2`, (1)--(3) imply

\[
\boxed{B_i(g)\ge \left(r(g)-\frac2{\ln2}\right)\alpha_i\quad\text{for every relevant }i.}
\tag{4}
\]

This report asks what (4) forces at the level of the **signed paired Fourier coefficients**, rather than trying the already-refuted arbitrary-coordinate upper-payment statement.

## 2. New scalar inequality: binary erasure entropy is bounded by Hellinger overlap

### Lemma 2.1
For every `t in [0,1]`,

\[
\boxed{h_2(t)\le 2\sqrt{t(1-t)}.}
\tag{5}
\]

Equality holds only at `t in {0,1/2,1}`.

### Proof
By symmetry write `t=(1-x)/2` with `x in [0,1]`, and define

\[
F(x)=\sqrt{1-x^2}-h_2\!\left(\frac{1-x}{2}\right).
\]

Then `F(0)=F(1)=0` and, on `(0,1)`,

\[
F'(x)=\frac{\operatorname{atanh}x}{\ln2}-\frac{x}{\sqrt{1-x^2}},
\]

\[
F''(x)=\frac{\sqrt{1-x^2}-\ln2}{\ln2\,(1-x^2)^{3/2}}.
\]

Thus `F''` is positive up to the unique point `sqrt(1-x^2)=ln2` and negative afterwards. Since `F'(0)=0`, `F'` first increases, then strictly decreases to `-infinity`, so it has exactly one zero in `(0,1)`. Therefore `F` first increases and then decreases to its endpoint value `F(1)=0`, hence `F>=0`. Equality is only at the two endpoints in `x`, which gives `t=1/2` and `t in {0,1}`. QED.

## 3. New child-spectrum separation bound

Fix a coordinate `i` and write, for residual labels `T` not containing `i`,

\[
u_T=a_T,\qquad v_T=a_{T\cup\{i\}}.
\]

The two child spectral laws are

\[
q_+(T)=(u_T+v_T)^2,\qquad q_-(T)=(u_T-v_T)^2.
\]

Their total-variation distance is exactly

\[
\operatorname{TV}(q_+,q_-)
=\frac12\sum_T\left|(u_T+v_T)^2-(u_T-v_T)^2\right|
=2\sum_T|u_Tv_T|.
\tag{6}
\]

On the same fibre, if `m_T=u_T^2+v_T^2` and `t_T=v_T^2/m_T` (with the zero fibre omitted), the erasure contribution is

\[
m_T h_2(t_T).
\]

Lemma 2.1 gives

\[
m_T h_2(t_T)\le 2m_T\sqrt{t_T(1-t_T)}=2|u_Tv_T|.
\]

Summing yields the exact universal inequality

\[
\boxed{B_i(g)\le \operatorname{TV}(q_+,q_-).}
\tag{7}
\]

This says that a coordinate with large spectral erasure entropy necessarily makes its two physical restrictions have well-separated Fourier-energy distributions. The direction is useful here because (4) lower-bounds `B_i` at every coordinate of a critical core.

### Corollary 3.1 — every coordinate of a critical core separates its children

Let `g` be a restriction-critical descendant with `r=r(g)>4/ln2`, and put

\[
b(r)=r-\frac2{\ln2}.
\]

Then every relevant coordinate satisfies

\[
\boxed{\operatorname{TV}(q_+,q_-)\ge b(r)\alpha_i.}
\tag{8}
\]

For a hypothetical counterexample above the Hod-scale value `C=6.4547837`, this forces, on the same descendant,

\[
b(C)=3.5693936182\ldots,
\qquad
\operatorname{TV}(q_+,q_-)>3.5693936182\,\alpha_i
\tag{9}
\]

for every relevant `i`.

## 4. Booleanity forces the overlap to be two-sided in sign

The magnitude statement (8) becomes more rigid when the signed Boolean convolution constraints are restored.

For every nonempty `U`, Booleanity `g^2=1` gives

\[
\sum_S a_Sa_{S\triangle U}=0.
\tag{10}
\]

Taking `U={i}` and pairing the two copies of each `i`-edge gives

\[
\boxed{\sum_Tu_Tv_T=0.}
\tag{11}
\]

Define the **upper spectral law** for coordinate `i` by

\[
\mu_i(T)=\frac{v_T^2}{\alpha_i},
\]

and on its support define the signed ratio

\[
Z_i(T)=\frac{u_T}{v_T}.
\]

Then (11) and (6) give the exact identities

\[
\mathbb E_{\mu_i}Z_i=0,
\qquad
\mathbb E_{\mu_i}|Z_i|
=\frac{\operatorname{TV}(q_+,q_-)}{2\alpha_i}.
\tag{12}
\]

Combining with (8):

\[
\boxed{\mathbb E|Z_i|\ge \frac{b(r)}2,\qquad
\mathbb E(Z_i)_+=\mathbb E(Z_i)_-\ge\frac{b(r)}4.}
\tag{13}
\]

So a critical core cannot pay its erasure entropy with overlap of only one relative Fourier phase: **each relevant coordinate must carry quantitatively large positive and negative signed Fourier overlap simultaneously.**

At `C=6.4547837`, a putative counterexample core would satisfy

\[
\mathbb E|Z_i|>1.7846968091,
\qquad
\mathbb E(Z_i)_+ = \mathbb E(Z_i)_->0.8923484046
\tag{14}
\]

for every relevant coordinate.

## 5. A second forced statistic: present-bit logarithmic surprise

Split the exact erasure entropy into its two oriented logarithmic terms:

\[
B_i=L_i+U_i,
\]

\[
L_i=\sum_Tv_T^2\log_2\left(1+\frac{u_T^2}{v_T^2}\right),
\qquad
U_i=\sum_Tu_T^2\log_2\left(1+\frac{v_T^2}{u_T^2}\right),
\tag{15}
\]

with the usual continuous boundary convention. Since `log_2(1+x)<=x/ln2`,

\[
U_i\le\frac{1}{\ln2}\sum_Tv_T^2=\frac{\alpha_i}{\ln2}.
\tag{16}
\]

Therefore (4) forces

\[
L_i\ge\left(r-\frac3{\ln2}\right)\alpha_i.
\tag{17}
\]

Under the upper spectral law,

\[
\frac{L_i}{\alpha_i}
=\mathbb E_{\mu_i}\log_2(1+Z_i^2).
\]

Hence every coordinate of the critical core obeys

\[
\boxed{\mathbb E_{\mu_i}\log_2(1+Z_i^2)
\ge r-\frac3{\ln2}.}
\tag{18}
\]

Equivalently, if

\[
q_i(T)=\Pr[X_i=1\mid X_{-i}=T]=\frac1{1+Z_i(T)^2},
\]

then conditional on `X_i=1`,

\[
\boxed{\mathbb E[-\log_2 q_i(X_{-i})]\ge r-\frac3{\ln2}.}
\tag{19}
\]

At the Hod scale,

\[
r-\frac3{\ln2}=2.1266985773\ldots,
\]

so the geometric mean posterior inclusion probability is at most

\[
2^{-2.1266985773\ldots}=0.2289812577\ldots.
\tag{20}
\]

Thus the same critical coordinate is simultaneously hard to erase, creates separated child spectra, has balanced positive/negative signed overlap, and—when the spectral bit is actually present—looks unexpectedly unlikely from the residual spectral set.

## 6. All-shift orthogonality is the genuinely Boolean constraint still unused

Equation (11) is only the `U=emptyset` member of a much stronger system. For every residual subset `U` not containing `i`, apply (10) to `U union {i}`. Splitting the sum by whether `i` is present gives

\[
\boxed{\sum_Tu_Tv_{T\triangle U}=0\qquad\text{for every residual }U.}
\tag{21}
\]

So `u` is orthogonal to **every translate** of `v` on the residual Fourier cube.

In physical language this is transparent. Define

\[
A_i(x)=\frac{g_+(x)+g_-(x)}2,
\qquad
D_i(x)=\frac{g_+(x)-g_-(x)}2.
\]

Their Fourier transforms are `u` and `v`, and because `g_+,g_-` are `+-1`-valued,

\[
A_i(x)D_i(x)=0,
\qquad
A_i(x)^2+D_i(x)^2=1
\tag{22}
\]

pointwise. Thus the new critical-core constraints can be restated as follows:

> for every relevant physical coordinate, two complementary-support signed functions `A_i,D_i` have Fourier transforms whose absolute coordinatewise overlap is large, whose signed overlap cancels under every translation, and whose upper/lower coefficient ratios have large logarithmic surprise.

This is a more rigid target than a generic moment problem for one random ratio.

## 7. Dead route found: the one-coordinate moment relaxation is too weak

To test whether (13) and (18) alone could close the argument, discard the full system (21) and retain only the scalar constraints

\[
\mathbb EZ=0,
\quad
\mathbb E|Z|\ge b/2,
\quad
\mathbb E\log_2(1+Z^2)\ge d.
\tag{23}
\]

At the Hod scale, `b/2=1.7846968091...` and `d=2.1266985773...`. The symmetric two-point law

\[
Z=\pm z\quad\text{with probability }1/2,
\qquad
z=\sqrt{2^d-1}=1.8349849192\ldots
\tag{24}
\]

satisfies all three conditions. It also satisfies the elementary second-moment allowance

\[
\mathbb EZ^2\le\frac{1-\alpha_i}{\alpha_i}
\]

throughout the already-known Hod-scale critical range `alpha_i<0.180554`, since `z^2≈3.367` while `(1-alpha)/alpha>4.53` at that endpoint.

Therefore **mean-zero sign balance plus one-coordinate moments cannot prove FEI**. The next attack must use the all-translate identities (21), or compatibility of these identities simultaneously across many physical coordinates. This is the concrete failure produced by move #2.

## 8. Global corollary: a counterexample core has bounded dual total correlation

Let

\[
B(g)=\sum_iB_i(g),
\qquad
\operatorname{DTC}(X)=H(X)-\sum_iH(X_i\mid X_{-i})=H(g)-B(g).
\]

Summing (4) over relevant coordinates gives

\[
B(g)\ge\left(r-\frac2{\ln2}\right)I(g)=H(g)-\frac2{\ln2}I(g).
\]

Hence every restriction-critical counterexample core with `r>4/ln2` satisfies

\[
\boxed{\operatorname{DTC}(X)\le\frac2{\ln2}I(g).}
\tag{25}
\]

At the Hod scale this says `DTC/H < 0.447016`. This does not close FEI, but it identifies another necessary shape: a high-entropy/high-ratio Boolean spectral law would have to retain most of its entropy as **erasure entropy**, rather than higher-order dual total correlation.

## 9. What moved and the next exact obligation

**Before:** the current selector route localized any FEI(C) counterexample to one restriction descendant with every coordinate locally critical and erasure-heavy, but the erasure lower bound was not yet translated into a signed Fourier-geometry condition.

**After:** on that same descendant, every relevant coordinate must satisfy all of the following simultaneously:

1. child spectral laws are separated by `TV(q_+,q_-) >= (r-2/ln2) alpha_i`;
2. the signed coefficient ratio has zero mean but absolute first moment at least `(r-2/ln2)/2`, forcing positive and negative first moments at least `(r-2/ln2)/4` each;
3. the present-bit surprise obeys `E log2(1+Z_i^2) >= r-3/ln2`;
4. the entire translated cross-correlation system `sum_T u_T v_{T triangle U}=0` holds for every residual shift `U`;
5. globally, the spectral dual total correlation is at most `(2/ln2)I`.

The scalar one-coordinate relaxation is explicitly insufficient. The **next exact obligation** is therefore a genuinely Boolean multi-shift statement: show that a Boolean function cannot satisfy the all-translate orthogonality (21), the low-influence/diffuse-profile conditions already recovered for the same critical core, and the quantitative overlap/surprise lower bounds above at every relevant coordinate. A useful candidate is a dimension-free inequality that upper-bounds, for at least one coordinate, `sum_T |u_Tv_T|` or the logarithmic surprise by a quantity paid by an original-coordinate influence budget **using more than the single shift U=emptyset**.

## 10. Literature scope

A bounded current primary-literature check found González--MacManus--Pereyra, arXiv:2606.00246 (2026), using restriction entropy decrements and stopping binary trees; Potapov, arXiv:2609.21563 (18 September 2026), proving FEI for plateaued and partially bent classes; and Han, arXiv:2312.08271, giving the known influence-plus-log-profile bound. I did not find the exact child-spectrum-TV / signed-overlap reduction above in that bounded search, but a search miss is not evidence of novelty. **Priority remains UNVERIFIED. Full FEI remains OPEN.**
