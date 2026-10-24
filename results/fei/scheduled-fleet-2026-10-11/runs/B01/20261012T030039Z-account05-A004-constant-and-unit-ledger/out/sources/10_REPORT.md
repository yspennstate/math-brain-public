# A038 stage 2: exact release of point-defect normalization credit

## exact target, quantifiers, hypotheses and units

Follow B08 lead notes v2: determine how much of root Delta is released as Gamma versus occupancy mutual-information credit along a physical coordinate tree of a point defect. This stage resolves that scoped mathematical target analytically with explicit error bounds, and prices the actual Bayes-reference reset. Full FEI remains OPEN.

For every integer n>=2, let f_n=1-2*1_{x=0} on the uniform physical cube. At every nonconstant node query an unqueried physical coordinate, with adaptive choices allowed, stopping at constant leaves. Physical translations and a global output sign give the same squared laws. All such complete singleton trees have the same ledger; no choice of coordinate order is assumed favorable. Proper-block queries and stopping at paid nonconstant leaves are outside the no-go scope.

Information is in bits; L=log2(e). Use the lead's notation M=sum_i h2(Inf_i), TC=M-H, Gamma_i=sum_{j!=i}[h2(Inf_j(parent))-average h2(Inf_j(child))]. Credit C_h=I(S_i;S_-i) is mutual information, distinct from physical total influence I. For point defects, source-exact K_occ=0 at every active node and Delta=TC. Constant leaves have Delta=TC=0. The k=1 character endpoint has zero spectral entropy and all information charges zero.

Main quantified results: let d=2^(1-n), I_n=nd and weighted tree sums G_n=sum w_h Gamma_h, C_n=sum w_h C_h, J_n=sum w_h JS_h. Then
Delta_n+J_n=G_n+C_n,
G_n=n h2(d)-sum_{k=1}^n 2^(k-n)h2(2^(1-k)).
For A_n=n(n-1)/2,
A_n d <=G_n<=(A_n+2L)d,
[2(n-1)-1]d<=J_n<=[2(n-1)+4L-1]d.
Consequently G_n/Delta_n and C_n/Delta_n tend to 1/2, J_n/Delta_n tends to zero. Ratios to Delta are used only for n>=3; Delta_2=0.

With the source-compatible coherent reveal kernel applied under both P and its product reference, the accumulated Bayes-outcome KL O_n and signed reference-reset correction R_n satisfy
0<=O_n<=8L d,
R_n=O_n+J_n-G_n, R_n/Delta_n -> -1/2.
The source kernel has no channel injection. Its signed reference reset cannot be discarded. Accumulated Gamma is not O(I) on ANY full singleton coordinate tree of these sources, since G_n/I_n>=(n-1)/2. This is not a statement about arbitrary proper-block rules or FEI failure.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor timestamp 2026-10-12 01:21 UTC; read B08 STREAM_NOTES.md v2 dated 2026-10-11 23:35Z and own STATUS.md. The lead is now present and explicitly assigns the point-defect release target. There is no disagreement with the lead. Read EXECUTION_PROTOCOL.json in full again, revision 2026-10-11-execution-v2. Prior campaign context and exact occupancy source remain the same source-complete inputs from stage 1; no generic Brain recall or remote-source re-fetch was needed this stage.

Read A039's run 20261011T223903Z-account05-A039-projection-under-restrictions: REPORT.md, DERIVATION.md, DEPENDENCY_REVIEW.md. The mathematical locators are compensated identity (1), Bayes reset (3), occupancy split (4), and point-defect local correction (5)-(6). It independently accepts A038's normalization interface and normalization-gap obstruction at partial scope, not the separate collision theorem. A039's physical transfer explicitly uses that interface, so mathematical downstream use of this stage-1 subresult is observed; shared index adoption remains unobserved. A088's current claims were inspected for review coverage; they do not supply acceptance of this new result.

Read own stage-1 REPORT.md, code/check.py and source-exact K_OCC_DEFINITION.md. The latter is original account02/B15 Theorem 2.1 and Section 4, retrieved at commit 2bf247373576eb406ca91bb3ea5f3ce5e5ab8588, blob 5ce14eaaec34f0d91f2d430dba576e19dddc6894. No occupancy definition was changed: K_occ=D(P+||Q_r), and K_full=v K_occ+Delta. The retired fixed-positive reserve remains retired. This run neither re-tests its collision falsifier nor re-proves the point-defect class FEI estimate.

The threshold/percolation manuscripts and earlier campaign materials were read at applicable interfaces last stage. They supply orientation only and no mathematical premise for this calculation; no new literature or novelty claim is made. Local source readback hashes and the exact prior source path are preserved in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

