"""Stage this worker's claim ledger, review packet, and deployable draft diffs."""
from pathlib import Path
import difflib
import json

root = Path(__file__).resolve().parent
patches = root / "patches"
patches.mkdir(exist_ok=True)
rows = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
ids = {r["claim_id"] for r in rows}
def add(number,statement,assumptions,proof,gap,source=None,epistemic_kind="unreviewed analytic proof"):
    cid=f"S1.w373.{number:03d}"
    if cid in ids:
        return
    rows.append({"claim_id":cid,"statement":statement,"assumptions":assumptions,
        "source":source or {"source_id":f"owner-own-work:w373:P0110:{number}","license":"owner-own-work","path":"ATTEMPT.md"},
        "proof_or_counterexample":proof,"independent_reviewer":"w374; verdict pending",
        "remaining_gap":gap,"status":"sketch","epistemic_kind":epistemic_kind,
        "submitted":False,"reviewed":False,"ingested":False,"retrievable":False})
    ids.add(cid)

add(2,"For the centered symmetric family with masses (1-1/n)/2 at +/-n^(1/3) and 1/(2n) at +/-n^(2/3), the lower variance exponent is 1/3 while the uniform upper exponential-moment exponent is 2/3.",
    ["Integer n>=2; exponent definitions are the analogous all-n moment thresholds, not FPP exponents."],
    "INDEPENDENT.md: Var X_n=(1-1/n)n^(2/3)+n^(1/3). For a<2/3, E exp(alpha|X_n|/n^a)>=exp(alpha n^(2/3-a))/n diverges for every alpha>0; for a>=2/3 it is <=exp(alpha).",
    "Independent check pending. No iid lattice-FPP realization is supplied; only the variance-to-exponential-tail inference is refuted.")
add(3,"On a four-edge square graph with iid Uniform[1,2] weights and opposite-corner endpoints, let A,B be its two route costs. Conditional on A<B, P(A<=3)=P(B>=3)=3/4 and P(A<=3,B>=3)=1/2; the conditional product 9/16 is false.",
    ["Finite square graph only; disjoint two-edge routes; iid continuous Uniform[1,2]; condition on the top route being the unique geodesic."],
    "ATTEMPT.md, Obstruction B: each cost has median 3, exchangeability splits each same-median quadrant in half, and the cross quadrant has probability 1/4 and is contained in A<B. Divide by P(A<B)=1/2. verification.json also checks an atomic 16-state analogue.",
    "Independent check pending. Does not refute unconditional independence in deterministic disjoint domains or establish a full-lattice counterexample.")
add(4,"For nearest-neighbor FPP on Z^d, d>=2, with every edge weight in [1,2], D(0,e1)=0 for every environment, so a strictly positive lower bound inf_{v!=0} ED(0,v)/|v|^b>0 is impossible for any real b.",
    ["Undirected nearest-neighbor lattice; positive bounded weights in [1,2]; D is maximum distance of a minimizing path from the endpoint segment."],
    "ATTEMPT.md, Obstruction C: the direct edge costs <=2, every other simple path has at least three edges and costs >=3, and loops have positive cost. The direct edge is therefore the unique minimizing path.",
    "Independent check pending. A sufficiently-large-distance lower bound, as in Chatterjee (A4), is untouched; do not reject the KPZ target.")
add(5,"High-probability agreement of costs in [n,2n] does not imply variance transfer: T_n=n and Y_n=n+nB_n with B_n Bernoulli(1/n) agree with probability 1-1/n but have Var T_n=0, Var Y_n=n-1, and E(Y_n-T_n)^2=n.",
    ["Integer n>=2; abstract cost coupling, not a constructed FPP environment."],
    "ATTEMPT.md, Obstruction D; verification.json enumerates the exact two-state coupling. The rare discrepancy has magnitude n and probability 1/n.",
    "Independent check pending. The actual cylinder route must control its L2 discrepancy relative to the passage-time standard deviation, not just the failure probability.")
add(6,"The norm g(x)=max(||x||_1,(3/2)||x||_infinity) has square-lattice symmetries and ||x||_1<=g(x)<=(3/2)||x||_1, yet for even n and w+1<=n/4, z=(n/2,w+1) gives g(z)+g(ne1-z)-g(ne1)=0 outside the width-w cylinder.",
    ["A norm countermodel on R^2; n even and w>=1 integer; no realization as an iid FPP time constant is claimed."],
    "GEOMETRY_OBSTRUCTION.md proves the norm axioms and evaluates g(ne1)=3n/2, g(z)=g(ne1-z)=3n/4. It fails every positive c w^2/n bend despite meeting the elementary candidate-law bounds.",
    "Independent check pending. FPP-specific curvature and nonrandom-error control remain missing inputs; this countermodel is not an FPP law.")
