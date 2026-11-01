"""Prepare reviewable research artifacts locally; never integrate a live store."""
import difflib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
proof_path = ROOT / "ATTEMPT.md"
text = proof_path.read_text(encoding="utf-8")
text = text.replace("fewer than l/4 of its edges", "at most l/4 of its edges")
proof_path.write_text(text, encoding="utf-8")

model = ["Undirected nearest-neighbour Z^2", "Independent Uniform[1,2] edge times", "T_n=T((0,0),(n,0)), integer n>=1"]


def section(start, end=None):
    tail = text.split(start, 1)[1]
    return tail.split(end, 1)[0].strip() if end else tail.strip()


def claim(number, statement, proof, assumptions=None, gap="The centered-noise KPZ crossover remains unproved.", status="proved special case", source=None):
    return {
        "claim_id": f"w360-{number}", "target": "P0104", "status": status,
        "exact_statement": statement, "assumptions": assumptions or model,
        "source": source or {"type": "owner-own-work", "path": str(proof_path), "location": number},
        "proof_or_counterexample": proof, "independent_reviewer": "w362",
        "review_status": "pending for this complete continuous packet",
        "remaining_gap": gap, "novelty_claim": False,
    }


rows = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
new = [
    claim("C2", "For fixed off-edge weights, T_n=c_e+min(U_e,a_e), where U_e=tau_e-1, A_e is the cheapest avoiding path, B_e the cheapest containing path with e's weight omitted, and a_e=clamp(A_e-B_e-1,0,1). If B_e is infinite set a_e=0. For a,b in [0,1], Cov(min(U,a),min(U,b))=(m^2/2)(M-M^2/2-m/3), m=min(a,b), M=max(a,b), U Uniform[0,1].", section("## Saved lemma C2:", "## Saved lemma C3:")),
    claim("C3", "For the finite edge set E_n of [-2n,2n]^2, resample each coordinate other than e independently with replacement probability 1-rho and share U_e. If J_n(rho)=sum_e E K(a_e(U_-e),a_e(U_-e^rho)), then Var(T_n)=integral_0^1 J_n(rho)d rho=integral_0^infinity exp(-t)J_n(exp(-t))dt. J_n(0)=L_n=sum_e Var(E[T_n|U_e]); J_n-L_n has nonnegative Hoeffding coefficients.", section("## Saved lemma C3:", "## Saved lemma C4:")),
    claim("C4", "For n>=9, n/8192<=J_n(1)<=2n/3. With a_e the clipped replacement threshold and eta=1/64, n/1024<=sum_e P(a_e>=eta)<=128n. The expected number of edges on the unique geodesic for which the best avoiding-path cost minus T_n is at least 1/128 is at least n/2048.", section("## Saved lemma C4:", "## Precise remaining input"), assumptions=model+["n>=9"], gap="Zero-noise robust margins are proved; their persistence at rate n^(-1/3) is not."),
    claim("C5", "If for every 0<epsilon<1/3 there are n-independent c,C>0, eta>0, p>1 and n0 such that L_n<=C n^(2/3+epsilon), R_n(1-s)<=C n(1+s n^(1/3-epsilon))^(-p) for all s in [0,1], and sum_e P(a_e>=eta,a_e^(1-s)>=eta)>=cn for 0<=s<=n^(-1/3-epsilon), then cK(eta,eta)n^(2/3-epsilon)<=Var(T_n)<=C(1+1/(p-1))n^(2/3+epsilon); hence the exponent is 2/3 if the inputs hold for every epsilon.", "Use C3. Integrate K>=K(eta,eta) on the lower window, and integrate the centered envelope with x=s n^(1/3-epsilon); integral_0^infinity(1+x)^(-p) dx=1/(p-1). Add L_n. The upper centered envelope and lower window are assumptions, not established results.", assumptions=model+["All displayed envelope and persistence hypotheses, uniform in n"], gap="Only the implication is proved; its centered envelope and lower-persistence inputs are still unproved."),
    claim("C6", "There is no c>0 such that K(a,b)>=c min(a,b) for every a,b in [0,1], where K is the continuous uniform threshold covariance and min(a,b) is shared-coordinate bare overlap probability.", "Set a=b tending to zero. K(a,a)/a=a^2/3-a^3/4 tends to zero. For a=1/64 the naive control K>=a/12 already fails. This does not refute a lower bound under thresholds bounded below.", assumptions=["U Uniform[0,1]", "a,b in [0,1]"], gap="A fixed positive-margin hypothesis repairs this specific lower-bound route, not the KPZ problem."),
    claim("C7", "For n>=9 and eta=1/64, Q_eta(s)=sum_e P(a_e(U_-e)>=eta,a_e(U_-e^(1-s))>=eta) is at least (1-s)^(N_n-1)n/1024, N_n=32n^2+8n. Hence Q_eta(s)>=n/2048 for s<=1/[2(N_n-1)].", section("## Attempt at the hard input:", "## Saved lemma C8:"), assumptions=model+["n>=9", "Independent resampling flags, independent of both original and fresh coordinates"], gap="The proved noise window is n^(-2), too short for the n^(-1/3) target; no exponent improvement follows."),
    claim("C8", "Let gamma,gamma' be endpoint geodesics in two independent environments and p_e=P(e in gamma). Then L_n=sum_e Var(E[T_n|U_e])<=sum_e p_e^2/4=E|gamma intersect gamma'|/4. For Uniform[1,2], DEP Corollary 1.3 applies and gives L_n<=C n^(2/3)(log n)^2 for n>=2, with C independent of n.", section("## Saved lemma C8:", "NEXT:"), gap="The first-order upper bound is supplied by the checked published theorem; centered covariance and positive-noise robust persistence remain open.", source={"type":"owner-own-work bridge plus attributed published theorem","path":str(proof_path),"primary_url":"https://arxiv.org/html/2307.01162v2","locator":"Equation (1.4), Corollary 1.3 equation (1.9), d=2 beta=2","hypotheses_checked":"a=1,b=2,absolute continuity,density>=1 a.e.; no curvature assumption"}),
    claim("G1", "Candidate sufficient noise lemma: for every 0<epsilon<1/3, constants c,C>0, eta in (0,1], p>1 and n0 independent of n exist such that R_n(1-s)<=C n(1+s n^(1/3-epsilon))^(-p) for all 0<=s<=1, and Q_eta(s)>=cn for all 0<=s<=n^(-1/3-epsilon), n>=n0. R_n=J_n-J_n(0), Q_eta counts coupled off-edge thresholds above eta. This is unproved.", "No proof. C4 establishes the marginal precursor at s=0; C7 extends it only to s of order n^(-2). C8 bounds the first-order floor, so the load-bearing unproved input is the centered crossover with a matching robust lower window.", status="conjecture", gap="Entire displayed noise lemma unproved; no parent solution is claimed."),
]
by_id = {row["claim_id"]: row for row in rows}
by_id.update({row["claim_id"]: row for row in new})
(ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in by_id.values()), encoding="utf-8")

