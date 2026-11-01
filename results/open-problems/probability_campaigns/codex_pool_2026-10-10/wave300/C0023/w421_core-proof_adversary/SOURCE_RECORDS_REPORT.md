Narrow C0023 intake records; historical assertions are not mathematical audit verdicts.

{
  "file": "~\\<private-repo>\\06_math_research\\probability_1000_intake_claude_20260907\\problems.jsonl",
  "line": 23,
  "record": {
    "admitted": true,
    "current_status": "no_resolution_found_in_documented_search",
    "dedup_key": "theta_pc_zero_intermediate_dimensions",
    "historical_status": "source_says_open",
    "intake": "claude_20260907",
    "locator": "Chapter XI Section 1, p. 136; also duminil_copin_icm_2018 Conjecture 1 p. 3 and duminil_copin_ising_potts_2017 Conjecture 1 p. 37",
    "problem_id": "C0023",
    "recorded_at": "2026-09-07T06:38:45Z",
    "result_status": "attempted_unsolved",
    "schema": "probability-problem.v1",
    "source_id": "garban_steif_noise_2012",
    "statement": "Prove theta(p_c) = 0 for Bernoulli percolation on Z^d for every d >= 3; open for 3 <= d <= 10 (known for d >= 11 by Fitzner and van der Hofstad, and for d = 2).",
    "status_search": "Bounded search 2026-09-07: no resolution for 3 <= d <= 10 found; the d >= 11 result (Fitzner-van der Hofstad 2017) and the half-space result of Barsky-Grimmett-Newman remain the state of the art.",
    "title": "No percolation at criticality on Z^d for 3 <= d <= 10",
    "verification": "unreviewed"
  }
}

{
  "file": "~\\<private-repo>\\06_math_research\\probability_1000_intake_claude_20260907\\attempts.jsonl",
  "line": 22,
  "record": {
    "attempt_id": "C0023-A001",
    "author": "claude-probability-1000-continue-0907",
    "independent_check": "",
    "key_identity": "",
    "method": "Try to bootstrap the half-space result of Barsky-Grimmett-Newman to the full space via a finite-energy and uniqueness argument.",
    "obstruction": "Infinite half-space susceptibility at p_c and a gluing lemma through the hyperplane are both unproved for 3 <= d <= 10.",
    "problem_id": "C0023",
    "recorded_at": "2026-09-07T06:38:45Z",
    "result": "In the half-space N x Z^{d-1} at p_c(Z^d) there is no infinite cluster (BGN). If the full space had an infinite cluster C at p_c, it would be unique (Burton-Keane), and by ergodicity and finite energy it would intersect every half-space; the half-space restriction of C is not the half-space percolation cluster (edges crossing the boundary are removed), and the half-space result only says the half-space's OWN clusters are finite, so C restricted to a half-space is a union of infinitely many finite half-space clusters connected through the other side. The natural next step is to show that infinitely many finite half-space clusters cannot connect through a hyperplane without creating an infinite half-space cluster on one side at a slightly larger p, i.e. to use the sharpness of the transition (Duminil-Copin-Tassion) in the half-space: at p_c the half-space cluster of the origin has infinite expected size? Not known: the half-space susceptibility at p_c(Z^d) could be finite, in which case the argument fails. I checked the d=2 analogue where everything is known: there the argument works because the half-plane susceptibility at 1/2 is infinite. So the reduction is: theta(p_c)=0 in Z^d follows if the half-space susceptibility at p_c(Z^d) is infinite together with a gluing lemma; the first statement is open.",
    "schema": "probability-attempt.v1",
    "substantive": true
  }
}

{
  "file": "~\\<private-repo>\\06_math_research\\probability_1000_intake_claude_20260907\\sources.jsonl",
  "line": 2,
  "record": {
    "access_evidence": "arXiv 1102.5761",
    "acquired_at": "2026-09-07T06:19:28Z",
    "acquisition_status": "validated_and_extracted",
    "bytes": 1522266,
    "extracted_characters": 243400,
    "extracted_sha256": "6a3b0000e40e220cb328514870902c84a913acec5d9e82a34ffb43d1714cf19c",
    "final_url": "https://arxiv.org/pdf/1102.5761",
    "http_status": 200,
    "intake": "claude_20260907",
    "kind": "pdf",
    "page_count": 151,
    "raw_relative_to_downloads": "sources/garban_steif_noise_2012/source.pdf",
    "reading_status": "unread",
    "schema": "probability-source.v1",
    "sha256": "fb1c1b1381c6cfe089b5038832f8c98e9800b09241835b69e931f7cfee822ea1",
    "source_id": "garban_steif_noise_2012",
    "statement_validation": "not_started",
    "text_relative_to_downloads": "sources/garban_steif_noise_2012/text.txt",
    "title": "Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems",
    "url": "https://arxiv.org/pdf/1102.5761"
  }
}

{
  "file": "~\\<private-repo>\\06_math_research\\probability_1000_intake_claude_20260907\\sources.jsonl",
  "line": 8,
  "record": {
    "access_evidence": "arXiv 1712.04651",
    "acquired_at": "2026-09-07T06:19:55Z",
    "acquisition_status": "validated_and_extracted",
    "bytes": 1131571,
    "extracted_characters": 73158,
    "extracted_sha256": "30ec55d98be90e7aacddfad608b27a8da5bb51844608cbc78c9062db74023f21",
    "final_url": "https://arxiv.org/pdf/1712.04651",
    "http_status": 200,
    "intake": "claude_20260907",
    "kind": "pdf",
    "page_count": 21,
    "raw_relative_to_downloads": "sources/duminil_copin_icm_2018/source.pdf",
    "reading_status": "unread",
    "schema": "probability-source.v1",
    "sha256": "d46fd63bd798736d1a463aade6e4c04f365da2e45d05d956a1812ec9c55950f2",
    "source_id": "duminil_copin_icm_2018",
    "statement_validation": "not_started",
    "text_relative_to_downloads": "sources/duminil_copin_icm_2018/text.txt",
    "title": "Duminil-Copin: Sixty years of percolation, ICM 2018",
    "url": "https://arxiv.org/pdf/1712.04651"
  }
}