# A067 — local Boolean granularity instead of dimension-level counting

## exact target, quantifiers, hypotheses and units

Packet A067, stream B14, run 20261011T220539Z-fleet05-A067-hypercontractive-refinement. The target is a Boolean-specific improvement of a logarithmic entropy-conversion loss. For every finite uniform-cube Boolean sign f, let q_S=hat f(S)^2 and define d_f(S)=max_{T containing S, q_T>0}|T| on nonzero nonempty coefficients. Put U(f)=sum_nonempty q_S(d_f(S)-|S|). We prove

    H(f)<=2I(f)+2U(f)-(2-log2(e))Var(f).

Thus the measurable regime U<=KI, for a fixed finite K, satisfies FEI with constant 2+2K independently of dimension. The support condition d_f(S)<=L|S| is a sufficient, entropy-free structural test giving constant 2L. A balanced support antichain has H<=2I-2. The global degree-granularity special case and the antichain corollary are not asserted to be new in the literature. Entropy is in bits throughout this new theorem. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the complete execution protocol, revision 2026-10-11-execution-v2, and the board snapshot written 2026-10-11 22:05 UTC. B14 STREAM_NOTES.md was absent at the supplied path; no direction was inferred from its absence. Read campaign README/CURRENT_STATUS and claim/obstruction navigation, the A067 assignment and B14 next-action contract, the campaign plan's targets and source guards, and the supplement's CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING. Earlier B05/B09/B19 reports were inspected as scope controls, not used as theorem premises. Large combined tool outputs were truncated; source reads below identify the mathematical portions actually used rather than asserting a full end-to-end audit of all background.

The threshold 38-page and earlier 29-page texts were inspected at their introductions and hypercontractive rare-gate argument. The relevant current locator is Section 5.1, Lemma 5.3, Eq. (29), around text lines 831-852. The 30-page and alternative 31-page percolation texts were inspected at the theorem introductions and Section 3 local-guard/pivotal arguments; their geometric hypotheses were not imported into a general-cube theorem. The text files required cp1252 decoding; an initial utf-8 read failed and was corrected.

The source-bound restriction interface was read in sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md, Sections 1-3, and ERASURE_REDUCTION.md. ROUTE_MAP_CURATED.md warns about unpaid source/history-transfer and quantization costs; those are not silently paid here. The supplement's SEED_LEMMAS.md Section 3 supplies the fixed-Renyi point-defect control, which is reproduced in the derivation.

