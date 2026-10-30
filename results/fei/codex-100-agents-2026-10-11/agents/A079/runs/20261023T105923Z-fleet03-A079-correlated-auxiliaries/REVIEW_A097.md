# Independent scoped review of A097's two-bin phase theorem

Source: A097 run20261023T062140Z, DERIVATION sections1--4.
Claim A097-NONEMPTY-PHASE-BIN-FUNDED-TRANSFER@1, statement SHA256
f8ee94db650f099b036f174a5e9d21989eee7c6110efd02901221b86b631a6a8.
Verdict: HOLDS AT STATED SCOPE, without repair; no universal source price.

Reconstruction: actual child means m+/-d give vacuum half-difference
2d B_U(sigma*A_U+m B_U). In each nonempty bin the half-difference is
2 B_U^2 sum_bin(u_T v_T). Squaring, summing and using the SAME inherited
comparison law for BOTH children yields the parallelogram lower bound.
Pinsker in bits then gives average coarse KL>=2x/ln2. Completion of the
square gives sum B^2(sigma A+mB)^2>=C-D^2/E4=Gamma. Block calibration
is normalized and reduces CE by precisely that coarse KL. Each prescribed
tail mixture costs at most x/ln2, so the complete physical transaction
retains x/ln2 beyond occupancy KL. All zero sectors and empty true bins
use explicit zero-mass conventions; no division is needed there.

Merging two same-sign sums increases their squared sum; splitting a
mixed-sign block increases it. Thus the two sign bins maximize squared
bin energy. With d=0, Booleanity sum u_T v_T=0 gives the stated nonempty
sign sums. Positive energy is equivalent to a nonisospectral query when
beta>0. Parity3 realizes the zero-energy boundary. Nothing here implies
energy>=constant*influence or an initially paid arbitrary Boolean source.

Our independent implementation uses A079's direct character-sum arithmetic,
not A097's author code. It recomputes beta=3/8,E4=21/512,Gamma=9/3584,
both full prescribed terminal references and their physical erasure/CE
increments on the frozen finite domain. It checks the exact rational
consequence increment<=-x; the stronger x/ln2 constant follows from the
displayed analytic Pinsker proof, not a floating comparison. Results are
in out/review_A097.json. The new ghost-singleton theorem is a separate
author extension, not part of this independent acceptance or a repair.
