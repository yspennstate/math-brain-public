# A068 / B14 stage 3: a full-support rank reference surviving one-point edits

## exact target, quantifiers, hypotheses and units

For every odd q>=5 let z_j=(-1)^{u_j} and

    F_q(x,z)=MAJ_q(x_i (-1)^{u_i u_{i+1}} : i=1,...,q),

with cyclic indices and 2q independent uniform physical sign bits. Pad with d>=0 unused bits, giving N=2q+d, and flip F_q at any one input v. Denote the edited Boolean function by G and delta=2^{-N}. The x block has q data coordinates; the z block includes the q original controls and all padding coordinates. All entropy and reference costs are in bits.

This stage proves a complete normalized full-support reference R_delta with

    H(G) <= Gamma_delta(G) := sum_A Ghat(A)^2 log_2(1/R_delta(A))
          <= C_reg I_x(G)+2 I_z(G) - (287/1920) I_x(F_q),
    C_reg=log_2(4+e)+2log_2(e*pi)<8.937.

In particular the original numerical block bound survives every single-point edit and every amount of padding for this cyclic family. The exact quadratic representation need not survive the edit. The original support-only reference does not remain valid unchanged; the full-support repair and its entire expected cost are essential. This is an edit-stable proper-class C020 payment, not universal FEI. The all-parameter proof is below. A070 independently accepted this unchanged theorem from the predecessor report; the full author validation package is completed here.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. Read BOARD.md supervisor snapshot 2026-10-13 23:39 UTC, B14 STREAM_NOTES.md v2 dated 2026-10-11 23:25 UTC, and own STATUS.md/LEARNED.md and stage-1 REPORT.md. The lead specifically assigns A068 exact q=5,7 cyclic replay and a point-defected member, so that robustness obligation takes precedence over the prior proposed private-data identification.

Read A088's stage-1 REPORT.md and A068 section in AUDIT.md. It independently accepts A068-QUADRATIC-CONTEXT-RANK-REFERENCE v1 at its precise private-data/quadratic-sign/recovered-C001 scope, including the normalized reference. Its independent exact validation covered the q=5 cyclic example. No A094 acceptance is inferred. A070's scope audit also inspected A068's structural hypotheses but explicitly did not claim a full A068 audit.

Read A069's stable-hierarchy edit-payment stage-1 REPORT.md, Sections 1-4. Its weighted L2 transfer for fixed nonnegative complete code costs and physical edit-influence bound are established tools and already independently reconstructed by A070. The present stage uses the same weighted triangle mechanism, and credits that source; it does not claim to invent perturbation transfer or repeat recursive-majority neighborhoods. The new work is a normalized uniform fallback for a previously support-only quadratic rank reference, and proof that the balanced cyclic margin pays it while preserving the same block coefficient.

The recovered baseline ingredients are the threshold source lem:ranktail/eq:euler-cost and its reference normalization, plus C_reg. The source used in stage 1 is baseline/current-threshold-paper.tex, SHA256 5d87f625fbadad4aa9841416712b8193a869fa9dffcb4e9c200d2f39a62e6a10. No new full-paper audit, web novelty search, brain mutation or claim of universal prior-art novelty is made. Exact source paths/hashes and review records are saved in out/SOURCES.json.


This stage resumes the interrupted 20261012T022241Z run: its report and two-case pilots existed, but full validation and protocol package did not. The original run is preserved without modification. out/PREDECESSOR_REPORT.md preserves the exact report reviewed by A070 (SHA256 3c53ca43f4455a89c327a1671567e10bb825ce6d0b8dce5d4f943f859a0927be). Its premature persistence paragraph is not evidence of completion. All current completion statements refer exclusively to this run.

