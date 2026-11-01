# Conditional countable-population uniqueness in a monotone face phase

Status: PROVED uniqueness within the precisely specified phase class; existence of this phase for the full initialized network remains OPEN. This is not a new global T384 limit.

Fix 0<rho<1, G=[[1,rho],[rho,1]], a matrix C, and finitely or countably many nonzero real marks z_i with M=sum z_i^2<infinity. For each mark choose a boundary coordinate b_i and the other coordinate p_i. Initial projected endpoints q_i(0) are fixed and shared by the two solutions compared. Assume continuous residuals on [0,T], absolutely continuous endpoint paths, and measurable theta_i in the Heaviside graph H(q_i,b): H(x)={0} for x<0, {1} for x>0, [0,1] for x=0. Require throughout the phase:

1. The support projection q_i,p remains positive (a.e. positivity suffices for the equations); its gate is 1.
2. z_i r_b_i<=0 for both candidate residual paths.
3. q_i,b'=z_i(r_b_i theta_i+rho r_p_i), and q_i,p'=z_i(rho r_b_i theta_i+r_p_i).
4. The residual identity is r(t)=R-C integral_0^t r(s)ds-sum_i z_i[(q_i(t))_+-(q_i(0))_+].

The increment series is uniformly absolutely convergent because bounded residuals imply |q_i(t)-q_i(0)|<=K|z_i|T, so each summand is bounded by K z_i^2 T. No summability of the un-subtracted initial outputs is required.

**Theorem.** This phase class contains at most one residual and endpoint trajectory for the given data. Gate fractions on sets where their coefficients vanish need not be unique, and no such uniqueness is asserted.

**Proof.** Denote differences by Delta. For a single boundary coordinate, set a=z_i r_b<=0, c=rho z_i r_p. Monotonicity of H gives (q_b-tilde q_b)(theta-tilde theta)>=0. Decompose

Delta q_b'=a(theta-tilde theta)+(a-tilde a)tilde theta+c-tilde c.

The first term cannot increase |Delta q_b|. The elementary absolute-value comparison (or a smooth approximation of |x|) therefore gives

|Delta q_b(t)|<=|z_i|(1+rho) integral_0^t ||Delta r(s)||_infinity ds.

This argument is valid for absolutely continuous functions and measurable graph selections; on the equality set the absolutely continuous difference has derivative zero almost everywhere; this is an a.e. comparison, not a pointwise Dini-derivative assertion. The exact tangential elimination is

Delta q_p(t)-rho Delta q_b(t)=(1-rho^2)z_i integral_0^t Delta r_p(s)ds.

Thus the same bound holds for |Delta q_p|, since rho(1+rho)+(1-rho^2)=1+rho. ReLU is 1-Lipschitz in the infinity norm. Subtracting the residual identities and summing the absolutely convergent difference series gives

||Delta r(t)||_infinity <= [||C||_infinity+(1+rho)M] integral_0^t ||Delta r(s)||_infinity ds.

Gronwall proves equality of residuals; the single-atom estimate then proves equality of all endpoints. QED.

## Meaning for the unfinished problem

The result removes residual-feedback nonuniqueness **after** a fixed monotone support phase has been established, even for infinitely many square-summable endpoints. It allows the boundary projection to leave zero: theta becomes its genuine active/inactive gate. Loss of strict inward attraction alone need not destroy uniqueness, provided z_i r_b remains nonpositive and the other support stays positive. No uniform lower bound on all support projections is used in this uniqueness proof.

What is not paid: showing that initialized marks enter this class, identifying initial endpoint data at a transition, proving the support remains positive, switching the designated boundary coordinate, or controlling infinitely many support-loss times. The all-zero endpoint branch of the earlier unselected inclusion is not an admissible alternative here when a positive support is required. This is a conditional phase uniqueness theorem, not a removal of the original entrance ambiguity.
