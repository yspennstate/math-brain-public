TASK: B15 ACCOUNT: account02 RUN: 2026-09-21T17:03:01.165703Z — FEI spectral remainder: valuation-tail majorization and an all-interpolants negative-credit obstruction

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**

**Execution context: WITHOUT_VERIFIED_BRAIN.** No genuine retrieved brain context was used in this mathematics.

**Model self-report:** GPT-5.6 Sol. **Reasoning effort requested:** maximum actually supported. **Configured/known reasoning effort:** UNKNOWN / not exposed. **Provider reasoning usage:** null / not exposed.

## 0. Fresh control, scientific frontier, and what moved

Authenticated fleet control was resolved at `yspennstate/math-research-brain` main commit
`c659fee54abcc190088286311cc97cf6854c0cfb`, OWNER CONTROL revision `2026-09-21.1`.
The full natural-language OWNER MESSAGE was read. B15 remains assigned to **FEI spectral remainder proof** under directive
`BRAIN-BENCHMARK-FEI-2026-09-21-01`; no account02/B15 pause or stop was present. The protected README Git blob was
`14c6dfefb9a567d99dea06c7cd48dbb38e7a56c9`.

The fresh `yspennstate/math-open-problems` scientific master on entry was
`4d927de8da1be5a61aa9dec10d418660e4686e87`; it advanced during this run and was refreshed before delivery.
I read the current repository rules and P03 entry, then the complete current spectral-lattice and centroid/carry handoffs and proofs,
the concave-restriction handoff, the current owner correction to the unrestricted numerical target, the preceding account02/B15
packet/product bridge, the account04/B15 bridge-collapse obstruction, and the account02/B18 KL-projection integration. The inherited
facts retained here are:

- for packet magnitudes `a`, masses `p_a`, valuations `r_a`, normalized physical meshes `b_a`,
  `H=2 R+2 D`, `R=sum_a p_a r_a`, `D=sum_a p_a log_2(1/b_a)`, and `R<=2 Ifrak<=2I`;
- `D` is not known to be universally influence-paid; raw normalizers and unconditional tensor subadditivity are dead routes;
- lattice-valued **physical** projections are an extra hypothesis, and the five-variable counterexample to automatic projection
  integrality is preserved;
- the fresh packet/product bridge keeps essential negative KL credits, but its fully recombined residual is `H-R`, so another global
  renaming or a potential-free one-coordinate payment is not progress;
- the owner correction supersedes the old unrestricted `6.4547837` target: the current public certified lower bound is already
  `>6.521845710923046575` from an 18-variable monotone seed. Full FEI has no known finite universal upper bound.

**Creative moves used this run:** FLEET_RULES **#3 prove something stronger** (replace the scalar `R<=2J` by an all-cost, all-tail
majorization theorem), **#5 add a parameter and differentiate** (interpolate continuously between the arithmetic and product-shadow
KL representations), and **#30 one scale/direction at a time** (extract every valuation-depth tail rather than only its first moment).
These are different from the preceding B15 run's midpoint bridge derivation.

**Tracked quantity.** Before this run, the universal valuation control retained only the first moment
`E_p r_a=R<=2J`, where `J=sum_i min(Inf_i,1-Inf_i)`. After this run there is a simultaneous family of `n` exact tail controls

`E_p (r_a-m+1)_+ <= 2 sum_{k=m}^n q_k^down`, `1<=m<=n`,

and, more strongly, an arbitrary nonnegative-cost inequality. This is a genuine strengthening of the arithmetic/geometric input,
not a structured-class FEI consequence. A second theorem shows that **every** convex arithmetic/product escort interpolation still
requires its negative information credits: even choosing the interpolation parameter adaptively cannot produce a credit-free FEI
bound on the one-point-defect family.

Coordination is nonoverlapping with the current neighboring account02 scopes: B14 is on existential restriction, B16 on signed/shared-variable
transport, B17 on a distinct support/face route, and B18 on restriction/KL-integration. This report stays on the packet valuation and
arithmetic-remainder interface.

