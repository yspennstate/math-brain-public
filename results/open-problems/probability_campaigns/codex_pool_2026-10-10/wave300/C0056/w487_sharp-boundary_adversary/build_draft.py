"""Prepare a concept-only bundle, with exact supported relation ends."""
import difflib
import hashlib
import json
from pathlib import Path

folder=Path(__file__).resolve().parent
source={"source_id":"owner-own-work:w487:c0056-boundary-20261010",
        "url":"file:///~/brain_workers/w487/ATTEMPT.md",
        "revision":"campaign-author-derivation-2026-10-10-unpromoted",
        "license":"owner-own-work (campaign derivation; independent/model gates separate)","excerpt":None}
entries=[]
def entry(key,name,title,statement,assumptions,kind="concept"):
    item={"key":key,"namespace":"analysis.spectral","logical_name":name,"kind":kind,
          "title":title,"statement":statement,"proof_text":None,"assumptions":assumptions,
          "domain":"probability and spectral theory","source":dict(source)}
    entries.append(item)

entry("poisson","spectral-poisson-transform-unnormalized","Unnormalized spectral Poisson transform",
      "For a probability Borel measure mu on R and eta>0, define F_eta(E)=integral_R eta/((t-E)^2+eta^2) dmu(t). For a unit vector's spectral measure of a self-adjoint H, F_eta(E)=Im <u,(H-E-i eta)^(-1)u>. The kernel has total Lebesgue integral pi.",
      ["mu is a probability Borel measure","eta>0","unit-vector spectral measure when H is used"],"definition")
entry("atomic","annealed-first-poisson-moment-does-not-imply-quenched-ac","Annealed first moment can conceal atomic spectral measures",
      "DRAFT concept backed by an author derivation, not a promoted theorem. For every lambda>0, the diagonal operator H delta_x=lambda V_x delta_x on ell^2(Z^3), with iid uniform[-1,1] V_x and no hopping, has atomic spectral measures for every realization. Yet sup_(E real,eta>0) E Im <delta_x,(H-E-i eta)^(-1)delta_x> <= pi/(2lambda). A bounded annealed first moment alone therefore does not imply quenched ac. This does not refute the Anderson operator with hopping.",
      ["lambda>0","iid uniform[-1,1] site variables","diagonal operator with no hopping"])
entry("criterion","annealed-integrated-poisson-p-moment-ac-criterion","Sharp power-moment boundary for a quenched ac criterion",
      "DRAFT concept backed by an author derivation, not a promoted theorem. Let mu_omega be random probability Borel measures, I a bounded open interval, 1<p<infinity, and eta_n>0 a deterministic sequence tending to zero. Set F_n(omega,E)=integral eta_n/((t-E)^2+eta_n^2) dmu_omega(t), jointly measurable. If sup_n E integral_I F_n^p <= C<infinity, then almost surely mu_omega|I=rho_omega dE with rho_omega in Lp(I), and E integral_I rho_omega^p <= C/pi^p. For 0<p<=1, integral_I F_eta^p <= |I|^(1-p)pi^p holds for every probability measure, including atoms; those power bounds alone cannot imply ac. p>1 is sufficient, not necessary for ac, and the criterion may yield zero mass on I.",
      ["random probability Borel measures","bounded open I","deterministic eta_n -> 0","joint measurability","1<p<infinity for the sufficient criterion"])
entry("second","uniform-diagonal-imaginary-resolvent-second-moment-divergence","Atomic model has a divergent second imaginary-resolvent moment",
      "DRAFT concept backed by an author derivation, not a promoted theorem. Let V be uniform[-1,1], lambda>0, eta>0 and F_eta=eta/((lambda V)^2+eta^2). Then E F_eta=arctan(lambda/eta)/lambda and E F_eta^2=1/(2(lambda^2+eta^2))+arctan(lambda/eta)/(2lambda eta). Consequently eta E F_eta^2 -> pi/(4lambda), while E F_eta -> pi/(2lambda), as eta -> 0 at fixed lambda.",
      ["lambda>0 fixed","eta>0","V uniform[-1,1]"])
