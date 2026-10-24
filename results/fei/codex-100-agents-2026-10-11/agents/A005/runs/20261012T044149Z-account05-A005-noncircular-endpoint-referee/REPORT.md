# exact target, quantifiers, hypotheses and units

A005/B01 stage 2, noncircular endpoint referee. Full FEI is OPEN. This stage consumes the new B01 minimal-violator dependency rather than repeating the stage-1 activation witness obstruction. All functions are actual finite uniform Boolean signs; H is squared-Fourier Shannon entropy in bits, I total physical influence, B=sum_i H(S_i|S_-i), and D=H-B is dual total correlation. Dimension n always counts RELEVANT coordinates; dummy padding is excluded.

The endpoint under audit is a C-violator f (H(f)>CI(f)) whose one-coordinate children are certified at the SAME finite C>=0. This is the stronger structural endpoint used by the lead and A002's near-erasure bridge. We also distinguish the weaker hypothesis that each pair of children is certified only on average. The assignment is to decide whether an arbitrary seed of ratio R>C can enter this endpoint through a diverging-dimension ratio-preserving embedding, and otherwise identify the precise obstruction.

Result: such an embedding is impossible, even with only average child certification. The obstruction is quantitative: n<=1+(2/ln2)/(H/I-C). This is an endpoint admission obstruction and a review of existing reduction claims, not a new universal entropy payment. The original universally quantified same-parameter low-influence good-coordinate implication remains OPEN; no impossibility for every alternative reduction is asserted.

# sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot 2026-10-12 04:39 UTC, B01 STREAM_NOTES v1 dated 2026-10-11 22:40Z, own STATUS/LEARNED and the complete execution protocol revision 2026-10-11-execution-v2. The stream lead's notes have not changed since the prior stage; new productive dependencies come from the board and saved source artifacts. out/SOURCE_MANIFEST.json pins 26 current input artifacts and the reused exact arithmetic helper by SHA256.

New sources inspected:

- B01 lead run 20261011T225200Z CLAIMS.json, B01-MINIMAL-VIOLATOR-STRUCTURE@1 and related erasure-fraction claims. Its REPORT was blocked in the harness; this stage supplies a complete independent proof, not a claim to have read unavailable text.
- A002 stage 2 run 20261011T234442Z, REPORT, ERASURE_LEDGER section 4 and CLAIMS: A002-NEAR-ERASURE-MAX-CONSTANT-BRIDGE@1. The maximum-constant implication is independently reconstructed here; its open premise is kept open.
- A003 stage 2 DERIVATION sections 3-4 and A075 stage 1 REPORT equations (1)-(3). They already prove the balanced-encoder collision formula and the majority bound. An initially considered diffusion mechanism was retired BEFORE computation because it would duplicate those results.
- A027/A028 stage 2 reports: complete path/terminal transport and arbitrary-controller endpoint. Their new quantitative constants are scope/context only, not proof premises. A030's plateau report and A051's descent squeeze likewise establish where arbitrary terminal entropy or the original ratio remains unpaid.
- B20 SYNTHESIS: avoid duplicating good-coordinate equivalences, root benchmarks and already retired half-tax/minimum-ratio searches.

ERASURE_REDUCTION sections 1-4, read and pinned in the prior stage, supplies the physical entropy/influence interface; it is reconstructed below. No new literature claim, internet premise, brain write or shared-index edit is used. The earlier broad H/I hardening baseline and exact product rigidity are not reopened.

# complete derivation or exact first unsupported line

Complete proof: [DERIVATION.md](DERIVATION.md). The mathematical delta is its signed slack conservation identity, its mechanism-independent admission obstruction, and the exact distinction between individual and average child certification.

For fixed C>=0 let delta=H-CI and let

    sigma_i = average_s [C I(f_i,s)-H(f_i,s)]

be the signed average child slack. Every individual child certified implies sigma_i>=0, but the converse is false. Physical influence recursion and the entropy restriction identity give

    Delta_i H = C Inf_i + delta + sigma_i,
    B_i = C Inf_i + delta + sigma_i - JS_i,
    D + (n-1)delta + sum_i sigma_i = sum_i JS_i.              (1)

