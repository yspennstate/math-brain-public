# Shifted thresholds disprove Han's absolute-overlap criterion

20 September 2026. Research continuation for the Friedgut–Kalai Fourier entropy–influence problem.

**Full FEI: OPEN.** This report proves a negative answer to the stronger coordinate-selection question in Han [H, Question 3.1], not a counterexample to FEI. The proof is analytical; the accompanying exact program checks finite identities and witnesses. Independent expert review, Lean formalization, and comprehensive priority clearance have not been completed.

## 1. Statement and scope

Use the uniform measure on the sign cube. For Boolean f, write

\[
I_i(f)=\sum_{S\ni i}\widehat f(S)^2,
\qquad
O_i(f)=\sum_{S\not\ni i}|\widehat f(S)\widehat f(S\cup\{i\})|.
\]

Han asks whether a universal finite C exists such that every Boolean f has at least one coordinate i with O_i(f)<=C I_i(f). The answer is negative, even for monotone functions invariant under every coordinate permutation.

**Theorem 1.** For integers m>=2, set n=m^2+1 and

\[
f_m(x)=\operatorname{sgn}\left(\sum_{j=1}^{m^2+1}x_j-m\right).
\tag{1.1}
\]

There are no ties: the sum and m have opposite parity. Every coordinate has positive influence, all coordinate ratios are identical, and

\[
\boxed{\frac{O_i(f_m)}{I_i(f_m)}
\ge \frac{1}{2\pi^2}\ln(m^2+1)-C_0\quad\text{for every }i,}
\tag{1.2}
\]

where C_0 is an absolute finite constant. In particular, the minimum over coordinates tends to infinity. The coefficient in (1.2) is a proved lower coefficient, **not a claimed sharp asymptotic coefficient**.

The functions are ordinary unweighted threshold functions. They are monotone and fully symmetric. Their individual influences satisfy

\[
I_i(f_m)=2^{-m^2}\binom{m^2}{(m^2-m)/2}
\sim \sqrt{\frac2\pi}\,e^{-1/2}m^{-1}.
\tag{1.3}
\]

The already-published FEI theorem for symmetric functions [OWZ, Theorem 1] gives H(f_m)<=12.04 I(f_m). Thus (1.2) separates Han's stronger sufficient condition from FEI on a class where FEI is already known. The symmetric-function FEI theorem is not a new result of this continuation.

The June 2026 paper [GMP, introduction, equation (3)] gives examples where a designated splitting coordinate fails, while another coordinate works. Here **every coordinate fails with every fixed universal coefficient**. This distinction is the relevant quantifier. The literature search checked those exact primary sources; it is not an exhaustive novelty certification.

## 2. Exact finite Fourier formulas

Put N=m^2 and s=(N-m)/2. There are N other coordinates after differentiating in one coordinate. The derivative D_i f_m equals the indicator that their sum is m, equivalently that exactly s of them are negative. Let

\[
p_N=2^{-N}\binom Ns.
\]

By symmetry, the Fourier coefficient a_{N,k} depends only on its degree k. Define the Krawtchouk coefficients K_j by

\[
(1+z)^{N-s}(1-z)^s=\sum_{j=0}^N K_jz^j.
\tag{2.1}
\]

Conditional on the boundary slice, the product of j specified signs has mean K_j/binom(N,j): summing these products over all j-subsets gives the coefficient in (2.1), and exchangeability makes their expectations equal. Therefore

\[
\boxed{a_{N,k}=p_N\frac{K_{k-1}}{\binom N{k-1}},\quad1\le k\le N+1.}
\tag{2.2}
\]

The constant coefficient is

\[
a_{N,0}=2^{-(N+1)}\left[2\sum_{r=0}^s\binom{N+1}{r}-2^{N+1}\right].
\tag{2.3}
\]

In particular I_i=p_N. For c_j=K_j/sqrt(binom(N,j)), counting the subsets not containing i gives

