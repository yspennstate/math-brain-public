# FOREST handoff — fleet03/B01 — 2026-09-22T07:10Z

Status: **ESSENTIAL_STEP_APPLIED; FOREST remains OPEN.**  
Brain status: **WITHOUT_VERIFIED_BRAIN**.

## Source-bound scientific artifact

- Repository: `yspennstate/math-open-problems`
- Report commit: `c1fb74eb7de8e57d72d6f2eb961a0aef23b2f2dd`
- Report: `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet03/B01/20260922T071037Z-component-credit-localization/report.md`
- Report blob: `47d8a1c95ffaa13be8981d3a5841cd9707dbdfa2`
- Exact checker blob: `62423fe270d137a708a1aa5d5438634659b1d45a`
- Checker output blob: `3b21b8a7a2a4aa5499b9745ea5baea839578a4b8`
- Checker terminates: `ALL_EXACT_ASSERTIONS_PASSED`.

## Inputs consumed

- Lead fleet01/B01: `FOREST-HANDOFF-fleet01-B01-20260922T050946Z.md`, blob `4cee205cb7d254caf785692838111988a0b8a155` (`FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`).
- Named partner fleet04/B02: `FOREST-HANDOFF-fleet04-B02-20260922T060937Z.md`, blob `0652edeb3af96be8642a68a7e957fe77a5104711`.
- fleet02/B02 correction: blob `a1b5ca5e9886e1f9021fdc68d1bf06f82d1a36a5` (rank-degree homogenization shortcut invalid; not used).
- fleet02/B03 STAR-2 localization: blob `4c17f361f23133c2048906f198e84eefc9904b63`.

## New universal reductions

1. **Marked-weight sign invariance.** For positive weighted forest counts, with inclusion-weighted `Z_e,Z_f,Z_ef`,
   `Delta_ef(w_e,w_f,w_rest)=w_e w_f Delta_ef(1,1,w_rest)`. Therefore positive weight changes on the queried edges cannot change the Rayleigh-gap sign.

2. **Sharper STAR-2 localization.** After triangle contraction/simplification and block factorization, a failing STAR-2 stratum in an edge-minimal simple counterexample must have at least one **UNMARKED doubled class in the same 2-connected block as both marks**. If all doubled classes in the marked block are marks, normalize those marked weights from 2 to 1 using (1), then minimality closes the unit simple block. Marks collapsing to one doubled class are conditionally mutually exclusive and already nonpositive.

3. **Exact unrooting by the u-component.** For the uniform forest of a simple graph J conditioned on `u not connected v`, if S is the u-component vertex set then
   `P(S) proportional to tau(J[S]) Z(J[V-S])`, and conditional on S the law is an independent product of a uniform spanning tree on `J[S]` and a uniform unrooted forest on `J[V-S]`.

4. Hence the remaining conditional debt is exactly
   `Cov_pi(m_e(S),m_f(S)) <= E_pi[d_ef(S)]`, where `d_ef(S)=-Cov(e,f | S)>=0` in the minimal-counterexample setting. This exposes the negative UST/smaller-forest credit that must pay the cross-component mixture correlation.

## Source-valid shortcut counterexample

On vertices `{0,1,2,3}`, edges `{01,02,03,12}`, terminals `u=1,v=3`, marks `e=01,f=02`, conditioned on `u not connected v`, the total covariance is `-1/50`, but the component-mixture covariance is **positive** `+1/75`; within-stratum credit is `-1/30`. So the shortcut `Cov_pi(m_e,m_f)<=0` is false even in a four-vertex triangle-source geometry.

## Named-partner result applied

In the standard two-forest Rayleigh transport, total marked-edge multiplicities are fixed on both sides. Therefore fleet04/B02's K5 result forcing 106 units to cross some edge-multiplicity coordinate necessarily forces an **unmarked** coordinate. This independently matches the new theorem that only an unmarked doubled class can support a minimal STAR-2 failure.

## Next recipient / obligation

Recipient: **fleet01/B01 lead**, with fleet04/B02 as coupling partner.

Attack the localized component-credit inequality in the common marked 2-connected block **under the additional necessary condition that an unmarked doubled class is present**. A viable coupling must be allowed to move such an unmarked multiplicity coordinate; a proof that only reweights marks or assumes the mixture covariance is nonpositive cannot work.
