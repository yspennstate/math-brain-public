# A069 stage 2: aligned edit energy and the addressing hierarchy reference

Full FEI remains OPEN. The original A069 v1 theorem has now been independently accepted by A070 at its stated scope. This stage supplies one bundled scoped extension, awaiting independent review.

## exact target, quantifiers, hypotheses and units

Uniform Boolean sign functions, Fourier probabilities fhat(S)^2, entropy and code lengths in bits, physical influence I=sum |S| fhat(S)^2. A hierarchy reference uses a rooted partition tree fixed before observing S, singleton leaves and bounded arity. Its complete all-set code is L_T(S)=1+sum_v b_v 1{S intersects C_v}, with Gamma_T(f)=E L_T(S_f) and H(f)<=Gamma_T(f).

New paid family: ordinary a-bit addressing, a>=1, on n=a+2^a bits padded to arbitrary N>=n, with arbitrary truth-table edits of density rho. The explicit binary tree below satisfies Gamma_T(f)<=16I(f) if N*rho<=1/8; every one-point edit satisfies Gamma_T(f)<=25I(f), and the 16 bound applies for N>=6. This is a complete code, not merely an entropy estimate inherited from unedited addressing.

New generic interface: for any Boolean g and any nonempty proper physical block Z, flip g on the subcube z=z*. Derive the exact weighted edit-spectrum cost in a fixed tree whose root separates Z and its complement Y. Quantify the retained restricted-core term and its physical-Parseval bound. No universal FEI conclusion for this interface is asserted.

Lead-directed calibration: Gamma(g_2)=17/2 at N=9 and 21/2 at N=10,11,12. Reuse the already certified 512 N=9 one-point edits with bound 25I, and the N=10 base; directly check the new N=11,12 bases.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md supervisor snapshot 2026-10-12 04:39 UTC, B14 STREAM_NOTES.md v2 (2026-10-11 23:25 UTC), own STATUS and stage-1 claims/output were read. Execution protocol fei-execution-protocol/2, revision 2026-10-11-execution-v2 was reread in full. This continues the A069 packet and follows the lead's majority/addressing targets while advancing the saved subcube-edit gap.

Source-bound dependency: A069-STABLE-HIERARCHY-EDIT-PAYMENT@1, statement SHA256 cd5f76a5bb9b392b3cd098f53516f83f2ae8e02fa78de7950f280d64c7245d4a. A070 REPORT/PROGRESS at runs/20261011T230551Z-account05-A070-analytic-route-referee independently accepted that version without repair, reconstructing masks, occupancy, weighted triangle and influence stability. Its separate three-reference point-edited-addressing no-go is context only; this stage does not redo that search or its pending queue-code work.

Primary source locators revisited: percolation_spectral_pivotal_entropy_30pp.txt, Lemma 2.1 refinement decoder; threshold_paper_38pp.txt, Section 5.7 addressing queue benchmark and Section 8 addressing identities. Prior stage's full proofs, exact validation and persistence records were consumed. The new proof uses explicit addressing coefficients and finite Parseval rather than an unreviewed spatial estimate. Exact path/hash provenance is in out/SOURCE_MANIFEST.json. No new literature search or priority assertion is made.

## complete derivation or exact first unsupported line

DERIVATION.md contains the complete finite-sum proof, equations (A1)-(A4) and (S1)-(S5). The critical steps are reproduced here.

Addressing has one uniformly chosen data coordinate j and an independently uniform subset of its a selector coordinates in every spectral sample. Use a balanced binary tree on selector coordinates, a complete binary tree on the 2^a data coordinates, and a binary root joining them. Add a binary padding tree under a second join if N>n. Define R(1)=0 and R(k)=1-2^{-k}+R(floor(k/2))+R(ceil(k/2)) for k>=2. An address cell of size k is occupied with probability 1-2^{-k}; the data sample occupies one path of a internal vertices. Consequently

    Gamma_T(A_a)=3+2a+2R(a)+2*1{N>n}<=8I(A_a)-5.

The decoder covers all subsets, including tails created by editing. Its maximum length is 2N-1. The accepted weighted-L2 edit bound and |I(f)-I(A_a)|<=2N*rho give

    Gamma_T(f)<=16I(f)-10+48N*rho-8rho.

Thus N*rho<=1/8 closes the 16I bound. For a single edit, N*2^{-N}<=3/8 and I(f)>=Var(f)>=15/16 because addressing is balanced. Hence Gamma_T(f)<=16I(f)+8<25I(f). No omitted label, empty atom, reference normalizer, or terminal entropy remains. For fixed a, the weighted-L2 cost difference under padding and a single flip tends to zero.

The influence reference instead costs exactly

    log2(e)+a+(a/2)*log2(a+2)+log2((a+2)/2)

on unedited (and padded) addressing. Its ratio to I is log2(a)+2+o(1), whereas the hierarchy ratio is <=8. This comparison locates the gain: a whole spectral set shares a single data path and the selector masks. Unedited addressing's FEI was already proved; this is a complete edit-stable reference, not a new claim to that baseline.

For the subcube interface, let rho=2^{-r}, h=g restricted to z=z*, m_h=Eh, and delta=f-g=-2*1{z=z*}h. Let W_Z,W_Y be the internal-mask costs of the two binary subtrees, and U_Z=E_{uniform subset of Z}W_Z=sum_v 2*(1-2^{-|C_v|}). Direct coefficient factorization gives the exact identity

    E_delta:=sum_S deltahat(S)^2 L_T(S)
       =4rho*[1+2*(1-rho*m_h^2)+U_Z+E_{S_h}W_Y].

