# FEI continuation: directional compression and a shared-control counterexample

20 September 2026. Full FEI: **OPEN before and after this continuation**.

This file is intended for `proofnet24/P03-fei/handoffs/2026-09-20__directional-compression.md`.

The report and executed checker are in the proposed directory `proofnet24/P03-fei/continuations/2026-09-20-directional-compression/`:

- `REPORT.md`: complete proofs, dependencies, scope, and the remaining gap.
- `verify_directional_compression.py`: integer/Fraction checker, Python and NumPy.
- `verification.json`: actual executed output, with the checker SHA-256.

## Mathematical delta

For f=(-1)^P, define V_d(P)={v: deg(D_v P)<=d}, with algebraic degree over F_2. This is a linear subspace and is unchanged by adding a polynomial of degree at most d+1. In a basis adapted to V_d, P=R(z)+Q(y,z), deg Q<=d+1, with no further low-degree directions in R. This algebraic basis change is NOT used to claim influence invariance.

If a nonconstant degree-at-most-d polynomial q approximates the directional derivative phase D_v f with error epsilon, then every physical j with D_j q nonzero satisfies

    min(Inf_j(f),1-Inf_j(f)) >= 2^(-d)-epsilon.

The proof commutes multiplicative derivatives, uses a union bound on the two approximation errors, applies binary-polynomial minimum weight, and bounds translation disagreement by twice the minority-sign mass.

If the directional derivative is instead epsilon-close to a constant sign, every physical pivot in the direction has entropy decrement at most

    min(2, h_2(epsilon)+2 epsilon/ln 2).

At zero error this is the PRE-EXISTING zero-cost signed-symmetry mechanism.

An r-dimensional V_d can be removed by r physical queries. The leaf FEI constant transfers with a universal floor

    kappa_d = min(2^(d+1), 2^d h_2(2^(-d))+2/ln 2).

At d=2, kappa_2=8-3 log_2 3+2/ln 2=6.130502579614458... . This numerical floor was already present as a local payment in NM13-02; the new contribution is the non-coordinate directional certificate and compression. A minimal-dimensional counterexample to a candidate constant >=kappa_2 must have V_2(P)={0}.

## Retired shortcut from this continuation

Local entropy decrements do NOT obey subadditivity when products share a control coordinate, even if all other variable groups are disjoint.

Let u_5(x)=1-2*1_{x=0}, a(t,x)=1 for t=0 and u_5(x) for t=1, and F(t,x,y)=a(t,x)a(t,y). Each factor has six variables; F has eleven. Exact rational logarithm enclosures give

    0.00239650700679 < Delta_t H(F)-2 Delta_t H(a) < 0.00239650700680.

This is not a FEI counterexample. Preserve all valid disjoint-variable tensorization and previously proved quadratic-core splicing results. The early floating-point tests that suggested the shortcut were incomplete and are not a theorem.

## Actual finite verification

65,812 Boolean functions through dimension four; 984,884 nonzero function/direction pairs; 1,724,992 low-degree coordinate assertions; exhaustive quadratic-approximation tests through dimension three; 36 finite compression trees through dimension eight; exact rational-interval verification of the eleven-variable obstruction. See JSON for complete counts. These are checks of the stated lemmas, not exhaustive FEI coverage through dimension eleven. No Lean formalization or independent audit is claimed.

## Full-scope gap

V_2 can be trivial. Approximate constant directions leave epsilon*log(1/epsilon) charges that are not known to be summable by influence. Neither this compression nor arbitrary-core splicing proves the universal erasure estimate sum_i H(S_i|S_-i)<=K I with finite universal K. Do not state or imply full FEI closure.

## Delivery and priority

This is a conversation-generated, pending-delivery package. No remote commit or scheduled-worker receipt is claimed. The patch adds only these new files and does not alter existing entrypoints, schedules, ownership, or atlas metrics. Verify it before applying it to a current checkout. Publication priority is unverified.
