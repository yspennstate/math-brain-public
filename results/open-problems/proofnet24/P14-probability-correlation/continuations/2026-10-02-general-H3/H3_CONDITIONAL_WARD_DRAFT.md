# Candidate general H3 electrical sum of squares

Research draft, 2 October 2026. This continues the independently audited general H2 theorem. The derivation below is complete as an algebraic candidate proof, but requires independent scrutiny of every Ward, covariance, and grounding step before promotion to a proved result. Historical novelty is not certified.

## Candidate theorem and notation

Use all notation and hypotheses of `GENERAL_H2_SOS_PROOF.md`: a connected finite weighted graph, distinct marked non-bridge edges e and f, positive conductances c_g, weighted tree sum tau, special unit-current potentials v,w with disjoint supports E,F, and zero interface S. Let

    A=N(E) intersection S, D=N(F) intersection S

be the port sets. The grounded harmonic rows p_x, boundary inverse T, and response rows eta_(e,g),eta_(f,h) are those of that theorem. Write the forest Rayleigh expansion as

    R_ef(lambda*c)=H0*lambda^(2n-4)+H1*lambda^(2n-5)
        +H2*lambda^(2n-6)+H3*lambda^(2n-7)+...

Assume H0=H1=H2=0. For each original edge g define

    a_g(x)=p_x*T*eta_(e,g)^T,
    b_h(x)=p_x*T*eta_(f,h)^T.

The first family is constant on D and throughout F; the second is constant on A and throughout E. Subtract those respective constants to obtain potentials alpha_g vanishing on D union F and beta_h vanishing on A union E. The candidate formula is

    H3=tau² sum_(g,h,k in original edges) c_g*c_h*c_k
             [alpha_g(x_k)*beta_h(y_k)
                -alpha_g(y_k)*beta_h(x_k)]².                (T)

Thus H3>=0. If H3 is positive, the marked forest edge indicators are negatively correlated for all sufficiently large lambda. Formula(T) gives no sign conclusion beyond another vanishing coefficient.

All response rows refer to unit currents, not conductance-weighted currents. The three explicit conductance factors in(T) are c_g,c_h,c_k; no factors c_e or c_f are missing or inserted.

The proof below chooses a convenient root to evaluate the right side. Full response charges are zero-sum and do not depend on this root, so shifting each auxiliary potential to vanish at its opposite port set gives the same alpha,beta for every root in S.

## 1. Port support and the response kernel

To make grounding transparent, first use full harmonic rows p*_x on all of S, including the identity row at every s in S. For x in E or F, these are the Dirichlet harmonic-extension rows. Their entries sum to one. The grounded rows are obtained by deleting the root coordinate and setting its field to zero. Define full response rows by the same eta formula with p* in place of p. Their coordinates sum to zero. Their only possible support is A for the e response, and D for the f response. Indeed every nonzero term involving v belongs to an E–E or E–S edge, and all harmonic rows there are supported on A; similarly for F.

Let B_e*=sum_g c_g eta*_(e,g)^T eta*_(e,g) be the full response matrix on S. For arbitrary real boundary values z, let h be their harmonic extension and let pi_e z be the common marked-endpoint value. Then z^T B_e* z vanishes exactly when z is constant on A.

The forward direction follows from every E–S edge xs: its eta evaluation is v(x)(h(s)-pi_e z). Since v(x) is nonzero, vanishing of every response forces h(s)=pi_e z for every port s in A. Conversely, if z is constant on A, the maximum principle makes its harmonic extension constant throughout E, with that same endpoint value; every eta evaluation vanishes. Values outside A are immaterial. Thus

    range(B_e*)=the full zero-sum contrast space on A,
    range(B_f*)=the full zero-sum contrast space on D.       (1)

This is a kernel statement, not an assertion that either matrix has nonpositive off-diagonal entries. The proof does not require an auxiliary positive-weight graph representation of B_e or B_f.

The H2 sum of squares implies every e response and f response is orthogonal in the boundary Green inner product. By (1), every A contrast is orthogonal to every D contrast. Hence A and D cannot have two distinct vertices in common: their shared difference vector would have strictly positive Green norm but would be orthogonal to itself.

