# T354 moves on the obstruction

- 2026-10-16, narrowed (agent A): repaired: RR, bias correction, fixed beta2, residual neighbourhood vs n(1-beta2); scalar finite-sum model proposed
- 2026-10-20, audited (agent C): RR beta1=0 eps=0 remainder lemma: second audit CONFIRMED (audit_C/AUDIT_RR_B1ZERO_agent_C.md); line re-filed 04:3x after the 04:22 repo revert
- 2026-10-20, audited (agent C): RR momentum and eps>0 remainder lemmas: enclosure algebra re-derived, CONFIRMED (audit_C/AUDIT_RR_MOM_EPS_agent_C.md); line re-filed 04:3x after the 04:22 repo revert
- 2026-10-20, audited (agent C): RR next-order term beta1>=0 eps=0: audit 2 CONFIRMED, hand re-derivation + own exact two-special solver on b=(6,2,-1x8), limits -0.880787/-0.541022/-0.087858 reproduced to 4e-6, no S term (audit_C/AUDIT_RR_NEXT_ORDER_agent_C.md)
- 2026-10-20, audited (agent C): RR next-order term beta1>=0 eps>0: audit 2 CONFIRMED, psi prime/second derivative and the solve re-derived by hand, own exact two-special solver with the erfcx t-kernel on b=(6,2,-1x8) at eps 1 and 10, six limits reproduced to 2e-6, no S term (audit_C/AUDIT_RR_NEXT_ORDER_EPS_agent_C.md)
- 2026-10-20, audited (agent C): RR unequal-curvature next-order term: eps=0 audit 2 and eps>0 (with r1) audit 1, both CONFIRMED; c1, the r slope r1 and the Q term re-derived by hand; exact roots on b=(6,2,-1x8), three curvature vectors, eps 0 and 1, beta1 0 and 0.9, 12 families, three-point intercept at most 3e-6; without r1 the eps 1 coefficient is off by up to 0.12 (audit_C/AUDIT_RR_CURVATURE_agent_C.md)
