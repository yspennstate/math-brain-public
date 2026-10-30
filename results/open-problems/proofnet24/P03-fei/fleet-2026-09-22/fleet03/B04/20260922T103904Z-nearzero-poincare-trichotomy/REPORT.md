# fleet03/B04 — exact near-zero Poincare-gap trichotomy for Boolean gates

**Outcome:** `ESSENTIAL_STEP_APPLIED / NEAR_ZERO_DENOMINATOR_CLASSIFICATION`  
**Full FEI:** `OPEN_NOT_PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Owner programme:** `FEI-ALL-TEAM-20260922T095941Z`, revision `2026-09-22.3`.

## 1. Exact target and source correction

The later owner order superseded this slot's BT4 work during the invocation. The active B04 target is now:

> classify and control the gate-margin quotient near
> \(W=(I-V_{\rm out})/4=0\) for genuine Boolean gates, starting from the Poincare equality structure and the exact two-child disagreement identity.

The current state explicitly refutes the old universal quadratic coefficients `0.337` and `0.34`; no positive claim below uses those coefficients. The source facts consumed are version-stable identities only.

Named completed other-account result consumed: fleet02/B12,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`
at commit `4ccd51ad517f425a529daa52c3352905b86ea69d`. I use its exact selector identities, in particular
\(p=V_s d\), the child-defect recursion, and the local quadratic term
\(c s(1-s)[d-(q_1-q_0)^2]\). I do **not** use its now-refuted Section 5 candidate.

The current all-gate source also gives
\[
W_G=\frac{I(G;p)-V_{p_{\rm out}}}{4}
\]
and says that adding \(c\,u(1-u)\) to the potential changes the gate defect by exactly \(cW_G\).

No completed FEI handoff from the newly assigned partner `fleet04/B04` was present at the fresh snapshot, so this run proceeded from the completed source above rather than waiting.

## 2. Exact two-child Poincare-gap identity

Let \(G\) be a Boolean gate under a full-support product bias. Split on coordinate \(i\), whose bias is \(s\in(0,1)\). Let \(G_0,G_1\) be the two restrictions, let
\[
q_a=\Pr[G_a=1],\qquad q=(1-s)q_0+s q_1,
\]
let
\[
d=\Pr[G_0\ne G_1],\qquad \Delta=q_1-q_0,
\]
and write \(W_a=(I(G_a)-V_{q_a})/4\).

The selector influence identity is
\[
I_i^t=V_s d=4s(1-s)d.
\]
The remaining coordinate influences average over the two restrictions, hence
\[
I(G)=(1-s)I(G_0)+sI(G_1)+4s(1-s)d.
\tag{2.1}
\]
The law of total variance gives
\[
V_q=(1-s)V_{q_0}+sV_{q_1}+4s(1-s)\Delta^2.
\tag{2.2}
\]
Subtracting (2.2) from (2.1) and dividing by four yields the exact identity
\[
\boxed{
W(G)=(1-s)W_0+sW_1+s(1-s)\bigl[d-\Delta^2\bigr].
}
\tag{2.3}
\]
Set
\[
\delta=d-\Delta^2.
\]
Because \(|\Delta|\le d\),
\[
\boxed{\delta\ge d-d^2=d(1-d)\ge0.}
\tag{2.4}
\]
Thus every term on the right of (2.3) is nonnegative.

## 3. Exact equality classification

**Theorem 3.1 (Poincare equality for actual Boolean gates).** Under a full-support product bias,
\[
W(G)=0
\]
if and only if \(G\) is constant or a literal/negated literal.

**Proof.** The forward direction follows from (2.3). If coordinate \(i\) is relevant, full support gives \(d>0\). Equality forces \(\delta=0\). From (2.4), \(d=1\); then \(d-\Delta^2=0\) gives \(|\Delta|=1\), so \((q_0,q_1)=(0,1)\) or \((1,0)\). Hence both restrictions are constants of opposite signs and \(G\) is a literal in coordinate \(i\). If no coordinate is relevant, \(G\) is constant. Conversely constants and literals have Fourier support only in degrees zero and one, so \(I=V_{\rm out}\). QED.

This is the exact point at which division by \(W\) is forbidden: the margin quotient is `0/0` at genuine equality states.

## 4. Quantitative interior neighborhood theorem

The same identity gives a source-free quantitative collar around equality.

**Theorem 4.1.** Suppose \(W(G)\le\varepsilon\) and the selector bias satisfies \(s\in[\alpha,1-\alpha]\), \(0<\alpha\le1/2\). Put \(\kappa=s(1-s)\ge\alpha(1-\alpha)\). Then
\[
W_0\le\frac{\varepsilon}{1-s},\qquad
W_1\le\frac{\varepsilon}{s},\qquad
\delta\le\frac{\varepsilon}{\kappa}.
\tag{4.1}
\]
Moreover
\[
\boxed{
\min\{d,1-d\}\le \frac{2\varepsilon}{\kappa}
\le \frac{2\varepsilon}{\alpha(1-\alpha)}.
}
\tag{4.2}
\]
Hence every interior selector is quantitatively in one of two branches:

1. **irrelevant branch:** \(d\le2\varepsilon/\kappa\), and then \(|\Delta|\le d\);
2. **dictator branch:** \(1-d\le2\varepsilon/\kappa\). In this branch, writing \(\tau=1-|\Delta|\),
\[
\boxed{
\tau\le\frac{3\varepsilon}{\kappa}.
}
\tag{4.3}
\]
Up to swapping the two child signs, this means
\[
q_0+(1-q_1)=1-\Delta\le 3\varepsilon/\kappa,
\]
so the children are quantitatively close in measure to opposite constants.

