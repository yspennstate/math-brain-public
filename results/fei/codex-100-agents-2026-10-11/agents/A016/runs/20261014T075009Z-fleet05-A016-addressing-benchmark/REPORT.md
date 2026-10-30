# A016 stage 6: two paid exposures with the same reference, and the exact terminal boundary

Full FEI is OPEN. On A020's new biased rare-query fixture, the SAME complete incoming full reference can be carried through q and one essential private-v query without renewing its bank. All four resulting terminal references are rate4 eligible. A later constant terminal shows that marginalization alone does not preserve rate4 eligibility: its complete inherited cost exceeds4I for every k>=6. These are dependency consumption and a scoped continuation, not a new broad FEI candidate.

## exact target, quantifiers, hypotheses and units

For every k>=3, delta=2^-k, A=1_(v=0), h=chi_u(1-A)+chi_q A, and a fresh positive-mean two-bit point mask s (mean1/2), put F=1 on gate x0 and h*s on x1. Bits are independent uniform physical 0/1 bits; signs are Boolean; entropy, cross-entropy CE and KL are in bits. Inherit the supplied A020 full root reference; after each query use its frequency marginal for BOTH physical children. No actual-spectrum reset, new activation lift, discarded terminal, or renewed bank is permitted. Test q then v0, and separately inspect the later physical leaf q0,v=0.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision2026-10-11-execution-v2. Read BOARD.md at stage start (07:47 UTC snapshot), middle/end readbacks (the shared board changed during this work), B04 STREAM_NOTES.md v2 unchanged2026-10-11 23:25 UTC, own STATUS.md and previous stage report/helper. Required campaign and paper/context reading is carried from prior stages; no new external literature assertion is used. New dependency reads: A020 run20261014T062539Z-fleet05-A020-selector-boundary-tests REPORT.md and CLAIMS.json, sections2-6; A019 run20261014T055119Z-fleet05-A019-orthogonality-extensions REPORT.md, private-query/refund and balanced-child scope; A018 run20261014T051305Z-fleet05-A018-shared-data-collision-law REPORT.md, supplied joint constant-branch reference. This consumes A020's exact second-query NEXT and complements its forced positive-row result. A094's board warning that paid incoming codes need not be eligible at descendants is respected. Source hashes are saved as close-time mutable receipts, not immutable stage-start revisions.

## complete derivation or exact first unsupported line

### 1. Independent source reconstruction and the one fixed root reference

The k-bit point indicator has Walsh coefficients delta everywhere. Each h_q child has mean +/-delta, main coefficient1-delta at{u}, and2^(k+1)-1 coefficients of magnitude delta. Their squared laws are equal, called P. In the parent, every u-absent child coefficient is transferred to queried frequency q PRESENT, while every u-present coefficient has q absent. Thus the positive empty unqueried row forces q present; the parent mean and full empty frequency mass are zero. The consistent incoming core reference is exactly

Q_h=(P_h+point_{q})/2.

This is A020's actual conditional lift of (P+point_empty)/2, reconstructed from signed Walsh coefficients. Its full empty-set reference is zero. With exact P_s uniform on four labels, the SAME full physical activation reference is

Q_F(gate,T)=[Q_h(core)*P_s(mask)+point_empty(T)]/4,

for BOTH gate frequencies. The true root conditional gate frequency is uniform, including the empty data row. This fully normalized reference contains its ghost mass and all physical labels.

The source posterior refund at either freshly lifted child is

D_child=[a log2(a/t)+(1+a)log2((1+t)/(1+a))]/2,
a=delta^2/4, t=(1+delta^2)/8.

Parent refund and core KL refund are zero. The formula and its positive limit (1/2)log2(9/8) independently establish the source forced-row divergence; finite checks additionally certify its stated1/32 lower bound on our frozen domain. Our independent review accepts the spectra, forced support, exact refund and divergent-ratio clauses plus reference eligibility. It does not purport to accept every other source clause (in particular its full K1 erasure proof or all-k1/32 estimate) merely from these checks. The source statement/hash is preserved.

