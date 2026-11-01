# P0104 sharp-boundary result and adversarial audit

The deliverable is a sharp finite-distance support criterion and a concrete
obstruction to variance estimates uniform over edge laws. It does not resolve
the fixed-law fluctuation-exponent target. Current openness and novelty are
UNKNOWN. The precise recovered source scope and versioned locators are in
SOURCE_STATUS.json.

C001 and C002 were saved in INDEPENDENT_OBSTRUCTION.md before I inspected
w366's proofs. They are derived directly in the ordinary undirected lattice
model, in all d>=2. For weights in [a,b], a>0, every nonstraight route from
0 to n e_1 costs at least (n+2)a, whereas the straight route costs at most
nb. Thus n(b-a)<=2a forces the exact straight-path identity. Essential
support endpoints and one edge-disjoint dogleg show the threshold is sharp
for iid laws. The complete proof, including equality and positivity, is
in the independent artifact.

For iid Uniform[1,1+epsilon] weights, the identity gives exactly
Var(T(0,n e_1))=n epsilon^2/12 for n epsilon<=2. Independence applies to
the deterministic straight-path edges. Setting epsilon=1/n disproves a
bound C Var(tau) n^theta with theta<1 if both its prefactor and onset
are required to be common to every law. This changes the law with n;
it makes no assertion about the asymptotic exponent for any fixed law.

## C003: necessary tradeoff between the constant and starting scale

This corollary was derived after peer-proof inspection; its proof relies on
the previously saved C001/C002, rather than a new geometric estimate.

Fix d>=2, 0<epsilon<=1, theta<1 and the iid Uniform[1,1+epsilon] law.
Put K=floor(2/epsilon). Suppose C>0 and an integer N>=1 satisfy

    Var(T(0,n e_1)) <= C Var(tau_e) n^theta for every integer n>=N.

Then either N>K, or C>=K^(1-theta). Indeed, if N<=K, apply the exact
variance identity at n=K, divide by the positive one-edge variance,
and obtain K<=C K^theta. This proves the disjunction. It is a necessary
condition; existence or sufficiency of such a bound is not asserted.

For theta=2/3, a bound beginning within this window must have
C>=floor(2/epsilon)^(1/3). With a common finite C and small epsilon,
its onset must instead lie beyond floor(2/epsilon). This quantifies the
missing uniformity premise while preserving the possibility of a
law-dependent asymptotic theorem. Independent referee w368 is pending.

## Paired proof audit

w366-C1 and C2 pass the fixed-endpoint audit in AUDIT_W366_C1.md. Four
deterministic, edge-disjoint paths justify the multiplication of path-sum
tail probabilities. Their shared vertices cause no dependence. The moment
criterion and critical Pareto endpoint are valid; their constants grow
with n and do not supply a KPZ exponent.

After my independent artifact was saved, I inspected w366's newly added
C3 and C4. They agree with C001/C002 restricted to d=2 and a=1. Both
receive KEEP as special cases. The variance normalization is essential
to C4, and a law-dependent onset escapes the refuted universal bound.
I do not certify the provenance or independence of the peer's later
derivation. Referee admission remains separate from this audit.

## Checks and limits

Command: python -X utf8 verify_boundaries.py. VERIFICATION.json records
2,336 exact finite-rectangle configurations. At/below the threshold,
all 1,168 checked configurations obey the identity. Above it, the
three cases produce 1, 2 and 4 detour counterexamples respectively.
Six exact continuous-uniform moment calculations agree with the
variance formula. Four choices of n check all six pairs of the peer's
fixed paths. The run used 0.03125 CPU seconds and about 0.034 wall seconds.
These supplement the written full-lattice proof; they do not replace it.

STUCK: the old Codex ledger worktree referenced by the C-intake README
is absent, and the C-intake has C-prefixed records rather than P0104.
I switched to an id-filtered export read and two exact live-store node
lookups. Those recovered the target, previous logarithmic obstruction,
and the primary source's Questions 13/15. No original-ledger byte check
or exhaustive owner-retirement check is claimed.

The hardest unresolved piece is unrestricted detour optimization as
n tends to infinity for one fixed admissible law beyond the finite
window. No bound in this packet establishes a polynomial variance
exponent, its positivity, or the planar value 1/3. No formal checker
was run. New claims remain author-derived special cases pending w368.

NEXT: w368 checks C001-C003, resolves duplicate peer cards, and admits
only the reviewed special-case material and supporting relations.
