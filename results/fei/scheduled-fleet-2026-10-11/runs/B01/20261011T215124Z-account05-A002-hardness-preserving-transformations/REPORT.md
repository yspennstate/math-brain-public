# exact target, quantifiers, hypotheses and units

Packet A002, B01, stable gap FEI-B01-A002-INITIAL. Reconstruct the tensor, balancing, point-activation, systematic-code and auxiliary-smoothing ledgers for every finite Boolean sign on the uniform cube. Every added physical coordinate must have its influence counted. Entropy is in bits; constants are handled without dividing by zero influence. The optimal constant C_* is an extended-real supremum, not an assumed finite number.

The packet's baseline reproduction is complete locally. The companion manuscript's simultaneous hardening and subexponential-scale reductions are independently reconstructed here. A separate full Fourier support admission proof fills the packet's explicit low-influence/full-support test. These results establish endpoint equivalence; full FEI remains OPEN.

Required supplementary artifacts: [TRANSFORMATION_LEDGER.tex](TRANSFORMATION_LEDGER.tex) contains complete proofs and dimensions, and [HYPOTHESIS_SURVIVAL.json](HYPOTHESIS_SURVIVAL.json) distinguishes preserved, lost, conditional and incompatible hypotheses.

# sources actually read, revisions and theorem locators

The protocol is fei-execution-protocol/2, revision 2026-10-11-execution-v2. Read the campaign README, CURRENT_STATUS, registries, packet index, stream actions, assignment contract and plan; supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING; BOARD; A001's 20261011T210330Z report; and earlier B05/B09/B19 reports. The B01 Claude STREAM_NOTES.md was absent at initial reading. This is an access limitation, not a mathematical blocker or a disagreement with the lead.

[out/SOURCE_MANIFEST.json](out/SOURCE_MANIFEST.json) records exact local byte hashes and encodings of 41 source files. Every listed file was loaded in full; theorem inspection focused on the following locators. Loading bytes is not independent certification of every theorem in a manuscript. Four provided paper text files require cp1252 decoding, not UTF-8; line-numbered copies are saved under out/.

- Companion manuscript, source_material/reductions/paper/main.tex, dated 11 October 2026: section 2, thm:simultaneous, lem:balanced, lem:diffuse, lem:activation, lem:coding, lem:codeexist, eq:gadget, lem:plateau, cor:subexponential. These are the primary objects of independent reconstruction, not dependencies on A001's acceptance status.
- Threshold 38-page text: section 8.3, Proposition 8.9 and Corollary 8.10. Earlier 29-page version was inspected for conventions and scope; its page numbering is not substituted for the later selector/activation source.
- Supplement sources/ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md, section 3: parity/pair lifts and nonhereditary zero erasure. Supplement seed lemmas and counterexample archive provide scope guards; their unbundled source links were not certified as read.
- Percolation 30-page and other 31-page texts: introduction and class scope. Neither geometric crossing assumptions nor their singularity conclusions are imported into a universal transformation proof. No attempt to certify their full proofs is claimed.
- Plan A002 acceptance contract: exact dimensions, mean/H/I, tensor limits, full-support admission, physical versus spectral independence; independent reviewers A086/A094.

The canonical registry's original B09 certificate defect and the distinction between an available endpoint upper tax and a necessary lower tax are retained. No B09 uncertainty theorem or numeric entropy certificate is an input to this proof.

# complete derivation or exact first unsupported line

The TeX ledger proves all statements by Fourier expansion, injective support maps, entropy chain rule, a finite union bound and a proved finite-law continuity bound. The critical exact smoothed ledger, absent from A001's independent reconstruction, is as follows. Fix a balanced diffuse seed b on n bits, a balanced gadget g with entropy H_g and influence I_g, and m>=2. Point-activate b^tensor m using s=ceil(2 log2 m), p=2^-s; systematically code its N=mn+s coordinates with r auxiliary bits. Write e_j=Pr((AS)_j=1) for those auxiliary spectral memberships and Q=sp+sum e_j. Replace only the s controls and r auxiliary physical bits by disjoint g gadgets. The resulting dimension is mn+d_g(s+r) and

    H(F) = pm H(b) + 2sp(2-p) + phi((1-p)^2) + H_g Q,
    I(F) = pm I(b) + I_g Q,
    EF = 1-p, Var(F)=p(2-p), 0<=Q<=p[s+r(2-p)].

