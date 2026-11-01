"""Targeted source recovery; writes only local reports."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
INTAKE = pathlib.Path("~/Downloads/Probability_1000_20h_20260906")


def exact_row(name, expected_line):
    p = INTAKE / name
    with p.open(encoding="utf-8-sig") as stream:
        for number, line in enumerate(stream, 1):
            if number == expected_line:
                record = json.loads(line)
                assert record["problem_id"] == "P0104"
                return {"path": str(p), "line": number, "record": record}
    raise RuntimeError("Named source row missing")


status = {
    "target_id": "P0104", "as_of": "2026-10-10",
    "exact_intake": exact_row("problems.jsonl", 175),
    "prior_attempt": exact_row("attempts.jsonl", 106),
    "primary_source": {
        "title": "50 years of first passage percolation",
        "authors": ["Antonio Auffinger", "Michael Damron", "Jack Hanson"],
        "url": "https://arxiv.org/pdf/1511.03262v2",
        "date": "2016-09-26 on title page; arXiv v2 submitted 2016-09-23",
        "verified_locator": "Section 3.1, Questions 13 and 15, PDF one-based page 37",
        "locator_correction": "Intake page 34/40 pointers do not locate both questions in checked v2",
        "short_source_quotes": ["under suitable conditions on F", "For suitable d, show that chi > 0."],
        "complete_scope_in_own_words": "On nearest-neighbour Z^d with iid nonnegative edge times, choose suitable edge-law conditions and an exponent definition; establish chi<1/2 for d>=2, the value chi=1/3 in the plane, and chi>0 in a suitable dimension.",
        "hypothesis_caveat": "The source deliberately leaves suitable conditions and the meaning of the scaling asymptotic open; it provides no universal complete hypothesis package.",
        "own_primary_check": "Direct public PDF find/open verified model, Questions 13/15, and section 3.1; peer locator was then checked independently.",
    },
    "working_model": {
        "law": "iid Uniform[1,2]", "graph": "undirected nearest-neighbour Z^2",
        "endpoints": "(0,0) and (n,0), integer n>=1",
        "target": "Var(T_n)=n^(2/3+o(1))",
        "exponent_definition": "chi=lim log Var(T_n)/(2 log n), if this limit exists",
        "selected_special_case": True, "curvature_assumed": False,
    },
    "recent_primary_literature": {
        "url": "https://arxiv.org/html/2604.01214v1",
        "title": "Rotationally invariant first passage percolation: Breaking the n/log n Variance Barrier",
        "date": "2026-04-01", "locator": "Theorem 1, sections 1.1 and 1.3",
        "checked_scope": "A polynomial variance saving for the stated bounded positive rotationally invariant Riemannian model; it is not a theorem about iid lattice Uniform[1,2] FPP.",
        "lattice_transfer_proved_by_this_paper": False,
    },
    "owner_prior_and_retired_check": {
        "ranking": "2026-09-07: attempted_un",
        "named_H_I_probe": "Targeted P0104 search found no matching proof in the named H/I attempt paths",
        "lean": "Annotated ranking line 600: attempted_un; no formal-check receipt identified",
        "store_claim_ids_checked": ["claim_f2576eacbf43455993d206cbe36d536a", "claim_925a5f66e641446fa12df62c9b4b5b34"],
        "store_meaning": "Verified abstract resampling framework is separate from the unverified scale-comparison wall",
        "recalled_math_memories": ["fpp_i3_neighbor_conditioned_sum_is_dep_plus_local_variance_2026_08_22", "l1prime_tightness_means_no_lossy_argument_can_work_2026_08_29"],
        "interpretation": "The targeted campaign evidence leaves chi=1/3 unmoved. This is not an exhaustive solved/retired search.",
    },
    "current_openness": "UNKNOWN", "parent_problem_solved": False,
    "novelty_claim": False, "formal_proof_receipt": None,
    "brain_publication": {"submitted": False, "reviewed": False, "ingested": False, "retrievable": False},
}
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(status, indent=2), encoding="utf-8")
print(json.dumps({"target_id": "P0104", "exact_source_row": 175, "prior_attempt_row": 106, "current_openness": "UNKNOWN"}))
