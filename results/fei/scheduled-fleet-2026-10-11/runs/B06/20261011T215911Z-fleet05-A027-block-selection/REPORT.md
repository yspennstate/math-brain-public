# A027 — Data-first proper-block selection

Full FEI remains OPEN. Two local proof-complete claims are saved for independent review; no independent acceptance or novelty clearance is claimed.

## exact target, quantifiers, hypotheses and units

All cubes are uniform, outputs are Boolean signs, Fourier coefficients are normalized, and H is in bits. For every m,r>=1 and Boolean core u, put p=2^(-r), d=1-Eu and F=1+A_r(u-1). The frozen rule queries all m physical core coordinates, leaving the r fresh activation controls unqueried, and stops at the resulting leaves. This is a proper block of the full cube, with no spectral-sample-dependent choice. The structural class for a dimension-independent payment is I(u)>=eta*m for fixed eta>0. No core FEI bound is assumed.

The proved conditional payment is B_W<=p(2dm+2)<=6pm, hence B_W<=(6/eta)I_W on this class. The channel contribution is paid using M_W<=(2/ln2)I_W. Every terminal function is constant or a point defect with H<=4I. Thus the complete constant is max(6/eta+2/ln2,4), uniformly in m, r and core bias. Artifact resolution and this restricted theorem do not resolve universal G-R-SELECT.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was read in full. The campaign README/status, claim and obstruction indices, packet matrix and plan were consulted, with the exact A027 contract and G-R-SELECT prioritized. BOARD.md was read at the stage opening. The B06 lead file was absent; no direction from it is invented. A021's control-first work was avoided by choosing a data-first rule.

Supplement CLAIMS C005/C006/C018/C019 and COUNTEREXAMPLES X001/X003/X009/X011 supplied the baseline and scope guards. BLOCK_RESTRICTION_IDENTITY sections 1-3 supplies the exact block identity and log-Sobolev channel bound; LOG_ALLOCATION sections 4-5 and the original B05/B19 reports supply the marker no-go, which is retained. The 38-page threshold paper Proposition 8.6 and Section 8.4 (Proposition 8.9, Corollary 8.10) were read at their actual scope. Earlier threshold and both percolation versions were consulted for their introductions/conventions; their geometric or composition theorems are not silently imported. SOURCE_READS.json records local observed SHA256 pins and exact read scopes. This stage does not claim a cover-to-cover independent audit of either large manuscript. No external literature novelty claim is made.

## complete derivation or exact first unsupported line

ADAPTIVE_BLOCK_SELECTION.tex contains complete proofs. For nonempty control Fourier sets the core fiber is the normalized squared spectrum of u-1, with mass 2p^2d. The empty control fiber has mass R0=1-2pd+2p^2d and nonempty-core mass q=p^2*(1-(Eu)^2). Its exceptional binary-entropy charge is bounded explicitly by 2p, including an exact rational verification of the elementary constants. Summing all fibers gives the conditional entropy bound without dropping any row.

Physical edge counting gives I_W=pI(u) and reserved terminal influence rpd. Each negative core assignment has probability d/2 and gives the point defect D_r, with influence 2rp. Its exact spectrum proves H(D_r)<=4I(D_r); no ancestral influence is reused.

An additional exact identity is B_W/p=vL+4delta(1-p)h2(delta)+(R0/p)h2(p^2v/R0), where delta=(1-Eu)/2, v=4delta(1-delta), and L is the conditional nonempty-core spectral entropy. In the fixed-core p->0 limit this retains H(u)-h2(v)+4delta*h2(delta). A universal bound on this full-core proper-block rule implies FEI with constant K+2; FEI implies that block bound with constant C+5. The proof includes the elementary edge-isoperimetric induction used to control h2(v), so this scope bridge does not rest on an unproved inequality.

The first unsupported line for UNIVERSAL selection is replacing m<=I(u)/eta, or paying the corresponding normalized defect-spectrum entropy for arbitrary low-density cores. Simply removing that hypothesis from the same full-core rule is FEI-equivalent and is not claimed as progress toward an easier endpoint.

