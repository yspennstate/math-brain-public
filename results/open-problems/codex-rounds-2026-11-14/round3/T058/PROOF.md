# Adjacent independent-set counts on an interior phase band

Write log for the natural logarithm and put

\[
 f(n)=2\log_2 n-2\log_2\log_2 n+2\log_2(e/2)+1,
 \qquad k=\lfloor f(n)\rfloor,\qquad t=\{f(n)\}.
\]

Let \(X_j\) count independent vertex sets of size \(j\) in \(G(n,1/2)\), and let

\[
 q_j=2^{-\binom j2},\qquad \mu_j=\mathbb E X_j=\binom nj q_j.
\]

Fix \(0<\delta<1/2\). All limits below are uniform over integers \(n\) with
\(\delta\le t\le1-\delta\). In particular they hold on the band
\(1/4\le t\le3/4\) studied in the earlier report.

**Proposition.** On this band,

\[
 \operatorname{Var}X_k\sim\mu_k,\qquad
 \operatorname{Var}X_{k-1}\sim\mu_{k-1},\qquad
 \operatorname{Cov}(X_k,X_{k-1})\sim k\mu_k.                 \tag{1}
\]

Consequently their correlation \(\rho_n\) satisfies

\[
 \rho_n\sim\sqrt{\frac{k(n-k+1)}{2^{k-1}}}
 \sim \frac{2\sqrt2}{e}\,2^{t/2}
             \frac{(\log_2 n)^{3/2}}{\sqrt n}.              \tag{2}
\]

In particular \(\rho_n\to0\). Also

\[
 \inf_{a,b\in\mathbb R}
   \mathbb E\bigl[(X_{k-1}-a-bX_k)^2\bigr]\sim\mu_{k-1}.  \tag{3}
\]

These are second-moment statements. They assert neither independence nor a concentration bound for the chromatic number.

## 1. Sizes of the means

Let \(L=\log n\), \(\ell=\log2\), \(M=2/\ell\) and \(c=1+\log\ell\). Then

\[
 k=M(L-\log L+c)-1-t=ML+O(\log L).                         \tag{4}
\]

For \(j=O(L)\), expanding \(\binom nj\) as a product gives

\[
 \log\binom nj=jL-\log j!+O(j^2/n).
\]

Indeed the correction to \(jL-\log j!\) is
\(\sum_{i=0}^{j-1}\log(1-i/n)\), whose absolute value is at most
\(2\sum_{i=0}^{j-1}i/n\) for sufficiently large \(n\).
Integral comparison gives \(\log j!=j\log j-j+O(\log j)\). Therefore

\[
 \log\mu_k
 =k\left[L-\frac\ell2(k-1)-\log k+1\right]+O(\log k+k^2/n).
\]

Substitution of (4) gives the exact bracket identity

\[
 L-\frac\ell2(k-1)-\log k+1
       =\log(ML/k)+\frac\ell2t.
\]

Since \(k=ML+O(\log L)\), multiplying the right side by \(k\) gives
\(tL+O(\log L)\), uniformly for \(0\le t<1\). It follows that

\[
 \mu_k=n^{t+o(1)}.                                        \tag{5}
\]

The exact consecutive-mean ratio is

\[
 \frac{\mu_{k-1}}{\mu_k}
       =\frac{k\,2^{k-1}}{n-k+1}.                         \tag{6}
\]

The definition of \(f\) also gives exactly

\[
 2^k=\frac{e^2}{2}\,2^{-t}\frac{n^2}{(\log_2 n)^2}.       \tag{7}
\]

Thus \(\mu_{k-1}/\mu_k=\Theta(n/\log n)\), and

\[
 \mu_{k-1}=n^{1+t+o(1)}.                                  \tag{8}
\]

On the stated band, (5) and (8) imply, for sufficiently large \(n\),
\(\mu_k\le n^{1-\delta/2}\) and
\(\mu_{k-1}\le n^{2-\delta/2}\). In particular both means are at most
\(n^{2-\delta+o(1)}\), and both tend to infinity. The errors here are uniform because the error in (5) was uniform.

## 2. Exact covariance identity

