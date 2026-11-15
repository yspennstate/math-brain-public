# T136 verification — round 6, 15 November 2026

The literature verdict is **PARTIAL-CLAIMED**: the candidates claim the fixed finite-temperature part of our row, and do not claim ground-state fluctuation order or a ground-state limiting law. This continuation independently rechecks round 5's conditional scalar moment lemma and proves the finite-depth signed compression identity E5; it does not certify the complete preprints.

All three candidates have author **OpenAI**. Exact TeX quotations below come from sources freshly opened through the read-only GitHub connector and saved in sources/. The repository's Apache-2.0 LICENSE is retained from the preceding round. No proof-correctness conclusion for the full papers or independent Lean replay is asserted.

## 1. The low-temperature Sherrington–Kirkpatrick free-energy limiting law

September 24, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/build/sections/01-introduction.tex), with the definitions and theorems. Main theorem, exactly:

```tex
\begin{theorem}[Limiting law]\label{thm:main}
For every fixed real $\beta>1$, there is a nondegenerate Borel probability measure $\nu_\beta$ such that
\[
 X_n(\beta)\ \Longrightarrow\ \nu_\beta
 \qquad\text{as }n\to\infty\text{ through all integers}.
\]
The measure $\nu_\beta$ has mean zero, variance one, and a finite exponential moment in a neighborhood of the origin. It is the unique probability measure with the moments specified in Proposition~\ref{def:law} below.
\end{theorem}
```

Its fluctuation-scale moment theorem is exactly:

```tex
\begin{theorem}[Moment convergence at the fluctuation scale]\label{thm:moments}
For each fixed $\beta>1$, there are real numbers $a_k=a_k(\beta)$, $k\ge1$, with the following property. For every integer $k\ge1$, there are constants $c_k>0$ and $C_k<\infty$ such that
\begin{equation}\label{eq:moment-rate}
 \big|\mathbb E Y_n^k-a_k\big|\le C_k n^{-c_k},\qquad n\ge2.
\end{equation}
There are also constants $c>0$ and $C<\infty$, depending on $\beta$, for which
\begin{equation}\label{eq:exponential-moments}
 \sup_{n\ge2}\mathbb E e^{c|Y_n|}\le C.
\end{equation}
The limits satisfy $a_1=0$ and $0<a_2<\infty$.
\end{theorem}
```

The law is specified by this proposition, exactly:

```tex
\begin{proposition}[Moment specification]\label{def:law}
Fix $\beta>1$ and let $C=\sum_{l=2}^{\infty}l^{-2}$. For an integer $k\ge1$, draw an integer $J\ge2$ with
\[
 \mathbb P(J=l)=\frac{l^{-2}}C.
\]
Conditional on $J$, draw $k+1$ independent copies $F_J^{c,0},\ldots,F_J^{c,k}$ of the completed free energy in \eqref{eq:completed-free-energy}. Set
\[
 t=\log J,
 \qquad P_k=\prod_{i=1}^k J^{-1/6}(F_J^{c,0}-F_J^{c,i}).
\]
Conditional averaging over the independent comparison copies gives
$\mathbb E[P_k\mid J=l]=\mathbb E Y_l^k$.
The constants in Theorem~\ref{thm:moments} satisfy
\begin{equation}\label{eq:law-moments}
 a_k=C\sum_{h=0}^{\infty}
 \mathbb E\!\left[P_k\left(\frac{t^h}{h!}
       -\mathbf1_{\{h\ge1\}}\frac{t^{h-1}}{(h-1)!}\right)\right],
\end{equation}
where the second term is absent for $h=0$. Each expectation is taken before the series is summed. The series of these scalar expectations is absolutely convergent. We have $a_2>0$, and the law in Theorem~\ref{thm:main} is uniquely determined by
\[
 \int z^k\,\nu_\beta(dz)=\frac{a_k}{a_2^{k/2}},\qquad k\ge1.
\]
\end{proposition}
```

The model is exactly our Gaussian Ising SK Hamiltonian, with the sum over i<j, coefficient n^(-1/2), zero external field, and unnormalized spin sum. The paper sets F_n=log Z_n, s_n^2=Var(F_n), and X_n=(F_n-EF_n)/s_n. Its completion is F_n^c=F_n-n log 2+zeta_n, with independent Gaussian variance beta^2/2, and Y_n=n^(-1/6)(F_n^c-EF_n^c). Therefore
\[
 n^{-1/3}\operatorname{Var}(F_n)=\mathbb E Y_n^2-\frac{\beta^2}{2n^{1/3}}
 \longrightarrow a_2(\beta)\in(0,\infty).
\]
The claim is a positive variance equivalent and a full-sequence, moment-characterized limiting law after exact expectation centering and exact standard-deviation normalization. It gives neither a familiar named distribution nor a separately evaluated formula for the variance constant. It covers each fixed finite real beta>1, with temperature-dependent constants; it supplies no uniform beta-to-infinity estimate.

