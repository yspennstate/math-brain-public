# P0323 ? Canonical DLR passage for Boursier's limit

Date: 2026-10-12. The proof below is an analytic proof, using Boursier's Theorem 3 as an input. Lean checks only the finite normalization identities in Normalization.lean, not this analytic proof.

## 1. Exact scope and conventions

The source is Boursier, arXiv:2209.00396v4, equations (1.1), (1.3), (1.4), Theorem 3, and Section 1.3. Fix beta>0 and s in (0,1) union (1,infinity). Write P=Riesz_{s,beta} for the limit in Theorem 3. The source does not display an explicit DLR kernel. Its comparison is with the canonical DLR equations for Sine-beta: conditional on the exterior AND the number of inside points. This manuscript proves precisely that specification, for the whole stated exponent range. It does not derive a prescribed grand-canonical activity or the conditional inside-count probabilities.

Put v(r)=|r|^{-s}, v(0)=+infinity, and b=2 beta. The factor two is necessary: Boursier's H_N sums ordered pairs i!=j. If the interaction is written as an unordered-pair sum, its inverse temperature is b.

Let Delta be any bounded Borel set of positive Lebesgue measure, m=N_Delta(gamma), eta=gamma restricted to Delta^c. Let B_{Delta,m} be the law of m independent uniform points on Delta, interpreted as an unlabeled configuration, and B_{Delta,0}=delta_empty. Define

    W_eta(x) = sum_{y in eta} [v(x-y)-v(-y)],
    E_Delta(u;eta) = sum_{i<j} v(u_i-u_j) + sum_i W_eta(u_i),
    Z_Delta(eta,m) = integral exp(-b E_Delta(u;eta)) B_{Delta,m}(du),
    Gamma_Delta f(gamma)
      = Z_Delta(eta,m)^{-1}
        integral f(u union eta) exp(-b E_Delta(u;eta)) B_{Delta,m}(du).

These expressions are defined on a P-full class described below. On its complement set Gamma to the identity kernel. The theorem proved is

    P Gamma_Delta = P                                              (DLR)

for every such Delta. Equivalently Gamma_Delta is the conditional law of the inside points given (eta,m). Zero-volume bounded Borel sets have zero points P-almost surely and require only the identity kernel. No uniqueness among infinite-volume Gibbs states is claimed.

## 2. First-moment control survives the limit

Rescale the N-circle to length N, using representatives in I_N=[-N/2,N/2). Its unlabelled law mu_N is the law of N unit-density particles with energy b sum_{i<j} h_N(z_i-z_j), where

    h_N(r)=N^{-s} g_s(r/N).

The choice of representative for I_N does not affect the interaction. Translation invariance on the circle implies E_mu_N N_A=|A| for every Borel A subset I_N. Indeed its first moment is translation invariant on that circle and its total mass is N. The cyclic ordering convention in Boursier contributes only a constant multiplicity to each unlabelled configuration, so it does not change this law.

For every bounded Borel A and integer L, min(N_A,L) is a bounded local Borel function. For N sufficiently large A is inside (-N/4,N/4), so Boursier's restricted process Q_N agrees with mu_N on A. Theorem 3 and monotone convergence give

    E_P N_A = lim_{L->infinity} lim_{N->infinity} E_mu_N min(N_A,L)
            <= |A|.                                             (2.1)

For arbitrary nonnegative Borel w the same inequality, E_P integral w dgamma <= integral w dx, follows first for simple functions supported in bounded regions, then by monotone convergence. In particular P has no point at 0 and

    E_P T_R <= 2 R^{-s}/s,
    T_R(gamma)=sum_{|y|>R} |y|^{-s-1}.                            (2.2)

The periodically extended process xi_N=sum_{z in gamma_N} sum_{k in Z} delta_{z+kN} is stationary with intensity exactly one on R. Thus (2.2) holds with equality for xi_N. All tail estimates below may use subconfigurations of xi_N and remain valid. No second moment, number rigidity, or uniform integrability of the untruncated particle count is needed.

## 3. Relative potentials and partition functions

