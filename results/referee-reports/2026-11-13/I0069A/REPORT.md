RESOLVED_IN_LITERATURE

# I0069: extrapolation of stochastic maximal regularity

Research date: 13 November 2026. This classification concerns the literal assertion of extrapolation to **every** r>2: it is already false in the literature. It does not claim that every weaker, coefficient-dependent extrapolation question in Problem 3 has been settled. The requested literature review and the audit connecting the known counterexample to the survey's precise definition are recorded below. No new theorem is claimed.

## Statement and source identification

Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, **Nonlinear Differential Equations and Applications NoDEA 32(6), article 123 (2025), 150 pages**, published 1 September 2025, [DOI 10.1007/s00030-025-01090-2](https://doi.org/10.1007/s00030-025-01090-2).

The version of record has Problem 3 on article **page 129 of 150**. Its standing assumptions are on p. 26, Definition 3.6 on p. 27, Definition 3.7 on pp. 27–28, and Definition 3.8 and Remark 3.9 on p. 28. The institutional download adds a cover page: article p. 129 is PDF page 130. The saved plain text preserves page boundaries with form feeds.

The corresponding preprint is [arXiv:2501.18561v5](https://arxiv.org/abs/2501.18561v5), submitted 27 August 2025 at 08:29:47 UTC, 103 pages. In v5, Problem 3 is on p. 92; the standing assumptions and strong solution definition are on p. 19 and Definitions 3.7–3.8 on p. 20. Do not mix these page numbers or the preprint's author-year bibliography keys with the published numbering.

Reference **[29]**, printed on article p. 135, is Sebastian Bechtel and Mark C. Veraar, *An extrapolation result in the variational setting: improved regularity, compactness, and applications to quasilinear systems*, **arXiv:2311.01271 (2023)**. Its current preprint is [v2, 3 July 2025](https://arxiv.org/abs/2311.01271v2); the title-page date is 4 July 2025. It is now published in **Stochastics and Partial Differential Equations: Analysis and Computations 13(4), 2000–2038 (2025)**, online 11 July 2025, [DOI 10.1007/s40072-025-00378-9](https://doi.org/10.1007/s40072-025-00378-9). The survey still cites its 2023 preprint. This is [BV23] in survey v5.

## Exact meaning of the survey's hypothesis

The following is a mathematical restatement of Definitions 3.6–3.8, including their quantifiers.

Fix the filtered probability space and a cylindrical Brownian motion W on the noise Hilbert space U. The Banach spaces X_0 and X_1 have UMD and type 2, and X_1 embeds continuously and densely into X_0. Write X_theta=[X_0,X_1]_theta for complex interpolation; in particular X_{1/2} is a complex interpolation space, not a real trace space. The real trace spaces elsewhere in the survey are X_{theta,p}=(X_0,X_1)_{theta,p}. In generator examples X_1=D(A) with an equivalent graph norm, but the standing definition starts with the embedded couple and the bounded maps

    A : X_1 -> X_0,
    B : X_1 -> gamma(U,X_{1/2}).

Here A and B are deterministic and independent of time. The survey says explicitly in §3.6 that it concentrates on this setting. The more general (t,omega)-dependent hypotheses in the critical-spaces papers and in [29] should not be silently inserted into the survey's standing definition. A deterministic example is, of course, also admissible in those broader settings.

For a finite-rank operator R=sum_j h_j tensor x_j, with (h_j) orthonormal in U, the gamma-radonifying norm is

    ||R||_gamma(U,X) = (E' ||sum_j gamma_j x_j||_X^2)^(1/2),

where gamma_j are independent standard real Gaussians on an auxiliary probability space. Completion gives gamma(U,X). This is the Hilbert–Schmidt norm when X is Hilbert. In L^q and Sobolev examples it is equivalent to the appropriate spatial square-function norm; it must not be replaced by the operator norm from U to X.

For p>=2 the admissible powers are kappa in [0,p/2-1) union {0}. Thus kappa=0 is the only choice at p=2, and **SMR^bullet_{p,0} is unweighted**. The translated weight is w_kappa^a(t)=(t-a)^kappa.

For every finite T>0, every deterministic a in [0,T], every stopping time tau with a<=tau<=T, and every progressively measurable pair

    f in L^p(Omega; L^p(a,tau,w_kappa^a; X_0)),
    g in L^p(Omega; L^p(a,tau,w_kappa^a; gamma(U,X_{1/2}))),

the zero-initial-value equation

    du + A u dt = f dt + (B u + g) dW,    u(a)=0                 (1)

must have a unique strong solution in L^p(Omega;L^p(a,tau,w_kappa^a;X_1)), satisfying

    ||u||_{L^p(Omega;L^p(a,tau,w_kappa^a;X_1))}
       <= C_T (||f||_{L^p(Omega;L^p(a,tau,w_kappa^a;X_0))}
             + ||g||_{L^p(Omega;L^p(a,tau,w_kappa^a;gamma(U,X_{1/2})))}) .   (2)

C_T is independent of a,tau,f,g. This is SMR_{p,kappa}. A strong solution is progressively measurable, lies almost surely in C([a,tau];X_0) intersect L^2(a,tau;X_1), and satisfies the integrated Itô equation in X_0 almost surely simultaneously for t in [a,tau]. Definition 3.7 refers to (3.8); the immediately preceding equation (3.11) and Definition 3.8 make the intended zero initial condition explicit.

The bullet adds the following requirements on every deterministic [a,b] subset [0,T], with constants uniform in a,b and in the data:

- If p>2, for each theta in (0,1/2),

      ||u||_{L^p(Omega;H^{theta,p}(a,b,w_kappa^a;X_{1-theta}))}
        <= C_{T,theta}(||f||_{L^p(Omega;L^p(a,b,w_kappa^a;X_0))}
                    + ||g||_{L^p(Omega;L^p(a,b,w_kappa^a;gamma(U,X_{1/2})))}) .

  H^{theta,p} is the time Bessel-potential space. No endpoint theta=1/2 is asserted.

- If p=2, kappa=0, replace that requirement by

      ||u||_{L^2(Omega;C([a,b];X_{1/2}))}
        <= C_T (||f||_{L^2(Omega;L^2(a,b;X_0))}
              + ||g||_{L^2(Omega;L^2(a,b;gamma(U,X_{1/2})))}) .

These are local-in-time properties quantified over all finite T, with C_T allowed to grow with T. They do not demand one constant for T=infinity. Remark 3.9 stresses that uniformity over starting and ending times is an extra requirement compared with the earlier critical-spaces paper.

## What the literature already decides

Brzeźniak and Veraar, *Is the stochastic parabolicity condition dependent on p and q?*, **Electronic Journal of Probability 17, paper 56 (2012), 1–24**, [DOI 10.1214/EJP.v17-2186](https://doi.org/10.1214/EJP.v17-2186), [arXiv:1104.2768v3](https://arxiv.org/abs/1104.2768v3), Theorem **4.1**, pp. **13–14**, consider

    du = Delta u dt + 2(alpha D + beta |D|)u dW

on the torus. Their sufficient condition is

    2 alpha^2 + 2 beta^2(p-1) < 1.                              (3)

Theorem 4.1(ii) proves failure above this threshold, including divergence of the L^p(Omega times time;H^{s+2,2}) norm for p>=2. Theorem **5.1**, pp. **16–17**, gives the corresponding H^{s,q} result. These are autonomous, deterministic operators, and A=-Delta is positive self-adjoint. Its H^infinity calculus is not the issue. In the survey this paper is **[43]**, and §3.6.3, article p. **36**, already discusses its higher-moment obstruction.

Reference [29] is particularly explicit: its v2 introduction, p. **2**, says that unrestricted extrapolation with general nonzero B is false because L^p(Omega) integrability may fail, citing that 2012 paper. Its positive result is Theorem **1.2**, p. **3**, with the more detailed Theorem **2.2**, pp. **6–7**. On a Hilbert Gelfand triple V -> H -> V*, A(t,omega):V->V* and B(t,omega):V->L_2(U,H) are progressively measurable and uniformly bounded. Under symmetry of A and

    Re <Av,v> - (1/2)||Bv||_{L_2(U,H)}^2
       >= lambda ||v||_V^2 - M ||v||_H^2,                      (4)

it gives L^r(Omega times time;V), the corresponding H^{theta,r} time regularity, and trace continuity for r in [2,p_0], with p_0>2 depending on the coercivity/boundedness parameters. With X_0=V*, X_1=V and X_{1/2}=H, these are the relevant SMR^bullet estimates. Time restriction/translation and stopping give the finite-interval formulation above. This does not establish all r>2. Their Problem **1.5**, p. **5**, asks about removing symmetry.

Thus the all-r alternative in Problem 3 has a known negative answer. The report does not assign a precise theorem to the phrase “some large range”: it does not specify a range or whether its size can depend on A,B. A universal range (2,2+epsilon) independent of the pair is also impossible, as the audit below shows. A pair-dependent small interval is known in the symmetric variational setting; a general replacement theorem is a different question.

## Audit in the exact zero-initial-data definition

The printed counterexample uses nonzero initial data. Here is a direct forcing check of the same, already-known mechanism; this removes that possible mismatch without asserting a new result.

Take X_0=l^2(N;R), A e_n=lambda_n e_n with lambda_n=n^2, X_1=D(A) with norm ||x||_{X_1}=||Ax||_2, and X_{1/2}=D(A^{1/2}) with norm ||A^{1/2}x||_2. These are Hilbert spaces; A is invertible and positive self-adjoint with bounded H^infinity calculus of angle zero. Set U=R and

    Bx = sigma A^{1/2}x,       0<sigma^2<2.                    (5)

Identifying gamma(R,X_{1/2}) with X_{1/2}, ||Bx||_{X_{1/2}}=|sigma| ||x||_{X_1}, so B has exactly the mapping property required in the survey. This is the spectral form of the 2012 example with alpha=0 and 2 beta=sigma (one may also restrict the periodic Laplacian to mean-zero even functions).

First, (A,B) belongs to SMR^bullet_{2,0}. To apply the survey's Theorem **3.17** (article p. **33**, v5 p. **24**), take V=D(A), H=D(A^{1/2}), and identify V* with l^2 using H as pivot. Under this identification the pairing is <z,v>=sum_n lambda_n z_n v_n. Consequently,

    <Av,v> - (1/2)||Bv||_H^2
       = (1-sigma^2/2)||Av||_2^2.

This is coercive with lambda=1-sigma^2/2>0 and M=0. The variational theorem supplies existence, uniqueness, estimate (2), and the p=2 bullet estimate, uniformly under deterministic time translations and stopping. The norm choices are legitimate equivalent graph norms since A>=I.

Now fix any T>0. For n sufficiently large put h_n=1/lambda_n<T and choose the deterministic progressively measurable data

    f_n(t)=lambda_n 1_(0,h_n)(t)e_n,      g_n=0,      u_n(0)=0.

The unique scalar coordinate y_n of u_n solves

    dy_n=-lambda_n y_n dt + lambda_n 1_(0,h_n)dt
                         + sigma sqrt(lambda_n)y_n dW.

It is nonnegative, has finite moments of every finite order on finite intervals, and

    E y_n(h_n)=1-e^(-1)=:m>0.

For t>=h_n, independence of future Brownian increments gives, for every r>2,

    E |y_n(t)|^r = E |y_n(h_n)|^r exp(c_r lambda_n(t-h_n)),
    c_r = -r + r(r-1)sigma^2/2.

Jensen gives E |y_n(h_n)|^r >= m^r. For c_r>0, therefore,

    ||f_n||_{L^r(Omega times (0,T);X_0)}^r = lambda_n^(r-1),

    ||u_n||_{L^r(Omega times (0,T);X_1)}^r / ||f_n||_{L^r}^r
       >= (m^r/c_r)[exp(c_r(lambda_n T-1))-1] -> infinity.    (6)

At c_r=0 the same ratio is at least m^r(lambda_n T-1), again unbounded. Hence

    (A,B) is not in SMR_{r,0}, and therefore not in SMR^bullet_{r,0},
    whenever r >= 1+2/sigma^2.                                (7)

For example sigma=1 gives SMR^bullet_{2,0} but failure for every r>=3, including r=4. This contradicts the unrestricted implication inside the survey's stated autonomous Hilbert setting. It consequently also contradicts that implication in any broader setting allowing (t,omega) dependence.

For any prescribed r>2, one can choose 2/(r-1)<=sigma^2<2, so there is no pair-independent epsilon>0 allowing extrapolation from p=2 to all 2<r<2+epsilon. This does not contradict [29]: its interval depends on the coercivity margin, which tends to zero as sigma^2 tends to 2.

The same exponent is obtained a second way from Itô's formula for |y|^r after the forcing stops: d E|y|^r/dt=[-r+(r(r-1)/2)sigma^2]lambda_n E|y|^r. Substitution sigma=2 beta recovers exactly (3) with alpha=0. No numerical experiment is needed.

For an independent check of the p=2 premise, set delta=2-sigma^2, z=Au, v=A^{1/2}u and h=A^{1/2}g. Itô's formula, first in a finite spectral truncation and stopped to make the martingale integrable, gives

    ||v(t)||^2 + delta integral_a^t ||z||^2
       = integral_a^t [2<z,f>+2 sigma<z,h>+||h||^2] + M_t,
    M_t=2 integral_a^t <v,sigma z+h> dW.

Young's inequality with parameter delta/4 in each cross term yields

    E||v(t)||^2 + (delta/2) E integral_a^t ||z||^2 <= K,
    K=(4/delta) E integral_a^b ||f||^2
        +(1+4 sigma^2/delta) E integral_a^b ||h||^2.

If C_1 is a universal L^1 BDG constant, the same identity and 2 C_1 xy <= x^2/2+2 C_1^2 y^2 give

    E sup_[a,b] ||v||^2
       <= (2+16 C_1^2 sigma^2/delta)K
           +8 C_1^2 E integral_a^b ||h||^2.

These constants do not depend on the spectral cutoff, a,b or stopping time. Differences of truncated solutions satisfy the same bounds with differences of the data; passing to the limit supplies the required solution and uniqueness for arbitrary progressively measurable L^2 data. This independently checks both the space estimate and the p=2 bullet estimate used above. The strictly positive margin delta is essential.

There is also no general all-r theorem on a fixed L^q space with q>2. For example take the periodic Laplacian on mean-zero L^q, X_1=H^{2,q}, and B=sigma |D|. At a fixed p_0>2, choose sigma nonzero but small enough for the printed perturbation criterion to apply to (A,0). Then (A,B) has SMR^bullet at p_0. The same single Fourier-mode forcing has input and output spatial norms proportional to 1 and lambda_n, respectively, uniformly in n; (6) excludes every sufficiently large r. This is the same printed parabolicity obstruction combined with the printed small-perturbation theorem. “Small B at one p” must not be interpreted as a bound that works simultaneously for all p.

## Remaining literature checks

Page numbers below refer to the specified saved arXiv version unless a journal/article page is explicitly given. The relevant sections, theorem statements and proof arguments were read; this is not a claim to have read every application in the long critical-spaces papers.

### Positive and negative settings

| Setting | What is established | Exact checked location |
|---|---|---|
| Autonomous deterministic A, B=0, X_0 UMD of type 2 | One unweighted stochastic convolution bound at p>=2 extrapolates to every r>2 and weights kappa in [0,r/2-1). No H^infinity-calculus assumption is needed for this extrapolation implication. | Survey Theorem 3.12, article p. 31 / v5 p. 22; Lorist–Veraar Theorem 8.2, v5 pp. 41–42. With the deterministic maximal regularity and transference step, this gives the bullet version. |
| Autonomous analytic A, B=0, X_0 Hilbert | SMR^bullet holds for all r>=2 and admissible powers, without assuming bounded H^infinity calculus. | Survey Theorem 3.13, article pp. 31–33 / v5 pp. 22–24. |
| Autonomous A, B=0, X_0 a closed subspace of L^q, q>=2, shifted A with bounded H^infinity calculus of angle <pi/2 | SMR^bullet for every r>2, kappa in [0,r/2-1); r=2 additionally when q=2. | Survey Theorem 3.14, article p. 32 / v5 p. 23; NVW Theorems 1.1–1.2, below. |
| Autonomous deterministic A, unrestricted nonzero B, even Hilbert and self-adjoint A | Extrapolation to every r>2 is false. | Brzeźniak–Veraar Theorem 4.1; exact forcing audit (5)–(7) above. |
| Progressively measurable (t,omega)-dependent A,B in a coercive symmetric Hilbert variational problem | An interval [2,p_0] with p_0>2; not every r. | Bechtel–Veraar [29], Theorems 1.2 and 2.2, v2 pp. 3, 6–7. |
| (t,omega)-dependent second-order systems with spatial Hölder regularity, real diagonal transport noise, and the stated stochastic ellipticity | All r>2, q>=2 and admissible powers, plus r=q=2. These are structural sufficient conditions, not an implication for arbitrary pairs from one exponent. | Agresti–Veraar periodic-systems Theorems 5.2–5.3, v4 p. 12, under Assumption 5.1, pp. 11–12. |
| General merely measurable time-dependent A, B=0 | No unrestricted extrapolation: already the deterministic forcing estimate can fail at a prescribed r>2. Deterministic variational theory still supplies a coefficient-dependent interval around 2. | Bechtel–Mooney–Veraar Theorems 2.2 and 2.5, v2 pp. 3 and 6. |

The last row concerns the variational realization X_0=H^{-1}, X_1=H^1 and complex uniformly elliptic divergence-form coefficients. Do not confuse it with regularity on X_0=L^2, which is a separate Lions problem, or with the autonomous theorem. Portal–Veraar's reference-operator theorem supplies the stochastic p=2 bound in this Hilbert variational scale. Taking g=0 imports the deterministic failure at the target r into SMR. The letter B in the deterministic counterexample paper denotes a matrix of drift coefficients, not a stochastic multiplicative-noise operator.

### Papers read and the limits of their conclusions

1. **Emiel Lorist and Mark Veraar**, *Singular stochastic integral operators*, **Analysis & PDE 14(5), 1443–1507 (2021)**, [arXiv:1902.10620v5, 13 June 2022](https://arxiv.org/abs/1902.10620v5). Theorem **1.3**, p. **6**, is the autonomous p-extrapolation result in the half-domain scale. The more general Theorem **8.2**, pp. **41–42**, covers complex and real interpolation scales, with arbitrary A_{r/2} weights and a constant bounded by C[w]_{A_{r/2}}^{max(1/2,1/(r-2))}. Theorems **1.1–1.2**, pp. **4–5**, give the Hörmander/Dini stochastic Calderón–Zygmund tools. Theorem **8.15**, pp. **48–49**, proves extrapolation for deterministic nonautonomous evolution families under Acquistapace–Terreni assumptions on A and A*, plus a compatible interpolation scale. It is not a theorem for arbitrary progressively measurable coefficients or general B u noise.

2. **Jan van Neerven, Mark Veraar and Lutz Weis**, *Stochastic maximal L^p-regularity*, **Annals of Probability 40(2), 788–812 (2012)**, [DOI 10.1214/10-AOP626](https://doi.org/10.1214/10-AOP626), [arXiv:1004.1309v4](https://arxiv.org/abs/1004.1309v4). Theorem **1.1**, reprint p. **2** / journal p. **789**, gives the H^infinity-calculus stochastic convolution estimate on L^q, q>=2, for p>2 and additionally p=q=2. Theorem **1.2**, reprint p. **4** / journal p. **791**, gives time regularity and the maximal trace estimate under invertibility. These papers initially use a half-order solution gain from noise valued in X; the survey shifts the scale to noise in gamma(U,X_{1/2}) and solution in X_1. Section **6**, reprint pp. **20–21**, explains the endpoint obstruction: p=2 cannot be added for general q>2. The target range r>2 in Problem 3 is deliberate.

3. **Van Neerven–Veraar–Weis**, *Maximal L^p-regularity for stochastic evolution equations*, **SIAM Journal on Mathematical Analysis 44(3), 1372–1414 (2012)**, [arXiv:1101.3504v4](https://arxiv.org/abs/1101.3504v4). Theorem **4.5**, preprint p. **16**, requires the explicit smallness inequality K_p^* L_F+K_p^diamond L_B<1. It does not remove arbitrary leading-order B. Its constants depend on p.

4. **Pierre Portal and Mark Veraar**, *Stochastic maximal regularity for rough time-dependent problems*, **Stochastics and Partial Differential Equations: Analysis and Computations 7, 541–597 (2019)**, [DOI 10.1007/s40072-019-00134-w](https://doi.org/10.1007/s40072-019-00134-w), [arXiv:1810.01183v3](https://arxiv.org/abs/1810.01183v3). Theorem **3.9**, pp. **13–14**, transfers SMR from a reference operator A_0 to a progressively measurable A(t,omega), **assuming pathwise deterministic maximal regularity with a uniform constant at the same exponent**. This does not infer that assumption at all other exponents. Theorem **4.5**, pp. **24–25**, handles higher-order systems with rough time dependence and suitably small highest-order stochastic perturbations. Theorem **5.3**, pp. **26–27**, treats spatially constant principal coefficients with diagonal real transport noise; Theorem **5.4**, pp. **27–28**, treats the spatially varying case in the L^p(L^p) setting under its hypotheses. These structural results do not contradict the |D| example.

5. **Agresti–Veraar**, *Nonlinear parabolic stochastic evolution equations in critical spaces Part I. Stochastic maximal regularity and local existence*, **Nonlinearity 35(8), 4100–4210 (2022)**, [arXiv:2001.00512v5](https://arxiv.org/abs/2001.00512v5). Assumptions **3.1–3.2**, preprint p. **18**, explicitly permit uniformly bounded, strongly progressively measurable A(t,omega), B(t,omega) on a common domain; their endpoint p=2 framework takes Hilbert spaces. Definitions **3.4–3.5**, p. **19**, are the earlier finite-horizon SMR and bullet definitions. Theorem **3.7**, p. **20**, gives autonomous H^infinity-calculus examples. Proposition **3.8**, p. **21**, transfers a space estimate to the bullet property at the **same** exponent, given a reference pair with bullet regularity. It is not extrapolation in p.

6. **Agresti–Veraar**, *Nonlinear parabolic stochastic evolution equations in critical spaces Part II: Blow-up criteria and instantaneous regularization*, **Journal of Evolution Equations 22, article 56 (2022), 96 pages**, [arXiv:2012.04448v4](https://arxiv.org/abs/2012.04448v4), 83 preprint pages. Proposition **6.8**, preprint pp. **66–67**, adds weights and bootstraps solution regularity **assuming** SMR at the target exponents and scales. Pathwise instantaneous regularization does not establish the missing moment estimates for the linear solution operator. This distinction matters because the obstruction above is precisely in L^r(Omega).

7. **Agresti–Veraar**, *Stability properties of stochastic maximal L^p-regularity*, **Journal of Mathematical Analysis and Applications 482(2), 123553 (2020), 35 pages**, [arXiv:1901.08408v2](https://arxiv.org/abs/1901.08408v2). Theorem **3.6**, preprint p. **9**, gives the H^infinity sufficient condition under the stochastic R-boundedness assumption; Theorem **7.9**, pp. **25–27**, gives equivalence with power-weighted estimates for a fixed exponent. These are B=0 results and do not establish general pair extrapolation.

8. **Agresti–Veraar**, *Stochastic maximal L^p(L^q)-regularity for second order systems with periodic boundary conditions*, **Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 60(1), 413–430 (2024)**, [DOI 10.1214/22-AIHP1333](https://doi.org/10.1214/22-AIHP1333), [arXiv:2106.01274v4](https://arxiv.org/abs/2106.01274v4). Theorem **1.2**, p. **2**, and the stronger Theorems **5.2–5.3**, p. **12**, permit (t,omega) dependence under Assumption 5.1. The drift can be a system, but the principal transport noise acts diagonally in the components. Theorem **3.2**, pp. **6–7**, gives a perturbation criterion C_det C_A+C_sto C_B<1 at each relevant p and weight. It cannot justify removing arbitrary B uniformly in p.

9. **Sebastian Bechtel, Connor Mooney and Mark Veraar**, *Counterexamples to maximal regularity for operators in divergence form*, **Archiv der Mathematik 123(2), 199–209 (2024)**, [DOI 10.1007/s00013-024-02014-9](https://doi.org/10.1007/s00013-024-02014-9), [arXiv:2401.05550v2, 2 February 2026 (title-page date 3 February)](https://arxiv.org/abs/2401.05550v2). Theorem **2.5**, preprint p. **6**, constructs failure at each prescribed p in (1,infinity) except 2 for time-dependent complex divergence-form operators on H^{-1}(R^d), d>=2. The pair may depend on the prescribed p. It does not assert one fixed operator fails at every p>2; Theorem **2.2**, p. **3**, supplies a small pair-dependent deterministic interval. This distinguishes time-exponent extrapolation from changing the spatial exponent.

### Deterministic antecedents and access limits

For an autonomous closed densely defined operator on a fixed Banach space, deterministic maximal L^p-regularity at one p in (1,infinity) is independent of p in that open interval. In the survey this is Theorem **3.1(6)**, article p. **24** / v5 p. **17**. This statement does not automatically extend to merely measurable nonautonomous operators, nor does it infer stochastic maximal regularity with nonzero leading-order B.

The historical references are:

- **Pavel E. Sobolevskii**, *Coerciveness inequalities for abstract parabolic equations*, **Doklady Akademii Nauk SSSR 157(1), 52–55 (1964)**; English translation **Soviet Mathematics Doklady 5, 894–897 (1964)**. This is the paper credited for p-independence by Prüss–Simonett, p. 415 and reference [9], p. 430. It is distinct from the survey's broader Sobolevskii reference, *Equations of parabolic type in a Banach space*, Trudy Moskov. Mat. Obshch. 10 (1961), 297–350; English translation AMS Translations (2) 49 (1966), 1–62.
- **Piermarco Cannarsa and Vincenzo Vespri**, *On maximal L^p regularity for the abstract Cauchy problem*, **Bollettino dell'Unione Matematica Italiana B (6), 5(1), 165–175 (1986)**. The author's CV and later literature give series B; one institutional metadata record incorrectly labels the journal A.
- **Giovanni Dore**, *Maximal regularity in L^p spaces for an abstract Cauchy problem*, **Advances in Differential Equations 5(1–3), 293–322 (2000)**, [DOI 10.57262/ade/1356651386](https://doi.org/10.57262/ade/1356651386). The extrapolation theorem is **Theorem 7.1**, also explicitly identified as such by Lorist–Veraar, p. 6.

The three original texts were sought, but usable full texts were not obtained: the institutional Cannarsa–Vespri record has no attached paper; guessed BDIM identifiers returned “object not found”; Euclid and mirror downloads returned access/anti-bot pages; the Sobolevskii full-text host timed out. Accordingly I do **not** invent an original theorem number/page for Sobolevskii or Cannarsa–Vespri or an exact page for Dore's Theorem 7.1. Their historical attribution is independently checked in the accessible primary paper **Jan Prüss and Gieri Simonett**, *Maximal regularity for evolution equations in weighted L^p-spaces*, **Archiv der Mathematik 82, 415–431 (2004)**, [DOI 10.1007/s00013-004-0585-2](https://doi.org/10.1007/s00013-004-0585-2). Its introduction, p. **415**, states p-independence and credits Sobolevskii and Cannarsa–Vespri; Theorem **2.4**, pp. **419–420**, proves its power-weight equivalence. That paper is saved and was read. This is a documented limitation of the requested historical full-text audit, not a gap in the counterexample or the survey definition.

### 2025–2026 follow-up search

Searches combined the survey title/arXiv number, Problem 3, stochastic maximal regularity, extrapolation, symmetry and the authors' names. An OpenAlex citation query through 13 November 2026 returned **21 citing records**; the query and full metadata list are saved in data/citation_search.json. This index is not exhaustive: the 2026 necessary-conditions preprint below explicitly cites the survey but was not in that returned list. Titles were screened; only relevant full texts are represented here. No paper found supplies the unrestricted positive implication for general (A,B); the known counterexample precludes one without extra assumptions.

- **Foivos Evangelopoulos-Ntemiris and Mark Veraar**, *Discrete stochastic maximal regularity*, **Mathematische Annalen 394, article 42 (2026)**, online 13 February 2026, [DOI 10.1007/s00208-026-03348-1](https://doi.org/10.1007/s00208-026-03348-1), [arXiv:2505.22145v2, 17 December 2025](https://arxiv.org/abs/2505.22145v2). It cites the survey as [4]. Theorem **4.2(3)**, p. **20**, gives discrete p-extrapolation; Theorem **4.3**, pp. **20–21**, adds weights. The numerical recursion in (1.1) has additive g dW and an autonomous operator A, with B=0. It inherits the existing continuous B=0 theory and does not settle the nonzero-B range question.
- **Emiel Lorist, Jan van Neerven, Mark Veraar and Lutz Weis**, *Necessary conditions for deterministic and stochastic maximal regularity*, [arXiv:2608.20266v2, 2 September 2026](https://arxiv.org/abs/2608.20266v2). It cites the survey as [3]. Theorem **3.7**, pp. **10–11**, and Corollary **3.8**, p. **11**, exhibit a UMD type-2 Banach function space and an autonomous A with bounded H^infinity calculus of angle zero but **no** stochastic maximal regularity at any p>=2. This answers a different geometric sufficiency question; it is not a one-p-versus-another counterexample and does not contradict the L^q-subspace sufficient theorem. Its endpoint result, Theorem **4.9**, p. **22**, concerns the stochastic R-boundedness condition (S_2), which holds exactly for Hilbert-isomorphic spaces. It must not be read as a theorem that every particular SMR_2 operator forces its underlying space to be Hilbert.
- The related October 2026 preprint **Genming Bai, Jianbo Cui and Buyang Li**, *Maximal L^p-L^q regularity of finite element methods for stochastic parabolic equations in polygonal domains*, [arXiv:2610.25275v1](https://arxiv.org/abs/2610.25275v1), was also checked. It concerns additive-noise heat equations and their spatial discretization, not the arbitrary-pair problem; it does not cite the survey. Its Hörmander argument is another B=0 application, not a new resolution here.

## Why the proposed general proof routes do not work

For autonomous B=0 the requested Calderón–Zygmund/Rubio de Francia route is already realized by Lorist–Veraar. Bounded H^infinity calculus is a sufficient way to enter that theory on appropriate L^q-based spaces, not a necessary extra hypothesis for p-extrapolation itself.

For nonzero B, writing u=S*f+S diamond(Bu+g) only yields a perturbation proof at exponent r when the operator taking u to S diamond(Bu) has norm less than one there (or under other hypotheses that independently establish invertibility). Bounded invertibility at one p does not imply bounded invertibility at all r. The known moment threshold gives a concrete failure even when A,B commute and A has the best possible functional calculus. Shrinking the time interval cannot supply the missing uniform spatial estimate: (6) diverges on **every** fixed positive interval as n increases.

In the general random time-dependent case, a proposed kernel S(t,s,omega) may depend on the Brownian increments between s and t. Its product with a progressively measurable g(s) is not automatically an admissible Itô integrand in s. A deterministic-kernel singular integral theorem cannot be applied without establishing its exact kernel and adaptedness assumptions. Portal–Veraar avoid this obstacle using a reference equation and a pathwise deterministic correction; the required deterministic maximal regularity remains an assumption.

## Checks, artifacts, and disposition

- Read the published Problem 3 and nearby discussion, both definitions including the bullet, and the exact bibliography entry [29]. Checked the two page-number systems separately.
- Matched the counterexample's operator domains, complex interpolation scale, gamma norm, initial condition, forcing class, finite horizons and uniform constants. The failure of (2) alone suffices; no unsupported assertion about fractional time regularity is needed.
- Checked the moment exponent by both the explicit stochastic exponential and Itô's formula, including the factor 2 in the 2012 paper's coefficient, the borderline c_r=0, and the signs at r=2,3,4 when sigma=1.
- The p=2 hypothesis includes the required continuous H-valued estimate through the variational theorem; failure at the target is for r>2. No endpoint r=2 extrapolation or theta=1/2 estimate was assumed.
- Every downloaded PDF was passed as bytes directly to pdftotext's stdin. Sources contain text only. No simulations, publication, pushes or subagents were used. Source provenance and hashes are in data/source_manifest.jsonl. Fetching/conversion code is in code/; the sandbox refused nice(10), so that requested process-priority setting could not be applied. No heavy numerical work was run.

Stop at the literature result: the literal unrestricted extrapolation assertion is false by the already-published moment obstruction. The remaining general, pair-dependent range question is not claimed solved. The unavailable historical original texts are explicitly identified above.

Task: “Open problem I0069.” Received 13 November 2026, 16:12 Asia/Tbilisi (session launch time; no finer user-message timestamp was supplied).
