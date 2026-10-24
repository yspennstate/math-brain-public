SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T14:12:30Z.
attacking: exact tent-scale regularity hierarchy for raw output laws, plus a C^{1,1} ruled-majority trace estimate from the completed account02/B15 one-sheet theorem.

# Tent-scale regularity hierarchy and ruled-majority curvature

Status: `ESSENTIAL_STEP_APPLIED / TENT_REGULARITY_TRICHOTOMY / RULED_MAJORITY_C11`. The unrestricted QFORM theorem remains OPEN. The shared continuous-representative claim remains separate and OPEN.

## 1. Scope and corrections consumed

Target: independent real X_i with densities <=1, symmetric A with s_3(A)>=1, Q=X^TAX. No moments, smoothness, compact support, or post-rotation independence are assumed.

Consumed live corrections include: no law-uniform pointwise quadratic Fourier decay; no independence after spectral rotation; no projection/X-ray-only control of the minority two-sheet trace; no arbitrary-joint rank-three coarea shortcut; no positive conditional projection-density moment shortcut. Nothing below uses those interfaces.

Partner used: account02/B15 handoff `20260923T130525Z-account02-B15-qform-auto11.md`, whose completed rough-input one-sheet theorem gives an original-coordinate indefinite physical 3x3 block a majority-output submeasure with density cap C_+, and whose target-valid phase-aligned sequence gives a quantitative shrinking-window obstruction.

## 2. Universal triangular approximate identity

For epsilon>0 define

K_epsilon(x) := (epsilon-|x|)_+ / epsilon^2,

so K_epsilon>=0 and integral K_epsilon=1. For a finite positive Borel measure mu on R put

H_epsilon[mu](y) := (K_epsilon*mu)(y).

Also define the density height functional

D_infty(mu) := inf{C>=0: mu(E)<=C |E| for every Borel E},

with D_infty=+infinity if no such C exists.

### Theorem 2.1 (exact height characterization)

For every finite positive measure mu,

D_infty(mu) = sup_{0<epsilon<=1} ||H_epsilon[mu]||_infty.

Proof. If mu=p dx and ||p||_infty<=D, Young's inequality gives ||K_epsilon*p||_infty<=D for every epsilon, so the right side is <=D_infty(mu).

Conversely suppose ||H_epsilon||_infty<=M for all 0<epsilon<=1. For every nonnegative phi in C_c(R),

int phi(y) H_epsilon(y) dy = int (phi*K_epsilon)(u) dmu(u) -> int phi dmu

because K_epsilon is an approximate identity. The left side is <=M int phi. Hence int phi dmu<=M int phi for every nonnegative compactly supported continuous phi, so mu<=M dx. Thus D_infty(mu)<=M. Taking the optimal M proves equality, including the extended-real case. QED.

This theorem does not presuppose absolute continuity.

### Theorem 2.2 (continuity is convergence, not boundedness)

For a finite positive measure mu:

(a) mu has a continuous density p if and only if H_epsilon[mu] converges locally uniformly on R as epsilon downarrow0. The locally uniform limit is p.

(b) mu has a density p in C_0(R) if and only if H_epsilon[mu] converges uniformly on all of R as epsilon downarrow0.

Proof. If p is continuous, then on every compact J it is uniformly continuous on J+[-1,1]. Since K_epsilon is supported in [-epsilon,epsilon], the standard approximate-identity estimate gives sup_{y in J}|K_epsilon*p(y)-p(y)|->0. If p is in C_0, p is uniformly continuous on R and the convergence is global uniform.

Conversely, every H_epsilon is continuous. A locally uniform limit p is continuous. For phi in C_c, both local uniform convergence and approximate-identity weak convergence give

int phi p dx = lim int phi H_epsilon dx = int phi dmu,

so mu=p dx. If convergence is global uniform, the limit is a uniform limit of C_0 functions, hence belongs to C_0. QED.

Thus the logical hierarchy is exact:

- absolute continuity: existence of some L^1 density;
- bounded density: uniform boundedness of the normalized tent family H_epsilon;
- continuous density: local-uniform convergence of H_epsilon;
- C_0 density: global-uniform convergence of H_epsilon.

Uniform boundedness alone does not imply convergence. For example, the measure 1_[0,1] dx has D_infty=1 but no continuous representative.

### Theorem 2.3 (quantitative Hölder implication)

If p has global Hölder seminorm [p]_{C^{0,alpha}}<infinity for 0<alpha<=1, then

||K_epsilon*p-p||_infty <= m_alpha [p]_{C^{0,alpha}} epsilon^alpha,

where

m_alpha = integral_{-1}^1 |v|^alpha (1-|v|) dv = 2/((alpha+1)(alpha+2)).

