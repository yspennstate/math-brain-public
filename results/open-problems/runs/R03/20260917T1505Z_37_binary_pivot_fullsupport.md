Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the accessible runtime exposes no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the fixed full-range numerical envelope: `r(10)=222.6104736743168493957921796888577...` remains exact and `r(11)<=523.4894710902614257202829985613411...` remains the strongest replay-certified bound; unchanged count `1 -> 2`. Methods used: #1 CHANGE THE CATEGORY, #25 COUNT THE SAME THING TWICE, #20 FIND WHY THE ALGORITHM FAILS.**

# R03 run37 — binary pivot pairs, asymptotically full null support, and a determinant-pencil obstruction

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source OPEN.** The frozen finite envelope does not move. The substantive progress is a source-scale sharpening of C285/C294 plus an exact binary-matrix representation of the surviving affine-excess count. No source-closure claim is made.

All thirty Section-B moves were already used somewhere in R03 by run34, so there is no literally unused numbered move left without falsely resetting history. I reuse #1/#25/#20 in new roles. This triple differs from run36's #27/#14/#5.

## 1. Continuity, controls, source match and frozen metric

Before new mathematics I recovered/read the required campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, targeted F0001 intake/history, newest own report `runs/R03/20260917T1405Z_36_basis_encoding_neardistinct.md`, and current neighboring R02/R04 states. R02 is on an unrelated outside target and R04 has retired repeated I0027 research; neither is a competing F0001 owner. The connector does not render all roughly 780 intake JSONL rows byte-for-byte in one response, so the intake check was exact/source-targeted rather than falsely described as a literal full visual dump.

The outside source remains intake `F0001`, Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 2.2:

\[
p_n=(2+o(1))n^2 2^{-n}
\]

for an iid uniform Rademacher `n x n` matrix. Thus the retained source-matched form remains

\[
\boxed{\Pr(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}.}
\tag{1.1}
\]

Let `T_n` be the exact equal/opposite signed row-pair and column-pair union. Retained C225 pays its overlaps. The fixed remainder is

\[
\boxed{r(n)=2^n\Pr(\det B_n=0,T_n^c),}
\tag{1.2}
\]

and source closure remains equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

Fresh primary-literature checking on 2026-09-17 still leaves (1.1) unresolved. Jain--Sah--Sawhney, arXiv:2010.06554 / GAFA 2021, prove the sharp elementary-mechanism asymptotic for finite-support laws that are **not uniform on their support**; for uniform support, including iid Rademacher, they give exponential-scale precision for total singularity and sharp compressible-sector control, not the sharp polynomial prefactor. Song--Wang, arXiv:2607.00495, determine a growing-corank Bernoulli regime. Hunter--Kwan--Sauermann--Sawhney, IMRN 2026, rnag126, prove `P(corank >= k) <= exp(-c n k)`. Neither supplies the missing `k=1` prefactor. Voigt--Ziegler (CPC 2006, arXiv:math/0308050) is explicit prior art for the random cube-hyperplane equivalence, so no novelty claim is made for that broad viewpoint. The dated search record is `artifacts/R03/20260917T1505Z_37_source_status.md`.

Pre-run and post-run finite envelope:

\[
r(10)=222.6104736743168493957921796888577\ldots
\]

exactly, and

\[
\boxed{
r(11)\le
\frac{32615069759481592686393385491735}{62303201039659529147657486336}
=523.4894710902614257202829985613411\ldots .
}
\tag{1.4}
\]

All retained branches for `n>=12` remain available.

## 2. Retained C285/C294 state

Put `d=n-1`. For a uniformly random invertible sign matrix

\[
R\in\{\pm1\}^{d\times d},
\]

write

\[
w_R=R^{-1}{\bf1},\qquad
C_R=\{x\in\{\pm1\}^d:x^Tw_R=1\},\qquad
M_R=|C_R|.
\tag{2.1}
\]

The rows of `R` are `d` forced points of `C_R`. Retained C285 defines, after deleting the exact signed-unit column-collision charts,

\[
E_d^\circ:=
\mathbb E_R\!\left[(M_R-d)\mathbf1_{\{w_R\notin\{\pm e_j\}\}}\right],
\tag{2.2}
\]

