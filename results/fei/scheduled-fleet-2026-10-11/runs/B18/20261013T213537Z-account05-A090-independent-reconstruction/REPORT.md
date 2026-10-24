# A090 stage 2: independent low-influence reconstruction and the higher-level frontier

## exact target, quantifiers, hypotheses and units

Verdict HOLDS for B20-ERASURE-LOW-INFLUENCE-COMPLETE v2 (A099). For any finite-valued s:N->[0,infinity) with s(N)=o(N), the supremum K_E(s) of aggregate spectral erasure B(F)/I(F) over all Boolean F satisfying 0<I(F)<=2^-s(N) equals the unrestricted supremum K_E, in the extended reals. No monotonicity of s, nonzero mean condition on the seed, finite universal constant, or exchange of an unproved remainder is assumed. The C018 corollary is C_FEI<=K_E(s)+2/ln2.

New A090 result, proved locally and pending independent review: for every fixed integer ell>=2, the same cutoff-class supremum of R_geell(F)/I(F) equals K_E, where R_geell is the sum of spectral edge entropy costs whose lower endpoint has cardinality >=ell. This retains the OPTIMAL aggregate erasure constant exactly, not just finiteness. All fresh parity coordinates of the hardening family have zero erasure and strictly positive influence, so the selected-coordinate minimum is exactly zero. This result concerns aggregate costs and does not transfer an existential good-coordinate witness.

Uniform cubes, actual Boolean signs, ordinary physical flip influence, entropy in bits, phi(x,y)=(x+y)h2(y/(x+y)), with continuous zero conventions. All dimensions in the proofs are arbitrary finite integers. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read at stage start: BOARD.md dated 2026-10-13 21:34 UTC, B18 STREAM_NOTES v2 (2026-10-11 23:34 UTC), own STATUS.md, and the complete EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2. The older lead target of a five-variable NPN census was superseded by the board's completed A071 census and A082 independent reconstruction; its requested A096 half-tax reconstruction was completed in this agent's first stage. Those facts justify consuming A099's new dependency under the protocol dispatch rule instead of repeating either baseline. This is a freshness correction to dispatch, not a mathematical disagreement with the lead.

The primary target was read first from A099 run 20261012T044129Z-account05-A099-candidate-assembly/CLAIMS.json. Original baseline ERASURE_REDUCTION.md sections 1-6 supplies the actual edge formula, disjoint tensor identities and C018 comparison; their activation consequences are directly reconstructed below. Own prior report was used only as scope context. BLIND_RECONSTRUCTION.md and FROZEN_SPEC.json were saved before opening A099 REFINEMENT_PROOF.md or CANDIDATE_MANUSCRIPT.tex. Those two proof sources were then compared, particularly Theorem thm:low, the exact B0/T12/R_ge2 decomposition and the explicit OPEN-C018-HIGHER conjecture. A096-UNIVERSAL-LEVEL12-ERASURE v1 was read from its claim and the assembled manuscript for frontier context, but is not a premise of the new parity-tail equality and is not independently accepted by this stage. A082 claim metadata was read to verify the existing census/bridge handoff; its finite mathematical result is not used here.

out/SOURCE_MANIFEST.json pins exact byte hashes. Source metadata discrepancy: A099 recorded exact-statement hash 522cb5ec2ed00fe5dfb5b485ea9e77d5eceb0eb3db2dd343f8627442e65b708a differs from UTF8 SHA256 ea6312747c33f095ab6255386e917294d733c4fe3589b1afbe709a810d0a9fec. Both are preserved in the review record; source-file byte hashes pin the actual statement. No hash convention is asserted and no mathematical corruption is inferred. No new browse, brain query, external write, source modification, or repeated five-bit exhaustive search was needed.

## complete derivation or exact first unsupported line

### 1. Independent activation derivation and the checkpoint correction

