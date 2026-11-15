# Deterministic diagonal QUE from delocalization and label symmetry

## Statement

Let \(B_N\) be a real symmetric random \(N\times N\) matrix whose law is invariant under conjugation by permutation matrices. Suppose that, outside an event of probability \(\varepsilon_N\), every unit eigenvector \(u\), including every unit vector in each repeated eigenspace, obeys
\[
 \|u\|_\infty\le L_N/\sqrt N,\qquad L_N\ge1.
 \tag{1}
\]
For each deterministic \(a\in[-1,1]^N\) with \(\sum_i a_i=0\), and every \(s>0\),
\[
 \mathbb P\left\{
  \sup_{\substack{B_Nu=\lambda u\\\|u\|_2=1}}
       \left|\sum_i a_i|u_i|^2\right|>s
 \right\}
 \le \varepsilon_N+2N^2
       \exp\left(-\frac{Ns^2}{32L_N^8}\right).
 \tag{2}
\]
In particular, for any \(D>0\), the supremum is at most
\[
 s_N=L_N^4\sqrt{\frac{32(D+2)\log N}{N}}
 \tag{3}
\]
with probability at least \(1-\varepsilon_N-2N^{-D}\). This tends to zero if \(L_N\) is a fixed power of \(\log N\) and \(\varepsilon_N\to0\). The test may depend on \(N\), but is chosen before the random matrix. No simplicity-of-spectrum assumption is made.

## 1. Permutation concentration

Fix real weights \(w_1,\ldots,w_N\) with \(|w_i|\le b\), and let \(\pi\) be a uniform permutation. Put
\[
 X_i=a_{\pi(i)},\qquad S=\sum_i w_iX_i.
\]
Each \(X_i\) has mean zero, so \(\mathbb ES=0\). Reveal \(X_1,\ldots,X_N\), retaining the sampled indices in the filtration if the values repeat, and write \(M_k=\mathbb E[S\mid\mathcal F_k]\).

Immediately before the \(k\)-th reveal let \(r=N-k+1\), let \(\mu\) be the mean of the \(r\) remaining values, and let \(W=\sum_{i=k}^Nw_i\). If the next revealed value is \(x\), the new remaining mean is \((r\mu-x)/(r-1)\), provided \(r\ge2\). Subtracting the two conditional expectations gives exactly
\[
 M_k-M_{k-1}
  =(x-\mu)\left(w_k-\frac{W-w_k}{r-1}\right).
 \tag{4}
\]
The first factor has absolute value at most 2. The average of the other weights lies in \([-b,b]\), so the second factor has absolute value at most \(2b\). Thus \(|M_k-M_{k-1}|\le4b\). The final reveal contributes zero because its value is already determined.

For completeness, a mean-zero random variable \(Y\) bounded by \(c\) in absolute value satisfies
\[
 \mathbb E e^{\theta Y}\le\cosh(\theta c)
                    \le e^{\theta^2c^2/2}.
\]
The first inequality follows from the secant bound for the exponential on \([-c,c]\) and \(\mathbb EY=0\); the second follows by integrating \(\tanh x\le x\) for \(x\ge0\) and using evenness. Apply this conditionally to the martingale differences, with \(c=4b\), and iterate. Then
\[
 \mathbb E e^{\theta S}\le e^{8Nb^2\theta^2}.
\]
Exponential Markov inequality, minimized at \(\theta=t/(16Nb^2)\), gives
\[
 \mathbb P\{|S|>t\}
 \le 2\exp\left(-\frac{t^2}{32Nb^2}\right).
 \tag{5}
\]
For \(b=0\), \(S=0\) and the assertion is immediate.

## 2. Multiplicities

Fix a matrix \(B\) satisfying (1), and an eigenspace \(V_\lambda\) of dimension \(m_\lambda\). Let \(Q_\lambda\) be its orthogonal projection. For each coordinate,
\[
 Q_\lambda(i,i)
  =\sup_{u\in V_\lambda,\ \|u\|_2=1}|u_i|^2
  \le L_N^2/N.
\]
Indeed \(u_i=\langle Q_\lambda e_i,u\rangle\), and equality in the supremum is achieved by normalizing \(Q_\lambda e_i\) when it is nonzero. Taking the trace proves
\[
 m_\lambda\le L_N^2.
 \tag{6}
\]

Choose any real orthonormal basis \(v_{\lambda,1},\ldots,v_{\lambda,m_\lambda}\) of this fixed eigenspace. No rule for making this choice commute with permutations is needed. Define the symmetric compressed matrix
\[
 T_\lambda(\pi)_{\alpha\beta}
 =\sum_i a_{\pi(i)}v_{\lambda,\alpha}(i)v_{\lambda,\beta}(i).
\]
The weights in each entry have absolute value at most \(L_N^2/N\), by (1). Equation (5), with \(b=L_N^2/N\), therefore gives
\[
 \mathbb P_\pi\{|T_\lambda(\pi)_{\alpha\beta}|>t\}
 \le2\exp\left(-\frac{Nt^2}{32L_N^4}\right).
\]
There are \(\sum_\lambda m_\lambda^2\le(\sum_\lambda m_\lambda)^2=N^2\) entries across all eigenspaces. Except on an event of probability at most
\[
 2N^2\exp\left(-\frac{Nt^2}{32L_N^4}\right),
 \tag{7}
\]
all entries have absolute value at most \(t\). On this event, for every unit coefficient vector \(z\),
\[
 |z^*T_\lambda z|
 \le t\left(\sum_\alpha|z_\alpha|\right)^2
 \le m_\lambda t\le L_N^2t.
 \tag{8}
\]
The same bound holds for real and complex \(z\). It controls every unit eigenvector in the eigenspace, rather than just the chosen basis.