Read A070's 20261013T212602Z REPORT.md and source-bound claim A070-REVIEW-A068-REPORTED-CYCLIC-EDIT-REFERENCE v1. It reconstructs this all-parameter theorem without a mathematical repair and independently checks 16 edits with 1,932 exact assertions. Its acceptance covers the theorem and accepted base dependency, not previously absent author files. Read A034's stage-1 phase-energy REPORT.md: distinct data labels remain a hypothesis and the two-row collision ledger remains a proposed next action. No completed collision theorem is imported.

## complete derivation or exact first unsupported line

### 1. Independently reconstructed cyclic influences

Put c_q=2^{-(q-1)} binom(q-1,(q-1)/2). Conditional on controls the transformed data signs are independent uniform, so every data influence is c_q. Flipping u_j toggles vote j-1 when u_{j-1}=1 and vote j when u_{j+1}=1. Thus zero, one and two votes toggle with probabilities 1/4,1/2,1/4. Toggling one vote changes majority with probability c_q. Toggling two changes it precisely when those votes agree and the remaining q-2 votes sum to +/-1, also giving c_q. Consequently

    I_x(F_q)=q c_q=:J,
    I_z(F_q)=(3/4)J.

At q=5 these are 15/8 and 45/32; at q=7 they are 35/16 and 105/64. Padding does not change them. The central-binomial recurrence is c_{q+2}/c_q=q/(q+1), so

    (q+2)c_{q+2}/(q c_q)=(q+2)/(q+1)>1,
    J>=15/8 for every odd q>=5.

These formulas are analytic for all q, with independent exact replay at the assigned dimensions in the checker.

### 2. The balanced base reference has a strict saved level cost

Let R_0 be the stage-1 normalized rank/affine-fiber reference for F_q, embedded on the N-dimensional spectrum by putting no Fourier coordinates in the padding block. In data rank order, for |S|=k and control index T,

    R_0(S,T)=w_k [prod_{i in S} i^{-2}/Z_k] 2^{-r_S} 1_{T in L_S},
    Z_k=sum_{|S|=k} prod_{i in S} i^{-2},

where L_S is the affine Fourier support of the quadratic control phase indexed by S, r_S=dim L_S, and w_k is the base majority spectral level mass. It is a probability law: the rank factor normalizes on each level, each affine fiber has 2^{r_S} points, and sum_k w_k=1. Its expected cost charges level selection, rank normalizer, all data ranks and all control affine coordinates exactly as in the accepted stage-1 proof.

Majority is balanced, so w_0=0 and the data spectral level K is positive. The normalized geometric reference 2^{-k}, k>=1, gives H(K)<=E K=J by Gibbs. Replacing the general Boolean level cost C_lev J by this stronger balanced cost in the same Euler rank proof gives

    Gamma_0(F_q) <= B := C_bal J+2 I_z(F_q),
    C_bal=1+2log_2(e*pi)=C_reg-C_lev+1,
    C_lev=log_2(4+e).

Here C_lev>5/2 because 4+e>6>sqrt(32), while C_reg<9. Since I_z=3J/4,

    B=(C_bal+3/2)J<9J,
    C_reg J+2I_z-B=(C_lev-1)J>(3/2)J.

This balanced margin is the budget for the edit. It is not earned again downstream and does not assume the edited function is balanced.

### 3. Uniform fallback; all normalization and edit cross terms retained

Let U_N(A)=2^{-N} on every spectral subset. Define

    R_delta(A)=(1-delta)R_0(A)+delta U_N(A), delta=2^{-N}.

Both branches are normalized, so sum_A R_delta(A)=1; R_delta(A)>=delta 2^{-N}=2^{-2N} at every atom. Its cost L_delta=-log_2 R_delta is nonnegative and at most 2N. For the unedited F_q,

    Gamma_delta(F_q) <= Gamma_0(F_q)+log_2(1/(1-delta))
                       <= B+3delta.

The last estimate follows from -ln(1-delta)<=delta/(1-delta), log_2 e<3/2 and delta<=1/1024. The small base-branch selection cost has not been dropped.