Take \((K,l)\) equal to \((k,k)\), \((k-1,k-1)\), or \((k,k-1)\).
Fix a vertex set \(A\) of size \(K\). There are
\(\binom Kj\binom{n-K}{l-j}\) sets \(B\) of size \(l\) with
\(|A\cap B|=j\). Let \(I_A,I_B\) indicate that these sets are independent.
The union of their edge constraints has size
\(\binom K2+\binom l2-\binom j2\). Hence

\[
 \mathbb E(I_AI_B)=q_Kq_l\,2^{\binom j2},\qquad
 \operatorname{Cov}(I_A,I_B)=q_Kq_l(2^{\binom j2}-1).
\]

For \(j=0,1\), the covariance is exactly zero. Summing over all ordered pairs \((A,B)\) gives

\[
 \operatorname{Cov}(X_K,X_l)
 =\mu_K\sum_{j=2}^l h_j(1-2^{-\binom j2}),                 \tag{9}
\]

where

\[
 h_j=\binom Kj\binom{n-K}{l-j}
                2^{-\binom l2+\binom j2}.                 \tag{10}
\]

For \(K=l\), this is also the variance identity, including its diagonal term. The endpoint is

\[
 h_l=\binom Kl=
 \begin{cases}1,&K=l,\\ k,&(K,l)=(k,k-1).\end{cases}        \tag{11}
\]

## 3. All other overlaps are smaller

We prove the uniform bound

\[
 \sum_{j=2}^{l-1}h_j
 =O\left(\frac{\mu_l K^5}{n^2}
                      +h_l K^2n2^{-l}\right).             \tag{12}
\]

Here \(K-l\in\{0,1\}\),
\(K,l=2\log_2 n-2\log_2\log_2 n+O(1)\), and
\(2^l=\Theta(n^2/(\log n)^2)\).

First take \(2\le j\le m=\lfloor l/2\rfloor\).
For a uniformly chosen \(l\)-set \(B\), a union bound over the
\(j\)-subsets of \(A\) gives

\[
 \frac{\binom Kj\binom{n-K}{l-j}}{\binom nl}
 \le \mathbb P(|A\cap B|\ge j)
 \le \binom Kj\frac{(l)_j}{(n)_j}
 \le \left(\frac{Kl}{n-l}\right)^j.
\]

In the last step, \(\binom Kj\le K^j\), \((l)_j\le l^j\), and
\((n)_j\ge(n-l)^j\); \((x)_j\) denotes the falling factorial.
Thus \(h_j\le\mu_l v_j\), where

\[
 v_j=\left(\frac{Kl}{n-l}\right)^j2^{j(j-1)/2}.
\]

The logarithm of \(v_j\), extended to real \(j\), is a convex quadratic.
A convex function on a closed interval is at most the larger of its endpoint values. Therefore

\[
 \sum_{j=2}^m h_j\le\mu_l m\max(v_2,v_m).                 \tag{13}
\]

Put \(u=\log_2 n\). Then
\(K,l=2u+O(\log u)\), \(m=u+O(\log u)\), and
\(\log_2(Kl/(n-l))=-u+O(\log u)\). Consequently

\[
 \log_2 v_m
 =m[-u+O(\log u)]+\frac{m(m-1)}2
 =-\frac12u^2+O(u\log u).
\]

In contrast \(v_2=2(Kl/(n-l))^2=\Theta(K^4/n^2)\), whose logarithm is
\(-2u+O(\log u)\). Hence eventually \(v_m\le v_2\). Equation (13) is
\(O(\mu_l K^5/n^2)\).

For \(m<j<l\), put \(s=l-j\); then \(1\le s\le l-m-1\le\lceil l/2\rceil\). From (10),

\[
 \frac{h_{l-s}}{h_l}
 =\frac{\binom K{l-s}}{\binom Kl}\binom{n-K}s
              2^{-sl+s(s+1)/2}.                           \tag{14}
\]

If \(K=l\), the first ratio is \(\binom ls\le K^s\).
If \(K=l+1\), it is
\(\binom K{s+1}/K=\binom{K-1}s/(s+1)\le K^s\).
Also \(\binom{n-K}s\le n^s\). Therefore