Proof. Write K_epsilon*p(y)=int_{-1}^1 (1-|v|)p(y-epsilon v)dv and apply the Hölder bound pointwise. QED.

No converse Hölder claim is used.

## 3. Exact QFORM fixed-unit normal form, with continuity separated

Let s(A)=s_3(A), the third largest eigenvalue modulus. Let mu_A be the law of Q_A=X^TAX and let T be the owner target class s(A)>=1.

Define

C_* := sup_{(A,X) in T} s(A) D_infty(mu_A),

allowing C_*=+infinity. Then

C_* = sup_{(A,X) in T} s(A) ||H_1[mu_A]||_infty.

Proof. The <= direction for the fixed-unit functional is immediate from Theorem 2.1. For the reverse direction, fix a target (A,X), epsilon in (0,1], and y in R. The scaled matrix A_epsilon=A/epsilon is still target-valid and s(A_epsilon)=s(A)/epsilon. Since Q_{A_epsilon}=Q_A/epsilon,

H_1[mu_{A_epsilon}](y/epsilon)
 = E(1-|Q_A/epsilon-y/epsilon|)_+
 = epsilon H_epsilon[mu_A](y).

Therefore

s(A_epsilon) H_1[mu_{A_epsilon}](y/epsilon)
 = s(A) H_epsilon[mu_A](y).

Taking suprema over y and epsilon and invoking Theorem 2.1 proves equality. QED.

This is a useful logical separation. The central owner theorem asks only for a universal bound on one fixed continuous unit-scale profile after spectral scaling. Raw continuity would additionally require, for each fixed target law, local-uniform convergence of its entire shrinking tent family. No continuity premise is needed to obtain D_infty.

## 4. Qualitative absolute continuity under much weaker assumptions

If A is any nonzero real symmetric matrix and the full input law is absolutely continuous with respect to Lebesgue measure, then Q(x)=x^TAx has an absolutely continuous pushforward law.

Proof. The critical set of Q is ker A, a proper linear subspace and hence Lebesgue-null. If E subset R is Lebesgue-null, define Omega_k={|x|<=k, |grad Q(x)|>=1/k}. Coarea gives

int_{Q^{-1}(E) cap Omega_k} |grad Q(x)| dx
 = int_E H^{n-1}(Q^{-1}(t) cap Omega_k) dt =0.

Since |grad Q|>=1/k on Omega_k, Q^{-1}(E) cap Omega_k is Lebesgue-null. The union of the Omega_k covers R^n\ker A. Hence Q^{-1}(E) is Lebesgue-null, and every absolutely continuous input law assigns it mass zero. QED.

Thus independence, the cap-one hypothesis, and three large eigenvalues are unnecessary for qualitative absolute continuity. They are needed only for the desired universal quantitative height theorem.

## 5. Applying the completed account02/B15 one-sheet theorem to regularity

Take an invertible indefinite ORIGINAL-coordinate physical block B=A_{S,S}. Condition only on the outside original coordinates. The completed account02/B15 rough-input theorem supplies a majority/one-sheet output submeasure mu_+ satisfying

mu_+ <= C_+ dx,

where, for spectral magnitudes lambda_1,lambda_2>0 and mu>0 in signature (+,+,-),

