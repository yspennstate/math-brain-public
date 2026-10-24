# R10 verification: random row weights and row normalization

Date: 2026-06-27.

Round discipline: exactly 5 read-only audit agents were launched.

## Agent reports

1. Anscombe audited iid Gaussian row normalization. Verdict: valid. For
   \(U_T=D_TG_T\), the pathwise comparison
   \(M_G/R_{\max}\le M_U\le M_G/R_{\min}\) holds, and over \(N=O(m)\)
   Gaussian rows both \(R_{\max}\) and \(R_{\min}^{-1}\) are
   \(e^{o_{\mathbb P}(m)}\). The \(\sqrt m\) norm scale contributes only
   \(O(\log m/m)\).

2. Nietzsche audited the general random row-weight theorem. Verdict: valid.
   Positive random weights may depend on the matrix. The exact assumption is
   \(\max_i|\log w_i|=o_{\mathbb P}(a_m)\) and \(M_m(A)>0\) with high
   probability. Zero weights must be excluded.

3. Locke audited non-Gaussian row normalization. Verdict: lower-side transfer
   is valid under explicit row-tail control. Bounded density alone proves the
   lower side for the unnormalized matrix but does not imply
   \(\max_i\|A_i\|=e^{o_{\mathbb P}(m)}\) for pathological heavy-tailed laws.
   No lower row-norm tail is needed for lower-side transfer.

4. Boyle audited phase-retrieval implications. Verdict: row-normalized iid
   real Gaussian frames at \(N=2m-1\) preserve the Balan--Wang singular-value
   base \(1/4\). The statement should refer to the Balan--Wang
   singular-value statistic \(\omega\); other conventions may square the
   statistic.

5. Dirac audited manuscript placement. Verdict: insert the transfer after the
   deterministic conditioning result, record a V.B-rand ledger row, and mirror
   the Lane O state. Dirac suggested unnumbered paragraphs to avoid theorem
   renumbering; the integration uses numbered theorem environments because the
   transfer is a reusable proved result and references are label-based.

## Integrated result

The manuscript now contains:

- Proposition `prop:random-row-weight`, a pathwise random positive diagonal
  transfer for arbitrary row-submatrix families and scales \(a_m\).
- Corollary `cor:row-normalized-gaussian`, proving the exact Gaussian
  row-normalized extremal base.
- Corollary `cor:pr-normalized-gaussian`, proving
  \(\omega(U_m)=4^{-m+o_{\mathbb P}(m)}\) for real normalized Gaussian
  critical frames.
- A non-Gaussian normalized-row lower-side remark with an explicit maximum
  row-norm tail hypothesis.

