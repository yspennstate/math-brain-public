# A043 stage 3: sharp ternary prime closure and a prime reserve obstruction

## exact target, quantifiers, hypotheses and units

Determine corrected product-biased Hplus/(I-Var) for essential Boolean prime gates, beginning with the entire ternary bias continuum left unresolved by the previous finite grid. A prime admits no genuine one-bit substitution on a proper essential block of size at least two; supports are disjoint. All probabilities are independent and interior. Delta=I-Var uses spectral influence. Hplus is in bits; E=(ln2)Hplus is its natural-unit version. Ordinary Fourier entropy H also includes the empty spectral atom. Degenerate boundary laws are treated by contraction or by limits of interior ratios, never division by a zero deficit.

Result: the sharp common supremum over all 104 ternary primes and all product biases is Cstar=2+4/ln2. Three previously remaining symmetry classes are proved here; majority and mux are reconstructed from the original A042/A044 sources with scoped reviews. All interior ternary prime ratios are strictly below Cstar. Exact disjoint composition closes every Boolean gate on at most three essential inputs and every read-once formula with fan-in at most three at this corrected constant. The ordinary uniform-input conclusion is H<=Cstar I, without claiming that this ordinary constant is optimal.

A signed singleton reserve holds in every dimension. Its tempting higher-degree companion fails even on a specified four-input prime, with an exact certified positive gap >13/100. Full FEI and the all-arity product-biased prime bound remain OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start (snapshot 2026-10-13 23:39 UTC), own STATUS.md and LEARNED.md, B09 STREAM_NOTES.md v2 dated 2026-10-11 23:33, and EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. B09's target is the n<=4 biased-prime supremum, and its review cap puts scoped reconstruction ahead of new broad candidates. This stage consumes the new majority and mux evidence before narrowly completing the remaining ternary packet. It does not recompute the lead's one-bit tax or AND coefficient.

Read original A042 stage-3 REPORT.md and CLAIMS.json, run 20261013T221414Z-fleet05-A042-bias-endpoint-certificates: A042-SHARP-MAJORITY3-BIASED-ENDPOINT@1, hash 396cfaaabff2fa337f7a038ca4380cbede25d84a6ccd96032829a36dbecad11e. Reconstructed the core all-bias upper inequality and symmetry orbit in REVIEW_MAJORITY.md. The source's explicit 400 error constant, edge remainder formulas and validation counts are excluded. A043 supplied the earlier lower-path input, so this is independent acceptance of the upper-bound portion only, not an independent acceptance of the shared sharpness input.

Read A044's original out/DERIVATION_CHECKPOINT.md in run 20261012T040658Z-fleet05-A044-non-symmetric-gate-classes. REVIEW_MUX.md reconstructs its three-input spectral formula, fixed-address bound and sharp global supremum. This is a scoped checkpoint review, not acceptance of a nonexistent completed claim package or of the broader profile transfer.

Read A042 stage-2 REPORT.md, run 20261012T002547Z-fleet05-A042-bias-endpoint-certificates, for A042-SHARP-BINARY-PRIME-ENDPOINT@1 (hash e163ebefc916767a00214eea2d54e56e53c9666821565f612f15a7ef4f17d5e8), exact binary formulas (3) and (7), and composition (9). Read own prior stage-1 claim and stage-2 progress. The binary formula is Hplus/delta=2+(2/ln2)[A(u)+A(v)] for corner gates, and [A(1-v1)+A(1-v2)]/ln2 for parity, with A(t)=t ln(1/t)/(1-t)<=1; these prove the binary input used here without a floating-point maximization. Own stage-1 prime/composition statement hash is bd9d9a2c11b8e82cc302f653748ffe650977e88c429bb63d6ef8cdffb673b4f2. No sharp-tax, percolation or external-paper theorem is an additional mathematical premise. Exact source file hashes are saved in out/source_receipts.json.

## complete derivation or exact first unsupported line

