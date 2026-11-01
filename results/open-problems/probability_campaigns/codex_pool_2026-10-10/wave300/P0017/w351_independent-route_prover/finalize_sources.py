"""Finish source metadata and stage one new-file hook patch; no live edits."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
path=ROOT/"CLAIMS.jsonl"
rows=[json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
row=rows[0]
row["statement"]="If every full-dimensional isotropic log-concave probability law nu on R^n satisfies Var_nu(g) <= C integral |grad g|^2 dnu for admissible locally Lipschitz g, then every full-dimensional log-concave law mu with covariance Sigma satisfies Var_mu(f) <= C integral grad f^T Sigma grad f dmu for locally Lipschitz f with finite variance and covariance-weighted energy. Conversely, take Sigma=I."
row["assumptions"]=["positive-definite finite covariance Sigma", "locally Lipschitz f with finite variance and covariance-weighted Dirichlet energy", "universal isotropic inequality assumed"]
row["source"]="Elementary affine change of variables in ATTEMPT.md L0; exact target matches arXiv:2610.05474v1 definition (5), Theorem 1.1. No universal target constant is proved here."
row["proof"]="Write X=m+Sigma^(1/2)Y and g(y)=f(m+Sigma^(1/2)y). Then Y is isotropic and log-concave, Var(g(Y))=Var(f(X)), and |grad_y g|^2=grad_x f^T Sigma grad_x f almost everywhere. Apply the assumed inequality. The converse follows by Sigma=I. The same locally Lipschitz class is preserved by the invertible affine map."
row["independent_reviewer"]="w353 (pending)"
rows[1]["assumptions"] += ["M_U bounds U conditional on V; M_V bounds V conditional on U"]
path.write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in rows),encoding="utf-8")
path=ROOT/"SOURCE_STATUS.json"
data=json.loads(path.read_text(encoding="utf-8"))
data["primary_sources"].insert(0,{"id":"arxiv:2603.29571v1","url":"https://arxiv.org/html/2603.29571v1","title":"Randomstrasse101: Open Problems of 2025","location":"Entry 13, Conjecture 30; covariance-scaled Cheeger formulation and Poincare discussion","verification":"Exact original target recovered. The printed halfspace expression has a dummy-variable inconsistency; this packet uses the unambiguous covariance formulation."})
data["cheeger_target"]="There exists a numerical c>0 independent of dimension and measure such that every full-dimensional log-concave probability law mu with covariance Sigma has h_mu>=c/sqrt(||Sigma||_op). Here h_mu is the infimum of mu^+(A)/min(mu(A),1-mu(A)) over measurable A of mass strictly between zero and one, using outer Euclidean Minkowski boundary content mu^+(A)=liminf_(epsilon down to 0) [mu(A+epsilon B_2)-mu(A)]/epsilon. For isotropic laws, Sigma=I."
data["local_record"]["exact_intake_record"]="Recovered from population/nodes.jsonl:7594 (problem) and :9049 (prior Gaussian attempt); no literal P0017 in the original Claude intake problems.jsonl."
data["owner_solved_retired_check"]="Targeted P0017 lookup in the required H/I attempts, Lean ranking, Team O board and population export found a prior Gaussian special case and no certified owner solved/retired receipt. This is not an exhaustive absence certificate; no novelty claim."
data["formal_check"]={"performed":False,"theorem":None,"trusted_axioms":None,"placeholder_proof_claimed":False}
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
text=(ROOT/"HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").rstrip("\n")
hook=json.loads(text)
assert len(hook["text"]) <= 300
patchdir=ROOT/"patches"
patchdir.mkdir(exist_ok=True)
live="~/primary_directive/hooks1000/proposals/math-w351.jsonl"
patch="--- a/"+live+"\n+++ b/"+live+"\n@@ -0,0 +1 @@\n+"+text+"\n"
(patchdir/"01_conditional_poincare_hook.diff").write_text(patch,encoding="utf-8")
print(json.dumps({"source_records_recovered":2,"claim_rows":len(rows),"hook_proposals_staged":1,"live_files_edited":0}))