If either port set is a singleton, ground at that port. The corresponding entire conditional marked score is constant in the remaining boundary fields, so all mixed coefficients vanish; its response rows and formula(T) are zero. Equivalently this is the familiar forest-block factorization at a one-vertex interface. It therefore suffices to consider |A|,|D|>=2. In that case choose

    r in A minus D.                                       (2)

For this root the grounded e response matrix is positive definite on A minus {r}. H2=0 forces every f auxiliary potential b_h to vanish on A, and harmonicity forces it to vanish on E. The f kernel similarly forces each e auxiliary potential a_g to be constant on D and F. Write its constant as k_g. Thus for this calculation

    beta_h=b_h, alpha_g=a_g-k_g.                          (3)

The full physical source of a_g is the lifted zero-sum row eta*_(e,g), supported on A; that of b_h is eta*_(f,h), supported on D. Lifting restores the root coordinate as minus the sum of the remaining coordinates. Because r is not in D, each f charge already has total sum zero in its ungrounded coordinates.

## 2. Forest generating function and Berezin convention

Use left Grassmann derivatives throughout. Write q_i=barpsi_i*psi_i, with the root field fixed to zero. Normalize Berezin integration so that

    integral exp(+barpsi L_r psi)=det(L_r),
    <product_(i in I) q_i>=det(K_(I,I)).

The positive Gaussian exponent is essential for the covariance signs below. Define

    V=sum_(i!=r) q_i-sum_(xy in edges) c_xy*q_x*q_y.

Then the exact normalized forest expansion is

    F(t):=sum_(j>=0) (tau_(j+1)/tau)*t^j=<exp(tV)>,
    t=1/lambda.                                          (4)

One can verify (4) by the same Euler-feature argument used for Q2,Q3 in the H2 note. In a (j+1)-component forest, each non-root component chooses either a vertex, with sign +, or an edge, with sign −. Removing the chosen edges creates the rooted forests counted by principal Green minors. Each non-root component has net multiplicity |vertices|-|edges|=1. Distinct selected roots force chosen edge endpoints and chosen vertices to be disjoint, exactly as Grassmann nilpotence does. Thus every forest has net multiplicity one. In particular Q4=<V³>/6; this is not a new unproved identification of a fourth coefficient.

Partition V into V_E+V_F+V_S exactly as in the H2 note. Conditional Gaussian elimination gives

    M_E(t)=<exp(tV_E)|boundary>_E,
    M_F(t)=<exp(tV_F)|boundary>_F,
    F(t)=<exp(tV_S)*M_E(t)*M_F(t)>_B.                     (5)

The harmonic rows and boundary covariance remain fixed under either marked conductance variation. Only M_E depends on c_e and only M_F on c_f. Put

    U_e(t)=partial_e log M_E(t)=t*u_e1+t²*u_e2+O(t³),
    U_f(t)=partial_f log M_F(t)=t*u_f1+t²*u_f2+O(t³).

The already proved H2 calculation gives

    u_e1=constant+barpsi B_e psi,
    u_f1=constant+barpsi B_f psi,
    B_e=sum_g c_g eta_(e,g)^T eta_(e,g),
    B_f=sum_h c_h eta_(f,h)^T eta_(f,h).                  (6)

Also u_e2=partial_e[<V_E²>_E-<V_E>_E²]/2, and similarly for f. No claim that this second score is supported only on the contrast response space is made. It can contain quartics, and their contribution is indispensable.

## 3. Exact marked-score Ward identity

For a pair of vertices define the deformed edge polynomial

    F_xy(t)=(barpsi_x-barpsi_y)(psi_x-psi_y)-t*q_x*q_y.

The odd vector fields

    Qpsi_t=sum_i (1-t*q_i)*partial_(psi_i),
    Qbar_t=sum_i (1-t*q_i)*partial_(barpsi_i)

annihilate every F_xy(t) when their sum includes both endpoints. This follows by a direct left-derivative calculation. For example partial_(psi_i)q_i=-barpsi_i; the t correction from the quadratic difference cancels the derivative of -t*q_x*q_y.

Consider the raw local F integral before conditioning:

    I_F(t;psi_D)=integral_(interior F)
          product_(i in F)(1+t*q_i)
          exp(sum_(edges incident F) c_xy*F_xy(t)).       (7)