This exact identity holds WITHOUT any child certification assumption. In particular negative sigma_i cannot be silently spent as a reserve. Put mu_i=sum_T min(p(T),p(T+i)). The scalar bound is JS_i<=(2/ln2)mu_i and mu_i<=min(Inf_i,1-Inf_i). To reconstruct the scalar interface, set z=2|uv|/(u^2+v^2). The packet divergence in natural units is (u^2+v^2)d(z), where d(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2. Since d'(z)=atanh(z)<=z/sqrt(1-z^2), integration from zero gives d(z)<=1-sqrt(1-z^2). Consequently the packet is at most (2/ln2)min(u^2,v^2). Summing proves the stated bound.

Assume delta>0 and all sigma_i>=0. D>=0 follows from conditioning reducing entropy and the chain rule. Therefore n>=2 and

    D + sum sigma_i + (n-1)delta
       <= (2/ln2) sum mu_i <= (2/ln2) I,
    0 < H/I-C <= (2/ln2)/(n-1).                             (2)

Thus no sequence of actual Boolean functions F_m can simultaneously satisfy n_m->infinity, H(F_m)/I(F_m)->R>C and certification of all average children at the SAME C. If C varies, necessarily C_m>=R_m-(2/ln2)/(n_m-1), hence liminf C_m>=R. This conclusion applies to every embedding with these output properties, not just activation, tensoring or diffusion. Relevant dimension is essential: adding dummy coordinates does not evade the theorem.

It does not follow that the child-certified endpoint is logically weaker or useless. If ANY C-violator exists, one with the fewest relevant variables exists and all its individual children are certified. Ruling out such witnesses would prove FEI(C) at the SAME C. However an arbitrary larger-gap seed cannot simply be carried into this endpoint while keeping its ratio and sending relevant dimension to infinity. Restriction extraction preserves a positive deficit, not a promised original ratio or fixed gap.

## Independent reconstruction of B01-MINIMAL-VIOLATOR-STRUCTURE@1: HOLDS

With all individual children certified, sigma_i>=0. Equation (1) gives Delta_i>=C d_i+delta>r d_i, because r=H/I=C+delta/I and n>=2 implies d_i<I. Hence B_i>(r-2/ln2)d_i. The entropy bound B_i<=h2(d_i)<=d_i log2(e/d_i) yields d_i<e^3 2^-r. Summation gives D/I<2/ln2 and more precisely D/I<=2/ln2-(n-1)(r-C), as in the original claim. It also yields B/H>1-2/(r ln2). Well ordering of relevant dimension establishes the least-violator hypothesis when any violator exists. This reconstruction uses the exact signed slack identity rather than the lead's numerical calibration. No repair to the original statement was needed; the original statement hash is retained in the local review record.

## Independent reconstruction of A002-NEAR-ERASURE-MAX-CONSTANT-BRIDGE@1: HOLDS

Fix epsilon in (0,1) and suppose H<=C_epsilon I on every Boolean function satisfying B>=(1-epsilon)H. Put C=max(C_epsilon,2/(epsilon ln2)). If FEI(C) fails, choose a least-relevant-dimension violator. Its children are certified; by (2), D<(2/ln2)I. Since H/I>C>=2/(epsilon ln2), D/H<epsilon. Thus the violator lies in the hypothesized near-erasure class and satisfies H<=C_epsilon I<=CI, a contradiction. The reverse direction is subset inclusion. The near-erasure class need not be restriction closed. The existing conditional bridge is accepted at that scope; NO universal bound for its premise is supplied. The new child-certification admission obstruction explains why a direct arbitrary-seed embedding is not the same proof as this minimality argument.

## Exact tensor loss of child certification

For any fixed seed f and C, let delta_0=H(f)-CI(f). Tensor independence gives

    delta(f^tensor m)=m delta_0,
    sigma_(copy,i)(f^tensor m)=sigma_i(f)-(m-1)delta_0.        (3)

If delta_0>0, every average child is eventually a violator. All one-copy decrements and JS payments are unchanged, while the root surplus grows. The final aggregate version is also exact:

    sum sigma(f^tensor m)
       =m sum sigma(f)-mn(m-1)delta_0,

where n is the seed's relevant dimension. The negative term accounts for the loss of child certification; it is not another influence budget.

Actual seed: the three-bit one-point defect has H=4-(9/8)log2 3, I=3/4 and each d_i=1/4. At C=8/3 it has delta_0=2-(9/8)log2 3>0. Its active child is the two-bit point defect, H=2,I=1; its other child is constant. Therefore sigma_i=1/3. Exact rational intervals certify

    1/6 < delta_0 < 1/3.

At m=1 both individual and average certification hold. At m=2, sigma_i=1/3-delta_0>0 for every coordinate, but individual certification fails: the constant branch leaves an untouched violating seed copy. At m=3 and m=4 every sigma_i<0, so average certification also fails. The frozen checker reconstructs actual truth tables and every child spectrum through twelve physical variables.

The rational certificate also proves R_seed-8/3>(2/ln2)/10, with outward lower margin 24062852687/35184372088832>0. Consequently no Boolean function on n>=11 RELEVANT inputs with ratio at least this seed's can have all average children certified at C=8/3. This is an all-dimensional consequence with an exact numerical threshold; it is not an exhaustive eleven-bit census or a disproof of FEI.

First unsupported universal line: prove an absolute-C signed Boolean inequality excluding a positive delta with all sigma_i>=0 while retaining (1)'s complete erasure/JS debt. Equation (1) and the admission obstruction alone do not pay that debt. Likewise, the previously open same-parameter implication for a UNIVERSALLY quantified low-influence selectable criterion is not settled by this audit. A proof request to B01/A002/A055 is now precise: supply the child-certified near-erasure exclusion, or an endpoint transfer that explicitly permits and pays the loss of the original ratio gap. Asking for another diverging-dimension ratio-preserving child-certified embedding contradicts (2).

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before the pilot. The fixed full domain contains all 278 labelled Boolean tables for n=0,1,2,3, each at C in {0,5/2,8/3,3}, tensor powers m=1,2,3,4 of the explicit three-bit defect at those four C values, and one baseline seed record: 1,129 root/C cases. No symmetry quotient, random search, n=4 census, automatic dimension escalation or GPU. Maximum direct truth-table dimension is twelve; estimated memory 80 MB, below the 300 MB gate.

Pilot domain: all 22 n<=2 tables at the same four C values, tensor m=1,2 and the baseline, 97 cases. The first pilot caught a wrong analytic fixture for the active two-bit child: its H and I had been halved twice. The conservation identity had passed; the independent actual child spectra correctly disagreed with the tensor expected slack. out/PILOT_FAILURE.json records the original error, exact correction and unchanged frozen domain. DERIVATION and the fixture were corrected before any claim was created. Corrected pilot: 837 exact assertions, zero failures, 0.076 seconds.

Full run: 14,961 assertions, zero failures, 14.508 seconds, below the frozen 60-second ceiling. out/FULL_VALIDATION.json includes the exact tensor slack signs, individual-certification flags, seed ratio interval and dimension-obstruction margin. The recorded 67 individually certified and 68 average-certified violator root/C cases are just fixtures in this declared domain, including repeated baseline/tensor cases; they are not distinct-function census counts or extremal claims.

The checker uses integer FWHT/Fraction spectra, independent physical edge counts, actual child truth tables, direct packet JS and spectral marginals for D. Entropy equalities are exact rational log-prime vectors. It verifies (1), every physical influence recursion and (3). The exact arithmetic helper from the prior A005 run is source-loaded WITHOUT executing its old writers or creating bytecode in that immutable run; its SHA256 is frozen. The lead's floating calibration code is not reused.

Strict signs use ln(r)=2 sum_(j=0..39) z^(2j+1)/(2j+1)+R for 1<=r<=2, z=(r-1)/(r+1), with 0<=R<=2z^81/[81(1-z^2)]. Binary range reduction and positive ln2 division preserve enclosure; arithmetic rounds OUTWARD to dyadic denominator 2^48. Threshold signs and child classifications use Fraction comparisons. No floating result is used to accept an inequality.

Commands from A005:

    python -X utf8 runs\20261012T044149Z-account05-A005-noncircular-endpoint-referee\code\intake.py
    python -X utf8 runs\20261012T044149Z-account05-A005-noncircular-endpoint-referee\code\check.py pilot
    python -X utf8 runs\20261012T044149Z-account05-A005-noncircular-endpoint-referee\code\check.py full
    python -X utf8 runs\20261012T044149Z-account05-A005-noncircular-endpoint-referee\code\finalize.py

No heavy/background process, Lean certification or new literature priority result is claimed. The universal statements follow from the displayed proofs, not from extrapolating the finite test.

# proof dependencies and changed downstream conclusions

The proof uses Boolean physical influence recursion, exact Fourier restriction identities, conditioning/chain rule and the reconstructed scalar JS bound. B01-MINIMAL-VIOLATOR-STRUCTURE@1 and A002-NEAR-ERASURE-MAX-CONSTANT-BRIDGE@1 are independently accepted at their original scopes in this local handoff, with unchanged statement hashes. The new admission obstruction consumes the former only after reconstruction; it is a narrow corollary plus a signed-slack interface, not a new broad universal candidate beyond the B01 review cap.

For A002/A003/A051/A055/B01: the critical-child endpoint excludes arbitrary fixed-gap seeds at unbounded relevant dimension. Do not infer seed-ratio admission from minimal-violator existence. Average child certification is weaker than certifying every branch, as the six-bit tensor witness proves. For A027/A028/A029/A064/A097: sigma_i is signed and can become negative under amplification; a claimed reserve must specify its actual children, sign and exclusive influence account. The surviving near-erasure bridge is a minimality reduction, not a hidden proof that its open class bound is paid. B20 may adopt the two reviews and the nonadmission theorem from this source-bound package; no shared claim status was changed by A005.

# one next mathematical action and independent reviewer

Next: attack the signed Boolean near-erasure payment ONLY on actual child-certified C-violators, using the tighter complete bank D+(n-1)delta+sum sigma_i=sum JS_i and the point-defect tensor signs as controls. A005 should audit any claimed universal structural exclusion at its first unpaid line, rather than ask for the now-impossible fixed-gap admission family. A094 should independently reconstruct the new obstruction and exact threshold; A087 should challenge average versus individual certification and the signed reserve. These are saved reviewer/consumer handoffs, not external messages or claims of completed review of the new corollary.

# actual persistence receipts or precise save blocker

REPORT.md, DERIVATION.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, code/ and exact out/ records are saved only in the designated A005 stage directory. Rolling STATUS.md is two lines; WORKLOG.md is appended with the stage and pilot correction, and LEARNED.md records durable mathematical statements. out/SCHEMA_CHECK.json validates exact protocol field sets (normalizing only the prose annotation on packet_ids), original/new statement hashes and compatibility. out/ARTIFACT_RECEIPTS.json records local SHA256 and byte sizes. All files are below 20 MB. No read-only source, other agent directory, board, shared index, brain database, Git repository, scheduler or trading tree was modified. Supervisor copying, mirror verification, adoption and independent acceptance of the new obstruction are pending external steps.

Universal bridge: This stage moves C018 through the B01 lead's child-certified near-erasure endpoint by independently accepting its minimal-violator structure and A002's max-constant bridge, retaining every signed child slack, and proving that an arbitrary fixed-gap seed cannot enter that endpoint through any diverging-dimension ratio-preserving Boolean embedding. It pays no new universal entropy term: the surviving gap is the signed near-erasure exclusion on genuinely certified children, with full descendant/terminal entropy retained. NEXT targets that exact first unsupported line because the admission obstruction rules out further broad hardening attempts of this type, while another isolated class calculation would leave the same C018 debt untouched.