Original data influences are p I_i(b). Every gadget leaf is charged by its host influence times its own leaf influence. Thus the code's potentially variance-sized influence is diluted rather than discarded. Physical inputs are independent; the new spectral memberships can be deterministic parity functions of old memberships.

Choose a systematic code with distance >2k+1 and a majority-of-parities gadget with minimum nonempty support 2k+1 and internal distance >=4k+2. Different outer supports differ on enough occupied blocks; different terms within one outer support differ inside a gadget. This proves distance >2k. Removing <=k physical coordinates cannot collide supports, preserves entropy and mean and subtracts exactly the queried influences. The children remain numerically in the same epsilon class with distance >k. This is a finite-depth plateau, not arbitrary restriction closure. All error terms are O_g(p log m), while the principal H/I terms are pm times the fixed seed values. This independently verifies R01 and, with activation length o(m) chosen explicitly in the TeX ledger, R02 from A001's graph.

The two-cell test uses the actual arbitrary seed: g_m=z f^tensor m and M_g=((1+g)/2)y1+((1-g)/2)y2. A class bound C gives mH(f)+4<=C[mI(f)+3]; m->infinity recovers H(f)<=C I(f). Point activation with s=ceil(2 log2(m+1)) has influence and minority probability tending to zero and ratio tending to the same seed ratio. The converse for both optimal constants is subset inclusion.

The packet's full-support test is addressed in both possible senses. If it means all physical variables relevant, delete irrelevant coordinates from the separated-support construction; all remaining ledgers survive. If it means every Fourier coefficient nonzero, exact separation is incompatible with it. For this second endpoint take the elementary activated tensor G_m on D_m=mn+1+s bits, append two dummy bits, and flip one physical value. With M_m=D_m+2 and delta=2^-M_m, coefficients change by exactly +/-2delta. Old nonzero coefficients have magnitude >=2^-D_m, so none can cancel; old zeros all become nonzero. Each added or old coordinate costs at most 2delta in influence, and total influence error is at most 2M_m delta.

The squared-spectrum total variation is at most 2sqrt(delta), by Parseval and Cauchy-Schwarz. A maximal-coupling proof bounds entropy change by h2(tau)+tau log2(2^M_m-1). These errors are exponentially small compared with the activated tensor influence of order 1/m. Hence all-Fourier-support plus arbitrarily small influence and minority probability again has optimal constant C_*. With slack, the same surgery preserves the relative-influence conditions of the smoothed construction; it destroys exact distance and plateau. No numerical logarithmic approximation is used to prove this limit.

For the auxiliary endpoint, an actual fixed base F_*(X,Y) times arbitrary fresh-data f^tensor m preserves its X spectral marginal and X-degree. Its conditional entropy adds mH(f) and its influence adds mI(f). Dividing any proposed dimension-free conditional bound by m proves full FEI. A hypothesis on the entire conditional spectrum, such as genuine product conditional laws, generally fails under this embedding when the arbitrary seed spectrum is nonproduct; it is not a free preserved hypothesis.

First unsupported line for a universal FEI conclusion remains: a finite bound on the entropy/influence ratios of any one of the admitted arbitrary-seed classes. The ledgers cannot supply that bound by renaming it. No unbounded Boolean H/I family has been found.

# executed validation with domain, arithmetic, commands and outputs

The frozen specification was saved before execution in [out/FROZEN_SPEC.json](out/FROZEN_SPEC.json). Pilot: all 22 labelled seeds through n=2, 5,204 exact assertions, 0 failures, about 0.12 seconds. Full fixed domain: all 278 labelled seeds through n=3, 81,246 exact assertions, 0 failures, about 4.95 seconds. No symmetry reduction, random search, heavy job, automatic dimension increase or GPU. Estimated memory is 40 MB; no >300 MB job was proposed.

