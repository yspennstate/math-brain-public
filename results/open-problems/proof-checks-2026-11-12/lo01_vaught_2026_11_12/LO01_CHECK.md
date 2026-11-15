# Row LO01 (Vaught's conjecture): what the October 2026 counterexample refutes, and what its Lean theorem says

12 Nov 2026. Sources read: arXiv 2610.15217v1 (N. L. Ackerman, C. E. Freer, R. W. Knight, 10 Oct 2026, "A
counterexample to Vaught's conjecture for L_{omega_1,omega}", 26 pages): abstract, introduction, the statements of
Sections 2 and 4, the proof of Theorem 4.36. The public Lean repository named in the paper
(github.com/cameronfreer/vaught-conjecture-counterexample, main branch, last push 10 Nov 2026): the README, the
file stating the main theorem, the file defining its conclusion, and the definitions it uses in the pinned library
(github.com/cameronfreer/infinitary-logic at 004f638). Nothing was built or run here.

## The claim

Theorem 4.36: a sentence of L_{omega_1,omega} in a countable relational language with exactly aleph_1 countable
models up to isomorphism and no perfect set of pairwise non-isomorphic models. This refutes Vaught's conjecture
for L_{omega_1,omega}, which is the topological Vaught conjecture for the group S_infinity (Lopez-Escobar), and
therefore the topological Vaught conjecture as stated for all Polish groups.

It does not touch the original conjecture: a countable complete first-order theory with uncountably many countable
models has a perfect set of them. The paper says so, and the repository's README says "not to the first-order
Vaught conjecture" in its first paragraph. Knight's 2002 manuscript claimed a first-order counterexample and was
never accepted; the present result is the infinitary argument only.

## How the proof is presented

Section 2 defines Knight systems (Ackerman's abstraction of Knight's method) and proves that the base class of a
Knight system has aleph_1 isomorphism types and no perfect set (Theorem 2.25). Section 4 builds a template system
and reduces the main theorem to three propositions (4.32, 4.34, 4.35: amalgamation in the level categories,
reconstruction with limits and boundedness, countably many structures per level). The paper states that these
three propositions are proved in Lean and omits their proofs; "many details are elided, especially near the end",
with a fuller manuscript announced. So the paper alone is not a complete written proof. The claim rests on the
formal proof.

## What the Lean theorem says (read, not built)

    theorem MainTheorem.densitySentence_hasThinAlephOneSpectrum_levels :
        HasThinAlephOneSpectrum densitySentence.{0}

    def HasThinAlephOneSpectrum (phi : L.Sentenceomega) : Prop :=
      Cardinal.mk (Quotient (isoSetoid phi)) = Cardinal.aleph 1 and
        not phi.HasPerfectSetOfPairwiseNonisomorphicNatModels

for L relational with countably many relation symbols. Reading the definitions down to the library:
- formulas: the infinitary connectives iSup and iInf take a family indexed by the natural numbers, so a
  Sentenceomega is a sentence of L_{omega_1,omega};
- isoSetoid phi is the isomorphism relation (existence of a Language.Equiv between the coded structures on N)
  restricted to the codes of models of phi; the first clause says these have exactly aleph_1 classes;
- HasPerfectSetOfPairwiseNonisomorphicNatModels is: some nonempty perfect subset P of the space of codes lies
  inside the models of phi and any two isomorphic points of P are equal. The second clause is its negation.
This is the usual statement of a counterexample, for models with universe N. The README says a companion theorem
(vaughtCounterexample_allCarriers_densitySentence) gives the count over all countable carriers and that the
sentence has no finite models; I read that theorem's name and description, not its statement.

The three files read contain no sorry, admit or axiom declaration. The README lists the axioms of the main theorem
as propext, Classical.choice and Quot.sound, pins Lean v4.36.0-rc1, and says the statement is also checked against
an external reference statement with Comparator and registered as Palomar entry PALOMAR-2026-10-07-000001. The
newest GitHub Actions run on main that I could see (1 Nov 2026, a dependency update) ended in success.

The README is explicit about two limits: the formalization proves the theorem for its own sentence
(baseLanguage.densitySentence) and "does not formalize every claim" of the paper; it does not identify the models
of that sentence with the paper's class of strongly coded templates. The Lean theorem and the paper's Theorem 4.36
therefore agree in what they conclude, not line by line in how the sentence is described.

## What was not checked

- The build. The repository has 765 Lean files; I did not compile it, run its axiom audit, or read the proofs. I
  did not read the definitions of the code space and its topology, or of the set of models of a sentence, beyond
  their use above. A wrong topology on the code space would change the meaning of "perfect".
- The mathematics of Sections 2 to 4 of the paper.
- The Palomar registry entry and the Comparator check.
The arXiv search of 12 Nov (lit/search/s1.xml, phrase "Vaught's conjecture", newest first) shows no comment,
correction or follow-up to the paper. It is one search with one phrase.

## Proposal for the row

Keep the row and state it as the first-order conjecture: every countable complete first-order theory with
uncountably many countable models has a perfect set of pairwise non-isomorphic countable models (equivalently,
continuum many). Beside it: the L_{omega_1,omega} form and the topological Vaught conjecture for S_infinity are
reported refuted (Ackerman, Freer, Knight, Oct 2026) by a proof whose written version is incomplete and whose
Lean statement, read here, says what is claimed. A counterexample for L_{omega_1,omega} does not give a
first-order one: the infinitary sentence is not a first-order theory, and the known reductions go the other way.
