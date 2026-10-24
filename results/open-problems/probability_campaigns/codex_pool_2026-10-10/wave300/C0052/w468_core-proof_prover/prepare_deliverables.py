"""Prepare local review artifacts and one explicitly authorized DRAFT submission.

Does not integrate drafts, edit a live repository, or write any SQLite store.
"""
from pathlib import Path
import difflib
import hashlib
import json
import re
from datetime import datetime, timezone

root = Path(__file__).resolve().parent
inbox = Path("~/math-brain-inbox/w468")
destination = inbox / "bundle_001.json"
assert not destination.exists(), "Preserve an existing shared draft; never overwrite it"
now = datetime.now(timezone.utc).isoformat()

def entry(key,name,title,statement,assumptions,proof_file):
    return {"key":key,"namespace":"probability.ising.randomcurrents","logical_name":name,"kind":"concept",
            "title":"DRAFT: "+title,"statement":statement,"proof_text":None,"assumptions":assumptions,
            "domain":"probability and mathematical statistical mechanics",
            "source":{"source_id":"owner-own-work:w468:C0052:"+key,"url":(root/proof_file).as_uri(),
                      "revision":"2026-10-10-author-draft","license":"owner-own-work","excerpt":None}}

entries = [
    entry("linear-obstruction","random-current-augmentation-linear-reversal-path-obstruction",
          "Augmented current meeting has no graph-uniform linear reversal",
          "DRAFT author proof, not a result about critical Z^3. On the finite path a-b-z_1-...-z_(m-1)-c-d with m>=1 bridge edges between b and c and uniform parameter t=beta J>0, sample independent random currents n1,n2,n3,n4 with sources {a,b},{c,d},empty,empty. Put p=tanh(t)^2. Then q=P(b connected to c in n1+n2)=p^m, while r=P(C_b(n1+n3) intersects C_c(n2+n4))=[1+m(1-p)]p^m. Thus q/r=1/[1+m(1-p)] tends to zero at fixed t, refuting a positive graph-uniform constant q>=c r. This does not refute a nonlinear comparison or a critical Z^3 comparison.",
          ["Finite path, zero field, uniform ferromagnetic t>0","Independent currents with the four specified source sets","The obstruction concerns linear graph-uniform comparisons only"],"TREE_OBSTRUCTION.md"),
    entry("single-occupation","single-random-current-hitting-not-sourceless-augmented-hitting",
          "The single-current hitting law differs from the augmented hitting law",
          "DRAFT author proof. On the path a-b-z_1-...-z_(m-1)-c-d, with m>=1 bridge edges b to c, let n have sources {a,b} and let n0 be an independent sourceless current, with uniform t=beta J>0. Writing s=sech(t), P(c in C_b(n))=(1-s)^m and P(c in C_b(n+n0))=(1-s^2)^m. Their ratio is (1+s)^(-m), so no positive graph-uniform lower comparison holds for fixed-endpoint single-current occupation versus augmented occupation. The two-point expression G(a,c)G(c,b)/G(a,b) gives the AUGMENTED hitting probability, not the single-current probability.",
          ["Finite tree path and zero field","One sourced current plus an independent sourceless current","Fixed-endpoint comparison; an endpoint-averaged Z^3 comparison is a separate question"],"TREE_OBSTRUCTION.md"),
    entry("coupling-average","ising-signed-coupling-susceptibility-weighted-current-average",
          "Exact susceptibility-weighted current average for the signed Ising coupling",
          "DRAFT author reduction with standard switching inputs; C0052 remains unresolved. In the zero-field unit-coupling nearest-neighbor Ising model on Z^3 at beta<beta_c, let G(x)=E[sigma_0 sigma_x], chi=sum_x G(x), xi=[lim_n -(1/n)log G(ne1)]^(-1), U4 the fourth joint cumulant, and lambda=-sum_{x,y,z}U4(0,x,y,z)/(chi^2 xi^3). Let independent X,W have law mu(x)=G(x)/chi. Given X,W, sample independent ORIGINAL currents with sources {0} symmetric-difference {X} and {y} symmetric-difference {y+W}; retain tagged vertices when endpoints coincide. Let Q_y be the averaged probability that 0 and y are connected in their union. Then lambda=2 xi^(-3)sum_y Q_y. For xi>=1 and B={y:||y||infinity<=floor xi}, with Q_B=|B|^(-1)sum_{y in B}Q_y, lambda>=2|B|xi^(-3)Q_B>=2Q_B. The original source target is lambda not tending to zero; no limit existence is assumed.",
          ["Translation-invariant subcritical free Gibbs state on Z^3","chi finite; xi is the exponential coordinate correlation length","Standard sourced-current construction, switching identity and tree-diagram summability bound"],"ATTEMPT.md"),
    entry("contact-kernels","original-random-current-endpoint-mixture-joint-hit-kernels",
          "Original current contact moments require joint-hit kernels",
          "DRAFT author reduction. In the subcritical translation-invariant zero-field Ising model on Z^3, put mu(x)=G(x)/chi and B={v:||v||infinity<=floor xi_exp}, with xi_exp>=1. Draw X,W independently from mu and Y uniformly from B; conditional on endpoints sample independent currents n1 with sources {0} symmetric-difference {X} and n2 with sources {Y} symmetric-difference {Y+W}. Set N=|B intersect C_0(n1) intersect C_Y(n2)|, m1=E N, m2=E N^2. For one ORIGINAL current n with endpoints 0,x, define k(v)=sum_x mu(x)P(v in C_0(n)) and k2(u,v)=sum_x mu(x)P(u,v in C_0(n)). Then m1=|B|^(-1)sum_{v in B}k(v)sum_{y in B}k(v-y) and m2=|B|^(-1)sum_{u,v in B}k2(u,v)sum_{y in B}k2(u-y,v-y). Diagonal terms are included. Adding one independent sourceless current gives k_aug(v)=G(v), whereas G(v)/chi<=k(v)<=G(v). Hence the corresponding first-moment comparison can lose chi^2. Two hits within one current are not factored into independent probabilities.",
          ["Same subcritical model and standard current identities as the coupling-average entry","Conditional independence is between currents; within-current joint hits stay in k2","Single-current components include their tagged anchor vertices"],"ATTEMPT.md"),
    entry("uniform-gap","three-dimensional-ising-original-contact-second-moment-open-input",
          "Unproved original-current second-moment input for C0052",
          "UNPROVED sufficient input, not a theorem or a solution of C0052. In the subcritical zero-field unit-coupling nearest-neighbor Ising model on Z^3, let X,W be independent with mu(x)=G(x)/chi, Y uniform in B={||y||infinity<=floor xi_exp(beta)}, and n1,n2 independent ORIGINAL currents with source pairs (0,X),(Y,Y+W), cancelling repeated endpoints modulo two. Put N=|B intersect C_0(n1) intersect C_Y(n2)|, m1=E N>0 and m2=E N^2. Proving m2<=C m1^2 with a beta-independent finite C near beta_c would yield lambda=-g>=2|B|xi_exp^(-3)/C>=2/C by Cauchy-Schwarz and switching. A bounded-ratio subsequence would suffice for the source's weaker nonvanishing limsup target. Neither bound is established here. Augmented hitting identities and finite-tree computations do not supply this missing input.",
          ["Near-critical subcritical nearest-neighbor zero-field Ising on Z^3","xi_exp>=1 and the specified susceptibility-weighted endpoint law","The uniform or subsequence second-moment estimate is an OPEN INPUT"],"ATTEMPT.md")
]
relations = [
    {"from_key":"contact-kernels","to_key":"coupling-average","kind":"depends_on",
     "rationale":"The kernels entry uses 'mu(x)=G(x)/chi' and the same ORIGINAL endpoint-current law defined in the coupling entry; its contact event lower-bounds the coupling entry's 'Q_B'."},
    {"from_key":"uniform-gap","to_key":"contact-kernels","kind":"depends_on",
     "rationale":"The gap entry asks for 'm2<=C m1^2'. The kernel entry gives exact formulas for 'm1=E N' and 'm2=E N^2', including within-current joint hits."},
    {"from_key":"uniform-gap","to_key":"coupling-average","kind":"depends_on",
     "rationale":"The gap entry's conditional 'lambda>=2|B|xi_exp^(-3)/C' uses the coupling entry's 'lambda>=2|B|xi^(-3)Q_B' and Q_B>=m1^2/m2."},
    {"from_key":"single-occupation","to_key":"contact-kernels","kind":"semantic_association",
     "rationale":"The path entry distinguishes 'single-current occupation versus augmented occupation'; the kernel entry states 'k_aug(v)=G(v)' while the ORIGINAL k may be smaller. The fixed-endpoint path result is not asserted to refute the endpoint-averaged Z^3 input."},
    {"from_key":"linear-obstruction","to_key":"uniform-gap","kind":"semantic_association",
     "rationale":"The path entry refutes only 'q>=c r' uniformly over graphs. The open input concerns ORIGINAL current components and cannot be obtained by assuming that linear augmented-to-original comparison."}
]
bundle = {"spec":"mathbrain-draft-v1","author_agent":"w468","bundle_slug":"c0052-original-current-overlap-gap-20261010",
          "entries":entries,"relations":relations}
