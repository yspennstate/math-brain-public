# Corollary: a sharp low-influence sensitivity factorial-moment inequality

**Status:** PROVED as an auxiliary universal inequality under `max_i Inf_i(f) <= 1/2`; full FEI remains OPEN. No novelty/prior-art claim is made.

The main report's depth functional has a clean input-side form which is worth recording separately because it joins APPROACHES routes 1 and 3.

Let `f:{-1,1}^n->{-1,1}` be Boolean, let `S` be its spectral sample, let

\[
j_i=\operatorname{Inf}_i(f)=\Pr(i\in S),
\]

and let `T=Sens_f(X)` be the sensitivity set of a uniform input `X`. Assume every active `j_i<=1/2`.

The one-row Palm-depth theorem gives

\[
\mathbb E[|S|-1\mid i\in S]\ge \frac12\log_2\frac1{j_i}.
\tag{1}
\]

Multiplying by `j_i` and summing over `i`,

\[
\begin{aligned}
\mathbb E[|S|(|S|-1)]
&=\sum_i j_i\mathbb E[|S|-1\mid i\in S]\\
&\ge \frac12\sum_i j_i\log_2\frac1{j_i}.
\end{aligned}
\tag{2}
\]

The exact two-local spectral/sensitivity bridge gives

\[
\Pr(i,j\in S)=\Pr(i,j\in T)\qquad(i\ne j).
\tag{3}
\]

Summing (3) over ordered pairs yields

\[
\mathbb E[|S|(|S|-1)]=\mathbb E[|T|(|T|-1)].
\tag{4}
\]

Therefore

\[
\boxed{
\mathbb E\big[|Sens_f(X)|(|Sens_f(X)|-1)\big]
\ge
\frac12\sum_i \operatorname{Inf}_i(f)
\log_2\frac1{\operatorname{Inf}_i(f)}.
}
\tag{5}
\]

This is entirely input-side on the left and converts the logarithmic spread of the influence profile into a required second factorial moment of the sensitivity set.

If `q_i=j_i/I(f)`, then

\[
\sum_i j_i\log_2(1/j_i)=I(f)\big(H(q)-\log_2 I(f)\big),
\]

so equivalently

\[
H(q)\le \log_2 I(f)+
\frac{2\,\mathbb E[|Sens(X)|(|Sens(X)|-1)]}{I(f)}.
\tag{6}
\]

Equation (6) by itself does **not** close FEI: the sensitivity second moment can be much larger than total influence, so inserting it naively into the global ordered-set entropy code loses dimension-free control. Its value is as a structural constraint and as a possible block-selection statistic.

## Equality classification

Equality in (5) is equivalent to equality in (1) for every active coordinate, because all summands have nonnegative deficits. The main report proves that simultaneous equality of all those rows forces, after deleting dummy coordinates and applying cube/output symmetries, a one-point defect. Conversely every one-point defect with at least two active coordinates attains row equality. Thus, within the stated low-influence regime,

\[
\boxed{\text{Equality in (5) iff the active function is a one-point defect.}}
\tag{7}
\]

The subcube-plus-one-point family from the main report shows that (7) has no dimension-independent positive normalized gap: the left-minus-right slack divided by `I(f)` can tend to zero along non-equality functions. Hence a useful quantitative version must be a weighted stability statement, not a fixed gap theorem.
