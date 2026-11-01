# A022 stage 4: one-point switches with arbitrary overlapping controllers

## exact target, quantifiers, hypotheses and units

Uniform Boolean signs, entropy in bits. For every paired quadratic bent sign
b on even k>=4, every vertex v, and every indicator A on any number of
independent uniform controller bits, F=b(1-2*1_(x=v)*A). No balance,
point-block width, overlap or contrast restriction on A. Establish exact
spectral logarithmic terms and one-use data access/terminal ownership.
New scoped target is proved: I_ctrl=2^-k I(1-2A) and
H(F)<=7I_data+2^-k H(1-2A). The arbitrary controller terminal is explicitly
inherited. TWO_VERTEX_PROOF.md also proves H<=9I_data+delta[H(1-2A)+H(1-2B)]
for two distinct vertices and arbitrary dependent controllers, k>=6.
Full FEI and universal stopping payment remain OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json read in full (2026-10-11-execution-v2); BOARD.md
snapshot 2026-10-14 01:41 UTC, B05 STREAM_NOTES v2 and own STATUS were
read at entry. Own prior v2 CLAIMS and PROOF.md provide the earlier paired
policy and complete scalar JS proof. A023 run 20261013T223305Z REPORT.md
was read for its single consumed separator reserve and terminal scope.
A021 run 20261014T011316Z REPORT.md, CLAIMS.json and DERIVATION.md §§1-2
and the start of §3 were read for bounded-contrast closure and the remaining
large-contrast cost. REVIEW_A021.md independently accepts only the upper
price/K6/K7 subclaims; its lower supremum and three-event application are
not accepted as a whole bundle. Source inventory hashes are locally saved.
No new paper, percolation or brain premise; old four-order census and A021's
bounded-contrast controller grid were not repeated.

## complete derivation or exact first unsupported line

PROOF.md §§1-4 is the complete scoped proof. It gives the actual signed root
coefficients bhat(S)1_(T=empty)-2delta b(v)chi_S(v)Ahat(T). All nonempty
controller rows are flat across data labels and contribute exactly
delta[H(1-2A)-phi((1-2alpha)^2)]+8delta alpha(1-alpha)k.
The controller-empty row has the two exact bent alignment masses. These
root formulas also hold for every bent sign, while the access proof uses
explicit quadratic pairing.

Query only the first bit in each pair, then STOP. Reference derivative is
1/2; a surviving point perturbation changes it by at most
2alpha*2^(-(k-q)), so d>=1/2-2^(-k/2)>=1/4 without any fair inactive branch.
Thus every access node is K4-good. One exceptional fiber retains q=1-2*point*A
up to a character. Equation(3) gives its full entropy, including empty rows.
Its alpha-log-alpha and data-spreading terms are bounded by7 times raw
partner influence; the character can only increase that data influence.
No controller influence pays this local term. The exceptional leaf's reach
and its spectral inheritance weight are BOTH tau=2^(-k/2), so the final
controller entropy bill is delta H(1-2A), not tau H(1-2A).

Exactly I_data=I_access+I_terminal,data and I_ctrl=delta I(1-2A) is entirely
terminal. JS is bounded by2d/ln2 using the explicit prior scalar proof.
Since 4+2/ln2<7, telescope gives the displayed one-use bound. If the
controller sign satisfies H<=C I, the full root bound is max(7,C)I.
This is a conditional inheritance statement, not an arbitrary-controller
certificate or a zero-credit completion to constant leaves.

TWO_VERTEX_PROOF.md closes the first unequal-reference collision: exact signed
interference and the adjacent -4delta b(v)b(w)E(AB) data-edge correction
are retained. The common exceptional leaf has actual post-cancellation
data influence >=2tau(m-1)(EA+EB), and its complete entropy is at most
tau[H(1-2A)+H(1-2B)]+9I_leaf,data. Every controller bill inherits once.

First unsupported universal line: arbitrary controller entropy is paid
without a terminal certificate, or growing numbers of edited vertices
admit a uniform terminal data-reserve bound without a support-size guard.
No such implication is made. The one-point large-contrast log is now paid
by a named actual data reserve, not by renewing whole child influence.

## executed validation with domain, arithmetic, commands and outputs

Specs were frozen before each search: FROZEN_SPEC.json,
RECONSTRUCTION_SPEC.json, WITNESS_SPEC.json and TWO_VERTEX_SPEC.json. Main pilot: k=4 all16
vertices, every controller on t=0,1,2 (22 tables):352 roots. Full: every
controller on t=0..3 (278 tables), k=4 all16 vertices, k=6 vertices
0,1,21,63 and k=8 vertices0,1,85,255:6672 labelled roots. No symmetry
quotient. Main maximum dimension is11. Seven separate witnesses include
controller-first point switches k=4,6,8 and two explicit OR/XOR three-event
overlapping four-bit controllers on k=4,8, maximum dimension12.

