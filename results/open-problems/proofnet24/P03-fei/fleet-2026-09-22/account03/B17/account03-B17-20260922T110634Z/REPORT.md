# account03/B17 — degree-adaptive logarithmic compiler for balanced dependence KL

**Run:** `account03-B17-20260922T110634Z`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** balanced nonlocal KL closure, Path B  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEAR-LOSSLESS_LOG_COMPILER / EQUALITY_BRANCH_CLOSED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact target and correction status

For a balanced Boolean function
\[
f:\{-1,1\}^n\to\{-1,1\},
\]
let
\[
P(S)=\widehat f(S)^2\qquad(S\ne\varnothing),
\quad r_i=P(i\in S),
\quad \mu=\sum_i r_i=I(f).
\]
Let `Q_r` be the maximum-entropy nonempty occurrence I-projection with the same coordinate marginals. The source-exact identities are
\[
K_{\rm occ}(f)=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(f),
\]
and, at a finite center `C`,
\[
R_C(f)=K_{\rm occ}(f)+C[I(f)-1]-H_{\max}(r)
      =C[I(f)-1]-H(f).
\tag{0.1}
\]
Thus the balanced core inequality is
\[
K_{\rm occ}(f)\ge H_{\max}(r)-C[I(f)-1].
\tag{0.2}
\]
The current state correctly records that (0.2) for all balanced Boolean functions is equivalent to full FEI with the same constant. This report therefore does **not** claim that rewriting (0.2) is progress. The new mathematics is instead a source statistic that compresses the full atomwise KL with arbitrarily small loss measured in the **exact FEI denominator** `I-1`, together with an exact hierarchy ledger and a closed equality branch.

The retired fixed potentials, the old AND-extremality proposal, the 0.337/0.34 quadratic repairs, raw `U4`, unweighted convolution `L2`, and fixed/sub-half-depth labelled KL truncations are not used.

## 1. Source-pinned premises and partner result actually applied

### IPROJ

`yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04`,
`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

It proves the unique conditional-product I-projection `Q_r`, the formula `K_occ=Hmax-H`, and the exact residual (0.1).

### HIERARCHY

`yspennstate/math-open-problems@2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`,
`proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`.

For a disjoint Boolean composition `F=G(f_1,...,f_m)` it proves
\[
K_{\rm occ}(F)
=K_{\rm occ}(G)+\sum_i\alpha_iK_{\rm occ}(f_i)+C_{\rm hier},
\qquad C_{\rm hier}\ge0,
\tag{1.1}
\]
with `C_hier` an explicit KL mismatch. It must not be dropped.

### EQUALITY RIGIDITY

`yspennstate/math-open-problems@84c69136ca6b008badb76f15bf1071d029c927aa`,
`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T085625Z-product-equality-rigidity/REPORT.md`.

On the balanced uniform slice,
\[
K_{\rm occ}=0
\iff
f=\chi_F b(x_A),
\tag{1.2}
\]
where `F` is nonempty and `b` is bent on an even set `A`. If `m=|A|`, then
\[
H(f)=m,
\qquad I(f)=|F|+m/2.
\tag{1.3}
\]

### PARTNER account04/B17 — exact suspension transport

The latest compatible completed partner result read for this run is
`yspennstate/math-open-problems@374c4874e914c7414abc9109fadf77cfc3947298`,
`proofnet24/P03-fei/fleet-2026-09-22/account04/B17/20260922T102740Z-b17-fei-r17/REPORT.md`.

For the balanced character suspension
\[
F(y,x)=y\,g(x),
\tag{1.4}
\]
it proves that the **entire** squared spectral law of `g`, including the old constant Fourier atom, becomes the nonempty spectral law of `F`, with
\[
K_{\rm susp}=\sum_i h_2(q_i)-H(g),
\qquad I(F)-1=I(g),
\tag{1.5}
\]
and gives an exact nonnegative decomposition of `K_susp` into constant-mode branch KL, anchored dependence KL, and reference-mismatch KL. I apply (1.4)-(1.5) in Section 4 below rather than merely citing the report.

### MULTISCALE PREFLIGHT

`yspennstate/math-open-problems@bff0d7b6c21485f386841c42582eb04f32705046`,
`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`,
refutes fixed/sub-half-depth labelled KL truncations on recursive ternary majority. A compatible later physical-tree theorem,
`proofnet24/P03-fei/fleet-2026-09-22/account01/B09/account01-B09-20260922T104421Z-fei/REPORT.md`,
proves the all-scale lower bound used in Section 5.

## 2. Main theorem: degree-adaptive log-likelihood compiler

The fixed-width logarithmic binning idea has a two-bit-per-tail-atom conditional-KL loss. The key change here is to make the log resolution proportional to the exact atomwise contribution to `I-1`.

Fix any `epsilon>0`. For a nonempty spectral label `S`, put
\[
d(S)=|S|-1.
\]
Define a deterministic statistic `Z_epsilon` as follows.

1. If `|S|=1`, retain `S` itself as a singleton label.
2. If `|S|>=2` and `P(S)=0`, use a dedicated zero-source label (refined by degree if desired).
3. If `|S|=k>=2` and `P(S)>0`, put
\[
w_k={\epsilon\over2}(k-1),
\tag{2.1}
\]
and record
\[
Z_\epsilon(S)=
\left(
 k,
 \operatorname{sgn}\widehat f(S),
 \left\lfloor{-\log_2P(S)\over w_k}\right\rfloor,
 \left\lfloor{-\log_2Q_r(S)\over w_k}\right\rfloor
\right).
\tag{2.2}
\]
(If a Fourier coefficient is zero, its sign is not used because it is already in the zero-source branch.) Define the retained logarithmic credit
\[
K_\epsilon(f)
:=D_{\rm KL,2}\bigl((Z_\epsilon)_\#P\Vert(Z_\epsilon)_\#Q_r\bigr).
\tag{2.3}
\]

### Theorem 2.1 — `B17-DEGREE-ADAPTIVE-LOG-COMPILER-v1`

For every balanced Boolean function, every dimension, and every `epsilon>0`,
\[
\boxed{
0\le K_{\rm occ}(f)-K_\epsilon(f)
\le \epsilon\,[I(f)-1].
}
\tag{2.4}
\]

#### Proof

Data processing gives `K_epsilon<=K_occ`. Apply the KL chain rule over the fibres of `Z_epsilon`:
\[
K_{\rm occ}-K_\epsilon
=\sum_zP_Z(z)
D_2\bigl(P(\cdot\mid z)\Vert Q_r(\cdot\mid z)\bigr).
\tag{2.5}
\]
Singleton fibres contribute zero. Fibres of zero `P`-mass contribute zero.

Consider a remaining fibre at fixed degree `k>=2`. The two floor bins in (2.2) imply that across this fibre each of `P(S)` and `Q_r(S)` varies by a factor strictly smaller than `2^{w_k}`. Hence the likelihood ratio
\[
L(S)={P(S)\over Q_r(S)}
\]
varies across the fibre by a factor strictly smaller than
\[
2^{2w_k}=2^{\epsilon(k-1)}.
\tag{2.6}
\]
The fibre average `P_Z(z)/Q_Z(z)` is a `Q_r(\cdot|z)`-weighted average of `L`, so it lies between the minimum and maximum likelihood ratios in that fibre. Therefore, pointwise on the fibre,
\[
{P(S\mid z)\over Q_r(S\mid z)}
={L(S)\over P_Z(z)/Q_Z(z)}
<2^{\epsilon(k-1)}.
\]
Consequently
\[
D_2(P(\cdot|z)\Vert Q_r(\cdot|z))
\le\epsilon(k-1).
\tag{2.7}
\]
Substituting (2.7) in (2.5) and summing gives
\[
K_{\rm occ}-K_\epsilon
\le\epsilon\sum_S P(S)(|S|-1)
=\epsilon(\mu-1)
=\epsilon[I(f)-1].
\]
This proves (2.4). `QED`.

### Why this is not just FEI renamed

`K_epsilon` is a concrete deterministic coarse statistic: it forgets exact coordinate labels inside each non-singleton log cell and retains only degree, source sign, and two finite-resolution log-price bins. The theorem proves a quantitative compression statement that is independent of FEI.

It does **not** prove (0.2). Indeed:

* If one could prove
  \[
  K_\epsilon(f)\ge H_{\max}(r)-C[I(f)-1]
  \tag{2.8}
  \]
  for all balanced Boolean `f`, then FEI at constant `C` follows immediately because `K_occ>=K_epsilon`.
* Conversely, FEI at constant `C` implies only
  \[
  K_\epsilon(f)\ge H_{\max}(r)-(C+\epsilon)[I(f)-1]
  \tag{2.9}
  \]
  by (2.4).

Thus the compiler preserves the universal problem to an arbitrarily small additive loss in the constant, while the **new theorem is the compression estimate (2.4), not the still-open payment (2.8).**

## 3. Exact equality branch is closed at `C=2`

Apply the source-pinned equality rigidity (1.2)-(1.3). If `K_occ(f)=0`, then automatically `K_epsilon(f)=0`, and
\[
2[I(f)-1]-H(f)
=2\left(|F|+{m\over2}-1\right)-m
=2(|F|-1)\ge0.
\tag{3.1}
\]
Therefore:

\[
\boxed{
K_{\rm occ}=0\quad\Longrightarrow\quad
H(f)\le2[I(f)-1].
}
\tag{3.2}
\]

This closes the **exact product-equality branch** of the balanced core inequality with the finite constant `C=2`. Any putative difficult balanced source at a larger FEI scale must have strictly positive dependence KL. The theorem does not yet give a dimension-free quantitative gap away from the character-times-bent family; that is part of the remaining nonzero branch.

## 4. Applying the partner suspension theorem: constant-mode exactness and rare-event logarithms

Take the partner's balanced suspension `F(y,x)=y g(x)`. Every nonzero spectral label of `F` is of the form
\[
\{y\}\cup T,
\]
where `T` is a spectral label of `g`. Hence
\[
|\{y\}\cup T|-1=|T|.
\tag{4.1}
\]
The old constant Fourier atom `T=emptyset` becomes the singleton `{y}`. By construction `Z_epsilon` retains this atom **exactly**, so the partner's constant-mode branch is not merged into a tail cell.

Using (1.5) and Theorem 2.1 gives the exact application
\[
\boxed{
0\le K_{\rm susp}-K_\epsilon(F)
\le\epsilon I(g).
}
\tag{4.2}
\]
This is an arbitrary-`epsilon` strengthening, on the full suspension face, of a fixed-width compiler whose discarded KL is only known to be `O(I(g))` with a fixed constant.

For the genuine sparse one-point-defect suspension used in the current no-loss barrier, the source asymptotic is
\[
{K_{\rm susp}\over I(g_m)}
=m-5+{1\over\ln2}+o(1).
\tag{4.3}
\]
Therefore (4.2) implies
\[
{K_\epsilon(F_m)\over I(g_m)}
\ge m-5+{1\over\ln2}-\epsilon+o(1).
\tag{4.4}
\]
The rare-event logarithm survives with asymptotically zero **relative** loss. This directly avoids the retired unweighted-`L2` mechanism, whose loss of the logarithm is the relevant obstruction.

## 5. Mandatory recursive-majority preflight

Let `M_m` be depth-`m` recursive ternary majority. The current source gives
\[
I(M_m)=\left({3\over2}\right)^m
\tag{5.1}
\]
and the physical KL-tree theorem gives
\[
K_{\rm occ}(M_m)
\ge
\left({3\over2}\right)^{m-1}
\left({m\over2}+\log_2{7\over16}\right).
\tag{5.2}
\]
Combining (2.4), (5.1), and (5.2),
\[
\boxed{
K_\epsilon(M_m)
\ge
\left({3\over2}\right)^{m-1}
\left({m\over2}+\log_2{7\over16}\right)
-\epsilon\left[\left({3\over2}\right)^m-1\right].
}
\tag{5.3}
\]
For every fixed `epsilon`, the right side is `Omega(m(3/2)^m)`. Thus this statistic does **not** collapse under the fixed/sub-half-depth recursive-majority barrier. The reason is structural: it is not a low-level atom list followed by one merged tail; it prices every occupied atom through its source and reference log scales with degree-dependent resolution.

## 6. Hierarchy transfer with an exactly payable residual

Now suppose
\[
F=G(f_1,\ldots,f_m)
\]
is a disjoint composition in which the outer gate `G` and every displayed child `f_i` are balanced under their uniform inputs. Put
\[
\alpha_i=\operatorname{Inf}_i(G).
\]
Then the exact source hierarchy gives (1.1), and the balanced influence composition identities give
\[
I(F)=\sum_i\alpha_i I(f_i),
\qquad
I(G)=\sum_i\alpha_i.
\tag{6.1}
\]
Define the **tree-compiled credit**
\[
K_\epsilon^{\rm tree}(F)
:=K_\epsilon(G)
 +\sum_i\alpha_iK_\epsilon(f_i)
 +C_{\rm hier}.
\tag{6.2}
\]
The hierarchy mismatch is retained in full; it is not reprojected away.

### Theorem 6.1 — `B17-HIERARCHY-SAFE-LOG-COMPILER-v1`

For every such balanced disjoint composition,
\[
\boxed{
0\le K_{\rm occ}(F)-K_\epsilon^{\rm tree}(F)
\le\epsilon[I(F)-1].
}
\tag{6.3}
\]

#### Proof

Subtract (6.2) from (1.1). The hierarchy credit cancels exactly:
\[
K_{\rm occ}(F)-K_\epsilon^{\rm tree}(F)
=
[K_{\rm occ}(G)-K_\epsilon(G)]
+\sum_i\alpha_i[K_{\rm occ}(f_i)-K_\epsilon(f_i)].
\]
Apply (2.4) to each local balanced source:
\[
\le\epsilon\left[(I(G)-1)+\sum_i\alpha_i(I(f_i)-1)\right].
\]
Using (6.1), the bracket equals exactly
\[
I(F)-1.
\]
This proves (6.3). `QED`.

Iterating Theorem 6.1 down an arbitrary finite balanced disjoint composition tree gives the same global bound `epsilon[I(F)-1]`; each local compression loss is paid by its own exact excess-degree currency and every hierarchy KL mismatch is retained. There is no double spending.

This is the requested precise branch ledger:

* **zero-dependence branch:** closed by Section 3 at `C=2`;
* **nonzero logarithmic branch:** compression loss is at most `epsilon(I-1)`;
* **disjoint hierarchy branch:** all mismatch KL is preserved exactly and the local loss budgets telescope to the same `epsilon(I-1)`;
* **rare-event / multiscale stress branches:** Sections 4-5 retain their logarithmic growth.

## 7. What is newly proved, and what remains unpaid

### New mathematics proved here

1. `B17-DEGREE-ADAPTIVE-LOG-COMPILER-v1`, equation (2.4): a concrete nonlocal logarithmic statistic retains the canonical dependence KL up to **arbitrarily small** `epsilon[I-1]` loss in every dimension.
2. The exact `K_occ=0` balanced branch is closed at `C=2` using the source-pinned equality rigidity.
3. `B17-HIERARCHY-SAFE-LOG-COMPILER-v1`, equation (6.3): the compiler is compatible with exact disjoint hierarchy transfer while retaining the entire hierarchy KL, and the discarded credit is again at most `epsilon[I-1]` globally.
4. The partner's suspension constant mode is retained exactly, sparse rare-event logarithms lose at most `epsilon I`, and recursive majority remains `Omega(m(3/2)^m)` under the compiler.

### Still open

The hard nonzero, composition-prime branch remains:
\[
K_\epsilon(f)
\stackrel{?}{\ge}
H_{\max}(r)-C[I(f)-1]
\tag{7.1}
\]
for one finite `C` (and one chosen `epsilon>0`) uniformly over all balanced Boolean `f`. Equation (7.1) is not proved here. By the admission theorem, proving it would essentially close FEI; merely naming it is not a result.

The useful next step is now narrower and source-explicit: exploit signed Boolean convolution / Walsh-lattice rigidity **inside one log-price cell or a controlled family of cells** to force a payable divergence whenever the compiled source approaches the dangerous I-projection envelope. Because the compiler has already bounded all information lost outside that statistic by `epsilon(I-1)`, such a cell-rigidity theorem would no longer need to recover an unbounded rare-event logarithm from an unweighted quadratic surrogate.

Primary recipient: `account01/B01` (credit-augmented Bellman supersolution). Partner feedback target: `account04/B17` (cross-path deficit transport).

## 8. Scope and integrity

No finite sweep is used as a universal proof. No old fixed potential or refuted intermediate lemma is revived. The new compiler theorems are analytic finite-probability identities/inequalities. Full FEI remains open. Repository synchronization is not native-memory ingestion; this run is `WITHOUT_VERIFIED_BRAIN`.
