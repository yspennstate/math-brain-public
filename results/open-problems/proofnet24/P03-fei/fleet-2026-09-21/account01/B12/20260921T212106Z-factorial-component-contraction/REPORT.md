# B12 FEI creative attempt: factorial-paid contraction of fine Palm trigger blocks

**Status:** **PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

**Route:** APPROACH 1, spectral-sample compression / sequential prediction.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical-brain retrieval or receiver-context use occurred.

**Claim level:** analytic partial theorem. No novelty or publication-priority claim.

This run read the required fresh FEI packet and then substantively consumed the completed other-account result

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260921T201418Z-palm-trigger-cluster/REPORT.md`

(report Git blob `4643e5dd27cc48a508820a30413e24b9c4717fac`). That report proves that sufficiently Palm-robust reciprocal rows have one exact common trigger signature and that nonreciprocal robust trigger edges are scale escapes. I also use the exact Palm insertion code from

`proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260921T191537Z-palm-insertion-information/REPORT.md`

and the stop-bank bound `H(K)<=5I` from the current account01/B18 synthesis. The purpose here is to pay the **within-trigger-block label entropy with the exact factorial rebate at coefficient one**, rather than merely bounding it by a multiple of that rebate.

## 1. Setup

Let

\[
  \mu(A)=\widehat f(A)^2,\qquad S\sim\mu,\qquad K=|S|,
  \qquad I=\mathbb E K,
\]

and

\[
  p_i=\Pr(i\in S),\qquad \pi_i=p_i/I.
\]

The inherited Palm insertion code gives

\[
\boxed{
H(S)\le H(K)+I H(\pi)-D_{\rm seq}-Q,
\qquad Q:=\mathbb E\log_2(K!),
}
\tag{1.1}
\]

where `D_seq=I I_2(L;P)>=0` is the true sequential-prediction saving.

For each active coordinate define a **labelwise factorial allocation**

\[
\boxed{
Q_i:=\mathbb E\left[
 \frac{1_{\{i\in S\}}}{K}\log_2(K!)
\right],
}
\tag{1.2}
\]

with the integrand zero at `K=0`. Then

\[
\boxed{\sum_i Q_i=Q.}
\tag{1.3}
\]

This allocation is exact and nonoverlapping: each terminal spectral set distributes its factorial rebate equally among its members.

## 2. Fine Palm robustness

Use the account04/B12 definition. Conditional on `i in S`, write

\[
 B=S\setminus\{i\},\qquad \nu_i=\operatorname{Law}(B\mid i\in S).
\]

Row `i` is `epsilon_i`-Palm-robust with trigger set `F_i` if

\[
\operatorname{TV}(\nu_i,U_{F_i})\le\epsilon_i,
\tag{2.1}
\]

where `U_F` is uniform on all subsets of `F`. Put

\[
 m_i=|F_i|.
\]

The new regime in this report is the **fine** robustness scale

\[
\boxed{
 m_i\ge1,\qquad \epsilon_i\le\frac1{16m_i}.
}
\tag{2.2}
\]

The statement below is conditional on (2.2). It does not silently assert that every Boolean derivative row satisfies this hypothesis.

## 3. PROVED: one row's logarithmic trigger address is paid by its own factorial allocation

### Lemma 3.1
If row `i` satisfies (2.1), then

\[
\boxed{
Q_i
\ge
p_i\Bigl[(1-\epsilon_i)\log_2(m_i+1)-2\log_2 e\Bigr].
}
\tag{3.1}
\]

Consequently, under the fine scale (2.2),

\[
\boxed{
p_i\log_2(m_i+1)-Q_i
\le
\left(2\log_2 e+\frac1{16}\right)p_i.}
\tag{3.2}
\]

The numerical constant is

\[
2\log_2 e+\frac1{16}
=2.9478900817779268\ldots .
\tag{3.3}
\]

### Proof

Conditioned on `i in S`, `K=1+|B|`, so

\[
\frac{Q_i}{p_i}
=\mathbb E_{\nu_i} g(K),
\qquad
 g(k):=\frac{\log_2(k!)}k.
\tag{3.4}
\]

First work under the ideal law `U_{F_i}`. Let `X~Bin(m,1/2)` and `K=1+X`, with `m=m_i`. The elementary integral estimate

\[
\ln(k!)=\sum_{r=1}^k\ln r
\ge\int_1^k\ln x\,dx
=k\ln k-k+1
\]

gives

\[
g(k)\ge\log_2 k-\log_2 e.
\tag{3.5}
\]

The exact binomial identity already used in the preceding companion calculation is

\[
\mathbb E\frac1K
=\mathbb E\frac1{1+X}
=\frac{2-2^{-m}}{m+1}.
\tag{3.6}
\]

Since `ln z <= z-1`,

\[
\begin{aligned}
\ln(m+1)-\mathbb E\ln K
&=\mathbb E\ln\frac{m+1}{K}\\
&\le (m+1)\mathbb E\frac1K-1\\
&=1-2^{-m}\le1.
\end{aligned}
\tag{3.7}
\]

Thus

\[
\mathbb E_{U_F}g(1+|B|)
\ge\log_2(m+1)-2\log_2 e.
\tag{3.8}
\]

To transfer this to `nu_i`, truncate

\[
 h(B)=\min\{g(1+|B|),\log_2(m+1)\}.
\]

Under `U_F`, `|B|<=m`, hence `h=g`; on the full state space, `0<=h<=log_2(m+1)`. Total variation therefore gives

\[
\mathbb E_{\nu_i}g
\ge\mathbb E_{\nu_i}h
\ge\mathbb E_{U_F}h-\epsilon_i\log_2(m+1),
\]
which with (3.8) proves (3.1).

For (3.2), rearrange (3.1) and use

\[
\epsilon_i\log_2(m_i+1)
\le \frac{\log_2(m_i+1)}{16m_i}
\le\frac1{16},
\]
where `log_2(m+1)<=m` for every integer `m>=1`. QED.

## 4. PROVED: coefficient-one global factorial payment for all fine robust rows

Let `R` be any collection of rows satisfying (2.2). Summing (3.2), using the exact disjoint allocation (1.3), gives

\[
\boxed{
\sum_{i\in R}p_i\log_2(m_i+1)
\le
Q+\left(2\log_2 e+\frac1{16}\right)I.
}
\tag{4.1}
\]

More precisely the factorial term on the right may be replaced by `sum_{i in R}Q_i`, so no rebate belonging to a row outside `R` has been spent.

This coefficient-one form is the point of the calculation. A rough lower bound `Q_i >= c p_i log m_i` would be insufficient inside (1.1), because `Q` occurs there with coefficient exactly `-1`. Equation (4.1) instead says that one logarithmic trigger/block address per fine robust row can be absorbed by the *actual* factorial rebate, leaving only `2.9479 I`.

## 5. PROVED: reciprocal trigger components can be contracted in the influence-profile code

Now apply the consumed account04/B12 trigger-locking theorem. On the fine robust rows, join two rows when the trigger relation is reciprocal. Every connected component `C` has one exact trigger signature `T_C`, and for every `i in C`,

\[
F_i=T_C\setminus\{i\}.
\tag{5.1}
\]

Hence all rows in `C` have the same

\[
m_C:=|T_C|-1,
\]

and `|C|<=m_C+1`.

Put

\[
P_C:=\sum_{i\in C}p_i.
\]

The label entropy *inside* this reciprocal block is

\[
E_C:=P_C H\left((p_i/P_C)_{i\in C}\right)
\le P_C\log_2|C|
\le\sum_{i\in C}p_i\log_2(m_C+1).
\tag{5.2}
\]

Summing over reciprocal fine-robust components and applying (4.1),

\[
\boxed{
\sum_C E_C
\le
Q+\left(2\log_2 e+\frac1{16}\right)I.
}
\tag{5.3}
\]

Thus the exact factorial rebate pays **all intra-component label entropy** of these trigger blocks with only an influence-scale remainder. No pairwise KL terms are summed and no latent cluster bit is counted repeatedly.

## 6. PROVED: the global prefix code reduces to a component-level code

Treat every fine-robust reciprocal component as one macro-label. Treat every remaining active coordinate as a singleton macro-label. Let `rho` be the resulting distribution of macro-label masses divided by `I`.

The entropy chain rule for the influence-profile distribution is exact:

\[
I H(\pi)
=I H(\rho)+\sum_C E_C,
\tag{6.1}
\]

where singleton macro-labels contribute zero internal entropy.

Substitute (5.3) into the inherited Palm code (1.1). The `+Q` used in (5.3) cancels the exact `-Q` in (1.1), giving

\[
\boxed{
H(S)
\le
H(K)+I H(\rho)-D_{\rm seq}
+\left(2\log_2 e+\frac1{16}\right)I.
}
\tag{6.2}
\]

Using the current proved stop-bank estimate `H(K)<=5I`,

\[
\boxed{
H(S)
\le
7.947890081777927\,I
+I H(\rho)-D_{\rm seq}.
}
\tag{6.3}
\]

This is a genuine contraction of the compression problem: **for every fine Palm-robust reciprocal trigger block, the individual coordinate labels disappear from the unpaid Shannon term.** The remaining entropy is only the entropy of the contracted component/singleton distribution, less the genuine sequential mutual-information saving.

A useful special case is immediate: if all active coordinates form one fine robust reciprocal component, then `H(rho)=0` and

\[
H(S)\le7.947890081777927\,I.
\tag{6.4}
\]

This is only a structured-class consequence, not the full FEI theorem.

## 7. A second interpretation: one scale-escape address is also factorial-controlled

For each fine robust row `i`, let `Z_i` be *any* random trigger chosen from `F_i` (for example, a chosen nonreciprocal scale-escape target when one exists). Then

\[
H(Z_i\mid i)\le\log_2 m_i\le\log_2(m_i+1).
\]

Therefore the same proof gives

\[
\boxed{
\sum_{i\in R}p_i H(Z_i\mid i)
\le Q+2.947890081777927\,I.
}
\tag{7.1}
\]

This does **not** authorize spending the same copy of `Q` twice. It says that either the intra-block label address or one chosen trigger/escape address has a coefficient-one factorial payment. A final component-level code must arrange these uses without double spending.

## 8. What changed, and the exact remaining gap

The preceding account04/B12 cluster theorem ended with a component-level charging problem: contract reciprocal blocks and pay their nonreciprocal scale escapes. The present theorem removes one concrete part of that problem.

- The **internal label entropy of every sufficiently fine reciprocal trigger block is now paid**, at coefficient one, by the actual factorial rebate already present in the Palm insertion identity.
- Equivalently, the diffuse influence-profile term `I H(pi)` contracts exactly to the macro-label entropy `I H(rho)`, up to `2.9479 I`.
- The factor-7/codimension-drop structure from account04/B12 can therefore be applied to the smaller component distribution rather than to every row separately.

The remaining universal implication is now:

\[
\boxed{
I H(\rho)-D_{\rm seq}=O(I)
}
\tag{8.1}
\]

for the contracted macro-label distribution, while also handling rows that do not satisfy the fine Palm condition (2.2). The current theorem does **not** prove (8.1). Many tiny components can still carry large component-address entropy, and a fixed-relative `epsilon=1/16` hypothesis alone leaves an `epsilon p_i log m_i` defect that cannot simply be dropped.

A next attack should use the account04 factor-7 quotient DAG and the physical `1/(16r)` close-row branch to construct a **macro-label parent code**: low-congestion components are predicted by the Palm prefix, while scale-escape components send one address upward and spend the coefficient-one factorial budget only once. If that macro-label entropy can be made `O(I)`, the fine-robust sector of the universal gap closes; nonrobust rows remain the separate stability sector.

**Full FEI remains OPEN.**
