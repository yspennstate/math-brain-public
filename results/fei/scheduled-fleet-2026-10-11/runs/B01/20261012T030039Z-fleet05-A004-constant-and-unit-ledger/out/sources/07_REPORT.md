# exact target, quantifiers, hypotheses and units

A002 / B01, stage 2, run 20261011T234442Z-fleet05-A002-hardness-preserving-transformations. The lead's explicit target is the erasure-fraction admission problem: given every arbitrary seed f, produce actual Boolean F_m with B(F_m)/H(F_m)->1 and H(F_m)/I(F_m)->H(f)/I(f), or prove an appropriate structural restriction on near-one erasure. Here B=sum_i H(S_i|S_-i), H is squared Fourier entropy in bits, and I=sum_i Pr(i in S). Physical inputs remain independent uniform signs. D=H-B is dual total correlation; TC=sum_i h2(I_i)-H is different.

This stage completes an exact aggregate-B ledger and a mechanism audit. It does NOT solve arbitrary high-ratio near-one-erasure admission. The [ERASURE_LEDGER.md](ERASURE_LEDGER.md) gives all derivations, the exact obstruction to paid bent dilution, a Boolean counterfamily to unjustified product-law stability, and a sharper universal implication from a hypothetical near-erasure class bound. Positive-entropy seeds are used when dividing by H; zero-entropy seeds have ratio zero and are treated separately.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage start (23:39 UTC snapshot, including all B01-B20 sections), B01 STREAM_NOTES v1 dated 22:40Z, own STATUS and LEARNED. The now-present lead notes direct this stage; there is no disagreement with the mathematical target. Read lead run 20261011T225200Z CLAIMS.json, especially B01-ERASURE-FRACTION-BRIDGE@1, B01-MINIMAL-VIOLATOR-STRUCTURE@1 and the OPEN B01-PRODUCT-LAW-RIGIDITY. Its REPORT was unavailable in the harness; proof-source placeholders in the claims are not treated as a saved report.

Read A005's 20261011T225209Z REPORT, sections 3-5: data/control erasure formulas and the distinction between H/I admission and witness transport. Its formulas overlap the coordinate part of this task. They are independently checked here and consumed as known interfaces; new progress is their aggregation into B/H transport, the Pareto obstruction, and the sharpened near-erasure universal implication. Read A079's 20261011T224806Z report for its bent-row conditional remainder and rare-tag scope; do not relabel its B_X as aggregate B or repeat its conditional admission.

Read supplemental sources/ERASURE_RIGIDITY.md sections 1-2 in full. Its complete dyadic divisibility proof already resolves exact product-law rigidity, although the lead's local claim still labels that statement OPEN. This stage reconstructs that existing proof independently and records the correction for source-bound adoption, without claiming a new theorem or modifying the lead's files. Also read prior own stage-1 ledger and proof package; the completed H/I baseline is not reopened.

The execution protocol remains fei-execution-protocol/2, 2026-10-11-execution-v2. [out/SOURCE_MANIFEST.json](out/SOURCE_MANIFEST.json) pins actual local inputs and the scope of their use. No literature novelty claim, new internet source, or unrelated paper theorem is used. Original source trees and all other agent folders remain read-only.

# complete derivation or exact first unsupported line

For probabilities x,y, let E(x,y)=phi(x)+phi(y)-phi(x+y), phi(x)=-x log2 x. B_i is the sum of E along coordinate-i spectral edges. Homogeneity supplies the new ledger. Disjoint tensors add B; fresh balancing preserves B; character multiplication and dummy padding preserve B. A systematic parity code has B=sum_(columns zero) B_i(seed); every auxiliary B_i is zero. Parity lift and all distance>1 coded constructions have B=0.

General point activation of h with mean a, d=1-a, controls s, p=2^-s, c=(1-pd)^2 and q_i=hat h({i})^2 gives

    B_data,i = p[B_i(h)-E(a^2,q_i)] + p(1-p)E(d^2,q_i)+E(c,p^2q_i),
    B_control = p(1-a^2)+(p-2p^2)d^2+E(c,p^2d^2).

The proof partitions all spectral edges into nonempty retained-data edges, nonempty control edges at empty data, and the exceptional constant edge. For a balanced b^tensor m, m>=2, singleton coefficients vanish, hence

    B(activation)=pmB(b)+s[2p-2p^2+E((1-p)^2,p^2)].

