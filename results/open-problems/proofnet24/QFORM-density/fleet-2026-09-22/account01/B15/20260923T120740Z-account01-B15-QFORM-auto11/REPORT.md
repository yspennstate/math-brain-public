SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T12:07:40Z.
attacking: a target-level regularity/closure lemma that turns Gaussian heat bounds into the raw L-infinity statement without assuming continuity, and a fractional original-coordinate majority-cone compiler using the completed account02/B15 theorem.

# QFORM account01/B15 — Gaussian regularity trichotomy and fractional majority-cone cover

**Status:** PROVED SUPPORTING LEMMAS / FULL QFORM OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and sources actually used

The target is unchanged: for arbitrary independent real coordinates with densities `0<=f_i<=1` and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound. Continuity is a separate stronger conclusion.


The completed assigned-partner result actually applied below is:

- `yspennstate/math-open-problems@4a7b432e38619707420962a272805f9646ad7e59`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T090720Z-account02-B15-QFORM-auto11/REPORT.md`.

For every invertible indefinite ORIGINAL-coordinate physical triple `S`, with `B=A_SS`, it proves that the majority/one-sheet output submeasure

`mu_S^+(E)=P(Q in E, G_S)`

satisfies

`mu_S^+ <= C_S dx`,                                                   (1.1)

for arbitrary rough cap-one product marginals and arbitrary outside quadratic coefficients/couplings. If the majority-sign eigenvalue magnitudes are `lambda_1,lambda_2` and the minority magnitude is `mu`, then

`C_S=(lambda_1 lambda_2 mu)^(-1/2) int_0^(2pi) [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2)dtheta`

and, with `kappa_S=sigma_min(B)`,

`C_S <= pi sqrt(2)/kappa_S`.                                         (1.2)

Reflection handles the opposite indefinite signature.

## 2. Absolute continuity is already unconditional at the qualitative level

### Lemma 2.1 — nonzero quadratic pushforwards of absolutely continuous laws are absolutely continuous

Let `F dx` be any absolutely continuous probability law on `R^n`; independence and the cap `F<=1` are not needed here. If `A` is any nonzero real symmetric matrix and `q(x)=x^T A x`, then `q_#(F dx)` is absolutely continuous with respect to Lebesgue measure on `R`.

**Proof.** The critical set of `q` is `ker A`, because `grad q(x)=2Ax`. Since `A!=0`, `ker A` is a proper linear subspace and hence Lebesgue-null. Let `N subset R` be null. Apply coarea on bounded balls and then let the radius grow:

`int_(q^{-1}(N)) F(x)|grad q(x)| dx`
` = int_N [int_(q^{-1}(t)) F dH^(n-1)] dt =0`.                       (2.1)

Thus `F(x)|grad q(x)|=0` a.e. on `q^{-1}(N)`. Off `ker A`, the gradient is nonzero, so `F=0` a.e. on `q^{-1}(N)\ker A`. The remaining part lies in the null set `ker A`. Hence

`P(q(X) in N)=int_(q^{-1}(N))F dx=0`.                               (2.2)

So the owner target's absolute-continuity part holds far below the three-large-eigenvalue assumptions. The unresolved theorem is quantitative `L^infinity`, not existence of a density. `square`

## 3. A target-level Gaussian regularity trichotomy

Let

`gamma_eps(u)=(sqrt(2pi) eps)^(-1) exp(-u^2/(2 eps^2))`

and for any probability measure `mu` on `R` put

`H_eps=mu*gamma_eps`.

Define the extended density-height functional

`D_inf(mu)=inf{C>=0: mu(E)<=C |E| for every Borel E}`,               (3.1)

with value `+infinity` when no such finite `C` exists. If finite, `mu=p dx` and `D_inf(mu)=||p||_infinity`.

### Theorem 3.1 — exact heat characterization of bounded density

For every probability measure `mu`, without assuming prior absolute continuity,

`boxed(D_inf(mu)=sup_(0<eps<=1) ||H_eps||_infinity)`                 (3.2)

in the extended interval `[0,+infinity]`.

**Proof.** If `mu<=C dx`, convolution with the probability kernel `gamma_eps` gives `H_eps<=C`, so the right side is at most `D_inf(mu)`.

Conversely, suppose the right side is `M<infinity`. For every nonnegative `phi in C_c(R)`, approximate-identity convergence gives

`int phi dmu = lim_(eps->0) int phi(y) H_eps(y) dy`
`            <= M int phi(y)dy`.                                    (3.3)

Hence `mu<=M dx`. Thus `D_inf(mu)<=M`. The infinite case follows by contraposition. `square`

This proves the central bounded-density conclusion from uniform heat height alone; no raw continuity is used.

### Theorem 3.2 — exact heat characterization of continuous density

A probability measure `mu` has a density `p in C_0(R)` if and only if `H_eps` converges in `L^infinity(R)` as `eps->0`. In that case the uniform limit is `p`.