Let h be any balanced Boolean core on d bits, k>=1, q=2^-k, A_k the all-zero control indicator, and F=1+A_k(h-1). Write core-frequency S and control-frequency U. The normalized Fourier coefficients are

    a_F(empty,empty)=1-q;
    a_F(empty,U)=-q for U nonempty;
    a_F(S,U)=q ahat(S) for S nonempty, all U.

Signs of control coefficients for another activated vertex do not change the squared spectrum. Edge entropy is homogeneous: phi(tx,ty)=t phi(x,y). At a core coordinate i, partition edges by residual core index T. For T nonempty, all 2^k control slices reproduce q^2 times the core cost. At T empty, the core cost was phi(0,ahat(i)^2)=0, but the nonempty control slices have masses q^2 and q^2 ahat(i)^2, and the empty slice has masses (1-q)^2 and q^2 ahat(i)^2. Thus exactly

    B_data(F)=qB(h)
       +q(1-q)sum_i phi(1,ahat(i)^2)
       +sum_i phi((1-q)^2,q^2 ahat(i)^2) >=qB(h).       (1)

A090's provisional checkpoint equality omitted the first correction sum. Comparison with A099 exposed the omitted pure-control slices, and CHECKPOINT_CORRECTION.md immediately saved the correction. A099's displayed formula includes both sums and needs no repair. The statement-only LOWER BOUND, and therefore the independently reconstructed theorem, survive. This report uses the corrected exact identity throughout; no claim of complete correct checkpoint algebra is made.

For each control coordinate j, the exceptional pair is ((1-q)^2,q^2), and every other occupied pair has equal squared masses. Queried influence is q, with q^2 in the exceptional pair. Therefore

    B_j(F)=2q(1-q)+phi((1-q)^2,q^2),  Inf_j(F)=q.    (2)

Each core influence is q times its original value. Direct pivotal counting gives the same formula, since the other k-1 controls are active with probability 2q and balanced h is negative with probability 1/2. Consequently

    I(F)=q[I(h)+k].                                  (3)

### 2. A099 v2 independently reconstructed, including oscillatory cutoffs

For nonconstant f on n>=1 bits, take m disjoint copies and h=z product_b f(x^(b)) with one fresh parity bit. The squared Fourier law is a product, so B(h)=mB(f), I(h)=mI(f)+1 and E h=0. Equations (1)-(3) imply

    B(F)/I(F)>= mB(f)/(mI(f)+1+k).                    (4)

Here is an independent choice of k that handles arbitrary oscillations in s without the author's initial-segment maximum. Let

    eta_m=sup_{N>=mn} s(N)/N.

Because s(N)/N->0 and every value is finite, eta_m is finite and tends to zero. For any fixed parity count ell>=1 choose

    k_m=ceil[4(n+1)m sqrt(eta_m)+2sqrt(m)],
    N_m=mn+ell+k_m.                                  (5)

Then k_m=o(m), k_m<=m eventually, and ell<=m eventually, so N_m<=(n+2)m. Since N_m>=mn and eta_m<=1 eventually,

    s(N_m)<=eta_m(n+2)m
           <=4(n+1)m sqrt(eta_m),
    k_m-s(N_m)>=2sqrt(m).                            (6)

Also I(f)<=n and mI(f)+ell+k_m<=(n+2)m eventually. Since log2((n+2)m)=o(sqrt(m)), (6) gives

    0<I(F_m)=2^-k_m[mI(f)+ell+k_m]<=2^-s(N_m).        (7)

Taking ell=1 in (4)-(7), the lower ratio tends to B(f)/I(f). Therefore K_E(s)>=B(f)/I(f) for every nonconstant seed. Supremizing gives K_E(s)>=K_E; the opposite inequality holds by class inclusion. This argument also handles infinite K_E: for every arbitrarily large finite seed ratio, an admissible sequence approaches it. No finiteness assumption or unproved exchange of limit and supremum is used. This establishes A099's exact v2 statement and, by the already reconstructed C018 comparison, its C_FEI corollary. Constants have B=I=0 and need no ratio.

### 3. New exact tail transport, all fixed ell>=2

