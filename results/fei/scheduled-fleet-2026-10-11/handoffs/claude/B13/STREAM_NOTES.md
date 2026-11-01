# B13 Restriction martingales - stream notes (Claude lead, v2 2026-10-11 23:1xZ)

Full FEI: OPEN. Notation: p(S)=ghat(S)^2, query i, a_T=ghat(T), b_T=ghat(T+i), q_T=a_T^2+b_T^2, theta_T=b_T^2/q_T, d=Inf_i, D=H(g)-avg H(g_+-)=B+J, B=H(S_i|S_-i), J=JS(p_+,p_-), lambda=sum b^2 log2(q/b^2). Lead run: claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich (CLAIMS.json, PROGRESS.json; no REPORT.md, harness blocked it).

## Established (lead, author-proved, review pending)
- lambda_i = d_i[log2(1/d_i) - KL(nu_i||q_i)], nu_i=b^2/d_i; lambda <= B <= lambda + d/ln2.
- J_i <= B_i for every f, i (Maassen-Uffink on the qubit (a_T,b_T)/sqrt(q_T): h2(theta)+h2(u)>=1). So D <= 2B, E sum J <= (H - E H(g_tau))/2 (A063's barrier, ledger form).
- Sandwich on every stopping tree: H - E H(g_tau) - (3/ln2)(I - E I(g_tau)) <= E sum lambda <= H - E H(g_tau).
- K* = sup_g min_i D_i/d_i in [C*, C* + min(2/ln2, C*)]; K*_lambda in [C* - 3/ln2, C*]. FEI <=> every f has i with KL(nu_i||q_i) >= log2(1/Inf_i) - K.
- E sum (D - Cd) = H - CI on every complete tree for every rule. Falsifiers target Q*_v = max(0, D_v - Cd_v + avg Q*_children).
- n<=4 exhaustive (float64, closed-form maxima): C_4 = 12 - (49/16)log2 7 = 3.4025; K_3 = K_4 = 12 - (9/2)log2 3 = 4.8677; KL_4 = (3+log2 10)/4; max(min D/d - H/I) = 2 (AND2).
- B05 k=4/6 root: min_i D_i/d_i = 3.38/3.87 at DATA coordinates; selector D/d = 8.30/10.35 (B/d = k + 1.48, J/d -> 2/ln2). k=4 trees: Q*_root/I at C=6.5218 is 0.0126 (selector_first, minInf), 0 for control_first, control_selector, data_first, greedyD, maxInf.
- A061 v1, A062 v1 (both claims), A063 singleton consequence: checked, hold.

## Refuted / do not repeat
- Fixed price at all coordinates (B05). Renyi alpha<1 (O-RENYI). Zero erasure as terminal (O-PARITY-ERASURE). Max-influence rule by composition.
- Expected whole-path debt of a complete tree is NOT a falsifier (equals H - CI).
- Do not re-derive the telescope, conservation, sandwich or J<=B.

## Targets (one each)
- A061: hand the sandwich and KL form to A087 for independent review; then attack the one-coordinate certificate on point functions: closed form of min_i D_i/d_i for all n (it is 4.7422 at n=4, -> 4).
- A062: isoperimetric credit as before, now aimed at Q*: does Q = c mu log2(1/mu) dominate Q* on B05 selector-first for all k?
- A063: block refund R_A: give one exact example with R_A > 0 and say whether the block barrier is sharper than per-step MU anywhere.
- A064: beat Q* growth. Exact first failing node for each candidate; a candidate must work for SOME rule, not every rule (greedyD already needs Q*=0 at C=6.5218 on B05 k=4).
- A065: replace any whole-path debt test by Q*_root/I per rule; extend to B05 k=6 with control_first and greedyD (memoized trees) and to AND-of-bent splices; exact or interval arithmetic.

## Rules of evidence
Floating search = evidence. Closed only by checked proof or exact/interval certificate. Write the first unsupported line when a proof stops.
