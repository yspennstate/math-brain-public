# P0193: a compactly supported initial law with persistent failure of log-unimodality

Status: complete author-checked candidate counterexample, 2026-09-06. No independent review and no novelty certification. This is a proposed negative answer to Hasebe, Ueda and Wang, *Log-unimodality for free positive multiplicative Brownian motion*, arXiv:2009.13848v1 (29 September 2020), Problem 4.7, PDF page 11. The published reference is Colloquium Mathematicum 169 (2022), 209-226; the archived version used here is the arXiv version. Source: https://arxiv.org/abs/2009.13848.

## Claim and normalization

Let \(\nu=(\delta_{1/10}+\delta_{10})/2\). In the source normalization
\[\Sigma_{\sigma_t}(z)=\exp\!\left(\frac t2\frac{z+1}{z-1}\right),\]
the law \(\sigma_t\boxtimes\nu\) is **not log-unimodal for every \(t\ge5\pi\)**. Its initial law has support in the compact interval \([1/10,10]\), so this disproves eventual log-unimodality for arbitrary compactly supported positive initial laws, if the argument and source match survive review.

Log-unimodality means unimodality of the image measure under the logarithm; ordinary unimodality on the positive line is a different claim. The initial law is multiplicatively symmetric but is not log-unimodal. Thus the source theorem for symmetric log-unimodal initial laws does not apply.

## The exact source criterion

Lemma 4.1(3), PDF page 8, says that \(\sigma_t\boxtimes\nu\) is log-unimodal if and only if, for every \(R\in(0,\pi)\), the equation
\[\frac{\sin R}{R}\int_0^\infty\frac{r\xi}{1+r^2\xi^2-2r\xi\cos R}\,d\nu(\xi)=\frac1t\tag{1}\]
has at most two solutions \(r>0\). We use its contrapositive by finding four distinct solutions for one value of \(R\), for each specified \(t\).

Put \(a=\log10\), \(u=\log r\), and
\[K_R(s)=\frac{1}{2(\cosh s-\cos R)},\qquad F_R(u)=\frac{K_R(u-a)+K_R(u+a)}2.\]
The integral in (1) equals \(F_R(u)\), because dividing its integrand's numerator and denominator by \(r\xi\) gives
\[\frac{r\xi}{1+r^2\xi^2-2r\xi\cos R}=\frac1{r\xi+(r\xi)^{-1}-2\cos R}=K_R(\log r+\log\xi).\]
Hence (1) is equivalent to
\[F_R(u)=\frac{R}{t\sin R}.\tag{2}\]
For fixed \(R\in(0,\pi)\), the function \(F_R\) is continuous, positive and even, and tends to zero at both infinities.

## Selecting the level and time

The function \(g(R)=R/\sin R\) is strictly increasing from 1 to infinity on \((0,\pi)\). Indeed
\[g'(R)=\frac{\sin R-R\cos R}{\sin^2R}>0,\]
because the numerator vanishes at zero and has derivative \(R\sin R>0\). Also \(g(\pi/2)=\pi/2\).

For each \(t\ge5\pi\), there is therefore a unique \(R_t\in[\pi/2,\pi)\) with
\[g(R_t)=\frac t{10}.\]
For this choice the right side of (2) is exactly \(1/10\), and \(\cos R_t\le0\).

## Four strict crossings

Since \(\cosh(\log10)=101/20\),
\[F_{R_t}(0)=K_{R_t}(a)=\frac1{2(101/20-\cos R_t)}\le\frac{10}{101}<\frac1{10}.\tag{3}\]
At \(u=a\), the contribution from the centered kernel alone gives
\[F_{R_t}(a)=\frac{K_{R_t}(0)+K_{R_t}(2a)}2\ge\frac1{4(1-\cos R_t)}\ge\frac18>\frac1{10}.\tag{4}\]
The same inequality holds at \(-a\) by evenness. Together with the limits zero at both infinities, (3)-(4) and the intermediate value theorem give a solution of \(F_{R_t}(u)=1/10\) in each of the four disjoint intervals
\[(-\infty,-a),\quad(-a,0),\quad(0,a),\quad(a,\infty).\]
Exponentiation is injective, so these give four distinct positive solutions of (1). Lemma 4.1 proves the claim.

## Separate algebra check in the original variable

The same signs can be checked without hyperbolic functions. At \(r=1\), both atom integrands equal
\[\frac{10}{101-20\cos R}\le\frac{10}{101}<\frac1{10}.\]
At \(r=10\), the atom \(\xi=1/10\) contributes, including its mass one half,
\[\frac1{2(2-2\cos R)}=\frac1{4(1-\cos R)}\ge\frac18.\]
At \(r=1/10\), the atom \(\xi=10\) gives the same lower bound. The integral tends to zero as \(r\downarrow0\) and as \(r\uparrow\infty\). Thus there are crossings in \((0,1/10),(1/10,1),(1,10),(10,\infty)\). These strict rational inequalities include the boundary time \(5\pi\), for which \(R_t=\pi/2\).

## Adversarial checks and limits

The crucial direction is the equivalence in Lemma 4.1, rather than a merely sufficient unimodality condition. Its full statement and proof must remain pinned to the source. The four crossings concern a positive density level, not just multiple extrema in an auxiliary transform. The time is selected separately for each \(t\), as the criterion permits. The upper bound on the central value is uniform for \(R\ge\pi/2\); the lower bound at the two flanks is uniform for all \(R\in(0,\pi)\). No numerical root finder or plot is used as proof. The argument only needs failure for arbitrarily large times; it proves failure for every time in the displayed half-line. It makes no assertion about smaller times or optimality of \(5\pi\).

The large-time mechanism can also be understood from \(K_R(s)\to[4\cosh^2(s/2)]^{-1}\) as \(R\uparrow\pi\): its width does not diverge. A separated two-point mixture of this limiting kernel remains bimodal. This observation motivated the construction; the finite-time rational inequalities above are the proof.

Focused primary-source searches on 6 September 2026 found the original paper, the authors' current publication pages, and Auer's 2026 paper on the law started at one. No matching later resolution of this exact compact-initial-law question was verified. This is not a certificate of current openness or originality. Author review and source checking are separate from independent review, which is pending.


## Scoped parent review receipt

The parent independently reviewed the historical question and the checked construction. Its report is at `~/<private-repo>/12_cognitive_architecture/audits/reports/2026/09/06/last200-implementation/P0193_compact_multiplicative_candidate_review.md`, SHA256 `25f7346145df9adc8b33ff33d802994613bd24342b25825c6cbc7df0d8d9261a`. The report found no gap in its checked scope. Structural validation is not mathematical certification. Present openness, novelty, human review, and unique canonical audit-node binding remain unverified. This receipt does not promote the result to an original solution.
