# Six open problems attacked, 2026-09-08 (afternoon session)

The morning session verified and settled candidates the campaign had already recorded. This one
attacked open problems directly. One is closed, four are reduced to explicit remaining statements,
and one gains a reformulation plus a structural fact. Every claim below was computed or derived
here; where I lean on someone else's step, it says so.

---

## 1. Ross's second conjecture — the counterexample is now COMPLETE

*Leskelä, Queueing Systems 100 (2022) 213–215, Problem 1.* Does faster modulation always lower the
mean stationary workload of a Cox queue?

Yesterday the campaign's construction had a verified mechanism and an unchecked quantitative half.
That half is now closed.

The environment is a cyclic CTMC on Z/1024 with **only clockwise** jumps — the point being that a
one-directional walk has complex character eigenvalues r(e^{iθ}−1), so its autocorrelation
oscillates instead of decaying monotonically. Deriving it:

  E[F(0)F(−s)] = 4 + ½·e^{−δs}cos(s),  δ = tan(π/m) = 0.00306797,

using r·sinθ = 1 for the frequency and r(1−cosθ) = tan(θ/2) for the damping. A reversible
environment could not do this. Substituting into the workload expansion,

  w(c) = ε + 2ε² + (ε²/2)·J(c) + R_c,  J(c) = ∫₀¹(1−u)e^{−δcu}cos(cu)du,  0 ≤ R_c ≤ 27ε³/(2(1−3ε)).

**J is non-monotone** — dJ/dc changes sign 11 times on [0.01, 40] — and its largest upward
excursion is J(6.2940) = 0.000970 → J(8.9785) = 0.023600, a rise of ΔJ = +0.02263 as c *increases*.
The rise survives the remainder whenever |ΔJ| > 27ε/(1−3ε), i.e. for every ε ≤ 10⁻⁴. At ε = 10⁻⁵
(so ρ = εM = 3×10⁻⁵, well inside the stability regime),

  **w(c₂) − w(c₁) ≥ 1.118×10⁻¹² > 0 with c₁ = 6.294 < c₂ = 8.979.**

Faster modulation strictly increases the mean workload. The universal monotonicity clause is false.

*What I lean on*: the workload expansion and the uniformity of its ε³ remainder come from the
campaign's written proof packet; I re-derived the autocorrelation and everything after it. The
rigour rests on that uniformity, so anyone promoting this should re-derive the expansion.

*My own error, recorded*: my first attempt picked the excursion at c ≈ 38, where damping has
flattened J to a rise of 0.0009, and concluded "not enough" at every ε. That was a bad choice of
excursion, not a property of the construction — the condition is linear in ε, so any fixed positive
rise suffices once ε is small enough. Take the largest excursion, not the first one you find.

---

## 2. Lyons's entropy-concavity Conjecture 2.6 — the 2×2 case reduced to one inequality

*Is Ent(P_Q) concave in the kernel Q?* Stated for all finite E; the 2×2 case was the first target.

For Q = [[a,c],[c,b]] the atom probabilities are p₀₀ = (1−a)(1−b) − t, p₁₀ = a(1−b) + t,
p₀₁ = (1−a)b + t, p₁₁ = ab − t with t = c² — the product measure Bern(a)⊗Bern(b) displaced by t
along (−1,+1,+1,−1). Three exact facts fall out:

- **p₁₀p₀₁ − p₀₀p₁₁ = c² identically.** The product cross-terms cancel and the surviving bracket is
  the sum of the four product probabilities, hence 1. Negative association in one line, and the log
  odds ratio L ≤ 0 with equality iff c = 0.
- **In coordinates (a, b, p₁₁) the probability vector is affine** — p₀₀ = 1−a−b+p₁₁, p₁₀ = a−p₁₁,
  p₀₁ = b−p₁₁ — so entropy is concave there for free, and ∂H/∂p₁₁ = |L| ≥ 0.