\[
\frac{O_i(f_m)}{I_i(f_m)}
=|a_{N,0}|+p_N\sqrt N\sum_{k=1}^N
\sqrt{1-\frac{k-1}{N}}\frac{|c_{k-1}c_k|}{\sqrt k}.
\tag{2.4}
\]

Every term is nonnegative. Differentiating (2.1) gives the exact recurrence

\[
K_0=1,\quad K_1=m,\quad
(j+1)K_{j+1}=mK_j-(N-j+1)K_{j-1}.
\tag{2.5}
\]

Thus c_0=c_1=1 and

\[
c_{j+1}=\frac{c_j}{\sqrt{j+1}\sqrt{1-j/N}}
-\sqrt{\frac j{j+1}}\sqrt{\frac{1-(j-1)/N}{1-j/N}}c_{j-1}.
\tag{2.6}
\]

These formulas retain the signs of the Fourier coefficients until the absolute overlap is actually formed. No unsigned-mixture substitution is used.

## 3. Hermite overlap diverges logarithmically

Let He_k be the probabilists' Hermite polynomials, defined by

\[
\exp(xt-t^2/2)=\sum_{k=0}^{\infty}\frac{\mathrm{He}_k(x)}{k!}t^k,
\qquad h_k(x)=\frac{\mathrm{He}_k(x)}{\sqrt{k!}}.
\]

At x=1, abbreviate h_k=h_k(1). Then h_0=h_1=1 and

\[
h_{j+1}=\frac{h_j}{\sqrt{j+1}}-\sqrt{\frac j{j+1}}h_{j-1}.
\tag{3.1}
\]

**Lemma 3.1.** As K tends to infinity,

\[
\boxed{\sum_{k=1}^K\frac{|h_{k-1}h_k|}{\sqrt k}
=\frac{\sqrt{2/\pi}\,e^{1/2}}{\pi}\ln K+O(1).}
\tag{3.2}
\]

### Proof of the fixed-argument Hermite estimate

The following derivation is included to avoid relying on a uniform asymptotic with unstated hypotheses. Set u_k(x)=exp(-x^2/4)h_k(x) and lambda_k=sqrt(k+1/2). The Hermite differential equation gives

\[
u_k''+\lambda_k^2u_k=(x^2/4)u_k.
\]

On 0<=x<=1, variation of constants gives

