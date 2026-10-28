SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B14, 2026-09-22T22:36:55Z.
attacking: translation/localization at the integrated-Fourier level: same-extreme L^p localization and the first decisive obstruction to positive weighted-moment regularity.

# account03/B14 — same-extreme Fourier localization and a target-valid weighted-moment obstruction

Run: `20260922T223655Z-account03-B14-QFORM-r20`
Programme: `QFORM-DENSITY-3EIG-20260922`
Status: `SUPPORTING_THEOREM_PLUS_REFUTED_INTERMEDIATE_MECHANISM / FULL_QFORM_OPEN / CONTINUITY_FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and scope

The full target remains OPEN: for every finite n, every independent real X_i with probability densities 0<=f_i<=1, and every real symmetric A with at least three eigenvalues of absolute value at least one, prove that Q=X^T A X has a density with one universal essential-supremum bound, or give a valid counterexample. Continuity is a separate requested conclusion.

This run uses no Gaussian, log-concave, moment, compact-support, connected-support, or post-rotation independence assumption. In particular it does not use the refuted law-uniform pointwise van-der-Corput estimate, arbitrary-joint rank-three coarea, conditional projection-density moments, scalar conditional suprema, or a bounded fragment-count/diameter reduction.

The B14 question addressed here is whether the current law-level localization can be pushed through the actual nonlinear Fourier energies used by the proof programme without losing the iid-copy structure, and whether a positive weighted Fourier moment can plausibly be made uniform over the full target class.

## 2. Partner theorem actually applied

Designated partner account04/B14 proved `QFORM-LAW-LEVEL-FINITE-MIXTURE-LOCALIZATION-v1` at

`yspennstate/math-open-problems@321ec7899f4972d125d641408512fe9e5e9dcf4c`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T201507Z-account04-B14-mixture-localization-r4/REPORT.md`.

Let D_n denote all product probability laws on R^n whose one-dimensional densities are bounded by one. Let F_n denote product laws whose marginals are indicators 1_E of compact finite unions of intervals with |E|=1. The partner theorem gives, for every mu in D_n, finite convex mixtures

mu_r = sum_a theta_{r,a} nu_{r,a},   nu_{r,a} in F_n,

such that ||mu_r-mu||_TV ->0. This reduction has no support-radius, fragment-count, separation, translation or moment parameter.

The theorem below applies that result to an actual family of Fourier inequalities and strictly strengthens the p=1 localization and the two-different-extremes Fejer upper bound from the preceding B14 run.

## 3. Exact same-extreme L^p Fourier localization

Let P:R^n->R be any measurable map, let w:R->[0,infinity] be Borel, and let 1<=p<infinity. For a probability law mu define

J_{p,w}(P;mu)
 = int_R w(t) | E_mu exp(i t P(X)) |^p dt,

with values in [0,infinity].

### Theorem 3.1 — `QFORM-SAME-EXTREME-LP-FOURIER-LOCALIZATION-v1`

For every measurable P, every nonnegative Borel w and every p>=1,

    sup_{mu in D_n} J_{p,w}(P;mu)
      = sup_{nu in F_n} J_{p,w}(P;nu).                    (3.1)

The equality is exact, including when either side is infinite.

### Proof

Fix mu in D_n and use the partner approximation mu_r=sum_a theta_{r,a}nu_{r,a}. For each fixed t,

E_{mu_r} e^{itP} = sum_a theta_{r,a} E_{nu_{r,a}}e^{itP}.

Because z -> |z|^p is convex for p>=1, Jensen gives

|E_{mu_r}e^{itP}|^p
 <= sum_a theta_{r,a}|E_{nu_{r,a}}e^{itP}|^p.

Multiplying by w(t)>=0 and integrating,

J_{p,w}(P;mu_r)
 <= sum_a theta_{r,a}J_{p,w}(P;nu_{r,a})
 <= sup_{nu in F_n}J_{p,w}(P;nu).                         (3.2)

Total-variation convergence implies convergence of expectations of every bounded measurable function, hence

E_{mu_r}e^{itP} -> E_mu e^{itP}

for each t. Fatou's lemma therefore yields

J_{p,w}(P;mu)
 <= liminf_r J_{p,w}(P;mu_r)
 <= sup_{nu in F_n}J_{p,w}(P;nu).                         (3.3)

Taking the supremum over D_n gives one inequality, while F_n subset D_n gives the reverse. QED.

### Translation quotient

For P_{A,d}(x)=x^T A x+d^Tx with symmetric A, write

