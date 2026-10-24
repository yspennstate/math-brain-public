# Independent audit of the lacunary/direct-tree checkpoint

Date: 2026-10-02. **PASS.** I read the complete separate
[derivation](three_crossing_lacunary_entropy_known_derivation.md),
independently checked its algebra and tree parameters, and opened the
primary Wan–Wright–Wu manuscript. This is an audit of an already covered
class, not a claim of a new FEI theorem for nearby three crossings.

The Hadamard split identity has the correct normalization. The inequality
\(h_2(t)\ge4t(1-t)\), together with
\(r_S(1-r_S)=(1-2q_S)^2/4\), gives
\(\Delta H\le2\sum P_Sh_2(q_S)\le2h_2(\alpha)\).
The real coefficients and signs introduce no missing assumption.

The stated induction for edge isoperimetry is correct: the internal
boundary sum is
\(a\log_2(2^{n-1}/a)+ah_2(q)\), the crossing boundary is at least
\(a(1-2q)\), and \(h_2(q)\ge2q\) on \([0,1/2]\). The physical
normalization is twice undirected edge count divided by \(2^n\).
Every pivot has a minority endpoint, so \(\alpha\le2p\).
The two density regimes in the proof yield \(h_2(\alpha)\le2I(f)\),
including the case \(p\ge1/4\), where isoperimetry gives \(I(f)\ge1\).
Thus \(\Delta H\le4I(f)\) is valid for arbitrary splits.

For a constant child, the support identity \(A=1-|B|\) and fixed sign
of the nonzero values of \(B\) are exact. The nonempty pair mass is
\(2\alpha(1-\alpha)\), so its conditional-entropy contribution is at
most \(2\alpha\). When \(\alpha<1/2\), the empty-pair contribution
is at most
\(2\alpha^2\log_2(1/\alpha)+(\log_2e)\alpha^2<2\alpha\).
The maximization of \(\alpha\log_2(1/\alpha)\) and the linear bound
\(\alpha\le1/2\) justify the displayed constants. For larger density,
the whole conditional entropy is at most \(1\le2\alpha\). The
conclusion \(\Delta H\le8\alpha\) follows.

The induction with \(C_b=8+4b\) is correct. One constant child consumes
no branching budget and is paid by the pivot influence. Two nonconstant
children each have budget at most \(b-1\); the universal split bound is
paid by the current total influence. Induction can formally be taken on
the number of remaining variables, so keeping the same budget at a
one-child node causes no recursion issue.

Strict superincreasing weights give the stated lexicographic order and
disjoint child score ranges. Their label strings concatenate, so the
retained crossing-count identity is exact even with arbitrary values at
attained scores. At a two-nonconstant-child node each child has at least
one crossing, and the chosen child's crossing count decreases by at
least one. This proves branching budget at most \(m-1\). At each fixed
depth, disjoint nonconstant score intervals each contain a distinct
retained crossing, so there are at most \(m\) nodes querying the common
coordinate of that depth. The resulting tree is read-\(m\), as claimed.

I independently opened the full primary
[Wan–Wright–Wu PDF](https://arxiv.org/pdf/1312.3003).
Its Lemma 1.5 bounds entropy by code length times \(\log_2|\Sigma|\)
plus \(2I(f)\); Lemma 1.7 gives code length \(4I(f)+2\operatorname{Cov}[T]\).
The covariance recurrence is exactly the one used in the note.
At a branching node, covariance is at most the average child variance,
which is at most parent variance; at a constant-child node the local
covariance is zero. Induction gives
\(\operatorname{Cov}[T]\le b\operatorname{Var}(f)\), and the displayed
prior-art bound follows from \(\operatorname{Var}(f)\le I(f)\).
This verifies the claimed qualitative historical subsumption by that
primary result. The secondary Shalev improvement is not needed for
either the proof or this subsumption.

The [author script](verify_three_crossing_direct_entropy_heat.py) was
rerun independently; the [report](three_crossing_direct_entropy_heat_checks.json)
records its finite scope. The analytic proof establishes the restricted
statements. It does not prove crossing-count descent when shifted score
copies overlap, or solve ordinary FEI for arbitrary nearby three crossings.
