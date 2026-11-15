# Row CO08 (the Erdős–Sós conjecture): the counting proof read and checked

12 Nov 2026. Sources: arXiv 2609.17877v1 (D. R. Wood, 15 Sep 2026, "The Erdős–Sós Theorem"), read in full;
the introduction of arXiv 2609.21159v2 (B. Frederickson, "Erdős–Sós via random cyclic orderings"). The proof is
credited to GPT-6 Astra ("A counting proof for Erdős problem 548", 2026); that text is not on arXiv and was not
read. Wood cites a Lean formalization (T. Adamczewski, Erdos548), not examined here.

## The statement

Every graph with average degree greater than t - 2 contains every tree on t vertices.

## The proof, as checked by hand

G has n vertices and m edges. M(G) is the set of pairs (pi, i), pi = (v_1, ..., v_n) an ordering of the vertices,
with v_1 v_i an edge; |M(G)| = 2m (n-1)!. For a tree T and a vertex r of T, R(T, r) is the set of (pi, i) in M(G)
such that G[{v_1, ..., v_i}] contains T with r placed at v_1. The claim is

    (2)   |M(G)| <= |R(T, r)| + (t - 2) n!,

and if G has no copy of T the right side is (t - 2) n!, which gives 2m <= (t - 2) n.

- Lemma 3 (r a leaf, r' its neighbour): |R(T - r, r')| <= |R(T, r)| + n!. For each ordering set aside the least i
  with (pi, i) in R(T - r, r'); for any other (pi, i) reverse the first i entries. The new first vertex v_i is
  adjacent to the new i-th vertex v_1, the copy of T - r sits in an earlier prefix that does not contain v_i, so
  T embeds with r at v_i. Reversal of a prefix of known length is an involution, hence injective.
- Lemma 4 (T = T1 u T2 glued at a non-leaf r): |R(T1, r)| + |R(T2, r)| <= |M(G)| + |R(T, r)| + n!. For
  (pi, i) in R(T1, r) \ R(T, r) other than the least such index j, move the block v_{j+1}, ..., v_i in front of
  v_2, ..., v_j. The image is in M(G) and cannot be in R(T2, r): a copy of T2 at v_1 inside
  {v_1, v_{j+1}, ..., v_i} and the copy of T1 at v_1 inside {v_1, ..., v_j} meet only in v_1 and would give T.
  Injectivity: two preimages of one image agree on a common initial segment, membership in the set-aside family
  depends only on that segment, and each ordering has one set-aside index, so j = j' and then i = i'.
- Induction on t: t = 2 is equality; a leaf root uses Lemma 3; a non-leaf root uses the hypothesis for T1 and T2
  (|V(T1)| + |V(T2)| = t + 1) and Lemma 4.

Every step holds. The argument is two pages and uses nothing beyond counting.

## The computer check (co08_check.py, co08_check.out)

Written from the statements above, not from any other code.

- Literal: for all 74 labelled graphs on 2 to 4 vertices and the 34 graphs on 5 vertices, the sets M(G) and
  R(T, r) were built as explicit sets of (ordering, index) pairs for every rooted tree on at most n vertices.
  (1) held 108 times, (2) 1018 times, Lemma 3 438 times, Lemma 4 906 times. The map of Lemma 3 was applied
  11,978 times and the map of Lemma 4 24,344 times: each image lay in the stated set and no image was hit twice.
- Counting: for the 156 graphs on 6 vertices, 150 random graphs on 7 vertices and 40 on 8, with every rooted
  tree on at most n vertices: (2) 26,176 times, Lemma 3 11,256, Lemma 4 45,046, and the theorem itself
  (average degree above t - 2 forces a copy) 4,632 times. No failure.
- Control: on K_5 with trees on 6 vertices (2) is an equality, and with t - 3 in place of t - 2 it fails for
  all 20 rooted trees, so the check can fail. (The line of the output that counts graphs with equality in (2)
  is uninformative: t = 2 is always an equality.)

## Follow-up literature (lit/search/s1.xml, s2.xml, s3.xml; titles and abstracts only)

No correction or objection found. Expositions and extensions since September 2026: Cummings 2609.32011
(exposition); Frederickson 2609.21159 (simplified proof, digraphs, hypergraphs, extremal examples for Kalai's
conjecture); Mubayi and Verstraëte 2609.08012 (Kalai's conjecture for tight trees) and 2609.10987 (digraphs);
Santos, Stein and Williams 2609.09142; Reed and Stein 2609.05417, 2609.05411 (dense graphs and the extremal
cases, by other methods). Frederickson's introduction attributes the antidirected-tree conjecture of
Addario-Berry, Havet, Linhares Sales, Reed and Thomassé to Riordan and Scott, to Santos, Stein and Williams and
to the model independently, and the extremal graphs for Erdős–Sós to Riordan and Scott.

## Proposal for the row

The conjecture is proved, and the proof was verified here line by line and by exhaustive small cases. Remove the
row from the open list. Kalai's conjecture and the antidirected version fell to the same method, so they are not
replacements. Candidates to examine for the slot: the Loebl–Komlós–Sós conjecture (median degree), and the
conjecture of Havet, Reed, Stein and Wood (maximum degree at least k and minimum degree at least 2k/3 force every
tree with k edges); whether the counting method reaches either was not looked at.
