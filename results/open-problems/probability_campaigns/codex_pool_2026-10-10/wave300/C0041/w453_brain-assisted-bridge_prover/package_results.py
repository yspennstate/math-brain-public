"""Package own mathematical drafts; only explicit worker/inbox paths are written."""
import difflib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
INBOX=Path("~/math-brain-inbox/w453")
assert str(ROOT.resolve()).replace("\\","/").lower()=="~/brain_workers/w453"
assert str(INBOX.resolve()).replace("\\","/").lower()=="~/math-brain-inbox/w453"
text=ROOT.joinpath("LEMMAS.md").read_text(encoding="utf-8")

def proof(section):
    part=text.split(section+".",1)[1]
    part=re.split(r"\nL[0-9]+\.\s",part,maxsplit=1)[0]
    return part.split("Proof.",1)[1].split("\nApplication",1)[0].split("\nScope:",1)[0].strip()

source={"source_id":"owner:w453:c0041-range-clock-20261010","url":"file:///~/brain_workers/w453/LEMMAS.md","revision":"draft-2026-10-10-conditional-normalization-v2","license":"owner-own-work (independent review pending)","excerpt":None}
def entry(key,name,kind,title,statement,assumptions,proof_text=None):
    return {"key":key,"namespace":"probability.randomenvironment","logical_name":name,"kind":kind,"title":title,"statement":statement,"proof_text":proof_text,"assumptions":assumptions,"domain":"probability theory","source":dict(source)}

