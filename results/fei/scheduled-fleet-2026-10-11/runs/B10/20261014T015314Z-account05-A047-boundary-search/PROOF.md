# Product-biased deletion audit and repair

All information is in bits. Inputs X_i are independent Bernoulli(p_i), 0<p_i<1. Fourier coefficients use the orthonormal centered product basis. The finite deterministic physical singleton stopping tree never queries a coordinate twice on one path. Keep original ambient coordinate labels and every terminal function.

## 1. The coherent sample and two different budgets

At a node querying i, let G_T,H_T be the two actual child coefficients. Put q_T=(1-p_i)G_T^2+p_i H_T^2. The parent coefficients on T and T union {i} are (1-p_i)G_T+p_i H_T and sqrt(p_i(1-p_i))(H_T-G_T). Their squared masses sum to q_T. Given the current sample with retained label T, choose physical branch b with probability P(X_i=b)*childhat_b(T)^2/q_T. Erase i. Zero rows are unreachable. Parseval gives physical branch probabilities and the actual child spectral laws. Iterate this kernel while retaining the full root sample S as a separate variable. At termination, W=S\Q(Pi) is the actual terminal Fourier sample.

Fix A containing all potentially queried coordinates. Define

  a_i=P(i in S) for i in A, otherwise 0;
  r_i=E 1_{i in S intersect Q};
  a=sum a_i, r=sum r_i;
  R_phys=I_phys(f)-E I_phys(f_leaf).

For Boolean f, Parseval applied to its i-difference gives P(i in S)=4p_i(1-p_i) Inf_i^phys(f). Influences of every unqueried coordinate average to their parent value under a restriction. Summing the reached-node pivotal costs gives R_phys. Consequently

  r_i=sum_{v querying i} w_v 4p_i(1-p_i) Inf_i^phys(f_v),
  a_i-r_i=E [4p_i(1-p_i) Inf_i^phys(f_leaf)], i in A,
  r=I_hat(f)-E I_hat(f_leaf)<=R_phys,

where I_hat denotes expected Fourier set cardinality. Coordinates outside A have no deletion and unchanged average spectral marginal. This distinction is essential: r=R_phys is true for fair biases, generally false for product biases.

## 2. One coordinate-resolved normalized reference

Given S, D=S intersect Q and W=S\D are invertible functions of one another, and deterministic given (S,Pi). Thus

  e=I(W;Pi|S)=H(W|S)=H(D|S).

For a_i>0 put theta_i=r_i/a_i. For a_i=0 use theta_i=0. Define ONE root-conditional reference on subsets d of S intersect A by

  rho(d|S)=product_{i in S intersect A} theta_i^{1_{i in d}}(1-theta_i)^{1_{i not in d}}.

Sum over all subsets to obtain product_i(theta_i+1-theta_i)=1. If theta_i=0 or 1 the actual deletion indicator is respectively 0 or 1 almost surely on i in S; hence the actual conditional law has no mass off the reference support. These endpoint conventions avoid any unsupported logarithm of zero.

Its expected cross entropy is sum_i [-r_i log theta_i-(a_i-r_i)log(1-theta_i)]. Therefore the exact identity is

  e + E_S D_2(P(D|S)||rho(.|S)) = sum_i a_i h2(r_i/a_i) =: C_coord.

Terms with a_i=0 are zero. KL is nonnegative: applying ln z<=z-1 to z=rho/P on the actual support gives -sum P ln(rho/P)>=1-sum_support rho>=0. This also proves the inequality at a support mismatch by infinite KL, although no mismatch occurs here.

Concavity of h2, with weights a_i/a, gives

  e<=C_coord<=a h2(r/a)<=a<=I_phys(f).

The comparison uses the actual r; do not replace r by R_phys inside h2, which is not monotone on its whole domain. The coordinate reference improves A050's common-theta reference and reduces to its uniform identity with r=R_phys. It is a deletion code, not a physical transcript generator or funding source for H(Pi|W).

## 3. Conversion and terminal scope

The coherent channel information satisfies j=I(S;Pi)=sum_v w_v J_v. The exact chain rule is j_W=I(W;Pi)=j+e-I(S;Pi|W), in particular j_W<=j+e. Physical output information o=I(Y;Pi)<=R_phys: at each node I(X_i;Y)<=I(X_i;Y,X_-i)=h2(p_i)Inf_i^phys(f_v)<=Inf_i^phys(f_v), by independence and Boolean fibers.

For completeness, each natural-unit spectral JS fiber is at most p(1-p)(G^2-H^2)^2/q, by ln z<=z-1. Weighted Cauchy gives q*((1/(1-p))+(1/p)) >= (|G|+|H|)^2, so that quantity is at most (|G|-|H|)^2 <= (G-H)^2. Sum fibers: J_v<=4 Inf_i^phys(f_v)/ln2. Therefore j<=4R_phys/ln2. With Gamma_W=H(Pi|Y)-H(Pi|W)=j_W-o,

  o/2+[Gamma_W]_+/2=max(o,j_W)/2
     <=2R_phys/ln2+e/2
     <=2R_phys/ln2+C_coord/2.