Choose a>=1 with Delta subset [-a,a]. If |y|>2a and |x|<=a, the segment between -y and x-y is at distance at least |y|/2 from zero. The fundamental theorem of calculus and |v'(r)|=s|r|^{-s-1} yield

    |v(x-y)-v(-y)| <= C_a,s |y|^{-s-1},
    C_a,s=s a 2^{s+1}.                                         (3.1)

By (2.2), T_{2a}<infinity almost surely. Work on the measurable class S of simple locally finite configurations having no point at 0 and T_{2a}<infinity. This class has full P-probability and is preserved by a finite resampling almost surely. For eta=gamma|Delta^c, its near part |y|<=2a is finite, with v(-y)<infinity for every point. Hence the near part of W_eta(x) is finite for each x in Delta (x is not an exterior point), and bounded below uniformly in x by -sum_{y in eta, |y|<=2a} v(-y). The tail converges absolutely and uniformly in x by (3.1) and has absolute value at most C_a,s T_{2a}. Thus W_eta is finite at every x in Delta and bounded below by a finite constant depending on eta.

Internal pair energies are nonnegative. For m fixed, E_Delta is bounded below, so exp(-b E_Delta) has a finite uniform upper bound. For almost every tuple in Delta^m the inside points are distinct, and every pair energy and exterior term is finite, so the integrand is strictly positive almost everywhere. It follows that

    0 < Z_Delta(eta,m) < infinity.                              (3.2)

This also handles m=0, where Z=1. All finite-cutoff potentials are Borel. Their pointwise tail limits are Borel, and integrations of Borel functions against the product uniform laws are Borel; therefore Gamma is a measurable probability kernel. Internal collision tuples have Lebesgue measure zero; their weight is defined as zero.

Changing the reference from 0 to a deterministic point x_* avoided by eta subtracts the same finite number W_eta(x_*) from each W_eta(x). Absolute convergence of the tail proves this subtraction identity; finite near sums cause no difficulty. Consequently E changes by the constant -m W_eta(x_*), which cancels between numerator and denominator. The normalized law is independent of that reference whenever both definitions are available.

Let W_eta^R restrict the sum to |y|<=R, R>2a, and let Gamma_Delta^R use this potential but the same v for internal pairs. Then

    sup_{u in Delta^m} |E_Delta(u;eta)-E_Delta^R(u;eta)|
           <= m C_a,s T_R(gamma).                              (3.3)

The supremum is over distinct tuples; both energies are infinite on collision diagonals and the weights there vanish.

## 4. Normalized-density perturbation lemma

Suppose two energies E,F on the same reference probability space satisfy |E-F-c|<=epsilon almost everywhere, for a constant c, and have finite positive Gibbs normalizers at parameter b>0. The constant c cancels. Then

    e^{-b epsilon} <= exp(-b(E-c))/exp(-bF) <= e^{b epsilon},
    e^{-b epsilon} <= Z_{E-c}/Z_F <= e^{b epsilon}.

Dividing gives that the density ratio of the two normalized laws lies in [e^{-2b epsilon},e^{2b epsilon}]. For every bounded f their expectations consequently differ by at most

    ||f||_infinity (e^{2b epsilon}-1),                         (4.1)

and, trivially, by at most 2||f||_infinity. This proof uses only integration of the pointwise inequalities, and requires no lower bound on a random normalizing constant beyond positivity. Normalization.lean independently verifies the algebraic cancellation of a constant multiplicative weight and the exponential energy-shift identity.

For any process with first-moment domination by Lebesgue measure, Markov's inequality and (2.2) give, for M>=1, t>0,

    P(m>M) <= |Delta|/M,
    P(T_R>t) <= 2 R^{-s}/(s t).

On {m<=M,T_R<=t}, (3.3) and (4.1) apply with epsilon=M C_a,s t. Therefore

    E |Gamma_Delta f-Gamma_Delta^R f|
    <= ||f||_infinity [ e^{2b M C_a,s t}-1
                +2|Delta|/M + 4 R^{-s}/(s t) ].                (4.2)

The same comparison bound holds for kernels built from subconfigurations of xi_N. Choose M large, then t small, then R large. This proves uniform L1 approximation. Independence between the count and the tail is not assumed, and the product m T_R is never claimed to have a finite expectation.

