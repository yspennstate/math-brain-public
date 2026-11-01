"""Prepare local review artifacts. This script never ingests or changes a store."""
import difflib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOW = datetime.now(timezone.utc).isoformat()
SRC = {
    "source_id": "owner-own-work:w477:C0052:conditional-bridge-20261010",
    "url": "~/brain_workers/w477/ATTEMPT.md",
    "revision": "author-checked-unreviewed-2026-10-10",
    "license": "owner-own-work (campaign deductions; classical inputs attributed)",
    "excerpt": None,
}


def entry(key, logical, kind, title, statement, assumptions, proof=None):
    return {"key": key, "namespace": "probability.statmech", "logical_name": logical,
            "kind": kind, "title": title, "statement": statement,
            "proof_text": proof, "assumptions": assumptions, "domain": "probability theory",
            "source": dict(SRC)}


entries = [
    entry("source-target", "c0052-source-subcritical-coupling-target", "concept",
          "C0052 exact source target: subcritical renormalized coupling",
          "HISTORICAL CONJECTURE; current openness UNKNOWN. For the free zero-field nearest-neighbour Ising state on Z^3 at 0<beta<beta_c, let G_beta(x)=E[sigma_0 sigma_x], chi=sum_x G_beta(x), xi=[lim_n -(1/n) log G_beta(n e1)]^{-1}, and U4 be the four-spin expectation minus its three Wick pairings. With the source convention g(beta)=sum_{x,y,z}U4(0,x,y,z)/(chi^2 xi^3)<=0, prove that g(beta) does not tend to zero as beta increases to beta_c. This is PIMS 2017, arXiv:1707.00520v1, equations 7.1-7.2 and Conjecture 6, printed p94. Critical smeared-field cumulants use a different normalization; no equivalence is assumed here.",
          ["nearest-neighbour ferromagnetic Ising model on Z^3", "free zero-field subcritical state", "chi and exponential xi finite at each beta<beta_c", "historical statement only; not solved here"]),
    entry("current-input", "original-current-ursell-identity-scope", "concept",
          "Scope and direction of the original-current Ursell identity",
          "ATTRIBUTED INPUT: for a finite free zero-field ferromagnetic Ising model, U4(x,y,z,t)=-2 G(x,y)G(z,t) P^{xy,zt}(x connected to z in n+m), where n and m are independent single currents, source labels cancel modulo two, and connectivity to oneself is permitted. The infinite-volume version at beta<=beta_c uses the no-infinite-path/continuity input in Aizenman-Duminil-Copin arXiv:1912.07973v4 section 3.2. Its equation 3.13 compares this probability from ABOVE by the overlap probability of independently enlarged clusters after adding sourceless currents. A lower bound on that enlarged-cluster probability alone is insufficient for a lower bound on the original probability.",
          ["free zero-field ferromagnetic Ising model", "current weights proportional to product J_e^n_e/n_e!", "independent currents with specified parity source sets", "infinite-volume extension requires the primary source's additional input"]),
    entry("L001", "fourth-moment-deficit-excludes-gaussian-limit", "lemma",
          "Conditional fourth-moment deficit witness",
          "Let X_n converge in law to X, E X_n=0, E X_n^2=1, and let |X_n|^4 be uniformly integrable. If liminf_n(3-E X_n^4)>=epsilon>0, then E X=0, E X^2=1, E X^4<=3-epsilon, and X is non-Gaussian.",
          ["distributional convergence", "centered variance-one variables", "uniform integrability of fourth powers", "positive liminf deficit"],
          "Truncate the first, second and fourth powers continuously. Weak convergence handles bounded truncations, and uniform integrability controls tails for the sequence and its limit. Thus all three moments converge. A centered variance-one Gaussian has fourth moment three, contrary to the positive deficit."),
    entry("L002", "variance-weighted-annealed-current-cumulant-identity", "lemma",
          "Exact block cumulant under variance-weighted sources",
          "In a finite connected free zero-field ferromagnetic Ising model with positive edge couplings, choose nonzero nonnegative weights a, M=sum_x a_x sigma_x, V=E M^2, and ordered endpoints with rho(x,y)=a_x a_y G(x,y)/V. Independently draw two endpoint pairs (X,Y),(Z,T) from rho and single currents n,m sourced at the respective pairs, cancelling repeated labels modulo two. Then 3-E[(M/sqrt(V))^4]=2 P(X connected to Z in n+m), including repeated endpoints.",
          ["finite connected graph with positive ferromagnetic couplings", "free zero-field state", "finite nonnegative weights not all zero", "independent pair draws and currents", "original-current Ursell identity with parity cancellation"],
          "Expand the fourth cumulant as a finite weighted sum of U4. Each Wick pairing sums to V^2. Insert the original-current identity and divide by V^2; the coefficient becomes rho(x,y)rho(z,t). Keep every repeated-label term using parity source cancellation."),
    entry("L003", "single-current-source-cluster-overlap-second-moment-criterion", "lemma",
          "A sufficient second moment for single-current source overlap",
          "Under the endpoint law of the variance-weighted cumulant identity, let C and C' be the independent SINGLE-current source clusters, W a finite vertex set, I=|W intersect C intersect C'|, q(v)=P(v in C), q(v,w)=P(v,w in C), A=sum_{v in W}q(v)^2>0, and B=sum_{v,w in W}q(v,w)^2. Then 3-E[(M/sqrt(V))^4]>=2A^2/B. A uniform upper bound B/A^2<=K would therefore provide a uniform deficit of at least 2/K. The ratio bound is an unproved extra input for critical 3D Ising.",
          ["all hypotheses and sampling conventions of the variance-weighted identity", "independence between the two marked SINGLE currents", "finite W and A>0", "no independence of two occupancies within one current"],
          "Independence of the two clusters gives E I=A and E I^2=B. A common vertex connects the two source roots in the union current. Cauchy-Schwarz gives P(I>0)>=A^2/B; combine with the exact cumulant identity."),
    entry("L004", "independent-nonempty-sets-divergent-mean-overlap-rare-intersection", "lemma",
          "Divergent mean overlap with vanishing intersection probability",
          "For integer K>=2 and N=K^3 vertices, independently draw C,C' to be the whole set with probability 1/K and otherwise one uniform vertex. They are independent, identically distributed and nonempty. For I=|C intersect C'|, P(I>0)=2/K-1/K^2+(1-1/K)^2/K^3 ->0, E I=K+2(1-1/K)/K+(1-1/K)^2/K^3 ->infinity, and E I^2=K^4+2(1-1/K)/K+(1-1/K)^2/K^3. Hence E I^2/(E I)^2 is asymptotic to K^2. This refutes a general first-moment inference, not the Ising conjecture.",
          ["integer K>=2", "two independent random sets with the stated mixture law"],
          "Both sets full has probability 1/K^2 and gives I=N. Exactly one full has probability 2(1-1/K)/K and gives I=1. With both singleton, agreement has probability 1/N. The formulas follow by summing these disjoint cases."),
    entry("L005", "switching-gaussian-even-moment-bound-positive-ising-weights", "lemma",
          "Switching supplies Gaussian even-moment domination",
          "For a free zero-field ferromagnetic Ising model on a finite graph, or its free infinite-volume limit with finitely supported nonnegative weights, let M=sum_x a_x sigma_x with a_x>=0 and V=E M^2>0. For every integer k>=1, E M^{2k}<=(2k-1)!! V^k and E exp(t M/sqrt(V))<=exp(t^2/2). In particular E(M/sqrt(V))^6<=15 and E[(M/sqrt(V))^4 1_{|M/sqrt(V)|>R}]<=15/R^2. Signed weights are not included.",
          ["free zero-field ferromagnetic Ising model", "finite graph or free infinite-volume spin-correlation limit", "finitely supported nonnegative weights", "V>0", "switching lemma for even parity source sets"],
          "In currents with sources equal to the parity set of a list of 2k spin labels and empty, the first label is connected to at least one other label: a repeated label gives a certain event, otherwise parity forces another source in its component. Switching identifies each event times the 2k-spin correlation with G(first,j) times the remaining-spin correlation. The union bound and induction give the Wick upper bound. Summing with nonnegative weights gives (2k-1)!! V^k. Spin-flip symmetry removes odd powers from the exponential; finite-volume passage proves the stated infinite-volume version. The sixth-moment tail inequality is pointwise."),
    entry("L006", "positive-covariance-lattice-field-coarse-sobolev-tightness", "lemma",
          "Coarse H^-2 local tightness after a smooth variance normalization",
          "Let sigma be a stationary centered bounded spin field on Z^3 with nonnegative pair correlations and positive box-sum variances. Fix smooth f0 with 0<=f0<=1, f0=1 on [-1,1]^3 and support in [-2,2]^3. Let V0,L=Var(sum_x f0(x/L)sigma_x) and Phi_L=V0,L^{-1/2} sum_x sigma_x delta_{x/L} for integer L>=1. Then Phi_L is tight in H^{-2}_loc(R^3). If E[Phi_L(f0)^6]<=15 also holds, every subsequential limit Phi has E[Phi(f0)^2]=1 and is nonzero. No uniqueness, conformal invariance or sharp regularity is asserted.",
          ["stationary centered bounded lattice field in dimension three", "nonnegative pair correlations", "positive box-sum variance", "specified smooth f0 and its own variance normalization", "sixth-moment bound only for the nonzero-limit conclusion"],
          "Nonnegative correlations give V0,L>=Sigma_L, the variance of the radius-L box sum. Cover any fixed compact by a fixed number N of translated radius-L lattice boxes. Stationarity and Cauchy-Schwarz bound the sum-over-cover variance by N^2 Sigma_L; positive correlations then bound every bounded complex coefficient sum on that compact. Thus every Fourier coefficient of a smooth cutoff of Phi_L has a uniform second-moment bound. Summing with Sobolev weights of exponent 7/4 gives a bounded expected H^{-7/4} norm. Compact embedding into H^{-2}, Markov and a countable cutoff exhaustion give local tightness. Evaluation at f0 is continuous; the sixth-moment bound supplies uniform integrability, so variance one passes to each limit."),
    entry("L007", "c0052-subcritical-coupling-random-root-overlap-criterion", "lemma",
          "Source-faithful subcritical coupling from a random-root overlap",
          "In the free zero-field nearest-neighbour Ising state on Z^3 at 0<beta<beta_c, write chi=sum_x G_beta(0,x)<infinity, xi>0 for the exponential correlation length and g=sum_{x,y,z}U4(0,x,y,z)/(chi^2 xi^3). Independently sample X,R with probability G_beta(0,x)/chi and single currents n,m sourced at {0,X},{0,R}, cancelling repeated labels. Put p_y=P(0 connected to y in n+tau_y m). Then -g=(2/xi^3)sum_y p_y. Let H={0,...,ceil(xi)-1}^3, N=|H|, Y uniform on H independently, W any finite set containing 0, I=|W intersect C(n,0) intersect (Y+C(m,0))|, A=E I and B=E I^2. Then A>=1/N>0 and -g>=2N A^2/(xi^3 B)>=2/(B/A^2). A bounded B/A^2 along some beta_j increasing to beta_c is therefore sufficient for the source's non-triviality definition. No such bound is proved here.",
          ["free stationary zero-field nearest-neighbour subcritical Ising state on Z^3", "finite susceptibility and positive finite exponential correlation length", "primary infinite-volume switching/Ursell identity", "two independent susceptibility-weighted marked SINGLE currents", "independent uniform root Y on the specified cube", "finite W containing 0", "the ratio bound is a separate unresolved input"],
          "In the summed Ursell identity set z=y+r. Stationarity replaces G(y,y+r) with G(0,r). Dividing the x,r sum by chi^2 gives the two independent susceptibility endpoint draws, and nonnegative summands justify Tonelli. This proves the exact identity for -g. Restrict its root sum to H and average over Y. Single-current cluster overlap implies the original union-current connection. Cauchy-Schwarz bounds P(I>0) below by A^2/B. At Y=0 both clusters contain 0, so A>=1/N. Finally N=ceil(xi)^3>=xi^3. The ratio condition remains unproved."),
    entry("ratio-gap", "c0052-susceptibility-current-random-root-second-moment-gap", "concept",
          "C0052 remaining gap: susceptibility-current overlap ratio",
          "UNPROVED INPUT: in the sampling scheme of the source-faithful subcritical random-root criterion, find beta_j increasing to beta_c and K<infinity such that E I_beta_j^2/(E I_beta_j)^2<=K. Here the endpoints use G_beta(0,x)/chi(beta), the root shift is uniform on a cube of side ceil(xi(beta)), and the overlap uses SINGLE currents inside a finite correlation-length-scale box containing 0. Spin two-point estimates, divergent expected overlap and a lower bound for clusters enlarged with sourceless currents do not establish this bound. The critical variance-weighted block ratio is a different quantity.",
          ["same objects, weights and normalization as the subcritical random-root criterion", "clearly conjectural proof input"]),
    entry("bad-shortcut", "divergent-mean-overlap-uniform-hit-inference-invalid", "concept",
          "Rejected route: a divergent overlap mean alone",
          "INVALID GENERAL INFERENCE: two independent identically distributed nonempty random sets with divergent expected overlap must have intersection probability bounded away from zero. The rare-full-set mixture counterexample disproves this inference; a relative second-moment or other anti-concentration estimate is required before using it for an Ising non-Gaussianity argument.",
          ["this entry records a refuted probabilistic inference, not a conjectured Ising counterexample"]),
]

