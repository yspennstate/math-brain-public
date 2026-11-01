# R42 verification - supercritical directional branch

Date: 2026-06-28.

Scope: downstream phase-retrieval packaging of
`rect:directional-row-fixed-excess`, not a new exact RMT theorem.

## Five-agent audit

Exactly five read-only agents were launched.

- Sartre (`019f0d71-97f5-7440-9dab-276dbfed72bc`) checked the row count:
  for \(N=2m-1+r\) and \(p=r+1\),
  \[
    \binom{N-p}{m-1}=\binom{2m-2}{m-1},
    \qquad
    m^{-1}\log\binom{2m-2}{m-1}\to\log4.
  \]
  The resulting lower-side base is \(\log4/(r+1)\) over the reals.
- Volta (`019f0d71-98d5-7380-a8e3-8cf5a4bd7bca`) supplied wording guardrails:
  define a fixed-excess branch statistic, and do not call it the full
  Balan--Wang statistic for \(r>0\).
- Banach (`019f0d71-99a0-7781-ae38-0865c6982900`) confirmed this is not a
  duplicate of the critical directional corollary and recommended insertion
  after the supercritical measurement-count remark.
- Linnaeus (`019f0d71-9a6e-7d53-9e57-e3cecddcd64c`) checked assumptions:
  directional small-ball gives full spark almost surely, but full spark does
  not identify the branch with the full supercritical lower-Lipschitz statistic.
- Hubble (`019f0d71-9b32-7952-8570-4c472f4a9e48`) verified the finite-budget
  specialization:
  \[
    \mathcal B_{m,r}^{\rm dir}
    =
    \binom{2m-2}{m-1}
    \sum_{|S|=r+1}\prod_{i\in S}L_{m,i},
  \]
  with extra slack \(\frac{r+1}{2}\log m\) in the real case.

## Integrated Statement

For fixed \(r\ge1\) and \(A_m\in\mathbb R^{(2m-1+r)\times m}\), define
\[
  \omega_r^{\rm fe}(A_m)=
  \min_{|T|=m+r}\sigma_{\min}((A_m)_T).
\]
If the independent rows satisfy affine directional small-ball bounds with
constants \(L_{m,i}\) and
\[
  \frac1m\log
  \sum_{|S|=r+1}\prod_{i\in S}L_{m,i}\to0,
\]
then for every \(\varepsilon>0\),
\[
  \mathbb P\{\omega_r^{\rm fe}(A_m)
  \le \exp[-(\log4/(r+1)+\varepsilon)m]\}\to0.
\]
On a common coupling the same estimate gives the a.s. lower envelope by taking
summable slack \(u_m=2\log m\).

## Guardrails

- This is the deficient-complement fixed-excess branch of the Balan--Wang
  partition geometry.
- For \(r>0\), both-spanning partitions can enter the full lower-Lipschitz
  statistic; see the killed R14 supercritical reduction.
- No full supercritical Balan--Wang theorem, upper side, or exact law is
  claimed.
