# A022 stage 5: growing edit sets and one terminal data bank

## exact target, quantifiers, hypotheses and units

Uniform Boolean signs, entropy in bits. For every paired quadratic bent sign
on k=2m>=4, q distinct data vertices, and arbitrary indicators A_j on the
same controller cube independent of the data, controllers may overlap or
depend arbitrarily. Write delta=2^-k, a_j=1-2A_j and
F=b[1-2 sum_j point_(v_j) A_j]. Proved under q^2<=2^(m-2):

    H(F)<=8 I_data(F)+delta sum_j H(a_j),
    I_ctrl(F)=delta sum_j I(a_j).

The more general q<=2^(m-2) bound has coefficient K(m,q) explicitly given
in PROOF.md (2). Constants/characters recursively composed by the absolute
guard obey H<=8I at all finite depths, with shared controller bits allowed.
This closes the guarded growing-edit mechanism, not full FEI.

## sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 read in full; entry BOARD snapshot
2026-10-14 04:29 UTC read with targeted B05/B06 and relevant agent followups
(the large full-board output was truncated, so no all-agent audit is claimed).
B05 STREAM_NOTES v2 and own STATUS read at entry. Prior A022 v3 proof and
TWO_VERTEX_PROOF supplied the two-point frontier, and stage3 PROOF section3
supplies the complete scalar JS bound. A028 run 20261014T022306Z REPORT read
for selector overhead/unguarded terminal reserve; A023 run 20261014T022245Z
REPORT read for whole-block geometric payment and its one terminal bank.
Neither report is a theorem premise here. No new web, paper or brain premise.
The all-controller finite census was not repeated.

## complete derivation or exact first unsupported line

PROOF.md contains the complete general proof. Its (4) gives the actual signed
root coefficients, retaining all cross terms before squaring; (5) retains
the adjacent -4delta b(v_j)b(v_l)E(A_j A_l) edge correction. These root
identities hold for all bent references. The access theorem uses quadratic
pairs: query the first bit of each pair, then STOP. Perturbation union mass
gives d>=1/2-q*2^-m>=1/4, so all access is K4-good.

Each reached terminal is a character times a controlled defect set on m
partner bits. Equation(7) is its exact entropy decomposition: joint-empty,
controller-empty/partner-nonempty, and all nonempty controller rows, with
the actual conditional squared signed laws. No row is erased. Entropy is
bounded by tau sum H(a_j)+tau s(8m+4log2(e)+8log2(e)/e), tau=2^-m,
s=sum EA_j. At each controller input the actual negative set has r<=q
points, so edge isoperimetry gives actual data I>=2tau s(m-log2 q).
Under the guard, character multiplication only increases this influence.
The stronger q^2 guard makes the resulting ratio less than8.

Physical terminal reach tau multiplies the spectral inheritance weight tau,
giving delta for each controller exactly once. Influence partition and
the scalar JS<=2d/ln2 telescope finish the theorem. Induction gives the
recursive closure without any rate increase at greater depth. Controllers
sharing bits is allowed because their actual controller edges occur in
disjoint data fibers.

There is no unsupported line within the scoped statements. The first
unsupported universal line is admission of arbitrary Boolean functions to
this guarded recursive grammar, or a substitute paid reserve for dense edit
fibers. At q near2^m the isoperimetric slack degenerates, the common character
may reduce influence, and the access perturbation estimate may fail.
Arbitrary controller entropy remains explicitly inherited outside the grammar.

## executed validation with domain, arithmetic, commands and outputs

Specs frozen before each job: out/FROZEN_SPEC.json and out/EDGE_SPEC.json.
Pilot6 fixtures: k8/q2 adjacent, split-fiber, all-zero and all-one controller
profiles; k12/q3 and q4 shared-fiber profiles. Full12 adds k12/q4 partner
square with all-one/common-AND/all-zero controllers, k16/q8 partner cubes
with all-one/cycling profiles, and a split-first-fiber cube with cycling
profiles. All controllers use two bits: literals, XOR, AND or constants.
Maximum dimension18; no symmetry quotient or automatic escalation.

