# A017 / B04 stage 2: point-flipped quadratic addressing

Run `20261011T234546Z-account05-A017-recursive-addressing`. Full FEI OPEN. Exact ledger and restricted stopping-tree proof complete locally; independent acceptance and supervisor transfer pending. B04 lead v2's assigned point-flipped-fiber target is resolved at the stated scope.

## exact target, quantifiers, hypotheses and units

Let n>=1, M:F2^n->F2^a be any fixed linear address map, and q a quadratic polynomial with q(0)=0. With independent uniform binary controls x and distinct sign data y_z, let b=(-1)^q, g=b-2*1_(x=0), and F*=g(x)y_(Mx). This is a single genuine Boolean point flip. The exact entropy and physical influence formulas below hold even with linear terms in q. The stopping-tree theorem requires q to have zero linear term. Input reuse in any program computing M is allowed; the final data coordinates remain distinct. Entropy is in bits, physical influence uses the uniform cube, and I(D_i) for a real derivative means its Fourier Dirichlet energy, not a Boolean pivotal probability.

Resolved: exact H/I for every such quadratic/address pair; finite certificates through n=6 for the specified frozen families; the fixed-r limit for the standard matching quadratic and prefix address map; exact root physical boundary charges; and a nonreusing, terminal-inclusive tree with zero bad-node boundary charge at threshold K=2 and H(F*)<=4(I(F*)-1).

## sources actually read, revisions and theorem locators

The updated BOARD.md (2026-10-11 23:39 UTC), B04 STREAM_NOTES.md v2 (23:25 UTC), own STATUS.md, and previous stage's full RECURSIVE_ADDRESSING.tex were read. The lead reports the A017 ledger HOLDS after 300 independent exact cases; this is recorded as scoped lead review evidence, not new A091/A090 acceptance. New direction: point-flipped quadratic fibers and which physical coordinates carry 2I(D). The lead identifies C019's remaining line as an adaptive tree paying boundary energy only when the exact B_i exceeds K*Inf_i. The other B04 agents are handling the generic selector bound, its audit, activations and finite falsifiers; those baselines were not re-derived as new results.

Read the lead run's CLAIMS.json, specifically B04-NODE-BOUNDARY v1 and B04-SECOND-MOMENT-PRICE v1, as motivation. Its REPORT.md is absent; no unstated proof from that missing report is assumed. The tree theorem here uses elementary B_i<=1, JS_i<=1 and exact restriction telescoping, so it does not depend on accepting the lead's new boundary inequality. The prior protocol remains `2026-10-11-execution-v2`; its required schemas are checked again by finalization. Threshold paper Section 8 Proposition 8.6 and Corollary 8.7 and the stage-1 quadratic Walsh proof are calibration/source inputs. All actual critical source hashes are pinned in `out/source_receipts.json`.

## complete derivation or exact first unsupported line

Full derivation: `POINT_FLIPPED_FIBERS.tex`.

Put r=rank M, D=n-r and k=rank of the polar form of q on ker M. On the zero fiber the unflipped quadratic has nonzero Fourier amplitudes alpha=2^(-k/2). Their sum is b(0)=1, so their positive and negative counts are N_plus=(2^k+2^(k/2))/2 and N_minus=(2^k-2^(k/2))/2. There are N_zero=2^D-2^k zero coefficients. Flipping the origin subtracts epsilon=2^(1-D) from every fiber coefficient. Thus the exact post-flip spectrum consists of the masses (alpha-epsilon)^2, (alpha+epsilon)^2, epsilon^2 with those three counts, zero masses omitted. Call its exact entropy E_(D,k). Only label zero changed, giving

H(F*)=2r+k+2^(-r)(E_(D,k)-k).

Physically, active address controls still have influence 1/2. On an inactive control i, the point flip toggles the two directed edge endpoints 0,e_i. Its influence changes by (1-2*l_i)2^(1-n). Adding this to the previous exact ledger gives the complete influence. Reachable data influence remains 2^(-r) per label, summing to one.

For even n, standard q=sum x_(2j-1)x_(2j), and prefix address rank r, set t=r mod 2, delta=2^(-n), D=n-r. Then k=D-t and

I(F*)=1+n/2+2(n-r)delta.

When u=2^(1-D+k/2)<=1/2,

H(F*)=n+r-t+4delta(1-2^(-t))(D+t-2)+(4-12*2^(-t))delta/ln2+R,