### 2. Marginal transport is a full-code identity

For any Boolean f and supplied normalized Q with finite CE, query a physical bit i. Set Q'=sum_{i-frequency}Q, identical for both children. The exact Walsh identity gives average_b P_(f_b)(T)=sum_e P_f(e,T). Therefore

CE(f,Q)=average_b CE(f_b,Q')+L_i,
L_i=sum_(e,T) P_f(e,T) log2[Q'(T)/Q(e,T)]>=0.

This retains every atom and both terminal costs. The support of a positive child atom is covered because its averaged mass is positive. Conditional likelihoods have ratio>=1. Iterating on an adaptive tree gives CE_root=weighted sum L_i+average leaf CE; this is an accounting identity conditional on having the root reference, NOT a construction of a universal cheap reference. It does not imply child rate eligibility. Our checks reconstruct it from independent truth tables and actual restrictions, not from an author's checker.

### 3. First query, explicitly paid conversion, and second query

Let Q1 be the marginal of the FIXED Q_F after q. Its core marginal is (P+point_empty)/2. All inherited gate conditionals remain uniform. Fresh A020 child references instead use the actual gate conditional on their empty data row; their data priors are the same. Thus the only conversion is the complete conditional KL

E=CE(child,Q1)-CE(child,Q_fresh)
 =(1+mu^2)/2 * KL_Ber(p_gate ||1/2), mu=+/-delta/2.

Using KL<=chi-square/ln2 and ln2>1/2 gives 0<=E<4mu^2=delta^2. This conversion is retained as a terminal debit, not erased. The exact inherited first-query debit is

L_q=(1/2)log2[(9+delta^2)/8]
 +(delta^2/8)log2[(9+delta^2)/(1+delta^2)].

Only the empty unqueried core/mask row has both q-reference sectors; its two gate copies have true masses1/4 anddelta^2/16. In particular L_q tends to(1/2)log2(9/8), not zero. The original fresh-child insertion J equals L_q+E. Conservatively log(10/8)<1/2, log2(10)<4 and delta^2<=1/64 imply J<1/4+3delta^2/2<=35/128<5/8. Hence the previously booked first-query ceiling is still valid INCLUDING conversion.

Now expose v0 at each actual q child and inherit Q2=sum_(v0-frequency)Q1. Both queries have actual full-function influence delta/2; all four physical histories are retained. Partition second-query Fourier rows into: ordinary paired small rows, main-u pair, empty-core pair with/without the constant gate contribution. Ordinary pairs have equal reference masses, conditional charge1, and total true mass at most delta. For the main-u pair, absent-sector cost is at most delta^2 using log(1+t)<=t/ln2, and present-sector cost at most k delta^2. Empty-core absent-sector cost is at most2delta^2; present-sector cost at most(k+2)delta^2 because its largest likelihood ratio is below16/delta^2. Consequently, at EITHER q child,

L_v < delta+(2k+5)delta^2 <3delta <=3/8.

The strict middle inequality follows from (2k+5)2^-k<=11/8<2 for k>=3. This is a second debit from the SAME owner; the first fixed debit is never renewed.

The supplied child-core costs c_b=H_k+K_core satisfy K_core<=1 and H_k<4(k+1)delta, while I(h_b)=1+(k-1)delta. Here H_k=eta((1-delta)^2)+(2^(k+1)-1)delta^2(2k); its main term is<4delta by -(1-epsilon)ln(1-epsilon)<=epsilon and ln2>1/2, and its small terms sum to<4kdelta. Physical edges give the displayed influence. Their unused core surplus is S_b=4I(h_b)-c_b>3-8delta>=2. The private HALF reserve is thus>=1. Mask half-budget leaves1 after paying its exact code; gate profile is at most2 and any positive-mean gate shortfall is at mostdelta, paid by that mask remainder. The private half-reserve is untouched before insertion. One such averaged reserve pays J+L_v<5/8+3/8=1 (indeed<83/128 under our sharper first bound), with no renewal. The conversion E is included in J. Complete final CE is retained: by marginal transport its leaf average is at most the inherited q-child average. Thus this conservative allocation pays the converted terminal costs and both queries; it does not count a released terminal bill as a newly created bank.

### 4. Every complete two-query terminal is eligible, for all k

Q2's core masses are t=(1-2delta+2delta^2)/2 at{u}, (1/2+delta^2) atempty, and delta^2 at every other remaining core frequency. In particular t>=25/64. At v0=1, h=chi_u for BOTH q branches; its full activation cost is

CE=1+(1/2)log2(16/t)<4,
I=3/2.

At v0=0 the two child means are+/-2delta, the main coefficient is1-2delta, and each other core coefficient has magnitude2delta. The full inherited terminal cost has four disjoint groups: empty data row (true mass(1+delta^2)/2, code length<=2); main-u group (mass(1-2delta)^2/2, length<6); other nonempty core groups (mass2delta-4delta^2, length4+2k); shared-only nonempty group (mass3delta^2/2, length<=5). Hence

CE <4+4(k-1)delta+(9/2-8k)delta^2
 <=4+4(k-1)delta.

Its influence is 3/2+(k-2)delta minus/plus delta/2. Even the smaller rate4 budget exceeds the displayed upper bound by at least2-6delta>0. All four normalized full references therefore have CE<4I, uniformly over k>=3. Parent/root eligibility also holds: CE_root<=H_k/2+7/2<7/2+2(k+1)delta, versus4I_root=6+2kdelta. Each inherited q child costs at most7/2+2(k+1)delta+delta^2, whereas its smaller4I is6+(2k-3)delta. These costs are explicit complete codes, not root-only entropy estimates.

### 5. Exact boundary: eligibility is not inherited indefinitely

Continue erasing q and ALL v frequencies of this SAME root reference, without resetting it. The core marginal on u is ((1+delta)/2,(1-delta)/2). At the ACTUAL history q0,v=0, h=+1, F is1 atx0 and s atx1, with I=3/4. The inherited reference has empty data atoms (9+delta)/32 and shared-only atoms (1+delta)/32 at both gate frequencies. The true empty data row has mass5/8 and the remaining true mass is3/8. Therefore

CE=5-[5log2(9+delta)+3log2(1+delta)]/8.

For every k>=6 this exceeds4I=3. Equivalently (9+delta)^5(1+delta)^3<2^16. This polynomial is increasing in delta, and the endpoint delta=1/64 is certified by the exact integer inequality577^5*65^3<2^64. The limit excess is2-(5/8)log2(9)>0. This is a supplied-reference eligibility obstruction, not a failure of FEI or of the telescoping identity. Its physical history is rare and has an unused bank; no claim that the excess is unpayable is made.

The first unsupported universal line is that every transported child is automatically eligible at the SAME rate, or that any signed terminal deficit has an unspent branch-specific owner. The explicit later terminal disproves the former shortcut. Universal construction of a cheap initial Q and conservation of signed conditional banks for arbitrary cores remain OPEN.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded all checks: own helper v1, k3..7, five actual families, all four q/v histories, no symmetry quotient, maximum full dimension12, expected90MB, hard60s limit. Pilot: `python -X utf8 code/check.py --pilot`. Full: `python -X utf8 code/check.py`. An explicit same-domain validation extension added complete conversion and one-owner accounting before rerunning. Final pilot495 assertions PASS in0.0242917s; full12,499 assertions PASS in0.6394851s. Every completed k is checkpointed immediately. Integer Walsh coefficients and Fraction masses certify normalization, support, erased-law identities, exact log-coefficient ledger cancellation, physical edge influences and all terminal costs. Sign intervals use36-term rational atanh series after range reduction1<=q<2, tail<=2z^73/[73(1-z^2)] and outward rational rounding; negative log weights reverse bounds. Decimal displays are not certificates.

TERMINAL_PROBE_SPEC.json was frozen before the extra named endpoint test. `python -X utf8 code/terminal.py` passed five fixed cases and31 exact assertions in0.0007457s, including the all-k>=6 integer sign certificate. The probe is a separate small named-history extension, not automatic dimension growth. Total13,025 final assertions including the repeated pilot; five distinct main families and five named endpoint checks. No failed mathematical assertion occurred. An assertion count in the endpoint summary was corrected from41 to31 before final receipt (six per case plus one global inequality); no proof result changed. The first persistence attempt used a raw-text source hash comparison; inspection of A020 code/persist.py line12 established its compact sorted statement-and-hypotheses JSON convention, which then verified exactly. out/SOURCE_HASH_BINDING.json records both conventions; no source hash or statement was altered. Jobs expected<=90MB; none required memok. Actual peak memory was not measured. No GPU, background process, windows, git, external messages, brain writes or other-agent mutations.

## proof dependencies and changed downstream conclusions

All new formulas and bounds above are reconstructed directly from Boolean truth tables, Walsh identities, reference normalization and elementary logarithmic inequalities. Source A020-BIASED-CHILD-FORCED-ROW-TRANSPORT-NOGO@1 receives a partial independent review of the explicit spectra, forced-row conditional support, refund formula/divergence and complete eligibility interface, without altering its source statement/hash or accepting excluded clauses. A018's sharp Gamma, A019's sharp curvature constant and universal slack premises are not needed. This stage does not contradict the stream lead; it follows the instruction to consume a new obstruction and preserve every terminal. The marginal identity is an elementary conditional supplied-reference interface, not claimed as a new universal reduction.

B04/A018/A019/A020/A090/A091/A094/B20 may use the two-query continuation with its EXACT starting Q, conversion and one-owner scope. They must not infer indefinite same-rate eligibility. Previous A016 stage5 bad-selector core-reuse obstruction is preserved; the mechanism changes here to inherited likelihood transport as promised. No shared registry or previous run was modified.

## one next mathematical action and independent reviewer

Transport the SAME remaining private bank along the active v=0 history to the constant h=+1 endpoint, charge its exact positive inherited terminal excess rather than resetting Q, and derive a general branch-weighted signed terminal-deficit invariant for arbitrary nonflat core children. A020/A019 review the inherited-v bound and conversion; A018/A090/A091/A094 audit reference support, one-use private reserve and the endpoint certificate. The known point fixture is the test of the invariant, not another target class enumeration.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and matching PACKET_DELTA.json, both frozen specs, code/, per-case checkpoints and exact outputs are saved inside A016 only. Rolling STATUS.md has exactly two lines; WORKLOG.md is appended and LEARNED.md records the durable interface and its failure boundary. out/PERSISTENCE.json verifies exact protocol fields, statement hashes, artifact hashes/sizes and final Universal bridge paragraph. New application independent review, supervisor adoption and mirror verification remain pending; local save is evidenced.

## Universal bridge

This stage moves C024 history transfer and B04's C019/C020 supplied-reference interface by one genuinely essential second private-data query: the SAME full root reference, explicit fresh-to-inherited conversion, retained four terminal codes and one nonrenewed private half-bank pay the first fixed debit and a second debit<3delta, for all k>=3. It also precisely limits that progress: further marginalization reaches an actual constant terminal with inherited CE>4I for every k>=6, certified by an integer inequality, so automatic same-rate child eligibility is false. Universal cheap-root construction and conservation of branch-weighted signed terminal reserves remain unproved. NEXT prices that explicit terminal excess from the already remaining owner and extracts the general signed-deficit invariant; this attacks the ownership/eligibility gap needed for full FEI instead of expanding an isolated class benchmark.