- Writing H(a,b,c) = φ(a, b, ab−c²) with φ concave, the only nonlinearity is ψ₃ = ab−c², whose
  Hessian is M = [[0,1,0],[1,0,0],[0,0,−2]]. The chain rule gives **Hess H = −(G + L·M)** exactly
  (verified symbolically: residual is the zero matrix), so the conjecture *is* the statement that
  N := G − |L|M is positive semidefinite.

N is PSD at every one of 360,000 admissible kernels. Its 1×1 and 2×2 minors are bounded below by 4
and 16, and the binding direction q = (1,1,a+b) reduces to a scalar inequality with minimum exactly
8 — all wide margins. Only **det N** is tight, vanishing as c → 0. Taking the Schur complement
against the 2×2 block removes that degeneracy entirely (every term carries c², which divides out):

  **4S + 2|L|/c² ≥ (g₁,g₂)K⁻¹(g₁,g₂)ᵀ,  S = Σ1/pᵢ,  gⱼ = G_{j3}/c.**

At c = 0 this is exact and pretty: S = 1/(ab(1−a)(1−b)) equals 1/(p₀₀p₁₁), the left side is 6S, and
g₁ = g₂ = 0 identically. Over 300,000 points the minimum of LHS − RHS is 96.0043 — exactly 6S at
the uniform kernel a = b = ½, which is therefore the extremal configuration.

**Two proof routes closed, from both sides — and a strategy that survives.** Bounding log(1+z) ≤ z
is far too lossy (23,000 failures). Dropping the |L| term as slack also fails, but only barely:
under strict admissibility and full precision, RHS > 4S at 13 of 300,000 points, every one with
RHS/(4S) between 1.000007 and 1.000120 and every one in a thin boundary layer with
min pᵢ between 2.8×10⁻⁶ and 4.3×10⁻⁵. (det K > 0 throughout, minimum 16.0009, so the multiplied and
unmultiplied forms are equivalent — an earlier apparent discrepancy between two samplings was my
own artifact of printing rounded coordinates and re-evaluating there.)

That failure pattern is itself the proof strategy. As any pᵢ → 0 the log term
|L| = log(p₁₀p₀₁/p₀₀p₁₁) **diverges**, so 2|L|/c² blows up precisely in the boundary layer where
RHS creeps above 4S by one part in ten thousand. So: prove RHS ≤ 4S in the interior, and let the
logarithm carry the boundary layer. The logarithm is load-bearing, but only there.

*Correction to my own first reading of the scan*: I initially wrote that the right side never
approaches the left. In relative terms that is false — RHS/LHS reaches 0.999972. It happens only
where min pᵢ → 0, where both sides diverge while the absolute margin grows. It is the absolute
margin that is bounded below, so a proof must be phrased in absolute terms.

**A clean reparametrisation.** Writing the four probabilities as w, x, y, z on the simplex and
setting r = xy/(wz) ≥ 1 (so |L| = log r), m = y/z, k = x/z, the ratios satisfy w/x = m/r and
w/y = k/r, which collapses the gradients to exact closed forms — verified to 8.5×10⁻¹⁴:

  **g₁ = 2(r−1)(r−m²)/(mr),  g₂ = 2(r−1)(r−k²)/(kr).**

Both vanish exactly at r = 1, i.e. c = 0. So the whole problem is three parameters (r, m, k) with
r ≥ 1, and the minimum margin 96 sits at r = m = k = 1. This also explains the shape of the
difficulty: RHS ∝ (r−1)² while log(r)/(r−1) → 1, so small r is automatic and large r is carried by
the diverging logarithm — leaving only the boundary layer, which is the region identified above.

---

## 3. Aldous–Janson's Ansatz 20 — the failure is exactly one term

*Inside their Open Problem 8, which asks for explicit bounds on |a(n,m) − a(m)|.*

Computing the harmonic descent chain's visit probabilities directly from a(n,n) = 1 and
a(n,m) = Σ_{i>m} a(n,i)/(h_{i−1}(i−m)) (validated: a(n,2) → 0.607927, a(n,5) → 0.316629):