where deleting/adding the retained JSS-structured filter changes the source-normalized quantity by only `o(1)`. If

\[
p_d^{\rm inv}=\Pr(R\text{ invertible}),
\]

C285 gives the exact Schur normalization and the constant-factor source comparison.

Run36/C294 proved the much stronger coefficient-complexity localization: for every fixed dense-support parameter `delta>0` and every sequence `s_d` with

\[
\frac{s_d\log d}{d}\to\infty,
\]

\[
\mathbb E_R\!\left[(M_R-d)_+
\mathbf1_{\{|\operatorname{supp}w_R|\ge\delta d\}}
\mathbf1_{\{\kappa(w_R)\le d-s_d\}}\right]=o(1),
\tag{2.3}
\]

where `kappa(w)` is the number of distinct nonzero absolute coefficient magnitudes. The proof uses actual basis rows to determine the magnitude parameters and Sárközy--Szemerédi only on the remaining rows.

This run uses (2.3) twice, once on the right null direction and once after transposition.

## 3. Method #1 — CHANGE THE CATEGORY: from affine sections to a paired binary determinant problem

Fix an invertible sign matrix `R` and a sign vector `x`. Put

\[
D_x=\operatorname{diag}(x),\qquad
S=RD_x,\qquad
B=\frac{J-S}{2}\in\{0,1\}^{d\times d}.
\tag{3.1}
\]

Because `S^{-1}=D_xR^{-1}`,

\[
\mathbf1^TS^{-1}\mathbf1=x^TR^{-1}\mathbf1=x^Tw_R.
\tag{3.2}
\]

The matrix determinant lemma gives

\[
\det(S-J)=\det S\left(1-\mathbf1^TS^{-1}\mathbf1\right).
\]

Since `S-J=-2B`,

\[
\boxed{
x\in C_R
\iff x^Tw_R=1
\iff \det B=0.
}
\tag{3.3}
\]

Thus every extra affine cube point can be viewed as a singular binary matrix obtained by pivoting an invertible sign matrix.

The two trivial mechanisms become literal zero rows and zero columns:

- `x` is one of the rows of `R` iff the corresponding row of `B` is zero;
- on the event `det B=0` with `S` invertible, `w_R=\pm e_j` iff column `j` of `B` is zero.

For the second assertion, `det B=0` and `S` invertible imply `1^TS^{-1}1=1`. Since `w_R=D_xS^{-1}1`, a signed-unit `w_R` therefore forces `S^{-1}1=e_j`, equivalently `Se_j=1`, equivalently a zero column of `B`; the converse is immediate.

This is an exact category change, not an asymptotic analogy.

## 4. Method #25 — COUNT THE SAME THING TWICE: exact binary-pivot identity

Define

\[
\mathcal N_d^\circ=
\left\{B\in\{0,1\}^{d\times d}:
\begin{array}{l}
\det B=0,\\
\det(J-2B)\ne0,\\
B\text{ has no zero row and no zero column}
\end{array}
\right\}
\tag{4.1}
\]

and let

\[
N_d^\circ=|\mathcal N_d^\circ|,
\qquad
I_d=\#\{R\in\{\pm1\}^{d\times d}:\det R\ne0\}.
\]

### R03-C296 — exact binary-pivot count

**STATUS: PROVED.**

\[
\boxed{
I_d E_d^\circ=2^d N_d^\circ.
}
\tag{C296.1}
\]

**Proof.** Count pairs

\[
(R,x),\qquad R\text{ invertible sign},\quad
x\in C_R\setminus\{\text{rows of }R\},\quad
w_R\notin\{\pm e_j\}.
\]

The left-hand count is exactly `I_d E_d^circ`.

Map a pair to `B=(J-RD_x)/2`. By (3.3), `B` is singular. Since `RD_x=J-2B` is invertible, and the row/column exclusions are exactly the no-zero-row/no-zero-column conditions above, the image lies in `N_d^circ`.

Conversely, fix `B in N_d^circ` and let `S=J-2B`. For every `x in {+-1}^d`, set

\[
R=SD_x.
\]

Then `R` is invertible. Because `det B=0`, (3.2)--(3.3) give `x in C_R`; the zero-row/zero-column exclusions guarantee that `x` is not a basis row and `w_R` is not a signed unit. Distinct `x` give distinct pairs. Hence every admissible binary matrix has exactly `2^d` preimages. QED.