---

## 1. Notation and inherited packet polynomial fact

Let `f:{0,1}^n->{-1,+1}` and let the spectral sample `S` have law

`mu(S)=fhat(S)^2`.

For each distinct nonzero Fourier magnitude `a`, let

`A_a={S: |fhat(S)|=a}`, `p_a=mu(A_a)=|A_a|a^2`.

Conditional on packet label `a`, `S` is uniform on `A_a`.

Let `epsilon_a` be the signed indicator of `A_a`, let

`V_a(x)=sum_S epsilon_a(S) chi_S(x)`,

and define the inherited physical Walsh valuation

`r_a=min_{V_a(x) != 0} nu_2(V_a(x))`.

The spectral-lattice proof shows that the binary indicator polynomial

`P_a=1_{A_a}`

has ordinary algebraic degree at most

`deg_F2(P_a) <= n-r_a`.                                               (1.1)

This is where the packet **signs** enter: `r_a` is computed from the signed mask before (1.1) is invoked. No automatic projection
integrality is assumed.

For a nonnegative coordinate-cost vector `c=(c_1,...,c_n)`, write

`T_c=sum_i c_i`,

and let `c_(1)<=...<=c_(n)` be the sorted costs. Define

`sigma_r(c)=sum_{k=1}^r c_(k)`, with `sigma_0(c)=0`.                   (1.2)

For a frequency center `b in {0,1}^n`, put

`j_i^(b)=Pr_mu[S_i != b_i]`.

The coordinatewise best center gives the folded spectral marginals

`q_i=min(Inf_i(f),1-Inf_i(f))`,                                      (1.3)

and `J=sum_i q_i<=I(f)`.

---

## 2. PROVED: all-cost valuation majorization

### Theorem B15-VALUATION-MAJOR-01

For every Boolean `f`, every nonnegative cost vector `c`, and every center `b`,

`boxed{ E_{a~p} sigma_{r_a}(c) <= 2 sum_i c_i j_i^(b). }`            (2.1)

Consequently, after taking the coordinatewise best center,

`boxed{ E_{a~p} sigma_{r_a}(c) <= 2 sum_i c_i q_i. }`                (2.2)

No FEI inequality is used.

### Proof

Fix a packet `a`. The weighted centroid theorem from the complete centroid-and-carries continuation applies to the support of the
binary polynomial `P_a`. For every center `b`, if `D_c(P_a)` is its weighted monomial degree, it gives

`E_{S uniform A_a} sum_i c_i 1_{S_i != b_i}`

`    >= (T_c-D_c(P_a))/2`.                                           (2.3)

By (1.1), every monomial of `P_a` contains at most `n-r_a` coordinates. Therefore its weighted cost is at most the sum of the
`n-r_a` largest entries of `c`. Hence

`T_c-D_c(P_a) >= sum_{k=1}^{r_a} c_(k)=sigma_{r_a}(c)`.              (2.4)

Insert (2.4) into (2.3), multiply by the packet mass `p_a`, and sum over packets. Conditional packet uniformity turns the left side into

`sum_i c_i Pr_mu[S_i != b_i]=sum_i c_i j_i^(b)`.                     (2.5)

This proves (2.1). Since (2.1) holds for every `b`, choose each `b_i` to minimize `Pr[S_i != b_i]`; the minimum is exactly `q_i`.
This proves (2.2). QED.

### Why this is stronger than the inherited reserve bound

Taking `c_i=1` gives `sigma_r(c)=r`, so (2.2) recovers

`R=sum_a p_a r_a <=2J`.                                              (2.6)

But (2.2) is not only a reproof of (2.6): arbitrary weights expose every depth tail separately.

---

## 3. PROVED: valuation-depth tails are paid by the least-active coordinates

Sort the folded marginals in decreasing order:

`q_1^down >= q_2^down >= ... >= q_n^down`.

### Corollary B15-VALUATION-TAIL-02

For every `1<=m<=n`,

