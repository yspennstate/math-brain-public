# A085 stage 3: minimum-influence endpoint adversary

## exact target, quantifiers, hypotheses and units

Audit the dimension-cutoff scope of A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS@1 and A096-TERMINAL-KL-REFUND-AUDIT@1. Both quantify over finite nonnegative sublinear cutoffs s(N)=o(N). For every N>=1 and actual nonconstant uniform-cube Boolean sign, identify the minimum positive physical influence and the admitted functions at its exact threshold. For every fixed ell>=2, determine the optimal higher-tail erasure and oriented-cost ratios over that endpoint class, across all dimensions. Entropy and logarithmic costs are in bits. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md, supervisor snapshot 2026-10-14 00:50 UTC, own STATUS.md, B17 STREAM_NOTES v2 dated 2026-10-11 23:40 UTC, and the complete execution protocol revision 2026-10-11-execution-v2. The lead's A071 grid and KB4/KB5 audit assignments were completed in this packet's preceding stages; their baseline is not repeated. The protocol's new-dependency dispatch now selects the board's A090/A096/A099 cutoff and terminal-KL continuation, consistent with the previous STATUS.

Read A090 run 20261013T213537Z REPORT in full, especially equations (5)-(14), A096 run 20261013T220343Z REPORT/CLAIMS and DERIVATION in full, especially equations (1)-(6) and the cutoff paragraph; A073 run 20261013T234148Z REPORT, and A099 run 20261014T001305Z REPORT, including their explicit terminal-payment gaps. These establish that the normalized reference audit has already received independent reconstructions; another unchanged-domain replay is not dispatched. Context/navigation/papers were read in earlier stages and supply no theorem premise here. Source byte receipts are saved in out/source_receipts.json; the new proof is self-contained.

## complete derivation or exact first unsupported line

PROOF.md gives the complete all-dimensional argument. For the smaller sign class A of size a, internal conditional-fiber entropy and the chain rule imply b(A)>=a(N-log2 a). Strict concavity endpoint comparison shows the minimum nonzero influence is N 2^(1-N); for N>=3 equality occurs precisely at one-point defects and their complements. N=1 has its two nonconstant signs; N=2 also has four signed dictators, alongside eight point/complement signs. The N=2 exceptions are retained explicitly.

Set s_*(N)=N-1-log2 N, so 2^-s_*=N 2^(1-N). For each point defect, all nonempty Fourier masses are 4*2^-2N. Equal-mass edge counting gives

    R_geell/I = 2-4*2^-N sum_(r=0..ell-1) binom(N-1,r),
    M_geell/I = (R_geell/I)/2.

The signed-dictator exceptions contribute zero tail. For every fixed ell>=2 the endpoint suprema are therefore exactly 2 and 1, approached as N tends to infinity and never attained at finite N. An actual five-bit witness independently certifies K_E>107/40>2. Also M>=B-I/ln2 and ln2>2/3 imply K_M>47/40>1. Thus the loss-free optimal-constant transport cannot be extended to arbitrary nonnegative cutoffs. The endpoint cutoff remains nonempty in every dimension, so the obstruction is stronger than the empty-class example s(N)=N. A strict cutoff above s_* has no nonconstant functions; constants are excluded before division.

Neither audited source asserts the false extension. Their stated sublinear hypotheses survive. PROOF.md independently checks the nonmonotone tail-envelope construction, its eventual dimension bound, logarithmic influence overhead, fixed-ell requirement and extended-real supremum logic. This is a completed cutoff scope check, not a full replay of either source's finite activation checker and not an independent acceptance of the assembled FEI chain. The first unsupported universal line remains one finite bound on K_E, equivalently a retained terminal-core KL payment. No finite-dimensional computation closes that line.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes computation. Exhaust all labelled truth tables for n=1,2,3 (276), then the point defect at zero and its complement for each n=4 through 10 (14), then the named five-bit negative set {5,12,13} (1). Exactly 291 cases, no symmetry quotient or automatic dimension escalation. The n<=4 baseline census is not repeated. Three fixed tail levels ell=2,3,4 validate the formulas, while the analytic argument covers every fixed ell>=2.

