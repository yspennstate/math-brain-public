# A063: the information actually revealed by a second query

Run `20261014T052608Z-fleet05-A063-information-revelation`, stream B13. The all-even-k theorem is proved below and in DERIVATION.md; independent review is pending. Full FEI remains OPEN.

## exact target, quantifiers, hypotheses and units

For every actual finite uniform-cube Boolean function and fixed two-coordinate canonical restriction experiment, identify the query-order refund as the information about the second spectral bit actually revealed by the first physical outcome. For every even k>=4 in the actual B05 family (r=2k, delta=2^-k, d=2^-3k), bound this information in both selector/control orders. Information units are bits; actual kernel probabilities and Boolean amplitudes are rational; zero fibers are omitted. No abstract spectrum is substituted for a Boolean function.

The result is `R_i_then_j=I(S_j;X_i|S_remaining)` and, for the family, `0<R_yz,R_zy<=32d^2/(3 ln2)<16d^2`. Every nonempty residual packet has zero refund. The block ceiling `R_A<=(B_A-J_A)/2` is exactly accumulated per-step MU; the family-specific channel support bound is much sharper. Prior AND2 supplies the already exact positive-refund sharpness example requested by the lead.

## sources actually read, revisions and theorem locators

Read the complete execution protocol (revision 2026-10-11-execution-v2); the latest board is headed 2026-10-14 05:21 UTC. Read B13 lead v2 2026-10-11 23:1xZ, particularly its A063 target and established MU/JS bounds. Followed that direction; no disagreement. These instructions prohibit repeating the telescope, conservation or MU proof, so those are baseline inputs.

The original A063 run supplies the canonical common-lift review and exact refund interface: A037 v1 `aa45c0dacad4b1897e4c2f62511ccd331caf0eb6dc7ecc88cddf5189e8cf2cdb` and A063 v1 `8f757badc3354b59dc3949bdfdd953cda052cf5e508390c98c978234eb703844`. The B05 source report sections 2-4 supply the actual family and logarithmic selector bound, whose lower-bound proof is reconstructed in DERIVATION.md. Read the A064 original reserve report and A097 20261013T222610Z scoped shared-data transfer report to keep complete terminals and one influence owner explicit. Board developments from A037/A038/A039/A061/A062/A064/A087/A094/A097 select the next mixed-query target, without treating board summaries as reviewed theorems. Exact local source hashes and reading scopes are in out/SOURCE_RECEIPTS.json. Earlier protocol/campaign/paper readings are recorded in the original run; no new paper theorem or complete new paper audit is claimed here.

## complete derivation or exact first unsupported line

DERIVATION.md contains the full finite-to-infinite analytic proof. The existing identities give `B_A-J_A=2R_A+sum_h P(h)(B_h-J_h)`. For two queries the first kernel depends only on the second spectral bit and the untouched residual; the second outcome is conditionally independent of root labels given the first outcome and residual. The conditional mutual-information chain rule gives the two-query formula.

The actual family has six coefficient classes and only one exceptional (empty) residual packet. In all other packets the 2x2 amplitude matrix has identical columns: `[[C_T,C_T],[d,d]]`. Either order therefore reveals zero information about the remaining block spectral bit. The central matrix is `[[1+C,C],[d,d]]`, C=-p(1-s+delta). For both order channels its raw conditional Bernoulli variance is at most 2d^2, and its outcome mean lies in [1/4,3/4]. The elementary KL/chi-square inequality gives the stated upper bound; opposite row probabilities prove strict positivity.

The selector bound is `B_y>=(1-delta)(k-2)d`. Consequently `R_A/B_y<=16d/((1-delta)(k-2))` tends to zero. For even k>=6 the accumulated MU ceiling is at least (15/32)d. A universal price `B_y<=K*d+M*R_A` for fixed finite K,M>=0 is thus false on actual Boolean functions. The same conclusion does not rule out paying the two-query block from control influence (which is much larger), more queries, or existing stopping certificates.

