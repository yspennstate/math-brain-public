# A paid reference can be carried without resetting it

All logarithms are base two; references are normalized probability laws on ALL Fourier subsets. Zero reference mass is allowed only where the true spectrum vanishes. The assertion below is an elementary complete-reference chain rule, used here to continue the specified paid A097 floor. It is not a new FEI-equivalent inequality or a claimed solution of universal reference construction.

## 1. One actual physical exposure

Let f be any Boolean sign and P(S)=hat f(S)^2. Supply any normalized Q with finite CE(P,Q). For a queried coordinate j, write p_tb=P(T union {j if b=1}), q_tb=Q(T union {j if b=1}), m_t=p_t0+p_t1, and v_t=q_t0+q_t1. Give BOTH actual physical children the SAME complete reference v. In particular v is a spectral marginal, not conditioning on a physical outcome, and generally is not either child's true law.

The signed Fourier coefficients of the actual child f_epsilon are a_t+epsilon a_(t+j). Thus its squared law P_epsilon is normalized (Booleanity gives Parseval), supported by v, and

    (P_+(t)+P_-(t))/2=m_t.                              (1)

Actual child laws still require the signed amplitudes. Formula (1) does not contradict A081's counterexample to reconstructing a physical child law from the unsigned parent alone. Only the conservative child REFERENCE uses Q alone.

Define the erasure B_j=H(P)-H(m) and the nonnegative conditional reference refund

    R_j = sum_t m_t D(P(b|t)||Q(b|t))
        = D(P||Q)-D(m||v) >= 0.                         (2)

Terms at m_t=0 vanish, with no arbitrary conditional distribution charged there. At every occupied t, v_t>0; Q's possible additional support remains in all normalizers. The exact identity is

    CE(P,Q)=B_j + [CE(P_+,v)+CE(P_-,v)]/2 + R_j.        (3)

Proof: conditional cross entropy disintegrates CE(P,Q) into CE(m,v)+H(P(b|t)|t)+R_j. Equation (1) makes CE(m,v) exactly the mean complete child CE. This proof retains the empty atom and all reference-only support. Gibbs' inequality supplies the only inequality. No outcome labels are charged or transmitted by (3).

If J_j=H(m)-[H(P_+)+H(P_-)]/2, the companion exact identity is

    D(P||Q)-[D(P_+||v)+D(P_-||v)]/2=R_j-J_j.           (4)

So KL alone need not decrease. Removing J_j, omitting terminal entropy, or treating marginalization as a phase reset would lose part of the account.

## 2. Adaptive histories and an already booked debit

For ANY finite physical decision tree that queries an unqueried coordinate at each node, assign child references by the marginalization in section1. The next query may depend on all previous physical outcomes. Every leaf reference is the original Q marginalized over exactly its path's queried coordinates; each is normalized, including every reference-only atom. Reach weights are physical uniform-cube probabilities 2^(-depth), not spectral probabilities. Multiplying (3) by reach and telescoping gives

    CE(P_root,Q_root)
      = E sum_internal B_j + E CE(P_leaf,Q_leaf)
        + E sum_internal R_j.                         (5)

Consequently the full erasure bill plus every complete terminal H+D is paid by the incoming CE, uniformly in tree shape, stopping depth, and dimensions. This is a conservative continuation of a paid reference, not a bound on the price of constructing that reference. It is compatible with, and elementary relative to, the campaign's existing entropy/tree-sandwich baseline; no novelty is claimed for chain-rule telescoping itself.

Let an ancestor quota be A, a previously EXECUTED debit be d, and the current stopped frontier have full expected CE=T. Write the genuinely remaining balance U=A-d-T, with no other reservations suppressed. On replacing frontier leaves by such trees, (5) yields

    A-(d+new erasures)-new terminal CE
       = U + new expected conditional refunds >= U.    (6)

