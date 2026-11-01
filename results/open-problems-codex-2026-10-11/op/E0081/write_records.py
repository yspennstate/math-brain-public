from pathlib import Path
import json
root=Path(__file__).resolve().parent
header='''# Literature and status check — E0081

Date: 12 October 2026. Retrieval used Python urllib from the shell, not a built-in web search. Raw successful responses, downloaded PDFs and extracted texts remain in this folder.

## Confirmed source

Jim Pitman and Wenpin Tang, **Patterns in Random Walks and Brownian Motion**, in *In Memoriam Marc Yor – Séminaire de Probabilités XLVII*, Lecture Notes in Mathematics 2137, Springer, 2015, pp. 49–88. DOI: 10.1007/978-3-319-18585-9_4. arXiv:1411.0041v3, posted 10 September 2015, manuscript dated 11 September 2015. Download: https://arxiv.org/pdf/1411.0041 (732611 bytes), saved as source.pdf/source.txt.

Question 1.7, printed/PDF page 5, verbatim (mathematical typography normalized):

> Given for each n a collection A_n of patterns of length n, what is the order of the expected waiting time ET(A_n) until some element of A_n is observed in a random walk?

The preceding paragraph specifies **simple symmetric random walks of length n with increments ±1 starting at 0**. No regularity, closure, monotonicity or cardinality hypothesis is imposed on A_n. Theorem 1.8, page 6, handles special families: excursions have mean of order n^(3/2), positive walks and bridges have order n, and the displayed bounds for fixed-negative-level first-passage walks are c n and C n^(5/4). Theorem 2.1, page 7, already gives an exact matching-matrix formula for any fixed finite collection. This is not a later solution to the asymptotic research program.

## Relevant papers and leads

1. Min-Zhi Zhao, Dong Xu and Hui-Zeng Zhang, **Waiting times and stopping probabilities for patterns in Markov chains**, arXiv:1602.06512v2 (2016/2017 version). PDF downloaded and inspected; its Theorem 2.1 is a generating-function linear system for a finite collection in a Markov chain. It does not give the asymptotic order for every scale-indexed collection in Question 1.7. Lead only.
2. Yuuya Yoshida, **A simple proof of the formula of Solov'ev–Nielsen–Blom for the expected waiting time**, arXiv:2410.13426v1 (2024). PDF downloaded and inspected. Theorem 1.1 is explicitly for one finite word. Useful for singleton/run means; not a solution for arbitrary families.
3. Søren Riis and Mike Paterson, **Coin flipping and waiting times paradoxes: Why fair coins are exceptional**, arXiv:2601.16580v2 (2026). PDF downloaded and inspected. Theorems 1 and 2 concern stochastic ordering and independent two-player string races; Theorem 5 gives a single-pattern generating function. Distinct model/quantifiers, not a solution to Question 1.7.
4. Urszula Ostaszewska and Krzysztof Zajkowski, **On the waiting time till some patterns occur in i.i.d. sequences**, arXiv:1302.4859v1 (2013). Abstract inspected in the arXiv response: solutions of the Guibas–Odlyzko finite linear system. Predates the source; lead only.
5. Krzysztof Zajkowski, **A note on the gambling team method**, arXiv:1310.4316v2 (2013). Abstract inspected: fixed-collection generating-function system with known initial outcomes. Predates the source; lead only.
6. Jungtaek Oh, **On distribution of runs and patterns in four state trials**, arXiv:2211.00774v2 (2022). Abstract inspected: run-length and waiting-time distributions for four-state trials. No full-scope solution identified in the abstract; full theorem audit not performed.
7. M. V. Koutras and F. S. Milienos, **Exact and asymptotic results for pattern waiting times**, *Journal of Statistical Planning and Inference* 142(6) (2012), 1464–1479. DOI: 10.1016/j.jspi.2011.12.028. Crossref bibliographic record fetched. Predates the source; full text not obtained, so no claim about its theorems. Potential classical-background lead.

The run mean used in ATTEMPT.md is classical. The new record gives independent complete proofs; it does not assert originality of the sharp extremal bounds.

Classical references read from the source bibliography: Stephen Breen, Michael S. Waterman and Ning Zhang, **Renewal theory for several patterns**, *Journal of Applied Probability* 22(1) (1985), 228–234, DOI 10.2307/3213763; Leo J. Guibas and Andrew M. Odlyzko, **String overlaps, pattern matching, and nontransitive games**, *Journal of Combinatorial Theory, Series A* 30(2) (1981), 183–208; Shuo-Yen Robert Li, **A martingale approach to the study of occurrence of sequence patterns in repeated experiments**, *Annals of Probability* 8(6) (1980), 1171–1176. These are prior finite-pattern methods, not later resolutions of Question 1.7.

## Search coverage and limitations

The arXiv math.PR search returned 20 entries, including the source, fixed-pattern papers above and unrelated queueing/scaling papers. Their titles and abstracts were reviewed; three later plausible papers were fetched in full. A broader recent-first arXiv search returned mostly unrelated transport and queueing applications, prompting the targeted search. Crossref returned the source DOI and related bibliographic records. No inspected theorem states and proves Question 1.7 with the same objects, hypotheses and quantifiers.

OpenAlex source search and DOI resolution returned HTTP 429, so a valid OpenAlex work ID could not be obtained for the normal cites:<work-id> query. A DOI-form citation-filter attempt also returned 429; that attempt is **not** counted as a successful citing-works search, and its filter syntax was not validated. Semantic Scholar's source-record/citations request and search returned HTTP 429. GitHub repository search returned HTTP 403 rate-limit exceeded. These failures prevent an exhaustive citation check. The correct status is **no verified full-scope solution found in this bounded search**, not a definitive assertion that none exists.

No SOLVED_IN_LITERATURE verdict is warranted. There is no purported resolving theorem to quote or line-by-line reduction to provide.

## Read-only brain and earlier work

Executed math_recall.py with “Pitman Tang pattern matching matrix waiting time”; it returned mostly off-target cards (including a permutation-pattern inequality paper). Executed brain.py recall with “pattern waiting time mistakes” and “Pitman Tang random walk patterns”; neither returned a directly relevant research result. The recall script reported an automatic index-refresh side effect; no remember/write command was requested, and it was not invoked again after the recalls. The prescribed scripts were treated only as hints.

Searched intake and pool JSONL records for E0081. Found E0081-A001 and neighboring E0082-A001 in probability_1000_intake_E_20260908. Their finite correlation-system lead is classical, but the claimed excursion density discrepancy is erroneous and the autocorrelation-only race identity omits cross correlations. ATTEMPT.md explains the corrections. Listed origin/master paths in ~/math-open-problems read-only, then filtered for E0081/Pitman: no relevant answer path found. No repository working tree was changed.

## Every network query/download recorded

The source download above preceded the structured log. Subsequent queries are listed below exactly, with their outcome. All dates are 2026-10-12.

'''
lines=[]
for line in root.joinpath('search_log.jsonl').read_text(encoding='utf-8').splitlines():
    x=json.loads(line)
    outcome=str(x.get('status',x.get('error')))
    lines.append(f"- **{x['service']}** — `{x['query_url']}` — {outcome}; date {x['date']}.")
