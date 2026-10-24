SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T16:45:14.687605Z.

attacking: orthogonal spectral-tail conservation across an original-coordinate cut, then a diffuse-three-eigenvector balanced-cut reduction.

# account03/B12 r37 — orthogonal spectral completion exports cancelled modes into cross blocks

Programme: QFORM-DENSITY-3EIG-20260922.  
Status: **PROVED SUPPORTING MATRIX THEOREMS / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**.  
Continuity: proved only in the explicit fractional-volume exit below; not proved for the full target.

## 1. Exact target and source corrections retained

The target remains: for independent real X_i with probability densities 0<=f_i<=1 and every real symmetric A having at least three eigenvalues of absolute value >=1, prove that Q=X^TAX has a density with universal essential-supremum bound, or give a valid counterexample.

This report never rotates the random vector and never treats a spectral remainder as an independent convolution. The pointwise law-uniform quadratic-phase decay shortcut remains false; arbitrary-joint coarea, worst-fiber suprema, and independence after spectral rotation are not used. Finite computations below are consistency checks only.

The useful extra structure exploited here is genuine for the phrase “add the remaining eigenvalues”: if A0 is formed from any selected subset of eigenpairs of A and R contains all remaining eigenpairs, then A=A0+R and A0R=RA0=0. This orthogonal spectral-support relation is much stronger than a generic matrix perturbation and survives arbitrary signs and arbitrary magnitudes of the added eigenvalues.

## 2. Main theorem: spectral-completion profile conservation

Let A0,R be real symmetric n-by-n matrices satisfying

    A0 R = 0,

and let A=A0+R. Fix an ORIGINAL-coordinate cut I union J={1,...,n}. Write

    C=A[I,I],      M=A[I,J].

For a PSD matrix G, write lambda_k(G) for its kth largest eigenvalue. Singular values are decreasing and are padded by zeros past the smaller matrix dimension.

### Theorem 2.1 (`QFORM-ORTHOGONAL-SPECTRAL-COMPLETION-PROFILE-v1`)

For every k>=1 and every p,q>=1 with p+q=k+1,

    s_p(C)^2 + s_q(M)^2 >= lambda_k((A0^2)[I,I]).                 (2.1)

In particular, if lambda_k((A0^2)[I,I])>=gamma^2, then every theta in (0,1) obeys the counting inequality

    N_C(theta gamma)
      + N_M(sqrt(1-theta^2) gamma) >= k,                         (2.2)

where N_T(t)=#{j:s_j(T)>=t}.

For k=3, (2.1) is the explicit three-line conservation law

    s1(C)^2 + s3(M)^2 >= gamma^2,
    s2(C)^2 + s2(M)^2 >= gamma^2,
    s3(C)^2 + s1(M)^2 >= gamma^2.                                (2.3)

Thus an arbitrary orthogonal spectral completion cannot erase a protected k-mode baseline carrier. Any modes that disappear from the final self-compression C are quantitatively exported to the final ORIGINAL-coordinate cross block M.

### Proof

Because A0 and R are symmetric and A0R=0, transposition gives RA0=0. Hence

    A^2=A0^2+R^2 >= A0^2.                                       (2.4)

Writing A in the physical block form

    A = [ C   M ; M^T   D ],

its I,I block after squaring is the exact identity

    (A^2)[I,I] = C^2 + M M^T.                                   (2.5)

Combining (2.4) and compression preserves PSD order:

    C^2+MM^T >= (A0^2)[I,I].                                    (2.6)

Therefore

    lambda_k(C^2+MM^T) >= lambda_k((A0^2)[I,I]).                 (2.7)

For PSD X,Y, Weyl's upper eigenvalue inequality gives

    lambda_{p+q-1}(X+Y) <= lambda_p(X)+lambda_q(Y).              (2.8)

Set X=C^2, Y=MM^T and p+q-1=k. Since the eigenvalues of C^2 are s_j(C)^2 and those of MM^T are s_j(M)^2, (2.7)-(2.8) prove (2.1).

