# A058 GU handoff: character-core reuse has zero tax

For

`F = product_j chi_{R_j}(y) f_j(x_j)`

with arbitrarily reused character cores and disjoint residual blocks, let
`R=triangle_j R_j`.  The supported Fourier sets all contain exactly `R`, so
their upper-set masses factor over the residual blocks.  Consequently

`U(F)=sum_j U(f_j)`, `G(F)=sum_j G(f_j)`, and
`I(F)=|R|+sum_j I(f_j)`.

Every core coordinate has `Delta_i U(F)=0`.  Thus, for every `a>=0` and
`0<=b<1`, a common residual bound `G<=aI+bU` transfers to `F` with the
identical pair.  On any restriction-closed residual class this yields

`U(F)<=a I(F)/(1-b)` and
`H(F)<=(2+2a/(1-b)) I(F)`.

This removes the fresh/disjoint shared-variable hypothesis for character
cores, with no dimension, overlap, reuse, cancellation, bias, or depth loss.
It does not use fixed-sign projection or unsigned indicator payment.

Next: replace deterministic core membership by the two-state posterior law
from one non-character shared coordinate.  Isolate and pay the resulting
joint signed four-channel covariance/KL term once.

Independent review is pending.  Universal GU and full FEI remain open.

