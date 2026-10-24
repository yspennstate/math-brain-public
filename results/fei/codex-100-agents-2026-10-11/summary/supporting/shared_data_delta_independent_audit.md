# Independent audit of the shared-data multiplexer delta

**Date:** 11 October 2026. **Status:** analytic delta reviewed internally; exact finite checker replayed. No mathematical correction is required for the added statements. This is an internal mathematical audit, not external peer review or a claim of novelty.

## Pinned scope

The comparison is between the previously completed source with SHA256

`3a395e98153f826fa9160c348e45779f204d3ea77376f40cd71ee57440ba8193`

and the retrieved 38-page source with SHA256

`5cff9d1b91c92883a6d35ec7674ff5953365cadc85299747e4047d9deb150dac`.

The new packaged PDF was independently hashed and matches

`182eba4219e14b7f87200a7d99d2755acc81d41198e4990902986909c19504bc`.

The source diff consists of an abstract adjustment and the inserted subsection with LaTeX label `sec:shared-multiplexers`. The implementation audit identifies this as Section 8.2. No earlier theorem or proof was changed by this source delta. This audit covers the added mathematics, not a fresh reconstruction of every unchanged baseline proof.

The retrieved source is `paper_v2/fourier-entropy-threshold-functions/paper/main.tex` relative to this audit. The prior implementation audit was read after independently checking the source delta; it is retained as `shared_data_extension_audit_2026-10-11.md`.

## Exact assumptions

At a multiplexer node:

1. The physical selector is a uniform block \(x\in\{-1,1\}^a\).
2. Every branch \(g_b\), indexed by \(b\in\{-1,1\}^a\), is a Boolean sign function on a common uniform data cube \(y\), independent of \(x\).
3. Branches may be biased, share data variables, and have overlapping Fourier supports.
4. For the orthogonal-neighbor closure, \(\mathbb E_y[g_b g_{b^{(j)}}]=0\) for every selector edge \((b,b^{(j)})\). Orthogonality is required for neighboring labels; it is not required for all pairs of labels.
5. The more general closure replaces that orthogonality condition by \(I_{\rm sel}(F)\ge ca\), where \(c>0\), while retaining the independent physical selector and branch FEI hypotheses.

For recursive closure, every newly introduced selector block occurs in none of that node's branches, and the relevant closure hypothesis holds at every internal node. All variables entering a node can be viewed on their common union cube by adding irrelevant coordinates. Leaves are regular Boolean functions, so the baseline ordinary FEI bound with coefficient \(C_{\rm reg}<8.937\) applies. The construction is finite; there is no bound on its finite depth, fan-in, or pattern of branch-data reuse.

## Analytic reconstruction

### Conditional spectral identity

Let \(N=2^a\), \(F(x,y)=g_x(y)\), and for each data Fourier set \(T\) write

\[
R_T=\frac1N\sum_b\widehat g_b(T)^2.
\]

For \(R_T>0\), define

\[
r_T(b)=\frac{\widehat g_b(T)^2}{NR_T},\qquad
u_T(b)=\frac{\widehat g_b(T)}{\sqrt{NR_T}},\qquad
\nu_T(S)=\left(\frac1{\sqrt N}\sum_b\chi_S(b)u_T(b)\right)^2.
\]

Both \(r_T\) and \(\nu_T\) are probability laws: the former by its normalization, and the latter because the normalized Walsh transform is orthogonal. Direct expansion gives

\[
\widehat F(S,T)=\frac1N\sum_b\chi_S(b)\widehat g_b(T),
\qquad
\widehat F(S,T)^2=R_T\nu_T(S).
\]

Thus \(R\) is the data-set marginal of \(\widehat F^2\). Independently, the joint probability law
\(\Pr(B=b,T)=N^{-1}\widehat g_b(T)^2\)
has uniform branch marginal, data marginal \(R\), and conditional branch law \(r_T\). Applying the entropy chain rule to these two laws yields exactly

\[
H(F)=a+\frac1N\sum_bH(g_b)
+\sum_{T:R_T>0}R_T[H(\nu_T)-H(r_T)].
\]

The empty data set is included. There is no balancedness assumption and no treatment of a coherent sum as an ordinary incoherent mixture. The interference appears in the explicit difference of the conditional entropies. Since \(H(\nu_T)\le a\) and \(H(r_T)\ge0\),

\[
H(F)\le2a+\frac1N\sum_bH(g_b).
\]

All normalizations and inequality directions in `prop:shared-data-collision` are correct.

### Influence and closure

Conditioning on the physical selector gives

\[
I_{\rm data}(F)=\frac1N\sum_b I(g_b),\qquad
I_{x_j}(F)=\frac1N\sum_b\Pr_y[g_b\ne g_{b^{(j)}}].
\]

For sign functions, \(\Pr[g_b\ne g_{b^{(j)}}]=(1-\mathbb E[g_bg_{b^{(j)}}])/2\). Consequently, neighboring orthogonality gives \(I_{\rm sel}(F)=a/2\). If every branch satisfies \(H(g_b)\le C I(g_b)\), then

\[
H(F)\le4I_{\rm sel}(F)+CI_{\rm data}(F)
\le\max\{4,C\}I(F).
\]

Under the more general condition \(I_{\rm sel}(F)\ge ca\), the same argument gives the coefficient \(\max\{2/c,C\}\). The spectral expression for selector influence is also exact, because \(R_T\nu_T(S)\) is the full spectral probability and selector degree is \(|S|\).

Applying the orthogonal-neighbor closure at each internal node preserves \(C_{\rm reg}\), since \(C_{\rm reg}>4\). Adding irrelevant coordinates to obtain a common data cube changes neither branch entropy nor branch influence. This validates the induction in `cor:recursive-multiplexers` without any loss depending on depth or data reuse.

## Verification performed

The supplied `verify_shared_data_multiplexers.py` was read and executed. It returns PASS on all 256 ordered pairs of Boolean functions on two shared data variables, including 96 orthogonal pairs. The collision identity, entropy inequality, and influence identity are checked with exact rational Fourier coefficients. Entropy is represented by rational coefficients of logarithms of primes; inequality signs are checked by clearing denominators and comparing positive integers. These are exact finite checks, not floating-point approximations or a proof in all dimensions.

The shared-majority example was checked separately using an independent rational Walsh calculation:

\[
g_+=\operatorname{Maj}_3(y_1,y_2,y_3),\qquad
g_-=\operatorname{Maj}_3(y_1,-y_2,y_4).
\]

Their inner product is zero. Their one-bit multiplexer has exactly two spectral atoms of mass \(1/4\), eight of mass \(1/16\), entropy \(3\), and influence \(2\), as stated in the manuscript.

## Consequence for the campaign frontier

F11 should treat the exact shared-data identity, the uniform complete-selector entropy upper bound, neighboring-orthogonal closure, and recursive regular-leaf closure as part of the current baseline. The selector-influence lower-bound version is also already proved: weakening orthogonality merely to a fixed positive average disagreement is not a remaining target.

Live directions include paying the collision correction when selector influence is small; nonuniform or nonrecursive affine-cell selectors; and composition settings without a fresh independent physical selector at each node. The arbitrary shared signed-dictator encoding \(F(z,y)=f(z)y\) remains outside the orthogonal-neighbor class: adjacent signed-dictator branches have inner product \(+1\) or \(-1\), never zero. The new theorem therefore does not absorb the unrestricted FEI reduction.

The campaign narrative should cite the updated baseline and these precise hypotheses. The audit itself makes no publication action and does not authorize replacing the new release with the earlier 36-page source or PDF.
