# Literature search

Date: 2026-10-12. Results are leads, not certified resolutions.

- kalai_pdf: https://arxiv.org/pdf/1801.02602
  Result: OK; 1229223 bytes.
- arxiv: https://export.arxiv.org/api/query?search_query=all%3A%22noise%20sensitivity%22%20AND%20%28all%3A%22walks%22%20OR%20all%3A%22groups%22%29&max_results=40
  Result: OK; 49586 bytes.
- openalex: https://api.openalex.org/works?search=noise%20sensitivity%20random%20walks%20groups&per-page=30
  Result: HTTP Error 429: Too Many Requests; 0 bytes.
- openalex_source: https://api.openalex.org/works/https://doi.org/10.1142/9789813272880_0017
  Result: HTTP Error 429: Too Many Requests; 0 bytes.
- crossref: https://api.crossref.org/works?query=noise%20sensitivity%20random%20walks%20Benjamini%20Brieussel&rows=20
  Result: OK; 109111 bytes.
- semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=noise%20sensitivity%20random%20walks&limit=20&fields=title,authors,year,url,abstract,externalIds
  Result: HTTP Error 429: ; 0 bytes.
- github: https://api.github.com/search/repositories?q=noise%20sensitivity%20random%20walks
  Result: OK; 55 bytes.

- 1901.03617 | https://arxiv.org/pdf/1901.03617 | OK (2026-10-12)

- 2512.08151 | https://arxiv.org/pdf/2512.08151 | OK (2026-10-12)

- 2403.01658 | https://arxiv.org/pdf/2403.01658 | OK (2026-10-12)

- openalex_retry | https://api.openalex.org/works?search=Three%20puzzles%20mathematics%20computation%20games&per-page=5 | HTTP Error 429: Too Many Requests (2026-10-12)

- semantic_retry | https://api.semanticscholar.org/graph/v1/paper/ARXIV:1801.02602/citations?fields=title,year,externalIds&limit=100 | OK (2026-10-12)

- OpenAlex source lookup 2026-10-12: https://api.openalex.org/works?filter=locations.landing_page_url:http%3A%2F%2Farxiv.org%2Fabs%2F1801.02602&per-page=5; HTTP Error 429: Too Many Requests

## Verified source and papers

- Gil Kalai, *Three puzzles on mathematics, computation, and games*, ICM 2018, arXiv:1801.02602. Source statement verified in Section 3.3.4, PDF p.22; local `kalai_pdf.pdf` and `kalai.txt` preserve it. Fixed epsilon in (0,1), infinite finitely generated group, Cayley SRW, l1 independence. The absence of virtual real homomorphisms is a sufficient-condition conjecture, not a theorem.
- Itai Benjamini and Jeremie Brieussel, *Noise sensitivity of random walks on groups*, ALEA 20, issue 2 (2023), starting p.1139 (Crossref page field), DOI 10.30757/alea.v20-42, arXiv:1901.03617v2 (17 June 2021). Theorem 1.4, arXiv PDF p.3: nonlazy dihedral SRW is not sensitive; lazy dihedral SRW is sensitive. Question 1.5 and Conjecture 1.6 on p.3 explicitly leave the general sufficient condition and Grigorchuk case open. Theorem 1.3 on p.2 concerns entropy sensitivity and partial entropy sensitivity of a permutational extension, and does not establish endpoint TV sensitivity on Grigorchuk.
- Ryokichi Tanaka, *Noise sensitivity on affine Weyl groups*, arXiv:2403.01658v5 (3 July 2025); Combinatorics, Probability and Computing, DOI 10.1017/S0963548325100126 (publication metadata from Semantic Scholar). Theorem 1.1, PDF p.2 requires support S union {id}. It is a special case with laziness and virtually abelian groups, not a resolution of the hypothesis in F0093.
- Jeremie Brieussel and Ryokichi Tanaka, *Noise sensitivity on virtually abelian groups*, arXiv:2512.08151v1 (9 December 2025). Theorem 1.1, PDF p.2 proves noise sensitivity iff no nonzero map onto Z for aperiodic, finite-second-moment, semigroup-generating walks on virtually abelian groups. This is not the general Liouville theorem and the infinite virtually abelian examples have virtual maps to R, outside the conjecture's sufficient-condition hypotheses. Example 1.4, PDF p.3 does supply a nonlazy aperiodic SRW example on D_infinity with four distinct symmetric generators {s1,s2,s1s2,s2s1}. Thus the existential SRW question has a positive special-case answer, but this does not meet the user's exact-case SOLVED_IN_LITERATURE requirement for the full problem.
- Ryokichi Tanaka, *Non-noise sensitivity for word hyperbolic groups*, arXiv:2211.03951v2, DOI 10.5802/afst.1803. Related obstruction on non-elementary hyperbolic walks, not Liouville cases (abstract returned by arXiv search).
- *Noise stability on hyperbolic groups*, arXiv:2501.08487, DOI 10.5802/ahl.273. Found in Semantic Scholar citations of Kalai; related non-Liouville direction, full text not inspected, no resolution claimed.

## Exact extracted statements (not full-problem solutions)

The following are word-for-word PDF text extractions; mathematical symbols and line breaks reflect PDF extraction. None is designated SOLVED_IN_LITERATURE.

