"""Package w505's results; only the expressly named draft inbox is shared."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w505")

def save(name, obj):
    (ROOT/name).write_text(json.dumps(obj, indent=2)+"\n", encoding="utf-8")

def own_source(key):
    return {"source_id": "owner-own-work:w505:P0162:"+key,
            "url": "file:///~/brain_workers/w505/ATTEMPT.md",
            "revision": "draft-2026-10-10-pending-independent-review",
            "license": "owner-own-work", "excerpt": None}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit-draft", action="store_true")
    args = parser.parse_args()
    measurements = json.loads((ROOT/"measurements.json").read_text(encoding="utf-8"))
    assert measurements["complete"]
    claims = [
      {"claim_id":"w505-C002", "statement":"For a Boolean uniform-cube function f(z,y)=g(z)+y h(z), its restriction deficit Delta_y(f)=H_2(f)-(H_2(f_+)+H_2(f_-))/2 equals sum_T r_T[h_2(w_T)+J(t_T)], where a_T=ghat(T), b_T=hhat(T), r_T=a_T^2+b_T^2, w_T=b_T^2/r_T, t_T=2a_T b_T/r_T, and J(t)=1-h_2((1+t)/2). Terms with r_T=0 are zero. In particular Delta_y>=sum_{T:b_T!=0} b_T^2 log_2(r_T/b_T^2)>=0.",
       "assumptions":["f takes values +/-1","normalized real Walsh transform under uniform cube measure","base-2 entropy, 0 log 0=0"], "source":"Independent derivation in ATTEMPT.md, exact local entropy identity.",
       "proof_or_counterexample":"Expand phi(a^2)+phi(b^2) using r and w, and phi((a+/-b)^2) using r and t. J>=0 and r h_2(w)>=b^2 log_2(r/b^2).", "remaining_gap":"Complete author derivation; independent referee check pending.", "status":"sketch"},
      {"claim_id":"w505-C003", "statement":"For every m>=1, let N=2^(2m), B(u,v)=(-1)^(u dot v) on F_2^m x F_2^m and F_m(u,v,y)=B(u,v)-(1-y)1{u=v=0}, y in {-1,+1}. F_m is Boolean and I_y(F_m)=1/N, while Delta_y(F_m)/I_y(F_m)>=log_2((2^m-1)^2+1). Hence no universal all-coordinate bound Delta_i(f)<=C I_i(f) exists.",
       "assumptions":["m is a positive integer","uniform product measure","base-2 Fourier spectral entropy"], "source":"ATTEMPT.md explicit obstruction; separate witness from earlier F4 refuted routes, no novelty claim.",
       "proof_or_counterexample":"Bhat(alpha,beta)=N^(-1/2)(-1)^(alpha dot beta), dhat=1/N. Thus a=Bhat-1/N, b=1/N, and r/b^2>=(2^m-1)^2+1. Apply C002 and sum N equal b^2 terms.", "remaining_gap":"Independent review of this exact family pending; this does not refute FEI or an existential coordinate lemma.", "status":"sketch"},
      {"claim_id":"w505-C004", "statement":"The explicit Boolean family F_m in C003 satisfies H_2(F_m)<=2 I(F_m) for every m>=1, despite its unbounded selector deficit/influence ratio.",
       "assumptions":["Exactly the family and normalization in C003"], "source":"ATTEMPT.md elementary chain-rule proof, owner-own-work.",
       "proof_or_counterexample":"I(F_m)=m+(2m+1)/N. Split the Fourier subset by selector inclusion, of mass rho=1/N; each conditional category has at most N atoms. H<=2m+h_2(rho)<=2m+rho(2m+log_2 e)<=2m+2(2m+1)rho=2I.", "remaining_gap":"Independent referee check pending; proved only for the named family.", "status":"sketch"},
      {"claim_id":"w505-C005", "statement":"For every uniform-cube Boolean f and coordinate i, with q=I_i(f), 0<=Delta_i(f)<=h_2(q)+4q(1-q). This upper bound retains a logarithmic loss in Delta_i/q as q decreases to zero.",
       "assumptions":["Normalized uniform Walsh transform","base-2 entropy"], "source":"ATTEMPT.md general upper bound; recalled F4 summary records a sharper high-influence estimate, so this is not claimed as new.",
       "proof_or_counterexample":"C002, concavity of h_2, J(t)<=t^2 from its positive even-power coefficients summing to one, and concavity of w(1-w). Sum r=1 and sum r w=q. Endpoints q=0,1 give Delta=0.", "remaining_gap":"Independent check pending; does not remove the small-influence logarithm.", "status":"sketch"},
      {"claim_id":"w505-C006", "statement":"A sufficient unproved input for full FEI is the existence of a universal C such that every nonconstant uniform-cube Boolean f has a positive-influence coordinate i with Delta_i(f)<=C I_i(f).",
       "assumptions":["Every dimension","all Boolean functions","the same C at every restriction"], "source":"Independent influence recursion in ATTEMPT.md; primary arXiv:2606.00246v1 Ansatz 1.1 describes the same induction principle for restriction-closed classes.",
       "proof_or_counterexample":"If supplied, induction uses I(f)=I_i(f)+(I(f_+)+I(f_-))/2 and H(f)=Delta_i(f)+(H(f_+)+H(f_-))/2; constants have H=I=0. The coordinate-selection premise itself has no proof in this packet.", "remaining_gap":"Prove suitable coordinate existence uniformly in the small-influence regime. Prior memory says maximal-influence selection and arbitrary-coordinate selection fail.", "status":"conjecture"},
      {"claim_id":"w505-C007", "statement":"The bounded finite check passed exact Walsh/influence identities for four F_m truth tables (m=1..4), independent direct character sums for m<=3, and the entropy identities/upper bound for all 276 Boolean functions of dimensions 1..3. Scalar selector ratios are 4.867668746754797 at m=1 and 20.328015411738306 at m=8.",
       "assumptions":["CPU gate max 20 seconds","largest enumerated truth table 512 points","entropy values use floating logarithms; spectra and influences use exact rational arithmetic"], "source":"measurements.json; python -X utf8 -B verify_obstruction.py --gate cpu20s-n9", "proof_or_counterexample":"The final run completed in "+str(measurements["seconds"])+" seconds; no GPU, training, formal proof assistant, or live-store write.", "remaining_gap":"Finite computation is corroboration, not proof for all dimensions or a referee keep.", "status":"numerical evidence"}
    ]
    path = ROOT/"CLAIMS.jsonl"
    known = {json.loads(line).get("claim_id") for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}
    with path.open("a", encoding="utf-8") as out:
        for row in claims:
            row.update(target="P0162", independent_reviewer="w506 (pending; no keep received)")
            if row["claim_id"] not in known:
                out.write(json.dumps(row, ensure_ascii=False)+"\n")
    primary = {"source_id":"arxiv:2606.00246", "url":"https://arxiv.org/html/2606.00246v1",
               "revision":"v1-2026-05-29", "license":"arxiv-nonexclusive", "excerpt":None}
    entries = [
      {"key":"fei-target", "logical_name":"fourier-entropy-influence-conjecture-uniform-boolean-cube", "kind":"concept", "title":"Fourier entropy-influence conjecture: exact uniform Boolean scope", "statement":"CONJECTURE: there exists a finite universal C such that for every n and every f:{-1,1}^n->{-1,1}, with fhat(S)=E[f(X) product_{j in S} X_j] under uniform independent signs, H_2(f)=sum_{S subset [n]} fhat(S)^2 log_2(1/fhat(S)^2) <= C I(f), where I(f)=sum_S |S| fhat(S)^2 and zero summands are zero. The dated intake P0162 ranking is historical; current global openness was not certified by w505.", "assumptions":["Uniform cube","Boolean +/-1 output","all dimensions; dimension-independent C"], "source":primary},
      {"key":"restriction-deficit", "logical_name":"boolean-fourier-entropy-restriction-deficit", "kind":"definition", "title":"Boolean Fourier entropy restriction deficit", "statement":"For f:{-1,1}^n->{-1,1}, normalized uniform Walsh coefficients and base-2 Fourier spectral entropy H_2(f), define f_+ and f_- by fixing coordinate i to +1 and -1, and Delta_i(f)=H_2(f)-(H_2(f_+)+H_2(f_-))/2. The coordinate influence is I_i(f)=sum_{S containing i} fhat(S)^2. The deficit ratio Delta_i/I_i is defined only when I_i>0.", "assumptions":["Uniform cube","Boolean +/-1 output","base-2 spectral entropy"], "source":own_source("definition")},
      {"key":"coordinate-obstruction", "logical_name":"bent-point-flip-obstruction-to-all-coordinate-fei-induction", "kind":"concept", "title":"Draft obstruction to all-coordinate FEI restriction induction", "statement":"DRAFT, pending independent referee check: for m>=1, N=2^(2m), u,v in F_2^m, y in {-1,+1}, let F_m(u,v,y)=(-1)^(u dot v)-(1-y)1{u=v=0}, with uniform inputs. This is Boolean. An independent calculation in w505/ATTEMPT.md gives I_y=1/N and Delta_y/I_y>=log_2((2^m-1)^2+1), which is unbounded, while the same family has H_2(F_m)<=2 I(F_m). It challenges an all-coordinate restriction-deficit bound; it does not challenge the FEI target or establish a new full theorem. Earlier owner F4 work already records related failed coordinate rules. Finite checks corroborate the calculation; they are not a referee keep.", "assumptions":["Exactly the displayed family","m>=1","uniform normalized Walsh transform","base-2 entropy","independent review pending"], "source":own_source("obstruction")},
      {"key":"missing-coordinate-input", "logical_name":"suitable-coordinate-input-for-fei-restriction-induction", "kind":"concept", "title":"Unproved suitable-coordinate input for full FEI", "statement":"UNPROVED INPUT: a universal finite C such that every nonconstant Boolean uniform-cube function has some positive-influence coordinate i satisfying Delta_i(f)<=C I_i(f), with the same C for all dimensions and all restrictions. Together with I(f)=I_i(f)+(I(f_+)+I(f_-))/2, it would prove FEI by induction from constants. The all-coordinate strengthening fails in the draft explicit witness; choosing a coordinate of maximal influence is not justified by this packet and prior owner work reports it fails. The missing work is a valid coordinate choice or a noncircular structural estimate in the small-influence regime.", "assumptions":["All Boolean functions and dimensions","uniform cube","same universal C at every inductive step"], "source":own_source("missing-input")}
    ]
    for entry in entries:
        entry.update(namespace="combinatorics.boolean_analysis", proof_text=None, domain="Boolean Fourier analysis")
    bundle = {"spec":"mathbrain-draft-v1", "author_agent":"w505", "bundle_slug":"p0162-restriction-quantifier-obstruction-w505-001", "entries":entries,
              "relations":[{"from_key":"coordinate-obstruction", "to_key":"restriction-deficit", "kind":"depends_on", "rationale":"The witness uses exactly the defined Delta_y and I_y, with base-2 uniform Fourier normalization."},
                           {"from_key":"missing-coordinate-input", "to_key":"restriction-deficit", "kind":"depends_on", "rationale":"The unproved local input quantifies over Delta_i/I_i as defined, not H/I."},
                           {"from_key":"missing-coordinate-input", "to_key":"fei-target", "kind":"semantic_association", "rationale":"The exact influence recursion makes the clearly unproved local coordinate premise sufficient for the stated full FEI target."}]}
    required = {"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
    assert len(entries)<=200 and all(required <= set(e) for e in entries)
    assert all(e["kind"] in {"concept","definition"} and e["proof_text"] is None for e in entries)
    keys = {e["key"] for e in entries}
    assert len(keys)==len(entries)
    assert all(r["from_key"] in keys and r["to_key"] in keys for r in bundle["relations"])
    # Only two depends_on edges, both ending at a definition with no outgoing dependency.
    assert all(r["to_key"]=="restriction-deficit" for r in bundle["relations"] if r["kind"]=="depends_on")
    text = json.dumps(bundle, ensure_ascii=False, indent=2)+"\n"
    (ROOT/"DRAFT_BUNDLE.json").write_text(text, encoding="utf-8")
    submission = {"prepared":True, "local_path":str(ROOT/"DRAFT_BUNDLE.json"), "submitted":False,
                  "reviewed":False, "ingested":False, "retrievable":False, "entries":len(entries),
                  "relations":len(bundle["relations"]), "local_schema_checks":"passed", "independent_review":"pending w506",
                  "note":"Do not run the live integrator from this worker; coordinator validates and integrates. No proof is promoted to theorem."}
    if args.submit_draft:
        INBOX.mkdir(parents=True, exist_ok=True)
        folder = INBOX.resolve()
        for number in range(1, 1000):
            target = folder/("bundle_%03d.json" % number)
            part = folder/("bundle_%03d.part" % number)
            if not target.exists() and not part.exists():
                break
        else:
            raise RuntimeError("No unused draft slot; existing artifacts left unchanged")
        assert target.resolve().is_relative_to(folder) and part.resolve().is_relative_to(folder)
        with part.open("x", encoding="utf-8") as f:
            f.write(text)
        os.rename(part, target)
        submission.update(submitted=True, inbox_path=str(target), submission_state="DRAFT awaiting independent review and coordinator validation")
    save("BUNDLE_STATE.json", submission)
    print(json.dumps({"claims":len(known)+sum(r["claim_id"] not in known for r in claims), **submission}))

if __name__=="__main__":
    main()
