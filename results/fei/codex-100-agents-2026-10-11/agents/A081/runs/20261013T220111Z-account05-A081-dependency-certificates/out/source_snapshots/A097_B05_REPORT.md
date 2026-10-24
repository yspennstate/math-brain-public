# A097 stage 2: B05 leaf references inserted into the compatible telescope

## exact target, quantifiers, hypotheses and units

Execute B20 STREAM_NOTES v2's A097 target: compute the exact control-first tree residual sum_h pi_h(B_h-kappa_h)/I_removed on the actual B05 activated bent-defect family for k=2,4,6,8. The B_h here is the queried coordinate's conditional spectral entropy at its actual restriction node; it is not the aggregate C018 B(f). All information uses bits and ordinary uniform physical influence.

For even k>=2 let delta=2^-k, e=2^(-k/2), r=2k and p=2^-r. The actual quadratic bent seed is b(x)=(-1)^(x1x2+...+x_(k-1)x_k), its one-point flip is b'=b-2*1_zero, h is their fair physical-selector splice, and F=1+A_r(h-1). All functions take values +-1. The physical tree queries the fresh point controls in their fixed order, stops inactive at the first mismatch, and otherwise queries the selector and stops at b or b'. The original B05 local no-go used even k>=4; k=2 is a legitimate additional Boolean calibration member.

Two prescribed complete reference modes are compared. E assigns the actual squared Fourier law to each seed leaf. U assigns the same uniform bent-spectrum reference Q(T)=delta to both seed leaves. All constant leaves use delta_empty. References include the empty atom and are fixed before the spectral sample; no interior reoptimization occurs. The A097 v1 compatible lift determines every interior and root law.

This stage supplies exact finite expressions with outward rational certificates, an all-even-k posterior-credit cap, an all-even-k control-first erasure bound B_tree<=3 I_removed, and the complete root-reference consequence CE<= (3+2/ln2) I. The family already has FEI certificates from A023/A064, so this is a reference-transfer/application certificate and mechanism diagnosis, not a new FEI class or universal constant. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md: supervisor snapshot 2026-10-12 00:49 UTC. B20 STREAM_NOTES.md v2, 2026-10-11 23:39Z, and SYNTHESIS.md were read; their precise A097 target is followed. Own STATUS/LEARNED and the prior A097 result were used. EXECUTION_PROTOCOL.json was reread in full, revision 2026-10-11-execution-v2. Original campaign status/registries/plan and supplemental sources/paper scope were read in stage 1; this stage does not repeat unrelated baseline work.

Source originals consumed for this application:

- B20 run 20261011T225100Z-claude-B20-erasure-activation-transfer: REPORT section 2, exact activation formula (A), and CLAIMS.json, B20-ACTIVATION-ERASURE-FORMULA v1. Its actual control-coordinate formula is inserted explicitly below. It is author-proved, not silently treated as independently accepted.
- A097 run 20261011T221240Z-account05-A097-cross-route-transfer: REPORT/DERIVATION in CROSS_ROUTE_SUBSTITUTION.tex, A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER v1. The reference telescope and terminal-credit cap are the precise reusable interface; A098 reconstructed the KL subclaim locally, while full independent review remains pending.
- Accepted archived B05/B19 local-no-go originals from stage 1, source commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b and independent review 7955d427222392911dc6af2e4ee3aa8aab67ac8c: actual bent point surgery, signs, no-go scope. Their local-refund failure is not re-proved.
- A023 run 20261011T221608Z-account05-A023-amortized-rarity-budget REPORT sections 2-6, and A064 run 20261011T224431Z-account05-A064-global-debt-potential REPORT, especially arbitrary-core reserve and both query orders. These already pay the family's entropy; their payment theorem is not claimed again as novelty.
- A012 run 20261011T234525Z-account05-A012-sparse-activation-accounting REPORT: direct balanced activation reference, exact core cost and posterior redundancy. Its balanced hypothesis does not apply to the nonbalanced core h here; no balanced activation formula is substituted without its mean correction.

Sources are pinned by observed local SHA256 in out/SOURCE_RECEIPTS.json. A navigation attempt guessed a nonexistent A098 run timestamp; it supplied no mathematical premise and changed no source. No online literature priority claim or full independent paper audit is made.

## complete derivation or exact first unsupported line

DERIVATION.md contains the full proof. CROSS_ROUTE_SUBSTITUTION.tex contains the corresponding theorem and formulas. The essential exact substitution follows.

There are N_+=(2^k+2^(k/2))/2 positive and N_-=(2^k-2^(k/2))/2 negative bent Walsh coefficients sigma e. The flip subtracts 2delta from all coefficients. At a data index of sign sigma the core selector coefficients are sigma e-delta and delta; its marginal is q_sigma=delta-2sigma delta e+2delta^2. The core mean is mu=e-delta and the activation coefficient is c=1-mu in [3/4,1).