base=["d is an integer >=1; X starts at 0 on Z^d", "nearest-neighbor transitions in a fixed or randomly sampled static environment", "every transition probability is at least a deterministic kappa in (0,1/(2d)] under the original law P", "T takes values in N union {infinity}; it need not be a stopping time"]
entries=[
entry("def-range","spatial-range-of-a-random-path-clock","definition","Spatial range of a random path clock","For a path X_n in Z^d started at 0 and a time T in N union {infinity}, define R_T=sup_{0<=n<=T}||X_n||_infinity. This is a path functional; neither T nor R_T needs to be a stopping time.",[],None),
entry("lem-clock","uniform-ellipticity-range-to-clock-bound-with-conditioning","lemma","Uniform ellipticity: spatial range to clock, with conditioning","Let X be a nearest-neighbor walk on Z^d, d>=1, started at 0, in a static environment with all transition probabilities at least kappa>0 under its original quenched or annealed law P. For any random time T in N union {infinity}, define R_T=sup_{0<=n<=T}||X_n||_infinity. For integers r,t>=0, m=r+1, P(T>t)<=P(R_T>r)+(1-kappa^m)^floor(t/m). For any event A with alpha=P(A)>0, P(T>t|A)<=P(R_T>r|A)+alpha^(-1)(1-kappa^m)^floor(t/m). The conditional walk is not asserted to retain uniform ellipticity.",base+["For the conditional statement, A has positive original-law probability alpha"],proof("L1")),
entry("lem-mean","fast-exponential-range-tail-gives-finite-random-clock-mean","lemma","A fast exponential spatial tail gives a finite mean clock","Let X be a nearest-neighbor walk on Z^d, d>=1, started at 0, in a static environment with all transition probabilities at least kappa>0 under its original quenched or annealed law P. Let T in N union {infinity} be any random time and R_T=sup_{0<=n<=T}||X_n||_infinity. Let Q=P or Q=P(.|A) for a specified event A with P(A)>0. If Q(R_T>r)<=C exp(-lambda r) for every integer r>=0, with C finite and lambda>log(1/kappa), then E_Q[T]<infinity. This is a sufficient condition; no necessity or implication from directional transience is asserted.",base+["Q is P or a conditioning on an event of positive P-probability", "Q(R_T>r)<=C exp(-lambda r) for all integer r>=0", "C is finite and lambda>log(1/kappa)"],proof("L2")),
entry("lem-counter","exponential-range-infinite-mean-inward-drift-random-box","lemma","Countermodel: exponential range with an infinite mean clock","On Z, set omega(x,+1)=1/4 for x>0, 3/4 for x<0, and 1/2 at x=0, with complementary left-step probabilities. Independently choose a positive integer R with P(R=r)=2^(-r), r>=1. Start the walk at 0 and let T be its first exit from [-R,R]. Then T is finite almost surely, R_T=sup_{n<=T}|X_n|=R+1 has an exponential tail and every polynomial moment, but E[T]=infinity. For fixed radius r, E[T|R=r]=(3/2)(3^(r+1)-1)-2(r+1). This is not a counterexample to directional-transience ballisticity for d>=2 iid environments: the construction is one-dimensional, non-iid, and not directionally transient.",["one-dimensional deterministic inward-drift environment described in the statement", "independent R with P(R=r)=2^(-r)", "T is random-box exit, not a directional regeneration time"],proof("L3")),
entry("route-refuted","refuted-unspecified-exponential-range-to-clock-implication","concept","REFUTED route: unspecified exponential range rate","REFUTED PROPOSAL, not a theorem: the proposed universal implication says that any uniformly elliptic nearest-neighbor walk and any almost-surely finite path clock with some exponential spatial-range tail must have a finite mean clock. The random-radius inward-drift countermodel refutes this implication. This does not refute the distinct iid directional-transience ballisticity statement.",[],None),
entry("gap","c0041-range-clock-bridge-gap-with-original-law-normalization","concept","C0041: the remaining range-to-clock input","DRAFT conditional proof route for C0041. In d>=2 iid uniformly elliptic nearest-neighbor environments, the input is annealed almost-sure transience in one fixed direction l; the target is almost-sure liminf positive speed in that direction. For the standard first regeneration time tau_1 and D=inf{n>=0:X_n.l<0}, the range-to-clock route would establish E_0[tau_1|D=infinity]<infinity from an exponential range bound under P_0(.|D=infinity) of rate lambda>log(1/kappa). Such a quantitative range bound has not been derived here from the target's qualitative premise. Conditioning requires the original-law estimate divided by P_0(D=infinity)>0, not ellipticity of the conditioned walk. A September 2026 external preprint claims the exact target; its proof is a separate review, so no current openness or novelty claim is made by this draft.",["Exact C0041 input: d>=2, iid site rows, uniform ellipticity, annealed almost-sure directional transience", "standard regeneration construction with P_0(D=infinity)>0", "No exponential range bound is part of the given input"],None),
]
relations=[
 {"from_key":"lem-clock","to_key":"def-range","kind":"depends_on","rationale":"The bound uses 'R_T=sup_{0<=n<=T}||X_n||_infinity', which the definition states as exactly that path functional."},
 {"from_key":"lem-mean","to_key":"lem-clock","kind":"depends_on","rationale":"The hypothesis 'lambda>log(1/kappa)' makes both terms of 'P(T>t|A)<=P(R_T>r|A)+alpha^(-1)(1-kappa^m)^floor(t/m)' summable with r=floor(a log(t+1))."},
 {"from_key":"lem-counter","to_key":"def-range","kind":"depends_on","rationale":"The countermodel's 'R_T=sup_{n<=T}|X_n|=R+1' instantiates the defined spatial range in dimension one."},
 {"from_key":"lem-counter","to_key":"route-refuted","kind":"refutes","rationale":"The countermodel has 'an exponential tail and every polynomial moment, but E[T]=infinity', contradicting the proposed conclusion 'must have a finite mean clock' for precisely the abstract hypotheses stated by the route."},
 {"from_key":"gap","to_key":"lem-mean","kind":"semantic_association","rationale":"The gap explicitly lacks 'rate lambda>log(1/kappa)' for the regeneration range; the conditional lemma explicitly requires that additional range-tail rate. The edge records a sufficient route, not an equivalence or a solution."},
 {"from_key":"gap","to_existing_logical":"math:probability.randomenvironment:open-problem-c0041-transience-in-a-direction-implies-ballisticity-for-uniformly-elliptic","kind":"cites","rationale":"The gap concerns the exact C0041 input and target recovered from Open Question 2.20. The existing target card's historical September 7 open-status note does not certify current openness."}
]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w453","bundle_slug":"c0041-range-clock-conditional-bridge-001","entries":entries,"relations":relations}
allowed={"definition","lemma","theorem","concept"}
keys={e["key"] for e in entries}
assert len(keys)==len(entries)<=200
for e in entries:
    assert e["kind"] in allowed and e["source"]["license"].startswith("owner-own-work")
    assert bool(e["proof_text"]) if e["kind"] in {"lemma","theorem"} else e["proof_text"] is None
