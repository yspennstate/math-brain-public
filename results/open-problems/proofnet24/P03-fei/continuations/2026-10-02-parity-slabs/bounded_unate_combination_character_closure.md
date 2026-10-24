# Conditional character closure for Boolean combinations of finitely many unate gates

2 October 2026. Complete elementary conditional lemma. This supplies no
new ordinary FEI theorem for the underlying gate combination. Its ordinary
FEI premise is explicit, not inferred from bounded gate count.

On the uniform cube define J(g)=Σ_i min(I_i(g),1−I_i(g)). It is the
minimum total physical influence over all output character modulations,
because I_i(χ_Tg) equals I_i(g) outside T and 1−I_i(g) inside T. Entropy
is unchanged by character modulation.

Let F be a restriction-closed Boolean class with ordinary FEI constant
C. Suppose every member g is a Boolean combination of at most m unate
Boolean functions on the same input variables:

g(x)=A(h_1(x),...,h_s(x)),  s≤m,

where A is an arbitrary Boolean rule and the coordinate orientations of
different h_r need not agree. The functions may share every input. The
following result is conditional only on this explicit class description
and the ordinary FEI premise:

H(g)≤[C+4(4m²−1)]J(g), m≥1.

Hence every χ_Tg satisfies ordinary FEI with the displayed constant,
uniformly over T and dimension.

For the proof, if a cube edge changes g, at least one of h_1,...,h_s
changes. The union bound gives I_i(g)≤Σ_r I_i(h_r). For a unate Boolean
h_r the absolute singleton Fourier coefficient is I_i(h_r), regardless
of its coordinate orientation. Parseval gives

Σ_i I_i(h_r)²≤Var(h_r)≤1.

Cauchy–Schwarz over r then gives

Σ_i I_i(g)²≤sΣ_rΣ_i I_i(h_r)²≤s²≤m².

Each I_i(g)>1/2 contributes strictly more than 1/4, so there are
b<4m² such coordinates, or b≤4m²−1. Let U be precisely that set,
and put f=χ_Ug. Then I(f)=J(g) and H(f)=H(g).

The fully proved bounded-coordinate gluing principle in
[parity_modulated_slabs_center_proof.md](parity_modulated_slabs_center_proof.md)
states that for any Boolean f and any fixed b-coordinate set U,

H(f)≤average H(f restricted on U)+4b I(f).

Its proof uses the universal exact pair inequality Δ_iH≤2h₂(I_i),
minority influence I_i≤2p, and the self-contained edge-isoperimetric
bound I≥2p log₂(1/p), which together give Δ_iH≤4I(f). At every
restriction depth the average total influence only decreases, so the
entropy split telescopes with cost 4bI(f). No local bound by I_i or
min(I_i,1−I_i) is assumed.

After assigning U, the character is a constant output sign and the
restricted g belongs to F. Ordinary FEI on those restrictions gives

average H(f restricted on U)
=average H(g restricted on U)
≤C average I(g restricted on U)
=C average I(f restricted on U)
≤C I(f).

This proves H(g)=H(f)≤(C+4b)I(f) and the displayed result. Empty
centering sets, constants and J=0 need no division. The m=0 class
contains only constants; its character modulations have zero entropy.

Examples of unate gates include arbitrary signed-weight halfspaces.
Therefore any already proved restriction-closed ordinary-FEI subclass
of Boolean combinations of at most m halfspaces has the stated
character closure. This does not prove ordinary FEI for arbitrary
intersections or Boolean combinations of halfspaces, whether parallel
or not. The campaign's ordinary slab and wide-gap union theorems are
valid applications because their FEI premises have separate full proofs.

Standard Chow identities, Parseval and character shifts are prior facts.
The generic closure is derived here from those identities and the
bounded-coordinate gluing lemma. Historical novelty and external
specialist review remain unverified. No unrestricted Boolean FEI,
arbitrary polynomial-threshold, nonuniform-input, or shared-circuit
theorem is asserted.