## 5. Exact periodic image identity and internal-energy bound

From Boursier's definition, for r,r_* away from N Z,

    h_N(r)-h_N(r_*)
       = sum_{k in Z} [v(r+kN)-v(r_*+kN)].                     (5.1)

To verify (5.1), subtract the two finite image sums in (1.1); their subtracted counterterms cancel. The resulting infinite series is absolutely convergent: for large |k| its summands are bounded by a constant times |kN|^{-s-1}, by the same derivative estimate as (3.1). Thus it equals the limit of those finite differences. This argument applies both when 0<s<1 and when s>1.

For 0<|r|<=2a and N>=4a, set

    c_s = lim_{L->infinity}
             [2 sum_{k=1}^L k^{-s} - 2 L^{1-s}/(1-s)],
    kappa_N = N^{-s} c_s.

This real limit exists for s!=1. For 0<s<1 the successive increments of sum_{k=1}^L k^{-s}-L^{1-s}/(1-s) are O(L^{-s-1}), by the mean value theorem applied to the integral of t^{-s}; their series converges. For s>1 the partial sum converges and L^{1-s}->0. Separating k=0 in the finite sums and pairing k and -k gives

    h_N(r)-v(r)-kappa_N
        = sum_{k>=1} [v(kN+r)+v(kN-r)-2v(kN)].                (5.2)

Taylor's integral formula on [kN-|r|,kN+|r|] bounds the bracket in absolute value by

    s(s+1) r^2 (kN-|r|)^{-s-2}.

Since kN-|r|>=kN/2,

    sup_{0<|r|<=2a}|h_N(r)-v(r)-kappa_N|
       <= epsilon_N,
    epsilon_N=s(s+1)(2a)^2 2^{s+2} N^{-s-2}
                  sum_{k>=1} k^{-s-2} -> 0.                  (5.3)

The term kappa_N contributes exactly binom(m,2) kappa_N to an inside m-particle energy; it cancels in the fixed-count Gibbs normalization. No divergent absolute exterior energy is used.

## 6. Finite-circle conditional laws converge to the truncated kernels

Fix N so large that [-R,R] and the local support of f are contained in (-N/4,N/4), and Delta subset I_N. Given the exterior gamma_N|_{I_N\Delta} and the inside count m, the ordinary finite-dimensional conditional law is binomial B_{Delta,m} weighted by

    exp(-b [sum_{i<j}h_N(u_i-u_j)
                 +sum_i sum_{y in gamma_N|I_N\Delta}h_N(u_i-y)]).

Indeed split the full unordered-pair energy into inside-inside, inside-outside, and outside-outside sums, the last being constant under this conditioning. The symmetric Lebesgue reference law gives the binomial inside reference, since its combinatorial label factors depend only on m. Denote this finite kernel Gamma_{N,Delta}. Hence, for every bounded function evaluated on the base configuration,

    E_mu_N f = E_mu_N Gamma_{N,Delta} f.                       (6.1)

Subtract sum_i sum_y h_N(-y), a constant depending on the exterior and m. For almost every exterior no y equals 0 modulo N, so this is legitimate. Apply (5.1) separately to each outside point. With

    eta_N^per = sum_{y in gamma_N|I_N\Delta} sum_{k in Z}delta_{y+kN},

the resulting exterior potential is exactly

    sum_{z in eta_N^per}[v(u_i-z)-v(-z)].                      (6.2)

This periodic exterior omits ALL copies of the inside points. It is a subconfiguration of xi_N, not an independent point process. Its first moment is nevertheless dominated by that of xi_N. For |z|<=R<N/2, only the k=0 copies occur, so its near part equals gamma_N|([-R,R]\Delta).

Define Gamma_Delta^R on the base configuration as in Section 3. Comparing its energy with the energy of Gamma_{N,Delta} after removing the constants above, (5.3), (6.2), and (3.1) give

    |energy difference|
       <= binom(m,2) epsilon_N + m C_a,s T_R(xi_N).            (6.3)

