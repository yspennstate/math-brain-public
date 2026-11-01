# HARD7-04 proof artifact: bounded three-point tree census gives the missing lower extreme

## Scope and status

This is a theorem-sized **PARTIAL** result toward the admitted source question `VDH-8.3-DUALITY`. It proves the sharp lower extreme for a clean deterministic barely-subcritical configuration-model subcase with degrees in `{1,2,3}`. It does **not** close van der Hofstad's full finite-third-moment discrete-duality question, and no novelty claim is made beyond the bounded current-literature check recorded in the run report.

Let the deterministic degree sequence have counts `n_1,n_2,n_3`, total half-edge count

\[
L_n=n_1+2n_2+3n_3,
\]

and empirical law `p_{r,n}=n_r/n`. Assume

\[
(p_{1,n},p_{2,n},p_{3,n})\to (3/8,1/2,1/8),
\]

`L_n` is even, and

\[
Q_n:=\frac{-n_1+3n_3}{L_n}=-\varepsilon_n<0,
\qquad \varepsilon_n\downarrow0,
\qquad N_n:=n\varepsilon_n^3\to\infty.
\]

The critical limiting mean and variance parameter are

\[
\mu_* = \frac74,
\qquad
R_*:=\frac{\mathbb E[D(D-2)^2]}{\mathbb ED}=\frac37.
\]

Let `L_1` be the largest component order of the configuration model on this degree sequence.

## Theorem

For every fixed `delta>0`,

