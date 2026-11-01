# Root derivation — when the full-score envelope is saturated

Status: exact finite-dimensional observation, not an additional sub-agent and not a concavity proof. This specifies where X031's adaptive envelope can add a proper reduction.

Let K be a strict three-site Hermitian contraction with nonreal cycle product K12 K23 conjugate(K13). Its centered atom-score span is the entire seven-dimensional space of centered functions on the eight measured outcomes.

To prove this, use a fixed diagonal gauge at the base and local coordinates

    Kii = a_i, K12 = r12>0, K13 = r13>0, K23 = r23 exp(i phi).

The seven nonempty inclusion moments are

    m_i=a_i,
    m_ij=a_i a_j-r_ij^2,
    m_123=a1 a2 a3-a1 r23^2-a2 r13^2-a3 r12^2
                         +2 r12 r13 r23 cos(phi).

Their Jacobian with respect to (a1,a2,a3,r12,r13,r23,phi) is block triangular. Its determinant has absolute value

    16 (r12 r13 r23)^2 |sin(phi)| > 0.

All seven coordinate velocities are legitimate local Hermitian velocities because strictness is open. Inclusion-exclusion is an invertible linear map from the seven nonempty moments to normalized atom probabilities. Dividing their derivatives by the positive base atoms therefore gives seven independent centered scores, proving the assertion.

Consequently, at such a reference K, X031's full-score exponential family is the entire positive probability simplex. Matching all its feature means identifies the full probability law: q_theta(Q)=p_Q for every strict Q. Its entropy majorant G_K(Q) is exactly H(p_Q), and its remaining inequality is exactly the original Hessian inequality. It is not a lower-dimensional simplification at these generic three-site references.

At a real-cycle reference, the cycle phase derivative vanishes and the displayed argument does not apply. Such references, count features, compressed score spaces, and four or more sites can leave a proper moment-matching family. For example a generic four-site matrix has at most 16−3=13 independent measured scores after diagonal gauge, below the fifteen dimensions of its atom simplex. No concavity of the resulting proper envelope is inferred from this dimension count.

This observation leaves X031's exact optimization dual, uniqueness, and envelope identities intact. A useful subsequent variational proof must exploit an actual reduction of features or prove new positivity even when the envelope is saturated.