Replace the one balancing bit by a fresh parity of ell>=2 bits:

    h=chi_Z product_b f(x^(b)),  |Z|=ell.

Every occupied Fourier set of h contains all of Z. Thus h is balanced and all its singleton Fourier coefficients vanish. Its aggregate erasure is still mB(f), its influence is mI(f)+ell, and its fresh parity coordinates have zero erasure. In (1) both correction sums now vanish exactly:

    B_data(F)=q mB(f).                               (8)

For an original seed coordinate, every nonzero-cost data edge has both endpoints containing Z. Its lower endpoint therefore has size at least ell, in every control slice. Each fresh parity coordinate has no adjacent occupied Fourier sets, including the exceptional empty-frequency row, because ahat(i)=0. Hence

    R_geell,data(F)=q mB(f),
    B_z(F)=0, Inf_z(F)=q>0 for every z in Z.          (9)

No parity frequency is treated as a change of physical basis: these are actual fresh coordinates and their influence overhead is explicitly retained.

The control part has a particularly simple exact tail count. Pairs with nonempty core S contribute kq in total and all have lower endpoint size >=ell. Pairs with empty core and a lower pure-control subset of size r>=ell have equal masses q^2. Their number is k*binom(k-1,r). Therefore

    R_geell(F)=q mB(f)+kq
      +2kq^2 sum_(r=ell..k-1) binom(k-1,r),           (10)

where the sum is zero for ell>k-1. In particular

    B0(F)=k phi((1-q)^2,q^2),
    T12(F)=2k(k-1)q^2,
    R_ge2(F)=q mB(f)+2kq(1-kq).                      (11)

Formula (11) also follows by subtracting the exact first two layers from (2),(8). It applies to every ell>=2, every actual seed, all m,k>=1. The extra cost is nonnegative because k2^-k<=1/2.

For nonconstant f, taking k_m from (5) yields admissible cutoff functions, k_m/m->0 and

    R_ge2(F_m)/I(F_m)
       =[mB(f)+2k_m(1-k_m2^-k_m)]
          /[mI(f)+ell+k_m] -> B(f)/I(f).             (12)

For general fixed ell, (9) gives the same lower limiting ratio and R_geell<=B supplies the upper supremum comparison. Thus, defining K_geell(s) over the cutoff class,

    K_geell(s)=K_E(s)=K_E (extended reals).           (13)

The fresh parity bits prove at the same time

    min_(i:Inf_i(F)>0) B_i(F)/Inf_i(F)=0,             (14)

exactly, independent of the seed aggregate ratio. This prevents falsely identifying (13) with a selectable-coordinate-hardness assertion. Formula (13) sharpens the assembly's additive layer comparison: deleting any fixed number of low Fourier layers and imposing arbitrary subexponentially small influence preserves the OPTIMAL aggregate-erasure supremum without additive loss. This is an extraction of full-FEI-strength hardness, not a payment theorem.

### 4. First unreconstructed universal implication

The source v2 theorem is reconstructed completely. The assembly's first unsupported universal payment is its explicit OPEN-C018-HIGHER conjecture:

    exists one finite K, for every actual Boolean f:
        R_ge2(f)<=K I(f).                            (OPEN)

No argument in the assembled manuscript closes it. The new (13) shows even its restriction to the low-influence cutoff class has optimal constant K_E. A097's reference identities, paid B0/T12 layers, and existing bounded-ratio B05 example do not constitute this missing all-dimensional payment. No full-chain acceptance of A099's separate B05 certificate application, A097 reference application, or history-specific C024 is issued here. The review accepts exactly the low-influence fragment and honestly isolates the remaining universal line.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before computation: all 22 truth tables on n=0,1,2, and four fixed n=3 masks 1,7,105,150; tensor count m=1,2; controls k=1,2,3; fresh parity count ell=1,2; 312 labelled activation functions, no symmetry quotient. Maximum ambient dimension 11. Helper uses an independent integer FWHT, Fraction masses/influence, and formal rational logarithm argument/coefficient dictionaries. Exact cancellation verifies entropy identities without numerical log signs. Memory estimate <80 MB, runtime guard 60 seconds; no heavy job or memok requirement was triggered.

