Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding model selector is exposed.**

# R7-07 immutable correction — scope of the uniform-escape corollary

Date: 2026-09-19 UTC  
Parent artifact: `research7_2026-09-17/R7-07/admissions/2026-09-19T131000Z__H0008_resolved_fresh_trials_roof_reduction.md`  
Parent creation commit: `070d13b9fb2859df68c52d567bdba5bc8195d068`

The main result of the parent artifact, **Theorem 4.2 (finite-roof reduction)**, is unchanged:

\[
 b_*>0,\qquad
 \ell_*:=\max_j E[D\mathbf1_{\{\mathrm{return}\}}]<\infty
 \quad\Longrightarrow\quad
 EH\le1+\frac{\max_j(1-b_j+\ell_j)}{b_*}<\infty.
\]

The resolved-trial construction, its geometric bound on the **number of resolved failures**, and the Markov-renewal density criterion are also unchanged.

There is, however, one qualification needed in Section 6 of the parent artifact.

## Correction

The parent text states `UE(epsilon)` as a lower bound `B(T)>=epsilon` on every **surviving** forward subtree, then in Lemma 6.1 applies that lower bound at every vertex of a failed excursion. That implication is too strong as written: a failed excursion may enter a finite/extinct forward branch, where `B=0` and the displayed product bound cannot use `1-B<=1-epsilon`.

Accordingly, the elementary bound

\[
P(D\ge h,F)\le(1-\epsilon)^{h+1}
\]

and the resulting explicit estimate

\[
EH\le1+\frac{1-\epsilon}{\epsilon^2}
\]

are certified only under the **stronger** hypothesis

\[
\boxed{
\mathrm{UE}_{\rm all}(\epsilon):
\quad B(T_v)\ge\epsilon
\text{ for every forward subtree }T_v
\text{ that can be entered during a trial, almost surely.}
}
\]

Equivalently, this elementary corollary excludes finite/dead forward branches as well as arbitrarily small positive escape conductances.

Under `UE_all(epsilon)`, the proof is valid verbatim: after first hitting depth `h`, returning across the trial edge requires `h+1` successive ancestor hits, each having conditional probability at most `1-epsilon`, so strong Markov gives the product bound.

Under the actual H0008 source one must instead handle extinct/finite branches separately. R14's theorem `rho(DF(e))<1` shows that the multitype process conditioned on extinction is spectrally subcritical (its mean matrix is diagonally similar to the extinction Jacobian on extinction-capable types), which strongly suggests an exponentially decaying **genealogical height** contribution from purely extinct branches. But that does not yet control the full failed random-walk excursion after alternating between surviving branch points and finite side branches. No such full estimate is claimed here.

Thus the correct hierarchy is:

1. **general exact reduction:** `ell_*<infinity` is sufficient for finite mean exit-level roof;
2. **fully proved elementary slice:** `UE_all(epsilon)` implies `ell_*<infinity` and the explicit roof bound;
3. **source-relevant next problem:** combine R14's subcritical extinction-Jacobian control with a return estimate through genuine surviving branch points to prove `ell_*<infinity` without `UE_all`.

This correction is recorded as a new immutable file rather than rewriting the parent artifact.