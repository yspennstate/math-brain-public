# A084 stage 2: complete analytic AND sign map

## exact target, quantifiers, hypotheses and units

For every independent Bernoulli input pair (p,q) in (0,1)^2, consider the genuine Boolean gate g(X,Y)=(-1)^(XY), the normalized product Fourier basis, and actual physical block A={X}. Classify F(p,q)=J_A-M_A, where J_A is physical-child/remaining-spectral-label mutual information and M_A is conditional spectral-label entropy. Units are bits. At the four outer edges, statements refer to the continuous extension. B17 lead v2 explicitly directed completion of the 902-box gap or a proof of the zero-curve count.

**Result:** the entire interior sign map is proved analytically at author level. Its zero set is given by explicit lines plus unique scalar roots, with all root counts, signs, and tangencies determined. Independent review remains pending. Full FEI remains open. The old 902 boxes need no further subdivision: a box may contain a true zero curve, and the proof classifies each point within it rather than asserting that the entire box has one strict sign.

## sources actually read, revisions and theorem locators

At stage start read BOARD.md snapshot 2026-10-12 04:39 UTC, B17 STREAM_NOTES.md v2 dated 2026-10-11 23:40 UTC, STATUS.md and LEARNED.md. Re-read the complete EXECUTION_PROTOCOL.json (2026-10-11-execution-v2) and stage-1 code/certify.py; the stage-1 derivation of four masses is reconstructed independently in PROOF.md's amplitude proof. Stage-1 REPORT.md boundary reductions and the source manifests remain provenance. The board's updated C018 scalar closure, K5 census, B09 accepted biased core, and B16 retained-KL findings were used to avoid duplicating closed work. No new claim here requires those external theorems. Current input SHA256 pins are in out/SOURCE_RECEIPTS.json. Local elementary calculus and entropy chain rules supply the proof; no external priority assertion is made.

## complete derivation or exact first unsupported line

The complete derivation is in PROOF.md. It is source-complete and does not rely on the grid or on the universal B09 uncertainty theorem. Its decisive reduction is

    theta=arcsin(sqrt(p)),
    alpha=atan(sqrt(p/(1-p))(1-2q)),
    psi(x)=h(sin^2 x), w=1-4pq(1-q)>0,
    F(p,q)=w[psi(theta)-psi(alpha)-psi(theta-alpha)].

This follows from the actual conditional physical and spectral laws in the remaining-label-zero sector. The label-one contribution cancels exactly. On (0,pi/2), differentiation and y=cot(2x) give

    (ln 2)psi''''(x)=16[2+y^2-y asinh(y)/sqrt(1+y^2)]>=32.

The elementary bound |asinh(y)|<=|y| proves the sign. For G_s(x)=psi(x)+psi(s-x)-psi(s), its derivative is strictly concave on (0,s/2), since G_s'''=psi'''(x)-psi'''(s-x)<0. This limits G_s to a single valley on that half-interval. A unique transition s_* is determined by 2psi(s_*/2)=psi(s_*); existence and uniqueness follow by convexity of psi before its inflection tau and strict convexity of K(s)=2psi(s/2)-psi(s) for s>=tau. Put p_*=sin^2(s_*).

For s<s_*, G_s<0 throughout the interior. At s=s_* its only interior zero is the midpoint tangency. For s_*<s<pi/4 it has exactly two simple reflected roots a(s),s-a(s), with a(s) uniquely defined in (0,s/2); G_s is positive between them and negative outside. For s>=pi/4 it is strictly positive throughout the interior. Reflections of psi convert every original bias pair to exactly one of these cases, including the region beyond its cancellation zero.

The exact full map in PROOF.md can be summarized as follows. The line q=1/2 is always zero. For p>1/2 there is the additional exact hyperbola q=1/(2p). Below q=1/2: p<p_* is entirely positive; p=p_* has one additional zero at q=1/[2(1+sqrt(1-p))]; p_*<p<1/2 has a negative interval between two positive intervals; p>=1/2 is entirely negative. Above q=1/2: p<=1/2 is entirely negative. For p>1/2 the region beyond q=1/(2p) is entirely negative; within the wedge (1/2,1/(2p)), apply the same scalar classification with effective bias 1-p. Thus p>1-p_* gives an entirely positive wedge; at p=1-p_* its midpoint zero is q=1/(2sqrt(p)); for 1/2<p<1-p_* there is a negative interval between two positive intervals.

The distinct interior q-root count, for each fixed p, is:

| Bias p | Number of q zeros |
|---|---:|
| (0,p_*) | 1 |
| p_* | 2 |
| (p_*,1/2) | 3 |
| 1/2 | 1 |
| (1/2,1-p_*) | 4 |
| 1-p_* | 3 |
| (1-p_*,1) | 2 |

The extra root branches are smooth on their open p ranges by the implicit function theorem; their definition as unique scalar roots is exact. No closed elementary formula for a(s) is assumed. Outer-edge identities are F(0,q)=F(1,q)=F(p,0)=0 and F(p,1)=-h(4p(1-p)). These, and the full interior classification, also cover arbitrary joint corner approaches; pointwise asymptotics are no longer being used as a substitute for a continuum theorem.