With economical s=ceil(2log2 m), B/H tends to B(b)/H(b), preserving rather than inflating the seed fraction. Control-dominated activation has limiting fraction 1/2. The selector formula is

    B(M_g)=B(g)/2 + (1/2)sum_i E(1,hat g({i})^2).

For g=z f^tensor m only the singleton {z} is possible, of mass (Ef)^(2m), so B(M_g)=mB(f)/2+E(1,(Ef)^(2m))/2. Therefore its fraction also tends to the seed's. The labels have zero erasure because each spectral set contains exactly one leaf label. These are aggregate-B conclusions beyond the retired H/I ledgers.

The strongest direct mixing repair tested is adding a fresh bent factor. For F=f^tensor m times bent b_r on 2r variables,

    H=mH(f)+2r, B=mB(f)+2r, I=mI(f)+r, D=mD(f).

Let R=H(f)/I(f), eta=D(f)/H(f)>0 and epsilon_F=D(F)/H(F). Then exactly

    H(F)/I(F) = 2/[1+(2/R-1)epsilon_F/eta].

Forcing B/H->1 forces ratio ->2 and cannot preserve a fixed seed ratio >2. More generally, tensoring any auxiliary with H/I<=C cannot preserve a seed ratio >C in that limit. This is an obstruction to this specified mechanism, not to every Boolean admission map. For seed ratios <=2, paid bent dilution plus a tuned deterministic parity does achieve both requested limits, and keeps a physical seed tensor. It pays dominant entropy/influence overhead; the unsolved case begins with ratios >2. The three-bit one-point defect is an exact such seed, with H=4-(9/8)log2 3, I=3/4 and D=1-(15/8)log2 5+(18/8)log2 3>0. Integer inequalities certify both H>2I and D>0.

Exact B=H implies a product spectral law, and Boolean dyadic rigidity then forces marginals in {0,1/2,1}, a character times a bent sign on an even coordinate subset, and H<=2I. This source-complete endpoint is already proved in ERASURE_RIGIDITY section 1. It does not extend quantitatively merely by continuity.

Indeed a concrete Boolean family is c_t times b_r, where c_t=(-1)^(uv) and u,v are parities of disjoint t-bit blocks, t>=2. Its dimension is 2t+2r, mean 2^(-(r+1)), and

    H=2+2r, B=2r, D=2, I=t+r,
    TC=2t-2, TV(P,product_i P_i)=1-2^(2-2t).

Take t=r^2, r>=2. Then B/H->1 but TC/H->infinity and TV->1. Thus near-one erasure does not force dimension-independent closeness to the product of spectral marginals, even for actual Boolean spectra. This low-ratio family pays its dependence with ample physical influence; it is not a counterexample to FEI or to a near-erasure H/I theorem.

Finally, if one fixed epsilon in (0,1) admits a bound H<=C_epsilon I on B>=(1-epsilon)H, then full FEI follows with constant **max(C_epsilon,2/(epsilon ln2))**, improving the additive C_epsilon+2/(epsilon ln2) inference from the erasure-fraction endpoint. Proof: a minimal-variable violator at C has all physical children certified. For delta=H-CI>0, every coordinate gives B_i>=(C-2/ln2)I_i+delta. Summation gives D<(2/ln2)I. Since its ratio exceeds C>=2/(epsilon ln2), it lies in the near-one class, contradiction. Constants and irrelevant coordinates are handled explicitly. The proof retains child deficits rather than assuming the near-one class is restriction closed.

First unsupported line: a fixed-epsilon, dimension-independent H/I bound on the near-one class, or a different actual Boolean transformation that inflates B/H without diluting a seed ratio above two. No such high-ratio admission or quantitative Boolean stability estimate is proved. This honest gap is the continuing universal target; no finite counterexample to a candidate constant is labeled a disproof of FEI.

# executed validation with domain, arithmetic, commands and outputs

[out/FROZEN_SPEC.json](out/FROZEN_SPEC.json) was saved before the search/checker. Pilot uses all 22 labelled signs through n=2; full fixed domain uses all 278 labelled signs through n=3. Additional checks cover all six balanced two-bit seeds, tensor count 2 or 3, controls 1,2,3 (36 cases), and four correlated-block cases t=2,3 and r=1,2, maximum dimension ten. No symmetry reduction, stochastic search, GPU, automatic dimension escalation or heavy job. Estimated memory is 60 MB, so the >300 MB gate is not applicable.

