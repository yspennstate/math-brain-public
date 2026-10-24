SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T08:12:23Z.
attacking: cap-preserving localization rigidity — quantify exactly how much spatial information an active localization label can reveal before normalized density caps must increase, and combine this with the completed account02/B14 cap-weighted compiler.

# account01/B14 — cap-preserving localization rigidity and zero-tax remote mixtures

Run: `20260924T081223Z-account01-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed: revision `2026-09-22.15`; programme activation revision `2026-09-22.5`.  
Status: **NEW LOCALIZATION-RIGIDITY / INFORMATION-CAP THEOREM + TARGET-VALID ZERO-TAX REMOTE-MIXTURE APPLICATION / FULL QFORM OPEN / CONTINUITY SEPARATE.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 0. Source discipline and mechanism change

Fresh brain control, the QFORM manifest/current-research/claims/corrections/memory protocol, and the account01/B14 assignment were read before this calculation. The live restrictions remain binding: no law-uniform pointwise quadratic Fourier decay, no independence after rotation, no arbitrary-joint coarea cap, no bounded-diameter or fixed-fragment-count reduction, and no unsupported good-minor extraction.

The initially proposed filler compactification mechanism was abandoned before being counted as progress. A source search found that exact truncation/filler compactification and smooth compact zero-loss closure had already been proved in the fleet, including this slot's earlier `QFORM-WHOLE-LAW-SMOOTH-LOCALIZATION-v1`. The present run therefore changes mechanism to **information carried by localization labels**.

The completed designated-partner result actually used below is account02/B14:

- canonical math commit `a785db1a405eec1874fc553b28b8178f32d416d0`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260924T065901Z-account02-B14-QFORM-auto11/REPORT.md`;
- theorem `QFORM-CAP-WEIGHTED-ACTIVE-MIXTURE-COMPILER-v1`.

In the notation needed here: for three independent active variables with positive marginal pieces `rho_{rj}`, masses `m_{rj}`, normalized caps `k_{rj}=||rho_{rj}||_infinity/m_{rj}`, and fixed invertible symmetric `3x3` active Hessian `B`, the partner proves

`||p_Q||_infinity <= 6 sqrt(pi) sum_alpha m_alpha / sigma_alpha`,                 (0.1)

where `sigma_alpha=min |eig(K_alpha^{-1} B K_alpha^{-1})|`. If every piece satisfies

`||rho_{rj}||_infinity <= M_r m_{rj}`,                                            (0.2)

then with `M=diag(M_1,M_2,M_3)` and

`sigma_0=min |eig(M^{-1} B M^{-1})|`,                                             (0.3)

the countable localization is zero-tax:

`||p_Q||_infinity <= 6 sqrt(pi)/sigma_0`,                                         (0.4)

uniformly in arbitrary conditioning-generated affine terms. The theorem already allows arbitrary fragment locations and no support or moment assumptions.

The new question addressed here is: **what does condition (0.2) actually permit a localization label to learn about an active cap-one variable?**

---

## 1. Localization labels and normalized cap budget

Let `X` have density `f`. A finite or countable randomized localization label `J` is equivalently a positive decomposition

`f(x)=sum_j rho_j(x)`,                                                            (1.1)

where

`m_j=int rho_j(x) dx=P(J=j)>0`,                                                   (1.2)

and the conditional density is

`g_j(x)=rho_j(x)/m_j=p_{X|J=j}(x)`.                                               (1.3)

The partner's mass-proportional cap condition is exactly

`||g_j||_infinity <= M_j`.                                                        (1.4)

Thus the cap paid after localization is the essential supremum of the conditional density, not the cap of the unconditioned law.

When the original cap-one density is saturated,

`f=1_E`, `|E|=1`,                                                                (1.5)

this condition has a strong rigidity consequence.

### Theorem 1.1 — `QFORM-ZERO-TAX-ACTIVE-LOCALIZATION-RIGIDITY-v1`

Assume (1.5) and let `J` be any finite/countable randomized localization label. For each positive-mass label let `g_j` be as in (1.3) and suppose

`||g_j||_infinity <= M_j < infinity`.                                             (1.6)

Then:

1. `g_j=0` a.e. outside `E`.
2. The mutual information obeys the exact cap-budget inequality

   `boxed: I(X;J) <= sum_j m_j log M_j.`                                          (1.7)

   In particular, if all `M_j<=M`, then

   `boxed: I(X;J) <= log M.`                                                      (1.8)

3. Every conditional law satisfies the sharp total-variation rigidity bound

   `boxed: d_TV(Law(X|J=j),Law(X)) <= 1-1/M_j.`                                  (1.9)

4. If `M_j=1` for every label, then

   `boxed: g_j=1_E a.e. for every j, hence J is independent of X.`               (1.10)

