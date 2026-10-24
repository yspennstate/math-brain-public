"""Build local DRAFT concepts and a narrowly scoped hook proposal; no ingestion."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
claims = {c["id"]:c for c in (json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines())}
definitions = [
    ("O1", "gaussian-optimizer-bias-draft", "DRAFT: Gaussian route selection changes the mean", claims["w517-P0297-O1"]["statement"]),
    ("O2", "gaussian-marginals-do-not-determine-crossing-exponents-draft", "DRAFT: Marginals do not determine crossing exponents", "Fix xi,kappa>0, epsilon_n=exp(-n) and m_n=ceil(exp(kappa*n)). On a graph of m_n parallel unit edges put D_n=min_i exp(xi*X_{n,i}) and let a_n be any median of D_n. If the fields within n are independent N(0,n), log(a_n)/log(epsilon_n) tends to xi*sqrt(2*kappa); if all fields are one common N(0,n), it tends to zero. Thus identical Gaussian edge marginals and D(X+c)=exp(xi*c)D(X) do not determine an optimized normalization exponent. No independence across n is needed. These growing graphs are not GFF or LQG models."),
    ("NT", "two-route-near-tie-error-bound-draft", "DRAFT: Conditional two-route near-tie error bound", "Let X be a finite centered Gaussian vector with covariance C positive semidefinite, V=max_i C_ii, xi>0, and exactly two lengths l_p=sum_i a_pi exp(xi X_i), with nonnegative nonzero coefficient vectors. Put f_p=log l_p, w_pi=a_pi exp(xi X_i)/l_p, Delta=f_1-f_2, R=(w_1-w_2)^T C(w_1-w_2), pi_p=exp(-beta f_p)/sum_{q=1}^2 exp(-beta f_q) and B_beta=pi_1*pi_2*R. Suppose nu(A)=E[R*1{Delta in A}] has density b on (-eta,eta), eta>0, and |b(t)-b(0)|<=L|t| there. For beta>0, |beta E B_beta-b(0)| <= 2 log(2)L/beta+(4 beta V+2 b(0))exp(-beta eta). No density assumption is needed outside this interval. For a cutoff family at scale T_n, divide this bound by T_n; a joint cutoff/temperature limit requires both resulting error terms to vanish and b_n(0)/T_n to have a determined limit. Those uniform hypotheses are not proved for LQG here."),
    ("3R", "competing-route-correction-to-gaussian-switching-draft", "DRAFT: A third route suppresses a pair's switching term", "Let Z,U,V0 be independent N(0,1), xi>0, M>=0, and let three parallel edges have log lengths f1=xi(Z+U), f2=xi(Z-U), f3=-M+xi V0. Their Gaussian field covariance is diag(2,2,1), positive definite. For full soft weights pi_p=exp(-beta f_p)/sum_{q=1}^3 exp(-beta f_q), the covariance distance of pair 1,2 is R12=4 and lim_{beta->infinity} beta E[pi_1*pi_2*R12]=[2/(xi sqrt(2*pi))]*Phi(-M/(xi sqrt(2))), where Phi is the standard normal distribution function. The isolated two-route contribution is 2/(xi sqrt(2*pi)). At M=0 the full pair contribution is half; for large M its ratio tends to zero. Pair gap regularity alone does not justify substitution into a full-model switching sum: the pair must beat every other route at its tie. This finite example does not refute w516's qualified reduction or an LQG dimension formula."),
]
entries = []
for key, logical, title, statement in definitions:
    claim = claims[f"w517-P0297-{key}"]
    entries.append({
        "key":key, "namespace":"probability.firstpassage", "logical_name":logical,
        "kind":"concept", "title":title,
        "statement":"Unreviewed campaign DRAFT; independent mathematical check pending. "+statement,
        "proof_text":None, "assumptions":claim["assumptions"], "domain":"probability theory",
        "source":{"source_id":f"owner-own-work:w517:P0297:{key}", "url":claim["source"]["path"],
                  "revision":"2026-10-10-author-draft-review-pending", "license":"owner-own-work", "excerpt":None},
        "review_status":"pending w518", "remaining_gap":claim["remaining_gap"],
    })
by_key = {e["key"]:e for e in entries}
relations = []
for fk,tk,rationale in [
    ("O2","O1","Both ends optimize Gaussian route lengths. O1 computes finite selection bias; O2 proves the same dependence issue can persist at normalization-exponent scale."),
    ("3R","NT","NT explicitly has exactly two routes. 3R gives an exact failure of using its isolated pair density as the corresponding contribution in a three-route denominator."),
    ("3R","O2","Both ends show that optimized costs depend on the joint competing-route structure, not merely one-edge marginals or a two-route marginal gap law."),
]:
    relations.append({"from_key":fk,"to_key":tk,"kind":"analogous_to","rationale":rationale,
        "supporting_ends":{"from_statement":by_key[fk]["statement"],"to_statement":by_key[tk]["statement"]}})
bundle = {"spec":"mathbrain-draft-v1","author_agent":"w517", "bundle_slug":"p0297-competitive-gaussian-paths-draft-001",
          "entries":entries,"relations":relations,"review_status":"pending w518; coordinator integration only"}
(ROOT/"bundle_001.json").write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
hook = {"id":"math-w517-01","area":"math","event":"PreToolUse",
        "cue":"A proof replaces a full-model pair switching contribution by an isolated two-route gap density without an all-competitor event.",
        "fire_when":"Three-route Gaussian control, M=0: a proof uses the isolated pair contribution b12(0) for the full pair 1,2 contribution.",
        "silent_when":"The denominator retains every route and the joint gap law explicitly includes competitiveness; or the proof states this as an open obligation.",
        "text":"At a near tie, retain every competing path in the soft-minimum denominator. In the three-route Gaussian control, an isolated pair gives twice the true contribution. Derive the competitor event before summing pair densities.",
        "evidence":"~/brain_workers/w517/NEAR_TIE_LEMMA.md, 3R: positive-definite covariance diag(2,2,1), M=0, full/isolated=1/2; author proof, referee pending; scar proof_steps_need_derived_joint_structure_2026_09_09",
        "proposer":"w517"}
assert len(hook["text"])<=300
(ROOT/"HOOK_PROPOSAL.jsonl").write_text(json.dumps(hook,ensure_ascii=False)+"\n",encoding="utf-8")
patch_dir=ROOT/"patches"
patch_dir.mkdir(exist_ok=True)
target="~/primary_directive/hooks1000/proposals/math-w517.jsonl"
patch=f"--- a/{target}\n+++ b/{target}\n@@ -0,0 +1 @@\n+"+json.dumps(hook,ensure_ascii=False)+"\n"
(patch_dir/"01_competing_path_hook.diff").write_text(patch,encoding="utf-8")
print(json.dumps({"entries":len(entries),"relations":len(relations),"hook_rows":1,"state":"local DRAFT prepared; not submitted or ingested"}))
