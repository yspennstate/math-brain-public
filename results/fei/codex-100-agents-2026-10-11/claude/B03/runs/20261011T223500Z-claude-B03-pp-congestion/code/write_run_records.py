"""Write CLAIMS.json, PROGRESS.json and PACKET_DELTA.json for this run (statement hashes computed here)."""
import json, hashlib, os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
RUN = "20261011T223500Z-claude-B03-pp-congestion"


def sha(s):
    return hashlib.sha256(s.encode('utf8')).hexdigest()


C = []


def claim(cid, stmt, hyp, status, src, deps, fu, nxt, reviews):
    C.append(dict(claim_id=cid, version=1, exact_statement=stmt, hypotheses=hyp, statement_sha256=sha(stmt),
                  contributors=["claude-B03-lead"], proof_source=src, proof_dependencies=deps,
                  review_records=reviews, status=status, supersedes=[], refutes=[], first_unproved_line=fu,
                  next_consumers=nxt))


claim("B03-R-REFINED-WITNESS-BOUND",
      "For f a read-k union (or intersection) of gates h_l, each a Boolean function of at most M regular functions, "
      "H(f) <= [2+log2 e+K0+log2 M] I(f) + log2 k * sum_{A!=0} fhat(A)^2 |F(A)| "
      "+ (6/5) sum_{A!=0} fhat(A)^2 sum_{l in F(A)} s_l log2(kappa_l/s_l) + sum_j Inf_j(f) E_{nu_j}[G_j], "
      "with K0=120/11+3+2log2 3+log2(6e) and F(A), s_l=|A_l|, kappa_l=|A cap R_l|, G_j=G_j(tau(j)) the witness "
      "statistics of the proof of Theorem 5.1 (current-threshold-paper.tex l.862-878); nu_j(T)=(d_j f)^(T)^2/Inf_j at A=T u {j}.",
      ["hypotheses of Theorem 5.1 (union:theorem); regular inner functions"], "PROVED",
      "REPORT section 3.1: the proof of Theorem 5.1 stopped before union:forestcount, union:logsum and union:Gmean",
      ["C003 proof (union:runbound and its ingredients)"], None, ["A014", "A086", "A094"],
      [{"reviewer": "claude-B03-lead", "kind": "author derivation by inspection",
        "result": "consistent; independent review pending"}])
claim("B03-PPQ-INTERFERENCE-LEMMA",
      "Let q be a prime power, PP_q the union of AND(L) over the lines of PG(2,q) with uniform bits, j a point, "
      "E_L=1[L minus j all true], S=sum_{L ni j} E_L. Then d_j g = S + r with ||r||_2^2 <= 2q(q+1)^2 4^{-q}; "
      "S has coefficient +-2^{-q} on each nonempty T inside some L minus j and (q+1)2^{-q} at the empty set; "
      "for every family E of sets and eta>0, Inf_j nu_j(E) <= (1+eta)[sum_L ||P_E E_L||^2 + (q+1)q4^{-q}1[0 in E]] "
      "+ (1+1/eta)||r||^2; and for q>=5, Inf_j >= (q+1)2^{-q}(1-(q^2+q/2)2^{-q}).",
      ["q prime power; uniform product measure"], "PROVED", "REPORT section 3.2 (Lemma I and Lemma W)", [], None,
      ["A014", "A086", "A094"],
      [{"reviewer": "claude-B03-lead", "kind": "exact check of ||r||^2 <= bound and Inf_j at q=2,3,4",
        "result": "passed (pp_exact.py)"}])
claim("B03-PPQ-BOUNDED-FEI-RATIO",
      "For every prime power q>=10, H(PP_q) <= C(q) I(PP_q) with C(q)=24.5494 (=2+log2 e+K0) + 2W log2(q+1)/(q+1) "
      "+ (11/5)log2(q+1)(2W P_q+3eps) + 2W(6/5+(q+1)P_q) + 2(Delta+eps)Gmax, where W=1/(1-(q^2+q/2)2^{-q}), "
      "eps=2q(q+1)2^{-q}W, Delta=q2^{-q}W, Gmax=(6/5)log2(q+1)+q+1, P_q=P(Bin(q,1/2)<11(q+1)/120-1). "
      "C(q) -> 2+log2 e+K0+12/5 = 26.9494 as q -> infinity; hence sup over all prime powers q of H(PP_q)/I(PP_q) "
      "is finite, although every DNF of PP_q has read >= q+1.",
      ["q prime power >= 10"], "PROVED",
      "REPORT sections 1 and 3.3-3.4: DNF read lower bound; Theorem R + Lemmas I, W, O, G + variance bound",
      ["B03-R-REFINED-WITNESS-BOUND", "B03-PPQ-INTERFERENCE-LEMMA",
       "from C003: union:path, h2(v)<=2I, v*Lambda<=(log e)I"],
      None, ["A014", "A015", "A086", "A094", "obstruction suite"],
      [{"reviewer": "claude-B03-lead", "kind": "author proof",
        "result": "complete; independent review pending (A086/A094)"}])
claim("B03-PPQ-EXPLICIT-CONSTANT-TABLE",
      "Evaluating the closed form C(q) of B03-PPQ-BOUNDED-FEI-RATIO at 40 digits with exact binomial counts gives "
      "C(12)=32.437, C(13)=30.451, C(16)=28.043, C(20)=27.435, C(200)=27.025, max over 12<=q<=200 equal to C(12), "
      "C non-increasing on 20<=q<=200. With Theorem 5.1 for q<=11 this gives sup_q H(PP_q)/I(PP_q) < 66.1.",
      ["q in [12,200] evaluated; q>200 by termwise monotonicity and Chernoff P_q <= 2^{-0.558q}"], "EVIDENCE",
      "code/pp_refined_constant.py, out/pp_refined_constant.txt", ["B03-PPQ-BOUNDED-FEI-RATIO"],
      "Termwise monotonicity of C(q) for q>200 is asserted in REPORT 3.4, not machine-checked; values are "
      "floating evaluations, not interval certificates.",
      ["A086", "A094"], [])