Thus on {m<=M,T_R(xi_N)<=t} the perturbation lemma applies with epsilon=binom(M,2)epsilon_N+M C_a,s t. Since E_mu_N m=|Delta| and xi_N has intensity one,

    E_mu_N |Gamma_{N,Delta} f-Gamma_Delta^R f|
    <= ||f||_infinity [
       exp(2b[binom(M,2)epsilon_N+M C_a,s t])-1
                  +2|Delta|/M+4R^{-s}/(s t)].                (6.4)

This is the needed uniform control of both conditional weights and their normalized partition functions. Its proof never takes a conditional weak limit directly.

## 7. Passage to the limit and full conditional identity

First take f bounded, Borel and local, supported on a bounded set K. For fixed R, Gamma_Delta^R f depends only on gamma restricted to K union Delta union [-R,R]; it is bounded and Borel. Consequently Boursier's Theorem 3 gives

    E_mu_N f -> E_P f,
    E_mu_N Gamma_Delta^R f -> E_P Gamma_Delta^R f.             (7.1)

Equations (6.1), (6.4), (7.1), and (4.2) imply

    |E_P f-E_P Gamma_Delta f|
    <= 2 ||f||_infinity [ exp(2b M C_a,s t)-1
                         +2|Delta|/M+4R^{-s}/(s t)].          (7.2)

Here N was taken to infinity with M,t,R fixed, so epsilon_N vanished. Given any positive error tolerance, first choose M to make the count term small, then t to make the exponential term small, then R to make the tail term small. Equation (7.2) therefore proves (DLR) for every bounded local Borel f.

To extend it, let nu=P Gamma_Delta, a probability measure on configuration space. The equalities just proved say that P and nu agree on bounded-region cylinder events. These events form a pi-system generating the count-map sigma algebra used by the source: counts in an arbitrary Borel set are limits of the counts in its intersections with [-j,j]. The pi-lambda theorem implies P=nu. Thus (DLR) holds for every bounded measurable f, including functions depending on arbitrarily distant exterior points.

Let G_Delta be the sigma algebra generated by the exterior configuration and N_Delta. Gamma_Delta f is G_Delta-measurable. The kernel keeps both of these objects unchanged. For bounded G_Delta-measurable g,

    E_P(g f)=E_P Gamma_Delta(g f)=E_P(g Gamma_Delta f).

This is exactly the defining identity of E_P(f|G_Delta). Hence the theorem gives the conditional specification, not merely an unconditional invariance statement.

## 8. Consistency of the canonical kernels

For Lambda subset Delta, fix an admissible exterior eta outside Delta and total inside count m. Under Gamma_Delta the density in Delta is given in Section 1. Split its inside configuration as u in Lambda and zeta in Delta\Lambda. Conditional on zeta and n=|u|, the binomial reference becomes B_{Lambda,n}, with factors involving zeta and label choices independent of u. The part of E_Delta depending on u is

    sum_{pairs in u}v + sum_{x in u,y in zeta}v(x-y)
                       +sum_{x in u}W_eta(x).

But W_{eta union zeta}(x)=W_eta(x)+sum_{y in zeta}[v(x-y)-v(-y)]. Therefore that part differs from E_Lambda(u;eta union zeta) by the constant n sum_{y in zeta}v(-y). This finite constant cancels, giving exactly Gamma_Lambda as this conditional law. Fubini's theorem, applied to the positive finite normalized densities, now yields Gamma_Delta Gamma_Lambda=Gamma_Delta. Conversely Gamma_Delta f depends only on the exterior of Delta and N_Delta, which are preserved by Gamma_Lambda, so Gamma_Lambda Gamma_Delta=Gamma_Delta. The class S is preserved by these resamplings almost surely since only finitely many points change and Lebesgue sampling puts no point at 0. Thus the kernels are consistent on a common full-measure class. Sets of zero volume are handled by identity kernels.

## 9. Hostile-referee audit and boundary cases