Write e=G-F_q. Its exact one-point Fourier coefficients are

    ehat(A)=-2 F_q(v) delta chi_A(v),
    ehat(A)^2=4delta^2.

Thus its entire weighted edit-spectrum cost is

    sum_A ehat(A)^2 L_delta(A)
       =4delta E_{U_N} L_delta <=8Ndelta.

Weighted Euclidean Minkowski, applied before squaring, gives

    sqrt(Gamma_delta(G))
       <=sqrt(Gamma_delta(F_q))+sqrt(sum_A ehat(A)^2 L_delta(A)),
    Gamma_delta(G) <= (sqrt(B+3delta)+sqrt(8Ndelta))^2.

This keeps the signed coherent cross terms. It is not the false entropy subadditivity of an incoherent mixture. Since R_delta is normalized and positive everywhere, Gibbs gives H(G)<=Gamma_delta(G), even though an edit fills atoms excluded by the original geometry. The reference really describes the complete spectral set, including new padding and empty-data atoms.

### 4. Exact rational payment by the saved margin

For N>=2q>=10, N 2^{-N} is decreasing. Using J>=15/8,

    a:=3delta/J <=1/640,
    b:=8Ndelta/J <=1/24.

B/J<9 implies

    (Gamma_delta(G)-B)/J
       <=a+b+2sqrt[b(9+a)] <=1/640+1/24+5/4.

The final inequality is an exact square comparison:

    4(1/24)(9+1/640)=5761/3840 <25/16=(5/4)^2.

A one-point edit changes each physical coordinate influence by at most 2delta; more precisely its change is 2delta(1-2b_i), where b_i indicates a base disagreeing neighbor at the edited input. Each padding influence becomes 2delta. Ignoring these positive padding contributions for the lower bound,

    C_reg I_x(G)+2I_z(G)
       >=C_reg J+2I_z(F_q)-2qdelta(C_reg+2).

Since C_reg+2<11 and 2q<=N,

    [2qdelta(C_reg+2)]/J <=11Ndelta/J <=11/192.

Combining all costs with the balanced saving gives

    [C_reg I_x(G)+2I_z(G)-Gamma_delta(G)]/J
       >3/2 -1/640 -1/24 -5/4 -11/192
       =287/1920.

This proves the exact all-q/all-padding/all-location claim. Every rare-reference, rank, level and edit charge is in one normalized reference. No terminal core entropy is discarded.

For fixed q and N tending to infinity by padding, the reference-selection cost and weighted edit cost tend to zero. On each original positive atom R_delta converges to R_0, and the finitely many original positive atoms give Gamma_delta(F_q)->Gamma_0(F_q). The forward and reverse weighted triangle inequalities give |sqrt(Gamma_delta(G))-sqrt(Gamma_delta(F_q))|<=sqrt(8Ndelta), hence Gamma_delta(G)->Gamma_0(F_q). Thus the paid functional passes the pad-and-flip test rather than diverging when zeros are filled.

### 5. The exact structural obstruction and remaining unsupported line

At the all-positive input with u=0, F_q=+1. Flipping that value makes the x_i derivative at the remaining all-positive data assignment equal to -1. It is nonzero also at the ordinary central majority pivotal assignments, equal to +1 there. For the final data rank these assignments are comparable to the all-positive assignment in the predecessor cube, so its pivotal support is no longer an antichain in the original conditional orientation. One cannot simply reapply the original fiber proof to the edited function. The old R_0 also has zero mass on all empty-data atoms because w_0=0; the edited function has a nonzero empty Fourier coefficient. Hence R_0 is not even an admissible reference after that edit.

The new statement is an explicit repair, not an assertion that arbitrary point edits preserve quadratic-gate membership. No theorem in stage 1 is refuted or silently strengthened to all edits of every regular/quadratic core.