Executed from the A022 workspace using python -X utf8:

- code/check.py pilot: 6 roots, 40,019 checks,
  1.315625s, PASS (60s cap).
- code/check.py full: 12 roots, 891,095 checks,
  1140 access nodes and 1152 terminal leaves,
  58.736523s, PASS (1800s cap).
- code/edge.py: 12 roots, 60 aggregate equalities,
  3.781380s, PASS. Independently reconstructs actual
  Boolean signs in natural coordinates and directly counts every coordinate
  edge; no Walsh/logarithm helper is imported.

Total 931,174 checks, including the repeated pilot. Full signed integer
Walsh coefficients are checked frequency by frequency against the exact
multi-edit formula. Influences are rational; entropy equalities use rational
prime-log forms, inequalities use outward80-bit atanh intervals with proved
50-term remainder. Every leaf's raw/character entropy, influence comparison,
empty mass and row marginals are checked. All actual access B<=4d and JS
inequalities, full entropy telescope and physical influence partition pass.
Multiplicities compress entropy sums without changing arithmetic. Exact
case expressions and prime-log interval receipts are in out/. Only runtime
clocks use floating point. Memory estimates180MB/60MB were below the300MB
trigger; peak memory was not measured. Jobs ran sequentially and stayed
within frozen limits. This is author verification, not independent acceptance.

## proof dependencies and changed downstream conclusions

Existing A022-ODDFACE-SURGERY-GAP-LEDGER advances v3 to v4. The prior scoped
claims and the A025 v1 partial review retain their original limits; no new
broad universal candidate is opened. The inherited A021 partial review is
preserved without claiming new review or acceptance of its bundled statement.
New dependence is the explicit scalar JS proof; terminal entropy, signed
interference, actual boundary payment and growth guard are derived here.
No FEI assumption is needed except when admitting externally certified
controller signs; within the recursive grammar that certification is induction.

B05/A023/A028 now have one terminal bank for growing numbers of unequal
controllers, retaining every delta H(a_j), rather than only two-point payment
or renewal of a shared reserve. General bent references have exact root
formulas but do not acquire a paired access policy from this result.
No shared registry was edited or message sent. Independent review is pending.

## one next mathematical action and independent reviewer

Replace the worst-case log(q) leaf loss by the actual conditional negative-set boundary/entropy profile; identify a paid dense-fiber condition that survives common-character cancellation while inheriting all controller entropies. A087 primary, A094 alternate independent reviewer.
Review the phi(M) bound, actual post-cancellation isoperimetry, common-character
influence comparison, both tau factors, and recursive sharing of controller
bits. These are the places where an apparently universal version could lose
its reserve; additional small controller tables would not resolve that gap.

## actual persistence receipts or precise save blocker

Required four protocol files, PROOF.md, scripts and exact outputs saved in
this run. STATUS is two lines; WORKLOG and LEARNED updated. Local receipt
out/ARTIFACT_RECEIPTS.json records byte counts and SHA256, exact field sets,
canonical statement hashes and compatibility equality. No file exceeds20MB.
No save blocker. Supervisor copying, canonical adoption, remote mirrors and
independent acceptance remain unverified.

Universal bridge: This stage moves C019/B05 localized stopping payment from
two edits to arbitrary growing edit counts under q^2<=2^(k/2-2), with one
actual post-cancellation terminal data bank, zero K4 access credit and every
controller entropy inherited once. It also closes a depth-independent H<=8I
recursive grammar. Dense edit fibers and universal admission remain open.
NEXT targets the exact conditional negative-set boundary where this bank
fails, the shortest route toward full FEI because it tests extension of the
payment mechanism beyond the support guard rather than another isolated
finite class or a wider controller census.