entry("bath","anderson-schur-bath-negative-imaginary-width-moment","Full deleted-site bath controls the stronger spectral moment",
      "DRAFT concept backed by an author derivation, not a promoted theorem. For H=A+lambda V on ell^2(Z^3), A nearest-neighbor adjacency and V iid uniform[-1,1], fix x, z=E+i eta, lambda>0, eta>0. With H^(x) the deleted-site compression and b the neighbor-coupling vector, set Sigma=<b,(H^(x)-z)^(-1)b>, a=E+Re Sigma and B=eta+Im Sigma>0. Conditional on all sites except V_x, Im G_xx=B/((lambda V_x-a)^2+B^2). Its conditional first moment is <=pi/(2lambda). For 1<p<infinity and K_p=integral_R(1+u^2)^(-p)du, its conditional p moment is <=K_p B^(1-p)/(2lambda); on |a|<=lambda/2 and B<=lambda/2 it is >=2^(-p)B^(1-p)/lambda. An eta-uniform integrated p moment thus requires a uniform resonance-weighted negative moment of B. No such estimate is supplied here, and the six neighbors are not independent branches.",
      ["lambda>0","eta>0","iid uniform[-1,1] site law","full deleted-site compression","nearest-neighbor adjacency with zero diagonal","1<p<infinity"])
entry("goe","free-lattice-ac-does-not-imply-periodic-goe-statistics","Free ac spectrum does not supply periodic-box GOE statistics",
      "DRAFT concept backed by an author derivation, not a promoted theorem. Free nearest-neighbor adjacency on Z^3 has absolutely continuous spectral measures. In periodic boxes of odd side L its eigenvalues are 2 sum_j cos(2pi k_j/L), k in (Z/LZ)^3. In any fixed nonempty interval compactly inside (-6,6), k -> -k pairs all momenta and forces at least half of the sorted adjacent spacings to be zero as the bulk count diverges. Strictly monotone unfolding preserves those coincidences, obstructing GOE bulk spacing statistics. This uses lambda=0 and does not refute fixed positive-disorder C0056.",
      ["lambda=0","periodic odd-L cubes","fixed nonempty interval compactly inside (-6,6)"])
entry("status","c0056-ac-and-goe-scope-status-2026-10-10","C0056 has separate ac and GOE obligations; current status unknown",
      "DRAFT source-status concept, not a theorem verdict. The recovered C0056 intake asks for both weak-disorder infinite-volume ac spectrum on Z^3 and GOE local statistics of finite-volume restrictions. Bourgade's 2018 survey uses centered iid variance-one sites and periodic boxes. A September 23, 2026 primary manuscript claims purely ac nonzero spectral restriction for iid uniform[-1,1] disorder at each fixed sufficiently small positive coupling, on a fixed interval above -6 in d=3. That claim's mathematical review gates are not established in this packet, and its stated theorem does not establish GOE statistics. Current openness is UNKNOWN; keep the two obligations and the law normalization explicit.",
      ["status checked 2026-10-10","primary manuscript is a claim, not an accepted proof receipt","no universal law-class or GOE quantifiers supplied by the qualitative intake"])

