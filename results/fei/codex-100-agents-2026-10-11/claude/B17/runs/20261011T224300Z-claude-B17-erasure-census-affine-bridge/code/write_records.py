# Writes CLAIMS.json, PROGRESS.json and PACKET_DELTA.json for this run, with statement hashes
# sha256(json.dumps({"statement":..., "hypotheses":...}, sort_keys=True, separators=(",",":"))).
import json, hashlib, os
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); RID = os.path.basename(RUN)

def h(st, hy):
    return hashlib.sha256(json.dumps({"statement": st, "hypotheses": hy}, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()

HB = ["f: {0,1}^n -> {-1,1}, uniform measure", "S random with P(S)=fhat(S)^2", "entropies in bits, 0 log 0 = 0",
      "I_i = sum over S containing i of fhat(S)^2", "B_i = H(S_i | S_-i)",
      "Delta_i H = H(f) - (H(f|x_i=0)+H(f|x_i=1))/2, JS_i = Delta_i H - B_i"]
PS = "StructuredOutput of run " + RID + " (report text; REPORT.md save refused by the harness), derivation sections "
claims = [
 dict(claim_id="B17-JS-PACKET-SCALAR", version=1, status="PROVED",
  exact_statement="For every z in [-1,1], ((1+z)ln(1+z)+(1-z)ln(1-z))/2 <= 1-sqrt(1-z^2). Consequently, for every Boolean f and coordinate i, 0 <= JS_i <= (2/ln2) sum over T not containing i of min(fhat(T)^2, fhat(T+i)^2) <= (2/ln2) min(I_i, 1-I_i).",
  hypotheses=HB,
  proof_source=PS + "(1)-(3): coefficientwise comparison of even power series; a_k=C(2k,k)/4^k satisfies a_{k+1}=a_k(2k+1)/(2k+2) and a_k>=1/(2k); packet identity s(1-sqrt(1-z^2)) = 2min(u^2,v^2).",
  proof_dependencies=["Shannon chain rule"], review_records=[], supersedes=[], refutes=[], first_unproved_line=None,
  next_consumers=["C005", "C018", "C019", "A026-AFFINE4-GOOD-COORDINATE", "A082-AFFINE4-ERASURE-BRIDGE", "A083 formalization"]),
 dict(claim_id="B17-KB-TWO-SIDED", version=1, status="PROVED",
  exact_statement="Let K_B(n) = max over nonconstant Boolean f with at most n relevant coordinates of min over relevant i of B_i/I_i, and C(n) = max H/I over the same set. Then K_B(n) <= C(n) <= K_B(n) + 2/ln2 for every n >= 1. With K_B = sup_n K_B(n) and C_FEI = sup_n C(n): C_FEI - 2/ln2 <= K_B <= C_FEI, so FEI holds iff K_B is finite.",
  hypotheses=HB,
  proof_source=PS + "(4)-(5): induction on relevant coordinates via Delta_i H = B_i + JS_i and I(f|0)+I(f|1) = 2(I-I_i); converse from sum_i B_i <= H.",
  proof_dependencies=["B17-JS-PACKET-SCALAR v1", "C005 identity Delta_i H = B_i + JS_i (re-proved in section (1))", "Shannon chain rule"],
  review_records=[], supersedes=[], refutes=[], first_unproved_line="K_B < infinity (equivalent to C000)",
  next_consumers=["C018", "C019", "G-R-SELECT", "B15", "A081 graph"]),
 dict(claim_id="B17-ZERO-ERASURE-TRANSPORT", version=1, status="PROVED",
  exact_statement="For Boolean f and coordinate i, B_i(f)=0 iff fhat(T)fhat(T+i)=0 for every T not containing i. Then both restrictions f|x_i=b have squared spectrum equal to the image of fhat^2 under S -> S minus {i}, so H(f|x_i=b)=H(f), JS_i=0 and I(f|x_i=b)=I(f)-I_i(f). For n >= 2, every maximizer of H/I over nonconstant Boolean functions with at most n relevant coordinates has B_i > 0 at every relevant coordinate.",
  hypotheses=HB, proof_source=PS + "(6).", proof_dependencies=["C005 identity (re-proved in section (1))"],
  review_records=[], supersedes=[], refutes=[], first_unproved_line=None,
  next_consumers=["A082-AFFINE4-ERASURE-BRIDGE (generalizes its free restriction step)", "B15", "B06"]),
 dict(claim_id="B17-KB4-CENSUS", version=1, status="CERTIFIED",
  exact_statement="Over all 65,534 nonconstant Boolean functions on 4 uniform bits: max_f min over relevant i of B_i/I_i = 4+(5/2)log2 5-(9/2)log2 3 < 107/40, attained exactly on 64 tables (the orbit of the 3-coordinate point function under permutation, translation and negation); max_f min over relevant i of Delta_i H/I_i = 12-(9/2)log2 3 on the same 64 tables; max_f H/I = 12-(49/16)log2 7 on the 32 four-bit point functions; max_f (sum_i B_i)/I = 4-(9/4)log2 3-(35/16)log2 5+(13/16)log2 13+(17/16)log2 17 on 192 tables.",
  hypotheses=HB + ["at most 4 relevant coordinates"],
  proof_source=RID + "/code/census_n4.py and out/census_n4.json: exhaustive; exact signs of integer log2-prime forms (rigorous double screen, rational atanh enclosures at 2^-320, big-integer fallback)",
  proof_dependencies=["linear independence over Q of log2 of distinct primes"],
  review_records=[{"reviewed_claim": "A082-FINITE-TRUE-ERASURE v1", "reviewer": "claude-B17-lead",
                   "verdict": "AGREES: same constant and extremizers; independent code and log method"}],
  supersedes=[], refutes=[], first_unproved_line=None, next_consumers=["A082", "A085 audit", "A081 graph"]),
 dict(claim_id="B17-KB5-CUTOFF", version=1, status="CERTIFIED",
  exact_statement="Let g:{0,1}^5->{-1,1}, g(x)=-1 iff sum_j x_j 2^j is in {5,12,13} (equivalently x1=0, x2=1, x4=0 and (x0 or x3)). All five coordinates are relevant; for i in {1,2,4}: I_i=3/16 and B_i/I_i = 16/3-(3/8)log2 3-(169/24)log2 13+(89/24)log2 89 (=2.6958875...); for i in {0,3}: I_i=1/16 and B_i/I_i = 16-(63/8)log2 3+15 log2 5-(169/8)log2 13+(85/8)log2 17 (=3.6048453...). Hence min_i B_i/I_i(g) > 107/40 > 4+(5/2)log2 5-(9/2)log2 3, and K_B(5) > K_B(4).",
  hypotheses=HB,
  proof_source=RID + "/code/search_n56.py certify(), out/search_n56.json; exact forms in out/family_scan.json; Walsh vector in the report, section (8)",
  proof_dependencies=["B17-KB4-CENSUS v1 (value of K_B(4))"], review_records=[], supersedes=[],
  refutes=["the statement K_B = K_B(4), i.e. any extension of the four-coordinate erasure constant to five relevant coordinates; the A082 claims are scoped and are not refuted"],
  first_unproved_line=None, next_consumers=["A082 exact K_B(5)", "G-R-SELECT", "B15", "A081 graph"]),
 dict(claim_id="B17-B09-INTERVAL", version=1, status="CERTIFIED",
  exact_statement="For g=(-1)^(XY), X~Bern(1/8), Y~Bern(1/4) independent, A={X}, masses (225,7,3,21)/256, M_A = H(masses)-h2(3/32), J_A = h2(3/32)-(1/8)h2(3/4): J_A-M_A = 7/4+(225/128)log2 3+(225/128)log2 5+(7/64)log2 7-(29/16)log2 29, which lies in [0.119545016024424957774322602741, 0.119545016024424957774322602742].",
  hypotheses=["definitions of M_A and J_A as recorded by B09 and A081"],
  proof_source=RID + "/code/b09_interval.py and out/b09_interval.json",
  proof_dependencies=["certlog rational atanh enclosures"],
  review_records=[{"reviewed_claim": "B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED", "reviewer": "claude-B17-lead",
                   "verdict": "NUMBER CONFIRMED inside the A081 interval; the B09 Maassen-Uffink dependency is still unpinned"}],
  supersedes=[], refutes=[], first_unproved_line=None, next_consumers=["B09", "A081", "A084"]),
 dict(claim_id="B17-SELECTION-GROWTH-EVIDENCE", version=1, status="EVIDENCE",
  exact_statement="Float evidence only: a frozen local search over 5-bit tables (18,452 restarts) found no table with min_i B_i/I_i above 2.6958875202; at n=6 (1,037 restarts) none above the same value; on AND_a and Tribes_{c,d} with n <= 16 (113 members) the largest min_i B_i/I_i is 2.697000 (a=3, c=6, d=2) while H/I reaches 3.83.",
  hypotheses=HB, proof_source=RID + "/code/search_n56.py and code/family_scan.py", proof_dependencies=[],
  review_records=[], supersedes=[], refutes=[], first_unproved_line="exact K_B(5); asymptotics of the composed family",
  next_consumers=["A082", "B15"]),
]
order = ["claim_id", "version", "exact_statement", "hypotheses", "statement_sha256", "contributors", "proof_source",
         "proof_dependencies", "review_records", "status", "supersedes", "refutes", "first_unproved_line", "next_consumers"]
for c in claims:
    c["statement_sha256"] = h(c["exact_statement"], c["hypotheses"])
    c["contributors"] = ["claude-B17-lead"] + (["A082"] if c["claim_id"] == "B17-KB4-CENSUS" else []) \
        + (["A081"] if c["claim_id"] == "B17-B09-INTERVAL" else [])
claims = [{k: c[k] for k in order} for c in claims]
with open(os.path.join(RUN, "CLAIMS.json"), "w", encoding="utf-8") as fh:
    json.dump(claims, fh, indent=1)
prog = {"protocol_revision": "2026-10-11-execution-v2", "run_id": RID, "stream": "B17", "packet_id": "B17-LEAD",
 "gap_id": "G-R-SELECT", "attempt_id": "B17-LEAD-01-erasure-census-cutoff",
 "method": "proof (JS scalar lemma, two-sided bridge, zero-erasure transport); exhaustive exact census on 4 bits; frozen float search on 5 and 6 bits with exact certification of the best tables; independent B09 enclosure",
 "mathematical_delta": "JS clause of C005 proved (phi(z) <= 1-sqrt(1-z^2)); FEI iff K_B finite, with slack 2/ln2, proved; K_B(4)=4+(5/2)log2 5-(9/2)log2 3 certified independently (A082 confirmed); explicit 5-variable g with min_i B_i/I_i = 2.6958875 > 107/40 certified, so K_B(5) > K_B(4); K_D(4), C(4) and max B/I on 4 bits certified; B09 J-M enclosed to width 1e-30.",
 "deliverable_status": "COMPLETE_LOCAL_SAVED_REVIEW_PENDING (REPORT.md refused by the harness; report text returned in StructuredOutput)",
 "mathematical_status": "BRIDGE_REDUCTION_PROVED_FINITE_CERTIFICATES_CHECKED_FULL_FEI_OPEN",
 "claim_versions_used": ["A082-FINITE-TRUE-ERASURE v1", "A082-AFFINE4-ERASURE-BRIDGE v1",
                         "A081-VERSIONED-DEPENDENCY-CERTIFICATE v1", "B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED", "C005", "C018"],
 "claims_created_or_changed": [c["claim_id"] + " v1" for c in claims],
 "source_artifacts": ["code/certlog.py", "code/census_n4.py", "code/search_n56.py", "code/family_scan.py",
                      "code/b09_interval.py", "code/write_records.py", "out/census_n4.json", "out/search_n56.json",
                      "out/family_scan.json", "out/b09_interval.json"],
 "next_consumers": ["A081", "A082", "A083", "A084", "A085", "B15", "B09"],
 "next_action": "Certify K_B(5) exactly: exhaustive census of the 2^31 output-normalized 5-bit tables (frozen spec, under 1 GB and 20 min) with a certified recheck of every table within 1e-9 of the maximum; reviewer A085.",
 "stagnant_substantive_attempts": 0,
 "blockers": ["REPORT.md write refused by the harness (subagent report-file rule); the full report is in the StructuredOutput"],
 "packet_ids": ["B17-LEAD"]}
with open(os.path.join(RUN, "PROGRESS.json"), "w", encoding="utf-8") as fh:
    json.dump(prog, fh, indent=1)
pd = dict(prog); pd["packet_ids"] = ["B17-LEAD", "A081", "A082", "A083", "A084", "A085"]
with open(os.path.join(RUN, "PACKET_DELTA.json"), "w", encoding="utf-8") as fh:
    json.dump(pd, fh, indent=1)
with open(os.path.join(RUN, "CLAIMS.json"), encoding="utf-8") as fh:
    for c in json.load(fh):
        assert c["statement_sha256"] == h(c["exact_statement"], c["hypotheses"])
        print(c["claim_id"], c["status"], c["statement_sha256"][:16])
print("records ok")