d=d_R+d_0,  d_R in Range(A),  d_0=P_{ker A}d.

Choose h with 2Ah=-d_R and translate physical coordinates x=y+h. Then

P_{A,d}(y+h)=y^T A y+d_0^Ty+constant.

Physical translation preserves coordinate independence, every density cap, and F_n. The additive constant is a unimodular Fourier factor. Consequently (3.1) depends on d only through P_{ker A}d. Range-compatible translations cost exactly zero, including for unbounded or arbitrarily fragmented supports.

## 4. Same-law Fejer localization, not two different extreme laws

For T>0 define

w_T(t)=(1-|t|/T)_+,

and the positive Fejer kernel

K_T(s)=int_{-T}^T w_T(t)e^{its}dt
      =T [sin(Ts/2)/(Ts/2)]^2 >=0.

For iid X,X' with common law mu and any real measurable P,

int_{-T}^T w_T(t)|phi_P(t)|^2dt
 =E_mu K_T(P(X)-P(X')).                                      (4.1)

Taking p=2 and w=w_T in Theorem 3.1 gives the exact same-extreme identity

boxed{
 sup_{mu in D_n} int_{-T}^T w_T(t)|phi_P(t)|^2dt
 =sup_{nu in F_n} int_{-T}^T w_T(t)|phi_P(t)|^2dt
 =sup_{nu in F_n} E K_T(P(U)-P(U')),
}                                                             (4.2)

where U,U' are iid with the SAME extreme law nu.

This is stronger than the preceding positive two-copy compiler, whose multilinear upper bound allowed two different extreme laws. The same-law identity follows because the Fourier energy is convex as a functional of the single law. It is directly decoupling-ready and avoids any claim that a conjugate sum/difference conditioning preserves density caps or independence.

## 5. A decisive target-valid obstruction to positive weighted Fourier moments

The preceding run showed that a uniform bound on

int |t|^alpha |phi_Q(t)|dt

would transfer continuity and a Hölder modulus. The following construction shows that no positive polynomial Fourier weight can be uniformly bounded under the target hypotheses, even on a fixed compact support and even within the diagonal solved subclass.

### Theorem 5.1 — `QFORM-NO-UNIFORM-POSITIVE-WEIGHT-FOURIER-MOMENT-v1`

Fix any beta>0 and any p>0. Then

sup int_R (1+|t|)^beta |phi_Q(t)|^p dt = infinity,             (5.1)

where the supremum may be restricted to the exact target matrix A=I_3 and to iid cap-one marginals that are indicators of compact finite unions of intervals contained in the fixed interval [1,10].

Thus no full-target proof can obtain continuity by first proving one law-uniform positive polynomial weighted Fourier moment. This does NOT refute a uniform unweighted L^1 Fourier estimate, the bounded-density conjecture, or continuity itself.

### Proof

Set R=10 and delta=pi/3. Fix s>=1. For every integer k satisfying

s+delta <= 2pi k <= sR^2-delta,

define

I_{k,s}=[ sqrt((2pi k-delta)/s), sqrt((2pi k+delta)/s) ].       (5.2)

Every such interval lies in [1,R], and for x in I_{k,s},

|s x^2-2pi k|<=delta,

so

cos(sx^2)>=cos(delta)=1/2.                                     (5.3)

The number N_s of admissible k is bounded below by interval length divided by lattice spacing minus one:

N_s >= [s(R^2-1)-2delta]/(2pi)-1
    = 99s/(2pi)-4/3.                                           (5.4)

For each such k,

|I_{k,s}|
 = (2delta/s)/[sqrt((2pi k+delta)/s)+sqrt((2pi k-delta)/s)]
 >= delta/(sR).                                                (5.5)

Hence the total favorable length obeys

sum_k |I_{k,s}|
 >= [delta/(sR)] [99s/(2pi)-4/3]
 = 99/60 - 4pi/(90s)
 > 1                                                         (5.6)

for every s>=1.

Therefore one may choose a compact finite union E_s of subintervals of the I_{k,s} having exactly |E_s|=1. Put f_s=1_{E_s}. It is a probability density satisfying 0<=f_s<=1 and supp(f_s) subset [1,10]. Define

g_s(t)=int_{E_s} exp(itx^2) dx.

By (5.3),

Re g_s(s)>=1/2,

and hence |g_s(s)|>=1/2. Let X_1,X_2,X_3 be iid with density f_s and put

Q_s=X_1^2+X_2^2+X_3^2.

This is the exact target matrix A=I_3. Independence gives

phi_s(t)=g_s(t)^3,

so

|phi_s(s)|>=1/8.                                               (5.7)

Because 0<=Q_s<=3R^2=300,

|phi_s'(t)|=|E iQ_s e^{itQ_s}|<=300.                           (5.8)

Let eta=1/(48R^2)=1/4800. If |t-s|<=eta, then by (5.7)-(5.8),

|phi_s(t)|>=1/8-300 eta=1/16.                                  (5.9)

Consequently

int_R (1+|t|)^beta |phi_s(t)|^p dt
 >= 2 eta * 16^{-p} * (1+s-eta)^beta,

which tends to infinity as s->infinity. This proves (5.1). QED.

### Why this is stronger than the pointwise-decay correction

The known phase-aligned construction already refutes a universal pointwise envelope |phi(t)|<=C|t|^{-gamma}. The present theorem converts the aligned bump into a fixed-width frequency window, using the bounded output range to obtain a uniform Lipschitz constant. The resulting positive weighted integral itself diverges along a sequence of admissible target laws.

The example is already in the partner's finite-fragment extreme class. Its support diameter is fixed; what grows is the number/oscillation scale of the fragments, consistent with the earlier B14 correction that no universal fragment-count cap preserves the relevant extremal behavior.

## 6. A useful conditional closure criterion, and exactly why it is not automatic

Although Theorem 5.1 rules out a universal positive weighted-moment premise, such a premise can still close specific structural branches where additional mixing proves it.

Suppose

Q=cX^2+gamma X+R(Y),

where X is independent of Y, f_X<=1, and c!=0. Completing the square and using the standard one-square Hausdorff-Young estimate gives

||phi_{cX^2+gamma X}||_3
 <= (2pi)^(1/3) 5^(2/3) |c|^(-1/3).                            (6.1)

Assume for some beta>1/3 that

M_beta=int_R (1+|t|)^beta |phi_R(t)|^2dt<infinity.             (6.2)

Then

int |phi_R(t)|^(3/2)dt
 =int [(1+|t|)^(beta/2)|phi_R|]^(3/2)(1+|t|)^(-3beta/4)dt

and Holder with exponents 4/3 and 4 yields

||phi_R||_{3/2}
 <= M_beta^(1/2) [2/(3beta-1)]^(1/6).                          (6.3)

Since phi_Q is the product of the two independent characteristic functions, Holder with exponents 3 and 3/2 gives

||phi_Q||_1
 <= (2pi)^(1/3)5^(2/3)|c|^(-1/3)
    M_beta^(1/2)[2/(3beta-1)]^(1/6).                           (6.4)

Thus Q has a bounded continuous density with

||p_Q||_infinity
 <= (2pi)^(-2/3)5^(2/3)|c|^(-1/3)
    M_beta^(1/2)[2/(3beta-1)]^(1/6).                           (6.5)

Theorem 3.1 says that the worst-case value of M_beta for a fixed remainder map R is exactly localizable to finite-fragment product laws. Theorem 5.1 says one may not infer a dimension-free M_beta merely from the original density caps; a structural smoothing theorem is still required.

## 7. What this pays and what remains unpaid

This run changes the B14 interface in two ways.

1. Every L^p Fourier energy with p>=1, including the Fejer L^2 collision functional with iid copies, has an exact zero-loss reduction to compact finite-fragment extreme product laws. There is no support-radius, separation, fragment-count, translation or moment tax.
2. The tempting upgrade from unweighted Fourier integrability to a uniform positive polynomial weighted moment is decisively unavailable under the full hypotheses, even for A=I_3 and fixed compact support. Weighted moments remain branch-specific tools only.

Therefore the highest-value remaining B14-compatible route is the unweighted one: preserve same-law/global finite-fragment localization while proving a dimension-free unweighted L^1 Fourier estimate or direct small-ball bound by aggregate-before-inversion geometry. Any continuation that tries to buy full-target continuity through a universal |t|^beta Fourier moment should be abandoned unless it adds genuinely stronger structural hypotheses and states them explicitly.

## 8. Source/correction discipline


Repository retrieval was genuine, but no authenticated native receiver-memory use occurred, so `WITHOUT_VERIFIED_BRAIN` remains required. No scheduler mutation, task creation, cross-account action, email/Drive action, notification enablement, public release, remote workflow, paid model/API/Codex call, credential use, or unrelated private transcript was used.