\[
u_k(x)=u_k(0)\cos(\lambda_kx)+\frac{u_k'(0)}{\lambda_k}\sin(\lambda_kx)
+\frac1{\lambda_k}\int_0^x\sin(\lambda_k(x-t))\frac{t^2}{4}u_k(t)\,dt.
\tag{3.3}
\]

For even k=2r,

\[
u_k(0)=(-1)^r\frac{\sqrt{\binom{2r}r}}{2^r},\qquad u_k'(0)=0.
\]

For odd k, u_k(0)=0 and u_k'(0)=sqrt(k) h_{k-1}(0). Stirling's formula makes the relevant initial amplitude

\[
(2/\pi)^{1/4}k^{-1/4}(1+O(k^{-1})),
\]

with the displayed alternating sign. The integral in (3.3) has sup norm at most (12 lambda_k)^(-1) sup|u_k|. Moving this term to the left first bounds sup|u_k| by O(k^(-1/4)), then bounds the remainder by O(k^(-3/4)). Consequently

\[
h_k(1)=(2/\pi)^{1/4}e^{1/4}k^{-1/4}
\left[\cos\left(\sqrt{k+\tfrac12}-\frac{k\pi}{2}\right)+O(k^{-1/2})\right].
\tag{3.4}
\]

In particular |h_k|<=C(k+1)^(-1/4) for all k. Formula (3.4) is also consistent with the classical fixed-argument Hermite expansion [D, section 18.15(v)].

### Completion of Lemma 3.1

The phases for k and k-1 differ by pi/2+O(k^(-1/2)). The product-to-sum identity and the inequality ||a|-|b||<=|a-b| imply

\[
\frac{|h_{k-1}h_k|}{\sqrt k}
=\frac{\sqrt{2/\pi}\,e^{1/2}}{2k}|\sin(2\sqrt k)|+O(k^{-3/2}).
\tag{3.5}
\]

This estimate is valid also near zeros of the sine because the error is absolute, not relative.

The function g(x)=|sin(2 sqrt(x))|/x is absolutely continuous on each compact subinterval of [1,infinity), with |g'(x)|<=x^(-3/2)+x^(-2) almost everywhere. Thus its sum and integral differ by O(1). Substituting u=2sqrt(x), and using the bounded primitive of the mean-zero periodic function |sin u|-2/pi, gives

\[
\sum_{k=1}^K\frac{|\sin(2\sqrt k)|}{k}
=2\int_2^{2\sqrt K}\frac{|\sin u|}{u}\,du+O(1)
=\frac2\pi\ln K+O(1).
\tag{3.6}
\]

Combining (3.5) and (3.6) proves (3.2).

## 4. A quantitative growing-degree comparison

A fixed-degree Hermite limit alone already disproves Han's universal bound, by first taking N to infinity and then increasing the finite cutoff K. The next lemma justifies the stronger logarithmic-in-dimension lower bound (1.2); it is not an interchange of those two limits.

**Lemma 4.1.** There is an absolute C such that, for square N and 1<=k<=N^(1/4),

\[
\boxed{|c_k-h_k|\le Ck^3/N.}
\tag{4.1}
\]

**Proof.** Write (2.6) as v_{j+1}=M_j^(N)v_j for v_j=(c_j,c_{j-1}), and write (3.1) using M_j^(0). Both initial vectors v_1 equal (1,1). For j<=N/2,

\[
\|M_j^{(N)}-M_j^{(0)}\|\le3\sqrt j/N,
\qquad \|M_j^{(0)}\|\le2,\quad\|M_j^{(N)}\|\le4.
\tag{4.2}
\]

Indeed, the first-row first-entry difference is at most 2sqrt(j)/N; the second-entry difference is at most 1/N, by

\[
(1-j/N)^{-1/2}-1\le2j/N,
\qquad \sqrt{1+1/(N-j)}-1\le1/N.
\]

Here and below the norm is the Euclidean operator norm. To control long products without an exponential-in-sqrt(k) loss, group consecutive matrices in pairs. Put a_j=1/sqrt(j+1), b_j=sqrt(j/(j+1)). Compare

\[
M_{j+1}^{(0)}M_j^{(0)}
=\begin{pmatrix}a_{j+1}a_j-b_{j+1}&-a_{j+1}b_j\\a_j&-b_j\end{pmatrix}
\]

with R_j=[[-1,-a_j],[a_j,-1]]. The norm of R_j is sqrt(1+a_j^2)<=1+1/[2(j+1)]. The three possibly nonzero entries of the difference have absolute values at most 2/(j+1), 1/(j+1), 1/(j+1), respectively. For the off-diagonal entry use

\[
a_j-a_{j+1}b_j=a_j(1-\sqrt{j/(j+2)})\le1/(j+1).
\]

Its Frobenius norm is therefore at most sqrt(6)/(j+1). Consequently

\[
\|M_{j+1}^{(0)}M_j^{(0)}\|\le1+3/(j+1).
\tag{4.3}
\]

Equations (4.2) give the perturbed pair bound

\[
\|M_{j+1}^{(N)}M_j^{(N)}\|
\le1+3/(j+1)+24\sqrt j/N
\tag{4.4}
\]

when j+1<=N/2. Multiplying (4.4), using log(1+t)<=t, and allowing one unpaired matrix gives

\[
\|M_{k-1}^{(N)}\cdots M_\ell^{(N)}\|
\le C\left(\frac{k+1}{\ell+1}\right)^3
\exp(Ck^{3/2}/N).
\tag{4.5}
\]

It suffices to bound the sums over all intervening indices rather than just every second index, so the exponent 3 is deliberately nonoptimal. For k<=N^(1/4), the exponential factor is uniformly bounded.

The discrete variation-of-constants formula, (4.2), (4.5), and |h_j|<=C(j+1)^(-1/4) now imply

\[
\|v_k^{(N)}-v_k^{(0)}\|
\le\frac{Ck^3}{N}\sum_{j=1}^{k-1}\frac{j^{1/4}}{(j+1)^3}
\le Ck^3/N.
\]

The finitely many small endpoint cases are covered by increasing C. This proves (4.1).

## 5. Proof of Theorem 1

Let K=floor(N^(1/4)). By (4.1) and the bound on h_k,

\[
\sum_{k=1}^K\frac{\left||c_{k-1}c_k|-|h_{k-1}h_k|\right|}{\sqrt k}
\le C\left(\frac{K^{13/4}}N+\frac{K^{13/2}}{N^2}\right)=o(1).
\tag{5.1}
\]

The factor sqrt(1-(k-1)/N) in (2.4) changes the h-sum by O((K/N)log(K+1))=o(1). Stirling's formula, with s=(N-sqrt(N))/2, gives

\[
p_N\sqrt N=\sqrt{2/\pi}e^{-1/2}+O(N^{-1}).
\tag{5.2}
\]

Keep only the nonnegative terms k<=K in (2.4). Equations (3.2), (5.1), and (5.2) yield

\[
\frac{O_i(f_m)}{I_i(f_m)}
\ge\frac{2}{\pi^2}\ln K-O(1)
=\frac{1}{2\pi^2}\ln N-O(1).
\]

Replacing ln N by ln(N+1) changes only a bounded error. Symmetry makes this estimate identical for every coordinate. This proves (1.2), while (5.2) proves (1.3). In particular it disproves Han's existential-coordinate assertion, not merely the assertion for a prescribed coordinate. QED.

## 6. A qualitative extension to every fixed nonzero threshold shift

More generally choose boundary sums r_N with the same parity as N and r_N/sqrt(N)->theta, for fixed theta!=0. The fixed-degree version of (2.6), or the generating function (2.1), gives c_k->h_k(theta). The proof of (3.4) on the fixed interval joining 0 to theta gives

\[
\sum_{k=1}^K\frac{|h_{k-1}(\theta)h_k(\theta)|}{\sqrt k}
=\frac{\sqrt{2/\pi}e^{\theta^2/2}}{\pi}\ln K+O_\theta(1).
\]

The sine in (3.5) becomes |sin(2 theta sqrt(k))|. Its weighted mean is unchanged for each fixed nonzero theta. Since sqrt(N)p_N->sqrt(2/pi) exp(-theta^2/2), the truncated limiting overlap equals (2/pi^2)ln K+O_theta(1). Nonnegativity and successive limits prove that every coordinate ratio diverges for these thresholds too.

No estimate uniform as theta->0 is claimed. At theta=0, the Hermite products in adjacent degrees vanish by parity. In particular, odd majority does not furnish this overlap obstruction. By taking a small but fixed nonzero theta, the obstruction can occur at an arbitrarily small fixed limiting bias; exact balance is not asserted.

## 7. What survives for the actual entropy-weighted route

For the Fourier spectral law p_S, define

\[
B(f)=\sum_i H(S_i\mid S_{-i}),
\quad
K(f)=\sum_i\sum_{S\not\ni i}\min(p_S,p_{S+i})
\left|\log_2\frac{p_S}{p_{S+i}}\right|.
\]

Zero terms have their continuous value zero. For every probability law,

\[
K(f)\le B(f)\le H(f),
\qquad B(f)\le K(f)+(2/\ln2)I(f).
\tag{7.1}
\]

The first upper bound follows by the chain rule and conditioning reducing entropy. On an edge with a<=b, its contribution to B-K is (a+b)log_2(1+a/b)<=2a/ln2; summing min(p_S,p_{S+i})<=sum_{S containing i}p_S proves the other bound.

For this symmetric family the already-known inequality H<=12.04 I consequently gives B<=12.04 I and K<=12.04 I, while sum_i O_i/I diverges. Thus no estimate

\[
\sum_i O_i(f)\le A K(f)+B_0 I(f)
\]

with fixed nonnegative A,B_0 can hold universally. Replacing the logarithmic weight by absolute overlap is genuinely too costly, even on a class where the entropy-weighted quantity is bounded.

The repository's remaining universal K<=C I or hereditary B<=C I route is **not refuted** by this example and is **not proved** here. The false pointwise shortcut H(f)<=B(f)+(2/ln2)I(f) must not be reinstated. The valid implication quantifies over every Boolean function (equivalently appropriate physical restrictions), as recorded in the existing recovery handoff.

## 8. Exact checks and current limits

Run `python verify_threshold_obstruction.py --max-m 64 --output verification.json`.

The executed checker crosschecks all 55 nonconstant symmetric thresholds in dimensions 1 through 10 against direct integer Walsh transforms, checks every coordinate separately, verifies Parseval and the influence formula, and computes exact rational intervals for n=5,17,65,257,1025,4097.

An explicit 32-variable threshold, +1 for at most 21 negative signs, has

\[
O_i/I_i=2314378859/1073741824>2.155433277599
\]

at every coordinate. For the sequence (1.1), the n=4097 ratio lies between 2.654791031287 and 2.654791031288. These values are finite checks, not the proof of divergence.

The program uses no unverified numerical eigenvalues or numerical Hermite asymptotics. A separate entropy-weight probe is floating-point exploration only and is not used in the proof. Its finite values are compatible with the known symmetric-function FEI bound; they do not establish a new uniform bound.

### Research delta and limitations

- New here: the all-coordinate shifted-threshold obstruction to Han Question 3.1, a quantitative logarithmic lower bound via a growing-degree comparison, and the resulting separation from the entropy-weighted route.
- Reused: Fourier differentiation, Krawtchouk slice formulas, classical Hermite asymptotics (proved in the needed form above), and the published symmetric-function FEI theorem.
- Recovered separately: the unpushed September 19 affine-drift/stability package. Its statements are not counted as new results of this report.
- Still missing: a universal dimension-free entropy/influence bound for arbitrary Boolean functions. No percentage-to-completion, full FEI closure, independent audit, or formal verification is claimed.

## References

[H] Xiao Han, *A New Bound for the Fourier-Entropy-Influence Conjecture*, Combinatorica 45, article 4 (2025), published online 20 December 2024. DOI: 10.1007/s00493-024-00133-z. Question 3.1 and equations (3.16)--(3.18). Primary source checked: https://link.springer.com/article/10.1007/s00493-024-00133-z

[GMP] Maria Jose Gonzalez, Paul MacManus, and Maria Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, 9 June 2026. Introduction, equation (3), and the distinction between a designated coordinate and a well-chosen coordinate. https://arxiv.org/abs/2606.00246v2

[OWZ] Ryan O'Donnell, John Wright, and Yuan Zhou, *The Fourier Entropy--Influence Conjecture for Certain Classes of Boolean Functions*, ICALP 2011, LNCS 6755, pp. 330--341. Theorem 1 gives constant 12.04 for symmetric functions. DOI: 10.1007/978-3-642-22006-7_28. Author manuscript: https://www.math.ias.edu/files/ODonnell_Fourier.pdf

[D] NIST Digital Library of Mathematical Functions, section 18.15(v), Hermite fixed-argument asymptotics, equations 18.15.24--18.15.27. https://dlmf.nist.gov/18.15#v

[Repository] `proofnet24/P03-fei/handoffs/2026-09-19__FROZEN_SESSION_RECOVERY.md`, actual source blob `2077f118112bfca756862fe240923ddc444b220e`, read in full: corrected universal/hereditary K/B route. `continuations/2026-09-19-balanced-substitution/REPORT.md`, blob `dc9daa94dc791a075ff2f9569d9c7e2fb0547179`, source lines 1--230 read: the earlier failed resolvent route and majority allocation formulas. Neither report proves or is used as a substitute for the shifted-threshold theorem above.