## 2. The low-temperature Sherrington–Kirkpatrick fluctuation scale

September 24, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/build/sections/introduction.tex). Main theorem, exactly:

```tex
\begin{theorem}\label{thm:main}
For every fixed $1<\beta<\infty$,
\[
 \sd(F_n)=n^{1/6+o(1)},\qquad \Var(F_n)=n^{1/3+o(1)}.
\]
More explicitly, for every $\eta>0$ there is $n_0(\beta,\eta)$ such that
\[
 n^{1/6-\eta}\le\sd(F_n)\le n^{1/6+\eta}
 \qquad(n\ge n_0(\beta,\eta)).
\]
Moreover, for every $\eta>0$,
\[
 \mathbb P\!\left(n^{1/6-\eta}\le|F_n-\mathbb EF_n|
                         \le n^{1/6+\eta}\right)\longrightarrow1.
\]
\end{theorem}
```

The paper absorbs beta into H and uses the uniform spin sum. Its F_n equals our log Z_n(beta) minus n log 2, so its centered fluctuations and variance are exactly ours. It claims the exponent and a typical centered magnitude with every positive power slack. This is weaker than a variance equivalent with positive constant and does not assert a limiting law; it assumes 1<beta<infinity fixed.

## 3. Full support of the zero-temperature Sherrington–Kirkpatrick order parameter

