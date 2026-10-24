"""Bundle C007: superseding revisions of the math-brain nodes affected by the Codex holder's corrections
(ledger rows C00xx-A002 and the two status changes). The integrator treats a resubmitted logical_name with a
new statement digest as a superseding revision. Runs after the C006 chain frees the store."""
import json, os, subprocess, sys
import brain_cycle_C001 as cyc
import brain_bulk_C004 as bulk
from intake_tools import HERE, now, records

AGENT = cyc.AGENT; INBOX = cyc.INBOX; ROOT = cyc.ROOT; POP = cyc.POP


def make_payload():
    problems = {r["problem_id"]: r for r in records(HERE / "problems.jsonl")}
    sources = {r["source_id"]: r for r in records(HERE / "sources.jsonl")}
    latest = {}
    for a in records(HERE / "attempts.jsonl"):
        if a.get("substantive") and not a.get("superseded_by"):
            latest[a["problem_id"]] = a
    entries, relations = [], []
    # corrected attempt nodes (same logical names as bundle C004b) for problems with an A002
    for pid in ("C0002", "C0004", "C0033", "C0034", "C0035", "C0036", "C0040", "C0044", "C0045"):
        p = problems[pid]; a = latest[pid]; ns = bulk.ns_of(p["source_id"]); s = bulk.slug(p["title"])
        stitle = sources.get(p["source_id"], {}).get("title", p["source_id"])
        if pid in bulk.DEDICATED:
            continue  # these had no bulk attempt node; their dedicated nodes are revised below where needed
        alogical = "attempt-" + pid.lower() + "-" + s
        astmt = ("ATTEMPT RECORD (SUPERSEDING REVISION 2026-09-07 12:4x after the Codex holder's review), author-checked only. " + a["result"]
                 + ((" Key identity: " + a["key_identity"]) if a.get("key_identity") else "") + " Standing obstruction: see the earlier attempt; the correction above replaces the flawed step only.")
        entries.append(bulk.entry("at-" + pid.lower(), ns, alogical, "concept", "Attempt on " + p["title"] + " (corrected)", astmt, None,
                                  ["Refers to the open problem node open-problem-" + pid.lower() + "-" + s, "Supersedes the 2026-09-07 morning attempt record"]))
        relations.append(dict(from_key="at-" + pid.lower(), to_existing_logical="math:" + ns + ":open-problem-" + pid.lower() + "-" + s, kind="depends_on", rationale="The attempt is about this problem"))
    # C0036 and C0034 and C0035 dedicated nodes: revise statements
    entries.append(cyc.entry("hm", "probability.determinantal", "harmonic-mean-product-domination-equivariant-determinantal-finite-group", "lemma",
        "Harmonic-mean product-measure domination for equivariant determinantal processes on a finite group",
        "PRIVATE AUTHOR-CHECKED DRAFT (revision 2), no independent review. Let Gamma be a finite group and Q a Gamma-equivariant positive contraction on l^2(Gamma) with 0 < Q < I, and P_Q the determinantal measure with kernel Q. Let HM(Q) be the harmonic mean of the eigenvalues of Q. Then P_Q stochastically dominates the product Bernoulli measure of density HM(Q), and P_Q is dominated by the product measure of density 1 - HM(I - Q). Precise chain: the minimal conditional ODDS of presence is s_min = 1/(J^{-1})_ee = HM/(1 - HM) with J = Q(I-Q)^{-1}, and the minimal conditional PROBABILITY is s_min/(1 + s_min) = 1/(Q^{-1})_ee = HM(Q) (revision 2 states the odds and the probability separately, after a reviewer noted the two had been conflated in a side note). This is weaker than Lyons's Conjecture 5.7 (geometric mean / Fuglede-Kadison determinant), which numerical monotone-coupling linear programs on Z/nZ, n <= 6, satisfy exactly, with FK + 0.01 failing on a tested instance; those LP results are floating-point evidence, not certificates.",
        "Write J = Q(I - Q)^{-1}, so that P_Q(X = A) = det(I - Q) det(J_A). For a site e and configuration B on Gamma minus e, P_Q(e in X | X minus e = B) = s_B/(1 + s_B) with s_B = det J_{B union e}/det J_B = 1/((J_{B union e})^{-1})_{ee}. For positive definite M and S subset S' containing e, ((M_{S'})^{-1})_{ee} >= ((M_S)^{-1})_{ee}, so s_B is nonincreasing in B and its minimum is s_min = 1/(J^{-1})_{ee} = 1/((Q^{-1})_{ee} - 1). Equivariance makes Q a convolution operator diagonalised by the characters, so (Q^{-1})_{ee} = (1/|Gamma|) trace(Q^{-1}) = 1/HM(Q); hence s_min = HM/(1 - HM) and the minimal conditional probability is s_min/(1 + s_min) = HM(Q). Holley's inequality with a product measure as the smaller measure reduces to this one-site condition, so P_Q dominates Bernoulli(HM(Q))^Gamma; the complement process has kernel I - Q, giving the upper domination.",
        ["Finite group Gamma", "Q Gamma-equivariant with 0 < Q < I", "Holley's inequality in its product-measure form"]))
    entries.append(cyc.entry("lp", "probability.determinantal", "union-marginal-coupling-of-projection-determinantal-laws-lp-feasible-evidence", "concept",
        "Lyons's union-marginal coupling question: transportation polytope feasible in every tested instance (floating-point evidence), naive conditional splitting fails",
        "PRIVATE NUMERICAL EVIDENCE (revision 2), not a proof and not an exact certificate. Lyons (ICM 2014, Question 2.8) asks whether for H = H_1 (+) H_2 orthogonal in l^2(E) there is a coupling of P_{H_1} and P_{H_2} whose union has law P_H; the union must be disjoint by cardinality, so the question is the nonemptiness of a transportation polytope with three marginals. A floating-point LP (HiGHS, minimum total violation) reported violation 0.0 on 1360 random instances with |E| in {3,...,6}, on |E| = 7 and 8 generic instances, on Fourier-mode subspaces of cycles and on star-space splits of the K_4 edge space. Revision 2 records the reviewer's point that double-precision feasibility is evidence only; an exact rational LP on rational-kernel instances is the next step. The naive conditional splitting fails to reproduce the P_{H_2} marginal (direct computation on |E| = 4). Open: a general construction.",
        None, ["Finite E, orthogonal subspaces", "Floating-point evidence only"]))
    entries.append(cyc.entry("sub", "probability.determinantal", "determinantal-symbol-in-k-theta-splits-into-independent-sublattice-copies", "lemma",
        "A stationary determinantal process whose symbol is a function of k theta is an interleaving of independent copies on the k residue classes",
        "PRIVATE AUTHOR-CHECKED DRAFT (revision 2), no independent review. Let f(theta) = g(k theta) for an integer k >= 2 and a symbol g into [0,1]; then the restrictions of the stationary determinantal process P_f to the residue classes kZ + j are independent and each is P_g after reindexing. Consequence for Lyons's Question 5.4: if P_g is an (m/k + 1)-block factor of an i.i.d. process then P_f is an (m + 1)-block factor. Revision 2 corrects the scope: this settles the question only when the reduced symbol g is a proved case, i.e. degree 1 (so f(theta) = a + b cos(m theta) for any m), and NOT all even degrees; for f of degree 4 the reduction produces degree 2, itself open.",
        "The Fourier coefficients of g(k theta) vanish off multiples of k, so K(x,y) = f-hat(x - y) = 0 unless x = y mod k; a determinantal measure with block-diagonal kernel is the product of the block measures (all minors factorise and correlation functions determine the law); within a class the kernel is g-hat(x - y). The block-factor consequence: interleave k independent block-factor constructions with independent i.i.d. sequences on the classes; the value at x depends on the window {x, ..., x + m}.",
        ["f = g(k .) with g a symbol into [0,1]", "Block-diagonal kernels give product measures", "Settled cases: reduced degree 1 only"]))
    # status changes: C0007 resolved, C0042 refuted
    for pid, title in (("C0007", "Profile of near-extremal level sets of the 2D DGFF"), ("C0042", "Ballisticity under the ellipticity moment condition")):
        p = problems[pid]; ns = bulk.ns_of(p["source_id"]); s = bulk.slug(p["title"]); stitle = sources.get(p["source_id"], {}).get("title", p["source_id"])
        logical = "open-problem-" + pid.lower() + "-" + s
        stmt = ("STATUS CHANGE 2026-09-07 12:4x: NO LONGER OPEN. " + p["statement"] + " Resolution: " + str(p.get("resolved_by", "")) + " Source posing it: " + stitle + ", " + p["locator"] + ". This node supersedes the morning 'open problem' revision; do not treat as a target.")
        entries.append(bulk.entry("op-" + pid.lower(), ns, logical, "concept", "Resolved: " + p["title"], stmt, None, ["Posed in " + stitle, "Resolved or refuted in the literature per the Codex holder's fetched source; verify before citing"]))
    for e in entries:
        e["supersedes_existing"] = True  # the integrator supersedes only when told to; without the flag every entry reads as a conflict (bundle_015 skipped 17/17)
    return dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug="probability-intake-claude-corrections-after-codex-review-c007", entries=entries, relations=relations)


