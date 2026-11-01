# Reversible nonconstant kernels: derivations, limits, and research targets

12 October 2026. Intermediate extension research. This note is separate from the existing paper. Results are labeled according to what is established here, inherited from the existing proof, or already in the literature. No general novelty claim is made.

## 1. Rate conventions

The state is an integer partition encoded by counts m_j >= 0 with sum j m_j = n. Put K(m) = sum m_j. A merger always concerns an unordered pair of distinct cluster instances, including distinct instances of the same size.

The original rates are 2/n per cluster pair and beta per internal link. For unequal sizes i,j this gives coarse merger 2m_i m_j/n and split 2 beta m_{i+j}. For equal sizes it gives m_i(m_i-1)/n and beta m_{2i}. These equal-size factors must be retained in every extension.

The original reversible law is
\[
\pi_0(m)=Z_0^{-1}\frac{(\beta n)^{K(m)}}{\prod_jm_j!}.
\]
The proved original comparison is
\[
\frac16\left(\beta+\sqrt\beta+\frac1n\right)
\le\gamma_0\le
4\left(\beta+\sqrt\beta+\frac1n\right).
\]
The extension project's sharper count proof further identifies gamma_0 with the count gap. The elementary kernel comparisons below do not depend on that stronger identity.

## 2. Common symmetric multipliers

Let c_n(i,j)>0 be symmetric. Multiply BOTH directions of each i,j reaction by c_n(i,j):

- Per cluster-pair merger: 2c_n(i,j)/n.
- Per internal link producing i,j: beta c_n(i,j).

The stationary law is exactly pi_0. Every detailed-balance equality is preserved edge by edge. If c_- <= c_n(i,j) <= c_+, then
\[
c_-\mathcal E_0(f,f)\le\mathcal E_c(f,f)\le c_+\mathcal E_0(f,f),
\qquad
c_-\gamma_0\le\gamma_c\le c_+\gamma_0.
\]
This includes arbitrary symmetric multipliers on complete state-space edges, not just functions of reacting sizes. It is a routine comparison theorem. The conclusion has uniform constants only when its assumed multiplier bounds have uniform constants.

### 2.1 The exact stationary cycle lift survives

For a nonempty set S of cut bonds on a circle, let k=|S|. At a boundary separating segments i,j, delete it at rate
\[
\frac{k-1}{n}c_n(i,j).
\]
At a link whose removal would split a segment into i,j, add the cut at rate beta c_n(i,j). The cut stationary law remains
\[
\pi_B(S)\propto\frac{(\beta n)^k}{(k-1)!}.
\]
The common multiplier cancels in each detailed-balance ratio.

For a multiset m with k components, the number of cut sets is
\[
\frac{n(k-1)!}{\prod_jm_j!}.
\]
Conditional on m, the cyclic multiset order is uniform. The expected number of boundaries separating i,j is 2m_i m_j/(k-1) when i differs from j, and m_i(m_i-1)/(k-1) otherwise. Multiplying by (k-1)c_n(i,j)/n gives the desired merger rate. When k=2, the two clusters share two distinct cut boundaries; the same formula remains valid.

Thus the pushforward law, variance identity, and stationary Dirichlet-form identity all remain exact for arbitrary positive c_n, including growing kernels. This is a stationary conditional-generator identity. It does not assert strong lumpability of the cyclic configuration process.

### 2.2 The harmonic reduction does not generally survive

Take n=4 and c(i,j)=i+j. A configuration with segment lengths (1,3) has total birth rate 6 beta; one with (2,2) has total birth rate 4 beta. Both have two cuts and total death rate 2. Therefore
\[
L_BK(1,3)=6\beta-2,\qquad
L_BK(2,2)=4\beta-2.
\]
Even the radial subspace of functions of K fails to be invariant. The original one-dimensional Boolean harmonic operators cannot simply be reused.

The original polynomial harmonic decomposition as a vector-space decomposition still exists; what fails is invariance of those subspaces under this new generator. The issue is not that every loss of full permutation invariance destroys the decomposition: unconditional permutation jumps, as in the spatial and nonreversible extensions, preserve each harmonic degree by equivariance. The size-dependent flip rates here need not do so.

## 3. General Gibbs weights and an exact weighted lift

Let w_j>0, theta=beta n, and let A(i,j)>0 be symmetric. Define
\[
\pi_w(m)=Z_w^{-1}
 \frac{\theta^{K(m)}\prod_jw_j^{m_j}}{\prod_jm_j!}.
\]
Choose the following rates:
\[
\text{merger per pair }=\frac{2A(i,j)}n,\qquad
\text{fragmentation per link }
 =\beta A(i,j)\frac{w_iw_j}{w_{i+j}}.
\]
For i<j the reverse coarse split is twice the displayed link rate times m_{i+j}; for i=j it is the displayed rate times m_{2i}.

