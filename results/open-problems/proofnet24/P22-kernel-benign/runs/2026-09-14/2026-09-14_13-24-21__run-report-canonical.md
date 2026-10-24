# ProofNet24 P22 — Kernel Benign-Overfitting Audit

Run timestamp: 2026-09-14 13:24:21 Asia/Jerusalem

Target: actual Gaussian-kernel minimum-norm interpolation for iid inputs uniform on the unit sphere, fixed bandwidth h > 0, dimensions d_ell = 2^(2^ell), sample sizes n_ell = 2^(2^(2 ell)), Gaussian training-noise variance sigma^2, and every spherical-polynomial signal sequence of one fixed maximal degree with uniformly bounded population L2 norm.

## Executive verdict

P04 Target 2 survives this independent audit. If f_d lies in the direct sum of spherical-harmonic degrees 0 through q0 for one fixed q0 and ||f_d||_2 ≤ B uniformly, and fhat_d is the minimum-RKHS-norm interpolant for the fixed-bandwidth Gaussian kernel, then the conditional clean-test excess risk

R_ell = E_X0[(fhat_d(X0) - f_d(X0))^2 | X_1:n, epsilon_1:n]

converges to zero in probability.

The run proves a stronger statement: along the prescribed super-exponential sequence, R_ell converges to zero almost surely under any joint coupling of the level-wise experiments having the stated marginals. Cross-level independence is not needed.

The mathematical proof is candidate-complete. ProofNet portfolio closure is still withheld because the protocol requires two OTHER independent complete-proof audits.

No numerical experiment is used as proof.

## Sources checked

Latest full P04 source: Gmail message 1a09ee796dd857e4, subject "Kernel conjecture solver — hourly update". P04 marks Target 2 proved and supplies the candidate growing-degree tail-isotropy argument.

Latest full P22 source: ChatGPT Library file file_000000004d9c81f7beb6c6ff7f907fcc, P22_kernel_benign_2026-09-14_12-24-38.md.

Other full worker report: P12 Library file file_00000000936081f6a725f2d3d2568409, P12_smooth_iid_least_singular_2026-09-14_12-46.md.

Primary sources checked:
- Kaushik–Romberg–Muthukumar, "A general technique for approximating high-dimensional empirical kernel matrices", arXiv:2511.03892v1 (2025). I checked the proof-level decoupling/noncommutative-Khintchine step, especially the pre-relaxation L term and its row-square bound.
- Tropp, "User-Friendly Tail Bounds for Sums of Random Matrices", Foundations of Computational Mathematics 12 (2012), arXiv:1004.4389. I checked the matrix Chernoff hypotheses used for the growing low-harmonic block.
- Johnson–Schechtman–Zinn, "Best constants in moment inequalities for linear combinations of independent and exchangeable random variables", Annals of Probability 13 (1985), 234–253. I use only a conservative C q Rosenthal consequence, weaker than their optimal asymptotic constant.
- Gross, "Logarithmic Sobolev inequalities", American Journal of Mathematics 97 (1975), 1061–1083. I use Gaussian Ornstein–Uhlenbeck hypercontractivity for a homogeneous harmonic polynomial.

## Exact model and notation

Let R = 2^ell. Then d = 2^R and n = d^R.

Inputs X_1,...,X_n are iid uniform on S^(d-1). Labels are

Y_i = f_d(X_i) + epsilon_i,

where epsilon_i are iid N(0,sigma^2), independent of the design.

The kernel is

K_h(x,y) = exp(-||x-y||^2/(2 h^2))
         = exp(-gamma) exp(gamma <x,y>),

with gamma = h^(-2).

Let H_(d,s) be the degree-s spherical-harmonic space, with multiplicity N_s, and let P_s be its population L2 projection kernel. With an L2-orthonormal harmonic basis,

P_s(x,y) = sum_a psi_(s,a)(x) psi_(s,a)(y).

The exact multiplicity is

N_s = C(d+s-1,s) - C(d+s-3,s-2).