The exact checker exhausts all cases through `d=4` and obtains

\[
\begin{array}{c|c|c|c}
d&I_d&N_d^\circ&\sum_R(M_R-d)\mathbf1_{\rm nontriv}\\ \hline
2&8&0&0\\
3&192&0&0\\
4&22272&1152&18432,
\end{array}
\]

with `18432=2^4*1152`, reproducing the retained run31 affine-excess value independently through the new binary classification. The archived output ends `SELF-CHECK PASS`.

## 5. A stronger algebraic characterization: the determinant pencil has a simple root

The new class has an intrinsic description not mentioning `R` or `x`.

If `B in N_d^circ`, then

\[
\operatorname{rank}B=d-1.
\tag{5.1}
\]

Indeed `rank(J-2B)<=rank(B)+1`; invertibility of `J-2B` forces `rank(B)>=d-1`, while `det B=0` gives equality.

Let `u` and `v` be nonzero left and right null vectors of this corank-one `B`. Then

\[
\operatorname{adj}(B)=\gamma vu^T
\]

for some nonzero scalar `gamma`. Since a rank-one determinant update is linear in its parameter,

\[
\det(B+tJ)
=t\,\mathbf1^T\operatorname{adj}(B)\mathbf1
=t\gamma(\mathbf1^Tv)(u^T\mathbf1).
\tag{5.2}
\]

Consequently

\[
\boxed{
\det(J-2B)\ne0
\iff
\operatorname{corank}B=1,
\quad \mathbf1^Tv\ne0,
\quad u^T\mathbf1\ne0.
}
\tag{5.3}
\]

Equivalently, `t=0` is a **simple root** of the determinant pencil `det(B+tJ)`. In particular, `J-2B` invertible automatically forbids equal or complementary row pairs and equal or complementary column pairs, because those would give equal or opposite rows/columns in `J-2B`.

Also, from `Bv=0`,

\[
(J-2B)v=(\mathbf1^Tv)\mathbf1,
\]

so whenever `J-2B` is invertible,

\[
(J-2B)^{-1}\mathbf1=\frac{v}{\mathbf1^Tv}.
\tag{5.4}
\]

Thus the absolute coefficient multiplicities in C294 are **exactly** the absolute-magnitude multiplicities of the binary right null vector. The transposed identity gives the same statement for the left null vector.

## 6. R03-C295 — the source-relevant corank-one sector has asymptotically full null support

This is the main source-scale strengthening of the run.

Choose, for example,

\[
s_d=\frac d{\sqrt{\log d}}.
\tag{6.1}
\]

Then `s_d log d/d -> infinity` while `s_d/d ->0`.

Work inside the retained collision-free, real-corank-one, JSS-unstructured sector `R_n^{UU}` from C280. Its left and right null supports satisfy a fixed lower bound `delta n`. Suppose the right null support is at most `n-s_d`. For **every** invertible-minor chart used in the exact cofactor count, deleting a nonzero distinguished coordinate leaves a vector `w` with

\[
|\operatorname{supp}w|\le d-s_d,
\qquad
\kappa(w)\le d-s_d.
\]

Hence C294 pays the entire cofactor-weighted contribution of this sector by `o(1)` after the R03 normalization. C280 then converts weighted to unweighted count with the fixed factor `delta^{-2}`, so

\[
2^n\Pr(\mathcal R_n^{UU},\ s_R\le n-s_d)=o(1).
\tag{6.2}
\]

Apply the same argument to the transpose:

\[
2^n\Pr(\mathcal R_n^{UU},\ s_L\le n-s_d)=o(1).
\tag{6.3}
\]

Therefore, outside a source-normalized `o(1)` set,

\[
s_L,s_R\ge n-s_d=n(1-o(1)).
\tag{6.4}
\]

### R03-C295 — sharp cofactor-weight reduction

**STATUS: PROVED from retained C280/C285/C294 and transposition.**

Let

\[
E_d^\circ=\mathbb E_R[(M_R-d)\mathbf1_{\{w_R\notin\{\pm e_j\}\}}].
\]

Then

\[
\boxed{
r(n)=(2+o(1))p_{n-1}^{\rm inv}E_{n-1}^\circ+o(1).
}
\tag{C295.1}
\]