Command from A090: python -X utf8 runs/20261013T213537Z-account05-A090-independent-reconstruction/code/check_transfer.py.

Initial v1 checker: PASS 3,952 assertions, 312 cases, 2.3080586 seconds. After deriving (11), SPEC_REVISION.md froze the additional identity checks on the unchanged domain. Final v2 checker: PASS 4,420 exact assertions, 312 cases, 1.7891364 seconds, saved in out/CHECK.json. The rerun was justified by new equations B0,T12,R_ge2, not additional precision or a larger census. Exact checks cover corrected one-parity extra rows, actual parent Parseval, tensor B, individual influences, control entropy formula, two-parity data/tail equality and both zero-erasure relevant bits. Analytic proofs, not finite tests, justify arbitrary m,k,ell,n and all cutoff functions s.

## proof dependencies and changed downstream conclusions

A099 B20-ERASURE-LOW-INFLUENCE-COMPLETE v2 is independently accepted at its exact stated scope. The reconstruction uses finite character sums, homogeneity of edge entropy, product-law tensorization, physical pivotal accounting and elementary sublinear asymptotics. Source B20 tensor/activation formulas are rederived; their existing pending metadata is not assumed as proof. C018 is used only for the C_FEI corollary and has the original self-contained source pin. The new higher-level transport requires no A096 T12 bound, no threshold/percolation theorem, and no universal FEI assumption.

A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS v1 is a new author-proved refinement, pending A094/A085 independent review. A090 is its mathematical contributor and does not independently accept its own new claim. A099/A096 can use it conditionally to focus the remaining normalized derivative reference on simultaneous unbounded levels, rather than treating fixed-level deletion or tiny total influence as structural exclusion. A005/A089 must retain the aggregate-versus-selectable distinction demonstrated by (14). Existing five-bit census and the already accepted singleton tax remain retired; no changes to other agents' outputs or shared ledgers were made.

## one next mathematical action and independent reviewer

Next: audit a source-complete proposed normalized derivative reference for R_ge2 on the two-parity arbitrary-tensor activation family. Require a single physical influence ledger and retain arbitrary terminal core entropy; test whether the reference reconstructs the original seed bill in (11)-(12), rather than silently excluding it by low influence or low-layer payment. Independent reviewer A094, alternate A085. Intended consumers A099/A096/A064 and B18/B20. This consumes the exact unpaid layer from the live assembly; another finite census or fixed-level estimate would not pay it.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json are saved in the assigned stage run, with code and out directories. Supporting files include BLIND_RECONSTRUCTION.md, CHECKPOINT_CORRECTION.md, RECONSTRUCTION_COMPARISON.md, PARITY_TAIL_PROOF.tex, FROZEN_SPEC.json, SPEC_REVISION.md, the independent checker, exact output, source manifest and receipt/schema validation. STATUS.md, WORKLOG.md and LEARNED.md are current inside A090 only. Local SHA256 receipts verify persistence; supervisor copy, GitHub/brain mirror, shared-index adoption, downstream use and independent review of the new refinement remain outstanding.

## Universal bridge

This stage moves C018 by independently accepting A099's loss-free aggregate low-influence completeness and proving an exact new remaining-level transport: for every fixed ell>=2 and every sublinear cutoff s, sup R_geell/I on that class equals K_E, with R_ge2=q mB(seed)+2kq(1-kq) and zero-erasure relevant parity coordinates. It reduces no universal constant and pays no higher-layer debt; the finite dimension-independent R_ge2<=KI estimate remains open. The shortest NEXT is an audit of one terminal-inclusive normalized reference for that very bill on arbitrary-tensor activations, because the exact formulas expose the original arbitrary seed cost and prevent another isolated low-level or low-influence result from being mistaken for full FEI.