`boxed{ E_p (r_a-m+1)_+ <= 2 sum_{k=m}^n q_k^down. }`                (3.1)

In particular,

`boxed{ Pr_p[r_a>=m] <= 2 sum_{k=m}^n q_k^down. }`                   (3.2)

At `m=1`, (3.1) is the old first-moment payment `R<=2J`. At `m=n`, it gives

`Pr_p[r_a=n] <= 2 min_i q_i`.                                        (3.3)

### Proof

Let `T` be the `n-m+1` coordinates with the **smallest** folded marginals, and take `c_i=1` on `T`, `c_i=0` otherwise. There are
`m-1` zero costs, so the sum of the `r` smallest costs is exactly

`sigma_r(c)=(r-m+1)_+`.                                               (3.4)

Equation (2.2) becomes (3.1). Since `(r-m+1)_+ >= 1_{r>=m}`, (3.2) follows. QED.

### Log-odds form

On active folded coordinates `0<q_i<=1/2`, define

`lambda_i=log_2((1-q_i)/q_i)>=0`.

Order the `q_i` decreasingly, so the corresponding `lambda_i` are increasing. Taking `c_i=lambda_i` in (2.2) gives

`boxed{
 sum_a p_a sum_{k=1}^{r_a} lambda_k^up
 <= 2 sum_i q_i log_2((1-q_i)/q_i).
}`                                                                       (3.5)

Zero-marginal coordinates are handled by truncating `lambda_i` and passing to the monotone limit; equivalently remove coordinates on
which the spectral sample is deterministic. Thus deep packet valuations are not an unstructured source of logarithmic loss: their whole
mass profile is majorized by the tail of the **folded influence profile**.

This does **not** pay the normalized mesh depth `X_a=log_2(1/b_a)`. The one-point defect already has `r_a=0` on both packets while one
packet has `X_a=n-1`. Therefore (3.1)-(3.5) isolate the remaining difficulty more sharply: uncontrolled depth can only hide in the
physical mesh `b_a` / packet information credits, not in an unpaid valuation tail.

---

## 4. PROVED: a continuum of exact arithmetic/product-shadow bridges

The preceding B15 run used the geometric midpoint between two exact representations of `2D`. The midpoint is not special.

Let

`N_a=p_a/b_a^2`, `N=sum_a N_a`, `q_a^N=N_a/N`,

and let `nu` be the independent Bernoulli law with the same spectral coordinate marginals. Put

`beta_a=nu(A_a)`,

`C_in=sum_a p_a D_KL,2(Unif(A_a)||nu(.|A_a))`,                       (4.1)

and `S_marg=sum_i h_2(Inf_i(f))`.

The two inherited exact identities are

`2D=log_2 N-D_KL,2(p||q^N)`,                                        (4.2)

`2D=S_marg-2R-D_KL,2(p||beta)-C_in`.                                (4.3)

Here `D_KL(p||beta)=sum_a p_a log_2(p_a/beta_a)` uses the sub-probability packet masses of `nu`; mass outside the Fourier support is
allowed.

For `0<=theta<=1`, define

`W_theta=sum_a N_a^theta beta_a^(1-theta)`,                          (4.4)

`m_theta(a)=N_a^theta beta_a^(1-theta)/W_theta`.                     (4.5)

### Theorem B15-ESCORT-BRIDGE-03

For every `theta in [0,1]`, exactly

`boxed{
 2D=(1-theta)(S_marg-2R)+log_2 W_theta
    -D_KL,2(p||m_theta)-(1-theta)C_in,
}`                                                                       (4.6)

and hence

`boxed{
 H=2 theta R+(1-theta)S_marg+log_2 W_theta
   -D_KL,2(p||m_theta)-(1-theta)C_in.
}`                                                                       (4.7)

At `theta=1`, this is the arithmetic free-energy identity. At `theta=0`, it is the product-measure/total-correlation identity. At
`theta=1/2`, it is precisely the geometric packet/product bridge from the preceding B15 run.

### Proof