- **Double counting:** fixed by b=2 beta, directly from Boursier (1.3). Omitting the factor two would produce the wrong temperature.
- **Vague convergence insufficient:** the proof uses the actual bounded-local-Borel convergence in Theorem 3. It does not silently infer setwise convergence from a continuous-test limit.
- **Periodization:** (6.2) excludes every copy of the inside configuration. Interactions between inside particles and their images remain accounted for by h_N on internal pairs and (5.3). Self-images are constants and are absent from Boursier's i!=j energy.
- **Random count times tail:** controlled on {m<=M,T_R<=t} and by two Markov bounds, not by E[m T_R], which need not be finite from first moments alone.
- **Small partition functions:** (4.1) uses density ratios; no inverse normalizer moment is assumed.
- **Exterior arbitrarily close to the boundary:** only nonnegative local singularities arise. They may make W unbounded above near a boundary, but its finite lower bound suffices for normalizability. No boundary gap is assumed.
- **General Borel sets:** only boundedness, positive finite Lebesgue measure, and locality are used; no smooth boundary, interval geometry, or boundary convergence theorem is needed.
- **m=0 or 1:** m=0 gives the empty inside configuration; m=1 has no pair energy and all estimates still hold.
- **s approaching 0:** R^{-s} tends to zero for each fixed s>0, but not uniformly in s; no logarithmic-case theorem is obtained by putting s=0.
- **s=1:** excluded because source (1.1) and Theorem 3 exclude it. The elementary tail inequality works there, but neither the source law nor its convergence at s=1 is being claimed.
- **Grand-canonical distinction:** canonical DLR conditions on the inside count. It does not determine P(N_Delta=m|eta), and it does not imply uniqueness or non-number-rigidity by itself.

## 10. What remains if a stronger interpretation is required

The full theorem above proves canonical DLR for all beta>0 and s in the source's thermodynamic-limit range. If ?anticipated DLR? requires an exterior-only conditional density with a specified insertion compensator/activity, that stronger assertion is not proved by Sections 1?9. Its remaining gap is the identification of the count-sector weights P(N_Delta=m|eta), with compatible normalization as m varies. No inference from fixed-count normalization to those weights is valid.

For 0<s<1, Dereudre?Vasseur Theorems 1.11 and 1.14 are promising additional inputs: they construct a special periodic accumulation point with non-number-rigidity and grand-canonical equations. Boursier's unique circular limit should identify it after checking additive kernel constants and the factor-two temperature convention. This is an implication to prove, not a theorem in print literally naming Boursier's limit, and is not asserted here without the full identification. For s>1 an exterior-only DLR result would additionally require the appropriate activity/equivalence-of-ensembles argument. These stronger tasks are distinct from the canonical theorem established above.

## 11. Additional proved reduction: exterior-only DLR for 0<s<1

This section uses Dereudre?Vasseur Proposition 1.5 and Theorems 1.11 and 1.14 as published theorem inputs. Their theorem is not reproved; the identification of its measure with Boursier's measure is proved here.

Fix 0<s<1. Denote by q_N the periodized kernel in Dereudre?Vasseur Proposition 1.1, d=1:

    q_N(r)=sum_{k in Z}[v(r+kN)-(1/N) integral_{I_N} v(t+kN)dt].

The integrals exist because s<1. For r and r_* not in NZ the definition and cancellation of the integral terms give

    q_N(r)-q_N(r_*)=sum_{k in Z}[v(r+kN)-v(r_*+kN)].

The absolute convergence proof is exactly (5.1): the summand has an integrable-gradient bound O(|k|^{-s-1}) for large |k|. Comparing with (5.1), q_N(r)-h_N(r) is a constant independent of r on the punctured N-circle. For a configuration with exactly N particles, replacing h_N by q_N changes its unordered-pair energy by binom(N,2) times that constant. It cancels in normalization. Thus, with inverse temperature theta=2 beta in Dereudre?Vasseur, their unlabelled P_N^theta is exactly our mu_N. Normalization of Lebesgue into the binomial law changes only another constant; cyclic versus free labelling changes only a constant multiplicity, as in Section 2.