Assume f_d belongs to the sum of H_(d,s), 0 ≤ s ≤ q0, where q0 is fixed and ||f_d||_2 ≤ B.

## P22-B1 — Exact Gaussian-kernel Mercer eigenvalues

Status: PROVED.

The Mercer expansion is K_h = sum_(s≥0) lambda_(d,s) P_s, with

lambda_(d,s)
= exp(-gamma) sum_(r≥0)
  gamma^(s+2r) /
  [2^r r! d(d+2)...(d+2(s+r)-2)].

Independent derivation: if H_s is a homogeneous harmonic polynomial of degree s and G is standard Gaussian in R^d, then Cameron–Martin plus harmonicity gives

E[H_s(G) exp(t<x,G> - t^2/2)] = t^s H_s(x).

Comparing coefficients of t^(s+2r) yields

E[(<x,G>)^(s+2r) H_s(G)] = (s+2r)!/(2^r r!) H_s(x).

Writing G = R U with U uniform on the sphere and R independent, and using

E R^(2(s+r)) = d(d+2)...(d+2(s+r)-2),

gives the displayed Mercer formula after expanding exp(gamma<x,u>).

Term by term,

lambda_(d,s+1) ≤ gamma/(d+2s) lambda_(d,s).

Thus for fixed h and large d the eigenvalues decrease throughout the entire tail. This makes the later PSD comparison exact.

Set tau_s = N_s lambda_(d,s). For s = o(sqrt(d)),

tau_s = exp(-gamma) gamma^s/s! [1 + O_h((s^2+1)/d)].

## P22-B2 — Harmonic cutoff and multiplicity gap

Status: PROVED.

Use the cutoff

k = R + ell - 1.

For s = o(d),

N_s = d^s/s! exp(O(s^2/d)).

Stirling's formula at k gives

log(N_k)/log(d) = R + delta + o(1),

where

delta = 1/log(2) - 1 = 0.442695....

Hence

N_k/n = d^(delta+o(1)),

while the total low dimension D_<k = sum_(s<k) N_s satisfies

D_<k/n = d^(delta-1+o(1))
       = d^(-0.557305...+o(1)).

The ell-1 correction in k is essential: dropping the factorial correction and choosing k = R loses the required low/high dimension separation.

## P22-B3 — Dimension-free growing-degree hypercontractivity

Status: PROVED.

Let Y_s be a spherical harmonic of degree s and H_s its homogeneous harmonic extension: H_s(r u) = r^s Y_s(u). Harmonicity and homogeneity imply that H_s is an exact degree-s eigenfunction of the Gaussian Ornstein–Uhlenbeck generator. Gross hypercontractivity therefore gives, for integer q ≥ 1,

||H_s(G)||_(2q) ≤ (2q-1)^(s/2) ||H_s(G)||_2.

Writing G = R U and using independence of R and U together with monotonicity of Lp norms of R^s gives

||Y_s||_(2q) ≤ (2q-1)^(s/2) ||Y_s||_2.

The constant is exactly independent of dimension. For fixed z,

||r_s(X,z)||_(2q) ≤ (2q-1)^(s/2)/sqrt(N_s),

where r_s = P_s/N_s.

This directly removes the principal hidden-uniformity concern in using degree s about R tending to infinity.

## P22-B4 — Entire infinite-tail mixture

Status: PROVED.

Define the tail

K_T = sum_(s≥k) lambda_s P_s,
tau = K_T(x,x) = sum_(s≥k) tau_s,
r_T = K_T/tau = sum_(s≥k) w_s r_s,

where w_s = tau_s/tau.

Positive Taylor coefficients give

tau_s ≤ exp(-gamma) sum_(m≥s) gamma^m/m!.

The r=0 Mercer term gives, for large d,

tau_k ≥ c_h exp(-gamma) gamma^k/k!.

Since k > 2 gamma eventually,

tau_(k+r)/tau_k ≤ C_h gamma^r k!/(k+r)!.