CORE_PROOF.md is the full local derivation. Its universal signed reserve uses Di=(f|Yi=1-f|Yi=0)/2 in {-1,0,1}. If ci=E Di then Var(Di)>=|ci|(1-|ci|) and ci^2 ln(1/ci^2)<=2|ci|(1-|ci|). Parseval yields

    E_single <= 4 delta - 2 R,
    R=sum_{|S|>=3}(|S|-2)P(S).

The exact catalogue exhausts all 256 labeled ternary sign tables, and identifies five prime input-permutation/reflection/output-negation orbits of sizes 16,8,8,48,24, with minimal masks 22,23,24,25,27. The symmetry preserves the full bias domain and ratio. The essential-block criterion is exhaustive: a proper block substitution gives exactly two distinct rows; conversely the row label supplies the Boolean inner gate. Thus the catalogue omits no prime class.

For all-equal signs (orbit 24), pair amplitudes are 1/2 and there is no triple. The scalar inequality h(|(a+b)/2|)<=[(1-a^2)+(1-b^2)]/2 pays singletons and gives E<=(4+ln4)delta. Its all-rare equal-bias path reaches Cstar.

For exactly-one (orbit 22), c_ij=(3mk-1)/4 and c_123=3/4. Each pair excess over ln4 P(ij) is at most (2/3) of the same triple mass T. Keeping the signed reserve's -2T gives E<=(4+ln4)delta-ln9 T. The path (1-q^3,q,q) reaches Cstar.

For mask 25, c_12=1-p3/2, c_13=-p2/2, c_23=-p1/2, c_123=-1/4. The distinguished pair contributes a negative -2T credit, while each other pair needs at most +2T. Together with triple entropy ln16 T, the higher-degree cost is at most ln4 delta+2T. The signed singleton reserve cancels it exactly. The path (q,q,1-q^3) reaches Cstar. Discarding the distinguished negative credit would leave an unpaid +2T.

The majority reconstruction gives E<=(4+ln4)delta-(ln4-1)T. The mux reconstruction gives E/delta=ln4+[d^2 ln(4/d^2)+2v0 A(1-q)+2v1 A(q)]/(v0+v1), where d=|m1-m0|. Geometry v0+v1>=d(2-d) and ln(2/d)<=2/d-1 pay the data-means term. All five classes therefore have the same sharp supremum. CORE_PROOF.md gives explicit centered-coordinate composition and contraction, establishing the stated formula closure. Its lower paths are analytic limits, not extrapolations of grid samples.

The companion E_ge2<=ln4 delta+2R is false on primes. The sign gate positive exactly at assignments 7,8,15, mask 33152, is essential and passes all ten proper block row tests. At probabilities (1/2,1/2,1/2,1/1024), its exact delta is 5257209/16777216 and R is 262911/4194304. The certified companion excess exceeds 13/100. Its Y4=0 slice is AND3, whose uniform companion excess is (3ln2-1)/8>0. The prime slice explains the obstruction. The actual total corrected inequality has margin greater than 9/20 in natural units at this point; this is not an FEI counterexample.

The first unsupported replacement is an all-arity cofactor-sensitive entropy payment that retains unused singleton slack and pays the higher-degree excess without charging the same mass twice. Prime irreducibility alone does not eliminate a degenerate composite slice. Neither the signed reserve nor ternary affine-coefficient identities establish the required replacement.

## executed validation with domain, arithmetic, commands and outputs

Every job had a frozen specification before execution, below the 300 MB trigger; no heavy job or automatic dimension increase was used. Estimated memory 20-60 MB; peak memory not measured. Each pilot completed below 60 seconds.