Previously executed debits are never refunded, terminal release is explicit, and no descendant bank is minted. If a pending policy was reserved instead, it must first be identified as pending and replaced once. Equation (6) neither prices unrelated conditional reset bills nor pays a second code describing the same output.

## 3. Source-bound application: A097's incoming negative-cell floor

Use exactly A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1: a>=1,b>=0,r>=1, g=1-2A_a on n=a+b data bits, F=g+2A_r D_n, supplied normalized source R with finite c. Put s=2^-a,t=2^-n,p=2^-r,mu=1-2s,rho=4pt,lambda=2p*2^-b. Empty calibration R0 has mass mu^2 at empty. The original complete floor is

    Rprime=(1-lambda)R0+lambda mu delta_empty+rho U_n,
    Q(U,T)=Rprime(T) P_F(U,T)/q(T),
    q=(1-lambda)P_g+lambda mu delta_empty+rho U_n.

This specific floor is normalized, supports P_F, and is fixed before any subsequent queries. Its original pricing is the independently accepted A097 source theorem, NOT re-proved or upgraded here:

    CE(P_F,Q)<=c+10(C+E+J),
    C=2ptb, E=2pta, J=2rpt,
    CE(P_F,Q)<=(2C0+10)I(F) if c<=C0 I(g).             (7)

A098's full-scope independent reconstruction is consumed with source-byte provenance. Apply (5) to THIS incoming Q, never a fresh descendant floor. For every adaptive finite physical data/control history,

    E sum B_j + E[H(F_leaf)+D(P_leaf||Q_leaf)]
       <= CE(P_F,Q) <= (2C0+10)I(F).                 (8)

The structural source R=P_g gives 18I(F). This closes an erasure-plus-complete-terminal ancestor-account continuation for arbitrary depths on the supplied floor, including active queries and outcomes with constant cores. It does not close A097's stronger desired local influence-scaled or canonical-floor-reset continuation. Known read-once FEI for this family is not new.

For an independent arbitrary Boolean terminal h with complete R_h, an edit-block-only policy leaves its full c_h=CE(P_h,R_h) unchanged at every leaf: Q_leaf=Q_edit,leaf times R_h. Erasures/refunds in (5) are those of the edit block, terminal CE is c_h plus edit terminal CE, and the initial paid account is c_h+(2C0+10)I(F). The proof makes no withdrawal from h's influence or surplus.

## 4. Exact boundary: ancestor payment is not a fresh local bound

Take a=2,b=0,r=1 and the UNIFORM supplied source R on its four Fourier subsets. The actual three-bit truth table (data bits first) is [1,1,1,1,-1,1,1,1]. The calibrated floor has data reference Rprime=(5/8,1/8,1/8,1/8). Query the first active data bit and take physical bit outcome1. The child is identically +1, hence physical influence0. Marginalizing the original complete Q over that queried spectral bit gives

    Q_child=(5/8,1/8,1/8,1/8)

in residual data/control mask order. Its full prescribed terminal CE is log2(8/5)>0, although actual entropy and influence are zero. Here lambda=1 and the original floor is exactly the root spectrum, so even a genuinely matching incoming reference has this local-rate failure. The checker derives all four fractions directly rather than assuming this display. Thus no finite K bounds EVERY inherited leaf CE by K I(leaf). Renormalizing to a fresh point reference would remove a real incoming liability; that is a separate reset requiring its own signed account. This actual reference obstruction is not a Boolean FEI counterexample.

## First unsupported universal line

For arbitrary Boolean f, produce a complete incoming reference Q at cost O(I(f)), or select and price permitted reference resets from genuinely unused signed capacity while keeping all other inherited liabilities. Merely carrying a paid Q is automatic by (3)-(5). A strategy insisting on local CE<=K I at every descendant fails even on the explicit constant child above. NEXT should test the signed reset from this SAME inherited Q to an admissible descendant floor, together with the complementary child's full cost and already booked debit; it should not spend effort proving another conservative no-reset continuation.