**Proof.** For a rank-`n-1` matrix the exact cofactor weight is `s_Ls_R/n^2`. Let

\[
W_n=2^{n-1}q_n^{UU}.
\]

The exact C280 cofactor identity says `W_n` is the source-normalized residual count weighted by `s_Ls_R/n^2`. The bad-support sector (6.2)--(6.3) contributes `o(1)` to both the weighted and unweighted quantities. On the complement,

\[
\frac{s_Ls_R}{n^2}\ge\left(1-\frac{s_d}{n}\right)^2=1-o(1).
\]

Hence

\[
r(n)=(1+o(1))W_n+o(1).
\tag{6.5}
\]

Retained C285 gives

\[
W_n=2p_d^{\rm inv}E_d^\circ+o(1),
\qquad d=n-1,
\]

where removing the remaining JSS-structured indicator costs only `o(1)`. Substitution proves (C295.1). QED.

This improves C285's fixed `delta^{-2}` comparison to an asymptotically sharp cofactor weight. It still does **not** prove `E_d^circ=o(d^2)`.

## 7. Combining C295 and C296: one exact binary count is asymptotically source-equivalent

Since

\[
p_d^{\rm inv}=I_d/2^{d^2},
\]

C296 gives the exact identity

\[
2p_d^{\rm inv}E_d^\circ
=2^{d+1-d^2}N_d^\circ.
\tag{7.1}
\]

Therefore C295 yields

\[
\boxed{
r(d+1)
=(1+o(1))\,2^{d+1-d^2}N_d^\circ+o(1).
}
\tag{C296.2}
\]

So the original sharp Rademacher conjecture is equivalent to the single binary-matrix counting statement

\[
\boxed{
N_d^\circ=o\!\left(d^2\,2^{d^2-d-1}\right).
}
\tag{7.2}
\]

The class to count is explicit:

> singular `d x d` binary matrices with no zero row/column for which `J-2B` is invertible; equivalently, exact-corank-one binary matrices whose left and right null vectors both have nonzero coordinate sum, with zero-row/zero-column charts removed.

Moreover, C294 and its transpose localize the source-relevant part further: after a source-normalized `o(1)` discard, **both** left and right binary null vectors have `d-o(d)` nonzero coordinates and `d-o(d)` distinct absolute magnitudes.

This is the new target produced by the run. It packages the endpoint obstruction into one determinant-pair count rather than another one-prime or one-sided Littlewood--Offord estimate.

## 8. Method #20 — FIND WHY THE ALGORITHM FAILS: the pivot condition is genuinely necessary

A tempting stronger statement would be that once zero/equal/complement collisions are removed, a singular exact-corank-one binary matrix automatically has `J-2B` invertible. That is false.

The exact checker verifies the concrete `5 x 5` matrix

\[
B_5=
\begin{pmatrix}
0&1&1&1&1\\
1&1&1&1&1\\
1&0&0&1&1\\
1&1&0&0&1\\
1&0&1&1&0
\end{pmatrix}.
\tag{8.1}
\]

It has no zero row/column, no equal or complementary row pair, no equal or complementary column pair, and

\[
\operatorname{rank}B_5=4.
\]

A right null vector is

\[
v=(0,1,-1,1,-1)^T,
\qquad \mathbf1^Tv=0,
\]

while a left null vector is

\[
u=(1,-2,0,1,1)^T,
\qquad u^T\mathbf1=1.
\]

Hence (5.2) is identically zero in `t`, and indeed

\[
\det(J-2B_5)=0,
\qquad
\operatorname{rank}(J-2B_5)=4.
\]

So the determinant-pair condition in `N_d^circ` cannot simply be deleted at finite `d`; the obstruction is exactly a zero-sum null direction. C295 says that this type of missing-pivot sector becomes negligible at the **source normalization** after the C294 full-support localization, not that it is empty.

Checker: `artifacts/R03/20260917T1505Z_37_binary_pivot_check.py`, creation commit `1e66df1f9349ef8465e6fb95eb954f6c0948a4d2`.

Executed output: `artifacts/R03/20260917T1505Z_37_binary_pivot_check.out`, creation commit `dad536f5510783859c173f9b8ba271081e155492`, ending `SELF-CHECK PASS`.