First unsupported universal line: after private data labels are identified, the signed colliding quadratic packets admit a complete reference with a sufficient paid margin and no dimension-sized fallback bill. The present proof uses both private-label packet structure and the balanced cyclic saving. It gives no universal rank-reference existence theorem, no arbitrary-control FEI claim, and no same-constant edit theorem for every FEI-certified class without a strict saved budget.

### 6. One identified private label: signed interface and failed inherited payment

For any Boolean F with distinct data coordinates 1,2 and arbitrary other coordinates, substitute x_2=epsilon x_1, epsilon in {+1,-1}, obtaining G. Index quotient subsets T by representatives excluding coordinate 2. Direct character substitution gives

    Ghat(T)=Fhat(T)+epsilon Fhat(T symmetric_difference {1,2}).

For any normalized parent reference R covering F's spectrum, define

    R_push(T)=R(T)+R(T symmetric_difference {1,2}).

The two-atom fibers partition the parent spectrum, so R_push is normalized and covers G. It satisfies Gamma_push(G)<=2 Gamma_R(F): use (a+epsilon b)^2<=2(a^2+b^2) and -log R_push(T)<=-log R(A) for either parent atom A. Terms with zero Fourier mass are omitted. This pays the parent cost, not the physical influence of G.

The naive universal replacement Gamma_push(G)<=K I(G) fails for every finite K. Take regular h=AND2 (output +1 only at (+1,+1)), constant quadratic orientations (+1,-1), and F(x_1,x_2)=h(x_1,-x_2). In spectral order empty,{1},{2},{1,2}, its coefficients are (-1/2,+1/2,-1/2,-1/2). Its accepted rank reference has weights (1/4,2/5,1/10,1/4), from level masses (1/4,1/2,1/4) and singleton rank weights proportional to (1,1/4). Identifying x_2=x_1 gives G=-1 but R_push=(1/2,1/2). Thus H(G)=I(G)=0 and Gamma_push(G)=1 bit. G itself has a free reference concentrated at the empty atom. This refutes the inherited payment, not FEI or existence of an adaptive paid output reference.

The frozen exhaustive 32-case two-bit check verifies the signed coefficient identity, factor-two inequality, Boolean normalization and influence with fresh truth tables, plus this exact reference witness. It does not certify larger colliding quadratic packets. The first unsupported line is a cancellation-aware normalized replacement reference paid by output influence, with all terminal entropy retained. A034's available stage-1 report still proposes its two-row collision ledger as NEXT; no completed ledger is assumed. These elementary identities carry no novelty claim against other streams' broader collision work.

## executed validation with domain, arithmetic, commands and outputs

The frozen specification out/FROZEN_SPEC.json precedes execution. It declares q=5,7; padding d=0,2,4; four fixed data edit assignments and four fixed control edit assignments, with padding edit assignment zero: 96 targeted actual Boolean edits, plus two base replays. This is not an exhaustive edit census or a symmetry reduction. The all-location assertion comes from the proof above.

Commands from the A068 workspace:

    python -X utf8 runs/20261013T234128Z-fleet05-A068-antichain-beyond-one-order/code/check_edit.py

The predecessor v2 bounded pilot passed before the unchanged full job resumed here. Current out/validation.json records PASS on 96 edits and two base replays, 2,589 exact assertions, in 23.458 seconds. Results are summarized in out/SUMMARY.json. A separate frozen check, python -X utf8 runs/20261013T234128Z-fleet05-A068-antichain-beyond-one-order/code/check_collision.py, passed all 32 signed-identification cases and 196 assertions in under 0.01 seconds; see out/COLLISION_SPEC.json and out/collision.json. The new implementation builds actual base truth tables and an integer FWHT, independently reconstructs every data-indexed quadratic packet with F2 polar-rank elimination, verifies physical and spectral block influences, and compares rank-one edits with a fresh actual edited truth-table FWHT for every unpadded fixture. Padding and all added spectral atoms are accounted for exactly by the coefficient formula and direct local edge updates.

