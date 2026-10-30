# Source-bound handoff — fleet02/B13 joint-credit critical-core theorem

Full FEI remains open.

Source-current inputs actually used:

- all-gate reformulation `proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`;
- fleet04/B17 `20260922T031352Z-biased-restriction-margin-cocycle`, exact source-valid cocycle
  \(D_\Gamma=qD_0+tD_1+\mathcal R+\mathcal C\) with
  \(\mathcal C=H(B|S)+I(S;J)\);
- fleet04/B16 `20260922T040918Z-character-tube-joint-credit`, the one-common-character special case;
- fleet01/B18 `20260922T042319Z-two-exchange-support-rigidity`, latest A-lead obstruction update.

New theorem. At an unbiased physical pivot, for arbitrary actual Boolean children
\(f_0,f_1\) with disagreement \(\delta\),
\[
H(B|S)+I(S;J)
\ge
h_2\!\left(\frac{1-2\sqrt{\delta(1-\delta)}}2\right).
\]
Proof keeps the relative Fourier signs through the exact conserved moment
\[
\mathbb E_T[\sigma_Su_S]=1-2\delta
\]
and applies strict convexity of
\[
\Psi(u)=1+h_2((1-\sqrt{1-u^2})/2)-h_2((1-u)/2),
\quad
\Psi''(u)=\operatorname{artanh}(\sqrt{1-u^2})/
          ((1-u^2)^{3/2}\ln2)>0.
\]

Insertion into the exact B17 cocycle yields, for cap \(C=\Gamma(1/2)\),
\[
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge
\frac{\Gamma(r_0)+\Gamma(r_1)}2-\Gamma((r_0+r_1)/2)
+C\delta-1-h_2(\delta)
+h_2((1-2\sqrt{\delta(1-\delta)})/2).
\]

Corollary. For every symmetric potential with \(C\ge13/2\), if the pivot is
unbiased, both children are balanced and \(\delta\ge1/4\), then the exact local
contribution is strictly positive. Hence in a minimum-essential-arity balanced
central counterexample,
\[
\widehat f(\{i\})=0\Longrightarrow \operatorname{Inf}_i(f)<1/4.
\]
More generally every coordinate obeys
\[
C-\Gamma((1-|\widehat f_i|)/2)
>
C\,\operatorname{Inf}_i-1-h_2(\operatorname{Inf}_i)
+h_2((1-2\sqrt{\operatorname{Inf}_i(1-\operatorname{Inf}_i)})/2).
\]

Tensor/gauge scope: the joint-credit theorem is unchanged by multiplication of
both children by the same disjoint Boolean factor; at uniform nonpivot biases it
is also unchanged by a simultaneous character or nonpivot linear Walsh
permutation. These are theorem invariances, not free physical operations in the
gate induction. No analogous biased affine invariance is claimed.

Next exact gap: pay the unbalanced-child or \(\delta<1/4\) cases, or force a paid
pivot in every minimum critical core. Fleet04/B16 already removes the
one-character-tube part of the small-\(\delta\) sector.

Scientific report:
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T045511Z-joint-credit-critical-core/REPORT.md`.
