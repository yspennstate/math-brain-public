# Horn 2 reduces to one definitional question — with the conditionality stated first

Author: main session c53c1d50, 2026-08-19 ~05:2x. Executes the step named in `leak_is_boundary_multiplicity.md` §4: *can a residual-class block have boundary multiplicity `D ≥ log n` while satisfying its other defining conditions?* **Read the status line before the argument.**

> **STATUS. This is a conditional chain, not a theorem. Its last link is a question about a definition that lives in the project tree we cannot read — the same absent layer that has already blocked G2, the tag-(25) derivation, and the crosspolytope embedding. Nothing below closes horn 2, and nothing below bears on the conjecture, which is OPEN. What it does is replace "prove absorption for the residual class" with one named yes/no question about whether a specific decomposition is admissible.**

## 1. Horn 2 is exactly the singleton-private-support regime

The dossier's batching builds the two-shadow graph `Γ` on private coordinates, with an edge `ij` when some row's private support contains both; and it states explicitly that **singleton private supports create no two-shadow edges** (S9 setup). So a block whose rows all have singleton private support has `ν(Γ) = 0` and `κ = 0`: **bounded congestion, i.e. horn 2.**

That is not a coincidence of my framing — it is the same fact that makes §2 available: after the packet's own compression every row has at most one private coordinate, which is precisely singleton private support. **Horn 2 and the boundary-multiplicity count are the same regime seen twice.**

## 2. High boundary multiplicity is a large star

`D ≥ log n` says: some private coordinate `j` carries at least `log n` rows, with distinct boundary partners. In the private-incidence structure that *is* a star of size `D` centred at `j` — rows `u_a(W) + λ_a x_j`, differing only in their boundary parts. The dossier's own vocabulary for this object is "ordinary star core", and its class definition excludes blocks with an `o(log n)` one (S6 p.123) — i.e. the class tolerates large stars and excludes small ones, exactly matching §2's threshold from the other side.

## 3. But large stars dissolve

This campaign already computed what a large star costs when decomposed by arms (`mu_on_dense_stars.md` addendum 2): root the homogenizer, make each arm a child, and **every child satisfies the full rooted target — both clauses — at exactly `1/β = 2.409`, with zero leak and no ancestor payment, for every `k`.** Size is irrelevant to that computation; a star of `log n` arms decomposes exactly as a star of 3 arms does.

So the object that high `D` forces into the block is precisely the object the campaign has shown to be harmless *under the right decomposition*.

## 4. The chain, and the single link that is missing

1. Horn 2 ⟹ bounded congestion ⟹ (§1) singleton private supports.
2. (§2 of `leak_is_boundary_multiplicity.md`) `λ = O(D·L)`.
3. `D ≥ log n` ⟹ (§2 here) a star core of size ≥ log n inside the block.
4. (§3) that star decomposes by arms into blocks each meeting the rooted target at `1/β`.
5. The residual class is defined to be what survives **every admissible Gale basis exchange** — so a block that dissolves under an *admissible* decomposition is not a class member.
6. Hence class members on horn 2 would have `D = o(log n)`, giving `λ = o(log n)·L`, which closes horn 2 under W1's scoped coefficient relief.

**The missing link is step 5: is the arm decomposition admissible?** "Admissible Gale basis exchange" is inherited from the earlier project tree and is never defined in the 200 pages (the rank lane searched for the neighbouring undefined term "useful junction basis" and found no definition either; I searched the Gale vocabulary in full at 01:0x and found only usages). Until that word has a meaning we can check, step 5 is an assumption wearing the clothes of a definition.

**And a second, smaller gap I will not paper over:** step 3 gives a star *inside* the block, but a class block may carry a star *plus* other structure, and the arm decomposition of the star may not extend to a decomposition of the whole block. My star computation is for a pure star. So even with step 5 granted, step 4 needs "the star's arm decomposition lifts to the ambient block" — true in the two-level cases I have computed, unverified in general.

## 5. What this is worth

Even fully hedged, the shape is useful:

- **Horn 1 and horn 2 are now qualitatively different.** Horn 1 carries the rank lane's *forced* `Θ(log n)` deficit — a proved obstruction (conditional on the dossier's class assertion) saying the packet's own tool cannot close it, with Target R-C naming what would. Horn 2 carries no such obstruction: it reduces to whether a specific, explicitly-computed decomposition counts as admissible.
- **It converts a research problem into a definitional one.** "Prove absorption for dense connector-incoherent blocks" becomes "does the arm decomposition count as an admissible Gale exchange, and does it lift?" Two yes/no questions, both answerable by someone holding the missing tree — and worth asking the owner whether that tree exists anywhere he knows of, since three campaign questions now terminate there.
- **It predicts something checkable without the tree:** if the arm decomposition is admissible, then no class member has high boundary multiplicity, so *every* class member on horn 2 has `D = o(log n)` — and any explicitly constructed class member should therefore exhibit low `D`. Since the campaign has never possessed a class member, this is a property to test the moment one appears, and a way to falsify the chain if one appears with high `D`.

**Nothing here proves anything about the residual class, whose inhabitation remains unknown, or about the conjecture, which remains open. The block-internal certificate for dense connector-incoherent cores — horn 1's content — is untouched.**
