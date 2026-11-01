"""Build a reviewable mathematical DRAFT; never integrate or write a live store."""
import json
from pathlib import Path

base = Path(__file__).resolve().parent
measure = json.loads((base/"measurements.json").read_text(encoding="utf-8"))
audit = json.loads((base/"affine_audit_measurements.json").read_text(encoding="utf-8"))
assert audit["cases"] == audit["passed"] == 372
assert measure["all_two_variable_restriction_pairs"]["passed"] == 256

target = base/"CLAIMS.jsonl"
all_rows = [json.loads(line) for line in target.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
source_rows = [row for row in all_rows if "source-" in row["id"]]
math_rows = [row for row in all_rows if "source-" not in row["id"]]
(base/"SOURCE_ROWS.jsonl").write_text("".join(json.dumps(row)+"\n" for row in source_rows),encoding="utf-8")
for row in math_rows:
    row["independent_reviewer"] = "w512; referee packet saved, mesh recipient registration unavailable at first request"
    row["review_state"] = "pending independent mathematical review"
target.write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in math_rows),encoding="utf-8")

verdicts = []
statements = [
    "Exact affine-indicator spectrum, entropy and active-coordinate influence formulas are correct.",
    "The affine-indicator class has sharp FEI constant 4; its fixed-codimension maximum occurs exactly at coordinate subcubes for codimension >=2.",
    "Nonempty spectral conditioning requires H=h_2(v)+vH(Q) and I=vE_Q|S|; an unweighted H(Q)<=C I bridge is false.",
    "Uniform per-coordinate chain entropy charging is false; independent input bits do not imply independent spectral-coordinate bits."
]
for index, statement in enumerate(statements,1):
    verdicts.append({"id":f"P0162-w511-audit-w510-C00{index}","claim_id":f"P0162-w510-C00{index}",
        "verdict":"KEEP","reviewer":"w511","statement":statement,
        "assumptions":"Exactly the scoped uniform-Boolean and affine assumptions in w510 ATTEMPT.md",
        "proof_or_counterexample":"Independent proof checks and boundary analysis in AUDIT_W510.md; exact exhaustive corroboration in affine_audit_measurements.json",
        "source":"~/brain_workers/w510/ATTEMPT.md",
        "remaining_gap":"Unrestricted FEI and novelty are not certified. Final referee w512 still required.",
        "status":"independently checked proof"})
(base/"AUDIT_W510.jsonl").write_text("".join(json.dumps(row)+"\n" for row in verdicts),encoding="utf-8")

prefix = "DRAFT: independent mathematical referee review pending; no novelty claim. "
def entry(key, logical, title, statement, assumptions):
    return {"key":key,"namespace":"analysis.boolean_functions","logical_name":logical,
        "kind":"concept","title":title,"statement":prefix+statement,"proof_text":None,
        "assumptions":assumptions,"domain":"Fourier analysis of Boolean functions",
        "source":{"source_id":"owner-own-work:fei-restriction-profile-boundary",
            "url":"urn:probability-research:fei-restriction-profile-boundary",
            "revision":"independent-campaign-draft-2026-10-10","license":"owner-own-work",
            "excerpt":None}}