Take `theta` times (4.2) plus `1-theta` times (4.3). The weighted packet KLs satisfy, by direct expansion,

`theta D(p||q^N)+(1-theta)D(p||beta)`

` =D(p||m_theta)+theta log_2 N-log_2 W_theta`.                        (4.8)

The `theta log N` terms cancel, giving (4.6); add `2R` and use `H=2R+2D` to obtain (4.7). QED.

### Thermodynamic derivative

Write

`L_a=log_2(N_a/beta_a)`.

Then `log_2 W_theta` is a log-sum-exp in `theta`, and wherever endpoints are nondegenerate,

`d/dtheta log_2 W_theta=E_{m_theta} L`,                              (4.9)

`d^2/dtheta^2 log_2 W_theta=(ln 2) Var_{m_theta}(L)>=0`.             (4.10)

Thus the escort partition function is convex, and `D(p||m_theta)` is the corresponding information-projection mismatch. Equations
(4.6)-(4.10) expose a genuine one-parameter choice of where the exact cancellation is stored; they do not themselves prove FEI.

---

## 5. PROVED obstruction: optimizing the escort parameter cannot replace the negative credits

A possible hope after (4.7) is to choose `theta` adaptively so the positive part is influence-small and then discard the two negative
credits. The genuine Boolean one-point defect kills that entire strategy.

Let

`f_n=1-2 1_{x=0}`, `n>=3`,

and put `j=2^{1-n}`. Its two packets satisfy

`A_0={empty}`, `N_0=1`,

`A_1={S:S!=empty}`, `N_1=2^n-1`,

`R=0`.                                                               (5.1)

The spectral coordinate marginals are all `j`, so

`S_marg=n h_2(j)`, `I(f_n)=n j`.                                    (5.2)

Under the product law,

`beta_0=(1-j)^n`, `beta_1=1-beta_0`, and `beta_0+beta_1=1`.          (5.3)

Discard both negative terms from (4.7) and define the credit-free escort bound

`U_theta=(1-theta)n h_2(j)+log_2 W_theta`.                           (5.4)

### Theorem B15-ALL-ESCORTS-FAIL-04

For every `n>=3`,

`boxed{ min_{0<=theta<=1} U_theta = U_0=n h_2(j). }`                 (5.5)

Consequently

`boxed{
 min_theta U_theta / I(f_n)
 =h_2(2^{1-n})/2^{1-n}
 =n-1+1/ln 2+o(1) -> infinity.
}`                                                                       (5.6)

So **even an optimally and function-dependently chosen interpolation parameter cannot yield a dimension-free FEI bound after the
negative packet-information credits are discarded.** The preceding midpoint obstruction was not an artefact of choosing `theta=1/2`.

### Proof

Convexity (4.10) shows that `U_theta` is convex. At `theta=0`, `W_0=beta_0+beta_1=1`. Its right derivative is

`U'_0=-S_marg + beta_0 log_2(N_0/beta_0)
                 + beta_1 log_2(N_1/beta_1)`.                        (5.7)

Define a probability law `tilde nu` that has packet masses `beta_0,beta_1` but is uniform inside each packet: it assigns mass `beta_0`
to the empty set and `beta_1/(2^n-1)` to each nonempty set. The second and third terms of (5.7) are exactly `H(tilde nu)`.

The genuine product law `nu` has the **same packet masses**. Conditional on the nonempty packet its entropy is at most
`log_2(2^n-1)`, with equality only for a uniform conditional law. Therefore

`H(nu)<=H(tilde nu)`.                                                 (5.8)

But `H(nu)=n h_2(j)=S_marg`, so `U'_0>=0`. A convex function with nonnegative right derivative at the left endpoint is minimized there,
proving (5.5). Equation (5.6) follows from the standard small-`j` expansion

`h_2(j)/j=log_2(1/j)+1/ln 2+o(1)`.                                  (5.9)

QED.

This obstruction is at the exact intended scope. The one-point defect itself satisfies FEI with bounded `H/I`; what diverges is the
credit-free interpolated upper expression. Therefore the theorem kills a proof shortcut, not the conjecture.