\[
 h_{l-s}/h_l\le w_s:=(Kn2^{-l})^s2^{s(s+1)/2}.
\]

Again \(\log w_s\) is convex. Let \(m'=\lceil l/2\rceil\).
We may bound the shorter actual sum by the sum over \(1\le s\le m'\).
Its endpoint values satisfy

\[
 w_1=2Kn2^{-l}=\Theta((\log n)^3/n),
\]

and, since \(\log_2(Kn2^{-l})=-u+O(\log u)\) and
\(m'=u+O(\log u)\),

\[
 \log_2 w_{m'}=-\frac12u^2+O(u\log u).
\]

Thus eventually \(w_{m'}\le w_1\). Convexity bounds the large-overlap sum by
\(h_l m'w_1=O(h_l K^2n2^{-l})\). Together with (13) this proves (12).

All midpoint comparisons are uniform: the constants in their
\(O(\log u)\) terms are bounded for \(0\le t<1\) and for all three pairs \((K,l)\).

## 4. Variance, covariance and correlation

For equal sizes \(K=l\), (9), (11), (12) and
\(0\le1-2^{-\binom j2}\le1\) give

\[
 1-q_l\le\frac{\operatorname{Var}X_l}{\mu_l}
 \le 1-q_l+O\left(\frac{\mu_l K^5}{n^2}+K^2n2^{-l}\right). \tag{15}
\]

For both sizes in question, \(q_l\to0\),

\[
 \frac{\mu_l K^5}{n^2}\le n^{-\delta+o(1)}\to0,
 \qquad K^2n2^{-l}=O((\log n)^4/n)\to0.
\]

This proves the two variance estimates in (1).

For \((K,l)=(k,k-1)\), divide (9) by \(k\mu_k\) and use \(h_l=k\):

\[
 1-q_l\le\frac{\operatorname{Cov}(X_k,X_l)}{k\mu_k}
 \le1-q_l+O\left(\frac{\mu_l k^4}{n^2}+k^2n2^{-l}\right).  \tag{16}
\]

Both error terms tend to zero by the same bounds. This proves the covariance estimate. The contribution of contained pairs alone is exactly \(k\mu_k(1-q_{k-1})\); all other overlapping pairs have smaller total contribution.

Combining (1) with (6),

\[
 \rho_n\sim k\sqrt{\mu_k/\mu_{k-1}}
          =\sqrt{k(n-k+1)/2^{k-1}}.
\]

Using (7), \(k\sim2\log_2 n\), and \(n-k+1\sim n\), the square of the last expression is asymptotic to
\(8e^{-2}2^t(\log_2 n)^3/n\). Taking its positive square root proves (2).

Finally, for any square-integrable random variables \(U,V\) with positive variance of \(U\), first minimize over the intercept to center the residual. Completing the square in the slope gives

\[
 \inf_{a,b}\mathbb E[(V-a-bU)^2]
       =\operatorname{Var}V
          -\frac{\operatorname{Cov}(U,V)^2}{\operatorname{Var}U}
       =\operatorname{Var}V(1-\operatorname{Corr}(U,V)^2).
\]

Apply this with \(U=X_k,V=X_{k-1}\). The variance estimates and
\(\rho_n\to0\) prove (3).

## Relation to concentration of the chromatic number

The earlier density theorem gives lower natural density
\(1/(1+2^{1/4})\) to the band \(1/4\le t\le3/4\), so (1)–(3) apply on a set of positive lower density. That deterministic input is independently rechecked in LOG.md and recheck_earlier.py.

Annika Heckel and Oliver Riordan, *How does the chromatic number of a random graph vary?*, [arXiv:2103.14014](https://arxiv.org/html/2103.14014), equation (10) and the discussion preceding Conjecture 10, already describe approximately Poisson marginal laws for these two counts and motivate their proposed contributions to chromatic fluctuations. The proposition supplies an explicit joint second-moment calculation on a specified band. It does not prove a joint Gaussian law and does not show how either count controls the chromatic number. That transfer remains necessary for a bound on its concentration width. No novelty in the broader literature is asserted for these overlap estimates.