status_path = ROOT / "SOURCE_STATUS.json"
source_status = json.loads(status_path.read_text(encoding="utf-8"))
source_status["first_order_bridge_primary_check"] = {
    "url": "https://arxiv.org/html/2307.01162v2", "version": "2023-10-13 v2",
    "title": "On the influence of edges in first-passage percolation on Z^d",
    "authors": ["Barbara Dembin", "Dor Elboim", "Ron Peled"],
    "hypotheses": "Equation (1.4): supported on [a,b], 0<a<b, absolutely continuous, density>=alpha>0 a.e.",
    "application": "Uniform[1,2] has a=1,b=2,alpha=1. Corollary 1.3 (1.9), d=2,beta=2,n>=2, gives sum p_e^2<=C n^(2/3)(log n)^2.",
    "derived_bound": "L_n<=C n^(2/3)(log n)^2 via the proved range bridge C8",
    "curvature_required": False, "independent_audit_of_published_proof": False,
}
status_path.write_text(json.dumps(source_status, indent=2), encoding="utf-8")
(ROOT / "STATEMENT_FOR_ADVERSARY.md").write_text("""# P0104 exact source and selected statement

Original target: ADH Questions 13 and 15, section 3.1, PDF page 37 in arXiv:1511.03262v2. Under suitable edge-law conditions, obtain chi<1/2 for d>=2, chi=1/3 in d=2, and chi>0 in a suitable dimension. The source leaves suitable conditions and the scaling interpretation unspecified; the attempt chooses an explicit variance definition. Intake record: Downloads/Probability_1000_20h_20260906/problems.jsonl:175. Current openness UNKNOWN; no novelty claim.

Selected target: independent Uniform[1,2] edge weights on undirected nearest-neighbour Z^2, endpoints (0,0),(n,0), integer n>=1. Prove Var(T_n)=n^(2/3+o(1)), with chi=lim log Var(T_n)/(2 log n) when it exists. No curvature, exponent existence, or independence of selected paths is assumed.

This replaces the initial statement-only checkpoint after source recovery; that checkpoint was already available to the adversary before the complete proof. The continuous replacement-threshold route and its robust-margin lemma are w360's boundary; w363's Bernoulli spectral route is separate. Full packet: REVIEW_PACKET.md and ATTEMPT.md.

NEXT: Audit the robust-margin lemma and published-theorem floor bridge; prove the centered-noise crossover.
""", encoding="utf-8")