- `python -X utf8 code/catalogue.py`: all 256 ternary tables, integer row comparisons and full 96-element sign/input symmetry action; 116 assertions, 104 primes, five exact disjoint orbits, about 0.053 seconds. Saved out/catalogue.json.
- `python -X utf8 code/check_proofs.py`: all five explicit gate tables at {1/16,1/8,1/4,1/2,3/4,7/8,15/16}^3 and five fixed boundary paths at t=2^-k, k=2..10; 1,760 total cases, 56,661 assertions, 18.612 seconds. Every normalized spectrum is compared with independent centered truth-table moments using Fraction arithmetic, including Parseval and the signed-derivative reserve. Class-specific inequalities use exact rational outward natural-log intervals. Saved out/proof_checks.json.
- `python -X utf8 code/check_obstruction.py`: one deliberately specified four-input prime, not a dimension-expanded search; all six size-two and four size-three block tests, exact independent moments, companion sign and total-margin certificates; final run 64 assertions, 0.024 seconds. Saved out/prime_obstruction.json. The first run certified the companion sign; the second retained that check and additionally measured singleton slack and total corrected margin.

For log intervals, normalize x by exact powers of two and set z=(x-1)/(x+1) in [0,1/3]. Sum 2 z^(2j+1)/(2j+1) for N=24 or 32; the positive tail is at most 2 z^(2N+1)/[(2N+1)(1-z^2)]. All sign decisions are rational. Decimal displays are supplementary. Complete continuum closure comes from the written inequalities; these finite checks are independent implementation checks. Frozen specs, exact outputs and source hashes are preserved locally. The final persistence validator checks schemas, statement hashes, compatibility bytes, all required artifacts and rolling status, and writes out/persistence_validation.json.

## proof dependencies and changed downstream conclusions

The new three orbit proofs, signed reserve and prime counterexample depend only on exact Boolean algebra, elementary logarithm inequalities and the exact local catalogue. The sharp binary bound is consumed at its explicit formula scope. Majority and mux are reconstructed at the explicitly limited scopes above; the majority's bundled corner constants and A044's generalized profiles are not premises. The earlier decomposition identity is rederived locally, avoiding an unreviewed whole-package assumption. The source manifest and scoped review records pin the actual versions used.

B09 can remove all arities <=3 from the continuous biased-prime frontier. A042/A044 receive substantive scoped reviews. A041/A045 and the lead must not use the false higher-degree companion even when restricting it to essential primes. No existing campaign claim with that exact proposed companion was located or refuted here; the record identifies it as a newly tested failed extension, rather than assigning refutation to an unrelated version. Uniform all-arity FEI and the n=4 all-bias optimum remain unresolved. New proof acceptance by two independent reviewers, registry adoption, supervisor copying, Brain ingestion and mirror verification remain pending.

## one next mathematical action and independent reviewer

NEXT: derive or obstruct a cofactor-sensitive payment using the actual unused singleton slack, starting with the explicit prime mask 33152 over its full bias continuum. This is a mechanism change from the disproved triple/quartic reserve companion, rather than a new unstructured grid. A042 and A091 should reconstruct the three new class inequalities and their sharp paths; A044 or A090 should independently replay the four-input prime and its exact companion gap. No reviewer is marked accepted before that work occurs.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, CORE_PROOF.md, both scoped review notes, three frozen specs, code and exact outputs, source receipts and final validation only within the A043 stage directory. STATUS.md has exactly two lines; dated WORKLOG.md and durable LEARNED.md are appended. Earlier run artifacts and other agents' files are unchanged. Local persistence is complete; external copying and review are pending. No save blocker exists.

**Universal bridge:** This stage moves the B09 lead's C025/G-BIASED-LTF prime localization target by closing every ternary prime over the entire product-bias continuum at the sharp constant 2+4/ln2, and by giving independent scoped reconstructions of the newly available majority/mux sources. It also closes a universal signed singleton reserve, while disproving its simplest higher-degree companion on a genuine four-input prime with certified excess >13/100. The all-arity corrected prime payment and full FEI remain open. NEXT retains the unused singleton slack and targets the exact cofactor interaction exposed by that prime; this is the shortest route toward a reusable all-arity payment because irreducibility and triple/quartic credit alone have now been ruled out as sufficient, rather than merely left uncertain.
