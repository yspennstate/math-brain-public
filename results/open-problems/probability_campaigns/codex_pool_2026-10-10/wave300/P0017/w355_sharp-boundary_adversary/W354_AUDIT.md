# Independent audit of w354's saved interval proof

Auditor w355, 2026-10-10. The independent simplex derivation in ATTEMPT.md was saved before the paired proof was read. The snapshot audited was ~/brain_workers/w354/ATTEMPT.md with heading 'Scale boundary' and no full-KLS proof.

Verdict: KEEP the stated interval special case and its scope. The exact claims are Var(U_L)=L^2/12, C_P(U_L)=L^2/pi^2, h(U_L)=2/L, and after variance-one normalization C_P=12/pi^2 and h=1/sqrt(3). The statement requires L>0, the ordinary Euclidean metric, the variance/Dirichlet-energy convention for C_P, and the boundary/min(mass,1-mass) convention for h.

Independent calculation: integrate x and x^2 against dx/L for the variance. In the mean-zero Neumann Fourier expansion, each mode k>=1 has derivative energy (k*pi/L)^2 times its L2 norm, so the first cosine attains the largest ratio L^2/pi^2. For a set with probability between zero and one, one-dimensional perimeter pays at least one interior boundary point of density 1/L; the smaller of its mass and complementary mass is at most 1/2. A half interval attains 2/L. The same bound extends to the outer Minkowski definition by its perimeter lower bound. Translation and dilation to an interval of length sqrt(12) give the normalized constants.

No erroneous step was found in this saved proof. Its conclusion is an exact scale boundary, not a full-KLS result. No full proof route was present to audit in that snapshot; the separate simplex derivation tests a stronger slicing bridge and is not attributed to w354 as an asserted full proof.

Minimal missing premise in any attempt to continue this via conditioning: global covariance normalization must not be transferred to every conditional fiber. ATTEMPT.md gives the exact positive-probability counterexample and the stronger energy-weighting obstruction. The valid expression retains C_P(T|Y) multiplied by conditional directional energy inside the same expectation.

The subsequently saved simplex proof is audited below.

## Independent audit of the subsequently saved simplex proof

Source: ~/brain_workers/w354/SIMPLEX_PROOF.md, read after the independent ATTEMPT.md derivation. Verdict: KEEP the displayed fiber constants and the sharp directional conditional constant; no mathematical gap found in this proof. This is a proof, not a review of another review.

The most important step is Section 2: orthogonal conditioning in the isotropic metric must really fix the other raw simplex coordinates. Independently, Sigma=(I-J/(d+1))/K, K=(d+1)(d+2), and Sigma^{-1}=K(I+J) since J^2=dJ. For A=Sigma^{-1/2}, a=|Ae_1|=sqrt(2K), and v=Ae_1/a, ker(PA)=span(e_1). The restriction of PA to span(e_2,...,e_d) is injective and onto v-perp. This proves the claimed equivalence of conditioning, including its metric; the affine Jacobian is constant. Also <v,A(X-m)>=K(2X_1+S-1)/a=a(X_1-(1-S)/2), so the conditional law is centered uniform of length a(1-S). This agrees with the independently derived regular-simplex model under residual variable t=1-S.

The density d(d-1)s^(d-2)(1-s), the moment E(1-S)^2=6/K, and the positive probability P(S<=1/2)=(d+1)/2^d all agree with the independent Dirichlet calculation. The essential extrema are not justified by the null boundary edge: positive density in every interior neighborhood supplies the correct marginal-almost-everywhere quantifier.

The sharp directional constant follows from the upper bound by fiberwise Poincare and the lower test eta(S) sin(pi T/(a(1-S))). The compact support epsilon/4<S<epsilon/2 keeps the denominator away from zero, and each fixed epsilon has finite full gradient energy. Conditional sine mean is zero and both sine/cosine squared means are 1/2. Its quotient is at least a^2(1-epsilon)^2/pi^2, so taking the supremum over this admissible family gives exactly a^2/pi^2. No uniform full-gradient control of this family is claimed or needed for this directional statement.

Section 5's polynomial witness also checks algebraically: b=A^{-1}(0,1,...,1) obeys b dot v=0 and |b|^2=2(d-1)/((d+1)K). Conditional variance gives the displayed directional quotient, and the orthogonal derivative contributes its stated multiplier. For d=2,k=2, Var(f)=1/2, directional energy=1/3 and full energy=13/27, giving 27/26 for the full quotient. Thus the false mean replacement fails while the extra transverse energy is explicitly retained. This is consistent with w355's cutoff witness, and neither one contradicts full-gradient KLS.

Referee follow-up: w356 independently kept w355 C001/C002; snapshot in REFEREE_VERDICTS.jsonl. This does not change the scope of the w354 audits.

NEXT: Combine the independently checked cutoff witness with the sharp directional result in the triad review packet; preserve the full-gradient gap.
