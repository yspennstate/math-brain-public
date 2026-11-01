"""Build review artifacts and an explicitly authorized DRAFT inbox bundle.

This does not integrate, seal, or mutate any live brain store.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w504')


def save_json(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def main():
    measurement = json.loads((ROOT/'measurements.json').read_text(encoding='utf-8'))
    assert measurement['status']=='PASS'
    claims = [json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    ids = {row['id'] for row in claims}
    source = {"source_id":"owner-p0162-w504-20261010","url":"urn:owner-work:p0162:w504:20261010",
              "path":str(ROOT/'PROOF.md'),"license":"owner-own-work"}
    localize = {"id":"w504-P0162-C006",
                "statement":"For any fixed tau in (0,1), the universal suitable-coordinate inequality is equivalent to its restriction to Boolean functions with max_i Inf_i(f)<tau, allowing different constants. A constant K_0 on this restricted class gives K=max(K_0,2/tau) universally, since every Boolean coordinate satisfies 0<=Delta_i(f)<=2.",
                "assumptions":["Uniform measure","Boolean functions in every dimension","Entropy in bits","Delta_i=H(f)-[H(f_i^+)+H(f_i^-)]/2","The all-small-influence selection bound is assumed, not proved"],
                "source":source,"proof_or_counterexample":"PROOF.md section 4: 0<=h_2<=1 in C001 gives 0<=Delta<=2; a coordinate with influence >=tau has ratio <=2/tau. The reverse implication is restriction of scope.",
                "independent_reviewer":"w506 (requested; pending)","remaining_gap":"At tau=1/16 the existence of one finite K_0 for all functions with all influences <1/16 remains unproved. The special family has large base influences.",
                "status":"proved special case","scope":"Conditional localization; known prior small-influence direction, no novelty claim"}
    if localize['id'] not in ids:
        with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as out:
            out.write(json.dumps(localize,ensure_ascii=False)+'\n')

    source_status = {
        "target":"P0162","title":"Fourier entropy versus total influence","checked_at":"2026-10-10",
        "historical_status":"attempted_un","historical_tier":5,"current_openness":"UNKNOWN","novelty_claim":False,
        "exact_target":"There is one finite C, independent of n and f, such that every Boolean f:{-1,1}^n->{-1,1} under uniform measure satisfies sum_S fhat(S)^2 log_2(1/fhat(S)^2)<=C sum_S |S| fhat(S)^2. Zero summands are zero; fhat(S)=E[f chi_S]. No balance or monotonicity is assumed.",
        "primary_statement_verified":True,
        "primary_sources":[
            {"url":"https://arxiv.org/pdf/1204.6447","title":"Open Problems in Analysis of Boolean Functions","author":"Ryan O'Donnell","revision":"v1, 29 April 2012","locator":"Printed page 5 (PDF page index 4), Fourier Entropy-Influence Conjecture","statement_status":"verified exact target; matches the intake citation"},
            {"url":"https://arxiv.org/html/2606.00246v1","title":"Further evidence towards the Fourier Entropy-Influence conjecture","authors":["Maria Jose Gonzalez","Paul MacManus","Maria Cristina Pereyra"],"revision":"v1, 29 May 2026","locator":"Introduction: FEI Conjecture and Ansatz 1.1","result_scope":"Restricted classes and conditional induction; not a full FEI proof"},
            {"url":"https://arxiv.org/abs/2609.21563","title":"On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions","author":"Vladimir N. Potapov","revision":"18 September 2026","locator":"Abstract checked","result_scope":"Plateaued and partially bent functions; not the full target"},
            {"url":"https://arxiv.org/abs/1312.3003","title":"Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture","locator":"Abstract checked","result_scope":"Read-k and decision-tree results; exact target independently matches"}
        ],
        "origin_reference":{"citation":"Friedgut and Kalai, Every monotone graph property has a sharp threshold, Proc. AMS 124(10), 2993-3002 (1996)","original_paper_retrieved":False,"attribution_sources":["O'Donnell 2012 page 5","Gonzalez--MacManus--Pereyra 2026 references"]},
        "owner_work_checks":[
            {"path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv","locator":"row 553","finding":"Historical tier 5 attempted_un"},
            {"path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006p01.json","locator":"op-p0162","finding":"Target and O'Donnell PDF page 5; current status explicitly unverified"},
            {"path":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006a04.json","locator":"at-p0162","finding":"Singleton distribution is not a Boolean spectrum; nonlinear convolution identities remain necessary"},
            {"paths":["probability_1000_attempts_H_20260912","probability_1000_attempts_I_20260914"],"finding":"No P0162 exact-ID record located in the targeted text search; not a global absence claim"},
            {"path":"prob1000_lean_20260908/RANKED_LIST_2026-09-07_annotated.md","locator":"row containing P0162","finding":"Historical status only; no actual P0162 formal theorem located"},
            {"path":"~/brain_workers/teams/W0300_O/TEAM_BOARD.md","finding":"No exact P0162 row in targeted board lookup; intentional new triads checked for lane overlap"},
            {"path":"~/<private-repo>/06_math_research/fei_step_numerics_2026_09_20/README.md","finding":"Existing min-step/total-step experiments; finite lower bounds and no universal conclusion"}
        ],
        "recall":{"command":"python -X utf8 ~/.claude/dreaming/brain.py recall P0162 Fourier entropy influence proof mistakes","timeout_seconds":60,"result":"timed out","fallback":"MEMORY.md grep returned no terms; read only the relevant filename matches","memory_slugs":["fei_package_checked_induction_step_needs_a_growing_constant_2026_09_20","fei_most_influential_coordinate_fails_by_composition_2026_09_24","fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23","perceptron_proof_open_gaps_fleet_2026_07_12"]},
        "current_openness_reason":"Recent primary papers and relevant owner work establish partial results and failed routes. The full solved/retired registry has not been certified comprehensively, so current global openness stays UNKNOWN. No novelty is asserted.",
        "formal_receipt":{"performed":False,"actual_theorem":None,"trusted_axioms":None,"admitted_placeholders_used":False,"reason":"Proof arguments are written and checked numerically; no Lean theorem was compiled."}
    }
    save_json(ROOT/'SOURCE_STATUS.json',source_status)

    (ROOT/'ATTEMPT.md').write_text('''# P0162 core-proof attempt

The full FEI statement is: under the uniform cube measure, every Boolean f has spectral entropy H(f)=sum_S fhat(S)^2 log_2(1/fhat(S)^2) at most C times I(f)=sum_S |S|fhat(S)^2, for one finite universal C. Zero terms are zero. The exact primary statement was recovered from O'Donnell, Open Problems in Analysis of Boolean Functions, arXiv:1204.6447v1, printed page 5; the 2026 restriction paper independently matches it. Current openness is UNKNOWN and no novelty is claimed.

The prior intake attempted a distribution uniform on singleton Fourier indices. Its entropy is log_2 n and mean size is 1, but such a law cannot be a Boolean spectrum: a linear combination with two nonzero coefficients produces a nonzero cross coefficient in f^2, contradicting f^2=1. The actual prior gap is the nonlinear Boolean convolution constraint. The H/I named archives and Lean ranking did not provide a new exact P0162 proof in the targeted reads. Owner FEI work already records growing finite restriction-step lower bounds, a reduction to small influences, and a counterexample to selecting the most influential coordinate via balanced composition. Those are relevant prior-work boundaries, not proof receipts for the full problem. Full source details are in SOURCE_STATUS.json.

The route is exact restriction entropy: Delta_i(f)=H(f)-[H(f_i^+)+H(f_i^-)]/2, alongside I(f)=Inf_i(f)+[I(f_i^+)+I(f_i^-)]/2. One uniformly good coordinate at every nonconstant Boolean function would finish induction. PROOF.md section 1 proves the exact coefficient identity including the nonnegative imbalance term; section 2 proves the reduction without hiding its input.

The substantive special-case attempt uses m=2k bits and the quadratic bent function g_m(b)=(-1)^(sum b_(2r-1)b_(2r)). Flip its value only at b=0,z=1 to obtain F_m(b,z)=g_m(b)-2*1_{b=0,z=1}. With t=2^-m, the selector has Inf_z=t and unbounded Delta_z/Inf_z. w505 independently found this obstruction before seeing this proof, and other triads also hold that obstruction; w504's complementary claim is the positive base-coordinate calculation. Every base coordinate j satisfies Inf_j=1/2+t and Delta_j<=2-(m/2)t<4 Inf_j. The proof computes both restrictions exactly and applies Jensen to u^2 log_2 u on [1/2,3/2]. A separate chain-rule argument gives H(F_m)<=2I(F_m); it does not assume arbitrary restrictions preserve the family. Complete algebra is in PROOF.md sections 3b and 3c.

Command python -X utf8 verify_adaptive.py --gate adaptive-n13-cpu20 passed 30 base-coordinate checks in four families and 64 coordinate checks of the exact entropy/influence identities. Maximum residual was 7.460698725481052e-14. At m=12, choosing the selector gives a ratio of 16.326969582936727; a base coordinate gives 3.9940634391370446. This run is a regression check of the formulas, not a formal verification or a proof of a universal constant.

The single hardest remaining lemma is suitable-coordinate selection in the all-small-influence regime. For example, prove one finite K_0 such that every nonconstant Boolean f with all Inf_i(f)<1/16 has some relevant i with Delta_i(f)<=K_0 Inf_i(f). The elementary bound Delta_i<=2 handles any function having Inf_i>=1/16 with constant 32, so this restricted input would yield the universal input with max(K_0,32). Nothing in the family calculation handles every such small-influence function. The largest-influence rule is already refuted and is not proposed.

Review requested from w506 for C001--C004 and C006; C005 remains conjectural. The independent adversary's construction is acknowledged rather than counted as a new w504 discovery. Draft brain entries remain concept material until review; submitted, reviewed, ingested, and retrievable are tracked separately.

NEXT: Audit C003's restricted spectra and Jensen step, then try a coordinate-averaged defect bound for all-small-influence Boolean functions using their full convolution constraints.
''',encoding='utf-8')

    def entry(key,name,title,statement,assumptions):
        return {"key":key,"namespace":"probability.boolean-fourier","logical_name":name,
                "kind":"concept","title":title,"statement":statement,"proof_text":None,
                "assumptions":assumptions,"domain":"analysis of Boolean functions",
                "source":{"source_id":"owner-p0162-w504-20261010:"+key,
                          "url":"urn:owner-work:p0162:w504:20261010:"+key,
                          "revision":"draft-review-pending-20261010-v1","license":"owner-own-work",
                          "excerpt":None}}
    basic = ["Uniform independent input bits","Boolean values -1,+1","Entropy in bits","Review-only DRAFT; no independent KEEP recorded for this entry"]
    entries = [
        entry('restriction-identity','draft-exact-restriction-entropy-defect',
              'DRAFT: Exact restriction entropy defect',
              'Review-only DRAFT of a worker-derived identity, not an accepted FEI proof. For Boolean f under uniform measure, let H be Shannon entropy in bits of squared normalized Walsh coefficients, and Delta_i=H(f)-[H(f_i^+)+H(f_i^-)]/2. For restriction coefficients u_T,v_T put w_T=(u_T^2+v_T^2)/2, p_T=u_T^2/(u_T^2+v_T^2), q_T=(u_T-v_T)^2/[2(u_T^2+v_T^2)]. Omit zero weights. Then sum w_T=1, Inf_i(f)=sum w_T q_T and Delta_i=sum w_T[1+h_2(q_T)-h_2(p_T)], where h_2 is binary entropy with zero endpoint terms. In particular 0<=Delta_i<=2. The extra imbalance term is nonnegative and cannot be dropped for an upper bound.',basic),
        entry('adaptive-family','draft-bent-rare-flip-base-coordinate-bound',
              'DRAFT: Suitable base coordinates in a bent rare-flip family',
              'Review-only DRAFT of a proved-by-worker special case pending independent check; no novelty or full FEI claim. For even m>=2, let g_m(b)=(-1)^(sum_{r=1}^{m/2}b_{2r-1}b_{2r}) and F_m(b,z)=g_m(b)-2*1_{b=0,z=1} on independent uniform bits b in {0,1}^m and z in {0,1}. Set t=2^-m. For every base coordinate j in [m], Inf_j(F_m)=1/2+t and Delta_j(F_m)<=2-(m/2)t<4 Inf_j(F_m), where Delta_j is parent spectral entropy minus the average spectral entropy of its two restrictions. This is an explicit family only; arbitrary Boolean coordinate selection remains unproved.',basic+['m is even and at least 2','The exception is exactly one vertex']),
        entry('family-fei','draft-bent-rare-flip-fei-constant-two',
              'DRAFT: FEI with constant 2 for the bent rare-flip family',
              'Review-only DRAFT of a proved-by-worker special case pending independent check. For even m>=2 define F_m(b,z)=(-1)^(sum_{r=1}^{m/2}b_{2r-1}b_{2r})-2*1_{b=0,z=1} on uniform independent bits. With spectral entropy H in bits, total influence I=sum_S |S| Fhat_m(S)^2, and t=2^-m, one has I=m/2+(m+1)t and H<=m+h_2(t)<=2I. This family satisfies FEI despite an unbounded selector Delta_z/Inf_z ratio; neither observation settles FEI for all Boolean functions.',basic+['m is even and at least 2']),
        entry('coordinate-gap','draft-small-influence-suitable-coordinate-gap',
              'DRAFT: Unproved suitable-coordinate input for FEI',
              'Unproved sufficient input, explicitly CONJECTURAL: there is a finite K_0 such that every nonconstant Boolean f on every uniform cube with max_i Inf_i(f)<1/16 has a relevant coordinate i satisfying Delta_i(f)<=K_0 Inf_i(f). Here H(f) is entropy in bits of squared normalized Walsh coefficients, Delta_i=H(f)-[H(f_i^+)+H(f_i^-)]/2 and Inf_i=sum_{S containing i} fhat(S)^2. The identity Delta_i<=2 handles any function with some Inf_i>=1/16 using constant 32. Thus this input would imply H(f)<=max(K_0,32) I(f) for every Boolean function by induction. The input itself is not proved, and choosing the largest influence is not justified.',basic+['One K_0 independent of dimension and function','EXISTS relevant coordinate, not FOR EVERY coordinate'])
    ]
    bundle = {"spec":"mathbrain-draft-v1","author_agent":"w504","bundle_slug":"p0162-adaptive-coordinate-review-draft-20261010",
              "entries":entries,"relations":[
                  {"from_key":"adaptive-family","to_key":"coordinate-gap","kind":"semantic_association","rationale":"The family proves a good coordinate exists in one explicit class; it does not establish the all-small-influence input."},
                  {"from_key":"adaptive-family","to_key":"restriction-identity","kind":"semantic_association","rationale":"Both statements concern exactly the same Delta_i under uniform measure; the family bound retains both entropy terms."},
                  {"from_key":"family-fei","to_key":"adaptive-family","kind":"semantic_association","rationale":"The statements concern exactly the same explicitly defined Boolean family, comparing its global entropy bound with local splitting costs."}
              ]}
    required = {'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
    keys = {e['key'] for e in entries}
    for e in entries:
        assert required <= e.keys()
        assert e['kind']=='concept' and e['proof_text'] is None
        assert e['source']['license'].startswith('owner-own-work')
        assert 'DRAFT' in e['title'] and len(e['statement'])>100
    allowed = {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
    for relation in bundle['relations']:
        assert relation['from_key'] in keys and relation['to_key'] in keys and relation['kind'] in allowed
    # Local staging precedes the explicitly authorized inbox publication.
    save_json(ROOT/'bundle_001.json',bundle)
    INBOX.mkdir(parents=True,exist_ok=True)
    n = 1
    while (INBOX/f'bundle_{n:03d}.json').exists() or (INBOX/f'bundle_{n:03d}.part').exists():
        n += 1
    part = INBOX/f'bundle_{n:03d}.part'
    dest = INBOX/f'bundle_{n:03d}.json'
    assert part.parent.resolve()==INBOX.resolve() and dest.parent.resolve()==INBOX.resolve()
    save_json(part,bundle)
    part.rename(dest)
    states = {"worker":"w504","target":"P0162","draft_path":str(dest),
              "submitted":{"state":"submitted-as-review-only-draft","entries":len(entries),"relations":len(bundle['relations'])},
              "reviewed":{"state":"pending","reviewer":"w506","mathematical_keeps_recorded":0,"receipt":"Complete proof sent as msg-067e31a82c; later receipt pending"},
              "ingested":{"state":"not-observed","integrator_run_by_worker":False},
              "retrievable":{"state":"not-tested","live_retrieval_claim":False},
              "promotion":{"all_entries":"concept/draft","unreviewed_theorems":0}}
    save_json(ROOT/'BRAIN_SUBMISSION.json',states)
    save_json(ROOT/'bundle_validation.json',{"status":"PASS","scope":"Local draft-schema checks only, not integrator approval or mathematical review","entries":len(entries),"relations":len(bundle['relations']),"all_relation_ends_resolved_locally":True,"source_license":"owner-own-work","unreviewed_theorem_entries":0,"formal_proof_check":False})

    proposal = {"id":"fei-coordinate-quantifier-w504-01","area":"math","event":"PreToolUse",
                "cue":"FEI restriction proof asserts a uniform per-coordinate entropy bound or chooses the most influential coordinate without a proof",
                "fire_when":"A proof writes Delta_i<=C Inf_i for every coordinate, or chooses the largest influence without proving it is a good split",
                "silent_when":"The agent states the global FEI target, computes an exact entropy identity, or explicitly labels suitable-coordinate selection as conjectural",
                "text":"Check the restriction quantifier: a fixed coordinate can have unbounded Delta/Inf while global H/I stays bounded. Prove a suitable coordinate or an amortization. Choosing the largest influence needs its own proof.",
                "evidence":"w504/PROOF.md sections 3b and 4; measurements.json m=12: selector 16.32697, base 3.99406; memory slug fei_most_influential_coordinate_fails_by_composition_2026_09_24",
                "proposer":"w504"}
    assert len(proposal['text'])<=300
    proposals = ROOT/'proposals'
    proposals.mkdir(exist_ok=True)
    (proposals/'math-w504.jsonl').write_text(json.dumps(proposal,ensure_ascii=False)+'\n',encoding='utf-8')

    patch_dir = ROOT/'patches'
    patch_dir.mkdir(exist_ok=True)
    note = (ROOT/'PROOF.md').read_text(encoding='utf-8')
    live_path = 'proofnet24/P03-fei/continuations/2026-10-10-w504-adaptive-coordinate/NOTE.md'
    lines = note.splitlines()
    patch = f'diff --git a/{live_path} b/{live_path}\nnew file mode 100644\n--- /dev/null\n+++ b/{live_path}\n@@ -0,0 +1,{len(lines)} @@\n'+''.join('+'+line+'\n' for line in lines)
    (patch_dir/'01_adaptive_coordinate_note.diff').write_text(patch,encoding='utf-8')

    last = measurement['families'][-1]
    report = f'''The full FEI conjecture is not proved. The packet proves a complementary special case: every base quadratic coordinate of the explicitly defined bent rare-flip family satisfies Delta_j<=4 Inf_j. It also gives an exact entropy identity, a conditional induction reduction, and H<=2I for that family. No novelty is claimed; w505 independently found the selector obstruction and other triads hold that obstruction.

Before/after compares the splitting coordinate on the same function. Command: python -X utf8 verify_adaptive.py --gate adaptive-n13-cpu20. At m=12, the selector has Delta/Inf={last['selector_delta_over_influence']:.12f}; a base coordinate has {last['base_coordinates'][0]['delta_over_influence']:.12f}. Thirty base-coordinate checks and 64 identity-coordinate checks passed; maximum numerical residual {measurement['max_absolute_identity_residual']:.3g}. CPU time {measurement['cpu_seconds']:.5f}s; wall time {measurement['wall_seconds']:.5f}s.

These computations verify formulas and are not a formal proof receipt. Independent mathematical review by w506 is pending. The hardest remaining input is a uniform good-coordinate bound for all Boolean functions with every influence below 1/16; the family does not resolve that regime. Source/status checks recover the exact primary statement but do not certify current global openness, which remains UNKNOWN.

Four review-only concept entries and three supported relations were published at {dest}. Submission is recorded in BRAIN_SUBMISSION.json; review is pending, ingestion is not observed, and retrievability is not tested. The worker did not run the integrator or alter a live store. The hook proposal is staged in proposals/math-w504.jsonl under the worker-folder write restriction; a reviewer can file it in the shared hook queue.

Apply the note only after independent review: from ~/<private-repo>/06_math_research/math-open-problems, the reviewer runs git apply --check ~/brain_workers/w504/patches/01_adaptive_coordinate_note.diff, then git apply with that same path. The test command is above; integration of the draft belongs to the validating coordinator.

NEXT: Independently check C003's two restricted spectra and Jensen step, then test a coordinate-averaged defect bound in the all-small-influence regime against balanced-composition counterexamples.
'''
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    packet = '''# Review packet for w506

Target and assumptions: STATEMENT.md and SOURCE_STATUS.json. Prior digest and hardest gap: ATTEMPT.md. Full derivation: PROOF.md. Claim rows: CLAIMS.jsonl. Bounded regression checks: verify_adaptive.py and measurements.json. Fresh gate: COMPUTE_GATE.json. Review-only brain submission: bundle_001.json and BRAIN_SUBMISSION.json.

Audit C003 first: F_m is Boolean; the b_j=1 restriction has entropy m-2; the b_j=0 restriction has the four control blocks stated in section 3b; its entropy is m-2+3mt-L(1,2a); and L(1,2a)<=2L(1,a) follows from Jensen on [1/2,3/2]. Check m=2 separately (the core has zero variables). The result is Delta_j<=2-(m/2)t<4 Inf_j.

Then check C001's entropy chain rules and normalization, C002's conditional induction quantifiers, C004's direct H<=2I argument, and C006's localization. C005 is expressly an unproved input; no KEEP on the reduction may promote it. The selector obstruction is independently supplied by w505; construction overlap is disclosed and no novelty is asserted. No lemma assumes arbitrary restrictions stay in this family.

Run: python -X utf8 ~/brain_workers/w504/verify_adaptive.py --gate adaptive-n13-cpu20
The recorded result is PASS: 30 base coordinates, 64 identity coordinates, maximum residual 7.460698725481052e-14, CPU 0.34375s. Floating logarithms are numerical evidence for the written formulas, not Lean or interval certificates. There are no admitted formal placeholders because no formal theorem was compiled.

Review statuses, ingestion, and retrieval must be recorded separately. The bundle contains concept entries only and deliberately labels the claims as review-only DRAFT. A complete file or source check is not a mathematical audit.

NEXT: Save a claim-specific KEEP/FIX/DROP verdict for C003; keep the universal coordinate-selection input unproved.
'''
    (ROOT/'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
    print(json.dumps({"draft":str(dest),"entries":len(entries),"relations":len(bundle['relations']),"claim_rows":len(claims)+(localize['id'] not in ids),"local_schema_validation":"PASS","mathematical_review":"pending","ingestion":"not-observed","retrievability":"not-tested"}))


if __name__=='__main__':
    main()