relations=[
 {"from_key":"atomic","to_key":"poisson","kind":"depends_on","rationale":"The atomic entry bounds 'E Im <delta_x,(H-E-i eta)^(-1)delta_x>'; the definition identifies 'F_eta(E)=Im <u,(H-E-i eta)^(-1)u>' and kernel integral pi."},
 {"from_key":"criterion","to_key":"poisson","kind":"depends_on","rationale":"The criterion states 'C/pi^p'; the transform definition states 'The kernel has total Lebesgue integral pi', fixing the normalization in its approximate-identity proof."},
 {"from_key":"second","to_key":"atomic","kind":"specializes","rationale":"The second-moment entry specifies 'F_eta=eta/((lambda V)^2+eta^2)' at E=0; the atomic entry uses the diagonal uniform model's scalar imaginary resolvent for every E."},
 {"from_key":"bath","to_key":"atomic","kind":"analogous_to","rationale":"The bath entry states 'Its conditional first moment is <=pi/(2lambda)'; the diagonal entry has the same bound while its spectral measures are atomic. This relates the averaging obstruction without treating the no-hopping model as the positive-hopping target."},
 {"from_key":"goe","to_key":"status","kind":"semantic_association","rationale":"The free entry states 'does not refute fixed positive-disorder C0056'; the status entry keeps 'both weak-disorder infinite-volume ac spectrum on Z^3 and GOE local statistics' as separate obligations."},
]
store_rows=[json.loads(line) for line in (folder/"STORE_MATCHES.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
if store_rows:
    parent=store_rows[0]; meta=json.loads(parent["metadata_json"])
    relations.append({"from_key":"status","to_existing_logical":meta["logical_id"],"kind":"semantic_association",
      "rationale":"The existing C0056 card states 'and GOE local statistics for its finite-volume restriction' and 'Current status unverified as of 2026-09-07'; the new status concept retains the GOE obligation and records 'Current openness is UNKNOWN' after recovering the dated primary claim. No refutation or solution edge is proposed."})

bundle={"spec":"mathbrain-draft-v1","author_agent":"w487","bundle_slug":"c0056-spectral-moment-boundary-20261010","entries":entries,"relations":relations}
local=folder/"bundle_001.json"
local.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
patches=folder/"patches"; patches.mkdir(exist_ok=True)
target="~/math-brain-inbox/w487/bundle_001.json"
patch="".join(difflib.unified_diff([],local.read_text(encoding="utf-8").splitlines(keepends=True),
    fromfile="a/"+target,tofile="b/"+target))
(patches/"01_c0056_boundary_draft.diff").write_text(patch,encoding="utf-8")

seen={e["key"] for e in entries}
assert len(seen)==len(entries)<=200
assert all(e["kind"] in {"concept","definition"} and e["proof_text"] is None for e in entries)
assert all(all(isinstance(e["source"][f],str) and e["source"][f] for f in ("source_id","url","revision","license")) for e in entries)
assert all(r["from_key"] in seen and (r.get("to_key") in seen or r.get("to_existing_logical"," ").startswith("math:")) for r in relations)
print(json.dumps({"local_draft":str(local),"entries":len(entries),"relations":len(relations),"theorems":0,"lemmas":0,"definitions":1,"concepts":len(entries)-1}))

# Freeze only the exact named author proof, not a corpus or review.
author_path=Path(r"~\brain_workers\w486\ATTEMPT.md")
body=author_path.read_bytes()
(folder/"W486_AUTHOR_PROOF_SNAPSHOT.md").write_bytes(body)
audit=json.loads((folder/"AUDIT_W486.json").read_text(encoding="utf-8"))
audit["artifact_sha256"]=hashlib.sha256(body).hexdigest()
audit["snapshot"]="W486_AUTHOR_PROOF_SNAPSHOT.md"
(folder/"AUDIT_W486.json").write_text(json.dumps(audit,indent=2)+"\n",encoding="utf-8")
claim={"row_id":"S1.487.6","target":"C0056","kind":"author_proof_audit","statement":"KEEP scoped w486 L1-L3: for bounded iid real site potentials, M=ess sup |V_x|>0, E in the free band, fixed lambda>0 and eta>0, the unrenormalized Born resolvent expansion converges in operator norm exactly when eta>lambda M; at equality its terms do not vanish.","assumptions":["bounded iid real site law","free nearest-neighbor hopping","E in [-2d,2d]","lambda>0 and eta>0 fixed before coherent-cube limits","a.s. rare cubes intersected with a.s. all-site bound"],"source":str(author_path),"source_sha256":audit["artifact_sha256"],"proof":"ATTEMPT.md, Adversarial check; AUDIT_W486.json","independent_reviewer":"w487 native audit of w486 author proof; model identities UNKNOWN","remaining_gap":"No spectral-type or GOE conclusion; model-identity gate unsatisfied","status":"proved special case","review_status":"scoped native KEEP; identity-gated promotion unavailable","novelty":"not claimed"}
with (folder/"CLAIMS.jsonl").open("a",encoding="utf-8") as stream:
    existing={json.loads(line)["row_id"] for line in (folder/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()}
    if claim["row_id"] not in existing: stream.write(json.dumps(claim)+"\n")
    bykey={e["key"]:e for e in entries}
    for n,r in enumerate(relations,1):
        rowid=f"S1.487.E{n}"
        if rowid in existing: continue
        destination=bykey.get(r.get("to_key"))
        endquote=destination["statement"] if destination else store_rows[0]["body"]
        row={"row_id":rowid,"target":"C0056","kind":"draft_relation","statement":r,
          "supporting_from_quote":bykey[r["from_key"]]["statement"],"supporting_to_quote":endquote,
          "source":"bundle_001.json and STORE_MATCHES.jsonl for the external end","proof":"Exact quoted ends support only the stated relation kind; all internal theorem-like claims remain concepts.",
          "assumptions":["new entries retain DRAFT concept status","external end resolved read-only before proposing link"],
          "independent_reviewer":"w488 / integrator pending","remaining_gap":"Relation review and ingestion not complete","status":"sketch"}
        stream.write(json.dumps(row,ensure_ascii=False)+"\n")
