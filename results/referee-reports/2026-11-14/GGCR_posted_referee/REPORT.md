# Referee report: cluster repulsion on the grandparent graph

Paper: yspennstate/grandparent-graph-cluster-repulsion at 8c7fb8b (paper/main.tex, 7 pages). Referee: an agent,
14 Nov 2026.
Claim: for Bernoulli(p) bond percolation on the grandparent graph GP_b, b >= 2, at every p, two distinct infinite
clusters touch along only finitely many edges almost surely (cluster repulsion). This answers, for GP_b, the question of
Haggstrom, Peres and Schonmann as restated by Bell, Chu, Rodgers, Terlov and Tserunyan (arXiv:2509.10631, Question 1.1).
The route: the cone reliability r(p) is the unique root in (0,1] of t = 1 - (1-p)(1 - pt)^b when it is positive;
an attached cone acts as a single edge of probability p r(p); disjoint boundaries B(a_{3k}) of b+2 edges give a
geometric tail for the number of touching edges, and sprinkling (HPS) finishes.

## Verdict

SOUND. Commit 3a07d69 ("Fix references"), PDF rebuilt (7 pages, no undefined references, no overfull boxes):

1. The BCRTT bibliography entry had wrong initials; the authors are S. Bell, T. Chu, O. Rodgers, G. Terlov and
   A. Tserunyan (checked on arXiv:2509.10631v2). Fixed.
2. The HPS question was cited as [HPS99, Question 3], a number I could not confirm (the chapter is not online).
   The locator is now p. 87, which is where BCRTT place it. Both occurrences changed.
3. The introduction now says that the HPS non-coexistence theorem (HPS99 Thm 4.1.6, as used in BCRTT Lemma 3.5)
   reduces the question to whether two light infinite clusters can touch infinitely often, and cites BCRTT
   Question 1.1 for the restated form.
4. SHA256SUMS regenerated for main.tex and main.pdf; a fresh clone with core.autocrlf=false passes all 15.

No change to any statement or proof.

## Proofs checked (re-derived)

- The graph: degree b^2 + b + 2; the parent map is recoverable (a parent shares b + 1 common neighbours with its
  child, any other neighbour shares 1), so GP_b is quasi-transitive with the stated non-unimodular weights b^{h(x)}.
- Cone lemma: r(p) satisfies t = 1 - (1-p)(1 - pt)^b; the right side is concave in t, so the positive root is unique
  when it exists; continuity in p follows from the implicit function theorem away from p_c and from the limit at p_c.
  Equivalent to Mazzei-Spakulova (arXiv:2611.09762, eq. (7)) through x = 1 - p r(p).
- Lemma on finite cones: the cluster of the cone K_z seen from its apex is open-connected to infinity with probability
  p r(p), independently across disjoint cones.
- Boundary lemma: B(a_{3k}) has b + 2 edges and boundaries at spacing 3 are disjoint; spacing 2 would also do, so
  3 is conservative.
- Tail bound: the number of touching edges between two clusters is dominated by a geometric variable; the sprinkling
  lemma then rules out infinitely many touches.

## Citations checked against the sources

- BCRTT arXiv:2509.10631v2: Question 1.1 is the HPS question from p. 87; Theorem 1.2 (heavy repulsion), Lemma 3.5,
  and the use of HPS99 Theorem 4.1.6 (non-coexistence of heavy and light) all as stated.
- MS26 arXiv:2611.09762: eq. (7) and its credit to Spakulova, Section 5.3, for p_c of the grandparent tree.
- Timar math/0702873 Theorem 1.1; Haggstrom-Jonasson math/0612812 end of Section 5 (nonunimodular case open);
  Hutchcroft arXiv:1711.02590 (p_c < p_h on nonunimodular transitive graphs).
- Bell-Rodgers slides (DDC, 24 Mar 2026): they name continuity of the two-point function as the hard step and leave the
  infinite-but-light touching case open; consistent with the introduction.
- Crossref, all six DOIs (HJ06, Hut20, Spa09, Tang19, Tim06a, Tim06b): authors, journal, volume, pages as listed.
- Prior-work search (web, two wordings, plus the arXiv listing after MS26): nothing answers the question for GP_b.

Not verifiable: Remark 2.2 attributes "p_c < p_h = p_u = 1 on GP" to [HPS99]. The chapter is not online and I could
not confirm the page. The statement itself is plausible (BCRTT and MS26 both describe the light phase on GP as
extending to p = 1), but the attribution should be checked against a copy of the book. A self-contained replacement
argument is not immediate: cone clusters use grandparent edges, so a naive branching bound does not give p_h = 1.
The sentence is left as written.

## Numbers checked independently

- code/check_proof.py rerun on Mac mini 2: all 15 checks pass. code/audit_data.py: 36 BFS configurations, 396 level
  counts, 48 pair rows; both JSON outputs byte-identical to the committed ones.
- "The largest number of edges between one pair was 14": maximum of adjacency_edges over 592 pairs is 14; the summary
  has 108 rows = 3 values of p x 3 depths x 12 seeds, as described.

## Minor (not acted on)

- The abstract is 155 words; the code-availability URL points at the repository root rather than a commit.
- "1/b < p < 1" for the light range understates it (MS26: p_c <= 1/b).
- The step-3 spacing in the boundary lemma could be 2.
- There is no AUDIT_<date>.md beside the .tex; this report serves as the audit.
