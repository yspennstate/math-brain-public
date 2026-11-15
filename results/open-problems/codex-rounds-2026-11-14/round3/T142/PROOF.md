# Exact quadratic projection without the full spectrum

Let $X,Y$ be independent uniform binary words of length $n$, and let

\[
f_n(x,y)=\operatorname{LCS}(x,y),\qquad m=2^n,\quad M=m^2.
\]

Index the letters from 0 to $n-1$. For a bit mask $u$, put

\[
\chi_u(x)=(-1)^{\operatorname{popcount}(u\mathbin{\&}x)}.
\]

## 1. Recheck of the variance bound

The functions $\chi_u(x)\chi_v(y)$, over all masks $u,v$, form an
orthonormal basis under uniform measure: distinct products have a fair bit
appearing once, and their expectation is zero. Write the corresponding
coefficients as $\widehat f_n(u,v)$. Parseval gives

\[
\operatorname{Var}(L_n)=\sum_{(u,v)\ne(0,0)}\widehat f_n(u,v)^2.
\]

Complementing both words leaves their LCS unchanged and multiplies a character
by $(-1)^{|u|+|v|}$. Thus all odd-degree coefficients vanish. If coordinate
$i$ is flipped, the difference of the two function values is twice the
sum of the character terms containing $i$. Squaring and averaging, then
summing over coordinates, gives

\[
\frac14\sum_{i=1}^{2n}\mathbb E(f_n(Z)-f_n(Z^{(i)}))^2
=\sum_{u,v}(|u|+|v|)\widehat f_n(u,v)^2
\ge 2\operatorname{Var}(L_n).
\]

Deleting the matched letter at a changed position from an optimal subsequence
shows that one flip changes $f_n$ by at most 1. The left side is therefore
at most $n/2$, proving $\operatorname{Var}(L_n)\le n/4$. For $n=1$,
$L_1$ is a fair indicator and its variance is $1/4$.

## 2. Partial transforms recover every quadratic coefficient

Define the unnormalized transform of one row by

\[
T_v(x)=\sum_y f_n(x,y)\chi_v(y).
\]

After processing that row, retain only $T_0(x)$ and the $n$ values
$T_{2^j}(x)$, for $0\le j<n$. Transforming these retained arrays over
$x$ gives

\[
C(u,v)=\sum_x T_v(x)\chi_u(x)
=\sum_{x,y}f_n(x,y)\chi_u(x)\chi_v(y)
=M\widehat f_n(u,v).
\tag{1}
\]

This identity is just rearrangement of finite sums. It recovers the same-word
quadratic coefficients from $C(2^i+2^j,0)$, and the cross-word quadratic
coefficients from $C(2^i,2^j)$. Exchanging $x$ and $y$ preserves $f_n$,
so the other same-word coefficients equal those already recovered. Consequently

\[
W_2=\frac{2\sum_{i<j}C(2^i+2^j,0)^2
                  +\sum_{i,j}C(2^i,2^j)^2}{M^2}
\le\operatorname{Var}(L_n).
\tag{2}
\]

Each Walsh transform on $m$ entries uses $n$ butterfly stages, with
$m/2$ butterflies per stage. There are $m$ row transforms and $n+1$
transforms on retained arrays. The transform work is $O(n4^n+n^2 2^n)$.
The bit recurrence for each LCS score uses $n$ steps at the stated fixed
cutoff, so the total work is $O(n4^n)$. The working storage is $O(n2^n)$.

The implementation retains one 32-bit row, $n+1$ arrays of signed 64-bit
integers, and one signed byte per word for the adjacent-sign statistic. At
$n=16$, the allocated arrays occupy exactly

\[
(17\cdot8+4+1)2^{16}=9,240,576\text{ bytes}.
\]

For $n\le16$, a row-transform intermediate has absolute value at most
$n2^n\le2^{20}$, and a column-transform intermediate at most
$n4^n\le2^{36}$. They fit their respective signed integer types. For a
quadratic coefficient, subtracting the zero-mean constant $n/2$ gives