- **The discrepancy is exactly the root term.** For the counterexample f = 1{j = 2^r} the gap runs
  0.9724, 0.9850, 0.9919, 0.9956 at n = 256…2048 — converging to 1 = a(n,n)f(n). My earlier
  argument gave only liminf ≥ 1; the computation shows it *equals* the root term.
- **No dominated-convergence proof can work**, for a quantified reason: sup_n a(n,i) = a(i,i) = 1
  on the diagonal while a(i) ≈ (6/π²)log i/i, so sup_n a(n,i)/a(i) = 1/a(i) diverges like i/log i —
  measured 1.64, 3.16, 6.36, 19.41 at i = 2, 5, 13, 55. Any correct Ansatz needs a hypothesis
  controlling f near the diagonal, not merely polynomial growth.
- **The repair.** Add f(n) → 0 to part (i). Then the gap vanishes in every case tested: f = j^{−1/2}
  gives −0.407 → −0.158 and f = 1/log³j gives −0.0497 → −0.0259 over the same range. For part (ii)
  the analogue is f(n) = o(Σ_{i≤n}a(i)f(i)) — which is why the authors' own applications survive:
  the Colless weight tends to ½, so the root term is O(1) against a sum of order log²n.
- **Their monotonicity conjecture holds.** They state that numerics support n ↦ a(n,i) decreasing;
  over seventeen values of n up to 1350 and nine values of i up to 89, 114 consecutive pairs, zero
  violations.

---

## 4. Romik's maximal-dimension Young diagram — the algorithm half

*"Describe the shape explicitly or by an efficient algorithm, prove it is unique."*

- **Uniqueness up to conjugation extends to n ≤ 44** (the campaign had n ≤ 40), exhaustively. The
  qualifier is forced, not cosmetic: dim(λ) = dim(λ′) identically.
- **Single-box hill-climbing provably fails.** Over n = 4…44 there are exactly four strict local
  maxima that are not global, and the first two are the **staircases**: δ₆ = (6,5,4,3,2,1) at
  n = 21 (gap 0.0164) and δ₇ = (7,6,5,4,3,2,1) at n = 28 (gap 0.1667), with a conjugate pair at
  n = 38 (gap 0.2400). Note 21 = T₆ and 28 = T₇. It is *not* a general fact about staircases — δ₃,
  δ₄, δ₅, δ₈ (n = 6, 10, 15, 36) trap nothing.
- **Radius 2 suffices on this range.** Of those four traps, zero survive two-box moves. So local
  search solves the problem for every n ≤ 44 provided the neighbourhood has radius ≥ 2, and radius 1
  first fails at n = 21.

*Method note*: hill-climbing alone would have reported success at 43 of 44 values and looked like a
working algorithm. Only comparison against exhaustive ground truth exposed n = 38, and only direct
enumeration of local maxima found the smaller n = 21 and n = 28 traps that random starts missed.

---

## 5. Lyons's Question 2.8 — the union coupling, reframed

*Given orthogonal projections with Q = Q₁+Q₂, is there a coupling of P_{Q₁}, P_{Q₂} whose union is
P_Q?* Ranks add, so the two sets must be disjoint a.s.

- Feasible in all 108 LP instances across nine rank splits, extending the campaign's evidence.
- **The obstruction, named.** With Q = VV\*, det(Q_S) = |det(V_S)|². Writing V = [V₁ V₂], the
  Laplace expansion along the first k₁ columns gives det(V_U) = Σ ±det((V₁)_{S₁})det((V₂)_{U∖S₁}).
  So P_Q(U) is the squared modulus of a **sum**, while independent splitting gives the **sum of
  squared moduli** — they differ by exactly the interference cross terms. That is why conditional
  splitting is not the coupling, and it states the question sharply.
