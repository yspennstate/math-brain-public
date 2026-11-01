# Actual nonorthogonal GD: macroscopic tightness and a subsequential inclusion

Status: PROVED partial theorem (internal), independently audited in reviews/e04_macro_review.md and reviews/e03_macro_review.md. This is not uniqueness or a full macroscopic limit. It identifies every subsequential limit of standard simultaneous GD by a marked-endpoint differential inclusion. The missing selection at the collapsed origin is explicit.

## Model, topology, and conclusion

Use exactly the assumptions, a,L,X,G, primitive joint law (F,C,N), and actual simultaneous GD equations (1) in BOUNDARY_GRID.md, with fixed gamma>0 and physical step h=gamma/L. Let T<infinity be fixed, let n run through ceil(T/h), and use polygonal interpolation of outputs at physical grid times nh. Set r_m=y-f_m. The held output has the same limits, since its maximum jump tends to zero in probability.

Then the output paths are tight in C([0,T];R^k), jointly with the initial primitives. Along every subsequence there is a further subsequence whose joint limit can be represented on an extended probability space by (F,C,N), a continuous residual r, and, for each atom (z,u) of N, absolutely continuous paths q_(z,u) and measurable fractions theta_(z,u) in [0,1]^k such that

q_(z,u)(0)=0,
q_(z,u)'(t)=z G D(theta_(z,u)(t)) r(t),              (1)

theta_j(t)=1 if q_j(t)>0, theta_j(t)=0 if q_j(t)<0,
theta_j(t) in [0,1] if q_j(t)=0,                    (2)

r(t)=y-F-C int_0^t r(s)ds-int z(q_(z,u)(t))_+ N(dz,du). (3)

D(theta) is the diagonal matrix of fractions. The Poisson integral in (3) converges absolutely and uniformly on [0,T]. Every such subsequential limit is absolutely continuous and obeys, for almost every t,

r'(t)=-Q_eff(t)r(t),
Q_eff(t)=C+int z^2 D(theta_(z,u)(t))G D(theta_(z,u)(t)) N(dz,du). (4)

In particular Q_eff(t)>=C in the PSD order and

||r(t)||<=exp[-lambda_min(C)t]||y-F||.              (5)

The effective matrix in (4) is a representation of the limiting output action. It is NOT asserted to be the weak limit of the finite-width pre-step tangent Grams; two binary indicators can have correlated occupation limits. No convergence of those Grams in L1, no uniqueness of (1)--(3), and no statement that every solution of the inclusion is realizable by GD is claimed.

## Uniform finite-horizon bootstrap, without finite-step loss descent

Put R_i,n^2=W_i,n^2+||U_i,n||^2 and S_n=a^(-2)sum_i R_i,n^2. For constants depending only on fixed X and gamma, the exact row update and output decomposition give

S_(n+1)<=(1+c_X gamma ||r_n||/a)^2 S_n,
||r_(n+1)-r_n||<=h A_X ||r_n||S_n
                       +h B_X (gamma/a)||r_n||^2 S_n.       (6)

These are the bounds already derived for the finite grid; their use over a growing number of steps requires the following bootstrap. Localize to S_0<=K and ||r_0||<=R. Until S_n exceeds 2K or ||r_n|| exceeds a chosen R_*, take a sufficiently large m that (gamma/a)R_*<=1. Then (6) gives

||r_n||<=R exp[c_1 K(nh)]<=R exp[c_1 K(T+1)].

Choose R_*>2(R+1)exp[c_1 K(T+1)]. On the same interval the row factor accumulated through ceil(T/h) is bounded by

exp[c_2 (gamma/a) R_* ceil(T/h)]
 <=exp[c_3 R_*(T+1)L/a]=1+o(1).                    (7)

For all sufficiently large m it is smaller than 2 (and its squared version can be made smaller than 2 for the S bound). Thus neither stopping threshold can be the first one crossed: the estimates through the preceding step keep the next values strictly below both thresholds. This closes the bootstrap for every step through T. There is no assertion that ||r_n|| decreases at finite m.