To prove (2.2), put r=N_C(theta gamma). If r>=k there is nothing to prove. Otherwise s_{r+1}(C)<theta gamma. Apply (2.1) with p=r+1 and q=k-r:

    s_{k-r}(M)^2
      >= gamma^2-s_{r+1}(C)^2
      > (1-theta^2) gamma^2.

Hence N_M(sqrt(1-theta^2)gamma)>=k-r. QED.

### Corollary 2.2: arbitrary remaining eigenvalues really are allowed

Let u_1,...,u_k be any orthonormal eigenvectors of the FINAL A with corresponding eigenvalues lambda_i, and define

    A0=sum_{i=1}^k lambda_i u_i u_i^T,
    R=A-A0.

Even with repeated eigenvalues, choose an orthonormal eigenbasis and split the eigenspaces orthogonally. Then A0R=0 exactly. Therefore (2.1)-(2.3) hold with no restriction whatsoever on the number, signs, sizes, or spectral spacing of every eigenvalue in R. In particular, “smaller” and “larger” added eigenvalues are treated on the same footing and no operator-norm smallness is imposed.

This is the matrix-level stability statement sought by this slot: the added spectral tail is not declared to be a small random quadratic error; it enters only through the positive square R^2 in (2.4).

## 3. Partner application at an actual inequality

The completed account04/B12 complementary-Schur shield proves the following on an actual physical block I. Under its notation, if the complementary compression D has three singular values at least mu and

    rho=||B12 D^{-1}||op,
    ell(rho)=(sqrt(rho^2+4)-rho)/2,

then for every symmetric hostile packet Theta,

    s3(C0) >= gamma_p := ell(rho)^2 mu.                          (3.1)

Here C0 is the resulting physical compression of the baseline matrix A0. No bound on Theta is required.

Now suppose the FINAL matrix is a spectral completion

    A=A0+R,       A0R=0,                                        (3.2)

with completely arbitrary added eigenvalues in R. Let C=A[I,I] and M=A[I,I^c]. Since

    (A0^2)[I,I]
       = C0^2 + A0[I,I^c]A0[I^c,I]
       >= C0^2,

(3.1) implies

    lambda_3((A0^2)[I,I]) >= gamma_p^2.                         (3.3)

Substituting (3.3) into Theorem 2.1 gives the concrete partner-consumed inequalities

    s1(C)^2+s3(M)^2 >= gamma_p^2,
    s2(C)^2+s2(M)^2 >= gamma_p^2,
    s3(C)^2+s1(M)^2 >= gamma_p^2.                               (3.4)

Thus the completed partner result survives arbitrary orthogonal spectral completion in a stronger form than an operator-norm perturbation statement: if the completion cancels protected modes inside the physical compression, those modes must reappear as cross-block singular directions.

For example, at theta=1/sqrt(2), if

    s1(C)<gamma_p/sqrt(2),                                      (3.5)

then (3.4) forces

    s3(M)>=gamma_p/sqrt(2).                                     (3.6)

If additionally the FINAL cross block has

    max_i (P_range(M))_ii <= 1/2,                               (3.7)

then the current fractional three-volume theorem can be applied with M0=M and E=0. It yields a continuous C0 density and

    ||p_Q||infinity
       <= 24 sqrt(3) e / [5 (gamma_p/sqrt(2))]
       = 24 sqrt(6) e/(5 gamma_p).                              (3.8)

For the partner's explicit values mu=2 and rho=1/2,

    gamma_p = 2(9-sqrt(17))/8
            = (9-sqrt(17))/4
            = 1.2192235935955849...,

so the threshold in (3.5) is 0.8621212708140693... and (3.8) is

    ||p_Q||infinity <= 26.213679558486305....                    (3.9)

This is an equation-level application of the completed account04/B12 theorem, not a copied citation.

## 4. New global structural step from only three large eigenvalues

The preceding theorem is most useful when one can force a baseline spectral-square carrier on a coordinate set. In the diffuse three-eigenvector regime this can be done at a universal scale.

