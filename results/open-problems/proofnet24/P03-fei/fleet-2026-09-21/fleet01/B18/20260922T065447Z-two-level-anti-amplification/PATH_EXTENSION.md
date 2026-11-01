# B18 addendum — single-path restriction-tree anti-amplification ladder

This addendum continues the same run and uses only the proved bank

\[
F(d)\ge -M,\qquad M<0.118,
\]

from `REPORT.md`. It does not change the classification: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

## 1. Universal path inequality

Let `f` be a minimum-dimensional counterexample to FEI at
\(C^\dagger=6.521851214\), and retain the fresh-character lift used in the main report.
Fix any realizable physical restriction path

\[
\sigma=(i_1=b_1,\ldots,i_r=b_r)
\]

of `r>=1` distinct original coordinates, and let `j` be any remaining original coordinate. Put

\[
e=\operatorname{Inf}_j(f_\sigma).
\]

Build the physical tree which reveals `i_1` at the root, follows only the chosen branch `b_1`, stops the opposite branch, then reveals `i_2`, and so on until the node `sigma`, where it reveals `j`. Every stopped branch and every final child is a proper restriction of the original minimum counterexample, hence has nonnegative lifted defect.

If `d_k` is the pivot disagreement at depth `k<r`, the source-exact tree compiler gives

\[
0>D(\widetilde f)
\ge
\sum_{k=0}^{r-1}2^{-k}F(d_k)+2^{-r}F(e).
\]

Using `F(d_k)>=-M` at every ancestor,

\[
0>
-2M(1-2^{-r})+2^{-r}F(e).
\]

Therefore every such path satisfies the exact necessary inequality

\[
\boxed{
F\!\left(\operatorname{Inf}_j(f_\sigma)\right)
<(2^{r+1}-2)M.
}
\tag{1.1}
\]

This is a genuine physical restriction statement. No coordinate label is charged unless it is actually revealed, and the stopped sibling branches are paid by minimum-dimensional safety.

## 2. Early-depth influence ladder

For `d>=1/2`, directly from

\[
F(d)=C^\dagger d-1-h_2(d)+\Theta(2d-1)
\]

and `h_2(d)<=1`, `Theta>=0`,

\[
F(d)\ge C^\dagger d-2.
\tag{2.1}
\]

Together with `M<0.118`, (1.1) gives:

### Depth one

The sharper main-report calculation already proves

\[
\boxed{
|\sigma|=1\Longrightarrow
\operatorname{Inf}_j(f_\sigma)<0.312.
}
\tag{2.2}
\]

### Depth two

Here `(2^{3}-2)M<6(0.118)=0.708`. But

\[
F(1/2)=C^\dagger/2-2=1.260925607>0.708.
\]

Since `F` is increasing on `[0.1741,1]`,

\[
\boxed{
|\sigma|=2\Longrightarrow
\operatorname{Inf}_j(f_\sigma)<0.5.
}
\tag{2.3}
\]

### Depth three

Here `(2^{4}-2)M<14(0.118)=1.652`. If `d>=0.56`, then by (2.1)

\[
F(d)\ge C^\dagger(0.56)-2
=1.65223667984
>1.652.
\]

Therefore

\[
\boxed{
|\sigma|=3\Longrightarrow
\operatorname{Inf}_j(f_\sigma)<0.56.
}
\tag{2.4}
\]

The exact margin in the displayed comparison is

\[
1.65223667984-1.652
={1479249\over6250000000}>0.
\]

### Depth four

Here `(2^{5}-2)M<30(0.118)=3.54`. If `d>=0.85`, then

\[
F(d)\ge C^\dagger(0.85)-2
=3.5435735319
>3.54.
\]

Hence

\[
\boxed{
|\sigma|=4\Longrightarrow
\operatorname{Inf}_j(f_\sigma)<0.85.
}
\tag{2.5}
\]

with exact margin

\[
3.5435735319-3.54
={35735319\over10000000000}>0.
\]

At depth five the crude single-path bank no longer gives a nontrivial influence ceiling because `62(0.118)>C^dagger=F(1)`. More branching, rather than a longer single path, is therefore essential beyond this point.

## 3. Interpretation and next gap

The main report already rules out one-step conditional influence `>=0.312` and forces one child of every first pivot to be `0.262`-diffuse. The present path theorem adds that a hypothetical minimum counterexample cannot hide a near-deterministic pivotal coordinate immediately behind a short sparse restriction: after two restrictions every remaining influence is `<0.5`, after three it is `<0.56`, and after four it is `<0.85`.

This is especially relevant to sparse-defect/addressing-like mechanisms, where a tiny root influence can become order-one after conditioning on a short address. Such an explosion cannot occur within the first four physical restrictions of a minimum counterexample at the fixed candidate.

The exact next mathematical gap is now a **branching** tree inequality: single-path payment becomes too expensive after depth four. A successful continuation must reuse positive payments across both children/frontier nodes, rather than follow one rare branch and pay a fresh worst-case `M` at every ancestor.

Full FEI remains **OPEN / NOT PROVED**.