The checker uses direct character sums and physical edge counts, integer/Fraction masses, formal prime-log forms and exact positive-series remainder intervals. It imports no source helper. The named witness's five coordinate ratios exceed 107/40 with exact rational interval lower bounds. The nonconstant endpoint counts at n=1,2,3 are respectively 2,12,16. Every completed case is flushed immediately to JSONL.

Executed from A085:

    python -X utf8 runs/20261014T005642Z-fleet05-A085-certificate-adversary/code/audit.py --pilot
    python -X utf8 runs/20261014T005642Z-fleet05-A085-certificate-adversary/code/audit.py

Pilot PASS: 20 cases, 235 assertions, 0.127179 seconds. Full PASS: 291 cases, 2,475 assertions, 12.526274 seconds. Outputs: out/pilot.json, out/audit.json, out/cases.jsonl and out/witness_certificate.json. Frozen memory estimate 80 MB; no >300 MB job was started and no memok trigger applied. Both runs finished below the 55-second budget. No floating-point value decides a mathematical sign, no GPU or background process was used, and every command completed. Artifact receipts are provided by code/finalize.py's schema/hash readback, not additional mathematical tests.

## proof dependencies and changed downstream conclusions

The new endpoint theorem depends only on finite cube edge counting, entropy chain-rule conditioning, concavity, Fourier character sums, a convergent positive log series and the explicit independently checked five-bit witness. It assumes no unreviewed FEI or terminal-payment bound. A090@1 and A096@1 are source targets, not premises for the endpoint proof. Their sublinear scope is supported; no original claim is refuted or overwritten, and no improvement to a universal constant is claimed.

B20/A099 must retain the cutoff quantifier when using low-influence or higher-tail completeness. A073's complete-normalizer warning remains valid; restricting the admissible dimension/influence domain is a separate way to lose the arbitrary terminal seed. Prior stage's generic helper error-budget correction remains pending and is not reopened. The new claim is a narrow scope certificate, not another broad unreviewed universal candidate.

## one next mathematical action and independent reviewer

Audit a concrete signed-Boolean terminal-core KL lower bound from A001/A096/A073 against the complete normalized reference and one influence ledger, retaining arbitrary seed entropy and the precise cutoff hypothesis. A090 is the primary independent reviewer of this endpoint certificate; A094 is alternate. A096/A099/B20 consume the two exact endpoint constants and keep their source sublinear statements unchanged. This replaces repeated activation-refund or finite-layer tests with the unpaid terminal inequality directly.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, PROOF.md, FROZEN_SPEC.json, CERTIFICATE_ADVERSARY.md, CERTIFICATE_FAILURE.json, code and exact out artifacts in the assigned stage directory. out/validation.json verifies exact protocol fields, report headings, endpoint counts and witness signs; out/manifest.json records persisted byte sizes and SHA256 values. All files remain below 20 MB. STATUS.md is two lines, and WORKLOG.md/LEARNED.md are updated only inside A085. No other folder or shared index was written. Independent review, supervisor copying, shared adoption and remote mirrors are unverified; there is no local save blocker.

## Universal bridge

This stage moves C018 by completing a dimension-cutoff scope check: at the exact minimum-positive-influence threshold the all-dimensional higher-tail supremum is 2 and the oriented supremum is 1, strictly below the unrestricted constants, so the sublinear-cutoff condition cannot be silently dropped. It preserves A090/A096's stated bridge and supplies an explicit endpoint obstruction to overextending it; the quantitative universal-bound improvement is zero. A dimension-independent payment of the complete terminal-core KL bill remains open. NEXT audits that actual signed-Boolean payment with one physical influence reserve because the exact endpoint and source transport separate a restricted admissible class from the surviving arbitrary seed, which is the shortest identified route to full FEI rather than another isolated class bound.