## 9. What this changes, and what it does not

The fixed finite envelope does **not** move, so this run is honestly `NO MOVEMENT` and the unchanged count becomes `2`. This is not yet the three-run stuck trigger. If the next run also fails to move the metric (or leaves the same obligation), R03 must execute the full Section-I thinking-only stuck protocol rather than add another local lemma.

The asymptotic obligation is now sharper than run36's prose endpoint. It is enough, and by C295/C296 source-equivalent, to prove

\[
N_d^\circ=o(d^2 2^{d^2-d-1})
\]

for the explicit pivotable binary class (4.1), and C294 allows attention to matrices whose left and right null vectors are almost fully supported and have almost all absolute magnitudes distinct.

Three routes were tested this run:

- **#1 CHANGE THE CATEGORY — success.** The affine-section excess became a paired binary determinant problem `det B=0`, `det(J-2B) != 0` with exact collision charts.
- **#25 COUNT THE SAME THING TWICE — success.** Counting `(R,x)` pairs versus binary pivot matrices gives the exact `2^d`-fiber identity C296, and together with C294 upgrades the cofactor weighting to C295.
- **#20 FIND WHY THE ALGORITHM FAILS — concrete obstruction.** The `5 x 5` matrix (8.1) shows that collision removal and real corank one do not force the pivot determinant to be nonzero; a zero-sum null vector is the precise failure mode.

A productive next research route is to exploit **both** near-distinct null vectors in the binary class simultaneously. Equation (5.2) turns the remaining matrices into exact-corank-one `0/1` matrices with two almost-injective cofactor profiles and nonzero null sums. A two-sided circuit/cofactor count may gain entropy unavailable to the one-sided Sárközy--Szemerédi step. Repeating another bounded sparse modular-plane family would not address (7.2).

## 10. Model/runtime and permissions

The limitation remains exactly as recorded in the controlling policy and current ledger. The exposed task-control interface offers prompt/title, schedule/timing, enabled state and notification controls, but no model-family or reasoning-effort field and no authenticated applied-runtime telemetry. GPT-6/maximum therefore remains a prompt request, not an enforceable setting from this worker. Historical `You cannot modify this task` failures, including P26 in one context, are authorization/workspace-context failures; repository history records later success from another authorized context. The legitimate fix requires an owning/admin-authorized product surface that also exposes model/reasoning controls, or platform support. There is no repository-side bypass. This run made no scheduler or permission change.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R03
  source: F0001 / Vu Conjecture 2.2 / iid uniform Rademacher singularity
  source_status: OPEN
  run_status: PARTIAL
  metric:
    definition: "r(n)=2^n P(det B_n=0, T_n^c), full n-range retained"
    before:
      r10: "222.6104736743168493957921796888577... exact"
      r11_upper: "523.4894710902614257202829985613411..."
    after:
      r10: "222.6104736743168493957921796888577... exact"
      r11_upper: "523.4894710902614257202829985613411..."
    movement: false
    unchanged_count_before: 1
    unchanged_count_after: 2
  methods: [1,25,20]
  new_claims:
    - "R03-C295 asymptotically full left/right null support and sharp cofactor-weight reduction"
    - "R03-C296 exact 2^d-fiber binary-pivot identity and source-equivalent pivot count"
    - "explicit d=5 collision-free exact-corank-one zero-sum-null obstruction"
  checker: "artifacts/R03/20260917T1505Z_37_binary_pivot_check.py"
  checker_commit: "1e66df1f9349ef8465e6fb95eb954f6c0948a4d2"
  checker_output: "artifacts/R03/20260917T1505Z_37_binary_pivot_check.out"
  checker_output_commit: "dad536f5510783859c173f9b8ba271081e155492"
  source_record: "artifacts/R03/20260917T1505Z_37_source_status.md"
  source_record_commit: "4c5955a7a73468ebb55895d029a7cfbd3491abd9"
  next_obligation: "count the pivotable exact-corank-one binary class at o(d^2 2^(d^2-d-1)) using simultaneous near-distinct left/right null structure; one more unchanged run triggers Section-I stuck protocol"
  delivery_scope: "own immutable R03 report/artifacts only; no shared-root or peer-file edit"
```

No email, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root write, or peer-file edit was made.