## 3. Return to the random matrix

Let \(P_\pi e_i=e_{\pi(i)}\). If \(Bu=\lambda u\), then \(P_\pi u\) is an eigenvector of \(P_\pi BP_\pi^{\mathsf T}\), and its observable is \(\sum_i a_{\pi(i)}|u_i|^2\). Thus (7)–(8), with \(t=s/L_N^2\), bound the probability of failure for a random relabeling of every fixed good \(B\) by the second term of (2).

Now sample \(B_N\), independently sample \(\pi\), and average this conditional estimate over \(B_N\). Bad \(B_N\) contribute at most \(\varepsilon_N\). Permutation invariance identifies the law of \(P_\pi B_NP_\pi^{\mathsf T}\) with that of \(B_N\). This proves (2). Substituting (3) makes its second term exactly \(2N^{-D}\).

## 4. Application to fixed-degree random regular graphs

Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [arXiv:2102.00963v3](https://arxiv.org/html/2102.00963v3), Theorem 1.4, supplies (1), with \(L_N\) a fixed power of \(\log N\) and \(\varepsilon_N=o(1)\), for every fixed \(d\ge3\). Its conditional tree-like-graph statement is combined with the probability of that graph event as explained immediately after the theorem. Normalizing adjacency by \(\sqrt{d-1}\) leaves eigenvectors unchanged. Uniform simple labelled random regular graphs have permutation-invariant law.

Consequently, for every deterministic sequence \(a_N\in[-1,1]^N\) with zero mean and every \(\delta>0\),
\[
 \mathbb P\left\{
 \sup_{\substack{A_Nu=\lambda u\\\|u\|_2=1}}
 \left|\sum_i a_N(i)|u_i|^2\right|
       >N^{-1/2+\delta}\right\}\longrightarrow0.
 \tag{9}
\]
This holds for all eigenvectors, and hence in particular for the bulk. For an arbitrary deterministic bounded real \(a_N\), subtract its spatial mean and rescale its supremum norm. The resulting conclusion is
\[
 \sup_{\substack{A_Nu=\lambda u\\\|u\|_2=1}}
 \left|\sum_i a_N(i)|u_i|^2-\frac1N\sum_i a_N(i)\right|
 \xrightarrow{\mathbb P}0.
 \tag{10}
\]
This is probabilistic diagonal QUE for prescribed deterministic vertex observables. It follows from the cited delocalization theorem and label symmetry; it does not use the OpenAI manuscripts. It is not an assertion of novelty. The unconditional error probability retains the exceptional-graph term \(\varepsilon_N\).

## 5. Independent checks and limits of the conclusion

**Variance check.** For the scalar permutation sum, put \(\sigma_a^2=N^{-1}\sum_i a_i^2\). Since \(\sum_iX_i=0\) and the coordinates are exchangeable,
\[
 \mathbb EX_i^2=\sigma_a^2,\qquad
 \mathbb EX_iX_j=-\frac{\sigma_a^2}{N-1}\quad(i\ne j).
\]
Expanding the square independently of the martingale proof yields
\[
 \operatorname{Var}S
  =\frac{\sigma_a^2}{N-1}
     \left(N\sum_iw_i^2-\left(\sum_iw_i\right)^2\right).
 \tag{11}
\]
This vanishes for constant weights, as it must. For an eigenspace-entry weight \(w_i=v_\alpha(i)v_\beta(i)\), Cauchy–Schwarz gives \(\sum_i|w_i|\le1\) and hence \(\sum_iw_i^2\le L_N^2/N\). The variance is at most \(\sigma_a^2 L_N^2/(N-1)\). Bound (5) is weaker by a polylogarithmic factor, consistently with (3).

**Projection check.** In a basis matrix \(U\) of an eigenspace, \(Q=UU^{\mathsf T}\), so \(Q(i,i)=\sum_\alpha|v_\alpha(i)|^2\). This gives the same trace \(m\) as (6). The bound in (6) requires (1) for every vector in the eigenspace; a coordinate bound on an arbitrarily chosen basis alone would not suffice.

**Uniformity over tests fails from these hypotheses.** For even \(N\), let \(u_i=\sqrt{2/N}\) on the first half of the coordinates and zero on the rest. Then \(\|u\|_\infty=\sqrt{2/N}\), but the mean-zero bounded test equal to 1 on that half and -1 elsewhere has \(\sum_i a_i|u_i|^2=1\). After a random relabeling, the same construction chooses its test from the relabeled support. Thus delocalization and label randomization cannot control an arbitrary vector-dependent test. The example concerns the abstract implication, not a claimed eigenvector of a random regular graph. General graph-dependent observables, off-diagonal observables, Gaussian-wave limits and relative equidistribution on shrinking sets are not established by (10).

**Constants.** The increment bound is \(2\cdot2b=4b\); its exponential bound has denominator \(2N(4b)^2=32Nb^2\). The substitution \(b=L_N^2/N\) produces \(32L_N^4/N\). Passing from entries to all vectors multiplies the threshold by at most \(m_\lambda\le L_N^2\), yielding the \(L_N^8\) in (2). Finally \(2N^2e^{-(D+2)\log N}=2N^{-D}\). No sharp constant or optimal logarithmic power is asserted.
