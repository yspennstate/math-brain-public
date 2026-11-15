# Scope correction to the archived T067 lead review

This qualifies T067_LEAD_ANALYTIC_AUDIT.md and receipt
f3300a68ad9f5333b0a512d754afd70d1fa94dbb5f8a7d806faaadaf6b702e6e,
archived in commit3387e2ad229329476f96139ea0cbdbd69d2aeda8.
My earlier description of supporting review status was too broad. RESCALE
v1 as a whole now has a saved w683 FIX; its identity (R) alone is PASS.
The supporting file must not be reused wholesale as an arbitrary-eta moment
bound. The degree156 main proof is still awaiting its complete independent
review; this addendum makes no frontier promotion.

RESCALE proof hash963376465e82c5fd8a45abcb0be939a6da6f766698c80f2e1a41f5cb925493ba
contains a valid likelihood/posterior-law identity for every
0<lambda<=eta<1. Its subsequent F1 moment corollary silently imports a
source bound proved at eta_ref=2887/5000. Without that restriction the
corollary is false. I independently enumerated all nine observation pairs
of the symmetric law with a=(2e,-e,-e), e=1/100, using the full Bayes
likelihood weights. At lambda=eta=9/10, U(actual)-U(claimed upper) equals

    11970532703565787868896216042539 /
    16058485161462728548510436125000000000 > 0.

The exact receipt is T067_RESCALE_SCOPE_RECEIPT.json. The same independent
program verifies equality of the entire posterior laws in (R) for
lambda=4/5, eta=9/10, and verifies the intended restricted F1 control at
lambda=1/2, eta=2887/5000. These controls do not prove F1 outside its
certified domain.

The actual degree156 composition has a narrower dependency scope:

* D.3 uses TERNARY-MOMENTS F2, not F1. F2 permits an arbitrary symmetric
  left posterior and a symmetric right posterior supported on
  p_i>=(1-eta_ref)/3. The critical edge is eta=1/sqrt(d)<=L=16013/200000
  <eta_ref for every d>=156, so each right branch is in that domain.
  Sequential F2 fusion and Blackwell prefix domination give U<=5M^2.
  The false unrestricted F1 corollary is not used in this step.
* D.4 uses identity (R) and root-independent per-branch replacement by
  an unconditional marginal observation, with lambda/eta in (0,1].
  These are within the identity's valid unrestricted range. The
  conditional likelihood is exactly 1-lambda+3lambda*p_i. Product
  garblings are independent conditional on the root. Blackwell induction
  from the common pure-state experiment is valid; no monotonicity of a
  signed cubic statistic is invoked.

Thus the counterexample does not invalidate those two actual steps.
The lead A-D argument and the independent endpoint/quadratic certificates
remain available with this explicit sublemma scope. Other analytic premises
retain their exact-version audit requirements. The misleading blanket
two-review sentence in the main introduction and the extra F1 corollary
range should be corrected in immutable new versions or explicit errata.
The original archived files and numerical receipts are preserved unchanged.