**Proof.** (4.1) follows termwise from (2.3). Let \(m=\min(d,1-d)\le1/2\). Then by (2.4),
\[
\delta\ge d(1-d)=m(1-m)\ge m/2,
\]
which proves (4.2). In the dictator branch write \(e=1-d\). Since \(e\le2\delta\) and
\[
1-\Delta^2=e+\delta,
\]
we have
\[
\tau=1-|\Delta|=\frac{1-\Delta^2}{1+|\Delta|}
\le e+\delta\le3\delta,
\]
which gives (4.3). QED.

## 5. First nonzero denominator terms

The exact local denominator contribution is \(s(1-s)\delta\).

On the irrelevant branch, \(|\Delta|\le d\), so
\[
d(1-d)\le\delta\le d.
\tag{5.1}
\]
Thus as \(d\to0\),
\[
\delta=d+O(d^2),
\qquad
W_{\rm local}=s(1-s)d+O(s(1-s)d^2).
\tag{5.2}
\]

On the dictator branch set
\[
e=1-d,\qquad \tau=1-|\Delta|.
\]
Then the denominator defect is exactly
\[
\boxed{
\delta=2\tau-e-\tau^2.
}
\tag{5.3}
\]
So its first nonzero term is \(2\tau-e\), with the exact quadratic correction \(-\tau^2\).

These formulas identify the two genuine interior ways in which the Poincare denominator can vanish.

## 6. Boundary collapse is a third mechanism and cannot be ignored

The interior collar does **not** classify all sequences with \(W\to0\), because a selector bias can itself approach the boundary.

Take the genuine two-input XOR gate, with first input bias \(p\in(0,1)\) fixed and selector bias \(s\downarrow0\). Its restrictions in the selector coordinate are \(G_0=x\) and \(G_1=1-x\). Hence
\[
d=1,\qquad \Delta=1-2p,\qquad
\delta=1-(1-2p)^2=V_p>0,
\]
while \(W_0=W_1=0\). Therefore (2.3) gives the exact denominator
\[
\boxed{W_{\rm XOR}=s(1-s)V_p\longrightarrow0,}
\tag{6.1}
\]
even though the local equality defect \(\delta\) stays bounded away from zero.

The gate source gives the exact XOR defect
\[
D_\Gamma=\Gamma(p)+\Gamma(s)-\Gamma(p+s-2ps).
\tag{6.2}
\]
Thus whenever \(W>0\), the exact margin quotient is
\[
\boxed{
\mathcal C_{\Gamma,\rm XOR}(p,s)
=-\frac{\Gamma(p)+\Gamma(s)-\Gamma(p+s-2ps)}{s(1-s)V_p}.
}
\tag{6.3}
\]
If \(\Gamma(0)=0\), \(\Gamma\) has a finite right derivative at zero and is differentiable at \(p\), then
\[
\boxed{
\lim_{s\downarrow0}\mathcal C_{\Gamma,\rm XOR}(p,s)
=-\frac{\Gamma'_+(0)-(1-2p)\Gamma'(p)}{V_p}.
}
\tag{6.4}
\]
So a uniform near-zero quotient theorem must include explicit boundary regularity/contraction control; Poincare equality rigidity alone cannot supply it.

This XOR sequence is not a counterexample to FEI. It is a counterexample to any proof that treats `W small` as automatically meaning `d-Delta^2 small` without controlling selector biases.

## 7. Exact effect of the quadratic safe direction on the quotient

Let \(\phi(u)=u(1-u)\). The gate source and selector identity imply exactly
\[
D_{\Gamma+c\phi}(G;p)=D_\Gamma(G;p)+cW(G;p).
\tag{7.1}
\]
Therefore for every point with \(W>0\),
\[
\boxed{
\mathcal C_{\Gamma+c\phi}=\mathcal C_\Gamma-c.
}
\tag{7.2}
\]
At \(W=0\) both the denominator and the perturbation contribution vanish, so (7.2) must be interpreted only off the equality set. This is the cleanest possible control of the quadratic direction near the denominator: it cannot create a singular quotient; it translates the quotient by a constant.

The old numerical coefficients are refuted universal candidates, but identity (7.2) remains valid for every real coefficient.

## 8. What this changes and the next unpaid implication

The near-zero-denominator problem splits rigorously into three regimes:

- **interior irrelevant:** \(d\to0\), with local denominator first order \(s(1-s)d\);
- **interior dictator:** \(d\to1\), children approach opposite constants, with local denominator \(s(1-s)(2\tau-e-\tau^2)\);
- **bias-boundary contraction:** \(s(1-s)\to0\), where the internal disagreement defect may remain order one; XOR gives an exact model and quotient formula.

Thus future gate-margin work should not scan or divide by tiny `W` indiscriminately. It should first label which of these three mechanisms is responsible.

**Next unpaid implication (`FEI-B04-BOUNDARY-QUOTIENT-v1`).** Prove for the current shaped candidate, or for a replacement finite-cap potential, a uniform upper bound on the boundary-contraction quotient after reducing to one live child. Equivalently, establish the required one-sided potential regularity/recursive cancellation in (6.3) and its non-XOR analogues, while keeping child defect and selector entropy terms. The interior denominator itself is now quantitatively classified by Theorem 4.1.

Primary recipient: `fleet01/B01`. Assigned partner for the next run: `fleet04/B04` once a completed compatible result is available.

## 9. Honest status

This report proves an exact equality classification, a quantitative interior near-equality theorem, exact first-order denominator formulas, and an exact boundary-contraction example/quotient formula. It does not prove a uniform upper bound for the full shaped-potential quotient and does not prove FEI. No novelty claim is made. `full_brain_connected=false`.