5. If `J=T(X)` is deterministic, then `I(X;J)=H(J)`, so

   `boxed: H(m) <= sum_j m_j log M_j`,                                            (1.11)

   and under a uniform cap budget `M_j<=M`,

   `boxed: M >= exp(H(m)).`                                                       (1.12)

For `N` equiprobable deterministic fragments this forces `M>=N`.

#### Proof

Because the decomposition is positive and `sum_j m_j g_j=1_E`, every `g_j` vanishes outside `E`.

On `E`, the posterior label probability is

`P(J=j|X=x)=m_j g_j(x)`.                                                          (1.13)

Hence its likelihood ratio relative to the prior label mass is

`P(J=j|X=x)/P(J=j)=g_j(x) <= M_j`.                                                (1.14)

Using the standard discrete-label formula for mutual information,

`I(X;J)=int_E sum_j m_j g_j(x) log g_j(x) dx`.                                   (1.15)

Since `log g_j(x)<=log M_j` wherever `g_j>0`,

`I(X;J)
 <= int_E sum_j m_j g_j(x) log M_j dx
 = sum_j m_j log M_j`,                                                           (1.16)

proving (1.7). Equation (1.8) is immediate.

For total variation, since both laws are supported on `E`,

`d_TV(g_j dx,1_E dx)=1-int_E min(g_j,1) dx`.                                     (1.17)

For `0<=g_j<=M_j`,

`min(g_j,1) >= g_j/M_j`.                                                         (1.18)

Integrating and using `int g_j=1` gives (1.9). The bound is sharp: take `g_j=M_j 1_S` with `|S|=1/M_j`.

If `M_j=1`, then `g_j<=1` on the unit-measure set `E` and `int_E g_j=1`, so `g_j=1_E` a.e.; this proves (1.10). If the label is deterministic, `H(J|X)=0`, so `I(X;J)=H(J)`, yielding (1.11)-(1.12). QED.

### Corollary 1.2 — exact support-resolution cost

Under the hypotheses above, if a conditional component `g_j` is supported in a measurable subset of `E` of Lebesgue measure at most `delta_j`, then

`boxed: M_j >= 1/delta_j.`                                                        (1.19)

Indeed `1=int g_j<=M_j delta_j`.

Thus a spatial localization to a tiny active tooth necessarily raises the normalized cap by the reciprocal tooth measure. For a saturated cap-one law there is no nontrivial **exact zero-tax spatial localization**: the only `M=1` decomposition is independent thinning of the entire original law.

---

## 2. What this means for arbitrary distant fragments

The theorem cleanly separates two kinds of remote-fragment structure.

### Diluted remote mixtures are genuinely zero-tax

Suppose

`f(x)=sum_j m_j h_j(x-a_j)`,                                                      (2.1)

where `sum_j m_j=1`, each `h_j` is a probability density with `0<=h_j<=1`, and the shifts `a_j` are arbitrary. No moment or bound on the shifts is assumed. The unnormalised component is

`rho_j(x)=m_j h_j(x-a_j)`,                                                        (2.2)

so

`||rho_j||_infinity <= m_j`.                                                      (2.3)

Therefore the partner's exact zero-tax condition holds with `M=1`, regardless of the number, separation, or support of the translated components. Conditioning on the latent component labels does not change the active density constant.

This permits countably many fragments at arbitrarily large distances and even infinite moments. For example, take

`m_j=6/(pi^2 j^2)`, `a_j=j^3`, `h_j=1_[0,1]`.                                   (2.4)

Then `f<=1`, the support is unbounded and the first absolute moment diverges, but every conditional component remains cap one.

### Saturated remote teeth are the opposite endpoint

Let `E` be any measurable set of measure one, possibly a countable union of arbitrarily remote narrow intervals, and let `f=1_E`. If a label tries to identify individual spatial teeth, Theorem 1.1 says the conditional cap must rise. For an equal `N`-tooth deterministic partition, each conditional density has cap exactly `N`, and

`I(X;J)=H(J)=log N=log M`.                                                        (2.5)

Thus the cap/entropy payment is exact. For countably many teeth whose masses tend to zero, no finite uniform normalized-cap budget can resolve all teeth deterministically.

This is not a counterexample to QFORM. It is a proof-interface theorem: **remote saturated fragments must be aggregated before a reciprocal-curvature certificate is paid.**

---

## 3. Completed account02/B14 theorem applied to an actual strict-target inequality

Take the dense indefinite active matrix

`B_* = 2 I_3 - 1 1^T
     = [[1,-1,-1],[-1,1,-1],[-1,-1,1]].`                                         (3.1)

Its spectrum is exactly

`spec(B_*)={2,2,-1}`,                                                             (3.2)

