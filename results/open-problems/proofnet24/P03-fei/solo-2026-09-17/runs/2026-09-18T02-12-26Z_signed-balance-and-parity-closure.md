# Solo FEI continuation: signed balance and parity-query closure

## Outcome

Full Friedgut--Kalai Fourier entropy--influence remains **OPEN**. This continuation proves three structural facts and uses them to eliminate two tempting shortcuts:

1. Booleanity gives exact equality of same-sign and opposite-sign absolute coefficient overlap in every nonzero spectral direction.
2. That equality is not local in coefficient-magnitude scale, and no fixed invertible linear change of spectral coordinates removes the logarithmic loss.
3. Conditioning on spectral parity exits the Boolean class into partial Boolean functions; this is the exact branch-closure class, and a universal normalized FEI inequality on it would already imply full FEI.

No finite universal bound for B/I, K/I or L/I is obtained. The results narrow what a successful signed-cancellation or parity-coding proof must do. Novelty relative to the full literature is UNVERIFIED.

All work in this continuation was done by the primary assistant. Subagents, delegated tasks, other-model calls, commissioned audits and outside contacts: zero. Actual model and reasoning-level metadata are not exposed and are therefore UNVERIFIED.

The current master head freshly read at the start was `18525e9d4da9621581107b3cdb75ded2fe5fb39e`. The newest prior solo checkpoint was `4219667a916658c99c28a9805a2eb1a8d5358223`. The root exclusions, P03 handoff, README, NEXT_STEPS, erasure reduction, newest reports and exact certificates were read before continuing. The original P03 finite-dimensional metric 6 is retained only as a prior reported fact; its exhausted cell enumeration was not resumed.

## 1. Exact sign-overlap balance

Write a_S=fhat(S). Booleanity is the signed convolution identity

    sum_S a_S a_(S xor U)=1{U=empty}.

For nonempty U, grouping the sum into unordered pairs {S,S xor U} proves

    sum_pairs a_S a_(S xor U)=0.

Separating positive and negative products therefore gives the exact identity

    sum_same-sign |a_S a_(S xor U)|
      =sum_opposite-sign |a_S a_(S xor U)|.             (1)

This holds separately for every nonzero U, not merely after summing coordinate directions.

The logarithmic edge cost has a different weight. If r=a^2>=s=b^2 and t=ln(|a|/|b|), then

    s log_2(r/s)=(2/ln 2)|ab| t exp(-t).                (2)

Identity (1) controls the overlap with weight one. It supplies no cancellation after inserting the scale weight t exp(-t).

## 2. An exact scale-local obstruction

For N=2^n, let f(0)=-1 and f(x)=+1 elsewhere. Its Fourier coefficients are

    a_empty=(N-2)/N,      a_S=-2/N for S nonempty.      (3)

In any coordinate direction i, the unique edge from the empty coefficient has opposite signs and absolute product 2(N-2)/N^2. The other N/2-1 edges are same-sign and each have product 4/N^2, so their total is also 2(N-2)/N^2. Thus (1) is perfectly balanced.

All same-sign edges have equal squared endpoint masses and contribute zero logarithmic cost. The opposite-sign edge contributes all of it:

    K_i=[8/N^2] log_2[(N-2)/2].                         (4)

Therefore exact unweighted cancellation cannot simply be asserted inside magnitude-ratio bands. A new quantitative transport argument would have to move cancellation credit between scales and prove that the same influence is not reused.

This is not a counterexample to FEI or to K<=C I. Here

    I=2n/N,      K/I=4 log_2[(N-2)/2]/N -> 0.

It is only a sharp counterexample to the proposed proof shortcut.

## 3. Every fixed linear basis still loses a logarithm

For nonzero U define the generalized influence

    alpha_U=Pr_x[f(x)!=f(x xor U)]
           =sum_S p_S 1{|S intersect U| is odd}.        (5)

If U_1,...,U_k span F_2^n, the parity measurements Y_j=|X intersect U_j| mod 2 determine the spectral subset X. Hence

    H(f)<=sum_j h_2(alpha_(U_j)).                        (6)

This includes every invertible linear reparameterization and every redundant fixed parity-query family.

For the one-point defect, every nonzero translation changes exactly two physical inputs, so alpha_U=2/N for all U!=0. Every spanning family has k>=n and (6) costs at least n h_2(2/N). Since I=2n/N, the ratio of this cost to I is

    h_2(2/N)/(2/N) -> n-1+1/ln 2,                       (7)

which is unbounded. In contrast, direct evaluation gives H/I->4. Thus the logarithmic loss is caused by fixed-marginal subadditivity, not by the actual Fourier entropy on this Boolean family.

## 4. Exact closure of conditioned parity queries

For one query U, define

    A=(f+T_U f)/2,      B=(f-T_U f)/2.

These functions take values in {0,+1,-1}, have disjoint supports, and their Fourier transforms are the even- and odd-parity projections of fhat. Their squared L2 norms are 1-alpha_U and alpha_U. Consequently the conditional spectral laws after the parity answer are the normalized squared Fourier laws of A and B.