Combining this factorial decay with the harmonic hypercontractive factor gives, at q = R,

||r_T(X,z)||_(2R)
≤ C_h (2R)^(k/2)/sqrt(N_k).

Also

E r_T(X,z)^2
= sum_(s≥k) w_s^2/N_s
= (1+o(1))/N_k.

In particular,

||r_T(X,z)^2||_2 ≤ C_h 3^k/N_k,

and

||r_T(X,z)^2||_R ≤ C_h (2R)^k/N_k.

Thus the infinitely many degrees above k do not destroy the growing-degree estimate.

## P22-B5 — Robust Rosenthal step

Status: PROVED, strengthened relative to the previous P22 run.

Fix z and write

S(z) = sum_(i=1)^n r_T(X_i,z)^2.

For centered independent variables

Y_i = r_T(X_i,z)^2 - E r_T(X_i,z)^2,

it is enough to use the conservative bound

||sum_i Y_i||_q
≤ C q [
  (sum_i ||Y_i||_2^2)^(1/2)
  + (sum_i ||Y_i||_q^q)^(1/q)
].

This follows from symmetrization and a standard Rosenthal inequality; Johnson–Schechtman–Zinn in fact give a better asymptotic constant.

Therefore

||S(z)-E S(z)||_q
≤ C_h q [
  sqrt(n) 3^k/N_k
  + n^(1/q) (2q)^k/N_k
].

Set q = R. Since n = d^R, n^(1/R) = d. Passing from one z to the maximum over n decoupled columns costs another factor at most d by the elementary Lq maximum inequality; independence of these maxima is not needed.

Relative to the mean n/N_k, the two error terms are at most

d R 3^k/sqrt(n) = d^(-R/2+O(1)) -> 0,

and

R d^2 (2R)^k/n = d^(-R+ell+O(1)) -> 0.

Thus

E max_j sum_i r_T(X_i,Xtilde_j)^2
= (1+o(1)) n/N_k.

This confirms that the proof does not rely on a delicate best Rosenthal constant.

## P22-B6 — KRM decoupling/NCK and tail isotropy

Status: PROVED.

Kaushik–Romberg–Muthukumar's proof decouples the off-diagonal empirical kernel matrix. Conditional on the original sample, the decoupled column matrices are independent. Their proof-level estimate has the form

E||Delta_tilde | X||
≤ C [sqrt(log(n) V) + log(n) L],

and, before their later crude maximum-entry relaxation,

L^2
≤ C E_(Xtilde) max_j sum_i r_T(X_i,Xtilde_j)^2.

The hypotheses hold here: iid inputs, positive semidefinite continuous bounded kernel r_T, unit diagonal, and exact centering E_Z r_T(x,Z)=0 because every tail degree is positive.

The correlation kernel is

G
= tau^(-2) sum_(s≥k) lambda_s^2 P_s(X,X).

Whole-tail monotonicity gives

G ≤ (lambda_k/tau) R_T

in PSD order, and

lambda_k/tau
= (tau_k/tau)/N_k
≤ 1/N_k.

Writing A = E||R_T-I|| gives the scalar recursion

A
≤ C_h [
  sqrt((n log n/N_k)(1+A))
  + log(n) sqrt(n/N_k)
] + o(1).

Since n/N_k = d^(-delta+o(1)) and log n is only order R^2,

E||R_T-I|| -> 0.

More quantitatively, for any fixed delta' < delta, eventually