The empty coefficient is included. The last term is the restricted core's actual spectrum, not an assumed low-cost Boolean leaf. Partial Parseval gives E_{S_g}W_Y=E_z E_{S_{g_z}}W_Y, so rho*E_{S_h}W_Y<=E_{S_g}W_Y. Since U_Z<=2(r-1),

    E_delta<=4E_{S_g}W_Y+4rho*(2r+1),
    Gamma_T(f)<=2Gamma_T(g)+8E_{S_g}W_Y+8rho*(2r+1).

This replaces the crude rho*N charge by an explicit control-size charge plus a source-compatible retained-core charge. On every free-coordinate edge, editing both endpoints leaves pivotality unchanged. On each control-coordinate edge crossing the subcube boundary, exactly one of g,f is pivotal. Thus Inf_i(f)=Inf_i(g) for i in Y and I_Z(f)+I_Z(g)>=2r*rho. The weighted triangle handles g/delta interference; squared spectra of g and f are never replaced by an incoherent mixture.

First unsupported universal line: choose a complete paid separating source reference for arbitrary Boolean g and transport its retained-core cost with a single influence budget that survives cancellation to f. The exact subcube identities do not prove that line. In particular an edit can make f constant, while the root-bit code still costs one, so no all-subcube Gamma_T(f)<=C I(f) claim is made.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before execution. One standard-library checker, version A069-stage2-exact-v1, uses integer FWHT, Fraction, actual Boolean truth tables, direct pivotal edge counts and an iterative prefix decoder distinct from the previous recursive implementation. Frozen memory estimate 32 MB, maximum runtime 60 seconds with a 55-second guard; no memok-sized job was started. Command from this run: `python -X utf8 code/check.py`.

Actual output out/CHECK.json: PASS, 5,338 target cases, 374,529 exact assertions, measured Python time 0.571 seconds. Domain:

* 728 addressing edits: a=1,N=3..7 and a=2,N=6..8 exhaust every edited vertex; a=3,N=11,12 uses the explicitly frozen first eight/last eight vertices. The latter are a bounded subset, not an orbit-complete census. Ten unedited addressing transforms are auxiliary calibrations.
* Two new g_2 base transforms, N=11,12, each gives Gamma=21/2 and I=9/4; direct physical influence agrees with spectral influence.
* 4,608 subcube edits: all 256 three-bit Boolean functions, all nonempty proper control subsets, all control assignments. These certify the rank-factorized edit spectrum, exact weighted cost, restricted-core marginal identity, and edge ownership, including constants and cancellation cases.

Decoder round trips and Kraft are checked for every subset at each addressing calibration dimension, up to N=12. Each edited coefficient is independently compared with the truth-table transform. Analytic inequalities supply all entropy signs; no floating entropy values, finite extrapolation, or numerical search is a proof.

out/REUSED_CERTIFICATES.json pins the prior g_2 records at N=9,10 and their source hash. N=9's 512 one-point edits and their 25I checks are reused, not recounted among the 5,338 new cases. The A070 review independently establishes the all-dimensional prior statement.

## proof dependencies and changed downstream conclusions

The only reused registered proof dependency is A069-STABLE-HIERARCHY-EDIT-PAYMENT@1, independently accepted locally by A070. Its source statement, hypotheses and digest are preserved; no earlier run was rewritten. One bundled new claim A069-ALIGNED-EDIT-ENERGY-ADDRESSING@1 records the exact identities and paid family. Independent review of this new claim is pending.

A070 can use this reference as a complete alternative to the queue reference missing from its failed three-reference hybrid; no suggestion that the C008 queue was invalid is made. A067/A068 can apply the exact subcube edit energy when using references that separate a physical edit block, retaining the terminal core. A088/A094 should check signed factorization, marginal normalization, and cancellation scope. B20 can adopt restricted C020 payment and the generic edit-cost interface, not universal FEI.

The non-Boolean singleton control still fails generic hierarchy payment, as established in stage 1. No step transports recursive-majority occupancy estimates or addressing occupancy estimates to arbitrary normalized-real spectra. Published read-once/addressing results remain baseline, and no novelty over all literature is claimed for the new neighborhood.

## one next mathematical action and independent reviewer

Next: derive the exact cross-energy of two subcube edits with overlapping control coordinates in one fixed all-set reference, then test whether first physical exposure owns it once while both restricted-core costs remain explicit. Reviewers A088/A094; A070 can independently replay the decoder/payment implementation. This consumes the generic source-compatible cost identity rather than rerunning a solved family or the already refuted influence-only reference.

## actual persistence receipts or precise save blocker

REPORT.md, DERIVATION.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, frozen specification, checker, exact outputs, source and local persistence hashes are saved only under A069. STATUS.md has exactly STATE/NEXT lines; WORKLOG and LEARNED are current. out/SCHEMA_CHECK.json verifies required protocol fields and statement hash conventions; out/RECEIPTS.json lists actual saved file bytes and SHA256 values. No local save blocker. Supervisor copy, mirrors, B20 adoption and independent acceptance of the new theorem are not asserted.

## Universal bridge

This stage moves C020 whole-set witness cost by supplying a complete hierarchy reference paid on edited addressing (16I at N*rho<=1/8; 25I for all one-point edits), exact lead-requested g_2 costs, and a generic subcube-edit energy identity that replaces blind rho*N with control-boundary scale plus the retained restricted-core code. Universal separating-reference selection, influence transport through cancellations, and overlapping-edit cross-energy remain unpaid. NEXT targets that cross-energy because it is the first term absent from the single-edit identity and can connect to shared-control ownership work in B05/B13; another unedited family result would not advance the universal reference interface. Full FEI remains OPEN.