At uniform biases the scalar bound J_v<=2 Inf_i(f_v)/ln2 sharpens this to R_phys/ln2+C_coord/2. Here is a self-contained verification: write z=(G^2-H^2)/(G^2+H^2) and d(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2. For z>=0, d'(z)=atanh(z), and the derivative of z/sqrt(1-z^2)-atanh(z) is (1-z^2)^(-3/2)-(1-z^2)^(-1)>=0. Integrating gives d(z)<=1-sqrt(1-z^2); symmetry and continuity cover all endpoints. Multiply by q=(G^2+H^2)/2 to obtain natural JS <=(|G|-|H|)^2/2<=(G-H)^2/2. Parseval and the physical pivotal identity finish the bound. This is A050's repaired conversion with a refined reference. If all terminal functions are independent of A then r_i=a_i for each i, C_coord=e=0 and W=S\A almost surely even when final query sets vary. No disjointness of terminal data cores is needed.

For the actual entropy ledger, let M_T and J_T be reached sums of erasure entropy and spectral channel information. Define Dbar_T=sum_v w_v[h2(p_i)/2-(J_v-M_v)]. Chain rules yield exactly

  H_hat(f)=E H_hat(f_leaf)+2M_T+H(Pi|W)/2+j_W/2-Dbar_T.

This identity does not assert a sign or payment for the complete residual. The checker retains and verifies each term. FIRST UNSUPPORTED LINE: one compatible normalized complete reference funds H(Pi|W)/2 together with signed erasure and the full terminal Fourier entropy from nonduplicated physical influence. Neither deletion capacity nor the conversion bound proves that line.

## 4. Unequal-bias boundary with an exact KL rebate

Take f=(-1)^(X0+X1+X2). Query X0, then X1 when X0=0 or X2 when X0=1, and stop. All three coordinates are essential. Put b_i=4p_i(1-p_i). The root spectral membership indicators are independent Bernoulli(b_i), because each biased literal has squares (1-b_i,b_i). Every branch changes only a scalar sign of the remaining parity, so the physical transcript is independent of S in this coherent lift.

The first deleted coordinate is fixed. Conditional on S, the two possible retained sets differ if and only if S contains coordinate 1 or 2. Thus

  e=(b_1+b_2-b_1 b_2) h2(p_0),
  (r_0,r_1,r_2)=(b_0,(1-p_0)b_1,p_0 b_2),
  C_coord=(b_1+b_2) h2(p_0),
  E KL=b_1 b_2 h2(p_0), R_phys=2.

The checker verifies the complete physical/root/terminal joint law, not just these formulas. Fair biases give e=1, C_coord=2 and common capacity 3h2(2/3)>2, showing strict improvement at fixed dimension: the last strict sign is equivalently 27>16. For p_0=epsilon, p_1=epsilon^2, p_2=3/4,

  a=3/4+4epsilon+O(epsilon^2), r=(19/4)epsilon+O(epsilon^3),
  C_coord=(3/4)epsilon log2(1/epsilon)+O(epsilon),
  a h2(r/a)=(19/4)epsilon log2(1/epsilon)+O(epsilon).

Hence common capacity/C_coord ->19/3. This follows from h2(t)=t log2(1/t)+O(t), not from numerical extrapolation. The leading KL rebate is O(epsilon^3 log(1/epsilon)). The finite rare fixture uses epsilon=1/256 exactly. This example tests unequal biases; it is not a failure of FEI or of A050's uniform theorem.

## 5. Independent review of A050 v1

A050-ACTIVE-LABEL-SCHEDULE-REPAIR@1, hash ccfae9d0cde91a86aad1a97cd77ab8fae8af4b7f5283386a89cd544cf590e4cb, is accepted at its exact uniform scope. Sections 1-3 reconstruct its entropy identification, influence telescope, normalized common-theta KL identity, endpoint/zero-reservoir repair, and conversion. Its bounded-reservoir coefficient follows by a<= (1+kappa)R and monotonicity of t h2(1/t), whose derivative is -log2(1-1/t)>=0. Its sharpness is independently reconstructed from A048's family: a=2^r+r2^(-2r-1), R=1+r2^(-2r-1), e=r(1-j_(2r+2))=r-o(1), while a h2(R/a)=r+log2(euler_number)+o(1). The channel bound gives r j_(2r+2)<=2r2^(-2r-1)/ln2 ->0. Thus the factor-one capacity is sharp in actual Boolean functions.

This review changes no A050 hypothesis or statement. The product and coordinate-resolved clauses are separately identified contributed extensions, not retroactively attributed to A050. The reviewer uses direct centered moments, physical edge counts and exact conditional rows; no A050 program is replayed. The review proves the theorem's scope, not a universal bank supply or downstream adoption.
