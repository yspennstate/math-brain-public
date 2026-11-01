from pathlib import Path
import json

root = Path(__file__).resolve().parent
logs = ['second_search_log.json', 'second_fetch_log.json', 'second_mirror_log.json',
        'second_author_log.json', 'second_archive_log.json', 'second_primary_log.json',
        'second_download_log.json']
parts = ['\n\n## Second serious attempt: searches and retrievals, 2026-10-12\n',
         'Each following record gives the service through its URL, the exact query or retrieval URL, the date, and the response. All requests used Python from the shell. HTTP success alone was not accepted as evidence of article retrieval.\n']
for name in logs:
    record = json.loads((root / name).read_text(encoding='utf-8-sig'))
    parts.append('\n### ' + name + '\n\n```json\n' + json.dumps(record, ensure_ascii=False, indent=2) + '\n```\n')
parts.append('''
### Retrieval assessment and exact references

Martin P. W. Zerner, *A non-ballistic law of large numbers for random walks in i.i.d. random environment*, Electronic Communications in Probability **7** (2002), paper 19, 191–197, DOI: 10.1214/ECP.v7-1060. The author publication list and Project Euclid article landing page agree with the survey bibliography. Direct PDF requests returned approximately 1.2 KB bot-challenge PDFs, not the article. Archive/mirror failures and incorrect modern URL attempts are retained above. The public text reader of the correct Project Euclid journalArticle/Download URL returned the complete seven-page text, with original printed page boundaries, saved as zerner_download_reader.txt. This is the source actually used for theorem verification.

Theorem 1, printed p.192, verbatim with mathematical layout linearized:
> Theorem 1. Assume (1) and let e ∈ Z^d with |e| = 1 and P_0[A_e ∪ A_{−e}] = 0. Then lim_{n→∞} X_n e/n = 0 P_0-a.s.

Here condition (1), printed pp.191–192, is:
> (ω(z, z + e))_{|e|=1}, z ∈ Z^d, are i.i.d. under P with ω(z, z + e) > 0 P-a.s. for all z ∈ Z^d, |e| = 1.

It is a theorem for Markovian RWRE, not a literature solution for general excited walks. It verifies the exchangeable-arrow special-case application in SECOND_ATTEMPT.md, Section 8. No uniform ellipticity is required.

Lemma 3, printed p.193, verbatim with mathematical layout linearized:
> Lemma 3. Let (X_n)_n ∈ (Z^d)^N be a fixed nearest neighbor path with X_0 = 0 and lim sup_{n→∞} X_n e/n > 0. Then sup_{c≥0} inf_{L≥1} lim sup_{M→∞} F_{M,L}(c) > 0.

Its definition of F uses the diameter of the plane-visit TIME set, not just its cardinality. This lemma is deterministic and therefore applies to cookie walks. A self-contained proof with simpler constants is also recorded in DETERMINISTIC_PLANE_LEMMA.md. Using it to solve the general problem requires the new probabilistic argument here; it is not a solution already in print.

Edwin Hewitt and Leonard J. Savage, *Symmetric measures on Cartesian products*, Transactions of the American Mathematical Society **80** (1955), 470–501, DOI: 10.1090/S0002-9947-1955-0076206-8. Crossref metadata retrieved successfully in hewitt_crossref.json; the AMS full PDF request failed with HTTP 403. The finite-alphabet representation needed for the attempt is proved directly in SECOND_ATTEMPT.md, Section 5, rather than relying on an unread theorem number.

### Exact source inputs for the fresh-hyperplane proof

Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, arXiv:1204.1895v2 (2012), https://arxiv.org/pdf/1204.1895. The already retrieved source.pdf is the complete 37-page source; source.txt preserves page boundaries.

Problem 4.7, p.19, verbatim with mathematical layout linearized:
> Problem 4.7. (d ≥ 1) Assume (IID), (EL), ℓ ∈ R^d\\{0}. Does X_n · ℓ/n converge P_0-a.s. on {|X_n| → ∞}^c to 0 as n → ∞? This would generalize [Zer02, Th. 1].

Theorem 2.5, p.7:
> Theorem 2.5. (d ≥ 1, range) Assume (IID) and (EL). If there is an orthogonal set F ⊂ E such that b_F = 0 then the range is P_0-a.s. infinite. If there is no such set then the range is P_0-a.s. finite.

Only its finite/infinite range dichotomy is used.

Theorem 3.16, p.14:
> Theorem 3.16. (d ≥ 1, Kalikow-type zero-one law) Assume (IID), (EL) and let ℓ ∈ R^d\\{0}. Then P_0[|X_n · ℓ| → ∞] = P_0[A_ℓ ∪ A_{−ℓ}] ∈ {0, 1}.

Lemma 3.18, p.14, proof pp.14–16:
> Lemma 3.18. (d ≥ 1) Assume (IID), E[ω(0, e, 1)] > 0 for all e ∈ E and let ℓ ∈ R^d\\{0} and u, w ∈ R with u < w. Furthermore assume that the range of the ERW is P_0-a.s. infinite. Then P_0[{X_n · ℓ ≥ u i.o.} ∩ {∀n ≥ 0 : X_n · ℓ ≤ w}] = 0.

These quotations are theorem inputs, not quotations of a paper answering Problem 4.7. The fresh-hyperplane proof is an original implication proved in this folder. Consequently its verdict, if accepted after review, is SOLVED rather than SOLVED_IN_LITERATURE.

### Read-only brain questions in this second attempt

- math_recall.py "excited random walk recurrent sublinear range bounded cookie stacks drift budget": returned the old unproved excursion estimate and related recurrence cards; no closure was accepted.
- math_recall.py "Zerner non-ballistic law large numbers iid random environment": returned neighbouring LLN references, not the exact 2002 theorem; the original paper was retrieved separately.
- math_recall.py "de Finetti exchangeable sequences directing measure": card claim_20e7e94fd93a2e51ba5becdbc47068b21245cc7d9d4def4e9e32ec611d9265ad distinguished infinite representation from finite exchangeability. The needed representation was independently proved.
- math_recall.py "excited random walks Lemma 3.18 infinite range slab finite modification": returned source and open-problem/attempt cards, including the warning that depleted environments need not be IID. No independent finite-modification theorem was supplied. The positive-replay argument was checked directly instead.

The initial topic and topic-mistakes brain.py recalls remain recorded above. No brain, store, ledger or repository was modified.
''')
with (root / 'LITERATURE.md').open('a', encoding='utf-8') as out:
    out.write(''.join(parts))
print('Recorded', len(logs), 'search/retrieval logs and checked theorem inputs.')
