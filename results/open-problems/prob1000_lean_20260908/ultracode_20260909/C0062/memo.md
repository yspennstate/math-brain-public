# C0062 - the maximal-dimension Young diagram for finite n (Romik, Section 1.18)

Date: 2026-09-09. Output dir: this directory. Budget used: about 1 h 50 min.

## 1. The problem as the source states it

Romik, *The Surprising Mathematics of Longest Increasing Subsequences*, manuscript of
August 20, 2014, Section 1.18, p. 64 of the book (PDF page 74), immediately after
Theorem 1.24 (the maximal-dimension shape converges to the Logan-Shepp-Vershik-Kerov
limit shape):

> "Note that the theorem gives only an approximate answer to the question that is valid
> in the limit of large n. More detailed results have been derived on the irreducible
> representation of maximal dimension and on its dimension, and on the related question
> of better understanding the asymptotics of the typical dimension of a Plancherel-random
> Young diagram (see [23], [140], [143]), but these results are still of an asymptotic
> nature. Some interesting open problems in this context would be to say anything precise
> (that is, nonasymptotic) about the maximal dimension shape for finite values of n (e.g.,
> in the form of some kind of explicit description or even just an efficient algorithm for
> computing this shape); to prove that the maximal dimension shape is unique; and to
> improve the asymptotic bounds in the papers cited earlier."

His references: [23] Bufetov 2012 (GAFA), [140] Vershik and Pavlov 2009, "Numerical
experiments in problems of asymptotic representation theory", Zap. Nauchn. Sem. POMI 373,
77-93 (J. Math. Sci. 168 (2010) 351-361), [143] Vershik and Kerov 1985 (Funct. Anal.
Appl. 19, 21-31). Footnote 12 traces the question to Bivins, Metropolis, Stein and Wells
(1954), Baer and Brock (1968) and McKay (1976).

