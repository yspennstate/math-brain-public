# A joint Gaussian limit for adjacent independent-set counts

All unmarked logarithms are natural. Put
\[
 f(n)=2\log_2 n-2\log_2\log_2 n+2\log_2(e/2)+1,
 \quad k=\lfloor f(n)\rfloor,\quad t_n=\{f(n)\}.
\]
Fix \(0<\delta<1/2\), and restrict throughout to integers satisfying
\(\delta\le t_n\le1-\delta\). Let \(X_j\) be the number of independent
\(j\)-sets in \(G(n,1/2)\), and write
\[
 q_j=2^{-\binom j2},\qquad \mu_j=\binom njq_j,
 \qquad U_j=\frac{X_j-\mu_j}{\sqrt{\mu_j}}.
\]

**Theorem.** Uniformly on this phase band,
\[
 (U_k,U_{k-1})\ \xrightarrow{d}\ (Z_1,Z_2),                 \tag{1}
\]
where \(Z_1,Z_2\) are independent standard normal variables.
More explicitly, define
\[
 \epsilon_j=\frac{\operatorname{Var}X_j}{\mu_j}-1+2q_j,
 \qquad c_n=\frac{\operatorname{Cov}(X_k,X_{k-1})}
                    {\sqrt{\mu_k\mu_{k-1}}}.
\]
Then \(\epsilon_j\ge0\), and, for every real \(s,t\),
\[
\begin{split}
 \left|\mathbb E e^{i(sU_k+tU_{k-1})}
                  -e^{-(s^2+t^2)/2}\right|
 \le{}& |st|c_n+\frac{s^2\epsilon_k+t^2\epsilon_{k-1}}2\\
      &+\frac{|s|^3}{6\sqrt{\mu_k}}
       +\frac{|t|^3}{6\sqrt{\mu_{k-1}}}.                  \tag{2}
\end{split}
\]
The right side tends to zero, uniformly for \((s,t)\) in a fixed bounded
set. It is at most \(n^{-\delta/2+o(1)}\) on such a set.

This is a statement about the two counts. It provides no concentration
bound for the chromatic number.

## 1. The moment input, rechecked

The round 3 calculation gives
\[
 \mu_k=n^{t_n+o(1)},\qquad \mu_{k-1}=n^{1+t_n+o(1)},       \tag{3}
\]
\[
 \operatorname{Var}X_k\sim\mu_k,\quad
 \operatorname{Var}X_{k-1}\sim\mu_{k-1},\quad
 \operatorname{Cov}(X_k,X_{k-1})\sim k\mu_k.               \tag{4}
\]
Here is a derivation sufficient to check the input and its uniformity.
Let \(L=\log n\), \(\ell=\log2\), and \(M=2/\ell\). Then
\[
 k=M(L-\log L+1+\log\ell)-1-t_n=ML+O(\log L).
\]
The product formula for \(\binom nk\) and integral bounds for \(\log k!\)
give
\[
 \log\mu_k
 =k\left[L-\frac\ell2(k-1)-\log k+1\right]+O(\log k+k^2/n).
\]
The bracket is exactly \(\log(ML/k)+\ell t_n/2\), so
\(\log\mu_k=t_nL+O(\log L)\). Also, exactly,
\[
 \frac{\mu_{k-1}}{\mu_k}=\frac{k2^{k-1}}{n-k+1},\qquad
 2^k=\frac{e^2}{2}\,2^{-t_n}
                         \frac{n^2}{(\log_2n)^2}.        \tag{5}
\]
These prove (3), uniformly for \(0\le t_n<1\).

For \((K,l)\in\{(k,k),(k-1,k-1),(k,k-1)\}\), conditioning on a fixed
independent \(K\)-set gives the exact identity
\[
 \frac{\operatorname{Cov}(X_K,X_l)}{\mu_K}
 =\sum_{j=2}^l h_j(1-2^{-\binom j2}),\quad
 h_j=\binom Kj\binom{n-K}{l-j}
                    2^{-\binom l2+\binom j2}.            \tag{6}
\]
Indeed two sets sharing \(j\) vertices share precisely \(\binom j2\)
edge constraints. Their joint probability is \(q_Kq_l2^{\binom j2}\).
For \(j=0,1\) their covariance is zero. The last term has
\(h_l=\binom Kl\), equal to 1 for variances and \(k\) for the mixed pair.

