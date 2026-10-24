import json, hashlib, os
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RID = os.path.basename(RUN)
def sha(st, hy):
    return hashlib.sha256(json.dumps({"statement": st, "hypotheses": hy}, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
H0 = ["uniform measure on {-1,1}^n", "f Boolean (+-1 valued)", "B(f) = sum_i H(S_i|S_{-i}) under P_f(S)=fhat(S)^2, bits", "I(f) = total influence, ordinary flip convention"]
claims = []
def add(cid, st, hy, status, deps, src, first, cons):
    claims.append({"claim_id": cid, "version": 1, "exact_statement": st, "hypotheses": hy,
        "statement_sha256": sha(st, hy), "contributors": ["claude-B20"], "proof_source": "REPORT.md " + src,
        "proof_dependencies": deps, "review_records": [{"reviewer": "A090", "status": "pending"}, {"reviewer": "A094", "status": "pending (alternate)"}],
        "status": status, "supersedes": [], "refutes": [], "first_unproved_line": first, "next_consumers": cons})
add("B20-ERASURE-TENSOR-ADDITIVE", "For Boolean f, h on disjoint coordinate sets, B(f (x) h) = B(f) + B(h) and I(f (x) h) = I(f) + I(h).", H0, "PROVED", ["definitions"], "section 1", None, ["A096", "A099"])
add("B20-ACTIVATION-ERASURE-FORMULA", "For Boolean h on n coordinates and F(x,y) = h(x) if y = y* else 1 on n+k coordinates, with delta = 2^-k and c = 1 - hhat(empty): I(F) = delta (I(h) + k c) and B(F) is given exactly by formula (A) of REPORT.md section 2; in particular B(F) >= delta [B(h) - sum_i phi(hhat(empty)^2, hhat({i})^2)].", H0 + ["k >= 1"], "PROVED", ["definitions", "Parseval"], "section 2", None, ["A097", "A099"])
add("B20-ROOT-BIAS-ERASURE-PAID", "For every Boolean h, sum_i phi(hhat(empty)^2, hhat({i})^2) <= (2/(sqrt(e) ln 2)) I(h), where phi(a,b) = (a+b) h2(b/(a+b)) in bits.", H0, "PROVED", ["Parseval", "|hhat({i})| <= Inf_i"], "section 3", None, ["A096", "A099"])
add("B20-ERASURE-LOW-INFLUENCE-COMPLETE", "Let s(N) = o(N) and K_E(s) = sup {B(F)/I(F): F Boolean on N coordinates, 0 < I(F) <= 2^(-s(N))}. Then for every Boolean f with I(f) > 0, B(f) <= (K_E(s) + 2/(sqrt(e) ln 2)) I(f); hence K_E <= K_E(s) + 1.7501 and, by C018, C_FEI <= K_E(s) + 4.636.", H0 + ["s: N -> [0,inf), s(N) = o(N)"], "PROVED", ["B20-ERASURE-TENSOR-ADDITIVE", "B20-ACTIVATION-ERASURE-FORMULA", "B20-ROOT-BIAS-ERASURE-PAID", "C018 inequality (5) for the C_FEI corollary"], "section 4", None, ["A096", "A097", "A099", "A100"])
add("C000-B20-VIEW", "There is an absolute C with H(f) <= C I(f) for every Boolean f on the uniform cube; equivalently (C018) sup B/I < inf; equivalently (this run) sup B/I over functions with I(F) <= 2^(-s(N)) is finite for some s = o(N).", H0, "OPEN", ["C018", "B20-ERASURE-LOW-INFLUENCE-COMPLETE"], "sections 4 and Universal bridge", "a bound of the pairs (S, S+i) with |S| >= 1 in B by C I(f) for arbitrary Boolean f", ["all streams"])
json.dump(claims, open(os.path.join(RUN, "CLAIMS.json"), "w", encoding="utf-8"), indent=1)
prog = {"protocol_revision": "2026-10-11-execution-v2", "run_id": RID, "stream": "B20", "packet_id": "A097",
 "gap_id": "G-BOOLEANITY", "attempt_id": "B20-ERASURE-ACTIVATION-TRANSFER-1",
 "method": "Exact activation and tensor computation of the erasure functional B, with an influence-paid bound for the root bias-erasure pairs, then the Shalev-style limit m -> infinity",
 "mathematical_delta": "K_E <= K_E(low influence) + 2/(sqrt(e) ln 2): the erasure constant of C018 is as hard on functions with I <= 2^(-o(N)) as in general; root pairs (empty,{i}) of B are paid by 1.7501 I; the remaining C000 debt sits in the pairs (S,S+i) with |S| >= 1",
 "deliverable_status": "COMPLETE_LOCAL", "mathematical_status": "LEMMA_AUTHOR_PROVED; C000_OPEN; INDEPENDENT_REVIEW_PENDING",
 "claim_versions_used": [{"claim_id": "C018", "version": "supplement 2026-10-11", "usage": "K_E <= C_FEI <= K_E + 2/ln 2 and L <= B <= L + I/ln 2"},
   {"claim_id": "A096-UNIFORM-SINGLETON-HALF-TAX", "version": 1, "usage": "reviewed by B20, sign typo in REPORT text"},
   {"claim_id": "A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER", "version": 1, "usage": "read; telescope is the consumer of the root-pair bound"}],
 "claims_created_or_changed": [c["claim_id"] + "@1" for c in claims],
 "source_artifacts": ["REPORT.md", "CLAIMS.json", "code/check_activation.py", "out/ACTIVATION_RESULTS.json", "out/RECEIPTS.json"],
 "next_consumers": ["A096", "A097", "A099", "A100", "A090", "A094"],
 "next_action": "Bound the level-one-to-two pairs sum_{|S|=1} sum_{i not in S} phi(fhat(S)^2, fhat(S+i)^2) by C I(f) using level-two Booleanity, or exhibit a family where that ratio diverges",
 "stagnant_substantive_attempts": 0, "blockers": [], "packet_ids": ["A097"]}
json.dump(prog, open(os.path.join(RUN, "PROGRESS.json"), "w", encoding="utf-8"), indent=1)
json.dump(prog, open(os.path.join(RUN, "PACKET_DELTA.json"), "w", encoding="utf-8"), indent=1)
rec = {}
for root, _, files in os.walk(RUN):
    for fn in files:
        fp = os.path.join(root, fn); rel = os.path.relpath(fp, RUN).replace(os.sep, "/")
        if rel == "out/RECEIPTS.json": continue
        b = open(fp, "rb").read(); rec[rel] = {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}
json.dump(rec, open(os.path.join(RUN, "out", "RECEIPTS.json"), "w", encoding="utf-8"), indent=1)
open(os.path.join(RUN, ".final"), "w").close()
print(RID, len(claims), "claims", len(rec), "files")