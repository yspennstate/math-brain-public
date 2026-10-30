# B12 handoff — explicit five-input prime center tube

Full FEI remains **OPEN / NOT PROVED**.

Live candidate:

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p).
\]

Consumed result: `fleet03/B18/20260922T065506Z-prime-central-orbits/REPORT.md`, blob `bdbc1c2378da80c6a7d1b1dbb02ceafa2496cc96`, which proves every essential five-input composition-prime gate has center slack at least `delta_5=0.004906502214` but leaves its common continuity radius nonexplicit.

New theorem: for **every** essential five-input composition-prime Boolean gate `P`,

\[
\max_i|p_i-1/2|\le2^{-18}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(P;p)>0.00029.
\]

The proof is gate-uniform and source-valid. For the actual signed biased Fourier coefficient vector `a(p)`,

\[
\partial_{p_j}a_S=
\begin{cases}
a_{S\cup\{j\}}/\sqrt{p_j(1-p_j)},&j\notin S,\\
\frac{1-2p_j}{2p_j(1-p_j)}a_S,&j\in S,
\end{cases}
\]

so on the `2^-18` cube `||a(p)-a(1/2^5)||_2<=15*2^-18`, giving spectral TV at most `15*2^-18`. Fannes--Audenaert costs `<315*2^-18`. Exact pivotal-probability transport plus the source potential costs `<470*2^-18+5 h_2(2^-34)`, and the output potential costs `<425*2^-18`. Total debit is

\[
1210\,2^{-18}+180\,2^{-34}=0.004615794168785214\ldots,
\]

leaving `0.000290708045... > 0.00029` from the inherited center reserve.

Owner-comparable base-potential margin consequence, when its denominator is positive:

\[
c_P(p)<0.267972856.
\]

Next useful target: five-input primes **outside** this explicit tube, preferably an interval-certified shell or an exact Boolean off-center falsifier. Higher-arity primes remain untouched.

Primary report: `fleet02/B12/20260922T072221Z-five-prime-explicit-tube/REPORT.md`.
