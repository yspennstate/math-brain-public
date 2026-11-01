# A037: activated bent-surgery posterior and reset ledger

Full FEI remains OPEN. This stage completes the B08 lead's requested k=2 tree calculation, consumes the independent review of A037 v1, and derives a fixed-core all-rarity cancellation law. It does not repeat the known entropy bound for this family or claim a universal payment theorem.

## exact target, quantifiers, hypotheses and units

Bits throughout. Physical inputs are independent fair bits indexed x0,x1,z0,...,z_(r-1),y. Let b(x)=(-1)^(x0*x1), b'(x)=b(x)-2*1[x=0]. The selector core g(x,y) is b for y=0 and b' for y=1. Set F_r=1+1[z=0](g-1). The principal finite certificate is r=4, a genuine seven-bit Boolean function. This k=2 endpoint lies outside B05's original k>=4 bent no-go theorem; it is the explicit endpoint requested by the lead.

At a node f_h querying i, d_h=Inf_i(f_h), D_h=h2(d_h), A_h=I(S_i;S_-i) (the lead's I_h, NOT physical influence), B_h=D_h-A_h, J_h=JS(P_child0,P_child1), and G_h=Gamma_h=sum_(j!=i)[h2(d_j)-average h2(d_j^child)]. M=sum_j h2(d_j), TC=M-H. Node weights are actual physical reach probabilities, not spectral occupancy weights. Inactive constant branches stop and their zero terminal accounts remain explicit.

Five frozen trees: CF-core queries four controls and retains g as terminal on the live branch; CF-split queries controls then selector and retains b,b'; SF-split queries selector then controls and retains b,b'; CF-full and SF-full append x0,x1 to the respective split order and stop at constants. These are specified orders, not optimized trees. Every node's posterior, reset and terminal account is retained in out/EXACT_LEDGER.json.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json, fei-execution-protocol/2 revision 2026-10-11-execution-v2, was reread in this invocation; exact schema fields persist. BOARD.md was reread at this stage (snapshot 2026-10-14 04:29 UTC), as were STATUS.md and B08 STREAM_NOTES.md v2, 2026-10-11 23:35Z. The lead's explicit A037 action is the k=2 control/selector order ledger; its warning forbids treating generic chain rules or the lift as new FEI payment.

Read lead REPORT.md in claude/B08/runs/20261011T225000Z-claude-B08-tc-restriction-ledger, Sections 3.1-3.2, 3.5 and 6; A039 REPORT.md and DEPENDENCY_REVIEW.md in runs/20261011T223903Z-fleet05-A039-projection-under-restrictions, plus its CLAIMS.json; A023 REPORT.md in runs/20261011T221608Z-fleet05-A023-amortized-rarity-budget for the already closed rare-family payment; original B05 REPORT.md (20261011T193057Z), Sections 2-3 and 7; own v1 REPORT/CLAIMS, stage 20261011T220010Z. Sources are pinned by hashes in out/SOURCES_READ.json.

A039 independently accepted both A037 v1 claims at stated scope, without repair; B08 lead independently reconstructed the physical lift and classified it correctly as bookkeeping. This run records those receipts without editing old runs or shared registries. The earlier 20261012/20261013/20261014T015149 directories do not contain completed reports; directory existence and the board's stages counter do not establish completed mathematics. Those interrupted invocations are not counted as substantive failed mechanisms.

The latest board shows A038/A039 advancing overlapping-control occupancy ownership and A023's disjoint rarity payment already complete. Accordingly the current contribution is a precise baseline cancellation/owner diagnosis for transfer, not another isolated family FEI result. The later occupancy claims are not used as premises here.

## complete derivation or exact first unsupported line

### 1. Compensated identity and common reference convention

Parent residual law q(T) is the average of actual signed-transform child squared laws p0(T),p1(T). Hence H(f)=B_h+J_h+average H(child). The marginal influences average, giving M(f)=D_h+G_h+average M(child). Subtract and use B_h=D_h-A_h:

    TC(f_h)=A_h-J_h+G_h+average TC(child).

Summing with physical weights w_h gives exactly

    sum w_h A_h + sum w_h G_h + E TC(leaf)
      = TC(root)+sum w_h J_h,
    sum w_h(D_h-A_h)+E H(leaf)=H(root)-sum w_h J_h.

These are the existing compensated identities, independently reconstructed here for the selected application; they are not claimed as a new theorem. They distinguish correlation credit A_h from the physical-child mixture credit J_h.

For a direct compatible reference check, let Q(T) be the product of the parent's residual spectral marginals. Use k(y|T)=p_y(T)/(2q(T)) on positive q fibers and k=1/2 on zero fibers for BOTH P and Q. Then Q_Y(y)=sum_T Q(T)k(y|T), and Bayes-predicted child reference Q_y(T)=Q(T)k(y|T)/Q_Y(y). Let R_y be the product of the actual child marginals. The signed reset is delta_y=E_(p_y) log2(Q_y/R_y). Its exact identity is

    average delta_y = D_2(fair||Q_Y)+J_h-G_h.

The code computes delta directly from rational Q_y,R_y, rather than defining it by the right side. Channel injection is zero under this common-kernel convention. Zero-fiber extensions may change D_out and delta separately; the convention is frozen and their compensated difference is invariant. A negative reset is a saving relative to the transported reference, not an independent newly minted bank.

### 2. Exact r=4 tree ledger

The root has I=19/64. Each displayed number below is a rounded illustration of an exact rational prime-log vector saved in out/EXACT_LEDGER.json. Those vectors, not these decimals, certify the identities. The interval certificates separately prove the stated comparisons.

| Tree | sum D | sum A | sum Gamma | sum JS | E TC(leaf) | E H(leaf) | sum B + E H(leaf) |
|---|---:|---:|---:|---:|---:|---:|---:|
| CF-core | .790760418 | .318701339 | .811065157 | .397939178 | .013557324 | .138557324 | .610616403 |
| CF-split | .841465300 | .327648581 | .849974922 | .432238862 | 0 | .0625 | .576316719 |
| SF-split | .887845102 | .371399951 | .803595121 | .429610429 | 0 | .0625 | .578945151 |
| CF-full | .872715300 | .327648581 | .881224922 | .463488862 | 0 | 0 | .545066719 |
| SF-full | .919095102 | .371399951 | .834845121 | .460860429 | 0 | 0 | .547695151 |

Root H is approximately 1.008555581 and root TC approximately .745384642. CF-split and SF-split have the same complete leaf spectra and expected leaf entropy 1/16, but different intermediate erasure/JS allocations. Certified SF-split minus CF-split net bill lies strictly between 26/10000 and 27/10000 bits. Appending the same data suffix subtracts 1/32 bit from both net bills, so the full-tree gap is identical. Each of the five retained-terminal net bills is certified below 8I; this is calibration, not a new family FEI bound (A023 already paid it).

The reset totals for CF-core, CF-split, SF-split are approximately -.353418234, -.357575204, -.363763338; all are certified negative. Their respective sum D_out values are .059707745, .060160856, .010221353. The different reset decompositions cannot be added across the two trees. Either complete ledger uses its own single sequence of inherited references.

### 3. Which node class owns the unpaid term?

CF-split weighted control erasure is .472059079, selector erasure .041757640, terminal entropy .0625. SF-split weighted control erasure is .462076744, root-selector erasure .054368408, terminal entropy .0625. The control chain carries most of the retained erasure. The root selector in SF has B/d approximately 3.479578; the terminal selector in CF has B/d approximately 2.672489. None of these finite ratios is an all-dimensional bound or an optimized good-coordinate constant.

In CF the four live control nodes have d=3/64,3/32,3/16,3/8 and weights 1,1/2,1/4,1/8. Their B/d values are approximately 2.381374,2.562165,2.695888,2.431167. Their Gamma values are approximately .258497,.435011,.722494,1.235515. Inactive control branches are constants. The remaining active selector core carries the saved terminal account at weight 1/16; after selector exposure the b branch retains two bits of entropy at weight 1/32, and the b' character retains zero. This names actual node/terminal owners instead of calling all correlation KL a fungible bank.

### 4. All-rarity quadratic cancellation for this fixed core

The core's Fourier coefficients are seven atoms of magnitude 1/4 (including empty) and one coefficient -3/4. Thus beta=E g=1/4, c=1-beta=3/4, I(g)=7/4, H(g)=4-(9/8)log2 3, M(g)=6-(9/4)log2 3, TC(g)=2-(9/8)log2 3. Put p=2^-r. The live control node with m unexposed controls is F_m and is reached with weight p*2^m; its control influence is c*2^-m and core-coordinate influences are (3/4,3/4,1/4)*2^-m.

Consequently the exact marginal control charge is

    D_ctrl(r)=p sum_(m=1)^r 2^m h2(c*2^-m).

Set phi(t)=h2(t)-h2(2t)/2. The exact reset-transfer sum is

    G_ctrl(r)=p sum_(m=1)^r 2^m [ (m-1)phi(c*2^-m)
                                  +2phi((3/4)*2^-m)+phi((1/4)*2^-m) ],
    D_ctrl(r)+G_ctrl(r)+p M(g)=M(F_r).

No independent reserve is created by this equality: it is the marginal-entropy telescope on the same physical path.

For 0<t<1, expand -ln(1-t) to obtain

    h2(t)=t log2(1/t)+t log2(e)-R(t),
    0<=R(t)<=t^2/[2(1-t) ln2].

Since t<=3/8 along these live controls and sum_(m>=1)2^-m=1,

    D_ctrl(r)/p=(3/8)r(r+1)+(3/4)r log2(4e/3)+epsilon_r,
    -9/(20 ln2)<=epsilon_r<=0.

This explicitly proves a quadratic marginal bill. Also M(F_r)=(r+2)h2(3p/4)+h2(p/4)=(3/4)p r^2+O(pr). Therefore G_ctrl(r)=(3/8)p r^2+O(pr), with constants depending only on this fixed core.

For completeness the exact root entropy comes from the empty atom (1-3p/4)^2, 2^r-1 control-only atoms (3p/4)^2, and 2^r copies of each nonempty core atom p^2*ghat(T)^2:

    H(F_r)=-(1-3p/4)^2 log2((1-3p/4)^2)
           +(3p-9p^2/8)r
           +p[6-(9/4)log2 3]-p^2[9/4-(9/8)log2 3].

In particular H(F_r)<=3pr+p[M(g)+(3/2)log2(e)]. The empty-atom bound uses -u log2 u<=(1-u)log2(e), and the other coefficients are explicit. Since 0<=B_ctrl<=H(F_r)-p H(g), the released correlation sum A_ctrl=D_ctrl-B_ctrl obeys

    A_ctrl(r)=(3/8)p r^2+O(pr).

The physical influence is I(F_r)=p(7+3r)/4. Hence D_ctrl/I, A_ctrl/I and G_ctrl/I each grow as r/2+O(1), while the retained-terminal erasure bill B_ctrl+p H(g) is O(I). The resource TC(F_r) itself has a quadratic leading term. This is a quantitative explanation of why these accounts can each be much larger than influence and still cancel in one owned ledger. It does not license spending their magnitudes separately. It is confined to this fixed core; no claim is made about arbitrary overlapping controls or core witnesses.

### 5. Exact first unsupported line

The missing universal implication is: after an actual mixed control/data query in overlapping activations, charge the signed reset/conversion residual to one demonstrably unused child/core surplus while retaining both complete terminal references. Neither the k=2 cancellation identity nor positive root TC proves that implication. Pricing Gamma locally by d or by d+JS remains refuted; repeating that failed mechanism is not proposed.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before the search. Command from A037:

    python -X utf8 runs\20261014T043944Z-fleet05-A037-conditional-credit-ledger\code\tree_ledger.py

Integer FWHT supplies exact coefficients; Fraction supplies probabilities, reach weights, influences and Bayesian reference masses. Entropy identities are checked by cancellation of rational coefficients of log2(prime). Every local TC identity, influence telescope, direct signed reset identity and five global terminal-inclusive balances is checked. Four independently built truth tables r=1..4 check the core/root formulas; r=5..12 use formula-only summaries and are not additional truth-table runs. No random or floating search was performed.

The rational log intervals use power-of-two range reduction and 96 terms of 2 sum z^(2j+1)/(2j+1), with rigorous remaining upper bound 2z^193/[193(1-z^2)], |z|<=1/3. Division by ln2 uses positive lower/upper endpoints and swaps interval endpoints for negative coefficients. Intervals certify the order gap, negative resets and each net bill below 8I. Runtime/assertion counts and exact vectors are in out/EXACT_LEDGER.json; current execution is recorded by the local persistence receipt. All jobs have <30 MB estimated memory and <60 seconds measured compute; no >300 MB job was started.

## proof dependencies and changed downstream conclusions

The finite ledger and all-rarity formulas are proved directly from this truth table, Walsh orthogonality and finite entropy/KL algebra. A039's compensated transfer and B08 lead L1/L2 are credited as existing interfaces, independently reconstructed; no unsupported later occupancy theorem is assumed. The original A037 claims retain their v1 mathematical statements and now have source-bound local acceptance receipts from A039 and the lead. Their immutable original files are unchanged.

A023 owns the existing rarity-family FEI payment; no duplicate new bound is registered. A039/A064/A097 now receive exact node/class charge and signed-reference benchmarks plus a quantitative account-cancellation diagnostic. This stage registers one narrow applied claim; it does not open another broad universal candidate while stream review queues remain substantial. Shared adoption and external review remain B20's responsibilities.

## one next mathematical action and independent reviewer

Next: consume A038/A039's exact shared-control occupancy fixture at one subsequent physical query; compute its signed inherited-reference reset together with both terminal costs, and determine whether the alleged source slack is unused after conditioning. Use the current exact class-account conventions. Reviewers: A088/A094 (independent review pending for the new application); A039 may review the application if it supplied no substantive repair.

## actual persistence receipts or precise save blocker

All writes are confined to A037. The run includes REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/tree_ledger.py, code/persist.py, out/FROZEN_SPEC.json, out/EXACT_LEDGER.json, out/SOURCES_READ.json and out/ARTIFACT_SHA256.json. STATUS.md, WORKLOG.md and LEARNED.md are updated. Hash/schema receipts validate local files; supervisor copying, brain ingestion, mirrors, shared registry adoption and downstream use are not claimed.

Universal bridge: This stage advances C024 history transfer and the C019 stopping-tree payment interface by closing the lead's exact five-tree benchmark with terminal accounts and direct compatible-reference resets, and proving that this fixed-core activation spends/cancels three quadratic accounts inside one owned resource. It contributes no universal constant: the bridge still lacks an actual unused child-slack payment after mixed shared-control/data exposure. NEXT is the shortest useful route because the finite disjoint-control baseline is now fully priced and the remaining obstruction is ownership under conditioning, which the live A038/A039 fixture directly tests; another independent rare-family entropy bound would not close that gap.