**Proof.** If `p in C_0`, then `p` is uniformly continuous and the Gaussian approximate identity gives `||p*gamma_eps-p||_infinity->0`.

Conversely, if `H_eps->h` uniformly, then `h in C_0` because every `H_eps` is in `C_0` and `C_0` is closed under uniform convergence. For every `phi in C_c`,

`int phi h dx = lim int phi H_eps dx = int phi dmu`,                 (3.4)

so `mu=h dx`. `square`

Therefore the regularity hierarchy is exact:

- absolute continuity: qualitative and already automatic for nonzero quadratic forms;
- bounded density: uniform boundedness of the heat regularizations;
- continuous density: the strictly stronger requirement of **uniform convergence** of those heat regularizations.

Boundedness alone cannot be used to infer continuity. For example, the probability density `1_[0,1]` has heat height at most one at every scale but has no continuous representative. This example is only a logical regularity witness, not a QFORM counterexample.

For every fixed `eps>0`, `H_eps` is `C^infinity` and

`||H_eps^(k)||_infinity <= ||gamma_eps^(k)||_infinity`,              (3.5)

so the heat surrogate has universal smoothness even when the raw density is merely measurable.

## 4. Exact fixed-unit Gaussian normal form for the full QFORM constant

Let `s(A)=s_3(A)`, the third largest eigenvalue modulus, and let `mu_Q` be the output law. Define the sharp extended owner constant

`C_* = sup_target s(A) D_inf(mu_Q)`.                                 (4.1)

Define also the fixed-unit heat constant

`C_G = sup_target s(A) ||mu_Q*gamma_1||_infinity`.                   (4.2)

### Theorem 4.1

`boxed(C_*=C_G)`                                                       (4.3)

with equality allowed to be `+infinity`.

**Proof.** The inequality `C_G<=C_*` is immediate from convolution contraction when `D_inf` is finite, and remains true in the extended sense.

For the reverse inequality, fix one target `A` and `0<eps<=1`. Put

`A_eps=A/eps`, `Q_eps=Q/eps`, `s(A_eps)=s(A)/eps`.

The scaled matrix is still an admissible target. Directly,

`(mu_(Q/eps)*gamma_1)(y)=eps (mu_Q*gamma_eps)(eps y)`.                (4.4)

Hence

`(s(A)/eps)||mu_(Q/eps)*gamma_1||_infinity`
` = s(A)||mu_Q*gamma_eps||_infinity <= C_G`.                         (4.5)

Taking the supremum over `eps->0` and using Theorem 3.1 gives

`s(A)D_inf(mu_Q)<=C_G`.                                               (4.6)

Then take the supremum over targets. `square`

This is an exact target-level regularity reduction aligned with the fleet's Gaussian heat-mode machinery: proving the raw universal density theorem is exactly the same as bounding one fixed smooth functional at unit heat scale over all spectral dilations. It does not assume raw continuity or even prior absolute continuity.

## 5. Partner application: eliminate the random conditional critical value from the majority event

Fix an invertible indefinite original-coordinate triple `S`. Write, after splitting `x=(u,w)`,

`A=[[B,E],[E^T,F]]`, `B=A_SS`.

Completing the square in the original coordinates gives

`Q=(u+B^{-1}Ew)^T B(u+B^{-1}Ew)+c_S(w)`.                             (5.1)

Let `g=grad Q=2Ax`. Then

`g_S=2B(u+B^{-1}Ew)`,                                                (5.2)

so exactly

`boxed(Q-c_S(w)=(1/4) g_S^T B^{-1}g_S)`                             (5.3)

and, because `B^{-1}=adj(B)/det B`, the majority/one-sheet event is

`boxed(G_S={g_S^T adj(B) g_S <=0}. )`                                (5.4)

Indeed, the majority sign is `sigma_S=-sgn det B`; multiplying `sigma_S(Q-c_S)` by the positive factor `4|det B|` turns it into `-g_S^T adj(B)g_S`. Thus the partner's random conditional critical value disappears from the event test. This uses only original-coordinate conditioning; no post-rotation independence is asserted.

## 6. New fractional majority-cone cover lemma

For a finite family `T` of invertible indefinite original-coordinate triples, define

`q_S(g)=g_S^T adj(A_SS)g_S`,
`G_S={q_S(grad Q)<=0}`.                                               (6.1)

Let `a_S>=0` be deterministic weights. Suppose the matrix-only fractional cover condition holds:

`boxed(sum_(S in T) a_S 1_{q_S(g)<=0} >=1  for every g in range(A).)` (6.2)

Because every realized `grad Q(X)=2AX` lies in `range(A)`, (6.2) holds pathwise on the source space.

### Theorem 6.1 — direct raw measure domination

Under (6.2), for **every** admissible rough cap-one product source,

`boxed(mu_Q(E) <= [sum_(S in T) a_S C_S] |E|)`                       (6.3)

for every Borel `E`. Therefore

