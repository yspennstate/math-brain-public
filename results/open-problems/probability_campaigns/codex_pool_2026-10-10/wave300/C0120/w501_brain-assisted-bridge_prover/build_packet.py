"""Build reviewable drafts and guarded intake diffs; never ingest or edit a live file."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

ROOT=Path(__file__).resolve().parent
REPO=Path("~/<private-repo>")
INTAKE=REPO/"06_math_research/probability_1000_intake_claude_20260907"
stamp=datetime.now(timezone.utc).isoformat()

def write_json(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def exact_record(path, field, value):
    with path.open(encoding="utf-8") as stream:
        for number,line in enumerate(stream,1):
            if value not in line:
                continue
            row=json.loads(line)
            if row.get(field)==value:
                return number,line.rstrip("\r\n"),row
    raise ValueError(f"Missing named record {value}")

problem_line,old_problem,problem=exact_record(INTAKE/"problems.jsonl","problem_id","C0120")
attempt_line,old_attempt,attempt=exact_record(INTAKE/"attempts.jsonl","attempt_id","C0120-A001")
_,_,source=exact_record(INTAKE/"sources.jsonl","source_id","chatterjee_chaos_2008")
recall=json.loads((ROOT/"recall_receipt.json").read_text(encoding="utf-8"))
fallback=json.loads((ROOT/"retrieval_fallback_receipt.json").read_text(encoding="utf-8"))
checks=json.loads((ROOT/"math_check_receipt.json").read_text(encoding="utf-8"))
live=json.loads((ROOT/"selected_live_cards.json").read_text(encoding="utf-8"))
card=next(c for c in live["cards"] if "Fluctuation exponent of directed polymers" in c["title"])
card_metadata=json.loads(card["metadata_json"])
corrected="For independent standard Gaussian weights g_v on Z_+^2, let M_n=max_p sum_{v in p}g_v over all n-vertex up/right paths starting at (0,0), with endpoint free. Improve Chatterjee's Var(M_n)<=C n/log n to Var(M_n)<=C_epsilon n^(1-epsilon) for some epsilon>0 independent of n>=2. This is the concrete power-improvement formulation of Section 12(3) in the Section 8 model. The general-dimensional fixed-temperature log Z_n problem is a separate related formulation, supported for nearly gamma disorder by Alexander-Zygouras arXiv:1204.1819; it is not the observable in the cited Chatterjee theorem. Current openness is UNKNOWN."
status={"schema":"w501-source-status-v1","target":"C0120","as_of":stamp,
        "current_openness":"UNKNOWN","parent_problem_solved":False,"novelty_claim":False,
        "source_scope_mismatch":True,"exact_target":corrected,
        "primary_source":{"source_id":"chatterjee_chaos_2008","url":"https://arxiv.org/html/0810.4221",
                          "version":"v2, 2008-12-16","locator":"Section 8 and Section 12(3), printed p.59",
                          "access":"verified primary HTML and PDF through web tool","quote":"Improve the fluctuation exponent in directed polymers.",
                          "intake_declared_pdf_sha256":source.get("sha256"),"declared_hash_recomputed_here":False},
        "related_source":{"url":"https://arxiv.org/html/1204.1819v2","locator":"Theorem 1.1 and Definition 2.1",
                          "model":"free-endpoint nearest-neighbor simple walk; fixed beta>0 and d>=1; i.i.d. centered nearly gamma disorder; exp(4 beta |omega|) moment",
                          "role":"related positive-temperature formulation; not identical to original target"},
        "prior_records":[{"path":str(INTAKE/"problems.jsonl"),"line":problem_line},
                         {"path":str(INTAKE/"attempts.jsonl"),"line":attempt_line}],
        "bounded_prior_checks":{"named_intakes":"C0120 found in original intake; other named intake matches were indices only",
              "attempts_H_and_I":"targeted rg returned no C0120 record in the two named attempt directories",
              "lean_campaign":"matching ranking row only; no formal proof receipt recovered",
              "Team_O_board":"no C0120 row returned by the targeted board search",
              "owner_research_directory":"no polymer/C0120/variance/retired/solved filename matched; not an exhaustive semantic audit",
              "recent_primary_literature":"bounded arXiv searches found no verified resolution of this exact model; this is not an openness certificate"},
        "served_model_evidence":{"requested_model":"gpt-6.1-sol","requested_reasoning":"max","requested_tier":"Fast",
              "system_declared_family":"GPT-6","response_side_served_model":None,"verified":False,
              "note":"Requested settings and system description are not a response-side attestation. No prohibited profile or credential file was read."},
        "review":{"independent_adversary":"w502","referee":"w503","statement_first_message_id":"msg-35a67c6b7b",
                  "author_claim_is_not_audit":True,"formal_check_receipt":None},
        "measurements":{"native_memory_recall":recall,"native_recall_actual_query":recall["query"]+" 3",
              "query_argument_count_fixed_for_future":True,"sqlite_title_scan":"interrupted at configured 15 s progress deadline; no complete timing receipt",
              "export_fallback":fallback,"indexed_card_lookup":{"elapsed_seconds":live["elapsed_seconds"],"returned":live["returned"],"mode":"ro"},
              "comparison_limit":"Different channels and queries; no global recall speedup or quality improvement is inferred.",
              "math_checks":{k:v for k,v in checks.items() if k!="checks"}}}
write_json(ROOT/"SOURCE_STATUS.json",status)
write_json(ROOT/"STORE_CORRECTION.json",{"state":"DRAFT_PENDING_REVIEW","target_id":card["id"],"expected_node_digest":card["digest"],
             "target_logical_id":card_metadata["logical_id"],"old_body":card["body"],"proposed_body":corrected,
             "support":{"primary_url":"https://arxiv.org/html/0810.4221","exact_locator":"Section 8; Section 12(3)",
                        "short_quote":"Improve the fluctuation exponent in directed polymers."},
             "preserve_related_variant":True,"do_not_promote_open_status":True,"reviewer":"w503","live_mutation_performed":False})

# Candidate patches are repository-relative unified diffs. Only the reviewer may apply them.
patches=ROOT/"patches"
patches.mkdir(exist_ok=True)
new_problem={**problem,"statement":corrected,"status_search":"Current openness UNKNOWN as of 2026-10-10; exact source scope corrected in w501 review packet; no novelty claim.",
             "source_scope_correction":{"worker":"w501","as_of":"2026-10-10","review":"pending w503","original_observable":"M_n, Gaussian planar zero-temperature polymer"}}
new_attempt={**attempt,"result":"No power-improvement proof is supplied. In the Gaussian source model, if E|P_n(g) intersect P_n(g^t)|<=C n^(1-delta) at t=n^(-alpha), fixed alpha,delta>0, the OU identity yields Var(M_n)<=(1+C)n^(1-min(alpha,delta)). The required coupled-overlap estimate remains open in this attempt. Conditionally assuming Var(F_n)=n^(2chi+o(1)) and chi=2xi-1, a power variance improvement requires xi<3/4, not merely xi<1. The scaling relation itself is not established here for the polymer model. See w501/LEMMAS.md for the direct per-site hypercontractivity-certificate obstruction.",
             "obstruction":"Polynomially small OU-time overlap loss is unproved; direct per-site hypercontractivity has an integrated certificate >=(n-1)/log n.",
             "correction_review":"pending w503, 2026-10-10"}
for filename,line_number,old,new,patch_name in [("problems.jsonl",problem_line,old_problem,new_problem,"01_c0120_source_scope.diff"),
                                             ("attempts.jsonl",attempt_line,old_attempt,new_attempt,"02_c0120_exponent_gap.diff")]:
    live_relative="06_math_research/probability_1000_intake_claude_20260907/"+filename
    patch=f"--- a/{live_relative}\n+++ b/{live_relative}\n@@ -{line_number} +{line_number} @@\n-{old}\n+{json.dumps(new,ensure_ascii=False,sort_keys=True)}\n"
    (patches/patch_name).write_text(patch,encoding="utf-8")

model="n>=2; Lambda_n={(i,j):i,j>=0,i+j<n}; independent standard Gaussian vertex weights; n-vertex up/right paths from (0,0), endpoint free; M_n=max path sum and P_n its a.s. unique maximizer."
entries=[]
def entry(key,name,title,statement,assumptions,kind="concept"):
    entries.append({"key":key,"namespace":"probability.gaussian","logical_name":name,"kind":kind,"title":title,
       "statement":statement,"proof_text":None,"assumptions":assumptions,"domain":"probability theory",
       "source":{"source_id":"owner-own-work:w501:C0120:"+key,"url":None,"revision":"draft-2026-10-10",
                 "license":"owner-own-work (campaign derivation, source audit, or refuted route; no novelty claim)","excerpt":None},
       "review_status":"DRAFT, pending independent w503 review","proof_artifact":"~/brain_workers/w501/LEMMAS.md"})
entry("model","gaussian-up-right-free-endpoint-polymer-model","Gaussian up/right free-endpoint polymer model",model,[],"definition")
entry("scope","c0120-gaussian-ground-state-source-scope-draft","C0120 original-source scope correction (draft)","DRAFT source correction: "+corrected,["Chatterjee arXiv:0810.4221v2 Section 8 and Section 12(3)"])
entry("bridge","gaussian-polymer-polynomial-ou-overlap-variance-bridge-draft","Polynomial OU overlap implies a variance power improvement (draft)",
      "DRAFT conditional deduction awaiting review. In the model: "+model+" Let g^t=e^(-t)g+sqrt(1-e^(-2t))g', g' independent, h_n(t)=E|P_n(g) intersect P_n(g^t)|. Var(M_n)=integral_0^infinity e^(-t)h_n(t)dt, h_n is nonincreasing, and h_n(n^(-alpha))<=C n^(1-delta), with fixed C,alpha,delta>0, implies Var(M_n)<=(1+C)n^(1-min(alpha,delta)). The overlap hypothesis is not proved.",
      [model,"Fixed C,alpha,delta independent of n; stated overlap hypothesis"])
entry("envelope","gaussian-polymer-per-site-hypercontractive-envelope-draft","Per-site Gaussian hypercontractivity envelope (draft)",
      "DRAFT source specialization. In the model: "+model+" Let q_v=P(v in P_n), a(t)=tanh(t/2), and g^t=e^(-t)g+sqrt(1-e^(-2t))g' with independent g'. Chatterjee Lemma 4.1 gives E|P_n(g) intersect P_n(g^t)|<=B_n(t):=sum_v q_v^(1+a(t)). Site indicators need not be independent.",[model,"Stationary standard Gaussian OU normalization"])
entry("barrier","gaussian-polymer-per-site-hypercontractive-certificate-barrier-draft","A lower bound on the hypercontractive certificate, not the variance (draft)",
      "DRAFT deduction awaiting review. For n>=2 and any q_v>=0 on Lambda_n={(i,j):i,j>=0,i+j<n} with sum_{i+j=k}q_v=1 on every layer, set B_n(t)=sum_v q_v^(1+tanh(t/2)). Jensen gives B_n(t)>=sum_{k=1}^n k^(-tanh(t/2))>=n^(1-tanh(t/2)), integral_0^infinity e^(-t)B_n(t)dt>=(n-1)/log n, and B_n(n^(-alpha))/n->1 for fixed alpha>0. This prevents this certificate from certifying a variance power improvement. It gives no lower bound on actual overlap or variance.",
      ["Nonnegative layer probabilities of mass one", "Layer k has k+1 sites", "Only the direct unweighted per-site certificate is assessed"])
entry("route","c0120-refuted-one-site-marginal-power-improvement-route-draft","Rejected direct per-site hypercontractivity route (draft)",
      "REJECTED inference, pending independent audit: even exact one-site path marginals q_v do not make the direct Gaussian hypercontractive certificate sum_v q_v^(1+tanh(t/2)) small enough at t=n^(-alpha) to certify a variance power improvement on the n-vertex up/right triangle. The certificate has an integrated floor (n-1)/log n. Stronger joint geometry or a different bound remains possible.",[model])
entry("threshold","c0120-conditional-kpz-three-quarter-threshold-draft","Conditional KPZ threshold correction: xi<3/4 (draft)",
      "DRAFT algebraic correction. Assume Var(F_n)=n^(2chi+o(1)) and chi=2xi-1 for the same model. Var(F_n)<=C n^(1-epsilon), epsilon>0 fixed, requires xi<=3/4-epsilon/4. xi<1 alone is insufficient: xi=4/5 yields variance exponent 6/5. These statements do not establish the KPZ relation for polymers.",
      ["Existence of stated variance exponent", "KPZ relation chi=2xi-1 assumed for this model"])
relations=[{"from_key":"scope","to_key":"model","kind":"depends_on","rationale":"The source correction's M_n is defined by the Gaussian up/right free-endpoint model."},
           {"from_key":"bridge","to_key":"model","kind":"depends_on","rationale":"The overlap identity needs the finite independent Gaussian path model and a.s. unique maximizer."},
           {"from_key":"envelope","to_key":"model","kind":"depends_on","rationale":"Gaussian OU hypercontractivity is applied to the path-incidence indicators in this model."},
           {"from_key":"barrier","to_key":"envelope","kind":"depends_on","rationale":"L3 evaluates precisely B_n(t)=sum_v q_v^(1+tanh(t/2)) from the envelope card."},
           {"from_key":"barrier","to_key":"route","kind":"refutes","rationale":"The barrier's certificate floor (n-1)/log n refutes using this direct certificate to certify a fixed power improvement; it does not refute the target variance bound."},
           {"from_key":"threshold","to_key":"bridge","kind":"semantic_association","rationale":"Both distinguish a needed positive power gap from a weaker asymptotic or exponent statement; the KPZ relation is a separate conditional route."},
           {"from_key":"scope","to_existing_logical":card_metadata["logical_id"],"kind":"cites","rationale":"The existing card attributes 'Var(log Z_n)' in 'general dimension' to Section 12(3); this draft records the source-model discrepancy."},
           {"from_key":"bridge","to_existing_logical":"math:probability.gaussian:ornstein-uhlenbeck-semigroup-and-mehler-formula","kind":"depends_on","rationale":"Uses standard Gaussian OU coupling e^(-t)g+sqrt(1-e^(-2t))g' and L2 self-adjoint contraction in the existing Mehler card."}]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w501","bundle_slug":"c0120-gaussian-overlap-certificate-drafts-001",
        "entries":entries,"relations":relations,"review_gate":"Concept/definition drafts only; no theorem promotion or live store writes before independent proof/model provenance gates pass."}
write_json(ROOT/"bundle_001.json",bundle)
inbox=Path("~/math-brain-inbox/w501")
inbox.mkdir(exist_ok=True)
destination=inbox/"bundle_001.json"
if destination.exists() or (inbox/"bundle_001.json.part").exists():
    raise FileExistsError("Do not overwrite an existing submitted bundle")
write_json(inbox/"bundle_001.json.part",bundle)
os.rename(inbox/"bundle_001.json.part",destination)
write_json(ROOT/"BUNDLE_STATES.json",{"prepared":True,"submitted":True,"submitted_path":str(destination),"submitted_at":stamp,
     "reviewed":False,"ingested":False,"retrievable":False,"concept_or_definition_only":True,
     "coordinator":"codex-01a12190","proof_referee":"w503","live_store_mutation_performed":False})

hook={"id":"polymer-certificate-w501-01","area":"math","event":"PostToolUse",
      "cue":"A Gaussian per-site hypercontractivity upper-bound certificate is being interpreted as an actual variance lower bound",
      "fire_when":"An agent infers Var(M_n)>=(n-1)/log n from the floor on its hypercontractive upper-bound certificate",
      "silent_when":"The statement explicitly bounds the certificate and separately proves or leaves open the actual variance",
      "text":"Check which quantity is bounded: a lower bound on a variance upper-bound certificate is not a variance lower bound. For Gaussian polymer site marginals, Jensen forces the direct certificate to stay large; it leaves actual variance open.",
      "evidence":"~/brain_workers/w501/LEMMAS.md L3; math_check_receipt.json n2_certificate_minus_actual_variance; scar perceptron_proof_open_gaps_fleet_2026_07_12",
      "proposer":"w501"}
assert len(hook["text"])<=300
(ROOT/"hook_proposal.jsonl").write_text(json.dumps(hook,ensure_ascii=False)+"\n",encoding="utf-8")

report=f"""C0120 is not solved. I recovered the cited Gaussian 1+1 ground-state model, found its mismatch with the intake/store's general-dimensional log Z formulation, and saved two candidate intake patches plus a guarded store-correction request. I proved a specific obstruction: direct per-site hypercontractivity has a certificate at least (n-1)/log n, even with exact site marginals. This is not a lower bound on actual variance. The missing step is a polynomial small-time OU coupled-overlap bound.