add(7,"The frozen w372 packet's unconditional cylinder variance-transfer bound 2(s-2delta)_+^2<=Var(F1-F2)<=2(s+2delta)^2 and conditional mean-gap localization bound survive this adversarial audit under their stated premises.",
    ["F_i have the same square-integrable distribution with sd s; G_i iid square-integrable; Delta_i=G_i-F_i>=0 have equal mean and L2 norm <=delta.",
     "Localization additionally requires a>=0 and fixed alpha,M with uniform exponential centered moments, plus a positive deterministic mean gap H_n at all possible departing vertices."],
    "PAIRED_AUDIT.md rederives the central L2 inequality and the deterministic-vertex Markov/union bound. Snapshot hash identifies only the bytes; it is not proof. No input independence is inferred after selection.",
    "w374's independent referee verdict remains pending. Actual Uniform[1,2] mean gap and global exponent matching are unproved.",
    {"path":"paired_ATTEMPT_snapshot.md","sha256":"9870466d65baaac52c448f24c098dcabd75233cae13bafa88dd9d92c06ef8627","locator":"L2 and L4; snapshot lines 31-81"},"adversarial audit of original proof")
add(8,"For iid Uniform[1,2] FPP on Z^2, existence of simultaneous uniform matching upper exponential-moment and lower variance/mean exponents supplies a sufficient reduction to chi=2xi-1 through Chatterjee Theorem 1.1; the reduction does not prove existence of those inputs.",
    ["All four epsilon-slack bounds in ATTEMPT.md hold with constants independent of endpoints; lower estimates use a sufficiently-large-distance cutoff.",
     "Continuous nearly-gamma law and finite moment generating function as in the published theorem."],
    "ATTEMPT.md specifies all quantifiers, squeezes chi_a=chi_b and xi_a=xi_b, and applies the published conditional theorem. Its additional relative-tail route is conditional on a tail estimate at the actual variance scale.",
    "The four matching estimates and the relative-tail input are not proved for this law; current openness and novelty remain UNKNOWN/no claim.",
    {"url":"https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p07-p.pdf","locator":"Theorem 1.1 (A1)-(A4)","proof_path":"ATTEMPT.md"},"proved reduction with unproved input")