Commands from A002:

```text
python -X utf8 runs/20261011T215124Z-account05-A002-hardness-preserving-transformations/code/source_audit.py
python -X utf8 runs/20261011T215124Z-account05-A002-hardness-preserving-transformations/code/exact_checks.py --nmax 2
python -X utf8 runs/20261011T215124Z-account05-A002-hardness-preserving-transformations/code/exact_checks.py --nmax 3
python -X utf8 runs/20261011T215124Z-account05-A002-hardness-preserving-transformations/code/finalize.py
```

The checker uses direct integer Walsh sums rather than the manuscript's compressed activation/code checker. Fraction arithmetic verifies spectra, means, variances and influences. Entropy equalities are checked as rational linear combinations of log2 primes. It verifies tensoring, balancing, two-cell selectors, unbalanced activation with 1/2 controls, systematic parity coding using columns 3,5,6, every assignment on up to two coded physical coordinates, and two-dummy point surgery with full Fourier support. Auxiliary smoothing covers all 16 two-bit seeds, on 20 final variables, by sparse exact expansion plus 32 deterministic truth evaluations per seed. It is not an exhaustive 20-bit truth-table check. The all-dimensional conclusions rely on the analytic proofs, not the finite check.

Results: [out/EXACT_CHECK_n2.json](out/EXACT_CHECK_n2.json), [out/EXACT_CHECK_n3.json](out/EXACT_CHECK_n3.json). No sign decision rests on floating point. The finalizer checks schemas, statement hashes, byte-identical packet compatibility and file sizes. No TeX/PDF compilation or Lean formalization is claimed.

# proof dependencies and changed downstream conclusions

The two local claims are source-complete proof packages with independent campaign acceptance still pending. Proof dependencies are elementary Fourier orthogonality, Boolean pivotal influence, entropy chain rule, finite union bound and the proved continuity argument; the full-support extension consumes the first local ledger claim at version 1. No open FEI premise is consumed unconditionally. A001 is a coordination source, not a circular theorem dependency.

Downstream: A005/A055 should reject rarity, small relative influences, fixed marginal, bounded X-degree, all-variable relevance and full Fourier support as sufficient exclusions of arbitrary seeds. A012/A021 must retain the control term spd and rare-selector entropy. A030/A078 may use support coding and the exact finite-depth restriction plateau, but should not infer hereditary easy leaves. A048/A060 can use tensor limits to eliminate additive overhead. A043 must check any prime-gate hypothesis separately; these operations do not preserve an unspecified prime class. A051 must distinguish relative influence smoothing from merely adding a balancing literal.

Product conditional spectral laws are a substantive endpoint hypothesis: a tensor with an arbitrary nonproduct seed destroys that property. Bounded dimension, fixed arity/depth/read bounds, geometric crossing structure, and full restriction-hereditary control have no universal preservation theorem here. This is a limitation of the tested transformations, not a disproof of those endpoints.

# one next mathematical action and independent reviewer

Next action: A005/A055 should test one concrete proposed structural endpoint against the exact smoothed-and-activated arbitrary-seed construction, and exhibit the precise failed hypothesis if it is excluded. A086/A094 should independently review the code redundancy and smoothing ledger, then the full-support one-point continuity estimate. A001 can consume this reconstruction to replace the previously unreviewed R01/R02 derivation gap. Review routing is through these saved artifacts; no message was sent to other agents.

# actual persistence receipts or precise save blocker

All outputs are saved within the assigned A002 run directory, and rolling STATUS.md, WORKLOG.md and LEARNED.md remain in A002. [out/ARTIFACT_RECEIPTS.json](out/ARTIFACT_RECEIPTS.json) lists output hashes and sizes. The finalizer's schema receipt certifies artifact construction only. The B01 lead notes were missing at source intake; later existence check is recorded separately. No source tree, another agent's folder, brain, shared board/index, git repository, mail service or scheduler was modified. Supervisor copying, Brain mirror verification, independent acceptance and downstream mathematical use are not claimed.
