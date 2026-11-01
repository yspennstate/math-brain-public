"""Rewrites the F0090 problem/attempt rows (Kalai Conjecture 8) after the GPS text was read: the box bound
does not need GPS at all, it follows from P(S meets B) = E Var(f | outside B) <= P(four arms from B).
Run once; keeps every other row byte-identical."""
import json, os
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
def rewrite(path, key, fn):
    rows = [json.loads(l) for l in (HERE / path).read_text(encoding="utf-8").splitlines() if l.strip()]
    n = 0
    for r in rows:
        if r.get(key) == "F0090" or r.get("problem_id") == "F0090":
            fn(r); n += 1
    with (HERE / path).open("w", encoding="utf-8", newline="\n") as s:
        for r in rows:
            s.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    print(path, "rows rewritten:", n)

def fix_problem(r):
    r["result_status"] = "candidate_full_solution"
    r["status_search"] = ("Dedup: no entropy-influence or spectral-sample rows in intakes A-E. WebSearch 2026-09-08 (entropy influence conjecture status): the general Fourier-entropy-influence conjecture is open (Han, Combinatorica 2025; further classes verified in 2026); no paper on the percolation special case found. The text of Garban-Pete-Schramm, 'The Fourier spectrum of critical percolation' (Acta Math. 2010, arXiv 0803.3750) was read for its box estimates: their Proposition 4.1 bounds P(|S_r| = k) by g(k)(R/r)^2 alpha_4(r,R)^2 and their Lemma 4.3 bounds P(S compatible with an annulus structure) by h(A)^2; neither is the plain one-box bound used below, which is instead derived directly in the attempt. Kept; see the attempt, which claims a proof.")

def fix_attempt(r):
    r["method"] = ("Two elementary steps. (1) Entropy of a random subset S of the n x n box by dyadic encoding: with pattern_k the set of dyadic boxes of side n 2^{-k} meeting S, the chain rule gives H(S) <= H(pattern_0) + sum_k H(pattern_{k+1} | pattern_k) <= log 2 + (log 15) sum_k E[N_k], where N_k is the number of occupied level-k boxes, because given pattern_k the next pattern is a choice of a nonempty subset of the four children for each occupied box. Hence H(S) <= log 2 + (log 15) sum_k sum_{B at level k} P(S meets B), for ANY random set S. (2) One-box bound for the spectral sample of the +-1 crossing indicator f: P(S_f meets B) = sum_{T meets B} f-hat(T)^2 = ||f||^2 - ||E[f | omega outside B]||^2 = E[Var(f | omega outside B)], and the conditional variance vanishes unless the outside configuration leaves the crossing undetermined, which forces four alternating arms (open to the left and right sides, closed to the top and bottom sides) from the boundary of B to the sides of the square; so P(S_f meets B) <= P(A_4(B)), the probability of that arm event. For the pivotal set P(P_f meets B) <= P(A_4(B)) trivially (a pivotal site in B has the four arms).")
    r["result"] = ("Combining (1) and (2): H(S(f)) and H(P(f)) are both at most log 2 + (log 15) sum_k sum_{B at level k} P(A_4(B)). For a box B of side r at distance d from the boundary, P(A_4(B)) <= C alpha_4(r, d) alpha_3^+(d, n) with alpha_3^+ the half-plane three-arm probability, of order (d/n)^2 on any lattice. On the triangular lattice alpha_4(r, d) = (r/d)^{5/4 + o(1)} (Smirnov-Werner), so the bulk boxes at level k contribute (n/r)^2 alpha_4(r,n) = (n/r)^{3/4 + o(1)} and the boundary boxes at distance d contribute (n/r)(d/r) alpha_4(r,d) (d/n)^2 = (d/n)^{7/4}(n/r)^{3/4} up to o(1) in the exponents, summing over dyadic d to the same order; hence sum_k E[N_k] <= C sum_k (2^k)^{3/4 + o(1)} <= C' n^{3/4 + o(1)}, while I(f) = E|S(f)| = E|P(f)| = n^2 alpha_4(1, n) = n^{3/4 + o(1)}. With quasi-multiplicativity in place of the exact exponents: sum_k (n/r_k)^2 alpha_4(r_k, n) = I(f) sum_k 1/(r_k^2 alpha_4(1, r_k)), and the series converges as soon as r^2 alpha_4(1, r) >= c r^{epsilon} for some epsilon > 0, i.e. as soon as the four-arm exponent is strictly less than 2. That holds on the triangular lattice (exponent 5/4). CONCLUSION: on the triangular lattice, H(S(f)) <= C I(f) and H(P(f)) <= C I(f) with absolute constants, which is Conjecture 8 as stated; on Z^2 the same argument gives the conjecture provided r^2 alpha_4(1,r) grows polynomially (four-arm exponent < 2), which I believe is known from Kesten's arm-exponent inequalities but did not verify. Author-checked only: the two steps are short and each was re-derived (the identity in (2) is Parseval for the conditional expectation, and the alternating-arms claim is the standard characterisation of when a box is pivotal-able), and the ledger holder should check the boundary-box bookkeeping and the Z^2 hypothesis before treating this as settled.")
    r["obstruction"] = ("None on the triangular lattice, if the two steps are right. What remains: the Z^2 version needs the strict inequality (four-arm exponent < 2), and the constant depends on the boundary-box estimate; the argument is specific to functions whose 'box influences' E Var(f | outside B) are summable over dyadic scales, so it does not touch the general entropy-influence conjecture, only the percolation special case Kalai singled out.")
    r["key_identity"] = ("P(S_f meets B) = E[Var(f | omega outside B)] <= P(four alternating arms from B); H(S) <= log 2 + log 15 sum_{scales} sum_{boxes} P(S meets B); sum_k (n/r_k)^2 alpha_4(r_k,n) = I(f) sum_k 1/(r_k^2 alpha_4(1,r_k)) converges when the four-arm exponent is below 2.")
    r["independent_check"] = "none yet; author-checked 2026-09-08"

rewrite("problems.jsonl", "problem_id", fix_problem)
rewrite("attempts.jsonl", "problem_id", fix_attempt)