C_+ = (lambda_1 lambda_2 mu)^(-1/2)
      int_0^{2pi} [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta

and in particular C_+<=pi sqrt(2)/kappa with kappa=min(lambda_1,lambda_2,mu). The other indefinite signature follows by reflection. Arbitrary outside quadratic curvature and cross couplings are allowed by the partner theorem.

Let p_+ be the density of mu_+, ||p_+||_infty<=C_+, and define the unnormalized triangular trace

T_{epsilon,+}(y)
 := int (epsilon-|u-y|)_+ dmu_+(u)
 = epsilon^2 H_epsilon[mu_+](y).

The partner's stated applied inequality is exactly

T_{epsilon,+}(y) <= C_+ epsilon^2.

There is a stronger regularity consequence which does not require p_+ to be continuous.

### Theorem 5.1 (ruled-majority C^{1,1} trace)

For every epsilon>0,

T_{epsilon,+} in C^{1,1}(R),

||T'_{epsilon,+}||_infty <= min(mu_+(R), 2 C_+ epsilon),

Lip(T'_{epsilon,+}) <= 4 C_+.

Equivalently, almost everywhere,

T''_{epsilon,+}(y)
 = p_+(y+epsilon)-2p_+(y)+p_+(y-epsilon),

so ||T''_{epsilon,+}||_infty<=4C_+.

Proof. Put k_epsilon(x)=(epsilon-|x|)_+. Its derivative is +1 on (-epsilon,0), -1 on (0,epsilon), zero elsewhere. Therefore

T'_{epsilon,+}(y)
 = int_y^{y+epsilon} p_+(u)du - int_{y-epsilon}^y p_+(u)du,

which is continuous. The mass bound gives |T'|<=mu_+(R); the density cap and total length 2epsilon give |T'|<=2C_+epsilon. Differentiating the two absolutely continuous interval integrals gives the displayed second derivative almost everywhere, bounded by 4C_+. Hence T' has a 4C_+-Lipschitz representative. QED.

In particular, for every y,h,

|T_{epsilon,+}(y+h)-2T_{epsilon,+}(y)+T_{epsilon,+}(y-h)| <= 4 C_+ h^2.

With the crude partner constant this is <=4 pi sqrt(2) h^2/kappa.

### Corollary 5.2 (curvature must be paid by the minority/two-sheet term)

Write the full output measure as mu_Q=mu_++mu_- according to the partner majority event and its complement, and let T_epsilon=T_{epsilon,+}+T_{epsilon,-}. Then for every y,h,

T_{epsilon,-}(y) >= [
  T_epsilon(y)
  - (T_epsilon(y-h)+T_epsilon(y+h))/2
  - 2 C_+ h^2
]_+.

Proof. Let G=T_epsilon(y)-(T_epsilon(y-h)+T_epsilon(y+h))/2 and similarly G_+,G_-. The preceding second-difference estimate gives |G_+|<=2C_+h^2. Since T_{epsilon,-} is nonnegative,

G_- <= T_{epsilon,-}(y).

Thus T_{epsilon,-}(y)>=G-G_+>=G-2C_+h^2, and taking positive parts proves the claim. QED.

This is an actual quantitative use of the completed partner result: the ruled majority component is not merely height-bounded; after triangular probing it has a uniform C^{1,1} curvature budget. Any sharper concavity in the full local small-ball profile must come from the still-unpaid minority/two-sheet product component.

## 6. Applying the partner high-frequency obstruction to the SAME tent kernel

The newest account02/B15 handoff supplies a target-valid sequence built from smooth compact cap-one sources for fixed A=I_3. Along s_m->infinity, the corresponding smooth output densities p_m and a continuous bounded weak limit p satisfy

|hat p_m(s_m)| >= 27/64,

hat p(s_m) ->0,

and all p_m,p are supported in [3,300].

This can be transferred directly to the normalized tent family, sharpening the warning relevant to Theorem 2.2.

Set

r_m := pi/s_m,

q_m := K_{r_m}*(p_m-p).

The Fourier multiplier of K_r is

hat K_r(xi) = [sin(xi r/2)/(xi r/2)]^2.

Hence at xi=s_m,

hat K_{r_m}(s_m)=4/pi^2,

so

liminf_m |hat q_m(s_m)| >= (4/pi^2)(27/64)=27/(16pi^2).

Since q_m is supported in an interval of length 297+2r_m,

||q_m||_infty >= ||q_m||_1/(297+2r_m) >= |hat q_m(s_m)|/(297+2r_m).

Therefore

liminf_m ||K_{r_m}*p_m-K_{r_m}*p||_infty
 >= 27/(4752 pi^2)
 > 5.75e-4.

Thus even for fixed A=I_3, smooth compact cap-one inputs, smooth approximating output densities, a continuous bounded limit, common compact support, and a uniform raw height cap, there is NO source-uniform shrinking-scale tent-desmoothing statement along arbitrary weak approximations. Fixed-scale weak trace is safe; shrinking-scale normalized trace is not.

This is fully consistent with Theorem 2.2: continuity is a statement about epsilon->0 for each fixed law, not a uniform interchange of source limit m->infinity and desmoothing scale r_m->0.

## 7. Consequences for the owner target

The B15 ledger is now exact.

1. Absolute continuity is qualitative and already follows from A!=0 plus absolute continuity of the joint source.
2. Essential boundedness is exactly uniform boundedness of the normalized triangular approximate-identity family, and by spectral homogeneity it is exactly the single fixed-unit tent functional over the owner target class.
3. Continuous density is strictly a convergence assertion for the shrinking tent family, not part of the central height implication.
4. On any completed ruled majority branch, the triangular trace has a quantitative C^{1,1} budget 4C_+; excess local concavity is forced into the minority/two-sheet term.
5. The partner phase-aligned example rules out using weak source convergence plus continuity to justify normalized shrinking-window convergence uniformly.

The first unpaid implication is still product-sensitive: control the minority/two-sheet triangular trace, or show the simultaneous minority regime forces an already-paid ridge/volume/grouped-coordinate branch. The live X-ray-only correction prevents replacing that term by a generic projection bound.

No rotated-independence assumption, law-uniform pointwise Fourier decay, arbitrary-joint coarea bound, or projection-only shortcut is used here.