### 3.1 Detailed balance

Suppose m' is obtained by merging unequal sizes i,j. Then
\[
\frac{\pi_w(m')}{\pi_w(m)}
=\theta^{-1}
  \frac{w_{i+j}}{w_iw_j}
  \frac{m_i m_j}{m_{i+j}+1}.
\]
Multiplying the reverse rate
2 beta A(i,j)(w_iw_j/w_{i+j})(m_{i+j}+1)
by this ratio gives 2A(i,j)m_i m_j/n, exactly the forward rate.
For equal sizes the same calculation yields the factor
m_i(m_i-1) and the single central split, with the same equality.

### 3.2 Weighted cycle construction

On nonempty cut sets use
\[
\pi_B^w(S)\propto
 \frac{\theta^{|S|}}{(|S|-1)!}
 \prod_{\text{cyclic segments }C}w_{|C|}.
\]
Delete the boundary separating i,j at rate
(k-1)A(i,j)/n. Add a cut producing i,j at rate
beta A(i,j) w_iw_j/w_{i+j}.

The ratio of the stationary weights when a cut is added at size k is
\[
\frac{\theta}{k}\frac{w_iw_j}{w_{i+j}},
\]
which is exactly birth rate divided by reverse death rate.
The number of configurations mapping to m is unchanged. Conditional cyclic order is still uniform because the product of the segment weights depends only on m. Therefore this lift pushes forward to pi_w and gives the exact polymer variance and Dirichlet identities.

For general w, the stationary measure is no longer uniform on a cardinality layer. In addition to the failure of generator invariance, the original harmonic orthogonality in the stationary inner product need not hold.

### 3.3 Bounded total potential comparison

Let (v_j,A_ref) be any reference Gibbs model at the same beta,n. Put
\[
V(m)=\sum_jm_j\log(w_j/v_j),\qquad
B=\max_mV(m)-\min_mV(m).
\]
Assume c_- <= A(i,j)/A_ref(i,j) <= c_+. Then
\[
c_-e^{-B}\gamma_{\rm ref}
\le\gamma_w\le c_+e^B\gamma_{\rm ref}.
\]

Proof: let rho=pi_w/pi_ref, whose maximum-to-minimum ratio is e^B. Orient every undirected reaction edge in the merger direction, from m to m'. Its conductance ratio is
\[
\frac{\pi_w(m)q_w(m,m')}{\pi_{\rm ref}(m)q_{\rm ref}(m,m')}
=\rho(m)\frac{A(i,j)}{A_{\rm ref}(i,j)}.
\]
Thus the Dirichlet forms compare using rho_min c_- and rho_max c_+.
The variances compare using rho_min and rho_max, since variance is the minimum over constants of the mean square deviation. Combining these estimates proves the claim.

A bound on each individual log(w_j/v_j) by a fixed constant does not make B dimension independent: there can be up to n clusters. Multiplying every w_j by exp(a j) has no effect on a fixed-mass law, and this gauge freedom can be used before calculating B.

## 4. Two explicit obstructions

### 4.1 Changing only the coagulation kernel can destroy reversibility

Keep fragmentation equal to beta per link but replace coagulation by 2A(i,j)/n. Consider n=4 and the cycle
\[
(2,1,1)\to(2,2)\to(4)\to(3,1)\to(2,1,1).
\]
The ratio of the products of the forward and reverse rates around this cycle is
\[
\frac{A(1,1)A(2,2)}{A(1,2)A(1,3)}.
\]
All instance multiplicities, central-split factors, beta factors and n factors cancel.

For A(i,j)=a(i+j)+b with a>0,b>=0 the ratio is
(2a+b)/(3a+b), which differs from one.
For A(i,j)=ij it is 2/3.
Kolmogorov's cycle criterion therefore rules out reversibility under ANY stationary law in these examples, not merely under the original Gibbs law.

### 4.2 Detailed balance and constant coagulation do not guarantee a useful uniform gap for arbitrary weights

For every n>=3 set beta=1/n, theta=1, A(i,j)=1, and
\[
\epsilon_n=e^{-n^2},\qquad
w_1=1,\quad w_n=\frac1{n!},\quad
w_j=\frac{\epsilon_n}{n!}\quad(2\le j\le n-1).
\]
Use the Gibbs-compatible fragmentation rule from Section 3.
The all-monomer state and the single n-cluster state both have unnormalized stationary weight 1/n!. In particular the single-cluster state G has probability at most 1/2.

Its total exit rate is
\[
q(G,G^c)
=\beta\sum_{i=1}^{n-1}\frac{w_iw_{n-i}}{w_n}
=\beta\left[
 2\epsilon_n+\frac{(n-3)\epsilon_n^2}{n!}\right]
\le3\beta\epsilon_n.
\]
The Rayleigh quotient of 1_G yields
\[
\gamma_w\le
\frac{q(G,G^c)}{1-\pi_w(G)}
\le\frac{6e^{-n^2}}n.
\]
Thus there is no uniform extension of the original gap scale to arbitrary positive Gibbs weights, even with the exact original coagulation rates.

The two endpoint states in fact carry almost all the mass. Every other partition contains a part of size 2 through n-1, so its unnormalized weight is at most epsilon_n/n!. Their total weight relative to either endpoint is at most p(n) epsilon_n <= 2^{n-1}e^{-n^2}. This is a genuine stationary bottleneck, not a failure of the stationary formula.

## 5. Affine kernels with an autonomous count chain

Take A(i,j)=a(i+j)+b, where a,b>=0 and a+b>0. Choose w_1=1 and
\[
w_j=\frac{aj+b}{j-1}\sum_{i=1}^{j-1}w_iw_{j-i},
\qquad j\ge2.
\]
Then Gibbs-compatible fragmentation has total rate beta(j-1) from a j-cluster:
\[
\beta(aj+b)\frac{\sum_{i=1}^{j-1}w_iw_{j-i}}{w_j}
=\beta(j-1).
\]
The exact weights are
\[
w_j=\frac1{j!}\prod_{r=2}^j(2aj+br).
\]
These are the affine Gibbs weights in Granovsky--Erlihson (2009), Eq. (2.40), after their parameters a,b are set to 2a,2b.

With K=k, the merger rate is
\[
\frac2n\sum_{u<v}[a(s_u+s_v)+b]
=2a(k-1)+\frac b n k(k-1),
\]
since sum s_u=n. The count chain is therefore genuinely Markov, with
\[
\lambda_k=\beta(n-k),\qquad
\mu_k=2a(k-1)+\frac b n k(k-1).
\]
Its derivative has birth rate beta(n-k-1), death rate mu_k, and killing
\[
\beta+2a+\frac{2bk}n.
\]
The constant positive vector gives the rigorous count bounds
\[
\beta+2a+\frac{2b}n
\le\gamma_Q\le
\beta+2a+\frac{2b(n-1)}n.
\]
For b=0, K-1 is an Ehrenfest chain with n-1 sites, independent birth beta and death 2a. Hence
\[
\gamma_Q=\beta+2a,\qquad
K-1\sim{\rm Binomial}(n-1,\beta/(\beta+2a)).
\]

**Prior-art boundary.** Granovsky--Erlihson (2009), Section 2.3, explicitly assert equality of the full solvable CFP gap and the count gap, and derive the pure additive exact value. Their Eq. (2.43) is expressed for initial laws with prescribed Gibbs conditional distributions, so deriving full-state spectral equality solely from that displayed law requires care. Regardless of how that logical step is reconstructed, the equality and pure additive value are already asserted in the primary literature and cannot be advertised as new problems solved here. This note independently establishes the rates, stationary measure and count chain; it does not claim a new complete affine full-state spectral proof.

Normalization to the primary source: use their coagulation parameters 2a,2b, their fragmentation parameter phi(1,1)=beta n, and then divide their generator by n. This gives exactly the rates above.

### 5.1 Rooted forests for pure additive coagulation

When b=0, the weights are w_j=(2aj)^{j-1}/j!.
There is a useful stationary lift to rooted forests on n labeled vertices, with each edge directed toward its component root.
From a forest, add a directed edge from a component root to any vertex of another component at rate 2a/n per such ordered pair; delete each edge at rate beta.
Between components of sizes i,j there are i+j allowed root-to-vertex connections, giving aggregate merger rate 2a(i+j)/n.

The labeled stationary law assigns a forest with n-K edges weight
(2a/(beta n))^{n-K}. The number of rooted labeled trees on a specified j-set is j^{j-1}; aggregating over set partitions yields
\[
\pi(m)\propto
\frac{(\beta n/(2a))^{K(m)}}{\prod m_j!}
\prod_j\left(\frac{j^{j-1}}{j!}\right)^{m_j},
\]
which agrees with the Gibbs law above after dropping a fixed-mass factor.
Detailed balance and conditional averaging identify the associated size-dependent fragmentation distribution.

This lift is not by itself a uniform full-gap proof for unlabelled polymers. At small beta, labeled forest shape and root variables can move only through rare edge deletions, whereas a single n-cluster has no such shape coordinate in the polymer state. Those extra slow variables must be removed or controlled.

## 6. The classical multiplicative/Ewens model

Set A(i,j)=ij and w_j=1/j. Then
\[
\text{pair merger}=\frac{2ij}{n},\qquad
\text{per-link split}=\beta(i+j),
\]
and
\[
\pi_{\rm E}(m)\propto
\frac{\theta^{K(m)}}{\prod_j j^{m_j}m_j!},
\qquad \theta=\beta n.
\]
This is the Ewens cycle-count law.

The process is the Metropolis random-transposition walk on cycle types, with time normalization
\[
L_{\rm E}=(n-1)\max(1,\theta)(P_{\theta^{-1}}-I).
\]
Jiang (2015), Eq. (7) and Theorem 4.2, give the partition eigenvalues. In the present units they are
\[
\Lambda_\lambda=\frac2n\left[
\binom n2-\sum_i\binom{\lambda_i}{2}
+\theta\sum_i(i-1)\lambda_i\right],\qquad\lambda\vdash n.
\]
For any nontrivial partition, the first difference of binomial sums is at least n-1 and the final sum is at least one; both are attained at (n-1,1). Consequently
\[
\gamma_{\rm E}=2\beta+\frac{2(n-1)}n.
\]
For example m_1 has affine drift
\[
L_{\rm E}m_1=2\beta n-
\left(2\beta+\frac{2(n-1)}n\right)m_1,
\]
which independently confirms the displayed gap as an eigenvalue.

A shared multiplier c_n(i,j) in [c_-,c_+] gives a growing-kernel class with the SAME Ewens law and
\[
c_-\left(2\beta+\frac{2(n-1)}n\right)
\le\gamma_{{\rm E},c}\le
c_+\left(2\beta+\frac{2(n-1)}n\right).
\]
This is a useful rigorous comparison class of order 1+beta, including beta=1/n. The exact base diagonalization is classical, and the multiplier step is routine comparison.

The shared-product model with w_j=1 instead has split rate beta ij per link and a different equilibrium. It must not be confused with this solvable Ewens model.

## 7. Shared additive and product kernels at the original Gibbs law

Keep w_j=1. The two natural growing multipliers have the following exact total rates.

For c(i,j)=i+j,
\[
\text{total merge}=2(K-1),\qquad
\text{total split}=\beta\left(\sum_jj^2m_j-n\right).
\]
For c(i,j)=ij,
\[
\text{total merge}=n-\frac1n\sum_jj^2m_j,\qquad
\text{total split}=\frac\beta6\sum_jj(j^2-1)m_j.
\]
The count is not autonomous in either case. Trivial comparison yields
gamma_add >=2 gamma_0 and gamma_prod >=gamma_0.
Also ij >=(i+j)/2, so gamma_prod >=gamma_add/2.

### 7.1 A rigorous uniform upper bound at beta=1/n

**Established here:** both shared additive and shared product chains satisfy
\[
\gamma(n,1/n)\le9,\qquad n\ge2.
\]
More generally this holds with 9C if c(1,j)<=C(j+1).

Here is a fully finite proof. At theta=1, define
\[
Z_0=1,\qquad
Z_n=\sum_{k=1}^n\frac1{k!}\binom{n-1}{k-1}\quad(n\ge1).
\]
The formula follows by first choosing the number k of ordered positive composition parts and then dividing by k!.
Pascal's identity gives, for n>=2,
\[
Z_n=Z_{n-1}+
\sum_{\ell=1}^{n-1}\frac1{(\ell+1)!}\binom{n-2}{\ell-1}.
\]
Therefore Z_{n-1}<=Z_n<=(3/2)Z_{n-1}.
The factorial moment identities for m_1 give
\[
\mathbb E m_1=Z_{n-1}/Z_n\ge2/3,\qquad
\mathbb E m_1^2=(Z_{n-1}+Z_{n-2})/Z_n\le2.
\]
By Cauchy--Schwarz,
\[
\pi_0(m_1>0)\ge
\frac{(\mathbb Em_1)^2}{\mathbb Em_1^2}\ge2/9.
\]

Let A={m_1=0}. Only fragmentation can exit A. For c(1,j)<=C(j+1), a cluster of size j>=3 creates a monomer at rate at most 2C beta j. A dimer exits A at rate beta c(1,1)<=2C beta, also bounded by 2C beta j. Thus q(m,A^c)<=2C beta n for m in A. Applying the indicator Rayleigh quotient,
\[
\gamma\le
\frac{\mathbb E[q(m,A^c)\mid A]}{\pi_0(A^c)}
\le9C\beta n=9C.
\]
Both named kernels satisfy the assumption with C=1.

This bounds the true spectral gap even though large clusters may interact at much faster rates. In particular, a prediction that the shared-product gap grows like sqrt(n) at beta=1/n, based only on a typical bulk kernel value, is false. Small-cluster observables remain a relevant constraint.

### 7.2 Unpaid lower bound and finite diagnostics

A substantive open target from the present work is a uniform lower bound for the shared additive model at beta=1/n, or more strongly
gamma_add comparable to 1+beta uniformly in n,beta.
The numerical lower bound gamma_add >=2(1+beta) is plausible but is NOT proved here.

The diagnostic script explore_gaps.py assembles the exact symmetric generator from merger edges and reverse split rates. It uses floating-point eigenvalues only. The saved finite_gap_diagnostics.json contains 47 cases, n=2,3,4,8,12,20,24, with additive beta values from .001 to10 and additional product cases at beta=1/n.
At beta=1/n:

| n | shared additive gap | shared product gap |
|---:|---:|---:|
| 4 | 2.915656 | 1.850620 |
| 8 | 2.720902 | 1.945188 |
| 12 | 2.602066 | 1.969638 |
| 20 | 2.471881 | 1.985689 |
| 24 | 2.431382 | 1.989083 |

The original n=2 gap is multiplied by 2 for the additive kernel, giving exactly 2(1+beta). At n=3 the additive gap can be calculated explicitly as
4 beta+3-sqrt(4 beta^2+1), also at least 2(1+beta).
These checks support a target; they do not prove an all-n theorem.

Simple Hamming-distance path coupling is insufficient: splitting a merged a+b cluster creates unmatched fragmentation at total rate proportional to beta ab. A stationary-lift proof must handle these angular effects rather than insert the average segment size into the old radial operator.

The unproved additive target is intentionally absent from the manuscript-ready LaTeX sections.

## 8. Primary literature inspected

1. Granovsky, B. L.; Erlihson, M. M. (2009), On Time Dynamics of Coagulation-Fragmentation Processes, Journal of Statistical Physics 134, 567--588. DOI 10.1007/s10955-008-9671-3. https://arxiv.org/html/0711.0503v3 . Equations (2.34), (2.40), (2.41) give the affine Gibbs family; Section 2.3, Spectral gap, gives count bounds and explicitly asserts full solvable-gap equality.
2. Jiang, Y. (2015), Mixing time of Metropolis chain based on random transposition walk converging to multivariate Ewens distribution, Annals of Applied Probability 25(3), 1581--1615. DOI 10.1214/14-AAP1031. https://arxiv.org/pdf/1204.1671 . Equation (7), Lemma 4.1, and Theorem 4.2 give the complete cycle-type spectral diagonalization used above. The source uses inverse Ewens parameter theta; this note uses theta for the Ewens activity and therefore calls Jiang's parameter theta^{-1}.
3. Paulin, D. (2016), Mixing and concentration by Ricci curvature, Journal of Functional Analysis 270(5), 1623--1662. DOI 10.1016/j.jfa.2015.12.010. https://arxiv.org/pdf/1404.2802 . Section 4.1, Proposition 4.1, gives a multistep-curvature route to order 1/n discrete-time gap bounds for the uniform split-merge/random-transposition model. Its rate normalization and stationary law differ from the shared-product model with w_j=1.

These are finite-state partition processes or directly relevant finite-chain methods. Spectral-gap statements for growth-fragmentation PDEs, linearized deterministic coagulation equations, or equilibrium-only Gibbs results do not by themselves settle the stochastic finite-partition gap considered here.

## 9. Deliverable map

- kernel_comparison.tex: manuscript-ready common-multiplier theorem and explicitly credited Ewens comparison class.
- nonreversible.tex: exact random-permutation conservative-motion theorem, including asymptotic real-part rate, best prefactor-one norm exponent, and a strict acceleration example.
- polymer_circulation.tex: optional direct nonreversible construction using only original polymer reaction edges; qualitative strict acceleration and a positive quadratic coefficient, with no uniform-in-n improvement claim.
- kernel_references.bib: Jiang primary citation to add to the manuscript bibliography.
- audit_sharp_count_quotient.md: independent algebra audit of the root agent's uniform additive-error count-gap certificate.
- explore_gaps.py and finite_gap_diagnostics.json: reproducible exploratory evidence, not proof.
