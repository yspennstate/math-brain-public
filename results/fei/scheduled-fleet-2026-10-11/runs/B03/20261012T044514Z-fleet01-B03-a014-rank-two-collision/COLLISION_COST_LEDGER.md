# Exact cost ledger

Family: `F_t(c,b,x)=s_t(c)M(b,x)`, where `c` has `t` bits, `b` is one bit,
and `M` selects between the two orthogonal majority variants in
`RANK_TWO_COLLISION_THEOREM.tex`.

| Cost | Exact value or bound | Payment |
|---|---:|---|
| Literal worst-case branch read | `2^(t+1)` | Obsolete raw parameter; diverges |
| Fractional data-coordinate congestion | `1` | Every branch has weight `2^(-(t+1))` |
| Spectral branch rank | `2` | Exact Boolean compatibility lemma |
| Rank/type name | `1` bit | The physical selector `b` |
| Sign-label spectrum | `H(s_t)` | `H(s_t)<4 I(s_t)` |
| Fixed colliding core spectrum | `H(M)=2` bits | `I(M)=2` |
| Ordered sign-controller roots | `2-2^(1-t)<2` | First `+1` stopping rule |
| Type-controller roots | `1` | Query `b` once |
| Total controller roots | `<3` | No root is reused |
| Rarity | exceptional sign probability `2^(-t)` | retained in `H(s_t)` and `I(s_t)=t2^(1-t)` |
| Subset-choice cost | `0` beyond the four explicit core atoms | exact spectrum |
| Reference normalizer | `2` bits | already equals `H(M)` |

The two cores have identical Fourier support, not disjoint support. Their
coefficient signs cancel into two atoms without `b` and two atoms with `b`.
This exact coherent sum replaces a worst-read or `k`-fold Cauchy--Schwarz
charge.

The class extension is from rank-one signed copies to rank-two branches.
The uniform constant is still four for all `t`; it does not depend on read,
address count, spectral overlap, or the vanishing rarity `2^(-t)`.

The unproved boundary is an arbitrary joint pair of Boolean address
controllers `(sigma,tau)` in the rank-two normal form. A marginal bound on
either controller is insufficient unless their joint posterior/collision
cost is also paid.
