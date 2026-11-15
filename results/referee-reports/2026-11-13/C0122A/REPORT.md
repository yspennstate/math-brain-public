RESOLVED_IN_LITERATURE

C0122: Chaos implies multiple peaks for finite centered Gaussian fields, with arbitrary covariance signs. No additional hypothesis beyond Chatterjee's setup is required.

The resolution is Jian Ding, Ronen Eldan, and Alex Zhai, “On multiple peaks and moderate deviations for the supremum of a Gaussian field,” *The Annals of Probability* **43** (2015), no. 6, 3468–3493, DOI [10.1214/14-AOP963](https://doi.org/10.1214/14-AOP963). The precise result used below is **Theorem 1.2**, checked in [arXiv:1311.5592v2](https://arxiv.org/abs/1311.5592v2), p. 2. The paragraph immediately following it, p. 3, explicitly identifies Open Problem 5 of Chatterjee's paper as solved. Its reference [4] is arXiv:0810.4221. Publication details and removal of the covariance-sign restriction are independently confirmed by [Ding's publication list](https://math.pku.edu.cn/teachers/dingjian/index.html) and [Eldan's institutional publication record](https://weizmann.elsevierpure.com/en/publications/on-multiple-peaks-and-moderate-deviations-for-the-supremum-of-a-g/).

The following gives the exact definitions and a rigorous deduction of the requested implication from the literature theorem. This is an application of an existing result, with no claim of a new proof of that theorem.

For a finite centered Gaussian field \(X_n=(X_{n,i})_{i\in S_n}\), write

\[
R_n(i,j)=\operatorname{Cov}(X_{n,i},X_{n,j}),\quad
\sigma_n^2=\max_i\operatorname{Var}(X_{n,i}),\quad
M_n=\max_iX_{n,i},\quad m_n=\mathbb E M_n,\quad
v_n=\operatorname{Var}(M_n).
\]

Chatterjee assumes distinct coordinates are unequal almost surely (condition (1), p. 3), so the maximizer is well-defined. With an independent copy \(X'_n\), put

\[
X_n^t=e^{-t}X_n+\sqrt{1-e^{-2t}}X'_n,
\qquad I_n^t=\arg\max_i X_{n,i}^t.
\]

His Definition 1.5, p. 6, calls the sequence chaotic if there exist \(t_n\to0\) for which

\[
\mathbb E R_n(I_n^0,I_n^{t_n})=o(\sigma_n^2).
\]

This concerns the **signed expectation**, not the expectation of the absolute overlap or its square. Definition 1.4 calls \(v_n=o(\sigma_n^2)\) superconcentration.

Definition 1.6, p. 6, requires deterministic sequences \(\ell_n\to\infty\), \(\varepsilon_n=o(\sigma_n^2)\), \(\delta_n=o(m_n)\), and \(\gamma_n\to0\), such that with probability at least \(1-\gamma_n\) a set \(A_n\subset S_n\) satisfies

\[
|A_n|=\ell_n,\qquad
R_n(i,j)<\varepsilon_n\quad(i\ne j\in A_n),\qquad
X_{n,i}\ge M_n-\delta_n\quad(i\in A_n).
\]

Thus Chatterjee's overlap condition is one-sided, and its height threshold uses the realized maximum. Definition 1.7 replaces \(\delta_n=o(m_n)\) by \(\delta_n=o(\sigma_n)\) for *strong* multiple peaks. That stronger property is not the question here; the 2008 paper already shows that chaos need not imply it.

Chatterjee's Theorem 1.8, pp. 6–7, establishes superconcentration equivalent to chaos for arbitrary covariance signs, and obtains chaos implying multiple peaks under \(R_n(i,j)\ge0\). The finite-field version is Theorem 3.7, p. 16: for integer \(\ell\ge2\), \(0<\varepsilon<\sigma^2\), and \(0<\delta<m\), the required set exists with probability at least

\[
1-4\sqrt{\frac{vm\ell^3\log\ell}{\delta\varepsilon}}
-4\left(\frac{v\sigma^4\ell^5\log\ell}{\delta^3m\varepsilon}\right)^{1/4}.
\]

In its proof, equation (11), p. 18, uses nonnegativity to control the probability of a large pairwise overlap by a sum of its expectations. Section 12(5), p. 59, asks to remove this restriction and mentions the missing second-moment estimate. These are exactly the source and problem specified in the task.

Ding–Eldan–Zhai's Theorem 1.2 can be written in the notation above as follows. There are universal constants \(C,c>0\) such that, for any finite centered Gaussian field, \(0<d\le m\), \(0<e\le\sigma^2\), and \(0<z\le1\), with probability at least

\[
1-Cv/d^2-z
\]

there is a set \(A\) satisfying

\[
|A|\ge\exp\left(\frac{c e^2 d z}{m\sigma^2v}\right),\qquad
|R(i,j)|\le e\quad(i\ne j\in A),\qquad
X_i\ge m-d\quad(i\in A).
\]

There is no nonnegative-covariance assumption. The authors' Definition 1.1 uses absolute covariance and the expected maximum; these differences require the following small conversion.

Suppose the sequence is chaotic. Chatterjee's Theorem 3.2, p. 12, holds without a covariance-sign restriction and gives, for every \(t>0\),

\[
0\le f_n(t):=\mathbb E R_n(I_n^0,I_n^t)
\le\frac{v_n}{1-e^{-t}},\qquad
v_n\le\sigma_n^2(1-e^{-t})+e^{-t}f_n(t).
\]

Applying the second inequality at the chaos times shows that
\(a_n:=v_n/\sigma_n^2\to0\).
All ratios below concern the nontrivial tail of the sequence with \(\sigma_n>0\); the normalized definitions themselves require that tail. For a finite field with \(\sigma_n>0\), its maximum has an unbounded upper tail, hence \(v_n>0\).

We also need \(b_n:=m_n/\sigma_n\to\infty\). Select a coordinate with variance \(\sigma_n^2\). Since \(M_n\) dominates this coordinate pointwise, for \(Z\sim N(0,1)\),

\[
a_n\ge\mathbb E\bigl[(Z-b_n)_+^2\bigr].
\]

The right side is strictly positive for each finite \(b_n\) and is decreasing in \(b_n\), so \(a_n\to0\) forces \(b_n\to\infty\). This also appears in Chatterjee's argument on p. 17 and uses no covariance-sign assumption.

For sufficiently large \(n\), choose

\[
e_n=\sigma_n^2a_n^{1/8},\qquad
d_n=m_na_n^{1/8},\qquad z_n=a_n^{1/8}.
\]

The theorem applies and its cardinality exponent is

\[
\frac{c e_n^2d_nz_n}{m_n\sigma_n^2v_n}
=c a_n^{-1/2}\longrightarrow\infty.
\]

Its exceptional probability is at most

\[
C\frac{v_n}{d_n^2}+z_n
=C\frac{a_n^{3/4}}{b_n^2}+a_n^{1/8}\longrightarrow0.
\]

Chebyshev's inequality additionally gives
\(\mathbb P(M_n>m_n+d_n)\le v_n/d_n^2\).
On the intersection of these two events, every selected point satisfies

\[
X_{n,i}\ge m_n-d_n\ge M_n-2d_n.
\]

Take a subset of size
\(\ell_n=\lfloor\exp(ca_n^{-1/2})\rfloor\),
set \(\varepsilon_n=2e_n\) and \(\delta_n=2d_n\), and bound the combined exceptional probability by
\(\gamma_n=(C+1)a_n^{3/4}/b_n^2+a_n^{1/8}\).
Then \(\ell_n\to\infty\), \(\varepsilon_n=o(\sigma_n^2)\), \(\delta_n=o(m_n)\), and \(\gamma_n\to0\). Moreover,
\(R_n(i,j)\le|R_n(i,j)|\le e_n<\varepsilon_n\).
This proves exactly Chatterjee's multiple-peaks property. Finitely many initial terms do not affect the conclusion.

The published result takes a different route from the proposed overlap second-moment bound. Section 2 of the preprint uses concentration to produce many sites with small absolute covariance, then applies this geometric fact to a Gaussian field restricted to a random near-maximum set. In particular, Lemma 2.2 handles signed covariances through signed displacement directions. This report does not claim a new bound on \(\mathbb E R(I^0,I^t)^2\).

Verification: downloaded both version-pinned arXiv papers, converted their PDF bytes directly to text, and read Chatterjee's definitions, Theorems 1.8, 3.2, 3.7 and its proof, and all of Section 12. Read Ding–Eldan–Zhai's Definition 1.1, Theorem 1.2, explicit problem identification, reference [4], and Section 2 proof route. Checked the parameter substitutions both by cancellation of units and by exact rational exponents. Source hashes and source URLs are in `sources/manifest.json`; the small arithmetic audit is in `data/verification.json`.

Access limitation: direct journal PDF endpoints and the IMS full-issue endpoint returned HTML or failed. The theorem statement and numbering above were directly checked in the saved arXiv v2, while the publication identity and substantive covariance-sign conclusion were corroborated with the two author/institutional records linked above. No claim is made to have inspected the final typeset theorem numbering independently.

Literature search stopped at this explicit solution, as instructed. The search included the 2014 book and the Ding–Eldan–Zhai lead; it did not continue through all the other named authors or claim an exhaustive 2008–2026 survey. Steps 2–4 requiring new research and simulations were not started: the user's literature-resolution stop condition had been met. No simulation estimates or counterexample claims are offered.

Task: “Open problem C0122” — 2026-11-13, approximately 06:13 +04.