Let U be the n-by-3 matrix whose columns are any three orthonormal eigenvectors of A with eigenvalues lambda_1,lambda_2,lambda_3 satisfying |lambda_i|>=1. Let u_j^T denote row j of U and assume the selected three-dimensional eigenspace is coordinate-diffuse in the explicit sense

    max_j ||u_j||_2^2 <= 1/256.                                 (4.1)

### Lemma 4.1 (balanced physical cut)

Under (4.1), there is an ORIGINAL-coordinate set I, with J=I^c, such that

    (1/4) I_3 <= U_I^T U_I <= (3/4) I_3,                       (4.2)

and therefore also

    (1/4) I_3 <= U_J^T U_J <= (3/4) I_3.                       (4.3)

#### Proof

Choose independent Bernoulli xi_j in {0,1} with probability 1/2 and set

    S=sum_j (xi_j-1/2) u_j u_j^T.

For a fixed unit vector x in R^3, put a_j=(u_j^T x)^2. Then

    sum_j a_j=1,
    0<=a_j<=1/256,
    sum_j a_j^2 <= 1/256.                                      (4.4)

Hoeffding's inequality gives

    P(|x^T S x|>=t)
      <= 2 exp(-2 t^2 / sum_j a_j^2)
      <= 2 exp(-512 t^2).                                      (4.5)

Take an epsilon=1/8 net N of S^2 with |N|<=(1+2/epsilon)^3=17^3=4913. The standard quadratic-form net estimate gives

    ||S||op <= (1-2epsilon)^(-1) max_{x in N}|x^T Sx|
            = (4/3) max_{x in N}|x^T Sx|.                      (4.6)

Thus ||S||op<=1/4 whenever every net point has |x^TSx|<=3/16. By the union bound and (4.5), the failure probability is at most

    2*4913*exp[-2(3/16)^2/(1/256)]
      =9826 e^{-18}
      =0.0001496497809715463... <1.                             (4.7)

Hence at least one realization satisfies ||S||op<=1/4. Taking I={j:xi_j=1},

    U_I^T U_I = (1/2)I_3 + S,

which proves (4.2); (4.3) follows from U_J^T U_J=I_3-U_I^TU_I. QED.

### Theorem 4.2 (`QFORM-DIFFUSE-3EIG-BALANCED-CUT-SPLITTER-v1`)

Under the target spectral hypothesis and (4.1), there is an ORIGINAL-coordinate cut I,J such that, with

    a=1/(2 sqrt(2)),
    C_I=A[I,I], C_J=A[J,J], M=A[I,J],

one has

    N_{C_I}(a)+N_M(a)>=3,
    N_{C_J}(a)+N_M(a)>=3.                                      (4.8)

Equivalently, if q=N_M(a), then BOTH self blocks contain at least 3-q singular values >=a. Therefore exactly one of the following structural outcomes occurs:

1. q>=3: the actual cross block has s3(M)>=a;
2. q=2: both self blocks have at least one singular value >=a;
3. q=1: both self blocks have at least two singular values >=a;
4. q=0: both self blocks have at least three singular values >=a.

Every additional eigenvalue of A, of either sign and arbitrary magnitude, is already included in this conclusion.

#### Proof

Define the selected spectral core

    A0=U Lambda U^T,
    Lambda=diag(lambda_1,lambda_2,lambda_3),

and R=A-A0. Then A0R=0. By (4.2), the three nonzero eigenvalues of

    (A0^2)[I,I]=U_I Lambda^2 U_I^T

coincide with those of

    Lambda U_I^T U_I Lambda,

whose least eigenvalue is at least 1/4 because |lambda_i|>=1. Thus

    lambda_3((A0^2)[I,I])>=1/4.                                (4.9)

The same argument with J gives the same bound there. Apply Theorem 2.1 with k=3, gamma=1/2 and theta=1/sqrt(2); then both thresholds in (2.2) equal

    theta gamma=sqrt(1-theta^2)gamma=1/(2sqrt(2))=a.