Executed commands from own A022 folder, each using python -X utf8:

- code/check.py pilot: 15,629 checks,
  1.037647s, PASS.
- code/check.py full: 432,778 checks,
  819.029970s, PASS. Exact root/leaf entropy formulas,
  influence partition and terminal-inclusive inequality all checked.
- code/edge_reconstruct.py: 6672 roots, 44480 physical
  fibers, 53,376 checks, 154.684884s, PASS.
  Uses direct natural-coordinate Boolean edge counts and no Walsh/log kernel.
- code/witness.py:7 cases, 482 checks,
  0.243350s, PASS. The k=8 controller-first root is
  rigorously K4-bad, while the paired data-access policy is good. Both
  OR/XOR overlap replays retain their full weighted controller entropy.
- code/two_vertex.py:8 frozen cases, 734 checks,
  0.871483s, PASS. Same-fiber adjacent versus distinct-fiber
  edits at k=6,8 with overlapping four-bit OR/XOR/literal controllers;
  exact signed cross-spectrum, E(AB) cancellation and full terminal bill.

Total 502,999 executed checks. Integer signed Walsh, Fraction influences,
exact rational prime-log expressions, outward80-bit log intervals from a
positive50-term atanh series with proved remainder. Root and leaf identities
are symbolic equality, not numerical closeness. Full records and prime-log
receipts are saved in out/. Only runtime clocks use floating point.
Memory estimates180 MB main/60 MB edge/70 MB witnesses/100 MB two-vertex; below300 MB trigger.
Peak memory is not claimed measured. Pilot/witness limits60s and full/edge
limits1800s were respected; jobs sequential, no GPU/background job or
automatic dimension escalation. Second implementation is author verification,
not an independent human acceptance.

## proof dependencies and changed downstream conclusions

Existing A022-ODDFACE-SURGERY-GAP-LEDGER advances v2 to v3, preserving inherited
scope and adding the one-/two-point controller theorems. It opens no new broad
universal candidate. C005 scalar proof is source-complete in prior PROOF §3;
the new signed spectra, mutation bound and terminal payment are rederived.
A021-POINT-SWITCH-RELATIVE-BIAS-PRICE v1 receives local partial review only
for its upper price and constant consequences; source statement/hash unchanged,
no repair contribution and no acceptance of its entire bundled theorem.
A025's inherited v1 constant-child review remains restricted to that subclaim.
All new A022 conclusions await independent review.

Downstream change: A021/A025 need not price every controller-first large-
contrast query for a single quadratic-bent point edit. Data-first paired
access is uniformly K4-good, regardless of controller overlap or width;
its exact terminal data bank pays the logarithmic spreading, and arbitrary
controller entropy is carried at its actual delta weight. A023's consumed
separator reserve is not renewed. A064's unfinished-core/controller question
now has a source-complete one-point data-first comparison. No shared registry
or other agent's folder was edited; no message was sent.

## one next mathematical action and independent reviewer

Extend the exact signed exceptional-fiber spectrum to growing edit sets; determine a data-dimension/support-size guard under which one actual terminal data bank pays all collisions at an absolute rate, retaining every controller entropy. A087 primary, A094 alternate review.
Review must check both factors of tau, the raw/character-shifted influence
comparison, adjacent E(AB) cancellation and the distinction between all-bent
root identities and paired quadratic access. This targets growing signed
collision ownership, not another exhaustive small controller census.

## actual persistence receipts or precise save blocker

All required protocol files, PROOF.md, TWO_VERTEX_PROOF.md, REVIEW_A021.md, code and exact outputs
saved locally in this run. STATUS has two lines, WORKLOG appended and LEARNED
updated. out/ARTIFACT_RECEIPTS.json records bytes/SHA256; finalize.py checks
field sets, compatibility equality, canonical statement hashes and20 MB cap.
No save blocker; supervisor copies, canonical adoption, independent acceptance,
remote mirrors and downstream use remain unverified.

Universal bridge: This stage moves C019/B05 localized odd-face payment at
the large-contrast one-point interface. It removes inactive-branch fairness
from paired access, gives zero K4 access credit for arbitrary overlapping
controllers, and pays the exact leaf spreading terms from terminal data
influence while retaining delta H(controller) intact. The first unequal-
reference collision is also paid at coefficient9, including actual adjacent
edge cancellation. Arbitrary controller FEI and growing edit sets remain
unpaid. NEXT determines the support-size guard for one data bank across
many such collisions, the shortest route toward universal ownership because
it tests reserve scaling rather than enlarging a paid controller grid.