source = {"source_id": "owner-own-work:w360:P0104:continuous-threshold-route", "url": "urn:owner-own-work:w360:p0104:continuous-threshold-route", "revision": "draft-2026-10-10", "license": "owner-own-work", "excerpt": None}


def entry(key, logical, title, statement, assumptions):
    return {"key": key, "namespace": "probability.fpp", "logical_name": logical, "kind": "concept", "title": title, "statement": statement, "proof_text": None, "assumptions": assumptions, "domain": "probability theory / first-passage percolation", "source": source.copy()}


entries = [
    entry("robust-margins", "uniform-fpp-linear-robust-replacement-margins", "Draft: linear robust replacement margins in uniform FPP", "Draft self-proved special case; independent review pending. On undirected nearest-neighbour Z^2 with iid Uniform[1,2] edge times and endpoints 0,n e1, integer n>=9, let gamma be the almost-sure unique geodesic and A_e the minimum passage time over paths avoiding e. The expected number of e in gamma with A_e-T(0,n e1)>=1/128 is at least n/2048. A fixed-path independence bound followed by a union over simple paths proves this marginal statement. It gives no persistence guarantee under positive coordinate resampling, and does not solve the KPZ exponent problem.", model+["n>=9", "Independent audit of campaign proof pending"]),
    entry("floor-bridge", "uniform-fpp-first-order-floor-independent-overlap-bound", "Draft: bound the uniform FPP covariance floor by independent overlap", "Draft bridge; independent review pending. For iid Uniform[1,2] undirected nearest-neighbour FPP on Z^2, endpoints 0,n e1, define T_n and L_n=sum_e Var(E[T_n|tau_e]). For endpoint geodesics gamma and gamma' in independent whole environments, L_n<=E|gamma intersect gamma'|/4=sum_e P(e in gamma)^2/4. The conditional mean in tau_e is monotone with range P(e in gamma), so the bounded-range variance inequality proves the bridge. Dembin-Elboim-Peled arXiv:2307.01162v2, equation (1.4) and Corollary 1.3 at d=2,beta=2, applies because Uniform[1,2] is absolutely continuous on a bounded positive interval with density at least 1. Thus L_n<=C n^(2/3)(log n)^2 for n>=2. This does not bound the centered covariance at positive noise.", model+["Published independent-overlap theorem invoked with full density/support hypotheses", "n>=2 for the logarithmic bound", "Independent audit of the campaign bridge pending"]),
    entry("open-crossover", "uniform-fpp-centered-threshold-noise-crossover-open-input", "Unproved: centered threshold crossover needed for uniform FPP KPZ", "Unproved sufficient input, not a theorem. For iid Uniform[1,2] undirected Z^2 FPP with endpoints 0,n e1, put U_e=tau_e-1 and a_e=clamp(A_e-B_e-1,0,1), where A_e is the cheapest avoiding path and B_e the cheapest containing path with e's weight omitted. Let U_-e^(1-s) independently refresh each other coordinate with probability s. For K(a,b)=Cov(min(U,a),min(U,b)), U Uniform[0,1], define J_n(rho)=sum_e E K(a_e(U_-e),a_e(U_-e^rho)) and R_n=J_n-J_n(0). The exact finite-product identity gives Var(T_n)=J_n(0)+integral_0^1 R_n(rho)d rho. A sufficient missing lemma would, for each 0<epsilon<1/3, give n-independent c,C>0, eta>0,p>1 with R_n(1-s)<=Cn(1+s n^(1/3-epsilon))^(-p) for all s in [0,1], and sum_e P(a_e>=eta,a_e^(1-s)>=eta)>=cn for s<=n^(-1/3-epsilon), for all large n. Together with the checked first-order floor bound these inputs imply Var(T_n)=n^(2/3+o(1)). Only zero-noise robust margins and a window of order n^(-2) have been proved in this packet.", model+["Displayed upper envelope and lower persistence are UNPROVED", "Constants uniform in n"]),
]
bundle = {
    "spec": "mathbrain-draft-v1", "author_agent": "w360", "bundle_slug": "p0104-continuous-margins-floor-001", "entries": entries,
    "relations": [
        {"from_key":"open-crossover", "to_key":"floor-bridge", "kind":"depends_on", "rationale":"The conditional exponent inference uses the floor bound L_n<=C n^(2/3)(log n)^2 from floor-bridge and the centered-envelope/lower-persistence inputs stated in open-crossover."},
        {"from_key":"open-crossover", "to_key":"robust-margins", "kind":"semantic_association", "rationale":"robust-margins gives an expected n/2048 geodesic edges with replacement slack >=1/128 at zero noise. open-crossover requires a cn robust-threshold overlap throughout a polynomial positive-noise window; the latter is explicitly not proved by the former."},
    ],
}
required = {"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
assert len(entries) == 3 and all(required <= set(e) and e["kind"]=="concept" and e["proof_text"] is None for e in entries)
assert len({e["key"] for e in entries}) == 3
for relation in bundle["relations"]:
    assert relation["kind"] in {"depends_on","semantic_association"}
    assert relation["from_key"] in {e["key"] for e in entries} and relation["to_key"] in {e["key"] for e in entries}
draft_dir = ROOT / "drafts"
draft_dir.mkdir(exist_ok=True)
payload = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
part = draft_dir / "bundle_001.part"
part.write_text(payload, encoding="utf-8")
part.replace(draft_dir / "bundle_001.json")
patch_dir = ROOT / "patches"
patch_dir.mkdir(exist_ok=True)
live_name = "~/math-brain-inbox/w360/bundle_001.json"
patch = "".join(difflib.unified_diff([], payload.splitlines(keepends=True), fromfile="a/"+live_name, tofile="b/"+live_name))
(patch_dir / "01_p0104_draft_bundle.diff").write_text(patch, encoding="utf-8")

measurement = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
check_count = sum(measurement[k] for k in ("exact_covariance_pairs","exact_refresh_couplings","positive_margin_controls","union_bound_constant_checks"))
receipt = {"draft_entries":3,"draft_relations":2,"local_draft_validated":True,"submitted":False,"reviewed":False,"ingested":False,"retrievable":False,"independent_reviewer":"w362","full_packet_sent":True,"exact_controls":check_count,"formal_check_receipt":None,"parent_solved":False,"next":"w362 audit C4/C8; then prove centered-noise upper envelope and robust lower persistence near rate n^(-1/3)."}
(ROOT / "REVIEW_RECEIPT.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
hooks_dir = ROOT / "hooks"
hooks_dir.mkdir(exist_ok=True)
hook = {"id":"threshold-margin-w360-01","area":"math","event":"stage-start","cue":"FPP variance lower bound inferred from bare coupled-geodesic overlap without a positive edge-replacement margin","fire_when":"A proof claims K(a,b)>=c min(a,b) uniformly for arbitrarily small thresholds.","silent_when":"Both replacement thresholds have an explicit fixed positive lower bound and the proof uses K(eta,eta).","text":"Bare geodesic overlap need not lower-bound threshold covariance: K(a,a)/a tends to zero. Check a fixed positive replacement margin and retain the first-order floor before integrating a noise-decay estimate.","evidence":"~/brain_workers/w360/CLAIMS.jsonl:w360-C6; MEASUREMENTS.json:49/64 deliberately invalid bare-overlap controls fail; corrected margin controls 36/36 pass","proposer":"w360"}
assert len(hook["text"]) <= 300
(hooks_dir / "math-w360.jsonl").write_text(json.dumps(hook)+"\n", encoding="utf-8")
hook_live = "~/primary_directive/hooks1000/proposals/math-w360.jsonl"
(patch_dir / "02_threshold_margin_hook.diff").write_text("".join(difflib.unified_diff([], [json.dumps(hook)+"\n"], fromfile="a/"+hook_live, tofile="b/"+hook_live)), encoding="utf-8")

report = f"""P0104 remains unresolved. I recovered its grouped primary questions and chose iid Uniform[1,2] undirected Z^2 FPP, with variance exponent as the explicit convention.

The substantive partial result is C4: for n>=9, the expected number of geodesic edges with replacement slack at least 1/128 is at least n/2048. C8 bounds the surviving first-order covariance by one quarter of independent-geodesic overlap. The full primary hypotheses of DEP Corollary 1.3 match this law, so that term is at most C n^(2/3)(log n)^2. These statements do not prove the centered-noise crossover.

Measured command: {measurement['command']}. {check_count} exact controls passed in {measurement['elapsed_seconds']} seconds under a governor state {measurement['gate_age_seconds']} seconds old. In a continuous two-edge control, the deliberately wrong normalization has error {measurement['invalid_normalization_control_error']}; the corrected identity has error {measurement['corrected_normalization_error']}. A deliberately invalid bare-overlap lower bound fails 49/64 cases; the positive-margin controls pass 36/36. These are controlled mathematical checks, not a deployed recall benchmark or an exponent experiment.

Brain handoff: drafts/bundle_001.json has three concept-only DRAFT entries and two supported relations. Submission, review, ingestion and retrieval are separate in REVIEW_RECEIPT.json. C4/C8 still need w362's independent audit. A weak no-replacement argument reaches only n^(-2) noise; the required n^(-1/3) centered-envelope and lower-persistence input is still unproved. No formal theorem receipt or novelty claim is made. Current openness UNKNOWN.

Apply: the authorized inbox submission mirrors the complete local DRAFT; patches/01_p0104_draft_bundle.diff is its reviewable unified representation. The coordinator validates and integrates after independent review; do not run live integration from this worker. The local hook proposal and its unified diff are ready for the rolling hook audit.

Operational receipt: mandatory brain.py recall finished in 15.418 seconds and emitted an automatic detached BM25 refresh. I did not invoke another recall or change a live recall control. Team-only delivery was unavailable; authorized direct mesh delivered the statement and referee packet. All research files are local except the explicitly authorized draft/proposal/progress handoffs.

NEXT: w362 audit C4/C8, then prove the centered-noise upper envelope and robust lower persistence near rate n^(-1/3).
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")
print(json.dumps({"claim_rows":len(by_id),"draft_entries":3,"draft_relations":2,"exact_checks":check_count,"local_validation":"PASS","parent_solved":False}))