The selector erasure is B_sel=sum_sigma N_sigma phi((sigma e-delta)^2,delta^2). Let H_b' be the exact entropy of masses (sigma e-2delta)^2 with these multiplicities. The selector's channel information is J_sel=H(q)-[k+H_b']/2. Under reference E, kappa_sel=0 and Q_h(empty)=mu^2. Under reference U, the two leaf references are identical, their reference physical posterior is fair, and kappa_sel=J_sel exactly; Q_h(empty)=delta mu^2/q_+.

At an active node with s controls remaining, u_s=2^-s, physical reach pi_s=p/u_s and d_s=u_s c. B20's activation coefficient formula gives the actual empty residual packet masses (1-d_s)^2,d_s^2, with q_s=1-2d_s+2d_s^2. Its control-coordinate conditional entropy is

    B_s=phi((1-d_s)^2,d_s^2)+(1-q_s).

This is precisely the y-coordinate summand of B20 (A): u(1-mu^2)+(u-2u^2)c^2+phi, using 1-mu^2+c^2=2c. Thus its measure, bias, normalizers and bit units match the target telescope. It is not an analogy to a balanced core.

Writing z_(s-1) for the active-child reference's empty mass, A097 v1 determines

    z_s=((1-d_s)^2/q_s)(1+z_(s-1))/2,
    w_s=(d_s^2/q_s)(1+z_(s-1))/2,
    kappa_s=q_s D_2((1,(1-2d_s)^2)/(2q_s) || (1,z_(s-1))/(1+z_(s-1))).

Only the empty residual packet contributes this posterior KL. Every nonempty packet has true and reference physical posteriors concentrated on the active child. All reference laws remain normalized and positive on true support.

The exact requested ratio is therefore

    R_k = [B_sel-kappa_sel + sum_(s=1)^(2k) (B_s-kappa_s)/u_s]
          / [2k c+delta].

These rational/logarithmic expressions constitute the exact values. The following decimals summarize certified rational intervals; they are not floating-point proof premises.

| k | B_tree/I_removed (also R_k under E) | K_tree/I_removed under U | R_k under U |
|---|---:|---:|---:|
| 2 | 2.529559232017 | 0.177128026958 | 2.352431205059 |
| 4 | 2.348254434608 | 0.027709745516 | 2.320544689093 |
| 6 | 2.222200785224 | 0.004241766778 | 2.217959018446 |
| 8 | 2.160400273400 | 0.000749758065 | 2.159650515335 |

out/RESULTS.json retains exact rational lower/upper endpoints, every node's charge/reference empty mass, terminal KL, root CE and full entropy/influence ratios. The correct influence accounts are

    I_removed=p(2k c+delta),
    I_terminal=p(k/2+kdelta),
    I(F)=I_removed+I_terminal.

The complete telescope keeps p times the actual average leaf entropy under E and p*k under U. Under U the terminal KL slack is p[k-H_b']/2. The independent closed root reference, grouped by deepest included control frequency, verifies its mass is exactly one and K_tree=p[k-H_b']/2-D_root. The direct integer-Walsh check compares every root reference atom at k=2,4 with that compressed formula. Interval overlap is merely an implementation check: the exact equality follows from the stated rational law and A097's proved chain rule.

The mechanism has a quantitative limit. The point-flipped bent spectral law satisfies chi-square(P_b'||uniform)=16delta(1-delta), exactly. Since ln t<=t-1 and the A097 posterior correction cannot exceed terminal reference slack,

    0<=K_tree/I_removed
      <=8delta(1-delta)/[(2k c+delta)ln2] = O(2^-k/k).

Thus these inexpensive seed references provide exponentially negligible credit. Increasing artificial terminal slack is not a free repair: it raises the terminal reference bill.

For all even k>=2 the erasure rate is uniformly paid on this fixed tree. Indeed phi(a,b)<=b log2(e_math/b) when a+b<=1, so

    B_tree/p <=4k c+C0+delta[k+log2(e_math)],
    C0=log2(e_math)+4+2log2(4/3)<13/2.

For k>=6, 2k c>=3k/2>=9 and delta(k+3/2)<=15/128, yielding B_tree/I_removed<3. The certified k=2,4 intervals supply the remaining cases. A lower bound B_tree/p>=4k c-2 proves B_tree/I_removed tends to 2, and the credit cap proves R_k under U also tends to 2. Each prescribed seed reference costs at most 2I(seed), so the actual complete root reference obeys

    CE(P_F,Q_F)<=(3+2/ln2)I_removed+2I_terminal
              <=(3+2/ln2)I(F).

This is the closed scoped C019 application. The first unsupported universal line is unchanged: arbitrary Boolean seed references and colliding histories must admit a dimension-independent payment of sum pi(B-kappa) together with their entire terminal costs. There is no such proof here. Further samples of this already bounded-ratio family would calibrate the same mechanism, not test full FEI.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before computation: helper A097-bent-reference-v2, k=2,4,6,8, two reference modes, eight cases, exact sign-count/deepest-control grouping, memory estimate 80 MB, 60-second runtime cap. The k=2 pilot executes two cases and independently reconstructs its seven-bit Boolean function. It passed 802 exact assertions in 0.024 helper seconds; out/PILOT.json retains the result.

Commands from A097:

    python -X utf8 runs\20261012T005449Z-account05-A097-cross-route-transfer\code\check_bent.py --pilot
    python -X utf8 runs\20261012T005449Z-account05-A097-cross-route-transfer\code\check_bent.py

The final full pass reports 50,162 exact assertions, zero failures, eight reference cases, helper runtime 1.286 seconds. Integer FWHT verifies the actual bent/point-flipped coefficients and every compatible reference atom independently at k=2,4; the largest reconstructed actual cube has 13 bits (8,192 root atoms). The k=6,8 cases use proved exact multiplicities, not a floating approximation or large truth-table relaxation. Complete root CE, entropy, terminal and physical influence accounts are checked as well as B-kappa. An initial full pass was followed by one added complete-CE check and rerun; counts are not summed across repeats.

All probabilities and reference recurrences use Fraction arithmetic. Logarithms are certified with dyadic range reduction into [1,2), 32 positive atanh terms and geometric remainder 2*z^65/[65(1-z^2)], exact rational division by the ln2 interval, and outward rounding to denominator 2^80. Signed multiplication swaps interval endpoints when necessary. The saved rational endpoints are the certificates; Decimal values are display only. No random search, GPU, dimension escalation, background task or job exceeding 300 MB was started. The all-even-k conclusions rely on the proof plus the two exact finite base-case certificates, not extrapolation of four ratios.

## proof dependencies and changed downstream conclusions

One scoped application certificate is attached to the existing A097 transfer mechanism, not a third broad B20 candidate. Dependencies: A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER v1 (its author proof and A098's locally reconstructed KL subclaim), B20-ACTIVATION-ERASURE-FORMULA v1 (reconstructed in this specific substitution), exact Boolean bent/point-flip algebra and the elementary chi-square/KL inequality. No unproved FEI endpoint is assumed.

A099/A100 can now replace the formerly unevaluated B05 erasure-minus-credit leaf with an explicit finite certificate and all-even-k payment for this canonical tree and fixed references. A039/A064 receive the exact reference recurrence and the exponentially small credit cap: better posterior credit cannot be presumed to pay a new seed's conditional labels. A023/A064 already cover entropy of this family; the new conclusion is compatibility-specific and does not supersede their broader arbitrary-bias/both-order work. Source statement hashes and acceptance scopes are recorded in CLAIMS/PROGRESS. No shared index or another agent's report was changed, and no downstream adoption is claimed.

## one next mathematical action and independent reviewer

Next: transport one fixed terminal-core reference through two overlapping point-control events, assigning each physical coordinate one influence account, and calculate the compatibility correction before attempting its influence payment. Coordinate with A039/A064's existing overlapping-control ownership target through this saved handoff: A097 owns the complete-reference correction, not another entropy proof for disjoint activations. This tests the first unresolved cross-route transfer beyond the now closed B05 calibration. Independent reviewers: A090 and A094. No external messages were sent.

## actual persistence receipts or precise save blocker

Saved in this run: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, DERIVATION.md, CROSS_ROUTE_SUBSTITUTION.tex, TRANSFER_HYPOTHESIS_CHECK.json, FROZEN_SPEC.json, code/check_bent.py and out/PILOT.json/out/RESULTS.json, with source and persistence receipts. STATUS is two lines; WORKLOG is dated and appended; LEARNED preserves the stage-1 theorem and adds this application's exact formulas and limitations. The finalizer checks required protocol field sets, statement hashes, delta equality and file sizes. All writes stay inside A097; no git, Brain write, other-agent modification or trading-tree access. Local persistence is verified; independent review, supervisor copy and mirror verification remain pending.

Universal bridge: This stage closes the B20-requested B05 application of C019/C024 by substituting the actual biased activation fibers and complete bent/defect leaf laws into the A097 reference telescope, certifying the exact four residual rates and proving B_tree<=3I_removed for all even k on this control-first family. It also quantifies the posterior credit's limit: O(2^-k/k) of removed influence, with both corrected and uncorrected erasure rates tending to 2. No universal FEI constant changes and arbitrary terminal seed costs/nonempty conditional labels remain open. NEXT addresses the complete-reference correction for overlapping control histories under one exclusive coordinate budget, because disjoint activation entropy is already paid and another isolated class calculation would leave the first nonadditive compatibility obstruction untouched.
