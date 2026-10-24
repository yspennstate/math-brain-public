"""Prepare math-only draft nodes and exact quoted relation ends; no live store writes."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "ATTEMPT.md").read_text(encoding="utf-8")


def proof(section):
    return TEXT.split("## "+section, 1)[1].split("\n## ", 1)[0].strip()


def entry(key, logical, kind, title, statement, assumptions, section=None):
    return {"key":key, "namespace":"probability.functional_inequalities", "logical_name":logical,
            "kind":kind, "title":title, "statement":statement,
            "proof_text":proof(section) if section else None, "assumptions":assumptions,
            "domain":"probability / log-concave Poincare inequalities / P0017",
            "source":{"source_id":"owner-probability300-20261010:w357:P0017:"+key,
                      "url":"owner-work://brain_workers/w357/ATTEMPT.md",
                      "revision":"author-proof-2026-10-10; independent referee pending",
                      "license":"owner-own-work", "excerpt":None}}


OBS = "For a full-dimensional isotropic log-concave law mu on R^n, X~mu and an independent G~N(0,I), t>0 is noise variance, Y=X+sqrt(t)G, nu_t=Law(Y), mu_y=Law(X|Y=y), A_y=Cov(mu_y), and T_t f(y)=E[f(X)|Y=y]. Write D_mu(f)=integral |grad f|^2 dmu and Q_t(mu)=sup_f D_nu_t(T_t f)/D_mu(f) over smooth bounded nonconstant tests with positive finite energy and their Sobolev closure. The localization precision corresponding to t is 1/t."
ENTRIES = [
    entry("obs", "gaussian-observation-posterior-dirichlet-contraction", "definition",
          "Gaussian posterior Dirichlet contraction: conventions", OBS,
          ["X is full-dimensional, isotropic and log-concave", "G is independent standard Gaussian", "t>0 is noise variance"]),
    entry("posterior", "gaussian-posterior-covariance-and-gradient-identity", "lemma",
          "A Gaussian observation creates posterior curvature, not prior curvature",
          "Let mu(dx) be proportional to exp(-V(x))dx with smooth convex V and a finite second moment. Let G~N(0,I) be independent of X~mu and t>0. For Y=X+sqrt(t)G, the posterior mu_y has density proportional to exp(-V(x)-|x-y|^2/(2t)). For smooth bounded f, grad_y E[f(X)|Y=y]=Cov_mu_y(f,X)/t. The strong-log-concavity Poincare bound gives C_P(mu_y)<=t and 0<=Cov(mu_y)<=tI. These assertions also hold for nonsmooth convex potentials by log-concave approximation; they do not assert C_P(mu)<=t.",
          ["convex potential V", "independent standard Gaussian noise", "t>0", "smooth bounded test f, followed by finite-energy closure"], "L1."),
    entry("mmse", "isotropic-gaussian-observation-unweighted-mmse-matrix-bound", "lemma",
          "Unweighted posterior covariance is bounded by linear prediction error",
          "For any centered random vector X in R^n with Cov(X)=I and an independent G~N(0,I), put Y=X+sqrt(t)G for t>0 and A_Y=Cov(X|Y). Then E_Y A_Y <= t/(1+t) I in positive-semidefinite order. Log-concavity is not required. This is an unweighted matrix expectation; no bound on its product with an arbitrary Y-dependent weight follows.",
          ["E X=0", "Cov(X)=I", "G independent of X", "t>0"], "L2."),
    entry("affine", "isotropic-log-concave-gaussian-posterior-affine-dirichlet-contraction", "lemma",
          "Affine posterior means contract in Dirichlet energy",
          "Let X have a full-dimensional isotropic log-concave law mu, G~N(0,I) be independent, t>0, Y=X+sqrt(t)G, nu_t=Law(Y), and T_t f(y)=E[f(X)|Y=y]. For f(x)=a.x+b, integral |grad T_t f|^2 dnu_t <= |a|^2/(1+t). This proves strict contraction only on affine functions and does not bound the corresponding supremum over all nonlinear test functions.",
          ["mu isotropic and log-concave", "independent standard Gaussian G", "t>0", "f affine"], "L3."),
    entry("reduction", "strict-gaussian-posterior-dirichlet-contraction-kls-reduction", "lemma",
          "A strict posterior Dirichlet bound is equivalent to a uniform KLS bound",
          "Let mu be full-dimensional log-concave with finite K=C_P(mu). Define Y=X+sqrt(t)G, nu_t=Law(Y), and T_t f(y)=E[f(X)|Y=y] using independent G~N(0,I). If integral |grad T_t f|^2 dnu_t <= q integral |grad f|^2 dmu for all finite-energy tests, where t>0 and 0<=q<1, then K<=t(1+q)/(1-q). Conversely, K<=C implies this contraction with q=C/t whenever t>C. Thus fixed numerical t,q valid for all regular isotropic log-concave measures yield KLS by regular approximation; KLS itself yields such constants. The uniform strict nonlinear contraction is an assumption, not a proved conclusion in this draft.",
          ["mu log-concave and full-dimensional", "K=C_P(mu)<infinity", "G independent standard Gaussian", "t>0", "0<=q<1", "strict contraction for every finite-energy test in the forward implication"], "L4."),
    entry("gaussian", "gaussian-posterior-dirichlet-contraction-sharp-noise-constant", "lemma",
          "Gaussian posterior contraction has sharp factor (1+t)^(-2)",
          "For mu=N(0,I), independent G~N(0,I), t>0 and Y=X+sqrt(t)G, the posterior is N(y/(1+t),t/(1+t)I). Its mean operator T_t satisfies integral |grad T_t f|^2 dLaw(Y) <= (1+t)^(-2) integral |grad f|^2 dmu for finite-energy tests, with equality for nonconstant affine f. The supremum is exactly (1+t)^(-2), and total variance recovers C_P(mu)=1. This special case uses the Gaussian posterior's translation structure.",
          ["mu standard Gaussian", "independent standard Gaussian noise", "t>0", "finite-energy test f"], "L5."),
    entry("false-route", "unweighted-mmse-does-not-control-energy-weighted-covariance", "concept",
          "Refuted route: substituting MMSE into an energy-weighted expectation",
          "In a Gaussian observation Y=X+sqrt(t)G, write A_Y=Cov(X|Y) and h_Y=E[|grad f(X)|^2|Y]. The unweighted estimate E A_Y<=t/(1+t)I does not justify E[||A_Y||_op h_Y]<=t q E h_Y for some q<1. The quantities share the same observation and need not be independent. A fixed one-dimensional isotropic Laplace law and tail-supported gradients make the latter ratio approach 1. This refutes that sufficient route, not KLS or strict contraction of the actual posterior mean operator.",
          ["weights are conditional gradient energies", "no independence of A_Y and h_Y is supplied"]),
    entry("laplace", "isotropic-laplace-gaussian-posterior-energy-weighted-covariance-saturation", "lemma",
          "Fixed isotropic Laplace law saturates the weighted posterior covariance",
          "Fix t>0, let X have density p(x)=(sqrt(2)/2) exp(-sqrt(2)|x|), and let G~N(0,1) be independent. Put Y=X+sqrt(t)G and a(y)=Var(X|Y=y). Then 0<=a(y)<=t and a(y) tends to t as y tends to positive infinity. For any nonzero smooth phi supported in (0,1), let f_L(x)=integral_{-infinity}^x phi(u-L)du and h_L(Y)=E[phi(X-L)^2|Y]. As L tends to positive infinity, E[a(Y)h_L(Y)]/(t E h_L(Y)) tends to 1. Consequently no fixed q<1 controls this ratio for every test function even for this one fixed isotropic log-concave measure.",
          ["X is the specified variance-one centered Laplace law", "G independent standard Gaussian", "t>0 fixed", "phi nonzero smooth and supported in (0,1)", "L tends to positive infinity"], "L6."),
    entry("gap", "p0017-nonlinear-gaussian-posterior-contraction-remaining-gap", "concept",
          "P0017 remaining bridge: uniform strict contraction for nonlinear tests",
          "For X~mu isotropic log-concave and Y=X+sqrt(t)G with independent standard Gaussian G, this draft does not establish numerical t>0,q<1 for which integral |grad_y E[f(X)|Y=y]|^2 dLaw(Y) <= q integral |grad f|^2 dmu for every nonlinear finite-energy f, uniformly in n and mu. Such a bound would imply KLS by the conditional reduction. Affine and Gaussian special cases do not settle it; the energy-weighted MMSE shortcut is refuted. October 2026 preprints separately claim the full parent KLS theorem, but their complete proofs have not been independently audited here.",
          ["isotropic log-concave mu", "independent Gaussian observation", "uniformity in dimension, measure and nonlinear test"]),
]
RELATIONS = [
    {"from_key":"posterior", "to_key":"obs", "kind":"depends_on", "rationale":"Uses the observation kernel and noise-variance convention."},
    {"from_key":"affine", "to_key":"posterior", "kind":"depends_on", "rationale":"The gradient is A_Y a/t and A_Y^2<=t A_Y."},
    {"from_key":"affine", "to_key":"mmse", "kind":"depends_on", "rationale":"Uses the unweighted matrix bound E A_Y<=t/(1+t) I."},
    {"from_key":"reduction", "to_key":"posterior", "kind":"depends_on", "rationale":"Posterior Poincare bounds the conditional variance; the gradient identity proves the converse."},
    {"from_key":"reduction", "to_key":"obs", "kind":"depends_on", "rationale":"Uses the precise Dirichlet contraction operator defined here."},
    {"from_key":"gaussian", "to_key":"obs", "kind":"specializes", "rationale":"Computes the same observation operator for mu=N(0,I)."},
    {"from_key":"laplace", "to_key":"false-route", "kind":"refutes", "rationale":"The fixed-law weighted ratio tends to 1, violating every q<1."},
    {"from_key":"false-route", "to_key":"mmse", "kind":"cites", "rationale":"Identifies the exact unweighted estimate that cannot be multiplied by h_Y."},
    {"from_key":"gap", "to_key":"reduction", "kind":"depends_on", "rationale":"The missing nonlinear estimate is exactly the sufficient hypothesis of the reduction."},
    {"from_key":"posterior", "to_existing_logical":"math:harvest.arxiv.mathematics:arxiv-2405-06616-theorem-3-13-68d962", "kind":"cites", "rationale":"The retrieved Brascamp-Lieb card requires a uniformly positive Hessian Gamma and yields Cov<=Gamma^-1; here that hypothesis is supplied by the Gaussian likelihood with Gamma=I/t."},
]


def main():
    draft = {"spec":"mathbrain-draft-v1", "author_agent":"w357", "bundle_slug":"p0017-gaussian-posterior-bridge-w357-001", "entries":ENTRIES, "relations":RELATIONS}
    draft_dir = ROOT / "drafts"
    draft_dir.mkdir(exist_ok=True)
    (draft_dir / "bundle_001.json").write_text(json.dumps(draft, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    known = {e["key"]:e for e in ENTRIES}
    path = ROOT / "CLAIMS.jsonl"
    old = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    old = [r for r in old if not str(r["id"]).startswith("w357-MATH-") and not str(r["id"]).startswith("w357-EDGE-")]
    for e in ENTRIES:
        old.append({"id":"w357-MATH-"+e["key"], "target":"P0017", "type":e["kind"], "statement":e["statement"],
                    "assumptions":e["assumptions"], "source":e["source"], "proof_or_counterexample":e["proof_text"],
                    "independent_reviewer":"w359 (pending); w358 adversary statement sent first",
                    "remaining_gap":"Uniform strict contraction for all nonlinear tests remains unproved by this worker.",
                    "status":"proved special case" if e["kind"]=="lemma" else "conjecture" if e["key"]=="gap" else "sketch",
                    "review_state":"author-proof; independent review pending"})
    for k,r in enumerate(RELATIONS,1):
        target = known[r["to_key"]] if "to_key" in r else None
        captured = json.loads((ROOT / "BRAIN_CARDS.json").read_text(encoding="utf-8"))
        source_quote = next(row["body"] for row in captured["cards"] if "Theorem 3.13" in row["title"])
        old.append({"id":f"w357-EDGE-{k:02}", "target":"P0017", "type":"edge", "relation":r,
                    "from_statement":known[r["from_key"]]["statement"],
                    "to_statement":target["statement"] if target else source_quote,
                    "source":"ATTEMPT.md and BRAIN_CARDS.json", "proof_or_counterexample":r["rationale"],
                    "assumptions":[], "independent_reviewer":"w359 (pending)", "remaining_gap":"Independent edge endpoint and rationale review.", "status":"sketch"})
    path.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in old),encoding="utf-8")
    state = {"bundle":"drafts/bundle_001.json", "submitted":False, "reviewed":False, "ingested":False,
             "retrievable":"not tested; no ingestion asserted", "integrator":"validating coordinator only",
             "parent_problem_solved_by_worker":False}
    (ROOT / "BUNDLE_LIFECYCLE.json").write_text(json.dumps(state,indent=2)+"\n",encoding="utf-8")
    print("Prepared local draft and exact claim/edge rows; no ingestion performed.")


if __name__ == "__main__":
    main()