- **The coupling is not unique** — spreads of 0.018 to 0.071 across six objective directions. The
  three marginal constraints leave a positive-dimensional polytope, so there is no canonical
  coupling to find by uniqueness; a proof must construct one with enough structure to be checkable.

---

## 6. The MMPP folklore conjecture — reduced to a negative correlation

*Conjecture 4.1 of the MAP open-problems paper: is the squared coefficient of variation of a Markov
modulated Poisson process at least 1?* The source says the authors believed it easy to verify and
that no proof is known for an arbitrary irreducible MMPP.

With D0 = Q−D, D1 = D and A := (D−Q)⁻¹, put **h := A1** — exactly the vector of mean times to the
next arrival from each state. Since πQ = 0 we have π(D−Q) = πD, giving two exact identities:

  **πDh = π·1 = 1**  and  **πDA²1 = π(D−Q)Ah = πh.**

Substituting into c² ≥ 1 (i.e. E[T²] ≥ 2E[T]²) collapses everything to

  **(π·λ)(π·h) ≥ (π·λh)² = 1,  i.e.  Cov_π(λ, h) ≤ 0.**

So the conjecture says precisely: *the arrival rate and the mean time to the next arrival are
negatively correlated under the stationary law.* Intuitively obvious — a high-rate state should have
a short wait — which is presumably why it is folklore, and it is exactly the unproved step.

**Verified.** πDh = 1 to 1.2×10⁻¹² over 140,000 random MMPPs; Cov_π(λ,h) ≤ 0 in every one (largest
value −8.1×10⁻¹¹); and the sign of c²−1 agreed with the sign of −Cov in all 140,000, so the
equivalence is confirmed, not merely derived. A separate search over 240,000 MMPPs at m = 2…8,
including deliberately non-reversible cyclic generators with a skew parameter, found minimum
c² = 1.00000000 exactly and nothing below.

**A second reading.** πh = ∫P(no arrival by t)dt is the mean forward recurrence time and 1/(π·λ) is
the mean interarrival time, so the conjecture is the inspection paradox for MMPPs: the wait seen
from a random instant is at least the mean gap. Equivalently — and this is the real content of the
folklore — *modulating a Poisson rate can only add variability*. Equality is exactly λ constant.

**Proved in passing.** h is monotone in the rates: differentiating (D−Q)h = 1 gives
∂hⱼ/∂λᵢ = −hᵢAⱼᵢ ≤ 0, since A = ∫e^{(Q−D)t}dt is entrywise nonnegative. Raising any arrival rate
shortens every state's expected wait. The right kind of ingredient, but not sufficient on its own,
since the covariance is across states under π rather than a derivative.

The remaining task is a correlation inequality for a **non-reversible** chain. For reversible Q the
deviation matrix is self-adjoint in the π-inner product with nonnegative spectrum off the constants
and the result follows — which already covers every two-state MMPP, since all two-state chains are
reversible.

---

**CLOSED later the same day (2026-09-08).** The reduction above was the right object seen from the
wrong side. Write the time-stationary survival as the Cox conditional expectation
S(t) = E_pi[exp(-integral_0^t lambda(X_s) ds)]; exp is convex and the exponent has mean lambda* t by
stationarity, so S(t) >= exp(-lambda* t) for every t, hence E[T^pi] = integral S >= 1/lambda* = E[T^alpha],
and the source's own Lemma 2.1 gives c^2 >= 1. No reversibility, no spectral argument. The same
line proves the general Cox-process form conjectured in the withdrawn arXiv:1802.08400, with equality
iff Poisson. The stochastic order (their Conjecture 4.2) does not follow. Lean: Prob1000/E0077.lean
(Jensen step, integral comparison, Palm algebra and assembly certified). Full account:
Downloads/Probability_E0077_MMPP_scv_proved_2026-09-08.md.

## Standing caveat

Prior art is unchecked on all five. That is the whole distance to any publishable claim, and nothing
here should be described as new until someone does the citation check.
