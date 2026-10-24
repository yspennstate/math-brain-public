# A094 second-chain challenge

## Frozen target

Audit `B05_A023_POSITIVE_DEFECT_RETAINED_v1` from original commit
`ed704e08ace97f8c295992ee560edfbe4d89a07a`, separately checking:

1. the exact scalar margin near the unique minimum of `R'`;
2. normalization of the point-defect spectrum for every rank;
3. selector influence and mean transport under arbitrary rank changes;
4. disjoint physical-input accounting in the tree endpoint; and
5. whether the result meets A023's stronger first-revelation credit standard.

## Hard regimes selected independently

- minimum scalar-slope window `t in (0.49,0.51)`;
- ranks `r=2,3,4`, where the point-block ratio is largest;
- nonstationary sequences with ranks through 128;
- activation probabilities tending to zero;
- arbitrary Boolean bases through three inputs;
- adaptive/pruned reveal orders; and
- nonconstant common terminal factors.

## Result

The three formal mathematical claims survive.  The exact slope margin is
`379/33600`; no floating sign decision is used.  Direct Walsh reconstruction
agrees with every recurrence and physical influence term.

The stronger interpretation as a first-revelation rarity-credit ownership
theorem does not follow.  The proof uses the nonnegativity of terminal `U` and
therefore remains an endpoint telescope.  Changing/shared terminal cores and
descendant-specific rarity ledgers are still open.
