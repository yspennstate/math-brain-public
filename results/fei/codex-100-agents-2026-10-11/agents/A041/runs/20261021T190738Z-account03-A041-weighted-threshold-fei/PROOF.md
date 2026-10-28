# Sharp two-jump coherence in the complete quadratic reference

All logarithms are natural. The physical inputs are independent Bernoulli variables with interior, possibly unequal, biases. Write v_i=4p_i(1-p_i), v_S=product_{i in S}v_i and P(S)=Fhat(S)^2. Deterministic coordinates contract first. The groups A,B are disjoint and nonempty. Mixed labels are U,T with both parts nonempty; M=sum P and D=sum (|U|+|T|-1)P. In particular M<=D<=Delta(F). No conditional distribution is formed when M=0.

## 1. An admitted replacement for free pointwise domination

For an actual two-weight threshold, use the canonical physical A-count expansion

    h_T(k)=Fhat_B(T;N_A=k)/sqrt(v_T)
          =constant+sum_j alpha_Tj g_j(k),
    g_j=2*1{N_A>=j}-1,
    K_A(U,T)=v_T sum_j alpha_Tj^2 ghat_j(U)^2.

Define K_B in reverse, K_star=max(K_A,K_B), Z=sum K_star, Q=K_star/Z and R=P/M on the COMPLETE mixed label space. Off-support reference atoms remain present. The accepted source identity gives Z<=D+M and positivity on actual support.

Let r_A(T) count the nonzero canonical alpha_Tj, and r_B(U) count the nonzero reverse coefficients. For every occupied mixed label both counts are positive. Set r(U,T)=min(r_A(T),r_B(U)). Cauchy-Schwarz, applied before discarding the amplitude signs, gives

    P(U,T)<=r_A(T)K_A(U,T),
    P(U,T)<=r_B(U)K_B(U,T),
    P(U,T)<=r(U,T)K_star(U,T).                         (1)

For example, if r_A<=r_B, the first inequality and K_A<=K_star prove the last. No Boolean estimate is applied to K_A/Z_A or to a selected spectral fragment. A label with zero actual amplitude has no logarithmic obligation.

Writing E_mix=sum P ln(v_{U union T}/P), C_star=sum P ln(v_{U union T}/K_star), the exact identity and consequence are

    C_star=E_mix+sum P ln(P/K_star)
          <=E_mix+sum P ln r(U,T).                    (2)

This is a logarithmic coherence charge, not the false absolute-tail budget. Its generic upper bound M ln min(|A|,|B|) still depends on arity. Neither E_mix nor this extra charge has a new universal mixed-deficit payment here. Equation (2) is a valid replacement interface and is not a proof of weighted FEI+.

The mass tax also has a slightly sharper universal bound than the earlier 2D/e:

    [M ln(Z/M)]_+<=D ln 2.                            (3)

For D>0 put x=M/D in (0,1]. Then M ln(Z/M)<=D x ln(1+1/x). The derivative of x ln(1+1/x) is ln(1+1/x)-1/(1+x)>0: for y>0, ln(1+y)>y/(1+y), by integrating 1/(1+t)>=1/(1+y) over [0,y]. Thus the maximum is ln2 at x=1. The case M=0 is zero. Consequently the complete signed identity remains

    E_mix=C_star+M ln(Z/M)-M KL(R||Q)
         <=C_star+D ln2-M KL(R||Q).                   (4)

The KL is the ordinary KL under the original R, not a degree-tilted KL without its harmonic factor. Equations (1)-(4) concern a spectral reference. Physical event-conditioned total correlation and good-coordinate spectral erasure are different quantities throughout.

## 2. Factor two is necessary on actual weighted gates, at every bias

Let a,b>=2, n=a+b, and F=2*1{at most one input is zero}-1. This is an actual two-weight threshold for every real 1<w<2: use weights w on A, 1 on B and threshold aw+b-w. A single missing input loses at most w; any two missing inputs lose at least 2>w. The gate is also the symmetric count tail N>=n-1, so the accepted all-bias symmetric-threshold theorem applies.

For a nonempty set S, the normalized coefficient Fhat(S)/sqrt(v_S) is the expectation over the complementary coordinates of 2^{-|S|} times the alternating sum of the values on the S-cube. This follows by conditioning in the centered product basis. In particular it has absolute value at most 1; hence every corrected Boolean entropy summand is nonnegative, even with unequal biases.

For T=B, the A-count profile is zero up to a-2, then takes the values

    h_B(a-1)=2^{1-b},  h_B(a)=(1-b)2^{1-b}.

