# account01/B15 addendum — target-wide critical-gap normal form

**Status:** `TARGET_LEVEL_REGULARITY_LEMMA / EXACT_CRITICAL_GAP_NORMAL_FORM`; full unrestricted QFORM remains **OPEN / NOT PROVED**.

Canonical addendum: `yspennstate/math-open-problems@12e4504e9089b5a310b0704fdea49062afc2c193`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260923T020319Z-account01-B15-qform-auto11/ADDENDUM_TARGET_WIDE_CRITICAL_GAP.md`.

Completed account02/B15 result actually used: `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, proving every fixed target output has a bounded `C_0(R)` density with a matrix-dependent constant.

Let `s=s_3(A)>=1` and let `C_*` be the sharp full-owner universal density constant (possibly infinite). Exact spectral scaling gives

`C_* = sup_target s ||p_Q||_infinity`.

Because every fixed target density is continuous, its value at the sole critical output `0` is approached by nonzero values. Scaling `A -> aA` preserves `s p` exactly:

`(as) p_{aQ}(at)=s p_Q(t)`.

Therefore, for every fixed `R>0`,

`boxed: C_* = sup_{target, |t|>=R} s p_Q(t)`.

More strongly, for every fixed `R>1`,

`boxed: C_* = sup_{target, |y|>=R} (s/2) P(|Q-y|<=1)`

and, with `T(u)=(1-|u|)_+`,

`boxed: C_* = sup_{target, |y|>=R} s E T(Q-y)`.

The reverse inequalities use the completed partner `C_0` theorem on the actual approximate-identity limits after scaling:

`(as/2) P(|aQ-at|<=1) -> s p_Q(t)`,

`as E T(aQ-at) -> s p_Q(t)`.

Thus the full conjecture is exactly equivalent to one fixed-scale positive small-ball estimate whose observation window may be required to stay an arbitrarily prescribed distance from the only critical output value. For example it is enough to prove

`sup_{target, |y|>=2} [s_3(A)/2] P(|X^TAX-y|<=1)<infinity`.

This does **not** rescue projection-only methods: the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` counterexample already concentrates at the noncritical level `-1`. Product provenance remains necessary. It also does not assert any target-uniform raw continuity modulus; only instancewise `C_0` regularity is used.