For completeness, all the other terms obey
\[
 \sum_{j=2}^{l-1}h_j
 =O\left(\frac{\mu_l K^5}{n^2}
                         +h_lK^2n2^{-l}\right).          \tag{7}
\]
To see this, split at \(m=\lfloor l/2\rfloor\). For \(2\le j\le m\),
a union bound over \(j\)-subsets of the fixed \(K\)-set yields
\[
 h_j\le\mu_l\left(\frac{Kl}{n-l}\right)^j2^{j(j-1)/2}
       =\mu_lv_j.
\]
The logarithm of \(v_j\) is convex in \(j\), so the sum is at most
\(\mu_lm\max(v_2,v_m)\). With \(u=\log_2n\), we have
\(K,l=2u+O(\log u)\), \(m=u+O(\log u)\), and therefore
\[
 \log_2v_m=-u^2/2+O(u\log u),\qquad
 v_2=2(Kl/(n-l))^2=\Theta(K^4/n^2).
\]
Thus \(v_m\le v_2\) eventually, giving the first term in (7).
For \(j>m\), set \(s=l-j\). The exact ratio is
\[
 \frac{h_{l-s}}{h_l}
 =\frac{\binom K{l-s}}{\binom Kl}\binom{n-K}s
                       2^{-sl+s(s+1)/2}
 \le (Kn2^{-l})^s2^{s(s+1)/2}=:w_s.
\]
The binomial ratio is at most \(K^s\), both when \(K=l\) and when
\(K=l+1\); in the latter case it equals \(\binom{K-1}s/(s+1)\).
Again use convexity on \(1\le s\le m'=\lceil l/2\rceil\).
Here \(w_1=2Kn2^{-l}\), whereas
\(\log_2w_{m'}=-u^2/2+O(u\log u)\). Consequently \(w_{m'}\le w_1\)
eventually, and the sum is at most \(h_lm'w_1\), giving the second
term in (7). All these estimates are uniform in \(t_n\).

Since \(\mu_l\le n^{2-\delta+o(1)}\), (6) and (7) prove (4). They also
give
\[
 \epsilon_j
 =O\left(q_j+\frac{\mu_j k^5}{n^2}+k^2n2^{-j}\right)
 \le n^{-\delta+o(1)}\quad(j=k,k-1).                     \tag{8}
\]
Nonnegativity of \(\epsilon_j\) follows directly from (6), whose diagonal
is \(1-q_j\). Finally, (4) and (5) imply
\[
 c_n\sim k\sqrt{\mu_k/\mu_{k-1}}
   =\sqrt{\frac{k(n-k+1)}{2^{k-1}}}
   =O\left(\frac{(\log n)^{3/2}}{\sqrt n}\right).         \tag{9}
\]

## 2. A marginal bound from forcing one independent set

Fix \(j\ge2\), put \(X=X_j\), \(\mu=\mu_j\), \(q=q_j\), and let
\(A\) be a uniformly chosen \(j\)-subset, independently of the graph.
Delete all edges with both endpoints in \(A\), and denote the resulting
count by \(X^A\). For fixed \(A\), the altered graph has the conditional
law of the original graph given that \(A\) is independent: the remaining
edges retain their independent Bernoulli laws. Thus, for every function
\(g\),
\[
 \mathbb E[Xg(X)]
 =\sum_{|A|=j}q\,\mathbb E[g(X)\mid A\text{ independent}]
 =\mu\,\mathbb E g(X^A).                                 \tag{10}
\]
Let \(D=X^A-X\). Deleting edges cannot destroy an independent set, so
\(D\ge0\). If \(A\) was already independent, no edge changes and \(D=0\).
If it was not, at least \(A\) becomes a new independent set, so \(D\ge1\).
It follows that
\[
 \mathbb P(D=0)=q.
\]
Taking \(g(x)=x\) in (10),
\[
 \mathbb ED=\frac{\mathbb EX^2}{\mu}-\mu
           =\frac{\operatorname{Var}X}{\mu}.
\]
For every nonnegative integer \(d\),
\(|d-1|=d-1+2\mathbf1_{\{d=0\}}\). Consequently
\[
 \mathbb E|D-1|
 =\frac{\operatorname{Var}X}{\mu}-1+2q=\epsilon_j.         \tag{11}
\]

Let \(U=(X-\mu)/\sqrt\mu\) and \(\psi(z)=\mathbb Ee^{izU}\).
All variables have finite support, so differentiation under expectation
is valid. Equation (10) gives
\[
 \psi'(z)=i\sqrt\mu\,
      \mathbb E\left[e^{izU}(e^{izD/\sqrt\mu}-1)\right].
\]
The inequality \(|e^{ix}-e^{iy}|\le|x-y|\) and (11) show that
\[
 \psi'(z)=a(z)\psi(z)+r(z),\quad
 a(z)=i\sqrt\mu(e^{iz/\sqrt\mu}-1),\quad
 |r(z)|\le |z|\epsilon_j.                                \tag{12}
\]
Taylor's formula with its integral remainder gives
\(|e^{ix}-1-ix|\le x^2/2\), for every real \(x\). Hence
\(|a(z)+z|\le z^2/(2\sqrt\mu)\). Since \(|\psi(z)|\le1\),
\[
 |\psi'(z)+z\psi(z)|
 \le |z|\epsilon_j+\frac{z^2}{2\sqrt\mu}.                 \tag{13}
\]
For \(z\ge0\), solve this differential equation by the integrating
factor \(e^{z^2/2}\), using \(\psi(0)=1\). We obtain
\[
 \left|\psi(z)-e^{-z^2/2}\right|
 \le\int_0^z e^{-(z^2-v^2)/2}
                 \left(v\epsilon_j+\frac{v^2}{2\sqrt\mu}\right)dv
 \le\frac{z^2\epsilon_j}{2}+\frac{z^3}{6\sqrt\mu}.
\]
Conjugation gives the same bound for negative \(z\). Thus
\[
 \left|\mathbb Ee^{izU_j}-e^{-z^2/2}\right|
 \le\frac{z^2\epsilon_j}{2}+
                        \frac{|z|^3}{6\sqrt{\mu_j}}.     \tag{14}
\]
In particular each marginal has a standard normal limit by (3) and (8).
No Poisson approximation is assumed in this argument.

## 3. Positive association and the joint characteristic function

Write the graph in terms of independent missing-edge indicators. An
increasing function is one that cannot decrease when any such indicator
changes from zero to one. For increasing real functions \(F,G\) of
independent Bernoulli variables,
\[
 \operatorname{Cov}(F,G)\ge0.                             \tag{15}
\]
Here is a proof by induction on the number of variables. For one
Bernoulli variable of parameter \(p\), the covariance is
\(p(1-p)(F(1)-F(0))(G(1)-G(0))\ge0\). For more variables, condition on
the last one. The conditional covariance is nonnegative by induction.
The conditional means are increasing functions of the last variable,
so their covariance is nonnegative by the one-variable calculation.
The formula for total covariance proves (15).

Both counts, and hence both \(U_k,U_{k-1}\), are increasing functions.
If \(V,W\) are this pair, (15) applied to their upper-threshold events
shows that
\[
 H(x,y)=\mathbb P(V>x,W>y)
              -\mathbb P(V>x)\mathbb P(W>y)\ge0.          \tag{16}
\]
Choose finite intervals containing their supports. For differentiable
functions \(a,b\), use
\(a(V)=a(v_0)+\int a'(x)\mathbf1_{\{V>x\}}dx\), with the integral over
the chosen support interval; use the analogous identity for \(b(W)\).
Multiplication, expectation and subtraction give the bilinear covariance
identity
\[
 \mathbb E[a(V)b(W)]-\mathbb E a(V)\mathbb E b(W)
       =\iint a'(x)b'(y)H(x,y)\,dx\,dy.                  \tag{17}
\]
This identity also holds for complex \(a,b\); no complex conjugate is
used. All integrals are finite. Taking \(a(x)=x,b(y)=y\) identifies
\(\iint H=\operatorname{Cov}(V,W)\). Taking instead
\(a(x)=e^{isx},b(y)=e^{ity}\), using (16), gives
\[
 \left|\mathbb Ee^{i(sV+tW)}
          -\mathbb Ee^{isV}\mathbb Ee^{itW}\right|
       \le |st|\operatorname{Cov}(V,W)=|st|c_n.           \tag{18}
\]
Combining (18) with the two marginal bounds (14), and using that every
characteristic function has absolute value at most one, proves (2).

By (3), uniformly on the band,
\(\mu_k^{-1/2}\le n^{-\delta/2+o(1)}\) and
\(\mu_{k-1}^{-1/2}\le n^{-(1+\delta)/2+o(1)}\).
Equations (8) and (9) therefore imply the stated rate in (2). The
two-dimensional characteristic functions converge to
\(e^{-(s^2+t^2)/2}\), the characteristic function of two independent
standard normals. The continuity theorem for characteristic functions
proves (1). Uniformity follows from the estimates: every sequence of
integers in the band tending to infinity satisfies the same limit.

In particular, for all real \(x,y\),
\[
 \mathbb P(U_k\le x,U_{k-1}\le y)\longrightarrow\Phi(x)\Phi(y).
\]
The same conclusion holds if each count is divided by its actual standard
deviation, since (4) makes the two normalizations asymptotically equal.

## Scope

Annika Heckel and Oliver Riordan, *How does the chromatic number of a random
graph vary?*, [arXiv:2103.14014](https://arxiv.org/html/2103.14014), discusses
approximately Poisson marginals near equation (10). The result above
adds a joint Gaussian conclusion to the moment estimates in the preceding
local report. No novelty in the literature is asserted.

Neither the joint limit nor (2) identifies the conditional law of the
chromatic number given the counts. In particular, no bound on its
concentration width follows here. The fixed interior-band assumption is
used in (8); no endpoint-phase claim is made.