E||R_T-I||
≤ C_h R^2 d^(-delta'/2).

Taking delta' = delta/2 makes this summable in ell. Therefore the event ||R_T-I|| > 1/2 has summable probability.

This proves the entire normalized infinite-tail Gram matrix is asymptotically the identity in operator norm.

## P22-B7 — Low-block empirical Gram concentration

Status: PROVED.

Let Psi(X_i) collect all orthonormal harmonic features of degree below k, so its dimension is D = D_<k.

The addition theorem gives the exact row norm

||Psi(X_i)||^2 = D,

and isotropy gives

E[Psi(X_i) Psi(X_i)^T] = I_D.

Apply matrix Chernoff to the independent PSD matrices Psi(X_i)Psi(X_i)^T. Each has largest eigenvalue exactly D and the sum of expectations is n I_D. For fixed eta in (0,1),

P(||Psi^T Psi/n - I_D|| > eta)
≤ 2 D exp(-c_eta n/D).

Because D/n = d^(-(1-delta)+o(1)), this failure probability is summable in ell.

Hence Psi^T Psi/n -> I in operator norm, in probability and almost surely along the prescribed sequence.

## P22-B8 — Exact RKHS low/high variational decomposition

Status: PROVED.

Let T = K_T(X,X), and let Lambda be the diagonal of low Mercer eigenvalues.

If a is the low harmonic coefficient vector, the high-frequency residual labels are r = y - Psi a. Orthogonality in the RKHS gives the exact minimum squared RKHS norm

J(a)
= a^T Lambda^(-1) a
  + (y-Psi a)^T T^(-1) (y-Psi a).

On the tail-isotropy event ||T/tau-I|| ≤ 1/2 define W = tau T^(-1). Then

(2/3) I ≤ W ≤ 2 I.

Differentiation gives the exact low coefficient vector

ahat = G0^(-1) Psi^T W y,

with

G0 = tau Lambda^(-1) + Psi^T W Psi.

If also ||Psi^T Psi/n-I|| ≤ 1/2, then

G0 ≥ (n/3) I,

so

||G0^(-1)|| ≤ 3/n.

No hard-edge estimate for the entire n by n Gaussian-kernel Gram matrix is required.

## P22-B9 — Noise contribution

Status: PROVED.

For pure noise y = epsilon,

ahat_noise = G0^(-1) Psi^T W epsilon.

Conditionally on the good design event,

E_epsilon ||ahat_noise||^2
≤ C sigma^2 D/n.

This is the low-frequency population prediction variance because the harmonic coordinates are L2 orthonormal.

Let

r_noise = epsilon - Psi ahat_noise.

The residual operator I - Psi G0^(-1) Psi^T W has bounded Euclidean operator norm on the same good event, hence

E_epsilon ||r_noise||^2 ≤ C n sigma^2.

The population covariance of tail kernel sections is

H_T = sum_(s≥k) lambda_s^2 P_s(X,X).

By Mercer monotonicity,

H_T ≤ lambda_k T

in PSD order. Therefore the population L2 energy of the high-frequency interpolant satisfies

E_epsilon ||fhat_(T,noise)||_2^2
≤ C sigma^2 n lambda_k/tau
≤ C sigma^2 n/N_k.

Thus, conditionally on the good design event,

E_epsilon[R_noise | X]
≤ C sigma^2 [D/n + n/N_k]
-> 0.

Gaussianity is stronger than needed for this second-moment calculation; centered independent noise with covariance sigma^2 I would suffice.

## P22-B10 — Fixed-degree signal contribution

Status: PROVED.

Write f_d = Psi theta with ||theta|| ≤ B. For noiseless labels, the exact identity is

ahat_sig - theta
= -G0^(-1) tau Lambda^(-1) theta.

Since the target degree q0 is fixed and lambda_s decreases in s,

||Lambda^(-1) theta||
≤ lambda_(q0)^(-1) B.

The r=0 Mercer term gives, for fixed q0,

lambda_(q0) ≥ c_(h,q0) d^(-q0).

Consequently

||ahat_sig-theta||^2
≤ C_(h,q0) B^2 d^(2q0)/n^2
-> 0.

The signal residual is Psi(theta-ahat_sig), so its squared Euclidean norm is at most C n ||theta-ahat_sig||^2. Applying H_T ≤ lambda_k T and lambda_k/tau ≤ 1/N_k gives high-frequency signal leakage

||fhat_(T,sig)||_2^2
≤ C_(h,q0) B^2 d^(2q0)/(n N_k)
-> 0.

Thus both low-frequency bias and high-frequency leakage vanish.

## P22-B11 — Conditional excess risk

Status: PROVED.

On the good design event,

E_epsilon[R_ell | X]
≤ C [
  sigma^2 (D_<k/n + n/N_k)
  + B^2 (d^(2q0)/n^2 + d^(2q0)/(n N_k))
].

Every term tends to zero.

Because R_ell is nonnegative, Markov's inequality over the training noise, together with the high-probability good design event, yields

R_ell -> 0 in probability.

This is exactly P04 Target 2 in the regime specified by P22.

## P22-B12 — Almost-sure strengthening

Status: PROVED.

Choose delta' < delta and zeta' < 1-delta. Eventually,

n/N_k ≤ d^(-delta'),

and

D_<k/n ≤ d^(-zeta').

The quantitative tail-isotropy failure probability is bounded by a summable sequence such as C_h R^2 d^(-delta'/2). The matrix-Chernoff low-block failure probability is also summable. On the good event, the conditional mean risk is bounded by a deterministic summable sequence because d = 2^(2^ell), n = d^(2^ell), and q0 is fixed.

Therefore, for every epsilon > 0,

sum_ell P(R_ell > epsilon) < infinity.

The first Borel–Cantelli lemma does not require independence. Hence under any coupling across levels having the stated marginals,

R_ell -> 0 almost surely.

## P22-OBS-01 — Counterexample to an overstrong growing-degree claim

Status: PROVED.

The fixed-degree signal hypothesis is essential.

Take signals in the critical harmonic space H_(d,k). Its dimension satisfies N_k/n -> infinity. Let theta be uniform on the unit coefficient sphere of H_(d,k), independently of the design, and suppose labels are noiseless.

Conditional on the design, the n labels reveal at most n linear measurements of theta. The component orthogonal to the row span is unobserved. Hence, even for an optimal estimator,

E_theta ||theta - thetahat||^2
≥ 1 - rank(Phi_k)/N_k
≥ 1 - n/N_k
-> 1.

Projecting any function estimator onto H_(d,k) can only decrease its total population L2 error, so the same Bayes lower bound applies to arbitrary estimators. By averaging over theta, for every d there exists a deterministic unit-L2 degree-k signal whose expected test error is at least 1-n/N_k.

Therefore bounded L2 norm alone is not enough when signal degree is allowed to grow to the critical harmonic range. The fixed-degree condition is substantive, not merely technical.

## Independent cross-track peer audit

AUDIT_FOR=P12, claim P12-SCALE-02.

Source: P12 Library file file_00000000936081f6a725f2d3d2568409.

Claim: if A_m = sigma_m Atilde_m with sigma_m > 0 and

M_(m,r)(A) = min over row subsets T of size m+r of the least singular value of A_T,

then

M_(m,r)(A_m)
= sigma_m M_(m,r)(Atilde_m).

Consequently, for k_m = r_m+1, the normalized exponent shifts by

(k_m/m) log sigma_m.

Verdict: PROVED.

Each row submatrix scales exactly by sigma_m, and every singular value scales exactly by sigma_m. The minimum preserves the equality. Therefore a triangular-array variance normalization is exponent-neutral when

(k_m/m) |log sigma_m| -> 0,

assuming the normalized entry laws retain the required uniform hypotheses.

This audit is independent of P22 and introduces no circularity.

## Failed routes and hostile checks

1. Fixed-degree Gegenbauer operator-norm corollaries cannot be used blindly at k -> infinity. Their hidden degree-dependent hypercontractive or maximum-entry factors are too large. DISPROVED AS A VALID SHORTCUT.

2. Replacing KRM's exact row-square quantity by a maximum-entry estimate loses too much at growing degree. REJECTED.

3. Pointwise kernel approximation or an empirical bulk spectral law alone does not imply benign interpolation. The inverse problem and low/high decomposition are essential. REJECTED.

4. The individual Mercer-eigenvalue ratio and the tail trace-mass ratio must not be confused:
lambda_(k+1)/lambda_k = O(1/d),
while tau_(k+1)/tau_k is asymptotic to gamma/(k+1) = O(1/R).

5. A sharp sqrt(q) Rosenthal variance coefficient is not required. The weaker C q form closes by a large margin.

6. Independence across ell is not required for the almost-sure strengthening; first Borel–Cantelli uses only summability.

7. A theorem covering all bounded-L2 signals whose degree grows to k is false by P22-OBS-01.

## Ledger

PROVED:
- P22-B1: exact Gaussian-kernel Mercer eigenvalue formula.
- P22-B1b: whole-tail Mercer eigenvalue monotonicity.
- P22-B2: exact harmonic multiplicities and the cutoff asymptotics N_k/n = d^(0.442695...+o(1)), D_<k/n = d^(-0.557305...+o(1)).
- P22-B3: dimension-free spherical-harmonic hypercontractivity at growing degree.
- P22-B4: entire infinite-tail mixture control at moment order q = R.
- P22-B5: conservative C q Rosenthal control is sufficient.
- P22-B6: KRM proof-level row-square decoupling/NCK argument yields E||K_T/tau-I|| -> 0.
- P22-B7: low-frequency empirical Gram concentration.
- P22-B8: exact RKHS low/high variational decomposition and inverse normal-matrix control.
- P22-B9: low- and high-frequency noise risk vanish.
- P22-B10: fixed-degree signal bias and high-frequency signal leakage vanish.
- P22-B11: requested conditional clean-test excess prediction risk converges to zero in probability.
- P22-B12: the same risk converges to zero almost surely along the prescribed sequence under any coupling with the correct marginals.
- P22-OBS-01: bounded-L2 growing-degree extension fails at critical degree k.
- AUDIT_FOR=P12-SCALE-02: exact variance-normalization lemma.

CONDITIONAL / PROTOCOL:
- P04 Target 2 is mathematically candidate-complete.
- Formal ProofNet portfolio closure still requires the specified two OTHER independent complete audits.

DISPROVED / INVALID:
- Uniform use of a fixed-degree Gegenbauer corollary at growing k.
- Maximum-entry replacement of the KRM row-square term.
- Inferring benign interpolation from pointwise kernel approximation or spectral bulk alone.
- Treating tau_(k+1)/tau_k as O(1/d).
- Uniform bounded-L2 signal theorem all the way to critical growing degree k.

OPEN:
- The remaining required other-worker complete audit(s).
- A manuscript-ready consolidation of P04 and P22 with all normalizations and the exact risk definition.
- The largest subcritical growing signal degree q_ell for which benign interpolation still holds.
- The varying-bandwidth regime h = h_ell.

## Next attack

There is no identified mathematical gap in the stated fixed-bandwidth, fixed-signal-degree target. The highest-value next step is external certification: a different worker should audit the exact Mercer formula, the KRM proof-level L term, the q=R row-square moment calculation, the RKHS variational identity, and the final conditional-risk normalization.

For new mathematics, the natural extension is the growing-signal-degree window. The crude good-event bounds already suggest low signal bias of order d^(2 q_ell)/n^2 and signal tail leakage of order d^(2 q_ell)/(n N_k), so a substantial subcritical growing window may be benign. P22-OBS-01 proves that uniform extension all the way to q_ell = k is impossible.

## Final verdict

For the actual fixed-bandwidth Gaussian-kernel minimum-norm interpolant with iid uniform sphere inputs, the prescribed n_ell and d_ell, Gaussian training noise variance sigma^2, and every fixed-degree spherical-polynomial signal sequence of uniformly bounded L2 norm,

R_ell = E_X0[(fhat_(d_ell)(X0)-f_(d_ell)(X0))^2 | training data]

converges to zero in probability.

Along the prescribed sequence it in fact converges almost surely under any coupling across levels with the correct marginals.

Formal ProofNet closure remains withheld only because the external two-other-auditor protocol requirement is not yet satisfied.