root.joinpath('LITERATURE.md').write_text(header+'\n'.join(lines)+'\n',encoding='utf-8')

claims=[
 ('For nonempty A subset {0,1}^n of density p, max(n,1/(2p)) <= E T_A <= n/p.', 'proved', 'ATTEMPT.md Section 1', 'Does not determine the order for a given structured family.', 'Exact rational tests on 398 finite collections.'),
 ('For q the density of (2n-1)-bit words containing an A-window, n/(2q) <= E T_A <= (2n-1)/q.', 'proved', 'ATTEMPT.md Section 2', 'Evaluating q_n asymptotically remains a finite union-counting problem.', 'Exact enlarged-set enumeration and rational automaton means for 398 collections.'),
 ('For A(n,k) containing a k-run, T_A=max(n,R_k), E R_k=2^(k+1)-2, and mu-mu^2/2 <= P(A(n,k)) <= mu, mu=(n-k+2)/2^(k+1).', 'proved_special_case', 'ATTEMPT.md Section 3; RunRecurrence.lean', 'Lean checks the algebraic recurrence only, not the probabilistic model.', 'Run density and history enumeration for k<=n<=8; exact means for n<=6; Lean exit code 0 in lean_check.txt.'),
 ('There exist families A_n,B_n with exactly equal cardinalities Theta(2^n/n), but E T(A_n)=Theta(n^2) and E T(B_n)=Theta(n).', 'proved_special_case', 'ATTEMPT.md Section 4', 'Disproves cardinality-only order, not the source research question.', 'Exact equal-cardinality constructions n=4..10; rational run asymptotics n=16..1024.'),
 ('Uniformly for 1<=m<=2^n, p=m/2^n, min_{|A|=m} E T_A = Theta(n+1/p).', 'proved', 'ATTEMPT.md Section 5 minimum proof', 'An extremal theorem does not determine the mean of a particular family.', 'All 62 prescribed-cardinality constructions with n<=5 checked in exact arithmetic.'),
 ('Uniformly for 1<=m<=2^n, p=m/2^n, max_{|A|=m} E T_A = Theta((1+log_2 m)/p), with explicit constants 1/24 and 10.', 'proved', 'ATTEMPT.md Section 5 upper and lower proofs', 'An extremal theorem does not determine the mean of a particular family; novelty not asserted.', 'Logarithmic bounds checked on 398 collections; all 62 prescribed-cardinality constructions n<=5 checked in exact arithmetic.'),
 ('The computed sequence n P(A(n,2 log_2 n)) approaches 1/2 and E T(A(n,2 log_2 n))/n^2 approaches 2 along n=2^r.', 'numerical_evidence', 'checks.json asymptotics; ATTEMPT.md Section 4 separately proves these limits', 'Finite numeric evidence alone does not prove asymptotics.', 'Exact rational run-state recursion, converted to floats only for table output.'),
]
with root.joinpath('CLAIMS.jsonl').open('w',encoding='utf-8') as f:
    for claim,status,loc,gap,checks in claims:
        f.write(json.dumps({'problem_id':'E0081','claim':claim,'status':status,'proof_location':loc,'remaining_gap':gap,'checks':checks},ensure_ascii=False)+'\n')