Their Section 2.4.1 constructs a special P_*^theta as an accumulation point of a subsequence of these same fixed-theta laws. Their local topology tests bounded local functions (and also local tame functions). In particular along the selected convergent subsequence every bounded local Borel expectation tends to its value under P_*^theta. But Boursier Theorem 3 says those expectations tend along the full sequence to their value under P=Riesz_{s,beta}. Hence P and P_*^theta agree on all bounded local cylinder events. The pi-lambda argument of Section 7 proves equality of the probability measures.

Applying Dereudre?Vasseur Theorem 1.14 to this now-identified measure gives, for every bounded Borel Delta and bounded measurable f,

    E_P f = integral P(dgamma) [1/Z_{*,Delta}^theta(gamma)]
            integral f(u union gamma_{Delta^c})
                     exp(-theta H_{*,Delta}^theta(u,gamma)) Pi_Delta(du),

where Pi_Delta is unit-intensity Poisson in Delta and H_{*,Delta}^theta is the measurable compensated insertion energy constructed in their Proposition 1.13 and Section 2.5.3. Its normalizer is finite and nonzero by their theorem. This is an exterior-only conditional DLR identity, as explicitly stated after Theorem 1.14. The equality P=P_*^theta also transfers Theorem 1.11: every count sector has positive conditional probability for each compact positive-volume Delta. This use of unique convergence is identification of a limit, not uniqueness among all Gibbs states.

Thus the grand-canonical identity with the Dereudre?Vasseur compensator IS established by reduction for 0<s<1. The compensator is their measurable one; this does not prove that it equals a particular deterministic integral-background renormalization. The analogous exterior-only description for s>1 is not proved here. Section 10's long-range identification concern is resolved by this section; its short-range/activity concern remains.

## 12. Verification record

checks.py ran 45 checks: 18 one-sided relative-potential tail bounds (s=.05,.3,.9,1.1,2,8 and R=5,20,100), 18 paired periodic-kernel error bounds (same s, N=8,20,80), and nine finite normalized-density perturbations at varied temperatures and energy offsets +/-10000. All passed in about 0.12 seconds, using mpmath at 50 decimal digits. Saved numerical_checks.json contains every value. These computations test finite/explicit inequalities; they are not evidence of an infinite-volume conditional law by themselves. The analytic proofs are Sections 2?9.


Lean verification completed: `lake env lean ~/brain_workers/TRIO_1011/op/P0323/Normalization.lean` ran from `~/lean_verify`, with a 3600-second subprocess timeout, exit code 0. Both lemmas passed; printed axioms are only propext, Classical.choice, Quot.sound. No sorry, native_decide, or unchecked axiom was introduced. The redundant `ring` after field_simp generated a linter warning only. See lean_check.txt. This checks finite normalization, not the full analytic DLR proof.

## 13. Further proved short-range bound: second moments and temperedness

Let s>1 and b=2 beta. Then h_N(r)=sum_{k in Z}|r+kN|^{-s}, with all terms nonnegative. Write H_N^u=sum_{i<j}h_N(x_i-x_j) for the unordered energy, and Z_N(b)=E_{B_{I_N,N}} exp(-b H_N^u). Partition the N-circle into N unit cells and let J_i be the central interval of length 1/2 in each cell. Under the binomial reference, the event A that exactly one particle lies in each J_i has probability

    P(A)=N! (1/(2N))^N >= (1/(2e))^N.

For the inequality, log(N!)=sum_{k=1}^N log k >= integral_1^N log t dt = N log N-N+1. On A the periodic extension is a perturbed unit lattice, with every indexed displacement of absolute value at most 1/4 from the cell center. The distance between a point and a point j lattice steps away is at least |j|-1/2. Hence, for each of the N base points, its sum of interactions with all periodic copies of all other base points is bounded by

    D_s=2 sum_{j>=1}(j-1/2)^{-s}<infinity.

Including copies of itself at other periods would only enlarge this upper bound. The unordered energy is one half the ordered base-point sum, and thus H_N^u<=N D_s/2 on A. Consequently

    Z_N(b)>=exp[-N A_s,b],
    A_s,b=log(2e)+b D_s/2.                                    (13.1)

Under mu_N at parameter b,

    E_mu_N exp(b H_N^u/2)=Z_N(b/2)/Z_N(b)<=1/Z_N(b),

