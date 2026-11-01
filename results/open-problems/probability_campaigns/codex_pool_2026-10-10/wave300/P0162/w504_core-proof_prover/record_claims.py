"""Append completed proof rows without touching live stores or other workers."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
source = {"source_id":"owner-p0162-w504-20261010","url":"urn:owner-work:p0162:w504:20261010",
          "path":str(root/'PROOF.md'),"license":"owner-own-work"}
claims = [
    {"id":"w504-P0162-C001","statement":"For a Boolean function f on the uniform cube and coordinate i, writing u_T and v_T for the Fourier coefficients of its two Boolean restrictions, w_T=(u_T^2+v_T^2)/2, p_T=u_T^2/(u_T^2+v_T^2), and q_T=(u_T-v_T)^2/[2(u_T^2+v_T^2)], one has Inf_i(f)=sum_T w_T q_T and Delta_i(f)=sum_T w_T[1+h_2(q_T)-h_2(p_T)]. Zero-weight indices are omitted; Delta_i=H(f)-[H(f_i^+)+H(f_i^-)]/2 and all entropies are in bits.",
     "assumptions":["Uniform product measure","Boolean output +/-1","Real Walsh coefficients","Normalized restriction spectra by Parseval"],
     "source":source,"proof_or_counterexample":"PROOF.md section 1: two exact entropy chain rules and the Walsh restriction coefficients.","independent_reviewer":"w506 (requested; pending)","remaining_gap":"No gap in the worker argument; independent verification is pending. This equality does not prove a uniform influence bound.","status":"proved special case","scope":"Exact identity, not a FEI proof"},
    {"id":"w504-P0162-C002","statement":"If one finite K bounds Delta_i(f)/Inf_i(f) for at least one coordinate of every nonconstant Boolean f on every uniform cube, then H(f)<=K I(f) for every Boolean f. Constants are trivial and irrelevant variables can be removed.",
     "assumptions":["The universal EXISTS-coordinate input is assumed, not proved","Every restriction remains Boolean","Uniform measure and entropy in bits"],
     "source":{"url":"https://arxiv.org/html/2606.00246v1","locator":"Ansatz 1.1","path":str(root/'PROOF.md')},
     "proof_or_counterexample":"PROOF.md section 2: induction and exact influence splitting.","independent_reviewer":"w506 (requested; pending)","remaining_gap":"The assumed universal coordinate-selection inequality is unproved.","status":"proved special case","scope":"Conditional reduction only; known source result"},
    {"id":"w504-P0162-C003","statement":"For even m>=2 define g_m(b)=(-1)^(sum_{r=1}^{m/2} b_{2r-1}b_{2r}) and F_m(b,z)=g_m(b)-2*1_{b=0,z=1} on the uniform (m+1)-bit cube. With t=2^(-m), every base coordinate j in [m] has Inf_j(F_m)=1/2+t and Delta_j(F_m)<=2-(m/2)t<4 Inf_j(F_m).",
     "assumptions":["m is an even integer >=2","Uniform independent input bits","The exception is precisely one point b=0,z=1","Entropy in bits"],
     "source":source,"proof_or_counterexample":"PROOF.md section 3b: exact spectra of both restrictions and Jensen for u^2 log_2 u on [1/2,3/2].",
     "independent_reviewer":"w506 (requested; pending)","remaining_gap":"Independent check pending. No general good-coordinate theorem is proved; arbitrary restrictions are not asserted to preserve this family.","status":"proved special case","scope":"Main adaptive-coordinate special case; no novelty claim"},
    {"id":"w504-P0162-C004","statement":"The Boolean functions F_m defined in C003 satisfy I(F_m)=m/2+(m+1)2^(-m) and H(F_m)<=2 I(F_m) for every even m>=2.",
     "assumptions":["All assumptions and the definition in C003","Uniform measure","Entropy in bits"],
     "source":source,"proof_or_counterexample":"PROOF.md sections 3 and 3c: exact influence; split the spectral law by presence of z to get H<=m+h_2(2^-m), then h_2(t)<=mt+t/ln 2.",
     "independent_reviewer":"w506 (requested; pending)","remaining_gap":"Independent check pending; this is only an explicitly defined family, not the full FEI target.","status":"proved special case","scope":"Direct family FEI bound; no closure hypothesis"},
    {"id":"w504-P0162-C005","statement":"Proposed unproved sufficient lemma: there is one finite K such that every nonconstant Boolean function f on every uniform cube has at least one relevant coordinate i satisfying Delta_i(f)<=K Inf_i(f).",
     "assumptions":["Uniform measure","Boolean functions in all dimensions","One K independent of the function and dimension","EXISTS coordinate; not FOR EVERY coordinate"],
     "source":{"url":"https://arxiv.org/html/2606.00246v1","locator":"Equation (1), Ansatz 1.1","path":str(root/'PROOF.md')},
     "proof_or_counterexample":"Reduction proved in C002; family C003 gives a positive instance, while the independent w505 selector obstruction refutes the all-coordinate strengthening.",
     "independent_reviewer":"w506 (requested; pending)","remaining_gap":"No uniform proof of existence of a good coordinate for arbitrary Boolean f. Most-influential selection is already refuted in owner prior work.","status":"conjecture","scope":"Single hardest remaining input; no promotion to theorem"},
]
path = root/'CLAIMS.jsonl'
existing = {json.loads(line)['id'] for line in path.read_text(encoding='utf-8').splitlines() if line.strip()}
with path.open('a',encoding='utf-8') as out:
    for row in claims:
        if row['id'] not in existing:
            out.write(json.dumps(row,ensure_ascii=False)+'\n')
            out.flush()
            print(row['id'],row['status'])