claim("B03-PPQ-EXACT-SMALL-Q",
      "Exactly (integer Walsh-Hadamard transform): I(PP_2)=63/32, I(PP_3)=5005/2048, I(PP_4)=1472205/524288; "
      "Inf_j = 9/32, 385/2048, 70105/524288; ||r||^2 = 3/4, 937/2048, 62275/262144; H/I = 2.48278, 3.19816, 3.71013 "
      "(entropy as an exact finite sum evaluated at 60 digits). At q<=4, ||r||^2/Inf_j > 1 and the asymptotic regime "
      "of the interference lemma has not started.",
      ["q in {2,3,4}"], "CERTIFIED", "code/pp_exact.py, out/pp_exact.json", [], None, ["A014"],
      [{"reviewer": "claude-B03-lead", "kind": "internal asserts (Parseval, I two ways, incidences)",
        "result": "passed"}])
claim("B03-A012-LEDGER-REVIEW",
      "The A012 activation ledger holds: for F=1+A_r(g-1) on r fresh controls, p=2^-r, mu=Eg, a=1-mu, v=1-mu^2: "
      "I(F)=pI(g)+rpa and H(F)=L((1-pa)^2)+(p-p^2)a^2 log2(1/(p^2a^2))+p[H(g)-L(mu^2)]+2rpv, L(t)=t log2(1/t). "
      "Re-derived by the lead and checked on all 256 g on 3 bits, r=1,2,3 (1,536 assertions; worst entropy gap 8.0e-51).",
      ["g Boolean; controls fresh and uniform"], "PROVED",
      "lead re-derivation; code/check_A012_activation.py, out/check_A012_activation.txt",
      ["A012-HEREDITARY-ACTIVATION-ADMISSION (ledger part only)"], None, ["A012", "A011", "A086"],
      [{"reviewer": "claude-B03-lead", "kind": "independent re-derivation + exhaustive exact check",
        "result": "passed"}])
claim("B03-UNIVERSAL-LOW-CONGESTION-COVER",
      "If every Boolean f admits a union-of-gates cover (gates = Boolean functions of at most M regular functions, "
      "M absolute) whose label, subset and rank/rarity functionals in B03-R-REFINED-WITNESS-BOUND are each at most "
      "C I(f), then H(f) <= C' I(f) for all f (FEI).",
      ["existence of the cover"], "CONDITIONAL", "immediate from B03-R-REFINED-WITNESS-BOUND",
      ["B03-R-REFINED-WITNESS-BOUND"],
      "Every f has a gate cover with (L)+(S)+(R) <= C I(f). False for DNF covers of majority (label cost about "
      "log k ~ n per set against I ~ sqrt n); open for regular-gate covers; equivalent in strength to C020.",
      ["A015", "A013", "B03 stream"], [])

json.dump({"run_id": RUN, "stream": "B03", "claims": C}, open("CLAIMS.json", "w", encoding="utf8"), indent=1)
P = dict(protocol_revision="2026-10-11-execution-v2", run_id=RUN, stream="B03", packet_id="A014",
         gap_id="G-B03-CONGESTION-UNBOUNDED-READ", attempt_id=RUN + "-a1",
         method="refine the Thm 5.1 witness ledger; spectral interference lemma for pivotal pieces; exact WHT at q<=4",
         mathematical_delta="Theorem R isolates the three log k sources of C003; on PP_q (read q+1 in every DNF) the "
                            "pivotal pieces of d_j f have disjoint Fourier supports up to an exponentially small "
                            "remainder, so all three are O(I): H(PP_q) <= C(q) I with C(q) -> 26.95, against "
                            "41+7log2(q+1) from Theorem 5.1.",
         deliverable_status="partial: CLAIMS/PROGRESS/PACKET_DELTA/code/out saved; REPORT.md write refused by the "
                            "harness for subagents, full text returned to the coordinator in the structured output",
         mathematical_status="PROVED (author) for Theorem R, Lemma I and the bounded ratio on PP_q; explicit constant "
                             "table EVIDENCE; universal bridge CONDITIONAL; FEI OPEN",
         claim_versions_used=["C003 (current-threshold-paper.tex)", "A012-HEREDITARY-ACTIVATION-ADMISSION v1",
                              "A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT v1"],
         claims_created_or_changed=[c["claim_id"] + "@1" for c in C],
         source_artifacts=["code/pp_exact.py", "code/pp_refined_constant.py", "code/check_A012_activation.py",
                           "code/write_run_records.py", "out/pp_exact.json", "out/pp_exact_stdout.txt",
                           "out/pp_refined_constant.txt", "out/check_A012_activation.txt"],
         next_consumers=["A014", "A015", "A086", "A094"],
         next_action="State Lemma I for arbitrary unions with the cross term sum_{l!=l'}<P_E u_l,P_E u_l'> and prove "
                     "an absolute constant for read-k unions on linear hypergraphs (gate intersections of size <= 1).",
         stagnant_substantive_attempts=0,
         blockers=["REPORT.md and .final not written: the subagent harness refuses report files; the coordinator "
                   "saves the REPORT text from the structured output"])
json.dump(P, open("PROGRESS.json", "w", encoding="utf8"), indent=1)
Q = dict(P)
Q["packet_ids"] = ["A014"]
json.dump(Q, open("PACKET_DELTA.json", "w", encoding="utf8"), indent=1)
print("written", len(C), "claims")
for c in C:
    print(c["claim_id"], c["status"], c["statement_sha256"])
