"""Create and validate an author DRAFT; the coordinator alone may ingest it."""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
INBOX=Path("~/math-brain-inbox/w510")
text=(ROOT/"ATTEMPT.md").read_text(encoding="utf-8")

def proof(claim):
    start=text.index("## "+claim+":")
    stop=text.find("\n## ",start+1)
    return text[start:stop if stop!=-1 else len(text)]

def entry(key,name,kind,title,statement,assumptions,proof_text=None):
    return {"key":key,"namespace":"probability.boolean_fourier","logical_name":name,"kind":kind,"title":title,"statement":statement,"proof_text":proof_text,"assumptions":assumptions,"domain":"analysis of Boolean functions","source":{"source_id":"owner-own-work:w510:P0162:"+key,"url":"urn:owner-own-work:w510:P0162:"+key,"revision":"draft-author-proof-2026-10-10-v1-independent-review-pending","license":"owner-own-work","excerpt":None}}

common=["Uniform probability on F_2^n","Boolean output in {-1,+1}","Normalized real Walsh coefficients","Shannon entropy in bits with zero-log terms equal to zero"]
entries=[
entry("defs","uniform-boolean-spectral-entropy-influence","definition","Uniform Boolean spectral entropy and total influence","For f:F_2^n->{-1,+1}, n>=1, on uniform input, write fhat(s)=E[f(x)(-1)^(s dot x)]. Its spectral law is Pr[S=s]=fhat(s)^2, summing to one by Parseval. Its Shannon entropy is H(f)=sum_s fhat(s)^2 log2(1/fhat(s)^2), including s=0 and using zero for zero-log terms. Its total influence is I(f)=sum_s |s| fhat(s)^2=sum_i Pr[f(x)!=f(x+e_i)]. Friedgut-Kalai's FEI conjecture asks for one finite absolute C with H(f)<=C I(f) for all n and f; no bias or variance restriction is part of this uniform-cube target. Current openness as of 2026-10-10 is UNKNOWN in this author packet.",common),
entry("affine","affine-indicator-fourier-entropy-orientation","lemma","Exact spectrum and influence of affine-subspace indicators","Let A=a+V be a nonempty affine subspace of F_2^n with codimension r>=1, U=V^perp, p=2^-r, and m the number of coordinates nonzero on some u in U. For f=1-2*1_A, fhat(0)=1-2p, fhat(u)=-2p*(-1)^(u dot a) for nonzero u in U, and fhat(s)=0 outside U. Each active coordinate has influence 2p, each inactive one zero, so I(f)=2pm. With q=(1-2p)^2, H(f)=-q log2(q)+8p(1-p)(r-1). Here 0 log2(0)=0, m>=r, and H=0 at r=1. Sign reversal preserves all squared-spectrum quantities.",common+["A nonempty affine subspace; r>=1","m counts active ambient coordinates, not just codimension"],proof("C001")),
entry("sharp","affine-indicator-fei-sharp-constant-four","theorem","Sharp entropy-influence constant 4 for affine indicators","For the class consisting of f=+/- (1-2*1_(a+V)) on uniform F_2^n and constant Boolean functions, H(f)<=4 I(f), and no smaller constant works uniformly over this class. At fixed codimension r>=2, put p=2^-r and H_r=-(1-2p)^2 log2((1-2p)^2)+8p(1-p)(r-1). If m is the active-coordinate count of V^perp, then H(f)/I(f)=H_r/(2pm)=(r/m)M_r where M_r=H_r/(2pr). The fixed-r maximum is M_r, attained exactly by coordinate subcubes up to translation and sign. M_r tends to 4. This is a special case, and the coordinate AND/OR limit 4 is known folklore; novelty is not claimed.",common+["Affine-subspace indicators and constants only","Fixed-r equality characterization restricted to r>=2"],proof("C002")),
entry("conditioning","nonempty-spectral-conditioning-mass-counterexample","lemma","Retain variance when conditioning the spectral sample","For a nonconstant uniform Boolean f, let S have probabilities fhat(s)^2, v=Var(f)=Pr[S!=0]>0, and Q be the law of S conditioned on S!=0. Then H(f)=h2(v)+v H(Q) and I(f)=v E_Q|S|, where h2 is binary entropy. No finite absolute C makes H(Q)<=C I(f) hold for all such f. For f_r=1-2*1_(x_1=...=x_r=0), r>=2, Q is uniform on 2^r-1 nonzero vectors, H(Q)=log2(2^r-1), and I(f_r)=r*2^(1-r); their ratio is at least ((r-1)/r)*2^(r-1) and diverges. The counterexample refutes the unweighted conditioned bridge, not the FEI conjecture. Constants have v=0 and Q is undefined.",common+["f nonconstant; v>0 for the conditioning identity","Explicit subcube counterexample uses r>=2"],proof("C003")),
entry("coordinate","spectral-coordinate-entropy-charging-counterexample","lemma","Spectral coordinate entropy cannot be uniformly charged to influence","For f_r=1-2*1_(x_1=...=x_r=0) on the uniform F_2^r cube, r>=2, its squared Fourier law S has Pr[i in S]=I_i(f_r)=a=2^(1-r) for every i. The first spectral-coordinate chain entropy increment in any deterministic ordering is h2(a), and h2(a)/I_i>=r-1. Thus no absolute C bounds every chain-rule increment H(1_(i in S)|previously exposed spectral coordinates) by C I_i(f) for all Boolean f. Also sum_i h2(I_i)/I is unbounded on this family although H/I tends to 4. For distinct i,j and r>=3, Pr[i,j in S]=2^-r, whereas Pr[i in S]Pr[j in S]=2^(2-2r); spectral coordinates are dependent despite independent input bits. The assertion does not rule out adaptive or block entropy budgets.",common+["Explicit coordinate-subcube family","Deterministic coordinate ordering","r>=3 for strict pair dependence"],proof("C004")),
entry("gap","general-fei-mass-weighted-spectral-entropy-gap","concept","Unresolved mass-weighted entropy gap beyond affine spectra","DRAFT unresolved route, not a theorem: for arbitrary nonconstant uniform Boolean f, let v=Var(f)>0 and Q be its nonempty conditioned squared Fourier law. General FEI would require a dimension-free bound h2(v)+v H(Q)<=C*v*E_Q|S|. The affine-indicator proof controls only uniform nonzero dual-subspace spectra. The false inequalities H(Q)<=C I(f) and a uniform charge of every individual chain entropy increment to that coordinate's influence cannot supply the missing estimate. A next proof step is a block exposure rule that preserves the factor v and explicitly permits correlated spectral coordinates. No full FEI resolution is claimed.",common+["Proposed route only; general entropy estimate unproved"])
]