This proves (4.8). QED.

## 5. Applying the newest fractional-volume theorem

In outcome 1 of Theorem 4.2, suppose in addition that the FINAL cross range satisfies

    max_i(P_range(M))_ii <= 1/2.                               (5.1)

The current volume-stability theorem applies directly with baseline M0=M and perturbation E=0. Since s3(M)>=a=1/(2sqrt(2)), it yields a continuous density vanishing at infinity and

    ||p_Q||infinity
      <= 24sqrt(3)e/(5a)
      = 48sqrt(6)e/5
      = 63.920673185321604... <64.                              (5.2)

Thus the bare three-large-eigenvalue premise is reduced, in the coordinate-diffuse selected-eigenspace regime, to explicit survivors:

- a high-leverage cross range (the hub/high-leverage branch), or
- q<=2 substantial cross directions together with the complementary self-block reserves in (4.8).

This is stronger than saying merely that a diffuse spectral core exists: arbitrary nonseparable additional spectrum has already been propagated through the matrix identity A^2=A0^2+R^2. The remaining cases are exactly mixed low-cross-rank/high-self-rank geometries, compatible with the fleet's grouped-bank/hub/rank-two work.

If (4.1) fails, then the selected large eigenspace has an explicit heavy ORIGINAL coordinate with leverage >1/256. That is the complementary localized/hub survivor. Hence Theorem 4.2 plus the heavy-row alternative gives a genuine quantitative structural split directly from the three selected large eigenvectors.

## 6. Why this does not solve full QFORM

The theorem does not yet bound the high-leverage-row branch, the high-leverage cross-range branch, or the mixed q=1,2 cases in (4.8). Nor does it provide a dimension-free density receiver from large self singular values alone when the corresponding coordinate bank is large. Those are the first unpaid implications after this run.

In particular, outcome q=0 gives three strong singular values on each self block, but invoking the original conjecture separately on those large banks would be circular. Likewise q=1,2 require a valid mixed self/cross analytic receiver, not an assertion that singular-value counts add as independent smoothing factors.

The full target therefore remains OPEN / NOT PROVED / NOT DISPROVED.

## 7. Finite checks

A deterministic Python checker in this run tested 10,000 random symmetric spectral completions A=A0+R with A0R=0, arbitrary mixed signs and remainder magnitudes spanning 1e-4 to 1e4. Across 28,738 admissible profile inequalities (2.1), it found zero violations; the smallest floating-point margin was 0.01557366338525279.

For the balanced-cut lemma, a 1024-by-3 Sylvester-Hadamard frame has exact row leverage 3/1024=0.0029296875<1/256. In 5,000 random Bernoulli partitions, all 5,000 had ||U_I^TU_I-(1/2)I||op<=1/4; the largest observed deviation was 0.109146152567772 and the smallest observed lambda_min(U_I^TU_I) was 0.3908538474322281. These are consistency checks only; the proof is (4.4)-(4.7).

## 8. Source pins

Fresh brain control initially resolved to `4e19b067da9367f9db2bd5ed4f6dbb7d3a860f1f`; prepublication refresh resolved to `d708fb9bc4d3798da196b908427256e3a012eba2`. OWNER CONTROL remained `2026-09-22.15`; programme revision remained `2026-09-22.5`. The live correction inbox blob remained `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

Completed designated partner actually applied: `yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Newest fractional-volume theorem actually applied: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Execution remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval and writes are not authenticated native learned-memory ingestion.

## 9. Next mathematical step

Attack the mixed splitter outcomes q=1,2 without losing original-coordinate product structure. The most promising precise target is a receiver combining r strong self singular directions with 3-r strong cross singular directions at a common universal scale, for r=1,2, while allowing arbitrary within-bank quadratic curvature and affine terms. A proof of that mixed receiver, together with the high-leverage hub exits, would convert Theorem 4.2 into a substantially more exhaustive diffuse-case compiler.