It follows on the localized event, uniformly over these steps,

S_n<=2K, ||r_n||<=R_*,
||r_(n+1)-r_n||<=h M_(K,R,T,X,gamma),
|| (W_i,n,U_i,n)-(W_i,0,U_i,0) ||<=epsilon_m R_i,0,
epsilon_m=O_(K,R,T,X,gamma)(L/a)->0.                (8)

The row displacement bound follows by summing row increments with the product bound (7). Initial S_0 and r_0 are tight, so K,R can be removed. Polygonal residual paths are uniformly bounded and Lipschitz on each localized event. Arzela--Ascoli gives tightness; the held/polygonal discrepancy is O_P(h). ReLU Lipschitzness and Cauchy--Schwarz also give

sup_n ||C_m,n-C_m,0||=O_P(L/a),
sup_n a^(-2)sum_i |W_i,n^2-W_i,0^2|=O_P(L/a),
sup_(n,j) ||a^(-2)sum_i h_i,n h_i,j^T-C_m,0||=O_P(L/a). (9)

The last estimate is a cross-time Gram bound, not a symmetry assertion: replace each h_i,n by h_i,0 and bound each difference by ||X||epsilon_m R_i,0.

## Endpoint compactness, with fractions rather than binary limiting gates

Let z_i,0=W_i,0/a. The exact projected update is

V_i,n=V_i,0+gamma z_i,0 sum_(j<n)G D(V_i,j)r_j+e_i,n,
sup_(i,n)||e_i,n||=O_P(L^2/a)->0.                  (10)

Indeed max_i R_i,0/a<=sqrt(S_0), so (8) gives max_i,n |W_i,n/a-z_i,0|=O_P(L/a), and there are O(L) steps. The uniform error estimate does not require gate continuity or a bound on the number of crossings.

For each matched initial marked endpoint atom (W_i,0/a,U_i,0)->(z,u), define the polygonal q_i,m=V_i/L in physical time. Its grid derivative is (W_i,n/a)G D(V_i,n)r_n, hence it is bounded on the localized event for each retained atom, and q_i,m(0)=XU_i,0/L->0. It is therefore precompact uniformly. The held gate vectors D(V_i,n) take values in a fixed bounded set, so their entries have weak-star subsequential limits theta in L-infinity. Uniform convergence of r_m and W_i,n/a->z passes the product with these gates through the integral equation, yielding (1). On any compact subinterval where a component q_j is bounded strictly away from zero, uniform convergence fixes the finite-width sign, so (2) holds almost everywhere; a countable exhaustion covers its positive and negative open sets. Nothing fixes theta at q_j=0 yet.

For rigor, carry out this extraction jointly with (f_0,C_m,0,N_m,S_0), the uniform error variables, and finitely many atom configurations on nested deterministic compact cutoffs epsilon<|z|<M, ||u||<B having zero-intensity boundaries. Order each finite set using a fixed coordinate ordering with no ties almost surely, match via point-process convergence, and extract uniform paths and weak-star gates. The weak-star topology on the bounded L-infinity set is metrizable using the separability of L1([0,T]); diagonal extraction over countably many cutoffs includes every Poisson atom. Energy localization makes these families tight. A joint representation of the extracted convergent random elements, or equivalently passage in their integral identities with bounded continuous test functions, preserves the finite-width identities. This is why initial energy and error variables must accompany the initial PPP in the coupling.

No marked-entrance selection is silently added: the paths remain indexed by their original u, but (1)--(2) alone allow several choices from q(0)=0. The finite-grid theorem gives additional early-time information, not a justified interchange of boundary and macroscopic limits.

## Exact output decomposition and uniform small-atom removal

An integration-by-parts identity in the parameter update avoids tangent-kernel averaging entirely. Since

W_i,n-W_i,0=(gamma/a)sum_(j<n) r_j^T h_i,j,

one has exactly

f_n-f_0
 =L^(-1)sum_i z_i,0(h_i,n-h_i,0)
  +h sum_(j<n) [a^(-2)sum_i h_i,n h_i,j^T]r_j.      (11)

