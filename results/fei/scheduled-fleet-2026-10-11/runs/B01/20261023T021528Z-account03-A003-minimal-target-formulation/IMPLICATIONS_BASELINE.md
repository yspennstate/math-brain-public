# Minimal targets with constants and the reset guard

All constants precede every dimension and Boolean-function quantifier. Information is in bits. Let alpha_i=Inf_i, B_i=H(S_i|S_-i), B=sum_i B_i, Delta_i=H(f)-mean H(f_child), and c=2/ln2. Every use of a local rule must apply to every reached restriction. Constants are treated separately with H=I=0.

The arrows below retain the source-complete A003 stage1/stage2 formulations. They are not newly claimed universal payment results.

| Premise, for all Boolean functions | Consequence | Exact sufficient constant |
|---|---|---|
| FEI(C): H<=CI | B<=CI; some relevant i has B_i<=C alpha_i | same C |
| E(K): B<=KI | some relevant i has B_i<=K alpha_i | same K |
| G(K): some relevant i has B_i<=K alpha_i | FEI | K+c |
| Some relevant i has Delta_i<=C alpha_i | FEI by dimension induction | same C |
| B<=lambda H+KI, 0<=lambda<1 | FEI | (K+c)/(1-lambda) |
| Only when max alpha_i<tau: some relevant i has B_i<=(lambda H/I+K)alpha_i | FEI | max(log2(e/tau)+c,(K+c)/(1-lambda)) |
| Same weak-regime rule, restricted to alpha_i>=u I/d, d the relevant dimension, 0<u<1 | same forward implication | same displayed constant |
| FEI(C) | the preceding high-average rule with lambda=0 | K=C/(1-u) |
| Downward edge sum L<=KI under ALL signed Boolean convolution identities | FEI | K+3/ln2 |
| Some relevant i has L_i<=K alpha_i under those identities | FEI | K+3/ln2 |
| Complete posterior witness residual R_*<=KI | FEI | 2+Kref+K |
| One physical stopping tree: sum reach B_i<=K sum reach alpha_i, leaves FEI(C0) | FEI | max(K+c,C0) |

Here L_i=sum_T p_(T+i)log2(1+p_T/p_(T+i)), zero terms understood continuously, and L=sum L_i. The exact interfaces are L<=B<=L+I/ln2 and Delta_i=B_i+JS_i with 0<=JS_i<=c alpha_i. I(parent)=alpha_i+mean I(children). Thus the stated implications include all terminal entropy. A B=0 leaf is not automatically an admissible terminal.

The signed identities are sum_S a_S^2=1 and sum_S a_S a_(S xor U)=0 for EVERY nonempty U, with real a. Inverse Walsh transformation gives f^2=1, so this is precisely Boolean admission. Rewriting the same unconstrained payment under these equations is not additional progress. The uniform singleton law with at least two positive singleton coefficients violates its pair convolution identity and is a mandatory non-Boolean control.

For the conditioned posterior-forest route, freeze one admissible representation, one feasible global lambda and the distinct actual runs. With t_A=sum_run 2^(-B_run), v=1-p_empty, c0=Lambda+log2 Z and U(A)=2^(-c0-Kref|A|)t_A,

    R_*=v c0+sum_(A nonempty) p_A[-log2 t_A],
    h2(v)+Kref I+R_*=H+v D(P^+||U),
    Kref=3+2log2 3+log2(6e).

U is a subprobability and the divergence includes its missing mass. v=0 is handled separately. This identity shows exactly what posterior optimization leaves unpaid. FEI alone does not admit a matching reference into this restricted witness family.

Within each frozen route, the first extra quantitative lemma is:

* Witness: exhibit admitted choices with R_*<=(C-Kref)I-h2(v), including the complete reference divergence, for a prescribed finite C. This is a sufficient exact payment certificate. Normalization alone is insufficient.
* Erasure: the fixed-budget P4 target: if max alpha_i<1/4, some i with alpha_i>=I/(2d) has B_i<=4 alpha_i. This remains OPEN and would give FEI(4+2/ln2). An unspecified finite high-average price is only a finiteness equivalence, as the reverse arrow shows.
* Signed Booleanity: for every fully admitted coefficient vector, exhibit a relevant i with L_i<=4 alpha_i (a fixed quantitative target), which would give FEI(4+3/ln2). This remains OPEN. The budget 4 is explicitly prescribed, not hidden in an unknown FEI constant; no same-price converse is supplied.

There is no canonical smallest lemma among all possible FEI methods. These are the first unpaid inequalities after the respective exact interfaces have been removed.

The new history constraint is common to the witness and stopping routes. For an admitted complete reference, an actual query releases conditional occupancy KL rho. A prescribed reset costs the signed likelihood Z. With all prior debits and full siblings retained, its exact remaining bank is

    U_new=U+w rho-w Z.

DERIVATION.md and the finite certificates refute the strengthening that canonical active resets always have Z<=0, even with source cost certified at C0=14. The surviving minimal history lemma must PAY positive Z from the SAME U+w rho. It cannot obtain a fresh root bank, discard the constant sibling's full inherited reference or replace weighted likelihood by absolute reference distance. This new obstruction changes no forward FEI constant in the table.
