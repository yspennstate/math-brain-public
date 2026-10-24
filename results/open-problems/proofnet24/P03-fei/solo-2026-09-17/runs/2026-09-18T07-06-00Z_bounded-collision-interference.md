# Solo FEI run: bounded coherent interference

Timestamp: 2026-09-18T07:06:00Z  
Status: full FEI remains **OPEN**. No subagents, delegated workers, other
models, or independent audits were used. Runtime model/reasoning metadata:
**UNVERIFIED**.

## Result proved in this run

I extended the preceding constant-four theorem from distinct data-parity
labels to bounded coherent collisions.

Let selector space be partitioned into subcubes `C_j`. On `C_j`, let

    f(x,y)=s_j chi_(T_j)(x) chi_(D_j)(y).

The `D_j` may repeat. Assume every cross-cell selector edge makes the two
endpoint data fibers disagree on at least half of the data cube. For a fixed
data label `A`, let `q_A` be the actual conditional selector squared-Fourier
law after coherently adding all cells with label `A`, and let `m_A` be the
incoherent mixture of those cell laws. Define

    Lambda=max_(A,S:m_A(S)>0) q_A(S)/m_A(S).

Then

    H(f)<=2 Lambda H(J)-(Lambda-1)H(D_J)
        <=2 Lambda H(J)
        <=4 Lambda I_x(f).                              (1)

If every data label occurs on at most `R` cells, Cauchy--Schwarz gives
`Lambda<=R`, so `H(f)<=4R I_x(f)`.

## Proof mechanism

The new scalar lemma is: for probability laws `q,m`, pointwise domination
`q<=Lambda m` implies

    H(q)<=Lambda H(m).                                  (2)

Writing `theta=q/(Lambda m)`, the surplus term is the expectation of the
concave function `theta log(1/(Lambda theta))`; Jensen makes it nonpositive
because `E_m theta=1/Lambda`.

For each repeated label, Cauchy--Schwarz gives `q_A<=r_A m_A`, while the
entropy of `m_A` is bounded by the entropy of its latent cell label plus the
exact codimension entropy of each subcube spectrum. Summing groups proves the
first two inequalities in (1). Subcube edge isoperimetry gives
`H(J)<=sum_i eta_i`; boundary separation gives `I_x>=sum_i eta_i/2`, proving
the last inequality.

Every theorem-sized assertion is proved in
`BOUNDED_COLLISION_PARITY_MULTIPLEXERS_2026-09-18.md`.

## Exact self-check

`check_bounded_collision_parity_multiplexers.py` passed two repeated-label
examples using exact rational Walsh arithmetic and 160-bit outward rational
logarithm intervals.

* Four equal subcube cells with one diagonally repeated label: `R=2`, but
  exact `Lambda=1`, `H(f)=4`, `I_x=2`.
* Eight point cells with an antipodal repeated label: `R=2`, exact
  `Lambda=2`, `H(f)=11/2`, `I_x=3/2`.

The generated certificate is
`bounded_collision_parity_multiplexer_certificate.json`. These checks are not
an independent audit and are not the proof of the universal theorem.

## What this does not prove

This does not establish a universal bound on `Lambda`. Point cells with a
common data label represent an arbitrary Boolean selector function, so the
unbounded-collision class already contains full FEI. Boundary separation is
also essential: otherwise an artificial cell boundary can have positive
description entropy and zero influence. No canonical decomposition of a
general Boolean function into bounded-interference, boundary-separated
parity cells is known here.

Thus the exact remaining full-scope gap is still a dimension-free proof of

    K(f)<=C I(f),

or equivalently the erasure bound `B(f)<=C'I(f)`. The present theorem supplies
a rigorous nonreuse mechanism for one structured overlapping class, not that
general inequality.

## Literature query

Keyword searches on 2026-09-18 located the O'Donnell--Tan composition theorem
(`arXiv:1304.1347`), O'Donnell--Wright--Zhou on read-once decision trees,
Shalev on read-k decision trees (`arXiv:1806.03646`), Han's influence-profile
bound (`arXiv:2312.08271`), and the recent restriction-induction work
(`arXiv:2606.00246`). No retrieved source stated (1). This was not a complete
literature review; novelty is **UNVERIFIED**.

## Measured execution

The first recorded shell timestamp was 2026-09-18T07:01:24Z. The theorem,
proof note, exact checker, certificate, literature query and this report were
completed by the report checkpoint at 2026-09-18T07:06:19Z: 4 minutes 55
seconds of measured wall-clock execution. This does not imply continuous work
between scheduled runs and is not claimed as an independent review.
