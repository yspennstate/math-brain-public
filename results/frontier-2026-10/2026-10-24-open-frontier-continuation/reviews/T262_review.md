# Referee check of the localized T262 generator lemma

**Verdict: the compact-state, clipped one-step proposition is sound, subject to two explicit formalizations below.** I checked the claimed rates in [T262_generator.md](../research/T262_generator.md), especially the $O(n^{-3/2})$ expectation remainders, the polynomially small bad event, and the conditional chi-square identities. This review does not assess entrance, compact containment over $O(n)$ steps outside the stopped regime, or the norm coordinate.

## Rate audit

Uniformly for $u\in[\delta,K]$, $\theta=c/n$ with $c\in[1/K,1/\delta]$. A Gaussian pair $(a,h)$ has polar radius $\rho$ independent of direction; the sign-disagreement wedge has probability $\theta/\pi$. Thus $S=\sum_i\rho_i^2{\bf1}_{F_i}$ has **all fixed moments $O(1)$**: each distinct-index term in its $p$th moment has order $(n\theta)^j$, $j\le p$. This justifies $J\le\theta^2 S$, $\|N_0/\sin^2\theta\|_p=O(1)$, $\|\Xi_0{\bf1}_B\|_p=O(n^{-1})$, and the $O(n^{-p})$ Markov bound for $S>n/1000$ for every chosen integer $p$. The binomial, conditional chi-square, and Gaussian components of $B^c$ have exponential tails. The dependence of $S$ on $q,V,H$ is immaterial to this union bound.

On $B$, $q,V\asymp n$ and $D=\sin^2\theta V\asymp n^{-1}$. Since $\langle X,Z\rangle=(\cos\theta-1)q+\sin\theta H$ has $L^p$ size $O(n^{-1/2})$ and $|\langle X,r\rangle|\le J$ has $L^p$ size $O(n^{-2})$, the projected numerator correction is $O_{L^p}(n^{-7/2})$ after division by $q$, and therefore

$$
\|(\Xi-\Xi_0){\bf1}_B\|_p=O(n^{-5/2}).
$$

These estimates require Hölder with moments of twice the target order; those moments are available. The bound $|\Xi|<1/2$ on $B$ follows deterministically from $|N_0|\le3\theta^2S$, $V\ge n/4$, and $S\le n/1000$ (the small projection correction can be absorbed), so the reciprocal Taylor expansion is legitimate.

The exact ReLU covariance calculation gives $\mathbb EN_0=n(\theta\cos\theta-\sin\theta)/\pi=-n\theta^3/(3\pi)+O(n\theta^5)$. Here $\|V-n/2\|_2=O(\sqrt n)$, so on $B$, $\|(1/V-2/n){\bf1}_B\|_2=O(n^{-3/2})$. Cauchy–Schwarz with $\|N_0/\sin^2\theta\|_2=O(1)$ establishes the **claimed $O(n^{-3/2})$ denominator-correlation error** without pretending numerator and denominator are independent. In particular

$$
\mathbb E[\Xi{\bf1}_B]=-\frac{2\theta}{3\pi}+O(n^{-3/2}).
$$

The longitudinal ratio $M=\langle X,Z+r\rangle/q$ has $L^p$ norm $O(n^{-3/2})$ on $B$: $\sin\theta\,H/q=O_{L^p}(n^{-3/2})$, $\cos\theta-1=O(n^{-2})$, and $\langle X,r\rangle/q=O_{L^p}(n^{-3})$. With $\|R^{-1}-1\|_{L^p(B)}=O(n^{-1/2})$ and $\|\Xi\|_{L^p(B)}=O(n^{-1})$, the omitted product $(R^{-1}-1)\Xi$ is $O_{L^p}(n^{-3/2})$, as are the $M$ term and smaller Taylor terms. The $L^3$ remainder suffices for the third absolute moment.

## Conditional moments and deletion of the bad set

Conditional on $k=|\{a_i>0\}|$, the positive Gaussian squares sum to $q\sim\chi_k^2$. Conditional on the entire $X$, orthogonal projection of the independent Gaussian $h_A$ gives $V\sim\chi_{k-1}^2$, with its law independent of $X$; hence $q$ and $V$ are independent given $k$. Their gamma-function moments yield exactly

$$
\mathbb E(R^{-1}-1\mid k)=\frac1{k-2},\qquad
\mathbb E((R^{-1}-1)^2\mid k)=\frac{k}{(k-3)(k-2)}
$$

for $k>3$. Since central $k$ differs from $n/2$ by $O_{L^p}(\sqrt n)$, the averages are $2/n+O(n^{-2})$. Deleting $B^c$ is harmless **only after restricting first to central $k\ge n/3$**: for $k\le3$ the untruncated inverse moments may not exist. On central $k$, fixed high moments of $R^{-1}$ are uniformly bounded for large $n$; Hölder and the arbitrarily high-power bound on $\mathbb P(B^c)$ then make the deletion error smaller than any prescribed power of $n$. This is how the proof's sentence about deletion should be read.

The three localized moment assertions follow: mean $u(2/n+\theta/(3\pi))+O(n^{-3/2})$, second moment $2u^2/n+O(n^{-3/2})$, and third absolute moment $O(n^{-3/2})$. Since $u\theta=1/n$, the extra drift is $1/(3\pi)$, and the stated generator follows by third-order Taylor. No unjustified independence was used in the flip calculation.

## Minor formal edits before reuse

1. Define $P,V,R$ only on $q>0$ and $k$ large enough, or give arbitrary values outside $B$; $q=0$ has positive (exponentially small) probability, so the current initial definition $P=I-XX^\top/q$ is formally undefined there. The clipped transition itself is well defined.
2. In the proof of (5), explicitly record $\|R^{-1}-1\|_{L^p(B)}=O(n^{-1/2})$ for the Hölder exponents used (e.g. $p=6$ or higher), rather than relying only on the later $L^3$ line. Standard central chi-square moment bounds give it.
3. State the $B^c$ deletion of (6) as a **central-$k$ truncated** expectation to avoid invoking nonexistent inverse moments for small $k$.

These are presentation and domain-of-definition repairs, not changes to the proposition. The proof remains a stopped local generator calculation; it cannot by itself establish the full T262 angle limit.