### 1901.03617

```text
Question 1.5. If (G, µ) is Liouville and has no virtual morphism onto Z, is it ℓ1-noise sensitive?
```

### 1901.03617

```text
Conjecture 1.6. The ﬁrst Grigorchuk group is ℓ1-noise sensitive.
```

### 2512.08151

```text
Theorem 1.1. Let Γ be a finitely generated virtually abelian group and µ be an aperiodic
probability measure on Γ with finite second moment such that the support generates the
group as a semigroup. Then the µ-random walk on Γ is noise sensitive in total variation,
i.e.
∥πρ
n −µn × µn∥TV →0
as n →∞,
for all ρ ∈(0, 1] if and only if Γ does not admit nonzero homomorphisms onto Z.
```

Semantic Scholar returned 15 citation entries, next cursor None. Relevant titles are reported above.

GitHub repository search returned zero repositories. This is not evidence that no paper exists. OpenAlex was repeatedly rate-limited, so its citing-source search could not be completed. Semantic Scholar supplied source citations instead. Prior ledger F0093-A001 read from the September intake: two invalid information-theoretic inferences are corrected in ATTEMPT.md. Repository path inventory was filtered for F0093/noise sensitivity/Brieussel and returned no matching path; this is not an exhaustive full-text repository search.

- Search 2026-10-12 arxiv_grigorchuk: https://export.arxiv.org/api/query?search_query=all%3AGrigorchuk%20AND%20all%3Anoise&max_results=30; OK 730 bytes

- Search 2026-10-12 openalex_cites_attempt: https://api.openalex.org/works?filter=cites:doi:10.1142/9789813272880_0017&per-page=100; HTTP Error 429: Too Many Requests

## Source Section 3.3.4, PDF page 22 (exact extraction)

```text
3.3.4. A beautiful problem by Benjamini and Brieussel. Consider n steps simple random walk (SRW)
Xn on a Cayley graph of a ﬁnitely generated inﬁnite group Γ. Refresh independently each step with
probability ϵ, to get Yn from Xn. Are there groups for which the positions at time n, Xn and Yn are
asymptotically independent? That is, the l1 (total variation) distance between the chain (Xn, Yn) and
two independent copies (X′
n, X′′
n) is going to 0, with n.
Note that on the line Z, they are uniformally correlated, and therefore also on any group with a
non trivial homomorphism to R, or any group that has a ﬁnite index subgroup with a non trivial
homomorphism to R. On the free group and for any non-Liouville group, Xn and Yn are correlated
as well, but for a different reason: Both Xn and Yn have nontrivial correlation with X1. Itai Benjamini
and Jeremie Brieussel conjecture that these are the only ways not to be noise sensitive. That is, if a
Cayley graph is Liouville and the group does not have a ﬁnite index subgroup with a homomorphism
to the reals, then the Cayley graph is noise sensitive for the simple random walk. In particular, the
Grigorchuk group is noise sensitive for the simple random walk!
```

Search limitations: rate limits prevented OpenAlex verification, and only the returned Semantic Scholar citation page was searched. The source DOI used in the unsuccessful OpenAlex lookup was provisional, not verified; no source identity or citing coverage is inferred from that lookup. The targeted arXiv Grigorchuk/noise search returned zero entries (search words need not occur in metadata). The bounded search supports only "no exact solution found," not an exhaustive assertion of open status.

- Published ALEA PDF fetch, 2026-10-12: https://alea.impa.br/articles/v20/20-42.pdf; HTTP Error 400: Bad Request

## Second attempt literature and brain queries

- 2026-10-12 arXiv growth query: https://export.arxiv.org/api/query?search_query=ti%3A%22growth%22%20AND%20au%3ABartholdi%20AND%20all%3AGrigorchuk&max_results=15; OK
- Read-only math-store recall: "Grigorchuk Liouville entropy noise sensitivity shared increments conditional entropy" and "Kaimanovich Vershik entropy criterion Liouville convolution total variation zero two law". General entropy and Pinsker hints; no specific solution.

- 2026-10-12 fetch Laurent Bartholdi growth paper: https://arxiv.org/pdf/math/0012108; OK

- 2026-10-12 Crossref growth title query: https://api.crossref.org/works?query.title=The%20growth%20of%20Grigorchuk%27s%20torsion%20group&rows=3; OK
- Additional read-only brain query: "Bartholdi Grigorchuk growth upper bound 0.767".

### Bartholdi growth input (not a solution of F0093)

Laurent Bartholdi, *The Growth of Grigorchuk’s Torsion Group*, arXiv:math/0012108, Theorem 1.1, PDF p.1. Exact extracted statement:

```text
Theorem 1.1. Let η be the real root of the polynomial X3 + X2 + X −2, and set α =
log(2)/ log(2/η) ≈0.767. Then the growth γ of Grigorchuk’s group satisﬁes
e
√n ≾γ(n) ≾enα.
```

The definition of growth domination on PDF p.1 is gamma(n)<=delta(Cn); hence the theorem gives |B(n)|<=exp(C_prime n^alpha) after absorbing the change of finite generating weights using Lemma 2.1 (PDF p.2). This verifies the external input used by Proposition A4. The result concerns group growth, not endpoint noise sensitivity.