Primary online checks: [Han, arXiv:2312.08271v2, 10 December 2025](https://arxiv.org/html/2312.08271v2), Section 3, Eqs. (3.13)-(3.15) and Remark 3.2, identifies an influence-only moment extremum that leaves a logarithmic rarity cost. [Hypercontractivity via the Entropy Method](https://zesty2.cs.uchicago.edu/articles/v009a029/) gives the general norm context. The recent plateaued-function paper abstract was inspected as a priority guard; none of its results is a dependency. No novelty assertion is made. SOURCE_MANIFEST.json records local source hashes and absent inputs.

## complete derivation or exact first unsupported line

DERIVATION.md is the complete proof and scope analysis; BOOLEAN_HYPERCONTRACTIVE_REFINEMENT.tex is the packet's requested mathematical deliverable, and REGIME_COMPARISON.md gives the old/new comparison.

The exact general level-count step H(P_k)<=log2 binom(n,k)<=k log2(en/k) introduces a dimension logarithm. Hypercontractivity controls noise-weighted level mass but does not supply an upper bound on within-level entropy without additional structure. Our replacement uses Boolean vertex quantization: 2^(|S|-1)D_S f is integer-valued and has degree d_f(S)-|S|, giving hat f(S) in 2^(1-d_f(S)) Z. Its coefficient surprisal is therefore at most 2(d_f(S)-1). Summing and paying the empty atom proves the displayed estimate.

The point defect has U<=I and gives H<=4I-(2-log2(e))Var, while the generic marginal estimate loses a ratio of order n. Level counting is tight on that family; an initial contrary comparison was corrected before finalization. The strict level-count improvement uses the existing addressing baseline: U=a/2 and I=1+a/2 give the exact bound H<=2a, versus a generic full-cube level-count bound Theta(a^2). This does not reopen or claim the addressing theorem as new. The actual point-defect H/I->4 and fixed-order Renyi failures are recovered calibration facts. The real singleton spectrum, and even an L2-small real perturbation of a constant sign, fail the new bound when Boolean quantization is removed.

Two actual-Boolean obstructions identify the limit of this mechanism. A one-point flip of a dictator has I->1 but U~n. A single optimized character anchor repairs that example, but it still fails on Maj_3 tensor a point defect: every character-anchored arithmetic envelope is >=3n/2, whereas I<=5/2 and H=2+o(1). These refute helper payments, not FEI. The proof handles every anchor, including anchors with zero coefficient, and retains the whole tensor factor.

The first unsupported universal line is the existence of a tail-stable arithmetic charge or fully paid partition with cost O(I) for every Boolean source. A universal bound on U or on the optimized single-anchor envelope is now refuted, rather than left as a hopeful gap. Physical restrictions are Boolean, but the U regime has not been proved hereditary.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: FROZEN_SPEC.json, written before any search. Standard-library Python, integer Walsh transforms and Fraction identities, no randomness or symmetry reduction, memory estimate below 50 MB. No job expected above 300 MB and no GPU or background/window process was used.

Executed commands from the A067 folder:

    python -X utf8 runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement/code/check.py pilot
    python -X utf8 runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement/code/check.py n4
    python -X utf8 runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement/code/check.py families

The pilot exhausts all 278 tables in dimensions 0-3, with independent direct character sums; 5,624 exact assertions passed in 0.0088 seconds. The separate fixed n=4 job exhausts all 65,536 tables; 1,776,588 exact assertions passed in 19.994 seconds. These check Parseval, local coefficient divisibility, influence against physical edges, and exact U accounting. The direct family command exceeded its frozen 60-second limit; its per-dimension guard was inadequate and the exception is preserved in out/DIRECT_FAMILY_LIMIT.md. No result from that failed job is counted. The separately frozen factorized replacement verifies 22 point-defect/surgery cases, seven tensor sources and all 4,064 character anchors; 45,356 exact assertions passed in 0.4993 seconds. It uses independent full superset transforms for all anchors at n=2,3,4 and four selected anchors at n=5,6,7,8. Its command is python -X utf8 runs/20261011T220539Z-fleet05-A067-hypercontractive-refinement/code/check_families_factorized.py, with output out/check_families_factorized.json. The addressing comparison is also checked in its explicitly frozen bounded domain. Entropy inequalities rest on the analytic proof, not floating logarithms; integer arithmetic certifies the finite ingredients.

## proof dependencies and changed downstream conclusions

The new local-granularity proof uses only elementary integer finite differences, Fourier orthogonality, and -x ln x<=1-x, all reconstructed in DERIVATION.md. It does not assume A066's integrated FEI target, the threshold theorem, a percolation transfer, or any unreviewed B09 lemma. The C019 stopping-tree interface is conditional: if node drops cost at most a times queried influence and leaves satisfy E U<=b E I, then H(root)<=max(a,2+2b)I(root). Both hypotheses remain unpaid universally.

B14 already had two source-complete pending claims from A066. Before registering the present claim, A067 independently reconstructed A066's exact heat identity and no-integrable-envelope obstruction, using a different dimension selection and direct binomial-polynomial integration. REVIEW_A066.md records ACCEPT_AT_STATED_SCOPE, including the almost-everywhere quantifier and units. This is a source-bound independent-agent review, without any repair or coauthorship. B20 adoption is pending; no other agent's file or shared registry was changed. This review reduces the local pending-candidate queue; A067's own theorem and helper obstruction require A088/A094 review.

Downstream: A070 can stop pursuing maximal-support-degree envelopes, including a single optimized character anchor. A088/A094 can review the mixed-derivative granularity proof and the all-anchor tensor obstruction. B06/B13 may use the explicitly scoped terminal bound in C019; they must pay the full access tree and leaf U. B20 receives the reviewed A066 dependency and the new source-bound result by supervisor copying, not an external message.

## one next mathematical action and independent reviewer

Next: replace maximal support degree by a tail-stable charge on a heavy Fourier coefficient, beginning with Maj_3 tensor point defect, while retaining the cost of any partition/anchor selection. This is a mechanism change prompted by exact obstructions, not another search for a universal U bound. Independent reviewers: A088 primary; A094 alternate/second. The completed A066 review can be consumed by A070/B20 immediately at its stated scope.

## actual persistence receipts or precise save blocker

All required files, deliverables, scripts and exact outputs are saved only under the supplied A067 run directory. STATUS.md, WORKLOG.md and LEARNED.md are current in A067. out/ARTIFACT_RECEIPTS.json records byte sizes and SHA256 checks of saved artifacts after generation; code/finalize.py checks the protocol's exact claim/progress field sets. No shared index write, git, brain mutation, mail, public release or cross-agent write occurred. Supervisor copying, GitHub/mirror ingestion and independent review of the new claim are pending, not inferred from local persistence. No file exceeds 20 MB.

**Universal bridge:** This stage moves C019 stopping-tree payment by supplying an explicit Boolean arithmetic terminal certificate H<=2I+2U-(2-log2(e))Var and closing its U<=KI regime, while rigorously excluding raw and single-anchor maximal-support costs as universal payments. It also independently verifies A066's analytic obstruction. The remaining bridge is a nonreusing access-tree/partition cost plus a tail-stable terminal charge; no access theorem is supplied. The stated NEXT attacks exactly the fragility exposed by tiny high-degree tails and arbitrary tensor factors, so it tests a necessary universal mechanism rather than adding another isolated family bound.