The checker uses an integer FWHT of actual truth tables and Fraction amplitudes/probabilities. H and B equalities are rational linear combinations of logarithms of primes. Point activation, general selectors, coded edge erasure, bent tensor invariants and correlated-block total variation are checked exactly. The pilot passed 1,224 assertions with zero failures in about 0.22 seconds. The full check passed 12,232 assertions with zero failures in about 8.02 seconds. Full results appear in [out/EXACT_CHECK_n3.json](out/EXACT_CHECK_n3.json). [out/SIGN_CERTIFICATE.json](out/SIGN_CERTIFICATE.json) proves H>2I via 3^9<2^20 and D>0 via 2^8*3^18>5^15 for the point-defect seed. No floating entropy approximation certifies a sign or universal conclusion.

Commands from A002:

```text
python -X utf8 runs/20261011T234442Z-fleet05-A002-hardness-preserving-transformations/code/check.py --nmax 2
python -X utf8 runs/20261011T234442Z-fleet05-A002-hardness-preserving-transformations/code/check.py --nmax 3
python -X utf8 runs/20261011T234442Z-fleet05-A002-hardness-preserving-transformations/code/finalize.py
```

Finite exact identities validate implementations. The all-dimensional formulas, limiting mechanism obstruction and universal implication are analytic proofs, not extrapolations from the finite domain. No Lean/PDF build or independent reviewer execution is claimed.

# proof dependencies and changed downstream conclusions

The aggregate ledger independently reconstructs the coordinate activation interface from A005 and uses the stage-1 H/I spectra as known inputs. Tensor, balancing and systematic-code B transport depend only on spectral edge adjacency. The Pareto obstruction and correlated Boolean counterfamily are source-complete applications of that ledger, not new broad universal-payment candidates. The sharpened implication uses the scalar JS restriction bound and minimal-violator reasoning independently reconstructed from the lead's versioned claim. No FEI conclusion is an unconditional premise.

For B01: mark the exact product-law rigidity source as already proved, but keep its quantitative near-one extension OPEN. A003/A005 should distinguish B/H transport from H/I transport and should not infer that rare activation increases the erasure fraction. A030/A078 coding can make every local erasure zero; it cannot serve this near-one admission. A051/A055 can use the minimal-violator quantitative localization with full child deficits. A031/A033 and B08 should use full Boolean phase/energy when attempting near-one stability; closeness to the product of marginals is refuted as a necessary consequence. A079's conditional row guard is distinct from this aggregate-B task.

# one next mathematical action and independent reviewer

Next: attack the lead's near-erasure bound **only on minimal-variable high-ratio witnesses**, where every physical child has nonpositive C-deficit and D<(2/ln2)I; test a signed-Booleanity argument linking that child certification to a dimension-independent D lower bound. This adds a genuine structural hypothesis beyond the false near-product shortcut and avoids building another paid dilution gadget. Reviewers A086/A094 should reconstruct the aggregate edge ledger and Pareto identity; A087 or A090 should independently reconstruct the sharpened minimum-counterexample implication. These are saved handoffs, not messages sent or completed reviews.

# actual persistence receipts or precise save blocker

The four protocol files, code/, out/, ERASURE_LEDGER.md and scoped hypothesis/admission record are saved in this A002 run only. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated locally. out/SOURCE_MANIFEST.json and out/ARTIFACT_RECEIPTS.json record input/output byte hashes; out/SCHEMA_CHECK.json verifies fields, statement hashes, file sizes and byte-identical packet compatibility. No shared tree, another agent file, board, lead notes, brain database, git repository, scheduler, trading folder or external service was modified. Independent review, supervisor copying, mirror verification and downstream adoption remain unclaimed.

## Universal bridge

This stage advances C018 through the lead's erasure-fraction target: it adds exact B transport to all conventional H/I admission maps, proves that bent inflation loses every seed ratio above two, rules out near-product closeness as a necessary structural conclusion, and sharpens the hypothetical near-one-class-to-FEI constant from C_epsilon+2/(epsilon ln2) to max(C_epsilon,2/(epsilon ln2)). No universal erasure constant has been bounded. What remains is the quantitative Boolean near-erasure payment on actual high-ratio minimal witnesses. NEXT targets their already certified physical children and D<(2/ln2)I, which is the shortest available route to the universal bridge because it uses the contradiction structure needed for full FEI rather than another isolated low-ratio class.
