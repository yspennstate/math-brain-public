# Adversarial audit of the reduction

## Independent derivations

1. Theorem 1 was derived by conditioning on the label and pairing T with -T. A second deterministic check is to sort the two thresholds: when L<-|H| both branch errors occur; when -|H|<L<|H| exactly one occurs; when L>|H| neither occurs. This is the same event count as the two linear forms L+H and L-H. The boundary cases obey the strict-indicator identity too, although classification ties need separate treatment.

2. For the orthogonal example, the direct signed score is r+Y Z_1+bY|Z_2|. Its two noise terms are independent centered normals. To verify independence without assuming it, condition on (Y,Z_2): Y Z_1 still has the same N(0,1) law. Separately, the law of Y|Z_2| is N(0,1) because the independent sign is balanced. This gives variance 1+b^2, independently of the branch formula.

3. The constants in Lemma 2 also have a proof independent of integrating the hazard. Put h=a-b>=0. Shifting the integration variable gives

       Q(b) = integral_a^infinity phi(s-h) ds
            = integral_a^infinity phi(s) exp(hs-h^2/2) ds
            >= exp((a^2-b^2)/2) Q(a).

   For the other inequality, for t>0 substitute s=t+z/t in the tail integral to obtain

       Q(t) = phi(t) A(t)/t,
       A(t) = integral_0^infinity exp(-z-z^2/(2t^2)) dz.

   A(t) is increasing, by pointwise monotonicity of its positive integrand. Hence A(b)<=A(a), giving

       Q(b)/Q(a) <= (a/b) exp((a^2-b^2)/2).

   These direct proofs in fact establish (5) for all a>=b>0. The condition b>=1 in the corollary supplies a uniform bound on a/b from a bounded squared gap.

4. Recomputing the margin loss directly gives r^2-r^2/(1+b^2)=r^2 b^2/(1+b^2). For b=1/sqrt(r), this is r^2/(r+1). For b=c/r, it tends to c^2. Thus the exponent in the limiting ratio is c^2/2, and the lower-bound exponent for the divergent example is r^2/[2(r+1)]. The independent numerical table checks both expressions against erfc tails.

5. The second moment of the even component is b^2 E[X_2^2]=b^2, rather than a dimension-dependent norm estimate. The distribution gives E[X_2^2]=1 exactly.

## Attempts to break the assumptions

- **Unbalanced labels:** the half-sum in (2) uses the prior 1/2 exactly. The theorem is not stated for unequal class probabilities.
- **Nonzero bias:** a general biased ReLU score need not have a linear odd component as in (4). Bias-free is essential to that particular decomposition.
- **More than one absolute-value term:** the indicator swap proves (1) for one absolute value. It does not prove it for sums of absolute values. Equation (3), not (1), is the statement for general odd/even decompositions.
- **A branch vector vanishes:** when u=v, the score can be zero on an entire half-space; a convention at zero changes classification error. The theorem excludes u+v=0 or u-v=0. The verifier explicitly rejects u=v.
- **Negative margins:** squaring a negative margin loses the classification direction. Formula (1) allows negative margins, but Corollary 3 explicitly requires both margins to be at least one. Negative-margin cases were included in the identity checks.
- **Singular covariance:** standardization can fail. Positive definiteness is an explicit hypothesis; no extension to singular covariance is claimed.
- **Rare errors:** an absolute quadrature tolerance or an additive o(1) disagreement bound can dwarf the target risk. The numerical integral is scaled by the Bayes tail, and the transfer statement requires disagreement at the target tail scale.
- **High probability versus expectation:** a training-event failure probability may dominate an exponentially small risk. The proof states its comparison conditionally and does not integrate away that issue.
- **Training dependence:** conditioning is justified only because the test point is independent of the training sample. No train/test exchangeability trick or uniform convergence argument is being used.
- **Network training:** the example is not asserted to be an interpolating GD output. Width can be increased by splitting identical neurons, but that alone supplies no learning theorem and is not used to claim overparameterized training behavior.
- **Novelty:** these elementary identities may be known. The deliverable is a fully checked reduction and a precise obstruction, not a claim of a new generalization theory.

## Numerical audit

`python -B verify_reduction.py` integrates the actual four-ReLU decision regions, conditional on the second Gaussian coordinate. It uses two panel resolutions and tighter tolerance in the second pass. All nine cases passed; the refined maximum relative discrepancy was 6.661338147750939e-15. There are also 28 tail-inequality checks and 15 rows of threshold data.

The initial integration failed at a real cusp in the correlated case. Splitting there fixed convergence without loosening the global tolerance. Numerical checks are approximate corroboration and are not used in any proof step. The finite truncation at |Z_2|=40 has omitted mass at most 2Q(40)<exp(-800); among the chosen cases the Bayes signal is at most 8, so that truncation is negligible even relative to the smallest checked error.