There are no inequalities in the statement. Three sub-questions: (i) an explicit
description or an efficient algorithm for the maximiser at finite n; (ii) a proof that
the maximiser is unique; (iii) better asymptotic bounds on the maximal dimension. The
ledger row states this faithfully. One qualifier is forced and is not in the source:
dim(lambda) = dim(lambda') for every lambda, so "unique" can only mean unique up to
conjugation. The earlier attempt A001 made the same point.

## 2. Finding

Nothing here settles any of (i)-(iii). What this attempt adds:

1. Prior art the campaign had missed. The exact computation the integrator asked me to
   "extend as far as feasible" was already far ahead of the campaign's n <= 44 in the
   literature before the source was written: Vershik and Pavlov (2009/2010, Romik's own
   reference [140]) found the maximal diagrams for all n <= 130 by exhaustive search, and
   Duzhin's table in OEIS A003040 gives the maximal dimension for n <= 153. The most
   recent paper, Duzhin and Smirnov-Maltsev, "On Young diagrams of maximum dimension",
   Communications in Mathematics 31 (2023) no. 3, 33-47 (arXiv:2311.15199), proves a
   structural lemma, states a structural conjecture, and says of it: "This statement has
   not been strictly proven, but during computer experiments it was found that all known
   Young diagrams with large and maximum dimensions with sizes up to 10^6 boxes have this
   geometric property." So as of December 2023 all three sub-questions are still open as
   theorems. Details in Section 6.

2. An independent exhaustive recomputation for every n <= 90 (my own code, hook-length
   formula, every partition), cross-checked value by value against the OEIS b-file. For
   every n <= 90 the maximiser is unique up to conjugation: a single self-conjugate shape
   for the 35 values n = 1, 3, 5, 6, 8, 10, 12, 15, 17, 21, 23, 27, 30, 34, 36, 38, 42, 44,
   47, 51, 53, 57, 61, 63, 67, 69, 71, 72, 74, 78, 80, 82, 84, 86, 90, and exactly one
   conjugate pair otherwise. The smallest log-gap between the maximum and the best
   non-conjugate shape is 0.00040 (n = 35 and n = 36); nine values of n have a gap below
   0.01. Whether Vershik-Pavlov recorded uniqueness explicitly for n <= 130 I could not
   check (the paper is behind a paywall and the Russian original did not load); the 2023
   paper does not mention uniqueness.

3. Structure of the maximisers for n <= 90, read off the exhaustive data. Orient each
   maximiser so that lambda_1 >= l(lambda) (number of rows). Then lambda_1 - l(lambda) is
   0 or 1 for every n <= 90; the boxes outside the symmetric core (lambda intersected with
   lambda') number at most 3, always lie on one side of the diagonal, at most one per
   row. This is exactly the Duzhin-Smirnov-Maltsev conjecture, which they report holds
   for all known maximisers to 10^6 boxes, so it is confirmation and not news.

4. A candidate structural theorem, with the naive proof route closed. The natural
   statement is: every maximiser has |lambda_1 - l(lambda)| <= 1. A proof would follow
   from a "width lemma": if lambda_1 >= l + 2 then some single-box move increases the
   dimension. I tested three versions exactly (integer hook products) on all partitions.
   (A) Move the top-right corner box to a new last row: false, first failure n = 13,
   (6,5,1,1) -> (5,5,1,1,1), 5720 -> 5005. (R7) Move some corner box to a new last row:
   true for all partitions with n <= 26, false at n = 27, (10,7,5,1,1,1,1,1), and 402
   further failures up to n = 45. (B) Some single-box move, any corner to any outer
   corner: true for every partition with lambda_1 >= l + 2 and n <= 40 (zero failures
   among all such partitions), unproved. Given that R7 survived to 26 and died at 27, B
   at 40 is weak evidence, and I report it as a conjecture only.

5. One exact identity, certified in Lean 4. For the hook (c+1, 1^b), the move (A) gives
   the hook (c, 1^(b+1)), and dim(after) / dim(before) = c / (b+1) = (lambda_1 - 1) / l(lambda)
   exactly. So among hooks the move increases the dimension iff lambda_1 >= l + 2, and
   ties iff lambda_1 = l + 1 (the two shapes are conjugate). The same exact ratio
   (lambda_1 - 1)/l holds for the near-rectangles (m, (m-1)^(l-1)) by the same hook
   bookkeeping (row-1 hooks shrink by one, column-1 hooks grow by one, both products
   telescope). The Lean file U_C0062.lean proves the binomial identity
   C(c+b, b+1) (b+1) = C(c+b, b) c, the strict inequality C(c+b,b) < C(c+b,b+1) when
   b + 2 <= c, and the tie at c = b + 1; it compiled clean and depends only on propext,
   Classical.choice, Quot.sound. It takes dim(c+1,1^b) = C(c+b, b) as the standard fact
   it is; the Lean certifies the arithmetic step, not the hook-length formula.

## 3. Method and checks

Enumeration (enum_maxdim.py): a numba loop over every partition of n with
lambda_1 >= l(lambda) (the other half is the conjugate image; dimension is
conjugation-invariant), log-dimension by the hook-length formula, top six kept, then an
exact integer recomputation of the top candidates in Python and an exact gap to the best
non-conjugate candidate. The count of enumerated partitions equals (p(n) + #{lambda_1 =
l(lambda)})/2 exactly at n = 30, 45, 60 (checked with sympy and a second partition
generator). Float error in the ranking is about 1e-13; the smallest gap is 4e-4, so the
float ranking cannot have misordered the top.

The second independent check earned its keep. My first run had an off-by-one in the
numba hook length (it ranked by the product of (hook+1)), and that wrong ranking agrees
with the true one for every n <= 82 and first disagrees at n = 83, where the OEIS/Duzhin
value was larger than my "maximum". I found the bug only because I compared against the
b-file. The buggy output is kept as maxdim_results_BUGGY_hookplus1.jsonl and
sweep_BUGGY.log; do not read them. After the fix every value for n <= 90 agrees with
A003040 (Schmidt's exhaustive SageMath values to 80, Duzhin's to 153), and the small-n
maximisers agree with A117500.

Scripts: enum_maxdim.py (sweep), analyze.py (uniqueness, OEIS comparison, structure),
make_table.py, test_width_lemma.py (move A and claim B to n = 28), test_width_rules.py
(R7 and R8 to n = 26), test_claim_c.py (R7 to n = 45, exact), test_claim_b_at_failures.py
(claim B at every R7 failure to n = 40). Data: maxdim_results.jsonl,
maxdim_table_1_90.txt, analysis.txt, b003040.txt (the OEIS b-file used for the
comparison), sweep_31_90.log. Lean: U_C0062.lean (copied from
~/erdos_fc/Prob1000/U_C0062.lean).

## 4. The strongest case that I am wrong, and the check

The claim most likely to be wrong is "unique up to conjugation for all n <= 90" - the
same claim already made for n <= 44, now extended. Ways it could fail: a partition
missed by the enumerator, or a tie hidden by floating point. The enumeration count check
rules out the first at three sample sizes and the generator is the standard rule_asc;
the second is ruled out by the exact recomputation of the top six and a minimum gap
of 4e-4 against 1e-13 float error. The check that would have exposed a wrong maximum is
the b-file comparison, and it did expose one (the hook+1 bug) before the fix. What the
data cannot say is anything about n > 90; the frontier of the literature is 130.

The second exposed claim is conjecture B. R7 looked equally solid at n = 26 and failed
at 27, so B may fail somewhere above 40. I ran the one check available, all partitions
to n = 40 with exact arithmetic, and report it as a conjecture, not a lemma.

## 5. What is not done

No proof of uniqueness, no efficient algorithm with a correctness guarantee, no new
asymptotic bound. The candidate theorem |lambda_1 - l| <= 1 for maximisers is not proved;
the single-move route through R7 is closed and the route through B is open. I did not
reach the Vershik-Pavlov text itself, so I cannot say whether uniqueness to 130 is stated
there in words. Nothing here is a reduction of the source's question to a sharper one.

## 6. Prior art (with what found it)

The session's web-search budget was already exhausted when this task started;
everything below came from curl to OEIS, crossref, episciences and mathnet, and from
the Romik PDF itself.

- OEIS A003040 (highest degree of an irreducible representation of S_n): b-file by
  Vasilii Duzhin to n = 153, terms to 80 from Eric M. Schmidt's exhaustive SageMath run;
  links McKay 1976 (first 75 terms; the 29th was misreported there and corrected 2013).
  Found by fetching oeis.org/A003040 directly.
- OEIS A117500 (the maximal partitions, lexicographically earlier of the conjugate pair;
  notes that a partition and its conjugate give the same degree).
- J. McKay, "The largest degrees of irreducible characters of the symmetric group",
  Math. Comp. 30 (1976) 624-631, doi 10.1090/s0025-5718-1976-0404414-x. Tables to n = 75.
- R. M. Baer and P. Brock, "Natural sorting over permutation spaces", Math. Comp. 22
  (1968) 385-410 (earlier tables); Bivins, Metropolis, Stein, Wells 1954 (Romik fn. 12).
- A. Vershik and D. Pavlov, "Numerical experiments in problems of asymptotic
  representation theory", Zap. Nauchn. Sem. POMI 373 (2009) 77-93; J. Math. Sci. 168
  (2010) 351-361, doi 10.1007/s10958-010-9986-x. Per Duzhin-Smirnov-Maltsev: "the first
  130 Young diagrams with maximum dimensions were found by an exhaustive search", and
  all diagrams differing from a symmetric one by at most one box were found to level 310.
  This is Romik's reference [140].
- N. N. Vassiliev and V. S. Duzhin, "Building irreducible representations of a symmetric
  group S(n) with large and maximum dimensions", Information and Control Systems (2015)
  no. 3, 17-22 (the greedy sequence, the shaking algorithm; the 15th greedy diagram is
  already not maximal).
- V. S. Duzhin and N. N. Vassiliev, "Asymptotic behavior of normalized dimensions of
  standard and strict Young diagrams - growth and oscillations", J. Knot Theory
  Ramifications 25 (2016).
- V. S. Duzhin and A. A. Chudnovskaya, "Search for Young diagrams with large dimensions",
  Computer Tools in Education (2019) no. 4, 33-43.
- V. Duzhin and E. Smirnov-Maltsev, "On Young diagrams of maximum dimension",
  Communications in Mathematics 31 (2023) no. 3, 33-47, doi 10.46298/cm.12641,
  arXiv:2311.15199. Theorem: if lambda differs from its symmetric core by at most one box
  per row and per column, reflecting the below-diagonal extra boxes above the diagonal
  strictly increases the dimension. Conjecture: every maximiser is its symmetric core plus
  boxes on one side of the diagonal, at most one per row (or column). Heuristic A* search
  on a restricted greedy tree to 42,000 boxes. Found via the crossref query
  "maximal dimension Young diagrams symmetric group Duzhin Vassiliev".
- I. Pak, G. Panova, D. Yeliussizov, "On the largest Kronecker and Littlewood-Richardson
  coefficients", arXiv:1804.04693 (cites A003040; asymptotics of the maximal dimension).
- L. Johnston, D. Kenepp, E. Nguyen, D. Paul, A. Schilling et al., "The immersion poset on
  partitions", J. Algebraic Combin. 61 (2025), doi 10.1007/s10801-025-01380-z - the one
  paper citing Duzhin-Smirnov-Maltsev; not read.
- A. M. Vershik and S. V. Kerov 1985 (the asymptotic bounds Romik wants improved).

Net: the campaign's frontier n <= 44 was behind the 2009 literature (130) and the OEIS
table (153). The question itself - a proof of uniqueness, a description, an algorithm
with a guarantee, sharper asymptotics - is open in print as of December 2023.

(This was the integrator's ask: attack C0062, the Romik maximal-dimension Young diagram
problem; extend the exact computation past n <= 40 and look for a uniqueness proof or a
structural theorem.)