## executed validation with domain, arithmetic, commands and outputs

The pre-search frozen specification is SEARCH_SPEC.json: every core truth table for m=1,2,3, with r=1,2,3; 828 activation cases, no symmetry reduction, no randomness, under 50 MB estimated RAM and a 60-second cap. VALIDATION_EXTENSION.json freezes the later transport-identity checks on the same domain. The fixed k=2,4,6 coded-plateau/bent fixtures are deterministic validations, not a search escalation.

Command: `python -X utf8 runs\20261011T215911Z-fleet05-A027-block-selection\code\check.py` from the A027 folder. Final execution passed 44,782 assertions in 1.355 seconds. Full integer Walsh spectra are compared to independently counted physical influences, actual leaf channel laws and exact fiber formulas. Entropy signs use Fraction enclosures from 22-term rational atanh series, with a proved geometric remainder and sign-correct division by the enclosure for ln2. The decisive conditional bound and terminal bounds are certified on every case. Exact identity checks use overlapping independently bounded entropy expressions; those checks are consistency validation, while the analytic proof establishes exact equality. Output is out/validation.json. No independent reviewer or Lean check is claimed.

## proof dependencies and changed downstream conclusions

The positive proof depends on the recovered exact block identity/channel payment and elementary entropy/Parseval facts. Original B05/B19 no-go is used only as a stress-family comparison, not as a premise of the positive theorem. Threshold activation formulas are baseline calibration; the new output is a block-specific conditional charge and stopping ledger, not a claim to have rediscovered the already known full-activation FEI equivalence.

For the quadratic parity-lift coded core on k+1 bits, H=k, aggregate singleton erasure=0, and I=(k+1)/2. The data-first block has B_W<=12I_W and complete constant 12+2/ln2 for every rarity. For the B05 bent-marker core on k+1 bits, I=k/2+(k+1)2^(-k)>=m/3, yielding B_W<=18I_W and complete constant 18+2/ln2. The bad marker singleton still has logarithmically unbounded erasure/influence ratio. BLOCK_CONTROLS.md gives the all-parameter calculations and distinguishes the substantial core block budget from the bad marker's tiny budget.

This can be consumed by A028/A029/A065/A097 as a concrete proper-block example and by A087/A094 for reconstruction. It does not certify arbitrary parity lifts, hidden arbitrary low-influence tensor cores or general selector trees.

## one next mathematical action and independent reviewer

Derive activation transport for a proper subset of low-density CORE coordinates, retaining the remaining-core Fourier fibers, and identify the shifted empty-core row payment. This changes the selection mechanism instead of repeating the now quantified full-core FEI-strength endpoint. A087 is the nominated independent reviewer; A094 is the alternate. Neither has reviewed this run yet. No messages are sent to them; the saved handoff names the consumers for supervisor copying.

## actual persistence receipts or precise save blocker

All required protocol files, both packet deliverables, frozen specs, proof, source pins, code and exact outputs are saved under this run directory inside A027. STATUS.md has exactly two lines, and WORKLOG.md and LEARNED.md are updated locally. out/PERSISTENCE_RECEIPT.json gives observed file hashes and byte sizes; code/finalize.py checks protocol claim/progress key equality and compatibility-copy equality. No source tree, shared registry or another worker folder was modified. GitHub/Brain copy and independent review are pending the supervisor; local persistence is not reported as mirror verification.

## Universal bridge

This stage moves C019 stopping-tree payment and G-R-SELECT by proving a complete, nonreusing proper-block ledger on an unbounded rare-activation class, including the B05 obstruction and a coded erasure plateau. It also pins the remaining universal payment to an exact defect-spectrum limit, with K+2/C+5 implications, rather than presenting the full-core choice as a universal reduction. What remains is a physically selectable smaller core block or a stopping tree that pays low-density core fibers and all leaves without assuming FEI for them. NEXT targets that exact unpaid row and residual core; it is the shortest continuation of the universal selection route because the current full-core rule's density-free extension is already FEI-strength, so further isolated dense-core classes would not remove the gap.
