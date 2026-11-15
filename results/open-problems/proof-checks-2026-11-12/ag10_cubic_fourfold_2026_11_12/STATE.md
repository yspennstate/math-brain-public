# AG10 state (12 Nov 2026)

Done: note `AG10_CHECK.md`; test `ag10_check.py` -> `ag10_check.out`; searches `lit/search/ids.xml`, `s1.xml`,
`s2.xml`, `s3.xml`.

Kept locally, not in the repository: `lit/2508.05105/` (Katzarkov-Kontsevich-Pantev-Yu, 82 pages),
`lit/2610.40811/` (Guéré, 16 pages), `lit/openai/` (62 pages; `main_c.txt` is the compact text, 2802 lines).

Source addresses:
- https://arxiv.org/abs/2508.05105 ; https://arxiv.org/abs/2610.40811 ; https://arxiv.org/abs/2603.04518 ;
  https://arxiv.org/abs/2607.26718
- https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026.pdf

Read: in 2508.05105 the introduction and Section 6.2 (compact text lines 1-280 and 2800-2960); in 2610.40811
lines 1-215; in the OpenAI preprint lines 1-150 (introduction), 889-905 (Proposition 3.10), 2436-2510
(Theorem 6.6, Proposition 7.1).

Not done: Sections 2 to 5 of 2508.05105; the proofs in Sections 3 to 6 of the OpenAI preprint. If the second half
of that preprint is taken up, start at Section 4 (line 1100 on) with Theorem 4.9 (the Sarkisov factorization
used), then Proposition 5.3, Lemma 5.6, Theorem 6.5 and Theorem 6.6.

## 12 Nov 17:56 - OpenAI preprint Sections 4-6 read line by line, no gap (one reader)
AG10_SECTIONS_4_6_READING.md. No gap in Sections 4, 5 and 6. A harmless sign misprint in (5.5) (- v(V/B) should be
+ v(V/B); (6.10) and the introduction are right). Large d enters the Sarkisov side only in Lemma 6.1: degree-<=14
covers of a bounded surface have pencils of bounded genus, against 2g-2 >= n sqrt d (Lemma 4.1). That is where the
rational cubics (d = 14, 26, 38, 42) must escape, and do. Prop 5.10's tables were checked exhaustive by brute force
(ag10_table514.py, .out). Not read in full: Sections 1-3 and 7. Status unchanged: the row stands on KKPY Thm 6.8 and
the OpenAI claim needs a second independent audit.

## 12 Nov 18:10 - the whole OpenAI preprint read (Sections 2-7), no gap; correction to the entry above
Sections 2, 3 and 7 are now read too (AG10_SECTIONS_4_6_READING.md; the name is historical). Section 3 holds: the
GW operator algebra of Thm 3.3 never mixes blocks, even when a blown-up K3 is Hodge isometric to T_M, because a
mixed relative tensor is triangular over an absolute tensor with insertion i_* W = 0 (Lemma 3.6). So Lemma 3.8 can
track whole blocks by central idempotents without a unique lattice decomposition. Lemma 3.9 (p_g = 1, rank 21
gives a K3) re-derived from Noether. Section 7 checked.
CORRECTION to the previous entry: large d does not enter "only in Lemma 6.1". It enters in Prop 5.4 (links over a
point or curve), Lemma 6.3 and Lemma 6.1. The Pfaffian d = 14 escapes at Prop 5.4. Status unchanged: one reader,
no gap; the row stands on KKPY Thm 6.8 until a second, independent audit.