September 27, 2026. Opened the actual [main source](https://github.com/openai/math/blob/main/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/build/main.tex). Main theorem, exactly:

```tex
\begin{theorem}[Full support at zero temperature]\label{thm:full-support}
If $\gamma\in\mathcal U$ minimizes $\mathcal P$, then
\[
 \supp\mu_\gamma=[0,1).
\]
In particular $\gamma(b)>\gamma(a)$ whenever $0\leq a<b<1$.
For the solution of~\eqref{eq:model-diffusion},
\begin{equation}\label{eq:main-consistency}
 \E[u_\gamma(t,X_t)^2]=t,\qquad
 \E[\Phi_{\gamma,xx}(t,X_t)^2]=1,
 \qquad 0\leq t<1.
\end{equation}
\end{theorem}
```

The finite-system Hamiltonian is ours, but gamma is a deterministic minimizer of the zero-temperature Parisi functional. Its Stieltjes support and diffusion identities are different quantities from sample-to-sample fluctuations of max H_n. This candidate is NOT-THIS for the requested ground-state fluctuation problem.

## Word-by-word scope comparison

| Our requirement | What the candidates cover |
| --- | --- |
| Ising spins; iid standard Gaussian g_ij; zero field | Exact agreement for the first two candidates. The third starts from the same model. |
| N^(-1/2) sum over i<j | Exact agreement; candidate 2 places beta in H and divides the spin sum by 2^n, a deterministic shift in log Z. |
| Dimension and range | Mean-field complete graph, no spatial dimension parameter; all integer system sizes. |
| Each fixed beta>1 | All finite fixed beta>1, with no uniform control at infinity. |
| Fluctuations of log Z_N(beta) | Exact centered quantity in candidates 1–2. |
| Determine the order | Candidate 1 claims a positive variance equivalent; candidate 2 claims only exponent 1/3 with power slack. Both give standard-deviation exponent 1/6. |
| Determine the limiting law | Candidate 1 claims full-sequence convergence to a unique moment-characterized standardized law. Candidate 2 does not. |
| Ground-state maximum | No variance order or limiting law for it is claimed in these three papers. |

For M_n=max H_n, the deterministic bound 0<=beta^(-1)log Z_n(beta)-M_n<=n log 2/beta gives the same bound for the absolute difference of centered variables. To make this bound negligible relative to n^(1/6) would require beta_n/n^(5/6) tending to infinity. A theorem for each fixed beta cannot be substituted into that growing-temperature regime. This identifies why this elementary transfer does not settle zero temperature.

## Follow-ups opened in this continuation

The update search used the web search tool and was limited to five minutes. Queries included the title with error/correction/refutation terms and SK ground-state limiting laws in 2026. No later settlement of the whole row, arXiv version of the two OpenAI candidates, refutation, error report, referee report, or specialist verification of their complete proofs surfaced; this is a bounded search result.

| Opened source | What was established from it |
| --- | --- |
| P. M. Aronow and Patrick Lopatto, [Lower and Upper Bounds for Glauber Dynamics from Typical States of the Low-Temperature Sherrington–Kirkpatrick Model](https://hexagonmath.org/2610.00402v1), October 20, 2026 | The primary landing page reports formalizing the fluctuation exponents and proving the positive-Laplace-window input. Its identifier belongs to Hexagon, not arXiv. This is not a claim to formalize the limiting law. |
| [fluctuations-palomar README](https://github.com/pmaronow/fluctuations-palomar/blob/main/README.md) | The actual current file excludes a fluctuation limit law and positive variance prefactor. Historical replay receipts apply to named revisions according to the authors; replay of a strengthened interface remains pending. Fresh text is unchanged from round 5. No local build/replay was run. |
| Yan Ru Pei, [Upper deviations of the Sherrington-Kirkpatrick free energy: the fifth-order law and the onset of constrained Parisi measures](https://arxiv.org/abs/2610.06480), v3 revised November 11, 2026; [actual HTML](https://arxiv.org/html/2610.06480v3) | The page still reports v3. Its large-deviation order of limits differs from a central fluctuation limit, and supplies no settlement of the ground-state question. |
| OpenAI, [EventuallyNatPos.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/SKFluctuations/EventuallyNatPos.lean) | Read the actual main_of_positiveLaplaceWindow declaration: PositiveLaplaceWindow is an explicit hypothesis. This is a conditional exponent theorem. |
| OpenAI, [lean/docs/281.md](https://github.com/openai/math/blob/main/lean/docs/281.md) | Documents ground-state-value identities and full support of an admissible minimizer, not sample-to-sample fluctuation scale or a limiting law. |

The two introductions, zero-temperature main source, limiting-law Section 9, companion foundations, Lean file, Lean scope document, and external README were freshly opened through the read-only GitHub connector in round 6. Other context files, including limiting-law Sections 2–4 and 7–8, 10 and the repository license, were read from inherited round-5 snapshots. Exact local snapshots, links, provenance and hashes are retained in sources/INDEX.md and audit.txt. No git command, repository checkout, post, account, external message, Lean build, or GPU computation was used.

## Recommended replacement for “where it stands”

OpenAI’s unrefereed *The low-temperature Sherrington–Kirkpatrick free-energy limiting law* (September 24, 2026), with its companion *The low-temperature Sherrington–Kirkpatrick fluctuation scale* (September 24, 2026), claims variance asymptotic to a positive constant times N^(1/3) and a moment-characterized limiting law for exactly centered and standardized log Z_N(beta) at every fixed finite beta>1. P. M. Aronow and Patrick Lopatto subsequently report formalizing the exponent theorem; the stronger variance equivalent and limiting law remain unverified in this audit. The ground-state fluctuation order and limiting law remain open on the evidence checked; *Full support of the zero-temperature Sherrington–Kirkpatrick order parameter* (September 27, 2026) concerns the deterministic Parisi minimizer instead.

## Spot check

Round 5's scalar source estimates survive independent rechecking. The branching Itô product and a separate conditional-variance calculation both give E[P_A P_B]=chi²+chi³k0 c²+g²k0²v²/2+O(c³). Parity at the earlier split retains the O(ch) triple error, including h=0, under the preceding regularity assumptions. The local copy recheck_round5.py repeats the 20 rational generator cases, 24 Wick checks, five size cancellations and finite hierarchy checks, writing only here.

The new result is a proof of the finite-depth version of the signed compression identity (E5). [PROOF.md](PROOF.md) derives a coefficientwise common-refinement identity for colored marked trees, preserving terminal coincidences between different cumulant parts. It derives the labeled real-power source rule directly at real masses and checks the external skeleton normalization W_cut/c^D. Each used block in each cumulant part contributes one source factor c s_k, which yields exactly c^(D_pi). The two-edge repeated-block formula and the AB,AC formula agree with the manuscript.

[audit.py](audit.py) checks 184 marked-refinement identities and 1,518 restricted-shape coefficients, independently counts 76,968 actual named-leaf assignments, checks 96 source derivatives against generalized-binomial jets, and compares 24 direct cumulant sums with the compressed formula on 12 graph families (4,735 full internal placements). Physical noninteger masses, repeated masses, terminal mass four, a very small first mass, nonbinary forks and repeated terminal labels are included. Removing a cross-part terminal coincidence deliberately breaks the two-slot identity: 1/8−7/64=1/64, whereas the distinct-only coefficient is −7/64. Commands, implementation failure and measured output are recorded in LOG.md and audit.txt.

The first audit failure was a tree-encoding bug: restricting an unordered tree must reorder its children by their first surviving slot. Correcting that representation passed all checks. This was not a counterexample to the signed identity. The scalar examples in the direct cumulant audit have zero future Gaussian increments and fixed nonzero cut fields; the coefficientwise marked tests retain arbitrary restricted-topology symbols. Continuous-clock limits, fixed-skeleton parameter differentiation, skeleton density bounds and the projected spin-model tests remain separate issues. Neither this finite identity nor the earlier scalar estimates verify the full stopped pressure increment or the limiting-law proof.