As a downstream consequence, both physical singleton restrictions have J_A>M_A throughout the real square 0<p,q<p_* (apply the map twice after exchanging the inputs). Hence even existential singleton selection cannot universally restore a tax-free biased restriction helper.

**First unsupported line at this target:** none identified in the derivation; independent review is required and has not occurred. The next universal unsupported line is a nonreusing influence/deficit payment for the necessary biased correction and conditional spectral entropy in a physical stopping tree. This stage does not supply that line.

## executed validation with domain, arithmetic, commands and outputs

The frozen spec FROZEN_SPEC.json precedes execution. Run from the agent folder:

    python -X utf8 runs/20261012T044029Z-fleet05-A084-continuum-parameters/code/check_signmap.py

The exact checker uses Fraction arithmetic, 24 terms of the atanh logarithm series with an explicit geometric-tail bound, outward 80-bit endpoint rounding, four-corner interval division, and rational square-root enclosures obtained using integer isqrt. Binary entropy intervals use concavity. It certifies the unique transition in the rational bracket

    7634531/20971520 < p_* < 152690623/419430400

with the exact bracket recorded in out/THRESHOLD_CERTIFICATE.json; displayed decimals are approximately 0.3640428066253662 and 0.3640428137779236. The checker performs 25 certified bisections to width below 10^-8 and stops.

It also validates 961 dyadic interior bias pairs (p,q=j/32, 1<=j<=31), checking exact four-atom F intervals against the separate conditional-sector expression. At the 31 q=1/2 points the exact zero identity is checked; all other point intervals have strict signs matching the separate angular reconstruction. Six rational hyperbola fixtures verify u=1-p and v=1 algebraically, and their F intervals contain zero. Total: 2,901 checks passed; observed Python checker runtime 0.7234 seconds. Numerical angles and sample root locations are evidence only, stored separately from the Fraction decisions; the continuum coverage and root counts are proved in PROOF.md. Outputs are saved immediately in out/THRESHOLD_CERTIFICATE.json, GRID_CHECKS.json, HYPERBOLA_ZERO_FIXTURES.json, ZERO_COUNT_EXAMPLES.json and RESULT.json. Estimated memory <80 MB; no job requiring the >300 MB memok gate was started; no GPU or dimension escalation.

A separate symbolic reconstruction (`python -X utf8 code/check_derivatives.py` from the run directory) verified all four derivative identities and the fourth derivative again in y=cot(2x) coordinates, with five exactly zero residuals in SymPy 1.14.0 (0.4982 seconds). For the fourth trig expression, a routine simplifier initially left a residual written in tan(x) and cos(4x); rationalizing it with the elementary twice-double-angle identity made the residual exactly zero. This was a simplifier normalization issue, not a failed derivative identity. The asinh positivity argument and the zero-count inference remain the explicit analytic proof, not symbolic-software assertions. Output: out/DERIVATIVE_CHECKS.json.

## proof dependencies and changed downstream conclusions

The proof uses the actual two-bit Fourier expansion, Shannon chain rule, elementary calculus, continuity, and the implicit function theorem for simple roots. There are no open FEI assumptions, no dependence on a finite census, and no invocation of Maassen-Uffink. This is a completion of the already-open A084 continuum packet, not a new broad FEI candidate. It replaces the stage-1 unresolved sign map with a full real-parameter theorem and identifies the second exact zero curve that the old box subdivision obscured. Its both-singleton consequence rules out a tax-free biased selection shortcut, while leaving B09's corrected uncertainty statement and uniform C018/C019 intact. The independent review queue is not treated as mathematical acceptance.

## one next mathematical action and independent reviewer

Next mathematical action: hand the full map to B09/B13 to test a source-complete terminal-inclusive tree charge at induced AND biases, retaining both actual singleton correction terms and single-use physical influence. The map tells precisely when choosing a coordinate can or cannot avoid a positive correction, so repeating the grid is retired. A090 is the primary independent reviewer of the curvature-to-root-count chain; A094 is alternate. Requested review points: the fourth derivative, strict-concavity zero-count inference, existence/uniqueness of the transition, and angle reflections on both sides of pq=1/2. Downstream consumers are A041/A046/A050/A057/A064/A096. No messages to others are sent; handoff is through these saved artifacts.

## actual persistence receipts or precise save blocker

REPORT.md, PROOF.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code and exact output are saved in this stage's A084-only run directory. out/RECEIPTS.json records SHA256, size, required-file/schema checks and current input pins; every file is below 20 MB. STATUS.md, WORKLOG.md and LEARNED.md are current. No shared file was modified, no git was run, no brain was written, and no process was detached. Independent acceptance and supervisor copy/mirror are pending; local durable save is complete.

**Universal bridge:** This stage closes the B17-lead continuum target completely: 902 previously unresolved boxes are replaced by an all-real-parameter analytic sign theorem, with the exact threshold, all zero branches, their counts, and four-edge coverage. It moves C019/G-BIASED-TAX by proving that singleton choice cannot eliminate the tax on the entire square (0,p_*)^2, but it improves no universal FEI constant. What remains is payment of a valid positive correction plus conditional spectral cost using nonreused physical influence and terminal entropy in the actual tree. The NEXT consumes a now-complete gate interface in that unpaid global ledger, rather than spending another stage on a sample grid or another isolated gate constant; it is the shortest route from this packet to the universal stopping-tree bridge.