\[
|C(u,v)|\le(n/2)M\le2^{35}.
\]

There are at most $\binom{32}{2}=496$ quadratic coefficients. Their squared
sum is therefore less than $2^{79}$, and unsigned 128-bit accumulators
suffice. The histogram moments, their products, and the conditional row-sum
squares also fit 128 bits by the bounds $0\le f_n\le16$, $m\le2^{16}$.

## 3. Adjacent statistic and derivative

Put $s_i=(-1)^{X_i}$, $t_i=(-1)^{Y_i}$, and

\[
S=\sum_{i=0}^{n-2}s_is_{i+1}+\sum_{i=0}^{n-2}t_it_{i+1}.
\]

Its summands are distinct Walsh characters, so $\mathbb ES=0$ and
$\mathbb ES^2=2(n-1)$. Let $F_n(\theta)$ be the mean LCS when the two
words independently have a uniform first letter and repeat the previous
letter with probability $(1+\theta)/2$. The density relative to uniform
words is

\[
\prod_{i=0}^{n-2}(1+\theta s_is_{i+1})
\prod_{i=0}^{n-2}(1+\theta t_it_{i+1}).
\]

Differentiating this finite polynomial at zero proves

\[
F'_n(0)=\mathbb E[f_n S]
=\frac2M\sum_{i=0}^{n-2}C(2^i+2^{i+1},0).
\tag{3}
\]

For $n\ge2$, Cauchy–Schwarz gives

\[
\operatorname{Var}(L_n)\ge\frac{F'_n(0)^2}{2(n-1)}.
\tag{4}
\]

The program obtains (3) both from the transformed coefficients and by directly
accumulating $f_n(x,y)S(x,y)$ before transforming. The direct sign sum for
one word is $n-1-2\operatorname{popcount}((x\oplus(x\!\gg1))\mathbin{\&}
(2^{n-1}-1))$. At $n=1$, it is zero; (4) is used only for $n\ge2$.

## 4. Boundary identities for an additional audit

Write $a_{ij}=\mathbb E[f_n s_i s_j]$,
$b_{ij}=\mathbb E[f_n s_i t_j]$, and $\mu_n=\mathbb E L_n$, with
$\mu_0=0$. Then

\[
b_{00}=1+\mu_{n-1}-\mu_n,
\qquad a_{0j}=-b_{j0}\quad(1\le j<n).
\tag{5}
\]

To justify the first-letter recurrence, suppose the first letters agree.
There is an optimal subsequence using both first positions. Indeed, if an
optimal alignment uses neither, prepend the equal first letters, contradicting
optimality. If it uses only one first position, that position is in its first
match; replace that match by the two first positions. All later matches still
follow it. Removing this first match then shows

\[
f_n(X,Y)=1+f_{n-1}(X_1\cdots X_{n-1},Y_1\cdots Y_{n-1})
\quad\hbox{on }X_0=Y_0.
\tag{6}
\]

The equal-first-letter event $E$ has probability $1/2$, and the suffixes
are independent of it. Since $s_0t_0=2\mathbf1_E-1$, equation (6) gives

\[
b_{00}=2\mathbb E[f_n\mathbf1_E]-\mu_n=1+\mu_{n-1}-\mu_n.
\]

On $E^c$, $s_0+t_0=0$. Conditional on $E$, the common first sign
is fair and independent of both suffixes. For $j\ge1$, (6) therefore gives

\[
a_{0j}+b_{j0}=\mathbb E[f_n(s_0+t_0)s_j]=0.
\]

Reversing both words preserves the score, giving the corresponding identities
at their last positions:

\[
b_{n-1,n-1}=1+\mu_{n-1}-\mu_n,
\qquad a_{i,n-1}=-b_{i,n-1}\quad(0\le i<n-1).
\tag{7}
\]

Equations (5) and (7) test individual coefficient signs and normalizations,
including a relation to the separately accumulated histograms at a different
word length. They do not imply a linear lower bound on (2) or (4).