root.joinpath('STATUS.md').write_text('''STATE: DONE
NEXT: Evaluate the enlarged-window hit probability for a specified natural family; full Question 1.7 remains unresolved.
VERDICT: PARTIAL

2026-10-12: Verified source arXiv:1411.0041v3, Question 1.7 p.5 and its symmetric-walk hypotheses. Later arXiv papers inspected; no full-scope resolving theorem verified. OpenAlex/Semantic Scholar/GitHub rate limits leave citation coverage incomplete.
2026-10-12: Proved universal bounds and E T_A=Theta(n/q) for an explicit enlarged-word density q. Constructed exactly equal-cardinality families with Theta(n) versus Theta(n^2) mean completion times.
2026-10-12: Proved sharp prescribed-cardinality extrema: min=Theta(n+2^n/m), max=Theta((1+log_2 m)2^n/m), uniformly for 1<=m<=2^n. Full proofs and limitations in ATTEMPT.md.
2026-10-12: Hostile-referee checks passed: 398 finite collections, 357 independent matching-matrix comparisons, 62 prescribed-cardinality constructions, exhaustive run/history checks, and Lean kernel verification of the run Bellman algebra (exit 0). Earlier ledger counting/race-identity errors were identified and excluded.
2026-10-12: Bounded attempt complete. Remaining gap: estimates for an individually specified natural family, notably the source's first-passage exponent gap, are not supplied by the extremal results. No full-scope solution or literature solution claimed.
''',encoding='utf-8')
print('Wrote LITERATURE.md, CLAIMS.jsonl, STATUS.md')