---

## 6. Finite sanity checks

`verify_tail_majorization.py` uses exact integer Walsh transforms and exact `Fraction` arithmetic. It checks (3.1) and the derived
packet-mass tail bound (3.2) on:

- the six-variable one-point defect;
- five-variable majority;
- the inherited five-variable lattice/integrality counterexample
  `1-2*1{y1=x1*x2,y2=x1*x3}`;
- the six-variable addressing function with two address bits;
- 64 deterministic seeded six-variable Boolean truth tables.

All checks pass. The seeded sample reaches packet valuation `r=3`. The verification file records every named rational tail budget and
the per-case random summary. These finite checks are only implementation sanity checks; Theorems (2.1) and (3.1) are proved above and
do not rely on enumeration.

---

## 7. Literature boundary and priority

A fresh primary-source check on 21 September 2026 still finds unrestricted FEI open in the inspected literature.

- V. N. Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563,
  posted 18 September 2026, proves sharp class constant `4` for plateaued Boolean functions and `2` for partially bent functions.
  This is a structured-class result. Its abstract also contains a closely related support-weight/algebraic-degree inequality and
  p-biased estimates, so **no publication-priority claim** is made for the weighted-centroid consequences used here.
- M. J. González, P. MacManus, M. C. Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*,
  arXiv:2606.00246, 29 May 2026, develops restriction/stopping-tree progress and new classes; its key universal restriction step is not
  proved for all Boolean functions.
- P. Li, G. Han, *Strengthening Han's Fourier Entropy-Influence Inequality via an Information-Theoretic Proof*,
  arXiv:2512.03117, 2 December 2025, gives a sharp information-theoretic inequality retaining an influence-profile entropy term; it does
  not supply the dimension-free payment missing here.

The current public optimization-constants ledger records the certified unrestricted lower bound
`C_FEI>6.521845710923046575` from an explicit 18-variable monotone seed. No finite universal upper bound is listed. The project owner
had already directed the fleet to use this corrected frontier rather than the older read-once `6.4547837` scale.

---

## 8. Before / after, failed routes, and exact remaining obligation

**Before.** The arithmetic route knew only the scalar valuation payment `R<=2J`, plus an exact free-energy/KL formula for `D`. The fresh
midpoint product bridge showed an essential KL cancellation, but account04 proved its fully recombined residual is `H-R` and has no
finite potential-free coordinate selector. It was still possible that deeper `r_a` layers hid an uncontrolled dimension-dependent
reserve, or that another interpolation between the two KL formulas could avoid retaining the negative credits.

**After.** Two things are now ruled in/out exactly:

1. **Valuation depth is completely profile-majorized.** Every integrated depth tail and packet-mass depth tail is paid by the least-active
   folded spectral coordinates via (3.1)-(3.2). The old `R<=2J` is only the first member of this family.
2. **Interpolation does not remove the information problem.** The whole arithmetic/product family (4.7) is exact, and the one-point
   defect proves that after discarding its negative information credits, even the best adaptive `theta` has ratio growing linearly in
   `n`.

Thus the surviving universal difficulty is more precise: it is the **normalized physical mesh / cross-packet information remainder**,
not a missing control on valuation tails and not a poor choice of the midpoint bridge.

A next B15 run on this route should attack the joint law of

`X_a=log_2(1/b_a)` and `r_a`

inside the KL-preserving mesh bands, using (3.1) to remove deep-valuation mass before attempting a neighboring-band carry payment. A
useful concrete target is a bound on the mesh-band free energy after conditioning to `r_a<m`, with the discarded `r_a>=m` contribution
charged using (3.1) **without discarding the packet KL**. The one-point defect is mandatory: it has `r_a=0` and large `X_a`, so any
claim that valuation-tail control alone pays `D` is immediately false. The valuation-misaligned product collision and the five-variable
physical-lattice counterexample remain mandatory stress tests as well.

Full FEI therefore remains **OPEN**.
