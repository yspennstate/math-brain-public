# R01 independent second-audit route for E0017 / Malrieu Conjecture 4.3

Date: 2026-09-19 UTC.
Role: R01, distinct from owner PROB20-07 and from P26.

This note is written before the audit report and before any checker. There is no essential finite core, so the intended audit is analytic rather than computational.

## Frozen R01 state

Do not reopen Aldous--Fill 3.44. The proved and audited exact formula stays

\[
\tau_2=\inf_{R:\,BR=I_{H_0}}\sup_{0\ne b\in H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},\qquad R_*=CB^TL^+,
\]

with distortion `C=1`. TFIK22 remains owner-side candidate complete with `R_TFIK22=0` and only the P26 qualifying outside audit. The free-CLOSABLE successor gate already reached its six-run rotation threshold, so this run must not manufacture a seventh empty admission scan.

## Why E0017 is audit-ready

Canonical claim: `operations/claims/E0017.md`.
Owner: PROB20-07.
Source: Florent Malrieu, *Some simple but challenging Markov processes* (2015), Theorem 4.1 / Conjecture 4.3 / Open Question 2.
Owner metric: `U_G=1`, PROVED-CANDIDATE.
P26 audit: `P26-AUDIT-E0017-MALRIEU-G-UNIMODALITY-75 = PASS_FULL_MATHEMATICAL_PROOF`.
Missing gate: one genuinely distinct non-owner/non-P26 end-to-end audit.

The audit must keep the source-scope qualification explicit: the mathematical core is strict one-hump shape plus endpoint limits for the exact Theorem-4.1 function under the displayed jump-rate convention. The printed numerical locator `r_c ~ 4.6` is inconsistent with that convention and is not to be silently certified.

## Three new-method routes

### #1 CHANGE THE CATEGORY

Move the stochastic-switching question into deterministic transform theory. Starting from Malrieu's displayed invariant-density formula, recover

\[
G(r)=\frac{\mathcal L k(r)}{\mathcal L j(r)},\qquad
\mathcal L f(r)=\int_0^\infty e^{-r\delta}f(\delta)\,d\delta.
\]

Then audit the shape of the input quotient `h=k/j`, not the switched process directly. The decisive identities to verify independently are

\[
k' = b*w,\qquad j''=2(b*b)>0,
\]

with `b(x)=2(x^2+4)^{-3/2}`, `w(x)=(x^2+4)^{-1/2}`, and the Wronskian

\[
q=k'j-kj'=j^2h',\qquad q'=k''j-kj''<0.
\]

This should force `h` to have exactly one turn.

### #21 ASK WHO ELSE HAS THIS SHAPE

Compare the required transform step with classical total-positivity / variation-diminishing results. Two relevant known mechanisms are:

- the sign-regular Laplace-transform ratio theorem of Karp--Vishnyakova--Zhang (Results Math. 80 (2025), 112);
- a Descartes rule for Laplace transforms, e.g. Ramos--Sousa, Analysis & PDE 16 (2023), Proposition 5.6.

These are prior art for the mechanism, so no novelty should be claimed for transform zero-counting itself. The E0017 package also contains a direct three-exponential Chebyshev proof, which should be checked independently so that the source claim does not logically depend on the 2025 theorem.

### #27 SWAP THE QUANTIFIERS

Instead of trying to show directly that `G'(r)` has one zero for all `r`, fix a horizontal level `c` and study

\[
\phi_c(\delta)=k(\delta)-c j(\delta)=j(\delta)(h(\delta)-c),
\qquad F_c(r)=\mathcal L\phi_c(r)=\mathcal L j(r)(G(r)-c).
\]

If `h` is one-peaked, every interior `\phi_c` has sign pattern `-,+,-`. Prove that a Laplace transform of such a function has at most two positive zeros by contradiction: if `F_c(r_i)=0` at three distinct `r_1<r_2<r_3`, choose a nonzero combination

\[
Q(\delta)=\sum_{i=1}^3 a_i e^{-r_i\delta}
\]

vanishing at the two sign-change points. The three exponentials form a Chebyshev system, so those are the only two roots and are simple; after a global sign choice, `Q\phi_c>0`, while

\[
\int Q\phi_c=\sum_i a_i F_c(r_i)=0,
\]

a contradiction. This turns all horizontal superlevel sets of `G` into intervals, hence gives one-hill order structure. Then separately exclude off-mode stationary inflections by the quadratic sign-matcher / first-three-moments contradiction.

## Adversarial checks to perform

1. Re-derive the jump-rate convention from Malrieu's actual generator and do not inherit the source's plotted `4.6` scale.
2. Check the source-to-`t=-tan(theta)` and then `x=t-1/t` reductions, including signs and the normalization factor.
3. Check that the nonintegrable `w` does not invalidate radial-decreasing convolution: truncate on centered intervals and pass monotonically.
4. Check the two-zero lemma counts multiplicity sufficiently to make the two prescribed roots of the exponential combination simple.
5. Check the superlevel-set argument rules out two separated hills because endpoint limits make all positive superlevel components bounded.
6. Check analyticity is enough to eliminate plateaus and to make an off-mode stationary point have odd multiplicity at least three.
7. Check endpoint asymptotics independently: `G(r)~r log(1/r)` as `r downarrow 0` and `G(r)~1/(8r)` as `r to infinity`.
8. Re-run bounded current literature/source-intent searches; record negative search only as bounded evidence, not a novelty certificate.

If all eight checks survive, the appropriate verdict is a source-core-scoped `PASS_FULL_MATHEMATICAL_PROOF`, which would move E0017 from one to two genuinely distinct full audits. No checker should be manufactured merely for bookkeeping because the proof has no essential finite core.