for rel in relations:
    assert rel["from_key"] in keys and (rel.get("to_key") in keys or "to_existing_logical" in rel)
serialized=json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
ROOT.joinpath("bundle_001.json").write_text(serialized,encoding="utf-8")

# Local prototype and unified diff; no live source file is changed.
prototype=ROOT.joinpath("measure_candidate_lookup.py").read_text(encoding="utf-8")
function=prototype.split("def lookup_candidate",1)[1].split("\ndatabase=",1)[0]
module='"""Read-only exact lookup for C/P intake candidate cards; no substring fallback."""\nimport re\nimport sqlite3\nfrom pathlib import Path\n\ndef lookup_candidate'+function+"\n"
ROOT.joinpath("copies").mkdir(exist_ok=True)
ROOT.joinpath("patches").mkdir(exist_ok=True)
ROOT.joinpath("copies/candidate_lookup.py").write_text(module,encoding="utf-8")
live="~/math-brain-build/src/math_brain/candidate_lookup.py"
ROOT.joinpath("patches/01_candidate_lookup.diff").write_text("".join(difflib.unified_diff([],module.splitlines(True),fromfile="a/"+live,tofile="b/"+live)),encoding="utf-8")

hook={"id":"range-clock-w453-01","area":"math","event":"stage-start","cue":"Regeneration or random-clock integrability is inferred only from an unspecified exponential spatial-range tail, without comparing its rate to the clock cost or citing a theorem that handles that rate.","fire_when":"Claim: UE plus some exponential regeneration-range tail automatically gives finite mean duration, using only a fixed-box escape estimate.","silent_when":"A complete valid theorem supplies the necessary rate, or a dimension-sensitive argument handles weaker rates; also silent outside clock integrability.","text":"Compare the spatial-tail exponent with the clock cost. UE plus some exponential range tail does not ensure a finite mean general clock (w453 L3). For conditioning on no backtracking, use the original-law bound divided by its event probability.","evidence":"~/brain_workers/w453/LEMMAS.md L1-L3; countermodel_checks.json (8 exact systems, 0 failures)","proposer":"w453"}
assert len(hook["text"])<=300
hooktext=json.dumps(hook,ensure_ascii=False)+"\n"
ROOT.joinpath("HOOK_PROPOSALS.jsonl").write_text(hooktext,encoding="utf-8")
hooklive="~/primary_directive/hooks1000/proposals/math-w453.jsonl"
ROOT.joinpath("patches/02_math_hook_proposal.diff").write_text("".join(difflib.unified_diff([],hooktext.splitlines(True),fromfile="a/"+hooklive,tofile="b/"+hooklive)),encoding="utf-8")

# The brief explicitly authorizes this inbox; other outside writes are avoided.
INBOX.mkdir(parents=True,exist_ok=True)
destination=INBOX/"bundle_001.json"
assert not destination.exists(),"preserve existing draft; choose a new numbered file"
temporary=INBOX/"bundle_001.json.part"
assert not temporary.exists(),"preserve existing partial draft"
temporary.write_text(serialized,encoding="utf-8")
temporary.rename(destination)
receipt={"spec":"w453-bundle-lifecycle-v1","draft_path":str(destination),"submitted":True,"reviewed":False,"ingested":False,"retrievable":False,"structural_checks":"passed locally; not integrator approval or mathematical audit","entries":len(entries),"relations":len(relations),"mathematical_status":"three own conditional/countermodel lemmas awaiting referee; target still unproved by w453","hook_status":"local proposal and named-path diff only, respecting worker output restriction","deployment":"No live store or global recall controls modified"}
ROOT.joinpath("BUNDLE_STATES.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt))
