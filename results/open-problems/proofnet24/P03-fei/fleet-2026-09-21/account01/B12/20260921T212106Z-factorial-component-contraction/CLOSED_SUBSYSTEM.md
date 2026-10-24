# Addendum: global cross-component companion-flow budget on a closed fine-robust subsystem

**Status:** analytic partial theorem; full FEI remains OPEN. No novelty claim.

This addendum continues the coefficient-one factorial contraction in `REPORT.md` and the reciprocal-trigger theorem of account04/B12. It addresses the next question: after reciprocal contraction, how much fine-robust mass can actually point outside its own component?

## 1. Closed fine-robust subsystem

Let `R` be a set of active coordinates such that every `i in R` is `epsilon_i`-Palm-robust with trigger set `F_i`,

\[
\operatorname{TV}(\nu_i,U_{F_i})\le\epsilon_i,
\qquad m_i:=|F_i|\ge1,
\qquad \epsilon_i\le\frac1{16m_i},
\tag{1.1}
\]

and assume the subsystem is **trigger-closed**:

\[
F_i\subseteq R\qquad(i\in R).
\tag{1.2}
\]

Contract the reciprocal-trigger graph using account04/B12. Each component `C` has a common signature `T_C`, and for every `i in C`,

\[
F_i=T_C\setminus\{i\}.
\]

Write

\[
m_C=|T_C|-1,
\qquad c_C=|C|,
\qquad e_C:=|T_C\setminus C|=m_C+1-c_C,
\qquad W_C:=\sum_{i\in C}p_i.
\tag{1.3}
\]

Thus `e_C` is the number of trigger coordinates of `C` lying in other reciprocal components.

Use the exact one-companion flow from the preceding account01/B12 run,

\[
r_{ik}:=\mathbb E\frac{1_{\{i,k\in S\}}}{K}=r_{ki}.
\tag{1.4}
\]

## 2. PROVED: each external trigger fraction creates real cross-component companion flow

For a source component `C` with `e_C>0`, define

\[
R_{\rm out}(C):=
\sum_{i\in C}\sum_{k\in T_C\setminus C}r_{ik}.
\]

### Lemma 2.1

\[
\boxed{
R_{\rm out}(C)
\ge
\frac3{16}\frac{e_C}{m_C}W_C.
}
\tag{2.1}
\]

### Proof

Fix `i in C` and put `E_C=T_C\setminus C`. Conditional on `i in S`,

\[
\frac1{p_i}\sum_{k\in E_C}r_{ik}
=
\mathbb E_{\nu_i}
\frac{|B\cap E_C|}{1+|B|}.
\tag{2.2}
\]

Under the ideal law `U_{F_i}`, symmetry gives

\[
\mathbb E_{U_{F_i}}
\frac{|B\cap E_C|}{1+|B|}
=
\frac{e_C}{m_C}(1-a_{m_C}),
\qquad
 a_m:=\mathbb E\frac1{1+\operatorname{Bin}(m,1/2)}
 =\frac{2-2^{-m}}{m+1}.
\tag{2.3}
\]

The function in (2.2) lies in `[0,1]`, so total variation and (1.1) give

\[
\frac1{p_i}\sum_{k\in E_C}r_{ik}
\ge
\frac{e_C}{m_C}(1-a_{m_C})-rac1{16m_C}.
\tag{2.4}
\]

For every `m>=1`, `1-a_m>=1/4`; for `e_C>=1`,

\[
\frac{e_C}{4m_C}-\frac1{16m_C}
=\frac{4e_C-1}{16m_C}
\ge\frac{3e_C}{16m_C}.
\]

Multiply by `p_i` and sum over `i in C`. QED.

## 3. PROVED: the target side has only a tiny outside-trigger companion capacity

Fix a target row `k in R`. Every source coordinate `i` in another reciprocal component that triggers `k` satisfies

\[
i\notin F_k;
\]
otherwise the trigger would be reciprocal and `i,k` would belong to the same contracted component.

Hence all incoming cross-component companion flow into `k` is bounded by the entire companion flow from coordinates outside `F_k`:

\[
\begin{aligned}
\frac1{p_k}
\sum_{i\notin F_k\cup\{k\}}r_{ki}
&=
\mathbb E_{\nu_k}
\frac{|B\setminus F_k|}{1+|B|}\\
&\le
\Pr_{\nu_k}(B\not\subseteq F_k)\\
&\le\epsilon_k
\le\frac1{16m_k}.
\end{aligned}
\tag{3.1}
\]

Therefore the total incoming cross-component companion capacity of a component `D` is at most

\[
\boxed{
R_{\rm in}(D)
\le
\sum_{k\in D}\frac{p_k}{16m_D}
=rac{W_D}{16m_D}.
}
\tag{3.2}
\]

The symmetry `r_{ik}=r_{ki}` means the total source outgoing flow and total target incoming flow are the same global quantity.

## 4. PROVED: a global nonreuse bound on the external-trigger fraction

Sum (2.1) over source components and (3.2) over target components. Every cross-component trigger pair is nonreciprocal, hence counted only once on the source side, while its symmetric companion mass is included on the target outside-trigger side. Thus

\[
\frac3{16}
\sum_C W_C\frac{e_C}{m_C}
\le
\sum_C R_{\rm out}(C)
\le
\sum_D\frac{W_D}{16m_D}
\le\frac I{16}.
\]

Therefore

\[
\boxed{
\sum_C W_C\frac{e_C}{m_C}
\le\frac I3.
}
\tag{4.1}
\]

This is an actual global companion-flow budget, not a sum of pairwise KL terms. In particular, for every `theta>0`, the total influence mass of components with external-trigger fraction at least `theta` obeys

\[
\boxed{
\sum_{C:e_C/m_C\ge\theta}W_C
\le\frac{I}{3\theta}.
}
\tag{4.2}
\]

## 5. Interpretation and remaining gap

The factor-7 quotient DAG from account04/B12 now has a second, independent restriction in the fine branch: **weighted external trigger density is globally companion-flow sparse**. A component can have many nonreciprocal scale-escape targets only if its influence mass is correspondingly small in the global first-moment budget.

Together with `REPORT.md`, the fine closed subsystem has two rigorously paid/compressed features:

1. all intra-component coordinate-label entropy contracts into the exact factorial rebate up to `2.9479 I`;
2. the weighted fraction of trigger addresses that leave their component has total budget at most `I/3`.

This is still not a proof that the macro-label entropy `I H(rho)` is `O(I)`. The missing issue is **log-weighting**: (4.1) controls `W_C e_C/m_C`, not `W_C(e_C/m_C) log(I/W_C)`. Many tiny components can therefore still carry large macro-label entropy unless the Palm predictor, the physical scale relation, or a new Booleanity constraint pays that logarithm.

The next clean target is a logarithmically weighted version of (4.1), or a component-parent coding theorem that converts the factor-7 scale jump plus the outside-trigger companion capacity into such a weighted bound without charging one target component repeatedly.

**Full FEI remains OPEN.**