R_0 and the mixture normalizations are checked with Fraction. Entropy and the *complete mixture-reference cost* use outward rational logarithm intervals: reduce to [1,2), t=(y-1)/(y+1), retain 22 terms of 2 sum_{j=0}^{21} t^{2j+1}/(2j+1), and bound the tail by 2t^{45}/[45(1-t^2)]. Positive ln 2 division uses the correct outward endpoints. Every edit is certified against the stronger rational coefficient 8I_x+2I_z; C_reg>8 follows from (4+e)e^2 pi^2>6*7*9>256. Output margins are rounded downward to 10^{-12}; entropy/cost endpoints are rounded outward. No floating-point entropy, scan fit or dimension extrapolation is used as proof.

The memory estimate is 40 MB, below the memok-trigger threshold. The pilot cap is 60 seconds and full cap 180 seconds with a 170-second internal guard. No GPU, persistent process, dimension escalation or heavy job was launched.

## proof dependencies and changed downstream conclusions

The dependency chain uses A068-QUADRATIC-CONTEXT-RANK-REFERENCE v1 as accepted at scope by A088, its explicit recovered C001 dependency, elementary balanced-level Gibbs, and the weighted L2/edit edge-count mechanism independently reconstructed from A069/A070. The precise expected-cost repair and unchanged cyclic coefficient are new local conclusions; the unchanged theorem was independently reconstructed and accepted at stated scope by A070 from the preserved report. Current fixtures and the narrow collision obstruction remain available for further review. A088's acceptance is recorded with source provenance, not inferred from the board alone. A070/A094 may challenge the new extension.

The lead's required q=5,7 and point-defect tests are satisfied with actual normalized reference costs rather than only numerical H/I values. A067/A070 can distinguish the failing exact antichain/support geometry from the valid paid full-support repair. B02/B04/B12 may use this point-edit-stable endpoint under the declared cyclic hypotheses; it is not permission to remove private data labels for free. The reference adapts to the known base geometry and N, never to the realized Fourier sample, and its uniform branch has an explicitly paid prior.

## one next mathematical action and independent reviewer

With the lead-directed edit-stability obligation settled, resume the single private-data identification from stage 1. Use the signed paired coefficients above to construct an output reference refunding destructive cancellation at one identified pair in a quadratic-oriented regular core; retain terminal entropy and every normalization charge. A034 may supply a future ledger, but its available source does not yet do so. Independent reviewers are A070 and A094; A088 can review the dependency substitution. No message is sent to other agents.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/, frozen specification and exact outputs are saved only in this A068 run. out/RECEIPTS.json contains local SHA256 and sizes; out/SCHEMA_CHECK.json confirms protocol field sets and compatibility-copy equality. STATUS.md remains two lines; WORKLOG.md is appended and LEARNED.md updated with the exact edit theorem and its limitations. No shared index, other-agent file, brain, Git, public repository, scheduler, email or mirror has been modified. Supervisor collection, shared-registry adoption, mirror verification and additional review remain pending. A070's source-bound theorem acceptance is already available and is distinct from these persistence states. The interrupted predecessor run has not been rewritten.

Universal bridge: this stage advances C020 whole-set witness cost by completing the lead-directed paid full-support rank reference after every one-point edit of padded cyclic quadratic-controlled majority, with all-size slack (287/1920) I_x(F_q), independent A070 reconstruction and 96 exact current fixtures. It also closes the naive inherited-reference payment after one private-data identification: a regular AND2 core gives one bit of cost at zero output influence. What remains is a signed cancellation refund and normalized replacement reference retaining terminal entropy when private labels collide, then a universal existence/payment argument. Constructing that refund at one identified pair is the shortest next route toward full FEI because it removes the precise hypothesis protecting the current complete reference and addresses an actual unpaid cost rather than adding another isolated class bound.