Validation: python -X utf8 ~/brain_workers/w501/validate_math.py passed {checks['envelope_cases']} finite envelope cases; exact n=2 variance and OU integration differ by {checks['n2_absolute_error']:.3g}. Native recall timed out in {recall['elapsed_seconds']:.3f} s with no output; python -X utf8 retrieve_from_export.py returned 20 candidates in {fallback['elapsed_seconds']:.3f} s, followed by four full read-only indexed lookups in {live['elapsed_seconds']:.5f} s. These different channels do not establish a global speedup. BRAIN_HYPOTHESIS_CHECK.md records which full hypotheses apply.

Apply after review: coordinator may run git -C ~/<private-repo> apply --check ~/brain_workers/w501/patches/01_c0120_source_scope.diff ~/brain_workers/w501/patches/02_c0120_exponent_gap.diff, then apply the kept patch(es) from the same directory. Store changes require the validating integrator; no live file was edited. The submitted inbox bundle contains seven concepts/definitions and eight typed relations. No unreviewed theorem is offered for promotion.

Risks: present openness, response-side served-model identity and independent proof review remain UNKNOWN/pending. A static export and raw indexed lookup do not certify serving-current revision status. The first recall harness mistakenly appended a bare 3 to its query; the harness is fixed, and the unchanged timeout receipt is not ranking-quality evidence. The bounded recall-fallback mechanism is a proposal, with measured local recovery only.