so

`min |eig(B_*)|=1`.                                                              (3.3)

Let the three active variables `Y_1,Y_2,Y_3` be independent. For each `r`, permit an arbitrary countable remote-mixture representation

`p_{Y_r}(y)=sum_j m_{rj} h_{rj}(y-a_{rj})`,                                      (3.4)

with `h_{rj}<=1`, no restriction on the shifts, support radii, moments, or component count. Let `W` be any independent environment and allow arbitrary measurable affine data `ell(W),c(W)`. Consider

`Q=Y^T B_* Y + ell(W)^T Y + c(W)`.                                                (3.5)

For every active piece in (3.4),

`||rho_{rj}||_infinity <= m_{rj}`,                                                (3.6)

so the completed account02/B14 Corollary 3.2 applies with

`M=I_3`, `sigma_0=min |eig(B_*)|=1`.                                              (3.7)

Therefore the actual inequality is

`boxed: ||p_Q||_infinity <= 6 sqrt(pi)
      = 10.634723105433096... .`                                                  (3.8)

This is an equation-level use of the designated partner result: the remote component labels are paid through its mass-proportional cap hypothesis, and the constant is exactly the same as for an unsplit cap-one active law.

### Ambient localization corollary

Embed `B_*` as an original-coordinate principal block of an arbitrary larger symmetric matrix,

`A=[[B_*,C],[C^T,D]]`.                                                           (3.9)

Let all original coordinates remain independent and cap one. Conditioning on the outside original coordinates `Z=z` gives

`Q|Z=z=Y^T B_*Y + 2(Cz)^T Y + z^T D z`.                                         (3.10)

This is exactly (3.5), so (3.8) holds pointwise in `z` and survives averaging:

`boxed: ||p_{X^TAX}||_infinity <= 6 sqrt(pi).`                                   (3.11)

By Cauchy interlacing, because the principal block has two eigenvalues `2` and one eigenvalue `-1`, the ambient matrix has at least three eigenvalues of modulus at least one. Hence (3.11) is a genuine branch of the owner's full arbitrary-sign target, with arbitrary outside curvature and couplings.

Using the concrete no-moment mixture (2.4) independently in all three active coordinates gives a fully explicit strict-target family with unbounded, arbitrarily distant supports and divergent first moments, yet the same constant `6 sqrt(pi)`.

---

## 4. The entropy barrier exactly matches the partner's equal-cell `N^2` tax

Take the saturated marginal `f=1_[0,1]` and split it deterministically into `N` equal intervals. Every label has mass `1/N`, conditional support measure `1/N`, and normalized cap

`M=N`.                                                                            (4.1)

Theorem 1.1 gives the exact information identity

`I(X;J)=log N=log M`.                                                             (4.2)

If all three active coordinates are localized this way and the partner compiler is applied with the common cap budget `M=N`, then for the matrix `B_*`,

`M^{-1} B_* M^{-1}=N^{-2}B_*`,                                                    (4.3)

so

`sigma_0=N^{-2}`                                                                 (4.4)

and the partner certificate becomes

`6 sqrt(pi) N^2`.                                                                (4.5)

Thus the previously observed `N^2` fragment-first tax is not merely an arbitrary normalization choice: within the cap-saturation compiler it is forced by the amount of deterministic spatial information carried by the labels. The **actual whole-law density remains bounded by `6sqrt(pi)`**; (4.5) is a localization-certificate loss, not a density lower bound and not a QFORM counterexample.

The correct proof order is therefore sharper than “avoid normalization”:

`aggregate saturated active law -> expose a valid three-curvature/bank certificate -> pay reciprocal curvature -> only then localize an independent environment.`

A localization label may be inserted earlier at zero tax only when its conditional active laws retain cap one; for an extreme saturated cap-one marginal, Theorem 1.1 says such a label contains zero information about the active coordinate.

---

## 5. Remaining implication

The full unrestricted QFORM theorem is still **OPEN**. This run removes ambiguity about what a constant-preserving active localization can do, but it does not produce the missing product-preserving three-curvature representation from bare `s_3(A)>=1`.

The next structural/analytic bridge is:

`QFORM-AGGREGATE-EXTREME-ACTIVE-LAW-BEFORE-STRUCTURAL-ROUTING-v1`:

> In the remaining no-good-physical-triple / concentrated-hub configurations, obtain a whole-active ridge, overlap, hub, grouped-bank, projected-crossing, or other proved receiver **before** any spatial label reveals significant information about a saturated cap-one active marginal.

Theorem 1.1 shows why ordinary tooth-by-tooth localization cannot be the missing step: at the extreme laws of the cap-one class, exact zero-tax localization is necessarily statistically independent of the active variable.

No claim of full QFORM or of continuous density is made.