Every port in D is a genuine variable here; by (2), the grounded root is not in D. The edge sum is annihilated by Qpsi_(F union D), so applying Qpsi_D to the integrand is the negative of applying Qpsi_F to its edge exponential. Interior integration by parts gives zero:

    product_(i in F)(1+t*q_i)*(1-t*q_j)
       =product_(i in F minus {j})(1+t*q_i),

which is independent of psi_j. The integral of its product with partial_(psi_j) of the edge exponential is zero. Hence Qpsi_D I_F=0. The bar identity is identical. The weighted vertex measure is precisely what makes the interior divergence vanish.

At t=0, Gaussian elimination gives

    I_F(0;psi_D)=det(L_FF)*exp(barpsi_D N_F psi_D),

where N_F is the contribution of this local subgraph to the boundary Schur complement. The conditional Gaussian normalization yields exactly

    M_F(t)=I_F(t)/I_F(0).

Varying c_f leaves N_F fixed: every harmonic extension has equal values at the marked endpoints, so its Dirichlet energy and Schur complement are unchanged. Therefore

    U_f(t)=partial_f log I_F(t)-partial_f log det(L_FF).

The subtracted term is a boundary-field constant. Since the Ward operators do not depend on c_f, the complete marked score U_f satisfies the exact identities

    Qpsi_D U_f(t)=Qbar_D U_f(t)=0.                    (8)

This argument does not falsely claim that the entire normalized local partition M_F is invariant: its Gaussian boundary normalizer may not be. The marked derivative of that normalizer is constant, and this is the needed cancellation.

## 4. Ward identity for the second-score constant-mode contraction

Write Dpsi=sum_(i in D) partial_(psi_i) and Dbar=sum_(i in D) partial_(barpsi_i). At orders t and t², (8) gives

    Dpsi u_f1=0,
    Dpsi u_f2=sum_(i in D) q_i*partial_(psi_i)u_f1.

Since B_f has zero row and column sums on D, applying Dbar to the second identity gives

    Dbar Dpsi u_f2=barpsi B_f psi.                     (9)

To fix its sign explicitly, partial_(psi_i)(barpsi B_f psi)=-sum_j barpsi_j(B_f)_(ji). Differentiating q_i contributes -psi_i*sum_j barpsi_j(B_f)_(ji), which after reordering equals the bilinear. The other term vanishes by the zero column sums. Constants in u_f1 contribute nothing.

Define the constant-covariance contraction operator

    D1=-Dbar Dpsi.

For every boundary polynomial P, Gaussian Wick differentiation in the rank-one covariance direction J=1*1^T is

    d/ds <P>_(T+sJ)|_(s=0)=<D1 P>_T.                 (10)

It follows by introducing one auxiliary Grassmann pair with covariance s and adding it identically to every port field, or directly by differentiating the Wick minors. For example D1*q_i=1 and D1*(q_i*q_j)=q_i+q_j-barpsi_i psi_j-barpsi_j psi_i; these reproduce the derivatives of the one- and two-pair determinants. Equations(9),(10) give

    <D1 u_f2>=-tr(T B_f).                             (11)

The root restriction in this step is genuine: applying a uniform Ward operator through a fixed zero root field would be invalid. Choice(2) eliminates that issue.

## 5. Cumulant expansion and activity normalization

The logarithmic marked cross derivative of (5) is the covariance of U_e,U_f in the tilted boundary Wick functional. Its first tilted density coefficient is

    W1=V_S+<V_E|boundary>_E+<V_F|boundary>_F.

Thus the coefficient of t³ in partial_ef log F is

    Cov(u_e2,u_f1)+Cov(u_e1,u_f2)
         +Cum(u_e1,u_f1,W1).                          (12)

The conductance-to-activity factors are

    R_ef(lambda*c)
      =-lambda^(2n-4)*tau²*F(t)²
            *partial_ef[log tau+log F(t)].

H0=0 removes partial_ef log tau. Under the equality geometry, the t coefficient is zero. H2=0 removes the t² coefficient. Therefore the multiplier F(t)² makes no additional contribution at t³ and

    H3/tau²=minus the expression in(12).              (13)

No factorial is missing: u_e2,u_f2 are coefficients of t² in the logarithmic scores, and the first tilt contributes its ordinary third joint cumulant. Equivalently this is -partial_ef(Q4-Q2*Q3+Q2³/3) after the lower coefficients vanish.

## 6. Evaluate the two second-score covariance terms

