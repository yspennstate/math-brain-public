# A034 stage21: remove the unequal-mass loss

## exact target, quantifiers, hypotheses and units

For every integer s>=1 and every ternary row u on a finite uniform physical cube that is a signed sum of at most s disjoint affine-cell indicators with intrinsic quadratic phases, B(u)=sum_T uhat(T)^2 log2(1/uhat(T)^2) <= K_s E(u), where K_s=2s[log2(s)+(s-1)log2(64s^2)+3+log2(e)]. No bound on codimension, cell mass ratios, or spectral correlations is assumed. Thus any Boolean F(x,y) partitioned into at most M affine physical Y cells with a quadratic phase and an arbitrary CELL-DEPENDENT affine X-label map on each cell satisfies H(F)<=K_M I_Y(F) and H(S_Y|S_X)<=K_M I_Y(F), under every mixed physical restriction. The complete source class also has H(F)<=2^(M+1)I_Y and H(S_Y|S_X)<=2^M I_Y by the elementary bounded-phase/active-Y argument, so its better full rate is min(K_M,2^(M+1)). The optional integer X-degree bound d>=1 is retained when present. Fixed-M admission excludes fresh Boolean data tensor factors of F2 phase degree above M+1. Proper FOUR-cell rows have K_4=280+8log2(e)<292; complete four-phase-cell sources also have full rate32.

The row theorem has no affine-completion hypothesis. This stage strengthens the existing phase-row mechanism, rather than opening an unrelated broad candidate. The old balanced-four-cell coefficient below6.5 remains valid on its sharper domain; the new coefficient below292 covers arbitrary mass disparity. Full FEI is OPEN. Rung: author proof with exact finite certificates, external review pending; NOT Lean-checked.

## sources actually read, revisions and theorem locators

The complete EXECUTION_PROTOCOL.json v2, current BOARD B07/B18/B19/B20 entries, B07 STREAM_NOTES v2, own rolling files and stage20 REPORT/PROOF/code; canonical README/CURRENT_STATUS, claim/obstruction/packet/dispatch registries; supplemental CAMPAIGN, CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and source inventory; campaign plan opening and current owner control. Paper text searches were limited to baseline/affine/shared-data locators across all four text versions. Earlier stages supply the prior full-paper recovery; no unseen paper theorem is used here. Source receipts distinguish actual source files and targeted reads. The proof is self-contained. The brain query returned the existing nonBoolean-control and mass-weighted-entropy gap cards, not the new result. The wake reported stale personal-state/dream notes, which are not mathematical premises. The current direct stage invocation authorizes this continuation beyond the historical campaign endpoint; no schedule or endpoint was changed.

## complete derivation or exact first unsupported line

PROOF.md supplies the derivation. Nonzero derivative energy of a grouped ternary quadratic-cell row is at least half its smallest cell mass. Split sorted masses at ratio64s^2. Within-group mass ratio is at most(64s^2)^(s-1). Across groups, the first nonzero derivative has tail norm at most one quarter its own norm; the reverse triangle and exact tail-energy bound give E(u)>=1/2 sum_g E(v_g). This is a GROUP comparison: the false ungrouped comparison is explicitly rejected by a constant two-cell cover. Physical disjointness makes grouped Fourier laws have the same total norm; Cauchy--Schwarz, Gibbs and mixture entropy give B(u)<=q sum_g B(v_g), keeping BOTH normalized conditional entropy and row-mass entropy. The combined constant is K_s above.

For cell-dependent affine carriers every row has at most M affine intersections, even when ranks and fiber masses differ. Sum complete row bills and use exactly sum_J E(u_J)=I_Y(F). X restrictions project the individual maps and add affine phases; Y restrictions intersect cells and restrict quadratic phases. Every history retains the same M. Fixing all old variables forces any fresh Boolean data tensor factor to have phase degree<=M+1; AND_(M+2) is excluded. The three-bit point defect is admitted; normalized psi_N violates any fixed rate for large N and fails ternary/unit-phase admission. Physical input laws remain uniform product laws.

For COMPLETE sources there is also a simpler small-M bound, credited to the bounded-phase mechanism: global F2 phase degree<=M+1 makes every nonzero Y influence>=2^-M. If N Y coordinates are essential then N<=2^M I_Y; the X spectral marginal is the deterministic label law and has entropy<=N, while the conditional Y entropy is<=N. This gives full rate2^(M+1), or32 atM4. The proper-row rate below292 has weaker hypotheses; the polynomial K_M eventually improves the elementary exponential source bound. Both rates and their hypotheses are retained explicitly.

