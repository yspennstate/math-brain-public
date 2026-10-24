# Exact posterior erasure for control-first activation

Stage 2, A012/B03. All entropy/cross entropy is in bits. This repairs the stage-1 physical-label obstruction and consumes A013's original projected-reference activation clause. No arbitrary-core FEI bound is assumed.

## 1. Complete output reference retaining the entire core bill

Let g be balanced Boolean on n uniform data coordinates, r>=1 fresh controls, p=2^-r, F=1+A_r(g-1). Fix a complete nonempty core spectral subprobability reference R_g(T), T nonempty, with z=sum_T R_g(T)<=1 and c_g=sum_T ghat(T)^2 log2(1/R_g(T)). If a supported core set has zero reference mass, the cost is infinite and the assertion is trivial. Define the fixed output reference

Q_F(empty,empty)=(1-p)^2,
Q_F(U,empty)=p^2                 for U nonempty,
Q_F(U,T)=p^2 R_g(T)              for T nonempty and every U.

Its total mass is 1-p+pz<=1. A generator chooses the vacuum with probability (1-p)^2, the control-only sector with probability p-p^2 and then a uniform nonempty control subset, or the data sector with probability p and then a uniform control subset and a trial from R_g; missing core reference mass is failure. The root/sector probabilities, all support choices, and the full subprobability penalty of R_g are present. No physical stopping leaf label is transmitted.

The actual Boolean spectrum is P(empty,empty)=(1-p)^2, P(U,empty)=p^2 for U nonempty, and P(U,T)=p^2 ghat(T)^2 for nonempty T. Hence

CE(P_F,Q_F)=p c_g + A_r,
A_r=2rp(2-p)+(1-p)^2 log2(1/(1-p)^2).                         (1)

In particular CE-H(F)=p[c_g-H(g)], exactly; the subprobability deficit is not erased. If c_g<=K I(g), then CE<=max(K,C_act) I(F), where I(F)=p[I(g)+r] and C_act is the sharp selector coefficient below. This is an ideal complete reference/cross entropy, not a claim that a one-symbol integer prefix code has no rounding overhead. Coding repeated independent output samples by arithmetic/Shannon codes approaches this ideal cost; no single-sample rounding bill is silently dropped.

## 2. Sharp all-r selector coefficient

Set

c_r=A_r/(rp)=4-2p-2(1-p)^2 ln(1-p)/(rp ln2).

The exact maximum over integer r>=1 is at r=3:

C_act=15/4+(49/12)log2(8/7), with 4.536<C_act<4.537.            (2)

Proof: -(1-p)ln(1-p)<=p, so c_r<=4+2/(r ln2). Since ln2>2/3, all r>=6 give c_r<4.5. Outward rational logarithm intervals certify c_3>4.5 and c_j<c_3 for j=1,2,4,5; the finite certificate plus this analytic tail proves the all-r maximum. The log certificates use the positive atanh series and its proved geometric remainder, not floating-point signs.

This coefficient is sharp for a bound of the form CE(F)<=p c_g+C I_sel(F) valid for every balanced core/reference. Taking an exact core reference makes c_g=H(g). Every complete subprobability output reference has CE>=H(F), so C>=A_3/(3/8)=C_act by the exact activation identity. Thus the construction realizes the optimal such activation transfer constant. This does not identify an optimal full-FEI constant.

## 3. Exact true witness and exact erased posterior

Use A011's control-first spectral coupling, reconstructed here. At each node choose a fair physical child, recursively sample its spectral witness with residual Fourier set V, and sample the queried spectral membership bit with probability

theta_V=(uhat(V)-vhat(V))^2/[2(uhat(V)^2+vhat(V)^2)].

The child-mixture residual mass is (uhat(V)^2+vhat(V)^2)/2, so the output masses in the two queried-frequency sectors are (uhat(V)+vhat(V))^2/4 and (uhat(V)-vhat(V))^2/4, the exact Boolean parent spectrum. Zero packets are never sampled. Let W retain the physical stopping/core leaf J, the sampled leaf data set T, and the membership bits on queried controls. Constants have the deterministic empty leaf spectrum; the terminal core uses its actual spectrum.

Let J=j mean first mismatch at control j (1<=j<=r), and J=* mean all controls match. Their probabilities are 2^-j and p respectively. Their depth entropy is

H(J)=D=sum_(j=1)^r 2^-(j-1)=2(1-p).

For a suffix with k remaining controls let s_k=2^-(k-1), m_k=1-s_k,
q_k=(1+m_k^2)/2, epsilon_k=s_k^2/[2(1+m_k^2)], and

B_k=q_k h2(epsilon_k)+(1-m_k^2)/2.