(root / "CLAIMS.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows),encoding="utf-8")

def entry(key,logical,title,statement,assumptions,cid):
    return {"key":key,"namespace":"probability.fpp","logical_name":logical,"kind":"concept","title":title,
            "statement":"DRAFT audit concept; independent mathematical review pending. "+statement,
            "proof_text":None,"assumptions":assumptions,"domain":"probability theory",
            "source":{"source_id":f"owner-own-work:w373:P0110:{cid}","url":f"urn:owner-work:w373:P0110:{cid}",
                      "revision":"unreviewed-draft-2026-10-10","license":"owner-own-work (campaign obstruction; no novelty claim)","excerpt":None}}

entries=[
    entry("tail-mismatch","variance-power-law-does-not-determine-exponential-tail-exponent","Variance scaling does not determine exponential-tail scaling",rows[1]["statement"]+" This is an abstract family, not FPP; it refutes inferring the strong upper exponent solely from the variance exponent.",rows[1]["assumptions"],"S1.w373.002"),
    entry("selected-routes","geodesic-selection-couples-disjoint-route-costs","Selecting a geodesic couples disjoint route costs",rows[2]["statement"]+" The iid disjoint route costs are independent before conditioning; conditioning on which route wins destroys that independence. Deterministic restricted domains computed without such conditioning remain a valid independence route.",rows[2]["assumptions"],"S1.w373.003"),
    entry("short-endpoint","bounded-positive-fpp-short-endpoint-zero-wandering","Bounded positive FPP has zero wandering at a short endpoint",rows[3]["statement"]+" The direct edge costs at most 2 while every alternative simple path costs at least 3. This does not refute an asymptotic lower wandering bound with a sufficiently-large-distance cutoff.",rows[3]["assumptions"],"S1.w373.004"),
    entry("variance-transfer","high-probability-cost-agreement-does-not-transfer-variance","High-probability cost agreement does not transfer variance",rows[4]["statement"]+" A cylinder localization probability must be paired with an L2 discrepancy small relative to the true standard deviation. No FPP realization or impossibility result is claimed.",rows[4]["assumptions"],"S1.w373.005"),
    entry("norm-bend","symmetric-bounded-norm-does-not-imply-axial-curvature","Lattice symmetry and norm bounds do not force axial curvature",rows[5]["statement"]+" The maximum of these two norms is a norm, but it has a flat axial face. A quadratic mean-gap route needs FPP-specific curvature, and nonrandom-error control when replacing actual means by the norm; this norm is not asserted to be an FPP limit shape.",rows[5]["assumptions"],"S1.w373.006")
]
target="math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation"
relations=[{"from_key":e["key"],"to_existing_logical":target,"kind":"semantic_association",
            "rationale":"The stored P0110 target asks for 'well-defined fluctuation and wandering exponents satisfying chi=2xi-1'; this scoped audit concept identifies an inference or quantifier that must be justified on a sufficient proof route. It neither proves nor refutes P0110."} for e in entries]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w373","bundle_slug":"p0110-adversarial-obstructions-w373-001","entries":entries,"relations":relations}
bundle_text=json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
(root / "bundle_001.json").write_text(bundle_text,encoding="utf-8")
live_bundle="~/math-brain-inbox/w373/bundle_001.json"
(patches / "01_p0110_draft_bundle.diff").write_text("".join(difflib.unified_diff([],bundle_text.splitlines(keepends=True),fromfile="a/"+live_bundle,tofile="b/"+live_bundle)),encoding="utf-8")

hook={"id":"fpp-estimate-scope-w373-01","area":"math","event":"stage-start",
      "cue":"An FPP proof infers strong exponent matching from a variance power law, or infers variance equivalence solely from high-probability localization.",
      "fire_when":"A proof says Var T=n^(2chi+o(1)) therefore the exponential concentration exponent is chi, without a relative-tail argument; or says T=T_C with probability tending to one therefore their variances match.",
      "silent_when":"Separate uniform exponential-tail estimates and quantitative L2 localization errors are proved, or explicitly retained as open inputs.",
      "text":"A variance exponent need not equal an exponential-tail exponent. High-probability agreement need not transfer variance. Check uniform endpoints, rare tails, and the L2 error relative to the true standard deviation; keep unproved inputs visible.",
      "evidence":"INDEPENDENT.md; ATTEMPT.md obstructions A,D; verification.json. Recalled scars fpp_beta_measured_and_it_does_not_move_the_wall_2026_08_15 and proof_steps_need_derived_joint_structure_2026_09_09.","proposer":"w373"}
hook_text=json.dumps(hook,ensure_ascii=False)+"\n"
(root / "hook_proposal.jsonl").write_text(hook_text,encoding="utf-8")
live_hook="~/primary_directive/hooks1000/proposals/math-w373.jsonl"
(patches / "02_fpp_scope_hook.diff").write_text("".join(difflib.unified_diff([],hook_text.splitlines(keepends=True),fromfile="a/"+live_hook,tofile="b/"+live_hook)),encoding="utf-8")

progress={"agent":"w373","row":"S1.w373.007","event":"P0110: saved independent scoped obstructions and kept the paired cylinder reductions as partial; quantitative mean gap and global exponent matching remain unproved.","evidence":str(root / "PAIRED_AUDIT.md"),"publication_status":"staged only; worker-only write restriction"}
(root / "PROGRESS_EVENT.json").write_text(json.dumps(progress,indent=2),encoding="utf-8")
(root / "TEAM_HANDOFF.json").write_text(json.dumps({"from":"w373","to":["w372","w374"],"kind":"found","body":"Adversarial audit keeps the frozen unconditional cylinder transfer and conditional mean-gap reductions as partial. GEOMETRY_OBSTRUCTION.md supplies a symmetric norm countermodel; all original result checks remain pending w374. Review packet: ~/brain_workers/w373/REVIEW_PACKET.md.","sent":False,"why_not_sent":"Worker brief forbids mesh send commands and shared database writes; disk handoff for named peers."},indent=2),encoding="utf-8")

print(json.dumps({"claim_rows":len(rows),"draft_concepts":len(entries),"draft_relations":len(relations),"shared_outputs_written":False,"independent_review":"pending w374","staged_patches":["patches/01_p0110_draft_bundle.diff","patches/02_fpp_scope_hook.diff"]},indent=2))
