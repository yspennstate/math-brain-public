# PROB20-20 backfill — recovered prior completed task response

**Recovery provenance:** recovered verbatim-in-substance from the immediately preceding completed automation response available in conversation context. The prior run attempted a GitHub write but no commit receipt/readback was exposed, and bounded repository search at restart found no copy under the requested task root. This file therefore archives the genuine prior mathematics rather than inventing missing history.

**Original status:** PARTIAL. The full Janson Problem 18.39 remained open.

## Exact target and source quantifiers

For one fixed weighted-allocation law in the supercritical regime
\[
0<\nu<\lambda,\qquad m_n/n\to\lambda,
\]
Janson Problem 18.39 asks whether \(Y_{(1)}/n\to_p0\) can hold along the full admissible sequence. Example 18.36 gives this only on a subsequence; Janson conjectures that full-sequence disappearance is impossible and more strongly predicts a fixed \(\varepsilon>0\) and a subsequence on which \(Y_{(1)}>\varepsilon n\) w.h.p.

After valid finite-mean boundary normalization,
\[
\pi_k=\frac{w_k\rho^k}{\Phi(\rho)},\qquad \sum_k\pi_k=1,\qquad \sum_k k\pi_k=\nu,
\]
and the allocation is the iid vector \((\xi_1,\ldots,\xi_n)\), \(\xi_i\sim\pi\), conditioned on \(S_n=m_n\). The normalized generating radius is one.

The prior run rechecked Janson Theorem 17.1 and Lemma 18.31. Theorem 17.1 implies the exact conditioning atom is subexponential:
\[
\frac1n\log\Pr(S_n=m_n)\to0.
\]
Lemma 18.31(ii) was explicitly **not** used at an arbitrary fast cutoff; its equality statement only holds below an existentially slow sequence \(\Omega_n\).

## Exact conditioning cost

Set
\[
p_n=\Pr(S_n=m_n),\qquad b_n=-\log p_n.
\]
Then
\[
\boxed{b_n\to\infty,\qquad b_n=o(n).}
\]
The first assertion follows from the weak law because \(m_n/n\to\lambda>\nu\); the second is Theorem 17.1.

Define
\[
K_n=\left\lfloor\frac{n}{b_n}\right\rfloor.
\]
Then \(K_n\to\infty\) and \(K_n=o(n)\).

## Universal truncated-overload saddle

