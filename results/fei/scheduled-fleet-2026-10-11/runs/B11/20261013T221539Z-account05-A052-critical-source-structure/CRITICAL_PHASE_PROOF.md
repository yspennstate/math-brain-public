# Critical-source restriction through Boolean row phases

All cubes are uniform and finite; entropy is in bits. Let f be a Boolean sign on n essential coordinates, A a nonempty proper queried block of a coordinates, and C its complement. Put w_t(x)=hat(f_x)(t), q_t=E_x w_t(x)^2, omitting q_t=0. Let nu_t be the squared Walsh spectrum of w_t/sqrt(q_t) on A. Then

    B_A=sum_t q_t H(nu_t),  I_A=sum_t q_t E_nu_t |U|,
    L_A=B_A+J_A,  H(f)-K I(f)=L_A-K I_A+E_x D_K(f_x).

Here J_A=sum_t q_t E z_t log2 z_t, z_t=w_t^2/q_t. Define c_t=E(z_t-1)^2, C_A=sum_t q_t c_t and Gamma_A=sum_t q_t log2(1+c_t). These are signed-row quantities: the fourth moments are computed after summing signed Fourier amplitudes. Jensen under density z_t proves J_A<=Gamma_A; Jensen across t gives Gamma_A<=log2(1+C_A).

## 1. Exact zero-channel exclusion

Suppose all physical children have identical squared spectra. Equivalently C_A=Gamma_A=J_A=0. Each positive row has w_t(x)^2=q_t for all x, so

    h_t(x)=w_t(x)/sqrt(q_t)

is an actual Boolean sign on a<n coordinates. Parseval gives nu_t=hat(h_t)^2. Hence

    B_A=sum_t q_t H(h_t), I_A=sum_t q_t I(h_t).

If FEI(K) holds for every Boolean function on fewer than n essential coordinates, H(h_t)<=K I(h_t). Therefore B_A<=K I_A. The physical children f_x also have fewer essential coordinates, so their deficits are nonpositive. The exact deficit identity now gives D_K(f)<=0.

Consequently a least-essential-dimension violating witness D_K(f)>0, K>=0, cannot have ANY nonempty proper isospectral block. In particular every such block must have C_A>0. This is stronger than the collision inequality alone, which leaves B_A unpriced when Gamma_A=0.

The h_t are Boolean functions, but need not be physical descendants of f. Their admission follows from dimension minimality among ALL Boolean K-violators; physical-descendant ratio criticality does not supply that admission. The function f=b(x1,x2)b(x3,x4), b=(-1)^(x1 x2), has R=2, all physical children R<=2, and a proper full-factor block with C_A=0, B_A=2, I_A=1. It is an exact counterexample to extending the exclusion to nonstrict physical ratio criticality alone. No component-pruning or virtual-descendant assumption enters the dimension-minimal proof.

## 2. Quantitative near-isospectral restriction

For arbitrary rows define h_t=sign(w_t), with sign(0)=1, and

    tau_t=||w_t/sqrt(q_t)-h_t||_2,
    eta_t=min(1,tau_t), eta_bar=sum_t q_t eta_t.

These phases are again actual lower-dimensional Boolean functions. Let rho_t be their squared Walsh laws. For unit vectors u,v, Cauchy--Schwarz gives TV(u^2,v^2)<=||u-v||_2. Orthogonality of the normalized Walsh transform therefore gives TV(nu_t,rho_t)<=eta_t. Also

    tau_t^2=E (sqrt(z_t)-1)^2 <= E(z_t-1)^2=c_t,
    eta_bar<=sqrt(C_A).

Let d=2^a and define psi_a(s)=h2(s)+s log2(d-1) for 0<=s<=1-1/d, and psi_a(s)=a above that point. This is concave, nondecreasing, continuous. The maximal-coupling entropy estimate is |H(P)-H(Q)|<=h2(t)+t log2(d-1), t=TV(P,Q): under a coupling with mismatch probability t, condition on the mismatch event; when mismatched a variable has at most d-1 choices. Apply the argument in both directions. For a larger upper bound on t use psi_a, capped by the trivial entropy range a. Expectations of a function in [0,a] differ by at most a TV, so

    H(nu_t)<=H(rho_t)+psi_a(eta_t),
    I(h_t)<=E_nu_t |U|+a eta_t.

Assume FEI(K) below dimension n, K>=0. Weighting its application to h_t yields

    B_A<=K I_A + sum_t q_t[psi_a(eta_t)+K a eta_t]
         <=K I_A+psi_a(eta_bar)+K a eta_bar.

If f is a dimension-minimal K-violator, physical children have D_K<=0. Thus, for EVERY proper nonempty block,

    0<D_K(f)<=Gamma_A+psi_a(eta_bar)+K a eta_bar.       (*).

In particular, if C_A<=1/4 then sqrt(C_A)<=1/2<=1-1/d, and

    D_K(f)<=log2(1+C_A)+h2(sqrt(C_A))
             +sqrt(C_A) log2(2^a-1)+K a sqrt(C_A).     (**)

There is no floating-point step, non-Boolean phase relaxation, or hidden terminal discard. Formula (*) retains the actual nonpositive mean child deficit in its derivation. The endpoint C_A=0 recovers the exact exclusion.

## 3. Honest gap and implication

These inequalities exclude zero channel and quantify how close a dimension-minimal witness can be to it at a specified deficit, block size and threshold. Their error grows with a and K and may exceed the deficit. They do NOT prove that some affordable block exists, or that all critical witnesses have uniformly bounded H/I. The first unsupported line remains a dimension-independent K and block-selection argument controlling this phase-approximation error plus Gamma_A below D_K(f), or directly forcing B_A+Gamma_A<=K I_A. Replacing signed convolutions by absolute sums loses the useful cancellations. Counting Boolean row phases as physical descendants would invalidate the ratio-critical version.