with |R|<=16*2^r*delta^2/ln2. The proof expands (1-z)^2 ln(1-z) using its convergent series and bounds the weighted remainder by u^4/6+(2/3)alpha*u^3. This is a proved error bound, not a floating fit. Hence at fixed r, along even n to infinity, H/I tends to 2. Even r has a small negative entropy correction; odd r has a positive order-n*delta leakage term from the unpaired fiber coordinate. The exact histogram applies to the small dimensions where that Taylor condition fails.

Root physical boundary charges C_i=2I(D_i) for the same prefix/matching family are explicit. Write L=n-r and tau_i=1 when an unaddressed control's partner is also unaddressed. Each addressed control has C_i=(n+1)/2+2L*delta. Each unaddressed control has C_i=(n+1)/2+2delta(n+1+2tau_i). For data y_z, C_(y_z)=2^(-r)(r+k+2w(z))+1_(z=0)*4L*delta, where w=0 for even r and otherwise is the last address bit. Their total is n+4L*delta. The sum over all physical coordinates is n(n+3)/2+2delta[L(n+r+3)+2k], whose ratio to I grows linearly with n. All controls carry large unlocalized boundary energy, and data coordinates carry an additional total of order n. This does not obstruct FEI; it obstructs blindly paying the entire boundary moment.

The stopping rule avoids that charge. Query all c controls with nonzero M columns; each pivot has influence 1/2. After the address is fixed, nonzero physical assignments exclude the flipped point and yield quadratic-sign leaves times one data sign. On the all-zero branch, choose a control whose remaining quadratic polar row is nonzero. Its influence is 1/2+2^(1-d)>=1/2, with d remaining controls. Its one-child is a quadratic terminal; its zero-child preserves the same structure. Stop when no quadratic interactions remain: that last leaf is a point defect times a fixed data sign.

Every internal node therefore obeys B_i<=1<=2Inf_i. Its exact bad-node gate B_i>2Inf_i never fires, so the localized boundary bill is zero. Each one-bit entropy drop is at most two bits, hence at most 4Inf_i. Quadratic sign leaves satisfy H<=2I by polar rank. For a point defect on d controls, p=2^(-d), H=-2(1-2p)^2 log2(1-2p)+8p(1-p)(d-1), I=2dp, and H<=4I: the first term is <=4p/ln2<8p; d=0,1 have zero entropy. Multiplication by the retained independent data sign adds one influence and no entropy. Exact restriction telescoping pays each pivot once and retains all terminal costs, proving H(F*)<=4(I(F*)-1). This constant is sharp on the q=0,M=0 point-defect subfamily as n grows.

For prefix/matching, with s=k/2 phase pivots, the exact spent influence is P=r/2+2^(-r)(1-2^(-s))+2s*delta. The final point-defect leaf has d=n-r-s controls and weight 2^(-(r+s)); its weighted phase influence is 2d*delta, and its full entropy is retained. Most initial order-n entropy lives in the other quadratic terminals. The small pivot budget is not claimed to pay those terminals for free.

First unsupported universal line: arbitrary Boolean phases need not admit such a high-influence pivot, nor a known globally paid boundary bill leading to certified leaves. The quadratic interaction graph and known flipped point provide it here. Multiple defects with incompatible phase gradients may remove that property. The M=0 arbitrary-phase case is still full FEI; no general entropy has been discarded.

## executed validation with domain, arithmetic, commands and outputs

Frozen pre-search specification: `out/FROZEN_SPEC.json`; exact case counts saved before execution in `out/case_plan.json`. Helper `code/check.py` v1.1 uses integer Walsh transforms of control-only signed indicators. Because every actual F* is linear in the distinct data signs, these compressed coefficients are its complete physical-cube spectrum; it never enumerates a fictitious independent spectral source or a 70-variable truth table.

Commands from A017:

`python -X utf8 runs\20261011T234546Z-account05-A017-recursive-addressing\code\check.py --pilot`

`python -X utf8 runs\20261011T234546Z-account05-A017-recursive-addressing\code\check.py`

`python -X utf8 runs\20261011T234546Z-account05-A017-recursive-addressing\code\derive_tables.py`

The first pilot caught an implementation error after four cases: fiber numerator amplitudes were incorrectly scaled by 2^r in the expected histogram. Only coefficient multiplicities should be repeated by 2^r. The repair, helper revision and unchanged domain are preserved in `out/PILOT_REPAIR.json`. The repaired pilot passed 182 root cases / 2,224 assertions in 0.098449 seconds.