common = ["Uniform Boolean cube","Base-2 Fourier entropy including the empty coefficient","0 log(1/0)=0"]
entries = [
    entry("split-profile","boolean-coordinate-split-binary-entropy-profile","Draft: Boolean coordinate split entropy profile",
        "For Boolean f and a specified coordinate i, write f^+ and f^- for its two restrictions, Delta_i=H(f)-(H(f^+)+H(f^-))/2 and delta=I_i(f). Then Delta_i<=h_2(delta)+(2/ln 2)delta, where h_2 is binary entropy. This upper bound is known prior work, independently rederived here. Its binary-entropy term cannot be replaced by a universal constant times delta at every coordinate.",common),
    entry("bad-bridge","false-universal-coordinate-split-linear-entropy-charge","Draft: false universal coordinate split charge",
        "The stronger assertion that there exists a finite universal K such that Delta_i H(f)<=K I_i(f) for every Boolean f and every specified coordinate i is false. This assertion quantifies over every coordinate and is stronger than an induction that chooses a suitable coordinate depending on f.",common),
    entry("point-flip","quadratic-bent-point-flip-selector-obstruction","Draft: quadratic bent point-flip selector",
        "For even n>=2, t in F_2^n, let g(t)=(-1)^(sum_{j=1}^{n/2} t_{2j-1}t_{2j}), h(t)=g(t)-2*1_{t=0}, and F(t,+1)=g(t), F(t,-1)=h(t). Both restrictions and F are Boolean. With p=2^-n, I_z(F)=p and Delta_z H(F)/p>=n-4/ln 2. Also I(F)=n/2+(n+1)p and H(F)/I(F) tends to 2. Thus this family refutes an every-coordinate linear charge, without refuting full FEI.",common+["Even n>=2","Specified selector coordinate z"]),
    entry("profile-sharpness","boolean-coordinate-split-profile-sharp-additive-constant","Draft: sharp additive constant in the split profile",
        "For even n>=2 use g(t)=(-1)^(sum_j t_{2j-1}t_{2j}), h=g-2*1_{t=0} and selector F(t,+1)=g(t), F(t,-1)=h(t). For p=2^-n, Delta_z H(F)/p=n+3/ln 2+O(p), whereas h_2(p)/p=n+1/ln 2+O(p). Hence [Delta_z H(F)-h_2(p)]/p tends to 2/ln 2, making the additive coefficient in Delta_i<=h_2(I_i)+(2/ln 2)I_i optimal. Multiplication by an independent dictator balances F and both restrictions while preserving their entropies and selector influence.",common+["Even n tending to infinity","Specified selector coordinate"]),
    entry("absolute-two","boolean-coordinate-split-entropy-two-bit-bound","Draft: sharp two-bit split increment bound",
        "For every Boolean f and every coordinate i, 0<=H(f)-(H(f^+)+H(f^-))/2<=2 bits. The upper bound is attained by f(z,x,y)=((1+z)x+(1-z)y)/2: it has four squared Fourier coefficients equal to 1/4, restricted entropies zero, and selector influence 1/2.",common),
    entry("spectrum-l1","bent-point-flip-squared-spectrum-l1-charge-obstruction","Draft: squared-spectrum charge obstruction",
        "For even n>=2, let g(t)=(-1)^(sum_j t_{2j-1}t_{2j}), h=g-2*1_{t=0} and let F join g,h across a selector z. Put p=2^-n. Then sum_S |ghat(S)^2-hhat(S)^2|/I_z(F)=4(1-p)/sqrt(p). This disproves a universal squared-spectrum L1 charge by influence at every specified split.",common+["Explicit even-dimensional quadratic bent family"]),
    entry("coordinate-choice","fei-restriction-induction-existential-coordinate-premise","Draft: retain the coordinate quantifier in FEI induction",
        "A restriction induction for a Boolean class closed under restrictions needs a uniform K and, for every f in the class, existence of a coordinate i with Delta_i H(f)<=K I_i(f). The quadratic bent point-flip selector has a bad selector coordinate, but each original coordinate has influence 1/2+2^-n and split increment at most 2, so its split ratio is below 4. A specified bad coordinate cannot refute this existential premise.",common+["Class closed under restrictions for the proposed induction"])
]
relations = [
    {"from_key":"point-flip","to_key":"bad-bridge","kind":"refutes","rationale":"The Boolean specified-split ratio exceeds every fixed K as even n grows."},
    {"from_key":"profile-sharpness","to_key":"point-flip","kind":"depends_on","rationale":"The sharpness limit uses the exact Boolean selector family."},
    {"from_key":"profile-sharpness","to_key":"split-profile","kind":"semantic_association","rationale":"The family approaches the additive constant in the stated upper profile."},
    {"from_key":"spectrum-l1","to_key":"point-flip","kind":"depends_on","rationale":"The squared-spectrum obstruction is computed on the same explicitly defined family."},
    {"from_key":"coordinate-choice","to_key":"point-flip","kind":"depends_on","rationale":"Its specified bad coordinate leaves all original coordinate ratios below 4."},
    {"from_key":"coordinate-choice","to_key":"absolute-two","kind":"depends_on","rationale":"The two-bit bound supplies the good-coordinate ratio bound."}
]
bundle = {"spec":"mathbrain-draft-v1","author_agent":"w511",
          "bundle_slug":"fei-coordinate-restriction-sharp-boundary-20261010","entries":entries,"relations":relations}