The full derivation, including all endpoint and inequality details, is in DERIVATION.md. The central calculation is as follows.

At the unique active node with k coordinates left, let d_k=2^(1-k). Its visit probability is w_k=2^(k-n), so w_k d_k=d. The next physical outcomes are a constant and a (k-1)-bit point defect, each with probability 1/2. Write phi(t)=h2(t)-h2(2t)/2, q0_k=(1-d_k)^2+d_k^2 and beta_k=2d_k(1-d_k). Directly from the actual Walsh law,
Gamma_k=(k-1)phi(d_k),
JS_k=phi(beta_k),
B_k=q0_k h2(d_k^2/q0_k)+beta_k,
C_k=h2(d_k)-B_k.
The exact nonempty residual-fiber contribution is beta_k; its undercount in the initial draft was caught by the first exact checker and corrected before any successful certificate.

With H_k the exact source entropy and Delta_k=k h2(d_k)-H_k,
H_k=B_k+JS_k+H_(k-1)/2,
Delta_k=C_k+Gamma_k-JS_k+Delta_(k-1)/2.
Multiplying by w_k and telescoping proves Delta_n+J_n=G_n+C_n and H_n=B_n^tree+J_n with no unpaid leaf silently discarded. Directly telescoping the phi formula yields the closed G_n above.

For h(t)/t=log2(1/t)+L+e(t), elementary logarithm inequalities give -Lt<=e(t)<=0, including t=1 by continuity. Since sum_k d_k<2, the weighted marginal-entropy sum is
S_n/d=n(n-1)/2+nL+E_n, -2L<=E_n<=0.
This proves the upper G_n bound. The lower bound follows from phi'(t)=1+log2[(1-t)/(1-2t)]>=1, hence phi(t)>=t. No numerical extrapolation establishes either bound.

For k>=3, beta_k<=3/8. Integrating the same derivative and using ln(1+u)<=u proves 0<=phi(x)-x<=2Lx^2 on [0,3/8]. Therefore
2-2d_k<=JS_k/d_k<=2+(8L-2)d_k.
The exact k=2 endpoint has JS_2/d_2=2. Summation gives the displayed J_n bounds. The existing exact H_k formula, with its empty contribution enclosed by elementary logs, gives
H_n/d=4(n-1)+2L+E_H,n,
-[2(n-1)+4L]d<=E_H,n<=0.
This is used for release/error quantification, not presented as a new class entropy theorem. It yields
Delta_n/I_n=n-5+L+o(1),
G_n/I_n=(n-1)/2+O(1/n),
C_n/I_n=(n-1)/2+L-2+O(1/n),
J_n/I_n=2+O(1/n),
B_n^tree/I_n=2+O(1/n).
The explicit bounds in DERIVATION.md include an all-n enclosure for C_n, so every asymptotic has a proved uniform error.

At k>=2, apply the actual coherent kernel to the parent residual product reference. The reference outcome probability of the constant child is
q_k=(1-d_k)^(k-1)/(2q0_k),
giving O_k=-log2[4q_k(1-q_k)]/2.
A039's signed Bayes-reference correction is independently reconstructed on actual child atoms:
rho_k=O_k+JS_k-Gamma_k.
For k>=3, q_k lies in [1/4,1/2], epsilon_k=1-2q_k<=2(k-2)d_k, and
O_k<= (8L/3)(k-2)^2 d_k^2.
The k=1,2 output charges vanish. Since sum_{k>=3}(k-2)^2 d_k=3, summing gives O_n<=8Ld. Thus R_n=O_n+J_n-G_n and R_n/Delta_n -> -1/2. The same bounds prove R_n<0 for all n>=9.

Finite normalization matters: n=2 has Delta=0, G=J=1 and C=0. It would be false to call Gamma and mutual information two nonnegative shares of root Delta at every finite n. Only the retained-JS identity and its asymptotic proportions are proved.

The first unsupported universal line is paying NET cumulative erased-label/witness cost plus terminal core entropy on overlapping activated sources or arbitrary Boolean functions with one nonreused physical influence budget. Here S_n-C_n=B_n^tree has a linear influence ratio even while G_n and C_n each have diverging ratios. Bounding a positive reference component again is not that missing payment.

## executed validation with domain, arithmetic, commands and outputs

Specifications were frozen before execution in out/FROZEN_SPEC.json, TARGET.md, and RESET_SUPPLEMENT_SPEC.json. Search-free domains: compressed n=2,...,16, direct Walsh tree reconstruction n=2,...,7, and all 32 physical query orders for n=2,3,4. The reset supplement uses the same dimensions and six direct actual kernel/reference atom checks. No dimension was raised automatically.