Full run PASS: 13,545 root spectrum cases, 484 terminal-inclusive stopping trees, 261,626 exact assertions, 18.830825 seconds. Coverage: all n=1..3 quadratic phases and a<=2 matrices; all n=4 quadratic phases on eight specified maps; matching/path/star/complete zero-linear quadratic graphs and all coordinate projection subsets plus three oblique maps at n=4,5,6; fifteen matching/prefix boundary fixtures at n=2,4,6. n=5,6 is this finite family, not all quadratics or all Boolean functions. The analytic formulas quantify over all finite dimensions.

Every control influence and joint spectral incidence is independently compared with physical edges and four-corner derivative evaluations, averaged exactly over the named independent data signs. Erasure, entropy drops, terminal payments and entropy telescopes use exact rational linear forms in log2 primes. Log intervals use 32 atanh terms and a proved rational tail, with signed coefficient interval propagation. Physical influence and telescopes are exact Fractions. Decimal displays in validation.json are illustrative; rational endpoints and exact log forms are the certificates. The derived exact spent-influence and point-defect reserve formula matches twelve saved matching trees with sixty additional assertions; no new search was used.

Selected H intervals below are rounded outward from the rational certificates, with r=0:

| n | H(F*) in bits | I(F*) | Total root boundary charge |
|---|---|---|---|
| 2 | 0 exactly | 3 | 12 |
| 4 | [3.325375780, 3.325375781] | 7/2 | 37/2 |
| 6 | [5.822504850, 5.822504851] | 67/16 | 465/16 |

All prefix r values appear in `out/tables.json` with exact expressions and rounded rational enclosures. Root case digest: `31b12aed34036f88551648aac7e32ec499d4ef331419f11bd9eb703a250b9fe5`. The maximum tested tree has 63 internal nodes and 64 leaves. Validation output is 407,428 bytes; memory remained far below the 300 MB gate. No GPU, heavy job, automatic dimension increase or background process was used. These are author checks, not independent human acceptance.

## proof dependencies and changed downstream conclusions

The exact surgery lemma builds on the explicitly proved stage-1 quadratic Walsh/fiber identity; its source and claim version are pinned in CLAIMS.json. Elementary physical restriction entropy/influence identities are reconstructed in this report. The lead's boundary lemma is the motivation, not an unpaid dependency. No unreviewed broad B05/B06 endpoint or claim that a second-moment bill is linearly paid is used.

A018/A019/A020 and B06 can now test a concrete successful C019 certificate: unlocalized boundary energy diverges relative to I, but its exact bad-node subset is empty in a terminal-certified tree. A013/A030/A077 retain the address map reuse certificate while replacing the quadratic phase by a single controlled nonquadratic defect. Consumers must preserve the terminal point-defect and quadratic-core entropy. The zero-linear-at-the-flipped-origin condition is required for this tree; the exact entropy/influence histogram permits general linear terms but makes no identical tree claim for them.

## one next mathematical action and independent reviewer

Next: test two point flips with different quadratic phase gradients in the same address fiber. Derive which zero-path pivots fall below influence 1/2, compute the exact B_i gate there, and seek a labelled terminal/boundary reserve that survives both defects without repeated influence. This is the first obstruction to the successful pivot rule and directly tests the lead's universal stopping payment. A091 is the primary independent reviewer; A090 is alternate/second. Requested reconstruction: histogram multiplicities, root charge projection, Taylor remainder, and terminal-inclusive physical tree. No message or review acceptance is asserted.

## actual persistence receipts or precise save blocker

All files are inside A017: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, POINT_FLIPPED_FIBERS.tex, code and exact outputs. `out/persistence_receipts.json` pins saved files and rolling-file hashes; protocol fields and compatible progress copies are checked exactly. STATUS.md, WORKLOG.md and LEARNED.md are current. No shared tree, other agent folder, brain, repository or external application was modified. Supervisor transfer, mirror verification and independent adoption are pending; no local save blocker exists.

**Universal bridge**: This stage moves C019 stopping-tree payment from a reused-address quadratic ledger to a genuine single-point nonquadratic perturbation: the exact localized bill sum_(B_i>2Inf_i) w_v 2I(D_i) is zero, and the terminal-inclusive entropy is paid by 4(I-1), while blind root boundary charge/I grows as n. The universal missing line is a hereditary pivot/paid-boundary rule with certified terminal debt for arbitrary Boolean phases. NEXT tests two incompatible phase gradients, the first situation that can destroy the successful >=1/2 pivot and force a real localized boundary payment; that is a direct stress test of the universal bridge rather than another unperturbed addressing class.