No unsupported line occurs inside this narrow theorem. The first unsupported universal line is that, after an actual mixed data/controller history, a named unused inherited conditional child/control slack pays the signed nonmatching reference conversion together with both complete retained terminal laws at a dimension-independent influence price. Information refund by itself provides no such bank.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json, helper v2, even k=4,6,...,40, 19 parameters and 38 query orders, six proved multiplicity classes. Full actual truth-table/Walsh reconstruction is confined to k=4,r=8,n=13 (8,192 truth entries and all 8,192 coefficients). No dimension escalation, random search or floating sign decision occurred. Estimated memory 70 MB, below the 300 MB memok trigger; no heavy job was launched.

Command from this run directory: `python -X utf8 code/check_refund.py`. Result: PASS, 10,246 exact assertions, observed runtime 43.765 seconds (frozen pilot and maximum both 60 seconds). The independent physical edge count gives selector influence 1/4096 and control influence 13/4096. Conditional independence is checked by exact rational cross-products. Entropy and information signs use 64 rational atanh terms, dyadic logarithm reduction, explicit positive remainder, outward interval division, and outward endpoint rounding to denominator 2^384. Decimal display fields are never certificates. The checker retains all four normalized terminal spectral laws and their expected entropy rather than assigning zero terminal debt.

The failed v1 draft could not serialize an enormous exact Fraction endpoint at k=4; it established no accepted validation output. v2 repairs serialization by rigorous outward interval rounding while keeping the exact kernel and domain. out/PRIOR_FAILURE.json preserves this deviation. At k=4, display-only refund/d^2 values are approximately 2.89808 (selector first) and 2.01843 (control first); expected terminal entropy is approximately 0.112766 bits. Named finite cases verify the analytic theorem, not its all-k quantifier.

## proof dependencies and changed downstream conclusions

The acyclic proof uses the already reconstructed A037 lift and prior A063 fixed-block refund interface, plus elementary KL/chi-square and B13 baseline singleton MU. B05's selector lower-bound proof is reconstructed directly, so its legacy floating self-check is not imported as a certificate. One narrow extension is added; no new broad universal candidate is opened. Independent review remains separate from author validation.

A064/A097 should keep the complete terminal/core bill and control influence account: the rare selector's entropy is in nonempty packets that return exactly zero history refund in this small block. A037/A039 can use the first-outcome reduction to check actual-channel conversions at a mixed-history node, but it supplies neither a generic reference KL refund nor a renewed root bank. The exact amount moved is a quadratic information bound versus a logarithmic selector bill, not a universal FEI constant.

## one next mathematical action and independent reviewer

At one selected A038/A039 exposed priority query, write the inherited common-row signed reference channel and price its nonmatching conversion correction from a named unused conditional child/control slack once, retaining both terminal spectral laws. Use the two-query refund theorem as an information control; do not reset rarity or continue refund-only B05 searches.

Independent reviewers: A087 (conditional chain rule and actual common-row reconstruction) and A094 (six-class all-k bound and retained-terminal audit). Consumers A037/A039/A064/A097 should attach the same source hashes before downstream use. This is a handoff in local files; no messages or writes to other agents were sent.

## actual persistence receipts or precise save blocker

The four required protocol files, DERIVATION.md, scripts, frozen specification, first completed instance and complete certificate outputs are saved in this unique run. code/finalize.py checks exact required key sets, statement digest, matching progress/delta, seven report fields, file sizes and two-line rolling status, then writes out/PERSISTENCE.json with actual SHA256 receipts. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated locally. The productive unfinished draft from the earlier stage is continued here under the latest requested destination; historical drafts are retained unchanged. No repository/mirror copy, supervisor adoption, public release or independent review is claimed.

**Universal bridge:** This stage moves C019 stopping-tree payment and C024 history transfer by proving that an actual selector-plus-one-control history channel refunds at most 16d^2 while the rare selector erases at least (1-delta)(k-2)d; it also resolves the lead's block-versus-singleton question by exact algebraic equivalence. What remains is a source-owned signed conditional-reference reserve that transports unused child influence to erased/core entropy while retaining both full terminals. NEXT tests that missing conversion at the team's already exposed A038/A039 mixed query, which is the shortest continuation toward a universal bridge because another isolated refund search cannot produce the missing logarithmic payment.
