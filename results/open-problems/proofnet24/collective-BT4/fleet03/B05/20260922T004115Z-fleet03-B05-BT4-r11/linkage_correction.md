# BT4 fleet03/B05 — correction to linkage addendum

Run: `fleet03-B05-20260922T0041Z-r11`
Status: `ESSENTIAL_STEP_APPLIED_WITH_CORRECTION`
Parent addendum blob: `f1545c2e4a546d17150bb20bbc59650a29eb2672`

The conclusion of Lemma C in `linkage_addendum.md` is retained, but one sentence in its Menger proof was too quick and must not be used as written.

## Quarantined sentence

The addendum said that 3-vertex-strongness gives three internally vertex-disjoint `w^-`-to-`w^+` paths and then treated the prescribed packed-cycle path

`w^- -> w -> w^+`

as one member of such a triple. Ordinary directed Menger guarantees a triple exists, but does **not** by itself guarantee that an arbitrarily prescribed path belongs to a chosen disjoint triple. That inference is quarantined.

## Correct proof of the two paths avoiding w

The needed conclusion follows more directly from the exact 3-vertex-strong property already proved for the normal form.

Because `D` remains strongly connected after deletion of any set of at most two vertices, the digraph `D-w` is 2-vertex-strong: deleting any further single vertex `z` leaves

`D-{w,z}`

strongly connected.

The packed cycle is oriented and has length at least three, so `w^-` and `w^+` are distinct vertices of `D-w`. By the directed vertex form of Menger's theorem applied **inside `D-w`**, there are two internally vertex-disjoint directed paths

`P_1,P_2 : w^- -> w^+`

in `D-w`. Both therefore avoid `w` automatically.

This proves exactly the path pair required by Lemma C, without prescribing one member of a three-path system.

The rest of the trichotomy proof is unchanged:

- if either `P_i` avoids `A union C`, Lemma B extracts an `R`-internal bypass of a proper `B`-segment containing `w`, and the marked-segment exchange gives `ell>=m+|S|-1`;
- if neither avoids `A union C`, both meet `A union C` internally, and their internal vertex-disjointness is inherited from Menger in `D-w`;
- if `|R|<m-1`, an `R`-internal bypass is impossible because it would require at least `m-1` distinct internal vertices of `R`, so both paths must enter `A union C`.

Thus Lemma C's stated reverse-avoidance / quantified-R-bypass / two-linkage trichotomy remains valid under this corrected proof.

## Sharpening Lemma B's extraction argument

A simpler exact extraction is also available. For any `w^-`-to-`w^+` path `P` avoiding `w` and avoiding `A union C`, let `q` be the **first** vertex of `B` visited by `P` after its start `w^-`. The subpath

`Q: w^- -> ... -> q`

has no internal vertex on `B`, and by the avoidance hypothesis every internal vertex lies in `R`. Since `q!=w`, the forward `B`-segment from `w` through `q^-` is a nonempty proper segment containing `w`; `Q` bypasses it. This gives Lemma B directly and removes any ambiguity about cyclic visit order.

## Surviving quantitative consequence

With the corrected Menger argument, Corollary D also survives: if both `P_1,P_2` avoid `A union C`, the two extracted bypasses have disjoint internal `R` sets, and hence

`|R| >= (ell_1-1)+(ell_2-1)
     >= 2m+s_1+s_2-4
     >= 2m-2.`

Therefore `|R|<m-1` forces **both** alternative paths through other packed cycles, while `|R|<2m-2` forces at least one such packed-cycle linkage.

No target-level closure is claimed. This correction preserves the strengthened segment-exchange result and the linkage trichotomy while removing the only unjustified prescribed-path use.