By (9), the second term is C_m,0 J_m,n+o_P(1) uniformly in n, where J_m,n=h sum_(j<n)r_j; its error is at most (T+h)R_* times the uniform cross-time Gram error. Polygonal interpolation and uniform residual convergence give J_m->int r.

For an arbitrary subset I of initial rows, summing actual projected increments yields

L^(-1)sum_(i in I)|z_i,0| ||h_i,n-h_i,0||
 <=(gamma n/L)||G|| R_* sum_(i in I)|z_i,0|sup_(j<=n)|W_i,j/a|
 <=(T+h)||G|| R_* [sum_(i in I) z_i,0^2+epsilon_m S_0]. (12)

For the last step, use |W_i,j/a-z_i,0|<=epsilon_m R_i,0/a and Cauchy--Schwarz: sum_i |z_i,0|R_i,0/a<=S_0. Thus the entire initial |z_i,0|<=epsilon output increment is uniformly controlled by its initial square mass, whose limsup expectation is O(epsilon^(2-alpha)), plus o_P(1). This removes small endpoints on the whole physical horizon, even if they cross repeatedly. Large |z| and large original marks for |z|>epsilon are removed by the finite-atom occurrence probabilities; no infinite stable second moment is used.

For each finite retained set, the first term of (11) converges uniformly to sum z(q_(z,u))_+, since q_i,m(0)->0 and ReLU is Lipschitz. In the limit, (1) implies the deterministic bound

sup_(t<=T)||q_(z,u)(t)||<=|z|||G||int_0^T ||r(s)||ds. (13)

Since int z^2 N(dz,du)<infinity almost surely, the limiting output sum is absolutely and uniformly convergent, and (12) permits removal of the finite-width cutoffs. This proves (3). Interpolating (11) does not change the limit: first prove it on grid nodes, then use the O_P(h) residual jump and the retained-path Lipschitz bound, followed by (12) for omitted atoms.

## Output chain rule and limiting loss decay

Equation (13), the corresponding derivative bound ||q'||<=|z|||G||||r||, and int z^2 N<infinity justify differentiating the Poisson sum in (3) in L1 time. Each component of an absolutely continuous function has derivative zero almost everywhere on its zero set. Thus

d(q_j)_+/dt=1{q_j>0} q_j'=theta_j q_j' almost everywhere, (14)

using (2) off zero and q_j'=0 a.e. on zero. A countable union over all atoms and k coordinates preserves this full-measure set of times. Substitution of (1) into (14) gives

d/dt int z(q)_+N = int z^2 D(theta)G D(theta)r N,

and hence (4). The integrand matrices are PSD and bounded by ||G||z^2, so the sum is well defined. Since C is positive definite a.s., the absolutely continuous residual energy satisfies

(1/2)d||r||^2/dt=-r^T Q_eff r<=-lambda_min(C)||r||^2.

Gronwall proves (5). This is a property of every limiting output, not a claim that the binary pre-step Gram converges to Q_eff. The frozen sliding example in e03 explicitly disproves that identification.

## The precise unpaid selector

The inclusion is genuinely underdetermined: choosing every q identically zero and theta identically zero satisfies (1)--(3) with r(t)=exp(-Ct)(y-F), irrespective of the original marks. Prior scalar results and e02's frozen-pair examples show that actual GD need not select this solution. Thus the result cannot be promoted to a unique limiting law by merely writing q(0)=0 or by selecting the minimum-norm vector at that origin.

What remains is a rule retaining mark-dependent entrance and governing all subsequent face transitions while r evolves, plus a uniqueness/stability theorem for that selected system. A possible route is to combine e03's varying-residual strip identity with FACE_SCHUR.md inside strict attracting cones, then prove entrance and exit matching. This partial theorem has paid uniform finite-horizon energy, output tightness, frozen second-layer Gram, endpoint compactness, uniform small-atom removal, and a compatible residual action. It has not paid that selection and uniqueness step, deep networks, or test-input predictions.