Its only jumps are alpha_{B,a-1}=2^{-b} and alpha_{B,a}=-b*2^{-b}. Also the full A coefficients of the two tails, divided by sqrt(v_A), are (1-a)2^{1-a} and 2^{1-a}. These finite alternating sums do not depend on any physical bias. It follows that on the complete top label

    P(A,B)/v_[n]=(n-1)^2/4^{n-1},
    K_A(A,B)/v_[n]=((a-1)^2+b^2)/4^{n-1},
    K_B(A,B)/v_[n]=(a^2+(b-1)^2)/4^{n-1}.              (5)

Thus P>K_star for every interior product law. If a=b=m,

    P(A,B)/K_star(A,B)
       =(2m-1)^2/[m^2+(m-1)^2]
       =2-1/[m^2+(m-1)^2] -> 2.                      (6)

For m=2 the ratio is 9/5. The proposed free domination P<=K_star is therefore false; even replacing its coefficient 1 by any fixed c<2 fails on actual Boolean gates. There is no numerical limit interchange: (6) is an exact rational identity for every m.

Every nonempty B-coefficient profile of this family has at most two jumps (the early branches are constant -1), and the same holds in reverse, for all interior product biases. Hence (1) also proves P<=2K_A and P<=2K_B on every mixed label, all arities and biases. Factor two is sharp in this two-jump class. By (2),

    C_star<=E_mix+M ln2<=c Delta(F)+D ln2
          <=(c+ln2)Delta(F),  c=460+80 ln2.             (7)

The last line uses the accepted symmetric-threshold theorem, nonnegativity of all corrected entropy summands, and D<=Delta. It spends one root deficit at the displayed additive rate, not two independent reserves. It retains the complete mixed entropy of the terminal B spectra. This is a reference-payment stress test on a baseline-paid family, not a new nonsymmetric FEI theorem and not a universal C_star<=K D theorem.

## 3. Aggregate overlap is also insufficient

For the fair four-input count tail N>=3 split 2+2, a mixed label with u=|U|, t=|T| has

    P=(5-2u-2t)^2/64,
    K_A=[(3-2u)^2+(2-2t)^2]/64,
    K_B=[(2-2u)^2+(3-2t)^2]/64.

Multiplicities are binom(2,u)binom(2,t). Direct summation gives

    M=17/64, D=39/64, Z_star=29/64,
    sum min(K_A,K_B)=13/64<M.

The N>=2 complement has the same squared spectra and quadratic references; the frozen search first locates that version. This disproves the separate shortcut sum min(K_A,K_B)>=M. It does NOT disprove Z_star<=D. Indeed, defining R_A=sum(|U|-1)K_A and R_B=sum(|T|-1)K_B, the exact bookkeeping identity is

    D-Z_star=R_A+R_B+sum min(K_A,K_B)-M.               (8)

Consequently high-degree reference mass can cover the overlap shortfall. The 840-case pilot has Z_star<=D throughout, maximum Z_star/D=56/61, but no general proof of (8)>=0 is claimed. This finite fact does not promote a new all-dimensional claim.

## 4. Independent reconstruction of A045's admission objection

Source: A045-EXCLUSIVE-PROFILE-OWNERSHIP-ADMISSION-OBSTRUCTION@1, statement hash ce2b1fec390b3a4c95326ac3e172d77076303d633b838c50aa8dff0382d152e2. The review uses a different route: derive the AND coefficient directly from the centered product basis and check the mean obstruction independently of all signs.

For integer W, W(W-1)>=0 pointwise, so if E W=p in (0,1), Var(W)>=p(1-p). For the AND sign on d inputs,

    P([d])=4 product_i p_i(1-p_i),
    [4^{d-2}/v_[d]minus{i}] P([d])=p_i(1-p_i)>0.

The proposed allocated variance is lambda_i p_i(1-p_i); retaining the mean and integer admission forces lambda_i>=1. Thus at least d owners are required, while degree capacity d-1 permits shared capacity within factor d/(d-1)<=3/2. The conclusion has exactly that scope: it excludes exclusive allocation, not linear degree sharing.

For fair AND3 the empty squared coefficient is 9/16 and the deleted top atom is 1/16. Renormalization gives empty mass 3/5. Every Boolean mean on the same fair cube is (j-4)/4, j=0,...,8, and none has square 3/5. Thus every phase choice fails admission. Both interior denominators and preserved means are used; deterministic inputs must contract. Verdict HOLDS at source scope, with no repair and no full-FEI consequence.

## First unsupported line

The selected signed payment C_star-M KL(R||Q)<=K D, uniformly over all actual two-weight gates and all interior biases, is still unproved. A positive C_star payment would suffice, but cannot use free atom domination, free overlap mass, exclusive integer-profile allocation, or an uncharged entropy of the jump index. The sharp two-jump replacement passes the recovered one-bit guards (r_A=1), keeps the coefficient-one pivotal failure at coefficient one, and keeps all off-support and terminal costs. The next action is to bound the actual average coherence logarithm and the diagonal tail entropy jointly from the same unused mixed-deficit ledger; no conditional spectral fragment is declared Boolean.
