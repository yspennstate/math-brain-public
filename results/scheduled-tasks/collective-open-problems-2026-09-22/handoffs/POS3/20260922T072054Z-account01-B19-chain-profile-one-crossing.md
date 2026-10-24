# POS3 handoff — exact chain-profile defect and no passive repeated return

Source: account01/B19 run `20260922T072054Z-account01-B19-POS3`. Outcome `ESSENTIAL_STEP_APPLIED`; parent POS3 remains **OPEN / NOT PROVED**; execution context `WITHOUT_VERIFIED_BRAIN`.

Consumed OTHER-account inputs:
- account02/B10 `20260922T064948Z-b10-a11`, handoff blob `bc7b56b0f40e2a1a1ff27f0a8f85b61465d60f12` (`POS3-RAY-RETURN-FRESH-MASS-v1`);
- lead account04/B10 r17, handoff blob `f5a263be6f1255619bc09574c10833602f1b8b85` (`COHERENT-GATE EXIT`).

New arbitrary-size theorem. Delete any chain `C={c_1<...<c_m}` and attach to each surviving element `q` its exact chain-prefix interval `I(q)=[lambda(q),rho(q)]`. For an adjacent incomparable pair `u,v`, fix the outside insertion fiber and its boundary states `s<=t`. If `A=I(u)` and `B=I(v)`, then their intervals overlap and the exact local swap defect `Delta=N(uv)-N(vu)` has a closed form.

If `A` is endpoint-shifted left of `B`, decompose the feasible window into `L=A\B`, `O=A∩B`, `R=B\A`, with cardinalities `ell,o,r`; then

`Delta=ell*o+ell*r+o*r >= 0`.

If `A subset B`, with left/inner/right pieces `L,O=A,R`, then

`Delta=o*(r-ell)`.

Thus the only sign-changing case is nesting, and its positive and negative defect units have disjoint exact labels `O x R` and `L x O`. This gives a fiberwise fresh-tail decomposition: opposite defect directions require opposite symmetric-difference tails of the chain profile.

Moreover the nested defect is single-crossing in either boundary coordinate. A fixed-profile insertion step is `T_I f(r)=1_I(r) sum_{q<=r} f(q)`, which preserves the property of having at most one sign change. Hence any finite one-sided fixed-profile insertion block is variation diminishing. A nested defect propagated through such a block cannot undergo outward/return/outward (two genuine sign reversals) without a new source: a profile-endpoint change, boundary/ray change, or departure from the fixed-profile regime.

Application: this proves the fixed-profile portion of account02/B10's fresh-mass residual. Combined with lead r17, the only unpaid location is the coherent aligned width-saturating three-antichain gate. New residual:

`POS3-COHERENT-ENDPOINT-REUSE-EXCLUSION`: show that the coherent gate either embeds into the one-sided fixed-chain regime above, or its first failure yields a genuinely fresh Hasse/profile endpoint that cannot later be reused without balance/span descent/width-four/autonomous reduction.

Canonical report: `proofnet24/collective-POS3/account01/B19/20260922T072054Z-account01-B19-POS3/REPORT.md`, commit `6839e16be65205c2a12375a1cd3617d150a5bfb6`, blob `d034992af1e46fa00c0795349ff910ee30e031eb`.

Verifier blob `8dedcd93f7e847b62701a8b685ed7e4584c74bc2`; output blob `57ac19b6eef815e9130acefe576deee5c878c63a`; exact regression totals `229306 + 64658 + 151872` cases, ending `POS3_CHAIN_PROFILE_DEFECT_CHECK_PASS`.