This partial-Boolean class is exact, not an overly broad relaxation. Given any g:{+1,-1}^m->{0,+1,-1}, add w and define a Boolean F by using equal values g(x) on the w-pair when g(x) is nonzero and opposite values +1,-1 when g(x)=0. Then

    [F(x,w)+F(x,-w)]/2=g(x)

for both w. Every partial Boolean function therefore occurs as one parity-projection branch of a Boolean parent.

The class is FEI-hard. Given Boolean h, set g(x,z)=h(x)1{z=+1}. With normalized squared spectrum,

    H_norm(g)=H(h)+1,       I_norm(g)=I(h)+1/2.         (8)

If H_norm<=C I_norm held for all partial Boolean functions, apply it with h replaced by h^(tensor r), divide by r and let r tend to infinity. This yields H(h)<=C I(h), full FEI.

Nor does repeated projection preserve partial Boolean values. For the two-bit one-point defect, projection onto both zero spectral parities is its constant Fourier coefficient, the constant function 1/2. Thus an adaptive parity proof cannot independently recurse on an allegedly easier class. It would have to preserve and exploit the coupling of all branches or the original signed convolution identities globally.

## 5. Exact checks and a caught implementation error

Executed from the solo folder:

    python check_signed_basis_barrier.py
    python -m py_compile check_signed_basis_barrier.py

The final run returned PASS using exact integer/rational arithmetic and 160-bit outward rational logarithm intervals. The saved certificate covers:

- the one-point coefficient, influence, sign-overlap and K formulas for n=2,...,10;
- all 1,844 pairs of a Boolean truth table through n=3 and a nonzero query direction for the projection identities;
- all 276 Boolean truth tables through n=3 for the partial selector lift;
- all 6,651 partial Boolean truth tables through n=3 for the Boolean-parent completion.

An intermediate checker version incorrectly expected the selector lift to duplicate each source spectral mass rather than split it in half between two selector coefficients. Its assertion failed. The normalization was corrected from p,p to p/2,p/2, after which the entropy and influence identities and the exhaustive checks passed. This was a checker error, not evidence for a mathematical claim. The failed assertion is recorded here so that the check history is not silently idealized.

Finite checks do not prove the universal statements; the algebraic proofs are in `SIGNED_BALANCE_AND_LINEAR_BASIS_BARRIER_2026-09-18.md`. These checks are self-checks, not independent audits.

## 6. Approach changes and negative results

The initial route in this continuation was to weight the exact signed cancellation by coefficient scale. Formula (4) gives an explicit obstruction: all logarithmic cost may occupy one sign class even when unweighted overlap is exactly balanced. The approach was changed to linear parity coding.

Arbitrary fixed bases and redundant fixed parity systems fail by (7). Conditioning avoids the specific marginal-entropy loss, but exact Fourier projection exposes the partial-Boolean closure. The completion construction and tensor lift show that proving the same inequality independently on each branch is not a reduction to an easier problem. The surviving possibility is a coupled, variable-length multiscale analysis that uses the original Boolean identities globally. No such analysis is supplied.

No random search, floating plateau, finite atlas extension, or resurrection of the disproved positive-power moment route was used.

## 7. Literature checks and novelty limits

Fresh searches included:

- `site:arxiv.org "Fourier entropy" "even function" Boolean influence`
- `site:arxiv.org "Fourier entropy-influence" lift parity`
- `site:arxiv.org Boolean Fourier entropy "even levels" influence`

They did not verify novelty for the signed-balance observation, the one-point basis obstruction, or the partial-branch completion. Primary sources reopened or surfaced include:

- González, MacManus and Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246, https://arxiv.org/abs/2606.00246 . Coordinate-restriction induction is overlapping prior art.
- Li and Han, *Strengthening Han's Fourier Entropy-Influence Inequality via the Edge-Isoperimetric Inequality*, arXiv:2512.03117, https://arxiv.org/abs/2512.03117 . Its abstract states a marginal-influence logarithmic bound; it does not supply the universal constant needed here.
- O'Donnell and Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, https://arxiv.org/abs/1304.1347 .
- Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, https://arxiv.org/abs/1806.03646 .

Search results cannot establish absence of prior art. No novelty or breakthrough claim is made.

## 8. Exact remaining obligation

For every real coefficient vector a whose inverse Walsh transform is Boolean, prove for some universal finite C

    sum_edges min(a_S^2,a_T^2)|log_2(a_S^2/a_T^2)|
       <= C sum_S |S|a_S^2,                             (9)

or construct a Boolean counterexample family with unbounded ratio. Existing reductions prove that this is equivalent to FEI up to an explicit additive constant.

Any signed-cancellation proof of (9) must transport cancellation across magnitude scales and avoid repeated influence credit. Any parity-query proof must analyze the coupled conditional branches without recursively assuming FEI on the exact FEI-hard partial-Boolean closure.

## 9. Measured execution

The supplied run start was 2026-09-18T01:59:11Z; the first sampled shell clock was 01:59:31Z. This report checkpoint is 02:12:26Z, 13 minutes 15 seconds from the supplied start and 12 minutes 55 seconds between shell-clock samples. This measures elapsed retrieval, reasoning, writing and checking time, not continuous model compute. GitHub delivery time is not included.

Earlier intervals between scheduled continuations are not claimed as active research. Neither the schedule nor this report establishes an hour of work or ten continuous hours.