def main(inbox_num):
    sys.path.insert(0, str(ROOT / "src")); cyc.HERE = HERE
    payload = make_payload(); print("entries", len(payload["entries"]), "relations", len(payload["relations"]))
    saved = HERE / "brain_bundle_C007.json"; part = INBOX / f"bundle_{inbox_num:03d}.part"; final = INBOX / f"bundle_{inbox_num:03d}.json"
    if final.exists():
        raise RuntimeError("Inbox already exists")
    saved.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"); part.write_bytes(saved.read_bytes()); os.replace(part, final)
    targets = [POP / x for x in ("brain.sqlite3", "brain.sqlite3-wal", "brain.sqlite3-shm", "brain_signal_cache.pkl", "brain_signal_cache.pkl.tmp", "integration_ledger.jsonl", "objects")] + [final.with_suffix(".rejected-note")]
    cyc.guard(*targets)
    r = subprocess.run([sys.executable, "-B", str(ROOT / "tools/integrate_drafts.py"), "--only", AGENT], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=1200, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    (HERE / "brain_ingestion_C007.json").write_text(json.dumps(dict(recorded_at=now(), scope=AGENT, exit_code=r.returncode, stdout=r.stdout, stderr=r.stderr, public_promotion=False, proof_review="none"), indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(exit_code=r.returncode, stdout_tail=r.stdout[-500:], stderr_tail=r.stderr[-200:])))


if __name__ == "__main__":
    main(int(sys.argv[1]))