allowed_kinds = {"definition","lemma","theorem","concept"}
keys = {row["key"] for row in entries}
assert len(keys)==len(entries)<200
for row in entries:
    assert row["kind"] in allowed_kinds and row["kind"]=="concept" and row["proof_text"] is None
    assert row["source"]["license"].startswith("owner-own-work")
    assert "C:/" not in row["statement"] and "w511" not in row["statement"]
for relation in relations:
    assert relation["from_key"] in keys and relation["to_key"] in keys
draft = base/"bundle_001.json"
draft.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

hook = {"id":"fei-split-quantifier-w511-01","area":"math","event":"stage-start",
    "cue":"(?i)(FEI|Fourier entropy).*(split|restriction|induction)|(split|restriction|induction).*(FEI|Fourier entropy)",
    "fire_when":"A draft FEI restriction proof charges entropy by coordinate influence at an arbitrary split without proving that the chosen coordinate is suitable.",
    "silent_when":"The argument has proved its coordinate-selection premise, or is only verifying an affine-indicator special case.",
    "text":"Before a Fourier restriction induction, write the coordinate quantifier. A point flip of a bent function gives Delta_i/I_i>=n-4/ln 2 at a specified split, while another coordinate is good. A bound for every i needs more than a bound for a suitable i.",
    "evidence":"~/brain_workers/w511/ATTEMPT.md C001; measurements.json grouped n=128 ratio 132.3280851227; pending referee review",
    "proposer":"w511"}
assert len(hook["text"])<=300
proposal = base/"math-w511.jsonl"
proposal.write_text(json.dumps(hook)+"\n",encoding="utf-8")
patches = base/"patches"
patches.mkdir(exist_ok=True)
live = "~/primary_directive/hooks1000/proposals/math-w511.jsonl"
(patches/"01_math_hook_proposal.diff").write_text(
    f"diff --git a/{live} b/{live}\nnew file mode 100644\n--- a/{live}\n+++ b/{live}\n@@ -0,0 +1 @@\n+"+json.dumps(hook)+"\n",encoding="utf-8")

inbox = Path("~/math-brain-inbox/w511")
inbox.mkdir(parents=True,exist_ok=True)
delivery = inbox/"bundle_001.json"
payload = draft.read_text(encoding="utf-8")
if delivery.exists():
    assert delivery.read_text(encoding="utf-8")==payload, "Refuse to overwrite a different existing draft"
else:
    pending = inbox/"bundle_001.json.part"
    with pending.open("x",encoding="utf-8") as out:
        out.write(payload)
    pending.rename(delivery)
receipt = {"prepared":True,"submitted":True,"submission_path":str(delivery),"entries":len(entries),
    "entry_kind":"concept/draft","schema_checks":"PASS; local structural checks only",
    "reviewed":False,"ingested":False,"retrievable":False,
    "review_state":"w512 independent mathematical review pending",
    "live_store_modified":False,"live_code_modified":False,
    "hook_proposal":"local file and unified diff for authorized coordinator; not filed globally"}
(base/"DELIVERY_STATE.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,indent=2))
