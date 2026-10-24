# A079 stage4: sharp arbitrary-ratio conditional payment

## exact target, quantifiers, hypotheses and units

Every actual Boolean F on exactly two uniform address bits and any number of
uniform data bits is admitted if every nonzero conditional Fourier row has a
coordinate-product spectrum with at most one nonfair varying frequency
coordinate, with arbitrary nonfair marginal and all other coordinates fair. Fixed frequency characters
are allowed. Fourier signs are ARBITRARY. Entropy is in bits and influence is
physical mean Fourier degree. Proved sharp conditional rate
Kcond=3/2+(5/2)h2(1/10), and general joint rate Kall=6+2log2(65/64).
If all nonfair primitive magnitude ratios are2,3,4, the sharper joint rate is
Kjoint=10-3log2(3). Neither joint rate is claimed sharp.
The exact conditional equality case is the three-bit point defect with two
address bits and one data bit. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read complete BOARD snapshot2026-10-14 02:53UTC, with the initially truncated
middle recovered in separate B07-B18 reads; B16 STREAM_NOTES.md v2 dated
2026-10-11 23:25Z; own STATUS and prior DERIVATION. Reuse the execution protocol
revision2026-10-11-execution-v2 already read in full in the preceding stage.
Read A032 stage4 REPORT/CLAIMS/QUADRATIC_OBSTRUCTION and phase_anf output/helper
(run20261014T015128Z); read A034 stage4 REPORT/CLAIMS
(run20261014T025347Z). These force the actual cubic row and leave unequal inverse
support payment open. Physical quadratic phases and Fourier-sign quadratic
phases are distinct hypotheses.

Read A068 stage4 REPORT in full (run20261014T023317Z), especially Section5:
it independently reconstructs our prior sharp same-cube quadratic collision,
pins the original statement/proof hashes and supplies no substantive repair.
The new run copies that claim with only this review record appended. Registry
adoption is not verified. Sources and SHA256s are in out/SOURCE_MANIFEST.json;
A032's actual witness source is additionally pinned separately. No new paper,
literature priority assertion, brain query/write or external message is used.

The unchanged lead target of distinct bent branches was closed as hardness
transport earlier. This run consumes new A032/A034 dependencies and develops
the precise forced cubic collision rather than repeating flat-padding tests.

## complete derivation or exact first unsupported line

DERIVATION.md gives the full proof. The inverse quadratic branch laws have flat
affine physical supports with integer height constraints. Disjoint supports
force amplitudes1 or2; proper intersections force both amplitudes1; equal
supports permit only the ratio-three nonfair case. A4:1 row requires at least
three fair frequency coordinates. For the forbidden smaller dimensions every
sign branch is automatically quadratic, so this exclusion holds for arbitrary
Fourier signs. Integer Walsh divisibility gives universal weight caps5/8 or17/32.

For EVERY two-address Boolean function, without product/phase assumptions,
H(w)<=E H_1/2(p)+2I_X. Fourier inversion pays each row's address mass; mixed-only
rows all have weight delta/4 and their extra cost is paid once by I_X>=delta.
This retains both H(w) and the complete H(S_Y|S_X). Under the fixed-ratio
admission, the regular rows pay the joint and conditional bills from physical
row influence. The ratio-three zero-fair-coordinate endpoint uses the actual
common mixed half cube and weights(5,1,1,1)/8; it gives the sharp conditional
rate, with all terminal entropy retained.

The included A032 cubic witness has row ratios4,3,3,2 and passes the new theorem.
The detailed affine-support classification remains quadratic-branch scoped.
The main conditional theorem has no phase-degree or ratio restriction: the
Gibbs/KL bound pays every regular one-nonfair row at5/2, and integer height
leaves only ratio3 for the zero-fair-coordinate endpoint. Odd norm divisibility
forces all its other address rows to be fair. A second Gibbs bound yields
Kall for full joint entropy, with address entropy retained.
First unsupported extension: a nonproduct/multiple-nonfair complete-core
reference transfer after actual data exposure, retaining the signed gap and
both terminal bills. Direct universal Renyi/I payment is already a known failed
route and is not proposed. More address bits, multiple nonfair coordinates per row, unrestricted
tensors and recursive collision closure are not established.

## executed validation with domain, arithmetic, commands and outputs

The frozen pilot command `python -X utf8 code\check.py --pilot` passed670
cases and 5531 assertions in 1.083s. The full command
`python -X utf8 code\check.py` passed 90540 cases and 1318988 assertions
in 505.704s, under its600-second cap.

