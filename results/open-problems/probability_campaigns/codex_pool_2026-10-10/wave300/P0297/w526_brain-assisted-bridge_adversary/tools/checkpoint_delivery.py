"""Save and validate this worker's small, unreviewed draft checkpoint."""

import difflib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMESPACE = "probability.lqg"

def entry(key, title, statement, assumptions, claim, primary):
    return {
        "key": key, "namespace": NAMESPACE, "logical_name": key,
        "kind": "concept", "title": title, "statement": statement,
        "proof_text": None, "assumptions": assumptions,
        "domain": "probability / LQG / finite Gaussian path controls",
        "source": {
            "source_id": "owner-own-work:P0297:w526:"+claim,
            "url": primary,
            "revision": "campaign-2026-10-10-draft-independent-review-pending",
            "license": "owner-own-work",
            "excerpt": "Own campaign deduction "+claim+"; independent check pending. URL supplies target context, not a proof of the new control.",
        },
    }

def main():
    entries = [
        entry("lqg-field-dependent-kpz-counterexamples", "DRAFT: why metric KPZ needs field independence",
              "Unreviewed campaign deduction from Gwynne-Pfeffer Theorem 1.4 and Corollary 1.7. Fix gamma in (0,2), a whole-plane GFF h and a nonempty deterministic planar domain U. Write Q=2/gamma+gamma/2 and xi=gamma/d_gamma for the canonical gamma-LQG metric D_h. The gamma-thick points X in U have Euclidean Hausdorff dimension 2-gamma^2/2 and D_h dimension d_gamma almost surely. Applying the independent-set equality dim_E X=xi Q dim_D X-(xi^2/2)(dim_D X)^2 to this field-dependent X instead gives 2; the residual is gamma^2/2. At gamma=sqrt(8/3), applying that equality to a nonconstant D_h-geodesic of intrinsic dimension 1 would instead give Euclidean dimension 3/4, whereas a connected continuous image with distinct endpoints has Euclidean dimension at least 1 by a Lipschitz distance projection. These are obstructions to deleting independence, not values of the general d_gamma.",
              ["Canonical subcritical LQG metric", "Gamma is fixed in (0,2)", "Thick points use circle-average limits", "Known d_sqrt(8/3)=4 for the geodesic control"],
              "C526.2-C526.3", "https://arxiv.org/abs/1905.11790"),
        entry("lfpp-absolute-softmin-bias-control", "DRAFT: diagonal soft-min bias and endpoint cancellation",
              "Unreviewed finite-Gaussian control. For each integer n>=1 set L_n=beta_n=n and K_n=2^(n^2). Take K_n distinct singleton paths of unit weights whose centered Gaussian fields all equal one common standard normal Z. The covariance is PSD with maximum diagonal 1. At fixed xi>=0 the hard log minimum is xi Z, but the soft minimum F_beta=-(1/beta)log sum_p exp(-f_p), with its exponent correctly interpreted as exp(-beta f_p), equals xi Z-n log 2 at beta_n=n. Thus normalized expectations differ by -log 2 although beta_n tends to infinity. This attains the absolute smoothing error bound. The bias does not depend on xi and cancels in endpoint differences; this control alone does not refute an integrated endpoint reduction.",
              ["Finite path model; no planar LFPP realization claimed", "Positive unit weights", "Perfectly correlated Gaussian singleton fields", "Fixed xi>=0"],
              "C526.5", "https://arxiv.org/abs/2109.01252"),
        entry("lfpp-integrated-softmin-counterexample", "DRAFT: integrated response needs uniform smoothing control",
              "Unreviewed analytic finite-Gaussian counterexample. For n>=1 let L_n=beta_n=n and M_n=2^(n^2). Take M_n distinct singleton paths with deterministic zero Gaussian fields and weight exp(n), plus one path with M_n independent N(0,n) fields and vertex weights 1/M_n. The centered Gaussian covariance is PSD diagonal with maximum variance v_n=n=O(L_n). Put f_n(xi)=log[(1/M_n) sum_i exp(xi sqrt(n) Z_i)] and H_n(xi)=min(n,f_n(xi)). The beta_n soft minimum is F_n(xi)=-(1/n)log[exp(-n^2(1-log 2))+exp(-n f_n(xi))]. At endpoints xi=0 and xi=2, the normalized hard expected difference tends to 1, while the normalized soft expected difference tends to 1-log 2. The hard medians at those endpoints are 0 and n for all sufficiently large n. For S_n=exp(f_n(2)), its mean is exp(2n), relative variance is (exp(4n)-1)/M_n, and Jensen bounds its negative logarithmic part using 2 sqrt(n) Z_bar; these bounds prove the stated limits. The fixed-network Gaussian interpolation integral equals the soft endpoint difference. Therefore beta_n->infinity, v_n=O(L_n), and convergent hard-min endpoint medians do not by themselves justify the integrated reduction. This is a general finite-path control, not a planar LFPP computation.",
              ["Finite family of nonempty paths with positive deterministic weights", "Allow deterministic zero Gaussian coordinates", "Independent long-path Gaussian coordinates of variance n", "Fixed endpoints xi=0 and xi=2", "No uniform smoothing-error premise imposed"],
              "C526.6", "https://arxiv.org/abs/2109.01252"),
        entry("lfpp-uniform-smoothing-error-bridge", "DRAFT: sufficient entropy control for a finite-to-scale reduction",
              "Unreviewed bridge checklist. For a finite nonempty family of real path log costs f_p(y), beta>0 and K paths, define H(y)=min_p f_p(y) and F_beta(y)=-(1/beta)log sum_p exp(-beta f_p(y)). Then 0<=H(y)-F_beta(y)<=log K/beta for every y. For growing families, L_n->infinity and log K_n/(beta_n L_n)->0 therefore suffice for normalized expected endpoint differences to agree whenever the hard endpoint limits exist and the costs are integrable. A sharper effective-entropy estimate may replace this sufficient condition. The finite Gaussian response identity also requires retaining the negative beta times covariance of path gradients; its two nonnegative pieces cannot be separated or discarded just because one route wins almost surely. Neither the entropy bound nor concentration evaluates the actual planar-LFPP normalization exponent.",
              ["Finite nonempty path families", "Positive beta and normalization L_n", "Integrable endpoint log costs", "Uniform entropy error tends to zero for the stated transfer"],
              "C526.4-C526.6", "https://arxiv.org/abs/2109.01252"),
    ]
    # Correct the explicit soft-min formula without an explanatory alternative.
    entries[1]["statement"] = entries[1]["statement"].replace(
        "F_beta=-(1/beta)log sum_p exp(-f_p), with its exponent correctly interpreted as exp(-beta f_p),",
        "F_beta=-(1/beta)log sum_p exp(-beta f_p)",
    )
    relations = [
        {"from_key": entries[2]["key"], "to_key": entries[1]["key"], "kind":"cites",
         "rationale":"Absolute control: 'bias does not depend on xi and cancels'. Integrated control: endpoint limits are '1' and '1-log 2'. The second construction supplies the endpoint distinction missing from the first."},
        {"from_key": entries[2]["key"], "to_key": entries[3]["key"], "kind":"cites",
         "rationale":"The control has log K_n/(beta_n L_n) tending to log 2, while the sufficient bridge explicitly requires that ratio to tend to zero. The control is excluded by the bridge premise."},
        {"from_key": entries[2]["key"], "to_existing_logical":"math:probability.gaussian:gaussian-poincare-inequality", "kind":"cites",
         "rationale":"Poincare card: 'f be locally Lipschitz with f and its gradient in L^2'. The finite path minimum is globally sqrt(v_n) times xi Lipschitz in standard Gaussian coordinates and integrable; variance concentration still does not fix its soft-min bias."},
        {"from_key": entries[2]["key"], "to_existing_logical":"math:probability.gaussian:gaussian-integration-by-parts-and-steins-characterisation", "kind":"cites",
         "rationale":"Gaussian card: 'X is centred Gaussian' and differentiability with 'appropriate integrability'. At every fixed finite n and beta_n the smooth path objective has bounded derivatives, so the interpolation integral equals its soft endpoint difference, which this control computes."},
        {"from_key": entries[3]["key"], "to_existing_logical":"math:probability.core:attempt-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity", "kind":"cites",
         "rationale":"Prior attempt: 'It does not calculate xi for other parameters.' Current checklist: concentration and uniform smoothing do not evaluate the actual planar-LFPP exponent. Both preserve the same unresolved numerical metric bridge."},
        {"from_key": entries[0]["key"], "to_existing_logical":"math:probability.core:open-problem-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity", "kind":"cites",
         "rationale":"Problem card asks for the 'almost sure Hausdorff dimension d_gamma'. The dependent-set controls invalidate uses of independent KPZ that would purport to calculate that metric dimension; they leave the target unresolved."},
    ]
    bundle={"spec":"mathbrain-draft-v1","author_agent":"w526","bundle_slug":"p0297-adversary-uniform-smoothing-20261010","entries":entries,"relations":relations}
    required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
    for e in entries:
        assert required <= e.keys() and e["kind"]=="concept" and e["proof_text"] is None
        assert e["source"]["license"]=="owner-own-work"
    keys={e["key"] for e in entries}
    for r in relations:
        assert r["from_key"] in keys and r["kind"]=="cites"
        assert (r.get("to_key") in keys) or r.get("to_existing_logical", "").startswith("math:")
    claims=[json.loads(l) for l in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(claims)==6 and all(c["review_state"]=="unreviewed" for c in claims)
    data=json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
    (ROOT/"DRAFT_BUNDLE_001.json").write_text(data,encoding="utf-8")
    inbox=Path("~/math-brain-inbox/w526")
    inbox.mkdir(parents=True,exist_ok=True)
    target=inbox/"bundle_001.json"
    if target.exists():
        assert target.read_text(encoding="utf-8")==data, "Existing draft differs; do not overwrite"
    else:
        part=inbox/"bundle_001.part"
        assert not part.exists(), "Unexpected part file; preserve it"
        part.write_text(data,encoding="utf-8")
        os.rename(part,target)
    lifecycle={"submitted":{"state":True,"path":str(target)},"reviewed":{"state":False,"reviewer":"w527"},"ingested":{"state":False},"retrievable":{"state":False},"entries":len(entries),"relations":len(relations)}
    (ROOT/"BUNDLE_LIFECYCLE.json").write_text(json.dumps(lifecycle,indent=2),encoding="utf-8")
    patches=ROOT/"patches";patches.mkdir(exist_ok=True)
    new=(ROOT/"staged/p0297_recall_gate.py").read_text(encoding="utf-8").splitlines(keepends=True)
    live="~/.claude/dreaming/p0297_recall_gate.py"
    diff="".join(difflib.unified_diff([],new,fromfile="a/"+live,tofile="b/"+live))
    (patches/"01_p0297_recall_gate.diff").write_text(diff,encoding="utf-8")
    hook={"id":"lqg-uniform-smoothing-w526-01","area":"math","event":"stage-start","cue":"soft.?min|smoothing.*beta|beta.*(network|mesh|path)","fire_when":"A proof passes from finite Gaussian path soft-minima to a growing-network normalized endpoint limit using only beta_n->infinity.","silent_when":"A fixed finite path family is kept fixed during beta->infinity, or a uniform entropy/error bound is already supplied.","text":"Before a growing-path soft-min limit, bound log|P_n|/(beta_n L_n) or a sharper entropy error. The C526.6 control has v_n=L_n=n and beta_n=n yet hard and soft endpoint limits differ by log 2. This is a draft lead; check its premises.","evidence":"~/brain_workers/w526/CLAIMS.jsonl:C526.6; FINITE_BRIDGE_INDEPENDENT.md; independent review pending","proposer":"w526"}
    assert len(hook["text"])<=300
    hook_line=json.dumps(hook,ensure_ascii=False)+"\n"
    (ROOT/"HOOK_PROPOSAL.jsonl").write_text(hook_line,encoding="utf-8")
    proposal=Path("~/primary_directive/hooks1000/proposals/math-w526.jsonl")
    proposal.parent.mkdir(parents=True,exist_ok=True)
    existing=proposal.read_text(encoding="utf-8") if proposal.exists() else ""
    if not any(json.loads(line).get("id")==hook["id"] for line in existing.splitlines() if line.strip()):
        with proposal.open("a",encoding="utf-8") as f:f.write(hook_line)
    receipt={"draft_bundle":str(target),"entries":len(entries),"relations":len(relations),"claims":len(claims),"local_validation":"required fields, draft concept kinds, relation endpoints, owner-own-work license, and JSON parse passed","mathematical_review":"pending w527","hook_proposal":str(proposal),"patch":str(patches/"01_p0297_recall_gate.diff"),"formal_check":None}
    (ROOT/"evidence/delivery_receipt.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
    print(json.dumps(receipt))

if __name__=="__main__":main()