All nonempty residual packets have theta=1/2 because the constant child has zero coefficient there. The exceptional residual-empty packet has q_k and epsilon_k as stated. Thus B_k is exactly the expected conditional membership-bit entropy at that node and is independent of the balanced core's full spectrum. The node is reached with probability 2^{-(r-k)}. Entropy chain rule gives

H(W)=D+pH(g)+sum_(k=1)^r 2^{-(r-k)} B_k,
H(W|S)=D+sum_(k=1)^r 2^{-(r-k)} B_k-A_r.                     (3)

This is the exact all-r posterior-erasure cost, not just the stage-1 lower bound. It is independent of n and of the balanced core g. It tends to two bits: the lower bound is D-A_r->2; the upper bound is D, because A_r minus the weighted B_k sum is a sum of actual nonnegative Jensen-Shannon increments (equivalently I(J;S)). For the upper bound, data-sector leaf T is determined by S and the remaining innovations are the membership bits already in S; W is exactly (J,S), so H(W|S)=H(J|S)<=H(J)=D. This also proves the limit without appealing to an unreviewed JS bound.

Explicit joint law useful for independent reproduction: on nonempty-data output (U,T), J=* is determined and the joint mass is p^2 ghat(T)^2. For control-only U, J is a stopping leaf. Put epsilon_i=epsilon_(r-i+1) for control indices i=1,...,r. For U empty,

Pr(J=j,S=empty)=2^-j product_(i=1)^j (1-epsilon_i).

For U nonempty, m=max(U), j>=m,

Pr(J=j,S=U)=2^-j epsilon_m 2^-(m-1)
                         product_(i=m+1)^j (1-epsilon_i).      (4)

The mass is zero for j<m. Earlier control membership bits are fair after the highest included index has been created. Summing (4) over j reproduces p^2 for every nonempty control U, and the empty-row sum is (1-p)^2. Formula (4), or the recursive coupling, supplies the exact posterior distribution. No tensor seed entropy is hidden in these control-only posteriors.

## 4. Independent review of A013's existing activation clause

The original A013-VACUUM-PROJECTED-COVER-STABILITY@1 activation clause is reconstructed separately, not repaired as part of its acceptance. The passive prefix/Kraft reference has raw control-only masses q(U)=sum_(j>=max U)4^-j and raw nonempty-data mass p^2 R_g(T). Its raw empty mass is sum_j4^-j. The total nonempty raw mass is

q_star=sum_j(2^j-1)4^-j+pz=2/3-p+p^2/3+pz>0.

Vacuum replacement gives Q13(empty)=(1-p)^2 and Q13(nonempty)=v q/q_star, v=2p-p^2. This is a full probability reference. Its exact CE is

h2(v)+sum_(S nonempty) P_F(S)log2(1/q(S))+v log2 q_star.

Since q(U)>=p^2 and q_star<=1, the exact expression is at most h2(v)+2rv+p c_g, and h2(v)<=2pr+2p/ln2 gives the stated A013 coefficient 6+2/ln2. All signs, missing reference mass and the normalization term are retained. Verdict: HOLDS for this explicitly named activation clause only; the rest of A013's cover/restriction claim is not independently accepted by this run.

The sharper Q_F in Section 1 is a separate refinement: it does not assert that A013's particular projected reference itself attains the sharp coefficient. It replaces coarse raw-Kraft vacuum/nonempty weights by the actual coherent control-sector probabilities. No modification or repair of A013's original proof is needed for the reviewed statement.

## 5. Operation scope and first unsupported line

Disjoint complete reference costs add. Fresh-character balancing permutes the spectrum/reference, preserves cost and adds one physical influence. Applying (1) to balanced outputs therefore preserves max(K,C_act) over arbitrary compositions of those operations, with each core bill multiplied by exactly its activation probability. General physical data restrictions may make a core unbalanced; they are outside this balanced-reference theorem. Shared controls and coherent products are outside disjoint factorization.

For g_t=z product_(j=1)^t f(x^(j)), a disjoint product reference has cost t c_f, and the new activation cost is p_t t c_f+A_(r_t), NOT just A_(r_t). The exact true witness retains p_t t H(f). With r_t=ceil(2log2(t+1)), the control overhead divided by p_t t tends to zero. Thus optimal control erasure does not make an arbitrary seed easier.

First unsupported universal line: every arbitrary balanced core admits a complete fixed reference with c_g<=K I(g) for one absolute K; alternatively, a new two-child collision transfer must pay its complete conditional core reference without assuming that statement. The original incidence queue's (L)+(S)+(R) infimum is not bounded by this separate output reference. This stage follows the lead's A012 target and consumes the existing A013 repair instead of repeating its coarse theorem or the solved projective-plane family.