For a cutoff \(K\), put
\[
Z_K=\xi\mathbf1_{\{\xi\le K\}},\qquad L_K(t)=\log\mathbb E e^{tZ_K}.
\]
Fix \(\mu>\nu\). For large \(K\), let \(t_K>0\) solve \(L_K'(t_K)=\mu\), and set
\[
J_K(\mu)=\mu t_K-L_K(t_K).
\]
The prior run proved, without variance, regular variation, or a local limit theorem,
\[
\boxed{t_K\to0,\qquad Kt_K\to\infty,\qquad J_K(\mu)\sim(\mu-\nu)t_K.}
\]
The proof uses: fixed positive tilt forces the truncated tilted mean to diverge; bounded \(Kt_K\) would permit dominated convergence back to mean \(\nu\); the saddle identity bounds the endpoint normalizer; Hölder gives convergence of every strict fractional tilt back to \(\nu\); integration of \(\mu-L_K'\) yields the rate asymptotic.

## Positive linear mass above the self-consistent scale

Write \(\delta=\lambda-\nu\), \(c=\delta/2\), and under the conditioned allocation
\[
T_n=\sum_iY_i\mathbf1_{\{Y_i>K_n\}}.
\]
Then the prior run proved
\[
\boxed{\Pr(T_n\ge cn\mid S_n=m_n)\to1.}
\]
Indeed, if \(T_n<cn\), the contribution from boxes at most \(K_n\) is at least \((\nu+\delta/3)n\) for all large \(n\). Chernoff plus the saddle asymptotic gives an unconditioned probability
\[
\exp\{-nJ_{K_n}(\nu+\delta/3)\}
=\exp\{-\omega(b_n)\},
\]
which remains negligible after division by \(p_n=e^{-b_n}\).

Consequently,
\[
Y_{(1)}>K_n\sim n/b_n
\quad\text{w.h.p.},
\]
and at most \((\lambda+o(1))b_n\) boxes can exceed \(K_n\).

## Exact factorial tail bounds

Put
\[
q_k=k\pi_k,
\qquad
Q(K,L)=\sum_{K<k\le L}q_k,
\qquad
Q(K)=\sum_{k>K}q_k.
\]
For a configuration \(y\), define
\[
F_r^{(K,L)}(y)
=
\sum_{\substack{i_1,\ldots,i_r\\\text{all distinct}}}
\prod_{j=1}^r y_{i_j}\mathbf1_{\{K<y_{i_j}\le L\}}.
\]
Then exactly
\[
\boxed{
\mathbb E[F_r^{(K,L)}(Y)\mid S_n=m_n]
\le n^rQ(K,L)^re^{b_n}.
}
\]
This follows by expanding over ordered distinct coordinates and occupancies, bounding the residual atom by one, and dividing by \(p_n\).

If
\[
T_{K,L}(y)=\sum_i y_i\mathbf1_{\{K<y_i\le L\}},
\qquad M(y)=\max_i y_i,
\]
then deterministically
\[
\boxed{
F_r^{(K,L)}(y)
\ge
T_{K,L}(y)^r
\left(1-\binom r2\frac{M(y)}{T_{K,L}(y)}\right).
}
\]
The proof subtracts ordered products with repeated indices and bounds each repeated-pair contribution by \(M T^{r-1}\).

## Universal entropy-tail lower bound on the maximum

With \(K_n=\lfloor n/b_n\rfloor\), set
\[
Q_n=Q(K_n),\qquad L_n=\log\frac{c}{Q_n},
\]
and for large \(n\)
\[
r_n=\max\left\{2,\left\lceil\frac{2b_n}{L_n}\right\rceil\right\},
\qquad
\eta_n=\frac{c}{4r_n^2}.
\]
The prior run proved
\[
\boxed{\Pr(Y_{(1)}<\eta_nn\mid S_n=m_n)\to0}
\]
and
\[
\boxed{
\eta_n\ge
\frac{c}{36}
\min\left\{1,\left(\frac{L_n}{b_n}\right)^2\right\}.
}
\]
Thus
\[
\boxed{
\frac{Y_{(1)}}n
\ge
\frac{c}{36}
\min\left\{1,
\left(
\frac{\log(c/Q(n/b_n))}{b_n}
\right)^2
\right\}
\quad\text{w.h.p.}
}
\]
(up to the floor in \(K_n\)).

Hence Janson's macroscopic-subsequence conclusion follows if
\[
\liminf\frac{\log(1/Q(n/b_n))}{b_n}>0
\]
along some subsequence. Conversely, every full no-condensation counterexample must satisfy
\[
\boxed{\log\frac1{Q(n/b_n)}=o(b_n).}
\]

## Truncated-band obstruction removing irrelevant future tail

For fixed small \(\eta>0\), define
\[
Q_n(\eta)=\sum_{K_n<k\le\eta n}k\pi_k.
\]
For every fixed integer \(r\ge2\) satisfying
\[
\binom r2\frac{\eta}{c}\le\frac14,
\]
the prior run proved
\[
\boxed{
\Pr(Y_{(1)}\le\eta n\mid S_n=m_n)
\le o(1)+2\exp\left\{b_n-r\log\frac{c}{Q_n(\eta)}\right\}.
}
\]
Therefore, under full no-condensation,
\[
\boxed{
\log\frac{c}{Q_n(\eta)}\le\frac{b_n}{r}+O(1).
}
\]
Taking \(r\asymp\eta^{-1/2}\) gives the necessary condition
\[
\boxed{
\log\frac1{Q_n(\eta)}\le O(\sqrt\eta\,b_n)+O(1).
}
\]
Thus a hypothetical counterexample must retain unexpectedly large size-biased mass in every fixed macroscopic band \((n/b_n,\eta n]\); the failure of the earlier full-tail criterion cannot be blamed only on inaccessible values above the putative maximum.

## Variational cutoff form

For any deterministic \(K_n\to\infty\) satisfying
\[
nJ_{K_n}(\nu+\delta/3)-b_n\to+\infty,
\]
the positive-linear-mass argument works with that cutoff, and the same factorial bounds give lower bounds on \(Y_{(1)}\) in terms of \(Q(K_n)\) or \(Q(K_n,\eta n)\).

The remaining deterministic optimization problem recorded by the prior run was whether every finite-mean radius-one law and every admissible supercritical centering must possess a subsequence/cutoff where the truncated-overload cost beats \(b_n\) while the relevant size-biased band mass is exponentially small on the \(b_n\)-scale.

## Prior run ledger

**PROVED (self-checked, not independently/formally verified):** exact conditioning-cost scale; truncated saddle asymptotics; linear mass above \(n/b_n\); factorial tail upper bound; repeated-index correction; entropy-tail maximum lower bound; truncated-band obstruction; variational cutoff extension.

**OPEN:** force the entropy-tail criterion along some subsequence for every fixed law, or build a single fixed-law full-sequence counterexample satisfying all band-mass constraints.

**Failed/insufficient routes retained:** generic subexponential one-big-jump theorems require hypotheses not available here; local CLTs cannot be assumed; raw partition counts are too coarse; Lemma 18.31(ii) cannot be used at arbitrary cutoffs; record gaps alone do not control exact conditioning atoms.

**Verification level:** self-review only. No universal solution claim was made.