since the energy is nonnegative. Jensen's inequality and (13.1) imply

    E_mu_N H_N^u <= (2 A_s,b/b) N.                            (13.2)

In each unit cell, particles are at distance at most 1, so their direct pair interaction is at least 1. If n_j are the N unit-cell counts, positivity of all other contributions gives

    H_N^u >= (1/2) sum_j (n_j^2-n_j).

Circle stationarity makes their second moments equal, and sum_j n_j=N deterministically. Thus

    E_mu_N n_j^2 <= 1+4 A_s,b/b =: K_s,b.                     (13.3)

By bounded-local convergence and monotone truncation, E_P N_[0,1)^2<=K_s,b. This also proves unit intensity for s>1: for n=N_[0,1), the uniform bound gives E_mu_N[n 1_{n>L}]<=K_s,b/L, so bounded-local convergence upgrades to convergence of E n, which equals 1. Stationarity then gives intensity exactly one.

Apply the pointwise ergodic theorem for integer translations to the integrable function gamma -> N_[0,1)(gamma)^2. The bilateral averages (2L+1)^{-1} sum_{j=-L}^L N_[j,j+1)(gamma)^2 converge P-almost surely to a finite random variable (the conditional expectation on the integer-translation invariant sigma algebra). Therefore P is supported on configurations for which

    sup_{L>=1} (2L+1)^{-1} sum_{j=-L}^L N_[j,j+1)(gamma)^2 < infinity.    (13.4)

This is the usual square-count temperedness condition. Ergodicity is not assumed. Neither (13.3) nor (13.4) says that the empirical density is deterministic. In addition, for s>1 the ordinary exterior potential sum_{y in eta}v(x-y) has an absolutely convergent distant tail uniformly for bounded x, since its expected envelope is bounded by a constant times integral_R^infinity t^{-s}dt. This removes the long-range compensator issue in this exponent range.

Georgii (1976) is a lead for upgrading canonical DLR with temperedness to a mixture of grand-canonical states. The accessible publisher abstract confirms a ?natural temperedness condition? and ?appropriate activities,? but the full theorem text was not retrieved. We therefore do not assert its exact applicability or a single deterministic activity from that abstract. Even a valid mixture theorem would leave the need to identify the activity relevant to this particular circular limit. This is the remaining short-range gap in the stronger exterior-only formulation.


## Final audit outcome and scope verdict

Self-refereeing found no unresolved analytic step in Sections 2?9's canonical DLR passage or Section 11's long-range identification, subject to the explicitly named published theorem inputs. Section 13 is independent of the unavailable Georgii theorem: the cell-energy lower bound uses positivity for s>1, Jensen is applied to a finite exponential moment obtained exactly from Z_N(b/2)/Z_N(b), and stationarity plus truncation justify the limit of first and second count moments. No empirical-density determinism or activity selection is inferred from temperedness.

The precise established results are:
1. Canonical DLR for Boursier's limit, all beta>0, 0<s<1 or s>1, every bounded Borel region.
2. Exterior-only grand-canonical DLR with the Dereudre?Vasseur measurable compensator for 0<s<1, by an explicit finite-ensemble and limiting-measure identification.
3. For s>1: unit intensity, second moment bounds, temperedness, and ordinary convergent exterior potentials.

The source leaves its anticipated specification implicit. If the target is canonical DLR, result 1 answers it fully. To avoid silently weakening a request for exterior-only DLR over the entire stated exponent range, the overall recorded verdict is PARTIAL. The outstanding stronger assertion is that, for s>1, there exists one activity z=z(s,beta)>0 such that the exterior-only conditional law in every Delta is proportional to

    z^{|u|} exp(-2 beta [sum_{pairs in u}|x-y|^{-s}
                      +sum_{x in u,y in eta}|x-y|^{-s}]) Pi_Delta(du).

Its missing step is a verified canonical-to-grand-canonical theorem application together with activity identification for this circular limit, rather than an unspecified mixture of activities. No counterexample is claimed. A prescribed deterministic compensator for the long-range gas, if additionally required, is also not established here.