Full domain: all65,536 actual Boolean truth tables with two address and two
data bits, without symmetry reduction; all24,990 ratio2,3,4 quadratic branch
pair cases on m=0,1,2,3 modulo simultaneous sign, with heavy half oriented zero;
12 frozen higher-rank/translation endpoints on m=4,5,7; A032's actual64-sign
witness; and the sharp conditional three-bit witness. No automatic dimension
growth occurred. Row-pair admissions/scalings are additional checked objects,
not extra Boolean-function counts. Every whole Boolean function in the n4
domain with at most one nonfair marginal has at most one other varying
frequency bit, hence affine branch signs and only ratio2 or3. The complete
n4 sweep therefore checks the full arbitrary-ratio/arbitrary-phase theorem
there;10,560 functions are admitted. The larger fixtures test its
quadratic-branch subclass; the analytic low-dimension exclusion supplies the
all-phase/all-dimensional bridge.

The original full helper stopped at its600-second guard during the Boolean
sweep, with no completed full receipt or inequality failure. It is preserved
in out/FAILED_FULL_V1.json. Revised v2 rounds the rational log enclosures outward
to denominator2^96 after retaining their proved tails; this controls repeated
denominator growth without weakening certificate validity. Its frozen specs
precede the successful revised pilot and full run.

Arithmetic: integer FWHT, gcd, Fraction, exact prime-log identities, rational
atanh enclosures with proved120-term tails and outward dyadic rounding. Validation checks the normalized
full/conditional entropy chain, physical influence, common mixed mask, exact
per-row uncertainty bounds, both entropy inequalities, affine support/amplitude
forms and weight bounds, and sharp conditional equality. No floating acceptance
test or independent-review claim is made for author code. Estimated memory was
below100MB, so no300MB memok-triggering job was started; one full job ran at a
time. out/validation.json and frozen specs preserve counts and arithmetic.


The general extension command `python -X utf8 code\general_certificates.py`
passed 2580 exact assertions in 0.048s: all25 height-two
one-bit pairs,647 coprime magnitude pairs among1024 screened pairs,640
symbolic m/q residual cases and five integer comparisons. The continuum
Gibbs/KL proof is analytic; these finite examples are not its substitute.
The only nonfair one-bit ratio is3:1, and121<128 certifies the exact square-root
comparison used to bound every other row at rate5/2. Its frozen spec and receipt
are saved separately.

## proof dependencies and changed downstream conclusions

The new theorem and universal row ledger are self-contained. A032 supplies an
actual witness and the question, not an unreviewed proof premise; A034's signed
odd-mask lemma is not assumed. A068's review of our prior claim is consumed
without modifying its statement or contributors. No original restricted claim
is refuted or superseded. This closes the unequal-support cubic fixed-ratio
case in every dimension, even beyond quadratic branch phases, and preserves
the actual conditional entropy rather than a proxy Q alone. It does not close
the universal weighted nonfair-row target or full FEI. All single-nonfair
coordinate odds are closed, not just the three named magnitude ratios.

## one next mathematical action and independent reviewer

Derive a conditional complete-core reference transfer for one actual nonproduct or multiple-nonfair-coordinate row after data exposure. Retain the signed address gap H(w)-E H_1/2(p), both terminal spectra and one unused physical reserve; do not replace the gap by a universal Renyi/I bound.
Independent reconstruction requested through this artifact: A088/A094 or A092,
especially the mixed-only address payment and exceptional ratio-three ownership.
A032/A034/A068 are immediate mathematical consumers. This is a handoff artifact,
not a sent message or claim of their downstream use.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json,
DERIVATION.md, frozen specs, code and exact out receipts are saved inside the
assigned run. STATUS has two lines; WORKLOG and LEARNED are appended.
out/PERSISTENCE_RECEIPT.json pins readback schemas, hashes and sizes. Local
persistence is verified; independent review, supervisor copying, registry
adoption and mirrors remain unverified. No save blocker exists.

**Universal bridge:** This stage moves the B16 G-PHASE-COND target toward C018
by proving a sharp all-dimensional conditional payment for product rows with
at most one nonfair coordinate, arbitrary marginal and arbitrary compatible
phase, including the forced cubic unequal-support row; it pays retained joint
entropy at Kall, sharpened to Kjoint for ratios2,3,4.
The universal two-address row ledger identifies the exact signed address gap
for further transfer, rather than discarding terminal entropy. The remaining
bridge is a nonproduct/multiple-coordinate conditional reference transfer after
data exposure with one physical reserve. NEXT is the shortest route toward
full FEI because it attacks the first operation that leaves this newly closed
admission, while arbitrary seed padding and direct Renyi payment are already
known to retain or misprice the universal obstruction.