Commands from A038:
python -X utf8 runs/20261012T012321Z-account05-A038-occupancy-term-audit/code/tree_release.py
python -X utf8 runs/20261012T012321Z-account05-A038-occupancy-term-audit/code/reset_check.py

Probabilities and physical influences use integer Walsh transforms and Fraction arithmetic. Exact entropy/KL identities require complete cancellation of rational coefficients of logarithms; bounded small-factor extraction leaves residual integers as exact formal log atoms and recognizes squares. Zero coefficient cancellation is a sufficient identity certificate. Signs and finite ratio enclosures use range-reduced 20-term atanh logarithm sums with explicit tail 2t^41/[41(1-t^2)] and correctly signed positive-ln2 division. Intervals are rounded outward to rational multiples of 10^-12. No float establishes a sign.

The first local-identity check failed because the draft counted the nonempty residual fibers incorrectly. out/INITIAL_CHECK_FAILURE.md records the unsupported line and correction. That incomplete run is not a certificate. The corrected release run passed 330 assertions in 32.1343374 seconds; the reset supplement passed 303 assertions in 45.7114759 seconds. Both are under the 60-second pilot cap, and their completed outputs are out/VALIDATION.json and out/RESET_VALIDATION.json. The reset checker loads only pure helper declarations from the first checker via AST, without executing its jobs. Both scripts have a 58-second guard. No job was expected to exceed 300 MB; the frozen estimate was 50 MB, so no heavy-job memok admission was needed.

At n=16 the exact release certificate encloses
G_n/I_n in [7.641764589382,7.641764589383],
C_n/I_n in [6.771496661321,6.771496661322],
J_n/I_n in [1.900859628358,1.900859628359],
Delta_n/I_n in [12.512401622344,12.512401622345].
These finite ratios need not equal their limiting fractions; the analytic error bounds establish the limits. Final receipts check schema, statement hash, compatibility equality and file sizes. Self-validation is not independent review.

## proof dependencies and changed downstream conclusions

This is a scoped verification/closure of the lead's existing normalization mechanism, not another broad universal positive candidate while B08 has queued claims. The exact source definition and actual point-defect Fourier law are retained. All tree formulas and Bayes-node identities are independently derived in this restricted family; no unreviewed universal payment premise is used. Standard finite KL/entropy algebra and elementary log bounds are the only mathematical tools.

The old claim is not overwritten. A039's independent partial review and actual use of A038's normalization identity are recorded with their precise scope. This stage adds explicit all-tree release fractions and the uniform Bayes-output bound. It does not duplicate A039's general chain rule or local Gamma falsifier as new work, and it does not refute a source-compatible net ledger.

A039/A037/A064 should retain O+J-G as the signed reset rather than charge Gamma from source influence or treat all root Delta as immediately available posterior credit. A040 receives the all-singleton-tree aggregate obstruction and its exact scope. A088/A094 are requested to review the release bounds, finite injection endpoint, and Bayes-support calculation. B20 may adopt the new scoped audit after review; no shared-index adoption or external acceptance is claimed.

## one next mathematical action and independent reviewer

Next: use this exact common-kernel ledger on F=1+(A OR B)(g-1), where A and B are rare control subcube events sharing one physical coordinate and g is an explicit retained Boolean core. Track the shared control's first physical revelation, the signed reset, and terminal H(g) together. The goal is a net transfer/cancellation law with ownership, not separate O(I) prices for Gamma or Delta. A088 is primary reviewer; A094 alternate. The complete point-defect release baseline can now be retired unless a specific review correction arrives.

## actual persistence receipts or precise save blocker

REPORT.md, DERIVATION.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, both checkers, frozen specifications, failure record and successful outputs are local to the authorized A038 stage directory. STATUS.md is current; dated WORKLOG.md is appended and LEARNED.md retains the quantitative formulas. out/SOURCE_RECEIPTS.json pins the exact inputs, and out/ARTIFACT_SHA256.json records final local readback hashes and sizes. No git command, brain write, other-agent write, shared-index mutation, mail or external publication occurred. Supervisor copying, mirror verification and independent review remain unobserved.

Universal bridge: This stage advances C024 history transfer and the bookkeeping portion of C019 stopping-tree payment by closing the lead's exact point-defect Delta-release question: both reset Gamma and posterior credit take asymptotic half-shares, with explicit JS injection and a Bayes-output charge at most 8 log2(e) d; the resulting signed reset is asymptotically minus half the root Delta. It supplies no new universal FEI constant and leaves complete erasure/witness and terminal-core payment open. The shortest NEXT is first-revelation ownership for two overlapping rare events under this same common reference, because the now-certified large signed cancellation shows that isolated positive-component bounds cannot reach the universal endpoint.
