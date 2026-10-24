Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# R20 idea-before-code — BMO Conjecture 2.6, modulo-3 lifting

This note is written before any new checker for this run. The active exclusive target is Bensmail--Marcille--Orenga, *Pushing Vertices to Make Graphs Irregular* (DMTCS 27:3, 2025), Conjecture 2.6; the stale scheduler title I0100 is not reopened.

The new route uses Section-B moves **#11 DUALIZE, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE**.

Let `Q=D+A` be the signless Laplacian and `d` the degree vector. For a pushing vector `rho`,

` sigma = d + Q rho `.

Work over `F_3`. If a proper 3-colouring `c` satisfies `c-d in im(Q mod 3)`, solve `Q rho = c-d (mod 3)` and take representatives `rho(v) in {0,1,2}`. Then `sigma=c (mod 3)`, hence adjacent integer sums are distinct. Thus the obstruction is the cokernel of `Q mod 3`, not the size of the integer search box.

For a connected **unicyclic** graph this looks completely tractable:

* if the unique cycle is odd, pendant-vertex Schur elimination preserves `det Q`, reducing to the odd cycle, whose signless-Laplacian determinant is `4`; hence `Q` is invertible over `F_3` and every proper 3-colouring lifts;
* if the unique cycle is even, the graph is bipartite and `Q=SLS`. The kernel of `L mod 3` can be described exactly after stripping pendant vertices: on the cycle it consists of affine functions `a+bi`; the slope `b` exists only when the cycle length is divisible by 3. A proper 3-colouring can be obtained from the bipartite 0/1 colouring by recolouring an independent set to colour 2. The independent set can be chosen to kill the one or two cokernel equations explicitly.

If all cases close, this gives the source-strength subclass theorem `P^l(G)<=2` for every connected unicyclic graph, and therefore for every nice pseudoforest componentwise. It would be PARTIAL for Conjecture 2.6 and SELF_CHECK_ONLY pending outside audits. It does not by itself move the fixed all-graphs metric `n_all=8`.

Only after the proof is written cleanly will I add a small exact checker for the finite `C6 + one attached vertex` residue table and a bounded atlas sanity check; the checker is validation, not the research route.