NEXT: w503 checks L3's certificate/variance distinction and the source correction; the next proof step is joint path geometry at t=n^(-alpha), stronger than per-site hypercontractivity.
"""
(ROOT/"REPORT.md").write_text(report,encoding="utf-8")
review="""Review request for w503: independent proof and source audit, not author approval.

Read STATEMENT_ONLY.md first, then LEMMAS.md, BRAIN_HYPOTHESIS_CHECK.md, SOURCE_STATUS.json, CLAIMS.jsonl, STORE_CORRECTION.json, and the validation receipt. L1/L2 are primary-source consequences; L3 is the main local deduction; L4 corrects a conditional exponent implication. Check finite Gaussian integrability, almost sure uniqueness, semigroup time normalization, Jensen layer counts, substitution u=e^(-t), and especially that the certificate lower bound is never promoted to an actual variance lower bound. The n=2 example is an independent normalization check, not the asymptotic proof.

The single hardest gap is h_n(n^(-alpha))<=C n^(1-delta) for fixed positive alpha,delta. It remains unproved. No parent-problem solved or current-openness claim is made. Evaluate source-scope and arithmetic patches separately from the mathematical deductions. If a lemma is kept, its scope is exactly the stated Gaussian triangle or the explicit conditional algebra; the broad fixed-temperature problem is not thereby solved.