required = {"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
keys = {e["key"] for e in entries}
assert len(keys)==len(entries)<=200
for e in entries:
    assert required.issubset(e) and e["kind"]=="concept" and e["proof_text"] is None
    assert e["source"]["license"].startswith("owner-own-work")
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",e["logical_name"])
for relation in relations:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in {"depends_on","semantic_association"}
graph = {key:[] for key in keys}
for relation in relations:
    if relation["kind"]=="depends_on":
        graph[relation["from_key"]].append(relation["to_key"])
def visit(node,ancestors):
    assert node not in ancestors, "dependency cycle"
    for other in graph[node]:
        visit(other,ancestors|{node})
for key in keys:
    visit(key,set())
body = json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
(root/"bundle_001.json").write_text(body,encoding="utf-8")

hook = {"id":"ising-current-law-w468-01","area":"math","event":"stage-start",
        "cue":r"(?is)(original|single).{0,80}current.{0,180}(lower.bound|occupation|hitting).{0,180}(G_av|G\(a,v\)|sourceless|augment)",
        "fire_when":"Use original current occupation lower bound G_av G_vb / G_ab after sourceless augmentation.",
        "silent_when":"For an upper bound on U4, add two sourceless currents and use the tree diagram.",
        "text":"Name the current laws before using a hitting identity for a lower bound. G_av G_vb/G_ab is for a sourced current PLUS a sourceless current. Enlargement upper-bounds single-current hits; a reverse estimate needs proof.",
        "evidence":"~/brain_workers/w468/TREE_OBSTRUCTION.md L1-L2; verification.json: at m=100 original/augmented meeting=1/37",
        "proposer":"w468"}
assert len(hook["text"])<=300
assert re.search(hook["cue"],hook["fire_when"])
assert not re.search(hook["cue"],hook["silent_when"])
(root/"proposals").mkdir(exist_ok=True)
hook_body = json.dumps(hook,ensure_ascii=False)+"\n"
(root/"proposals/math-w468.jsonl").write_text(hook_body,encoding="utf-8")

note = (root/"ATTEMPT.md").read_text(encoding="utf-8")+"\n\n"+(root/"TREE_OBSTRUCTION.md").read_text(encoding="utf-8")+"\n\n"+(root/"STATEMENT.md").read_text(encoding="utf-8")
(root/"RESEARCH_NOTE.md").write_text(note,encoding="utf-8")
(root/"patches").mkdir(exist_ok=True)
def new_file_diff(relative,contents):
    return "diff --git a/"+relative+" b/"+relative+"\nnew file mode 100644\n"+"".join(difflib.unified_diff([],contents.splitlines(keepends=True),fromfile="/dev/null",tofile="b/"+relative))
research_relative = "06_math_research/probability_C0052_w468_20261010/RESEARCH_NOTE.md"
(root/"patches/01_c0052_current_law_note.diff").write_text(new_file_diff(research_relative,note),encoding="utf-8")
(root/"patches/02_current_law_hook.diff").write_text(new_file_diff("hooks1000/proposals/math-w468.jsonl",hook_body),encoding="utf-8")

claims = [json.loads(line) for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
for claim in claims:
    if claim["id"] in {"w468-C0052-L1","w468-C0052-L2"}:
        claim["independent_reviewer"] = "w469: scoped KEEP in REVIEW_W468.md; w470 designated referee pending; served-model evidence unavailable"
        claim["audit_artifact"] = "~/brain_workers/w469/REVIEW_W468.md"
(root/"CLAIMS.jsonl").write_text("".join(json.dumps(c,ensure_ascii=False)+"\n" for c in claims),encoding="utf-8")

# The acquired narrow mesh lease is clm-f869aadc6d. Only this worker's named
# bundle is submitted, complete and atomically renamed; existing files are preserved.
inbox.mkdir(parents=True,exist_ok=True)
part = inbox/"bundle_001.json.part"
with part.open("x",encoding="utf-8") as stream:
    stream.write(body)
assert not destination.exists()
part.rename(destination)
state = {"worker":"w468","candidate":"C0052","prepared_at":now,"draft_path":str(destination),
         "lease":"clm-f869aadc6d","submitted":{"state":"submitted","entries":len(entries)},
         "reviewed":{"state":"partial","scoped_keeps":{"w469":["L1","L2"]},"pending":["w470 L1-L5","response-side served-model evidence"]},
         "ingested":{"state":"not confirmed; coordinator integrates"},"retrievable":{"state":"not checked; no ingestion receipt"},
         "promotion":"concept-only DRAFT; parent C0052 NOT SOLVED"}
(root/"BUNDLE_STATE.json").write_text(json.dumps(state,indent=2),encoding="utf-8")
validation = {"command":"python -X utf8 prepare_deliverables.py","status":"PASS","entries":len(entries),
              "relations":len(relations),"all_entries_concept_only":True,"dependency_graph_acyclic":True,
              "owner_own_work_license_tags":True,"hook_fire_control":True,"hook_silent_control":True,
              "warning":"Structural validation only; not a mathematical proof, source seal, model receipt, or live-store integration."}
(root/"draft_validation.json").write_text(json.dumps(validation,indent=2),encoding="utf-8")

tree = json.loads((root/"verification.json").read_text(encoding="utf-8"))
kernel = json.loads((root/"kernel_verification.json").read_text(encoding="utf-8"))
report = f"""C0052 is not solved in this packet. Its current openness is UNKNOWN. The exact 2017 source asks that signed g(beta) not tend to zero as beta approaches beta_c; xi is the exponential correlation length along e1. No limit existence is assumed.

The useful change is an exact account of the ORIGINAL current law in the old second-moment route. ATTEMPT.md proves the susceptibility-weighted coupling identity, the contact-moment reduction, and the first/joint occupation-kernel formulas. The hardest remaining input is UCM: a uniform bound on E[N^2]/E[N]^2 for the original current components. Adding sourceless currents changes their hitting probabilities. Two exact path examples show why graph-uniform linear reversals and fixed-endpoint occupation lower comparisons cannot be presumed.

Measured controls: python -X utf8 verify_tree.py passed {tree['checks_passed']} exact checks on {tree['cases']} paths in {tree['elapsed_seconds']:.6f} seconds of computation. python -X utf8 verify_kernels.py passed {kernel['checks_passed']} exact checks on one four-cycle in {kernel['elapsed_seconds']:.6f} seconds, including all repeated endpoint tuples. At t=log(3), bridge length 100, the original/augmented meeting ratio is exactly 1/37. These are finite mathematical controls, not a measured improvement in live brain recall or a critical Z3 estimate.

Five concept-only DRAFT entries with five scoped relations were submitted to ~/math-brain-inbox/w468/bundle_001.json under lease clm-f869aadc6d. Structural validation and both hook controls passed. w469 gave scoped KEEP to the two tree claims; w470 has the full packet. Model evidence, full review, integration and retrievability remain separate pending states in BUNDLE_STATE.json. No live store was written.

Reviewer application: git -C ~/<private-repo> apply ~/brain_workers/w468/patches/01_c0052_current_law_note.diff adds the full research note. The hook proposal is staged in proposals/math-w468.jsonl and patches/02_current_law_hook.diff for reviewer landing under this worker's write restriction. integrate_drafts.py is reserved for the validating coordinator under the explicit no-live-store-write rule.

Risks: the reduction relies on the standard subcritical infinite-volume sourced-current construction and switching identity. UCM may be stronger than necessary; a bounded-ratio subsequence already suffices for the source target. The path counterexamples do not exclude a nonlinear or lattice-specific reverse comparison. Tests and a scoped KEEP cannot fill the remaining Ising gap.

NEXT: Prove a dimension-specific joint-hit bound for k2 and an original-current first-moment lower estimate that bound the ratio in equations (E)/(D)^2, or give a precise counterexample to UCM.
"""
(root/"REPORT.md").write_text(report,encoding="utf-8")
checksums = {name:hashlib.sha256((root/name).read_bytes()).hexdigest()
             for name in ["STATEMENT.md","ATTEMPT.md","TREE_OBSTRUCTION.md","REVIEW_PACKET.md","REPORT.md","CLAIMS.jsonl",
                          "verify_tree.py","verify_kernels.py","compute_gate.json","kernel_compute_gate.json",
                          "verification.json","kernel_verification.json","patches/01_c0052_current_law_note.diff","patches/02_current_law_hook.diff"]}
(root/"REVIEW_CHECKSUMS.json").write_text(json.dumps({"purpose":"Review-file checksums only; not integrator digests, a source manifest, seal or proof receipt","files":checksums},indent=2),encoding="utf-8")
print(json.dumps({"draft":str(destination),"entries":len(entries),"relations":len(relations),
                  "math_checks":tree["checks_passed"]+kernel["checks_passed"],"claims":len(claims),
                  "packet_sha256":checksums["REVIEW_PACKET.md"],"attempt_sha256":checksums["ATTEMPT.md"],
                  "states":state,"validation":validation},indent=2))