\[
\mathbb P\!\left(
L_1 < (1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\right)\to0.
\]

Equivalently,

\[
L_1\ge (1-o_p(1))\frac{6}{7\varepsilon_n^2}\log(n\varepsilon_n^3).
\]

The proof uses exact tree-component enumeration plus a second moment. The key cancellation is the configuration-model analogue of the cancellation behind the classical Erdős--Rényi tree census.

---

## 1. Exact tree census

A tree component on `k` vertices with `a,b,c` vertices of degrees `1,2,3` must satisfy

\[
a+b+c=k,
\qquad a+2b+3c=2(k-1),
\]

hence necessarily

\[
a=c+2,
\qquad b=k-2c-2.
\tag{1.1}
\]

Let `X_{k,c}` be the number of tree components with this profile. For a fixed chosen vertex set of the prescribed degrees, the number of pairings of its half-edges that produce a tree equals

\[
\frac{(k-2)!}{\prod_v(d_v-1)!}\prod_v d_v!
=(k-2)!\prod_v d_v
=(k-2)!2^b3^c.
\]

After those `2(k-1)` half-edges are paired internally, the remaining half-edges may be paired arbitrarily. Therefore

\[
\boxed{
\mathbb E X_{k,c}
=inom{n_1}{c+2}
 \binom{n_2}{k-2c-2}
 \binom{n_3}{c}
 (k-2)!2^{k-2c-2}3^c
 \frac{(L_n-2k+1)!!}{(L_n-1)!!}.
}
\tag{1.2}
\]

This identity is exact.

The finite checker archived with this run brute-forces every pairing for four small degree sequences and verifies (1.2) exactly with rational arithmetic.

---

## 2. Size-biased reformulation and the Cramér point

Set

\[
q_{r,n}:=\frac{r n_r}{L_n},\qquad r=1,2,3.
\]

If `D_n^*` has law `q_{r,n}`, then

\[
\mathbb E D_n^*=2+Q_n=2-\varepsilon_n.
\]

For a profile `m=(m_1,m_2,m_3)` satisfying `m_1+m_2+m_3=k` and `m_1+2m_2+3m_3=2k-2`, write

\[
\Pi_n(m):=rac{k!}{m_1!m_2!m_3!}
\prod_{r=1}^3 q_{r,n}^{m_r}.
\]

From (1.2),

\[
\mathbb E X_m
=\frac{L_n}{k(k-1)}\Pi_n(m)F_n(m),
\tag{2.1}
\]

where

\[
F_n(m)
=\prod_{r=1}^3\frac{(n_r)_{m_r}}{n_r^{m_r}}
\prod_{j=0}^{k-2}\frac{L_n}{L_n-(2j+1)}.
\tag{2.2}
\]

Thus the infinite-population part of the tree census is exactly the local large-deviation probability that `k` iid size-biased degrees have sum `2k-2`.

Let

\[
M_n(\lambda)=\mathbb E e^{\lambda(D_n^*-2)}.
\]

Since the limiting law has all three atoms positive, there is for all large `n` a unique `\lambda_n>0` with

\[
\frac{d}{d\lambda}\log M_n(\lambda_n)=0.
\]

Define

\[
I_n:=-\log M_n(\lambda_n).
\]

The cumulant expansion gives

\[
\lambda_n=\frac{\varepsilon_n}{R_*}+o(\varepsilon_n),
\qquad
I_n=\frac{\varepsilon_n^2}{2R_*}+o(\varepsilon_n^2).
\tag{2.3}
\]

Indeed `K_n'(0)=-\varepsilon_n`, while `K_n''(0)\to R_*=3/7`.

Under the tilted law

\[
\alpha_{r,n}:=
\frac{q_{r,n}e^{\lambda_n(r-2)}}{M_n(\lambda_n)},
\]

the mean degree is exactly `2`. Hence, because the support is `{1,2,3}`,

\[
\alpha_{1,n}=\alpha_{3,n}=:x_n,
\qquad
\alpha_{2,n}=1-2x_n,
\tag{2.4}
\]

with `x_n\to3/14`.

A uniform finite-support lattice local CLT applies to this triangular family: the three tilted atom probabilities stay bounded away from zero and the span is one. Consequently, for every fixed sufficiently large `A`, if `G_k` denotes the set of profiles satisfying the tree constraint and

\[
|m_r-k\alpha_{r,n}|\le A\sqrt{k}+2
\quad(r=1,2,3),
\]
then uniformly for the `k` used below,

\[
\sum_{m\in G_k}\Pi_n(m)
\ge c k^{-1/2}e^{-kI_n}
\tag{2.5}
\]

for some `c>0` independent of `n,k`.

For completeness, (2.5) follows directly by exponential tilting. On the event `\sum D_i^*=2k-2`, the likelihood ratio from `q_n` to `\alpha_n` is the constant `\exp(-kI_n+2\lambda_n)`. Under `\alpha_n`, the centered variable `D^*-2` has three atoms `-1,0,1`, variance bounded above and below, and span one. Fourier inversion, splitting `|t|\le k^{-2/5}` from its complement, gives a uniform `c k^{-1/2}` lower bound for the atom at `-2`; the same Gaussian window estimate places a fixed positive fraction of that atom inside `G_k`.

---

## 3. Finite-population cancellation

For `m\in G_k`, expand (2.2). Since `k=o(n^{2/3})` in the regime used below,

\[
\log F_n(m)
= -\frac12\sum_{r=1}^3\frac{m_r(m_r-1)}{n_r}
  +\frac{(k-1)^2}{L_n}
  +O\!\left(\frac{k^3}{n^2}+\frac{k}{n}\right).
\tag{3.1}
\]

Write `p_{r,n}=n_r/n`, `\mu_n=L_n/n`, and `m_r=k\alpha_{r,n}+O(\sqrt{k})`. Then

\[
\log F_n(m)
=\frac{k^2}{n}
\left[
\frac1{\mu_n}
-\frac12\sum_{r=1}^3\frac{\alpha_{r,n}^2}{p_{r,n}}
\right]
+O\!\left(
\frac{k^{3/2}}n+rac{k^3}{n^2}+\frac{k}{n}
\right).
\tag{3.2}
\]

The bracket is `O(\varepsilon_n)`. To see the structural cancellation, first use the untilted size-biased vector `q_{r,n}=r p_{r,n}/\mu_n`:

\[
\sum_r\frac{q_{r,n}^2}{p_{r,n}}
=\frac{\mathbb E D_n^2}{\mu_n^2}
=\frac{2+Q_n}{\mu_n}
=\frac{2-\varepsilon_n}{\mu_n}.
\tag{3.3}
\]

Hence

\[
\frac1{\mu_n}-\frac12\sum_r\frac{q_{r,n}^2}{p_{r,n}}
=\frac{\varepsilon_n}{2\mu_n}.
\tag{3.4}
\]

Since `\alpha_n-q_n=O(\varepsilon_n)`, (3.4) yields the claimed `O(\varepsilon_n)` bracket. At the critical limit this is the exact identity

\[
\sum_r\frac{q_r^2}{p_r}=\frac2\mu.
\tag{3.5}
\]

For `(p_1,p_2,p_3)=(3/8,1/2,1/8)`, `\mu=7/4`, `q=(3/14,4/7,3/14)`, and both sides of (3.5) equal `8/7`; this exact rational identity is also checked by the archived script.

Now take

\[
k\asymp \varepsilon_n^{-2}\log N_n.
\]

Then

\[
\frac{\varepsilon_n k^2}{n}=O\!\left(\frac{(\log N_n)^2}{N_n}\right)=o(1),
\]

\[
\frac{k^{3/2}}n=O\!\left(\frac{(\log N_n)^{3/2}}{N_n}\right)=o(1),
\qquad
\frac{k^3}{n^2}=O\!\left(\frac{(\log N_n)^3}{N_n^2}\right)=o(1).
\]

Therefore

\[
\boxed{F_n(m)=1+o(1)}
\tag{3.6}
\]

uniformly for `m\in G_k` and for all `k` in the window used below.

Combining (2.1), (2.5), and (3.6), if `T_k` is the number of good tree components of order `k`, then

\[
\boxed{
\mathbb E T_k\ge c_1 n k^{-5/2}e^{-I_n k}.
}
\tag{3.7}
\]

---

## 4. A window contains many candidate components in expectation

Fix `\delta>0` and set

\[
K_n=\left\lfloor
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\right\rfloor,
\qquad
J_n=\left\lfloor\varepsilon_n^{-2}\right\rfloor.
\]

Let

\[
Z_n:=\sum_{k=K_n}^{K_n+J_n}T_k.
\]

Since `I_nJ_n=O(1)` and `K_n\asymp\varepsilon_n^{-2}\log N_n`, (3.7) gives

\[
\mathbb E Z_n
\ge c_2 J_n n K_n^{-5/2}e^{-I_n(K_n+J_n)}.
\]

Using `n\varepsilon_n^3=N_n` and (2.3),

\[
J_n n K_n^{-5/2}
\asymp
\frac{N_n}{(\log N_n)^{5/2}},
\]

while

\[
I_nK_n=(1-\delta+o(1))\log N_n.
\]

Hence

\[
\boxed{
\mathbb E Z_n
\ge \frac{N_n^{\delta+o(1)}}{(\log N_n)^{5/2}}
\longrightarrow\infty.
}
\tag{4.1}
\]

The `J_n\asymp\varepsilon_n^{-2}` size window is essential: counting a single exact size loses precisely the factor needed in the most slowly barely-subcritical regimes.

---

## 5. Exact two-component ratio and decorrelation

Take two good profiles `m,m'` of sizes `k,\ell`. Two distinct tree components must be vertex-disjoint. Comparing the exact joint tree count with the product of the two one-component counts gives

\[
\frac{\mathbb E[X_m X_{m'};\,\text{distinct components}]}{
\mathbb E X_m\,\mathbb E X_{m'}}
=V_n(m,m')P_n(k,\ell),
\tag{5.1}
\]

where

\[
V_n(m,m')
=\prod_{r=1}^3
\frac{(n_r)_{m_r+m'_r}}{(n_r)_{m_r}(n_r)_{m'_r}},
\]

and

\[
P_n(k,\ell)
=\frac{(L_n-2k-2\ell+3)!!(L_n-1)!!}
{(L_n-2k+1)!!(L_n-2\ell+1)!!}.
\]

Taylor expansion gives

\[
\log V_n(m,m')
=-\sum_r\frac{m_rm'_r}{n_r}
+O\!\left(\frac{k\ell(k+\ell)}{n^2}\right),
\tag{5.2}
\]

\[
\log P_n(k,\ell)
=\frac{2(k-1)(\ell-1)}{L_n}
+O\!\left(\frac{k\ell(k+\ell)}{n^2}\right).
\tag{5.3}
\]

Thus

\[
\log(V_nP_n)
=\frac{k\ell}{n}
\left[
\frac2{\mu_n}
-\sum_r\frac{\alpha_{r,n}^2}{p_{r,n}}
\right]
+O\!\left(
\frac{k\ell}{n\sqrt{k}}+
\frac{k\ell}{n\sqrt{\ell}}+
\frac{k\ell(k+\ell)}{n^2}
\right).
\tag{5.4}
\]

The bracket in (5.4) is `O(\varepsilon_n)` by the same critical cancellation as in Section 3. Uniformly for `k,\ell\in[K_n,K_n+J_n]`,

\[
\frac{\varepsilon_n k\ell}{n}
=O\!\left(\frac{(\log N_n)^2}{N_n}\right)=o(1),
\]

and the profile/error terms are respectively `O((\log N_n)^{3/2}/N_n)` and `O((\log N_n)^3/N_n^2)`. Hence

\[
\boxed{
V_n(m,m')P_n(k,\ell)=1+o(1)
}
\tag{5.5}
\]

uniformly over all good pairs.

Summing (5.1) over all good profile/size pairs yields

\[
\mathbb E[Z_n(Z_n-1)]
\le (1+o(1))(\mathbb E Z_n)^2.
\tag{5.6}
\]

Consequently

\[
\frac{\operatorname{Var}Z_n}{(\mathbb E Z_n)^2}
\le \frac1{\mathbb E Z_n}+o(1)\to0.
\]

Therefore

\[
\mathbb P(Z_n=0)\to0.
\]

With high probability there is a tree component of order at least `K_n`, proving the theorem.

---

## 6. What this does and does not resolve

This proves the exact lower leading constant for the simplest bounded three-point subcritical degree array singled out in the preceding STUCK1 report. The mechanism is now explicit:

1. exact tree enumeration;
2. size-biased Cramér tilting;
3. a critical first-order cancellation between sampling without replacement and pairing depletion;
4. a size window of width `Theta(epsilon^{-2})`;
5. a second-moment ratio whose leading `k ell/n` term cancels for the same reason.

The full source question remains open on this track because the exact post-giant residual sequence need not have bounded support. Extending the argument requires a uniform truncation/exponential-collar version of Sections 2--5 that allows residual degrees up to the sharp scale `O(epsilon^{-1} log N)` without losing the local lower estimate or the second-moment cancellation.

No closure or audit claim is made.