relations=[
{"from_key":"affine","to_key":"defs","kind":"depends_on","rationale":"The affine formula uses the normalized squared Fourier law in the definition: 'I(f)=sum_s |s| fhat(s)^2' and 'H(f)=sum_s fhat(s)^2 log2(1/fhat(s)^2)'."},
{"from_key":"sharp","to_key":"affine","kind":"depends_on","rationale":"The sharp theorem's exact ratio 'H_r/(2pm)' uses the affine lemma's supporting end 'I(f)=2pm' and its displayed entropy formula, together with m>=r."},
{"from_key":"conditioning","to_key":"affine","kind":"depends_on","rationale":"The conditioned counterexample uses the affine lemma's equal nonzero Fourier squares; this gives the supporting conclusion 'Q is uniform on 2^r-1 nonzero vectors'."},
{"from_key":"coordinate","to_key":"affine","kind":"depends_on","rationale":"The coordinate lemma uses the affine supporting end 'Each active coordinate has influence 2p' and counts dual vectors to establish its entropy and joint-probability ends."},
{"from_key":"gap","to_key":"conditioning","kind":"semantic_association","rationale":"The unresolved route retains the proved conditioning end 'H(f)=h2(v)+v H(Q)' and does not use the refuted unweighted bridge."}
]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w510","bundle_slug":"p0162-affine-sharp-boundary-w510-001","entries":entries,"relations":relations}
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
assert 0<len(entries)<=200
keys={e["key"] for e in entries}
assert len(keys)==len(entries)
for e in entries:
    assert required<=set(e)
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",e["logical_name"])
    assert e["source"]["license"]=="owner-own-work"
    assert bool(e["proof_text"]) if e["kind"] in ("lemma","theorem") else e["proof_text"] is None
for rel in relations:
    assert rel["from_key"] in keys and rel["to_key"] in keys
    assert rel["kind"] in ("depends_on","semantic_association")
graph={key:[r["to_key"] for r in relations if r["from_key"]==key and r["kind"]=="depends_on"] for key in keys}
def walk(key,ancestors):
    assert key not in ancestors,"cyclic depends_on"
    for nxt in graph[key]:
        walk(nxt,ancestors|{key})
for key in keys:
    walk(key,set())
serialized=json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
(ROOT/"DRAFT_BUNDLE.json").write_text(serialized,encoding="utf-8")
INBOX.mkdir(parents=True,exist_ok=True)
final=INBOX/"bundle_001.json"
part=INBOX/"bundle_001.json.part"
if final.exists() or part.exists():
    raise SystemExit("Inbox output already exists; refusing to overwrite another artifact")
part.write_text(serialized,encoding="utf-8")
part.rename(final)
states={"bundle":str(final),"prepared":True,"submitted":True,"reviewed":{"state":"pending","reviewer":"w512","adversary":"w511"},"ingested":{"state":"not performed by w510; coordinator action unverified"},"retrievable":{"state":"not tested; no live-store write or integration run"},"entries":len(entries),"relations":len(relations),"claim_ids":["P0162-w510-C001","P0162-w510-C002","P0162-w510-C003","P0162-w510-C004"],"author_proof_only":True,"novelty":"not claimed","full_fei_solved":False,"mesh_output_claim":"clm-848fa51e9e"}
(ROOT/"BUNDLE_STATES.json").write_text(json.dumps(states,indent=2)+"\n",encoding="utf-8")
print(json.dumps(states))