relations = [
    {"from_key":"L002","to_key":"current-input","kind":"depends_on","rationale":"The variance-weighted identity inserts the stated original-current Ursell identity with its original cluster event."},
    {"from_key":"L003","to_key":"L002","kind":"depends_on","rationale":"The overlap lower bound is converted to the exact block fourth-cumulant deficit in L002."},
    {"from_key":"L004","to_key":"bad-shortcut","kind":"refutes","rationale":"L004 has independent nonempty sets, E I tending to infinity, and P(I>0) tending to zero, which negates the asserted implication."},
    {"from_key":"L007","to_key":"current-input","kind":"depends_on","rationale":"L007 uses the original infinite-volume current event and stationarity; the enlarged-cluster upper bound is excluded."},
    {"from_key":"L007","to_key":"source-target","kind":"semantic_association","rationale":"L007 gives a conditional lower bound for exactly -sum U4/(chi^2 xi^3); it does not prove the unproved ratio condition or C0052."},
    {"from_key":"ratio-gap","to_key":"L007","kind":"depends_on","rationale":"The gap specifies the exact root, endpoint and normalization hypotheses whose missing ratio bound would activate L007."},
    {"from_key":"L006","to_key":"L005","kind":"semantic_association","rationale":"For the Ising application only, L005 supplies the sixth-moment assumption needed for L006's nonzero-limit conclusion; L006's tightness argument itself only uses stationary nonnegative covariance."},
    {"from_key":"source-target","to_existing_logical":"math:probability.statmech:open-problem-c0052-non-triviality-of-the-scaling-limit-of-the-three-dimensional-ising-mod","kind":"semantic_association","rationale":"The existing card says 'the renormalised coupling constant does not vanish'; this source-faithful concept spells out g(beta)=sum U4/(chi^2 xi^3) and the approach from beta<beta_c, preserving UNKNOWN current status."},
]