All bundle entries are concept/definition drafts. Submitted, reviewed, ingested and retrievable are separate states in BUNDLE_STATES.json. Do not promote theorem truth or ingestion on the strength of matching hashes or numerical checks. No formal receipt or admitted placeholder is presented. Response-side served-model evidence for author/referee is not available here; record it independently if available, otherwise preserve UNKNOWN and the provenance gate.

Use REVIEW_MANIFEST.json to bind exact artifact bytes. Save a separate verdict with scoped KEEP/FIX/DROP and the remaining gap. NEXT: check L3 and source scope before any global-store change.
"""
(ROOT/"REVIEW_PACKET.md").write_text(review,encoding="utf-8")
names=["STATEMENT_ONLY.md","ATTEMPT.md","LEMMAS.md","BRAIN_HYPOTHESIS_CHECK.md","SOURCE_STATUS.json","CLAIMS.jsonl",
       "STORE_CORRECTION.json","REPORT.md","REVIEW_PACKET.md","bundle_001.json","BUNDLE_STATES.json","math_check_receipt.json",
       "recall_receipt.json","retrieval_fallback_receipt.json","selected_live_cards.json","COMPUTE_GATE.json",
       "validate_math.py","retrieve_from_export.py","read_selected_cards.py","hook_proposal.jsonl",
       "patches/01_c0120_source_scope.diff","patches/02_c0120_exponent_gap.diff"]
manifest={"schema":"w501-review-artifact-hashes-v1","created_at":stamp,"purpose":"Review byte identity only, not store cryptographic ceremony or a mathematical proof",
          "files":[{"path":str(ROOT/name),"sha256":hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in names]}
write_json(ROOT/"REVIEW_MANIFEST.json",manifest)
print(json.dumps({"packet":str(ROOT/"REVIEW_PACKET.md"),"submitted_bundle":str(destination),"entries":len(entries),"relations":len(relations),
       "manifest_sha256":hashlib.sha256((ROOT/"REVIEW_MANIFEST.json").read_bytes()).hexdigest(),"parent_solved":False}))