`boxed(||p_Q||_infinity <= sum_(S in T) a_S C_S.)`                   (6.4)

**Proof.** Apply the completed account02/B15 submeasure theorem (1.1):

`P(Q in E)`
` <= E[1_{Q in E} sum_S a_S 1_{G_S}]`
` =  sum_S a_S P(Q in E,G_S)`
` <= |E| sum_S a_S C_S`.                                             (6.5)

Nothing else is used. `square`

This is a genuine application of the completed partner theorem to the raw target inequality, not merely a citation. It pays the output law before any projection-only or rotated-independence shortcut can occur.

The scale is correct: under `A -> rA`, each `C_S -> C_S/r` while `s_3(A)->r s_3(A)`. Hence a purely matrix-theoretic estimate

`inf_(fractional covers a) sum_S a_S C_S <= K/s_3(A)`                (6.6)

would immediately prove the owner conjecture with universal constant `K` on that structural class.

### Theorem 6.2 — partial cover / heat-posterior version

For arbitrary nonnegative weights put

`R_a(g)=sum_S a_S 1_{q_S(g)<=0}`.                                    (6.7)

At any Gaussian scale `eps` and any center `y` with heat height

`H_eps(y)=E gamma_eps(Q-y)>0`,

let

`dnu_(eps,y)/dP=gamma_eps(Q-y)/H_eps(y)`.                            (6.8)

Then the partner submeasure domination gives the exact inequality

`boxed(H_eps(y) E_nu R_a(grad Q) <= sum_S a_S C_S.)`                 (6.9)

Indeed each summand equals `(mu_S^+*gamma_eps)(y)<=C_S`.

Consequently, if `R_a>=delta` pathwise on a branch, then

`H_eps(y)<= [sum a_S C_S]/delta`                                    (6.10)

at every center and scale. Conversely, any large heat height forces the heat posterior to concentrate on gradients with very small cost-weighted majority coverage.

This is the precise regularity/structure interface: Theorem 4.1 says a failure of the full raw density bound produces a sequence of fixed-unit smooth heat profiles with `s(A)H_1(y)->infinity`; (6.9) then forces every cost-efficient original-coordinate indefinite-triple bank to see asymptotically only its simultaneous minority region under the corresponding heat posterior.

## 7. The remaining obstruction is explicit, and the lemma alone does not solve it

Define the simultaneous minority core for a bank `T` by

`M_T(A)={g in range(A): q_S(g)>0 for every S in T}`.                 (7.1)

Outside this cone, at least one partner majority event is active. With unweighted coefficients,

`P(Q in E, grad Q notin M_T(A)) <= [sum_(S in T) C_S]|E|`.           (7.2)

Thus any unbounded contribution left after a cost-efficient bank must live on the original-coordinate product source restricted to the simultaneous minority core.

This is not vacuous and also shows why the current lemma is not a full proof by itself. For the diagonal signature `(1,1,-1)` exact-rank-three form, the negative eigen-direction is on the minority side of the sole physical triple, so a one-sheet majority cover cannot cover all of `range(A)`. The known rank-two/opposite-sheet smoothing mechanisms are genuinely still needed. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction prevents replacing that remaining product-sensitive minority term by a generic projection cap.

Therefore the first unpaid implication after this run is:

**either** construct, in every surviving nonpaid matrix class, a fractional bank of original-coordinate partner submeasures (possibly combining the majority triples with another completed minority/ridge/grouped-coordinate certificate) whose total scale-homogeneous cost is `O(1/s_3(A))`,

**or** prove that the simultaneous minority core forced by failure of such a cover lies in one of the already-paid product-preserving branches.

## 8. Continuity ledger

The new bounded-density compiler proves only measure domination and essential boundedness. It intentionally does **not** claim raw continuity.

If a separate argument proves that the same fixed instance has a continuous density `p`, then (6.3) immediately upgrades to the pointwise bound `p(t)<=sum a_S C_S` for every `t`, with no constant loss: otherwise continuity would create a positive-measure set above the essential bound.

Equivalently, by Theorem 3.2, the separate continuity task is exactly the uniform-desmoothing statement

`||mu_Q*gamma_eps-p_Q||_infinity ->0`,                               (8.1)

whereas the central owner target requires only the much weaker uniform height bound of Theorem 3.1. No target-uniform desmoothing rate, pointwise quadratic Fourier decay, rotated independence, or projection-only shortcut is assumed anywhere above.

## 9. Classification

- Absolute continuity under the target hypotheses: **PROVED**, in fact for every nonzero `A` and every absolutely continuous joint input law.
- Exact target-level bounded-density regularity lemma: **PROVED**, equations (3.2)-(4.3).
- Completed partner result applied to an actual raw inequality: **PROVED**, equations (6.3)-(6.9).
- Continuous-density conclusion for the unrestricted owner target: **OPEN / separate**.
- Full universal QFORM density constant: **OPEN / NOT PROVED / NOT DISPROVED**.
