# H(2092) d=9 continuation — exact local-barrier computation

Date: 2026-09-17. Direct user-requested research continuation. Source target remains the Hadamard construction problem at order `2092=4*523`; this report is **OPEN/PARTIAL**, not a construction.

## Starting checkpoint

Continued exactly from commit `788f9ebb0329436c20119fdc23e38001f0d7911c`, profile `(17,17,17,35)`, with nonzero K-orbit counts `(28,28,28,27)` and the four explicit orbit sets recorded there. Re-expanding all four length-523 sign sequences and recomputing every periodic autocorrelation from scratch reproduces

`E = sum_{s=1}^{522} R(s)^2 = 20736`,

with 108/522 exact zero residual shifts. K-invariance makes the residual constant on 58 nine-element multiplicative cosets. After dividing each orbit residual by four, the 58-coordinate integer vector is

```
-1 -1 -3 -1 3 -1 0 -2 1 -2 -2 1 0 1 1 0 1 2 0 1 0 -1 -1 1 -1 0 4 -2 2
-1 -1 -3 -1 3 -1 0 -2 1 -2 -2 1 0 1 1 0 1 2 0 1 0 -1 -1 1 -1 0 4 -2 2
```

and its squared norm is exactly `144`. The second half repeats the first because autocorrelation is even under `s -> -s`.

## Exhaustive one-swap neighborhood

For each of the four blocks, I enumerated every legal cardinality-preserving move `selected orbit -> unselected orbit`. There are

- `28*30 = 840` moves in each of blocks 0,1,2;
- `27*31 = 837` moves in block 3;
- total `3357` legal single swaps.

For every move I rebuilt the affected length-523 sign sequence, recomputed all 523 periodic autocorrelations by exact integer dot products, combined with the other three unchanged blocks, and evaluated the full 522-shift squared residual. **No one-swap move has energy below 20736.** Thus the checkpoint is an exact strict/non-improving local minimum for the complete legal one-swap neighborhood. This is a search-landscape theorem only; it is not nonexistence of a d=9 witness.

## Exhaustive simultaneous two-block repair test

For every one of the 3357 single swaps I also stored its exact 58-coordinate residual delta. I then exhaustively compared pairs of swaps acting in **different blocks**, where the autocorrelation deltas add exactly because each affected block is changed once. This covers all simultaneous two-block cardinality-preserving one-orbit exchanges. No such pair lowers the normalized squared residual below 144; in particular, no pair gives zero.

The different-block condition is important: two exchanges inside the same sequence do not have an additive PAF delta because their interaction term changes, so this calculation does not falsely claim to exhaust arbitrary two-exchange changes inside one block.

An additional 2,905 exact random simultaneous three-block exchanges around the same checkpoint found no improvement. This last statement is diagnostic only and is not exhaustive.

## Consequence for route selection

The previous plan proposed two- and three-swap local repair. The exact calculation now shows that **all one-swap moves and all additive cross-block two-swap moves are exhausted without progress**. Continuing ordinary local descent from this checkpoint is therefore low value.

The next construction attack should change representation rather than spend more compute on the same basin. The strongest exact closure gate already in the repository is the split-617 theorem: all 29 paired character equations over `F_617`, together with either surviving d=9 row-sum profile, imply exact integer periodic complementarity. The current E=20736 point satisfies only one of those 29 equations, despite being close in the integer PAF norm. This mismatch strongly suggests optimizing the 29 finite-field equations directly, with the orbit cardinalities imposed, rather than optimizing Euclidean PAF energy.

A second useful route is the surviving `d=6` multiplier tier from the P15 handoff, which has row-sum profiles `(5,5,19,41)` and `(7,19,29,29)` and has not been eliminated by the d=9 local-barrier calculation.

## Scope

- No H(2092) matrix is claimed.
- No d=9 nonexistence theorem is claimed.
- The universal Hadamard conjecture remains open.
- Exact new information: the recorded E=20736 checkpoint has no improving legal single-orbit exchange and no improving simultaneous exchanges in two distinct blocks.
- Existing worker/scheduler state was not modified.