bundle = {"spec":"mathbrain-draft-v1", "author_agent":"w477",
          "bundle_slug":"c0052-source-coupling-conditional-bridge-20261010",
          "entries":entries, "relations":relations}
local_bundle = ROOT / "bundle_001.json"
local_bundle.write_text(json.dumps(bundle, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

claims_path = ROOT / "CLAIMS.jsonl"
existing = {json.loads(line)["id"] for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()}
with claims_path.open("a", encoding="utf-8") as output:
    for item in entries:
        if not item["key"].startswith("L"):
            continue
        claim_id = "w477-"+item["key"]
        if claim_id in existing:
            continue
        gap = "None for the stated conditional lemma/counterexample. The exact-source C0052 gap remains the unproved ratio bound in L007; this is not a C0052 solution."
        if item["key"] == "L007":
            gap = "Bound the specified susceptibility-current random-root B_beta/A_beta^2 along beta_j increasing to beta_c."
        row = {"id":claim_id,"target":"C0052","type":"counterexample" if item["key"]=="L004" else "lemma",
               "statement":item["statement"],"assumptions":item["assumptions"],"source":dict(SRC),
               "proof":item["proof_text"],"independent_reviewer":"w479 (requested; not yet checked)",
               "remaining_gap":gap,"status":"proved special case","review_status":"unreviewed","novelty_claim":False}
        output.write(json.dumps(row, ensure_ascii=False)+"\n")
        output.flush()

patches = ROOT / "patches"
patches.mkdir(exist_ok=True)
proposed = ROOT / "targeted_math_id_lookup.py"
live = "~/.claude/dreaming/targeted_math_id_lookup.py"
diff = "".join(difflib.unified_diff([], proposed.read_text(encoding="utf-8").splitlines(keepends=True), fromfile="a/"+live, tofile="b/"+live))
(patches/"01_exact_math_id_lookup.diff").write_text(diff, encoding="utf-8")

hook = {"id":"ising-id-w477-01","area":"math","event":"PostToolUse",
        "cue":"an exact C-number lookup returns a different problem logical_id",
        "fire_when":"C0052 recall fallback returns the C0051 attempt whose body merely mentions C0052",
        "silent_when":"the result's logical_id contains c0052 as a complete ID segment and all unverified labels are preserved",
        "text":"Check the logical ID before using a C-number card. A C0052 mention on a C0051 attempt is related evidence. After a recall timeout, use a bounded read-only ID lookup and retain the source's unverified labels.",
        "evidence":"w477/STORE_LOOKUP.json (exact C0052 hit, 0.1851389 s); baseline export lookup returned C0051, 9.150454 s; brain.py recall timed out at 60 s",
        "proposer":"w477"}
(ROOT/"HOOK_PROPOSAL.jsonl").write_text(json.dumps(hook)+"\n", encoding="utf-8")
hook_live="~/primary_directive/hooks1000/proposals/ising-id-w477.jsonl"
hook_diff="".join(difflib.unified_diff([], [json.dumps(hook)+"\n"], fromfile="a/"+hook_live,tofile="b/"+hook_live))
(patches/"02_ising_id_hook.diff").write_text(hook_diff,encoding="utf-8")

lifecycle = {"bundle":str(local_bundle),"prepared":{"value":True,"at":NOW},
             "submitted":{"value":False,"path":"~/math-brain-inbox/w477/bundle_001.json"},
             "reviewed":{"value":False,"referee":"w479","note":"No different-model receipt or scoped KEEP is yet recorded."},
             "ingested":{"value":False},"retrievable":{"value":False},
             "promotion":"HOLD: author-checked DRAFT; no integrator is run by this worker."}
(ROOT/"BUNDLE_LIFECYCLE.json").write_text(json.dumps(lifecycle,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"entries":len(entries),"relations":len(relations),"claims":len(existing)+sum("w477-"+e["key"] not in existing for e in entries if e["key"].startswith("L")),"local_bundle":str(local_bundle),"live_mutations":0}))
