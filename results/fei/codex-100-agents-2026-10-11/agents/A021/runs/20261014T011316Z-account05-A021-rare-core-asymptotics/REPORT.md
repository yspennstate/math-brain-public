# A021 stage 4: optimal logarithmic contrast price and small-disagreement closure

## exact target, quantifiers, hypotheses and units

Advance the existing C019 ownership target by consuming A023's one-bit
reserve and A025's multi-bit failure. For arbitrary Boolean branches G,H
on one uniform data cube, fresh independent point controls of any width,
gamma=P(G!=H)>0 and eta=P(G=-1), determine the worst erasure/influence
price in terms of contrast eta/gamma, uniformly as selector rarity and
gamma vanish. Entropy is in bits, influence is physical, and reach
weights are ordinary uniform probabilities. Then apply the criterion to
the multi-bit three-event controller, retaining arbitrary terminal cores.

## sources actually read, revisions and theorem locators

- BOARD.md, supervisor snapshot 2026-10-14 01:10 UTC, especially B05,
  A023 one-use reserve, A025 repeated-price failure, and A027 signed
  transport. Read B05 STREAM_NOTES.md v2 and own STATUS.md at entry.
- EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2: field contract,
  scoped review, frozen computation, preservation and completion rules.
- A023 run 20261013T223305Z-account05-A023-amortized-rarity-budget:
  SEPARATOR_RESERVE_PROOF.md, REVIEW_A021_WITNESS.md, CLAIMS.json;
  single-separator addition to A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER v2.
  Its review accepts only our prior witness and balanced control B,d
  transfer, not the whole A021 stage-3 bundle. That scope is preserved.
- A025 run 20261014T002956Z-account05-A025-rare-event-counterfamily:
  REPORT.md and PROOF.md sections 1–3: exact point-switch sector masses,
  moderate-disagreement criterion, repeated full-face counterfamily, and
  the unpaid small-disagreement regime. The failed repeated-price
  mechanism is consumed, not reproved as this stage's result.
- Own completed stage-3 mechanism and earlier bent-flip constants are
  background only: the new theorem and Boolean lower family are derived
  self-contained in DERIVATION.md. No new paper or brain premise is used.

Exact source paths and saved-byte hashes are in out/source_inventory.json.

## complete derivation or exact first unsupported line

DERIVATION.md proves, for every live point-selector query with underlying
branches G,H and c=1/ln2,

    B_i/d <= max{4,c+log2(8 eta/gamma+4)}+2c/sqrt(e).

The proof separates the full constant core Fourier row, bounds its cost
uniformly, and controls nonconstant packet mass by 8eta+4rho^2 gamma.
The remaining-selector nonempty sector is exact, not a marginal entropy
proxy. It follows that eta<=gamma/5 gives strict 6-goodness and eta<=gamma
gives strict 7-goodness at EVERY layer, with no lower bound on gamma.

Define P(theta) as the supremum of B_i/d over actual Boolean branch pairs
in every dimension and all point-control widths with eta/gamma<=theta.
For every real theta>=8,

    log2(theta)-3 <= P(theta) <= log2(theta)+307/45.

Thus P(theta)/log2(theta) tends to one. The lower bound uses actual balanced
bent/one-vertex-flip branches: eta=1/2, gamma=2^-m, B/d>=m-2. This
extracts the necessary leading logarithm for any scalar contrast-only
price; a global potential avoiding that price needs an explicitly owned
rebate. Rarity width itself does not add a logarithm to this interface.

For S,W,U,V independent positive point blocks of ANY positive widths and
ANY independent Boolean core g, set A=WUV+S(U OR V-WUV), F=1+A(g-1).
Expose S, then the surviving conjunction or union. The separator's ratio
eta/gamma is <=1/5; the success-branch union ratio is <=1. Therefore this
actual stopping prefix has EXACTLY ZERO strictly 7-bad control charge,
uniformly even for highly biased cores and vanishing branch disagreement.
With pi=EA and a_g=1-Eg, its exclusive accounts are

    I_ctrl=a_g J(A), E I_terminal=pi I(g), E H_terminal=pi H(g),
    H(F)<=(7+2/ln2)a_g J(A)+pi H(g).

The sharper constants give a prefix rate <10. If H(g)<=C0 I(g), the
completed bound is H(F)<=max(10,C0)I(F). The arbitrary-core terminal
ratio is explicitly inherited, not proved or discarded. The earlier
balanced one-bit theorem is independently accepted at the entropy/face
scope stated in REVIEW_A023.md; no substantive repair was supplied.

