# B05 / A023 — dense nullity-two retained credit

## Outcome

**AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW.** The coordinate-alignment
hypothesis has been removed at kernel width two. For every

\[
P(x,y)=(-1)^{x^TMy+\mathrm{affine}}D(y),
\qquad \operatorname{rank}M=m-2,
\]

with arbitrary Boolean coherent core \(D\) and arbitrary physical
orientation of the two-dimensional kernel,

\[
\boxed{H(P)\le2I(P),\qquad U(P)\le2I(P).}
\]

Every finite adaptive/pruned restriction tree on the shield variables and
every common disjoint Boolean terminal core \(h\) therefore satisfies

\[
\boxed{U(Ph)-\sum_\ell w_\ell U(P_\ell h)\le2I(P).}
\]

The constant is independent of dimension, physical kernel orientation, core
bias and spectrum, defect count, overlap, address count, tree depth, reveal
order, and dyadic leaf probability. Constant two is sharp. Full FEI remains
**OPEN**.

## Packet and bounded objective

- Stream/packet: B05 / A023 (amortized rarity budget).
- Attempt: `B05-A023-DENSE-NULLITY-TWO-10`.
- Stable gap: `B05_RARE_REFUNDS`.
- Objective: take the newest aligned-width theorem's next unpaid case and
  either compare dense two-bit fiber influence to physical root influence or
  certify that a new retained interaction term is necessary.

The comparison succeeds exactly; no additional interaction credit is needed
at width two.

## Mathematical delta

The preceding theorem handled arbitrary coordinate-aligned width \(t\), with
constant \(K_t=\max\{2,C_t\}\), and certified \(t\le4\). It explicitly left
dense physical orientation open already at width two because influence is
not invariant under a general linear basis change.

This run covers every rank-\((m-2)\) matrix in the original physical basis.
It strictly joins the prior arbitrary-orientation nullity-one theorem to the
aligned-nullity-two theorem and removes the last orientation hypothesis at
width two. The proof is analytic for all dimensions; the finite checker is
only a normalization diagnostic.

## Proof mechanism

Let \(K=\ker M\). Orthogonality in \(x\) decomposes the squared Fourier law
into a uniform choice of a coset of \(K\), a uniform extension of a character
of \(K\), and the two-bit Fourier law of the restricted core. Therefore

\[
H(P)=2r+\mathbb E_C H(D_C),\qquad r=m-2.
\]

Let \(z\) be the number of zero physical columns of \(M\), equivalently the
number of standard coordinate vectors lying in \(K\), and let
\(A=\sum_{j:\,\mathrm{col}_jM=0}\mathrm{Inf}_j(D)\). Since \(\dim K=2\),
\(z=0,1,2\). Exact classification of two-bit Boolean functions gives

\[
\mathbb E_C H(D_C)\le2-z+2A.
\]

Meanwhile nonzero physical rows and columns make their derivatives balanced:

\[
I_x(P)\ge r/2,
\qquad I_y(P)=(m-z)/2+A.
\]

Thus \(2I(P)\ge2r+2-z+2A\ge H(P)\). The complete signed tree charge is root
\(U\) minus nonnegative terminal \(U\); a common disjoint factor cancels by
tensor additivity. This pays the whole hierarchy once from the root reservoir
without asserting nodewise positivity.

The full proof, including zero Fourier atoms and all three orientation cases,
is in `PROOF.md`.

## Verification

`CHECK_DENSE_NULLITY_TWO.py` uses exact integer Walsh transforms and rational
influences. It verifies the three analytic two-bit fiber inequalities on all
16 truth tables; exhausts 19,760 rank-\((m-2)\) matrix/core pairs for
\(m\le3\), \(s\le3\); and tests 1,000 deterministic larger instances through
\(m=7\). For every instance it reconstructs the full physical truth table,
checks

\[
H(P)=2r+\mathbb E_C H(D_C),\qquad H(P)\le2I(P),
\]

and includes dense, one-axis-aligned, and fully aligned kernels. The largest
observed \(H/I\) was exactly 2. The analytic proof, not enumeration,
establishes the theorem.

## Scope and obstruction checks

- **Rare restrictions:** arbitrary finite pruning and dyadic leaf rarity are
  included through the complete signed endpoint telescope.
- **Shared coherent cores:** \(D\) is arbitrary and shares all \(y\)-variables
  with the bilinear shield.
- **Dense orientation:** handled in the original physical coordinates; no
  influence-preserving basis change is assumed.
- **Point defects / sparse surgery:** included as choices of \(D\), but no
  pointwise selector-only payment is claimed.
- **Near tensors:** do not contradict the fixed width-two theorem. The prior
  rank-one tensor embedding still shows that uniform control of all aligned
  widths is full-FEI-hard.
- **Tree closure:** the endpoint payment does not require restricted
  descendants to retain nullity two; no stronger restriction-closed claim is
  made.

## Exact remaining obstacle

`B05_RARE_REFUNDS/KERNEL_WIDTH_GE_3` remains open. At kernel width three,
fiber spectra are no longer restricted to affine or flat laws. The aligned
case reduces to the ordinary three-bit FEI constant, while an all-width
uniform extension is already full-FEI-hard. The next useful move is not
another finite-width maximum: derive a signed interaction credit between the
shield and a genuinely nonflat three-bit fiber that vanishes on the disjoint
tensor embedding but remains positive for changing coherent fibers. Such a
credit must be single-use under the complete tree telescope.

## Sources and status

- Owner control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B05 assignment blob `05447e6d999437bb82a266b427bd76a4b37266b6`.
- Nullity-one predecessor receipt
  `762c425a4d56287e2dfda853cc581fa2e9e0a457`, proof blob
  `d3b79b8a3e4c485b9f693ec22be4e9210b637738`.
- Aligned-width predecessor receipt
  `09fe8877f0362b6b46361d2e5acbcb10f8dc5dd9`, proof blob
  `484097d7b7634b0fb644d38aee093cdd7d096fe8`.

The present theorem was rederived directly and does not depend on the
computer-assisted width-three/four constants. It awaits A087/A094 or B19
review. No external novelty claim, packet completion, native Brain ingestion,
or full-FEI settlement is made.

