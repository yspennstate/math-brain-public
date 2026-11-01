"""2026-09-10: second attempt on F0019 (Zygouras, Question 2: f'(beta) < 0 in the whole strong disorder regime).
Appends attempt row F0019-A002 to attempts.jsonl; problems.jsonl untouched (status stays attempted_unsolved).
Written by claude-prob1000-0910. Run once."""
import json
from pathlib import Path
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent.parent
row = {
    "schema": "probability-attempt.v1",
    "attempt_id": "F0019-A002",
    "problem_id": "F0019",
    "author": "claude-prob1000-0910",
    "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "substantive": True,
    "method": ("Re-read the source around Question 2 (PDF pp. 12-13) and separate the two overlap functionals that "
               "F0019-A001 conflated. Gaussian disorder. p_n(beta) = n^{-1} E log Z_n is convex with p_n'(beta) = "
               "beta (1 - R_n(beta)), R_n = n^{-1} sum_{i<=n} E mu_n^{(x)2}(S_i = S'_i) the two-replica overlap under the "
               "LENGTH-n polymer measure (Gaussian integration by parts). By convexity, at every differentiability point "
               "of p (all but countably many beta) lim_n R_n(beta) =: R(beta) exists and f'(beta) = -beta R(beta); so "
               "Question 2 at differentiability points is exactly: is R(beta) > 0 throughout strong disorder? The "
               "source's (3.11), -c_1 log W_n <= sum_{i<=n} I_i <= -c_2 log W_n under strong disorder, concerns the "
               "ONE-STEP overlap I_i = mu_{i-1}^{(x)2}(S_i = S'_i), a different functional; it gives, under very strong "
               "disorder, liminf n^{-1} sum I_i >= c_1 |f(beta)| > 0 a.s., but says nothing directly about R_n."),
    "key_identity": ("f'(beta) = -beta lim_n R_n(beta) at differentiability points; f(beta) = -int_0^beta s R(s) ds "
                     "(f is Lipschitz, |f'| <= beta)."),
    "result": ("(i) Question 2 is equivalent, at differentiability points, to positivity of the Cesaro two-replica "
               "overlap R(beta) under mu_n, and it is NOT implied by very strong disorder by any argument in the source: "
               "Bates and Bates-Chatterjee assume f' < 0 on top of very strong disorder for exactly this reason. "
               "(ii) The only implication from very strong disorder available for free: f(beta) < 0 forces R(s) > 0, "
               "i.e. f'(s) < 0, on a set of s in (0, beta) of positive Lebesgue measure (since f = -int s R ds), so f' "
               "cannot vanish on all of (0, beta). (iii) In d = 1, 2 strong disorder is very strong disorder for all "
               "beta > 0 (CV06, L10), and in d >= 3 for bounded disorder (Junk-Lacoin 2024, the source's Theorem 3.10) "
               "but the Gaussian case is unbounded and is the source's Question 1; so for Gaussian disorder Question 2 "
               "reduces to: R(beta) > 0 for every beta in the strong-disorder region, with no intermediate region in "
               "d = 1, 2. (iv) Correction to F0019-A001: its claim that the mu_{i-1} one-step overlap of (3.11) and the "
               "mu_n replica overlap differ by an o(n) boundary term is unproven and is the whole gap; the identity in "
               "A001 is right, the bridge to (3.11) is not."),
    "result_status": "attempted_unsolved",
    "obstruction": ("No known inequality bounds the length-n replica overlap R_n below by the one-step overlaps or by "
                    "|f(beta)|. A route: the derivative of the one-step decomposition, d/dbeta E[log W_i - log W_{i-1}], "
                    "involves mixed overlaps between mu_{i-1} and mu_n; if these are comparable to R_n on average one "
                    "gets R(beta) >= c |f(beta)| / beta, which would answer Question 2 quantitatively in the very strong "
                    "disorder region. Not carried out."),
    "independent_check": "",
}
ap = HERE / "attempts.jsonl"
with ap.open("a", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
print("appended F0019-A002")