First unsupported universal line: choose an actual policy for every
Boolean f whose large-contrast switches and complete terminal entropy
are paid from one nonreused physical influence reserve. No universal
bounded-contrast representation is shown. Arbitrary-width small-gamma
threshold-4 payment also remains open; the new closure uses threshold 7.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications were saved before each job. Commands from A021:

    python -X utf8 runs/20261014T011316Z-account05-A021-rare-core-asymptotics/code/check.py
    python -X utf8 runs/20261014T011316Z-account05-A021-rare-core-asymptotics/code/overlap.py
    python -X utf8 runs/20261014T011316Z-account05-A021-rare-core-asymptotics/code/save_metadata.py

First pilot PASS in 1.8691 seconds: all 256 ordered two-bit Boolean branch
pairs at widths 1..6, totaling 1,536 exact actual-node spectral
reconstructions. This includes 90 strict K6 and 882 strict K7 sign
certificates, plus 96 irrelevant queries; the remaining pairs impose
neither bounded-contrast hypothesis. Nine compressed bent cases m=4..20
certify the lower bound. Separately generated direct truth tables/edge
counts reconstruct 54 A023 one-use reserve cases, without importing its
helper or output. The all-dimensional proofs do not extrapolate from them.

Second pilot PASS: 96 separator K6 cases and 48 declared success-branch
K7 entries (24 distinct local states, two explicitly redundant R labels),
using core minority 1, 1/2, 1/16 and 2^-32. Minimum branch disagreement
is 13/137438953472. Sixteen compressed controller spectra are reproduced
by full actual Walsh transforms. The first pass took 0.4274 seconds;
after clarifying that a redundant R label is not physical total U width,
the unchanged domain was rerun and passed in 0.4818 seconds.

All decisions use Fraction, integer Walsh and normalized positive
sixteen-term atanh log series with proved tails rounded OUTWARD to
128-bit dyadics. No floating-point sign or extrapolation is a certificate.
Only runtime clocks use floating point. Frozen memory estimates were
70 and 100 MB, both under the memok threshold; no heavy job, dimension
escalation, GPU or continuing background process was used.

## proof dependencies and changed downstream conclusions

The new criterion, contrast asymptotics and arbitrary-core application
are self-contained proofs. Source ideas are credited to A025's exact
selector-sector split and A023's overlap family; their full-price failure
and single-bit theorem remain intact. Standard Parseval, binary entropy
log-sum, the physical influence telescope and JS<=2d/ln2 are the elementary
interfaces used, with the latter's scalar proof supplied below.

For clarity, JS<=2d/ln2 follows from
[(1+x)ln(1+x)+(1-x)ln(1-x)]/2<=1-sqrt(1-x^2) on [-1,1].
The derivative comparison is artanh(x)<=x/sqrt(1-x^2), proved by
differentiating on [0,1) and using equality at zero. Apply to each pair
of squared child coefficients, then use (|u|-|v|)^2<=(u-v)^2 and
sum(u-v)^2=4d. Thus no unpaid JS premise is hidden in the terminal ledger.

The small-gamma obstruction is resolved for bounded inactive-branch
contrast at threshold 7. It is NOT resolved for arbitrary branch pairs
or relabeled threshold 4. A023 v2 receives a scoped independent entropy/
face review in a local copy; its earlier unbalanced-core two-event claim,
full retained-KL computation and arbitrary nested reservations are not
accepted by this review. Source files and shared registries are untouched.

## one next mathematical action and independent reviewer

At a selected large-contrast switch, name a signed terminal/core reserve
that pays the unavoidable logarithmic excess once, and carry the same
underlying gamma through all remaining point controls. Test against the
balanced bent-flip lower family and A025's repeated-price failure before
claiming a universal history rule. A023 and A025 should independently
reconstruct the constant-row split, optimal log coefficient and arbitrary
core transfer; A087 should review the proof chain and local review scope.
This is a saved source-bound handoff, not a sent message.

## actual persistence receipts or precise save blocker

The four required protocol files, DERIVATION.md, REVIEW_A023.md, scripts,
frozen specs and exact outputs are saved in this run. code/save_metadata.py
checks protocol keys, canonical statement hashes, output counts, review
source hash and the final bridge paragraph; out/artifact_receipt.json
records local artifact hashes and file sizes. STATUS.md has two lines;
WORKLOG.md and LEARNED.md are updated only within A021. Independent
acceptance of the new theorem, canonical adoption, remote mirrors and
downstream mathematical use are not asserted.

## Universal bridge

This stage moves C019 stopping-tree payment and its C024 history interface
by determining the optimal logarithmic contrast price uniformly in rarity,
then eliminating repeated face reservations for bounded-contrast point
switches. It closes the entire multi-bit three-event family at threshold
7 with arbitrary terminal core bias and full terminal entropy retained.
What remains is a single owned rebate for large contrast and all terminal
cores under a universal physical policy. NEXT targets that exact excess
using the proved sharp lower family, rather than enlarging a paid class:
it addresses the necessary missing global payment directly.