First unsupported universal line: an arbitrary Boolean core need not have bounded row piece count, and no original-influence-priced bounded-piece decomposition is proved. Taking singleton cells can have M=2^n. The theorem therefore supplies no dimension-independent universal FEI constant.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json, FROZEN_SYMBOLIC.json and FROZEN_CARRIER_SHORT_BOUND.json precede their respective searches. Commands are `python -B -X utf8 code/check.py MODE` for rows/scales/carrier/audit, `python -B -X utf8 code/symbolic.py` and `python -B -X utf8 code/carrier_short.py`. All arithmetic is integer/Fraction, including rational logarithm intervals from16 positive atanh terms with a geometric remainder. Entropy upper intervals are checked against LOWER bounds on the claimed constants; this is not a floating-point sign check. Single-group entropy equality is checked as vector identity. The analytic proof supplies the all-dimensional conclusion.

| Job | States/fixtures | Exact assertions | Seconds |
|---|---:|---:|---:|
| rows | 6654 | 46453 | 4.581 |
| scales | 8 | 121 | 0.567 |
| carrier | 729 | 11526 | 0.415 |
| audit | 0 | 418 | 0.002 |
| symbolic | 256 | 41474 | 1.675 |
| carrier_short | 729 | 2916 | 0.651 |

Total: 102,908 exact assertions PASS. The exhaustive row domain is nY0..3 with canonical singleton quadratic cells (6654 ternary rows including zero); it is not all higher-dimensional affine geometry. Eight dense unequal-scale two-cell fixtures use nY8..11. The actual Boolean differing-carrier fixture has nX2,nY4 and all729 physical mixed restrictions, independently checked through full-F integer Walsh coefficients and direct physical differences. The short-bound job checks the SAME729 restrictions for actual global ANF degree<=3, nonzero Y influence>=1/4 and full rate8. The symbolic36-coordinate certificate checks256 signed four-cell rows, with1/2/3/4 mass groups and maximum codimension34, by a second implementation using exact shifted physical intersections. It does not enumerate2^36 points. Runtime per job stays below55 seconds and memory estimate below40MB. No automatic dimension escalation, GPU, remote compute, detached job or large artifact was used.

Fresh memok returned physical free7.7GB and commit free10.4GB before the formal attempt. The subsequent Lean wrapper independently held admission with `SETUP_UNVERIFIED: Compute status is distressed or unknown`, exit2; no compiler certificate resulted. The proposed core theorem formalizes only integer-denominator rounding from9 first<=16 energy and32 summed<=33 first to summed<=2 energy; it does not formalize the Fourier/entropy theorem. Its source and held receipt are saved. No failed formal attempt is counted as mathematical validation.

## proof dependencies and changed downstream conclusions

No externally accepted theorem is assumed: the derivative gap, support isoperimetry, coherent entropy and full ledger are reconstructed. Stage20's explicit unequal-four-cell mass-disparity obstruction is now removed at fixed piece count. Its common-carrier restriction is replaced by arbitrary independent affine carriers on the phase cells; its sharper balanced/common-rank constants remain available. The next gap is growing piece count, not unbounded codimension or mass disparity at fixed count. This is one strengthening of the existing pending candidate, not an acceptance of earlier unreviewed versions.

## one next mathematical action and independent reviewer

A079/A033 should reconstruct the first-nonzero-group reverse triangle and the entropy domination argument without relying on the checker. A088/A094 should challenge physical-restriction closure, tensor guard, empty/constant rows and SAME-IY ownership. No peer has yet reviewed this version and no messages or external writes were sent. After reconstruction, remove piece-count dependence or prove an original-influence-priced bounded-piece decomposition for arbitrary Boolean cores; further balanced-only cases no longer address the frontier.

## actual persistence receipts or precise save blocker

The four protocol artifacts, complete proof, three frozen specifications, code and six PASS outputs are saved inside this run. PROGRESS/PACKET_DELTA match byte-for-byte, with packet_ids=[A034]. out/protocol_validation.json checks exact field sets; out/artifact_receipts.json records SHA256 and sizes. STATUS.md has exactly two lines; WORKLOG and LEARNED append this stage. All files are below20MB. Local persistence is verified; supervisor copying, GitHub/brain mirrors, independent acceptance and public release are not claimed. No brain store, shared tree or other agent folder was modified.

## Universal bridge

G-PHASE-COND advances from a mass-relative conditional estimate to a codimension-free COMPLETE row payment for every fixed number of disjoint quadratic affine pieces, including arbitrary unequal proper FOUR-cell fibers. It also gains a hereditary cell-dependent-affine-carrier class with unbounded labels and unrelated carrier ranks. The precise remaining universal cost is K_s=O(s^2 log s) as the piece count grows; no C018 erasure or C019 stopping bank is funded by merely restating this bound. NEXT targets piece-count-independent signed cancellation or an influence-priced bounded-piece decomposition because that is the remaining obstruction in the same full-entropy interface to arbitrary Boolean cores.