For a bilinear q(a)=barpsi a^T a psi, Wick differentiation gives

    Cov(q(a),P)=d/ds <P>_((T^-1+s*a^T*a)^-1)|_0.

Its covariance variation is -T*a^T*a*T. The polynomial u_e2 is supported only on A (with the root field omitted), because every harmonic row in E and every E edge uses only those ports. Every f response potential vanishes on A. Hence its induced covariance variation restricted to A is zero, and

    Cov(u_e2,u_f1)=0.                                 (14)

Each e response potential a_g is constant k_g on D. Its induced covariance change on D is therefore -k_g²*J. Applying(10),(11), and decomposing B_e as in(6), gives

    Cov(u_e1,u_f2)
       =sum_g c_g*k_g²*tr(T B_f)
       =sum_(g,h) c_g*c_h*k_g²*R_h,                  (15)

where R_h=eta_(f,h)*T*eta_(f,h)^T is the energy of b_h. This is the nonzero second-score correction that a false literal contrast-span argument would miss.

## 7. Evaluate the tilted triple cumulant

Constants drop from third cumulants. The bilinear part of W1 also contributes zero. Indeed the Gaussian third cumulant of bilinears B_e,B_f,C is the sum of the two cyclic traces; after whitening by T, H2=0 means the positive-semidefinite matrices T^(1/2)B_eT^(1/2) and T^(1/2)B_fT^(1/2) have productzero, so both traces vanish.

The quartic part of W1 is exactly

    -sum_(xy in original edges) c_xy*q(p_x)*q(p_y),

because conditional contraction of the original quartic has this uncontracted degree-four boundary term. For two response rows a,b with a*T*b^T=0, the determinant Wick rule gives

    Cum(q(a),q(b),q(x)*q(y))
       =[(x*T*a^T)(y*T*b^T)
            -(y*T*a^T)(x*T*b^T)]².                  (16)

For verification, write the four-vector Gram determinant in a block with upper diagonal entries aTa,bTb and cross inner productzero. In the third-cumulant combination, its constant terms and the terms involving only one response cancel; the remaining determinant correction is precisely the displayed wedge square. This also fixes its positive sign.

Using(16) and the conductance decompositions of B_e,B_f gives

    Cum(u_e1,u_f1,W1)
      =-sum_(g,h,k) c_g*c_h*c_k
          [a_g(x_k)*b_h(y_k)-a_g(y_k)*b_h(x_k)]².     (17)

## 8. Electrical completion for arbitrary multiport source charges

Fix g,h. Write a=a_g, b=b_h, k=k_g. Their physical Laplacian charges are supported on A and D, respectively; b vanishes on A, and a equals k on D. Put

    j_xy=c_xy*(a_x*b_y-a_y*b_x),
    i_xy=c_xy*(b_x-b_y).

Their divergences are

    div j=b*(La)-a*(Lb)=-k*(Lb),
    div i=Lb.

The electrical flow i has energy R_h. Discrete integration by parts gives its energy inner product with j as

    <j,i>_energy=sum_x b_x*(div j)_x=-k*R_h.

Consequently j+k*i is a circulation and

    sum_edges c_xy*[a_x*b_y-a_y*b_x]²-k²*R_h
       =sum_edges c_xy*[(a_x-k)*b_y-(a_y-k)*b_x]².    (18)

This calculation uses general zero-sum multiport charges, not a unit dipole assumption. Equivalently it follows directly by expanding the shifted wedge and applying the same Laplacian integration by parts.

Combining(13)--(18) proves exactly(T), with alpha=a-k and beta=b under the convenient root. The full lifted response charges are independent of grounding and determine potentials up to additive constants. Their opposite-port shifts remove those constants; thus(T) is root-independent.

## Audit targets and current status

The key new ingredient is the exact marked-score Ward identity, including its local normalization cancellation. The formula depends on no assumption that B_e is an M-matrix, no confinement of the second score to its literal contrast span, and no inference that H2=0 implies independence.

Independent exact tests of the shifted-wedge formula are being carried out in `H3_response_wedge_heat.py`. Such tests support normalization but cannot replace the proof. The current draft should be checked especially for: all-order forest identity(4); the root exclusion in(7)--(11); the sign of the constant-mode contraction; the marked derivative of the local Schur complement; the third-cumulant sign(16); and the lift to physical source charges in(18).
