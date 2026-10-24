Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0029 — scaled positive tilt, D4 symmetry, and a source-equivalent free-energy criterion

Worker: `R7-04`  
Native ID: `6aabe7ea6e1881919a65503f8445a813`  
Canonical target: `P0029`  
Classification: CLOSABLE OUTSIDE  
Run-start master snapshot: `a2edb89a3281f9ee2bcbc5fa99354d1b9835ae95`  
Fresh pre-delivery master snapshot: `a2c6dadd5b27691ad8823436a80048e3a880b7d1`  
Previous report: `research7_2026-09-17/R7-04/runs/2026-09-18/2026-09-18T223800Z__report.md` @ `977ead471881528673145d42bae8c23630ad53a3`  
Frozen source metric: `D_* := limsup_n E[rho_n/n | exactly two peaks]`.

## 1. Source and scope

Krzysztof Burdzy's living page *My favorite open problems*, Problem 9, asks: for a uniformly random labeling of the `n x n` nearest-neighbor square conditioned on exactly two peaks, does their graph distance `rho_n` satisfy `rho_n/n -> 0` in distribution?

Primary source, checked 2026-09-19 local: https://sites.math.washington.edu/~burdzy/open_mathjax.php . The page still labels this as Problem 9 and refers to Billey–Burdzy–Sagan (2013) and Burdzy–Pal (2020).

A bounded current literature check also recovered:

- K. Burdzy and S. Pal, *Twin peaks*, Random Structures & Algorithms 56 (2020), 432–460, DOI 10.1002/rsa.20883. Its abstract treats one-peak square geometry, ladders, and two-peak tree settings, not the square-grid asymptotic in Problem 9.
- P. Agrawal, A. H. Erturk, A. Louis, *Successive vertex orderings of connected graphs*, arXiv:2604.07408 (2026), which gives exact general successive-ordering/inclusion–exclusion machinery. The P0029 reductions below therefore make no novelty claim about general successive-order enumeration.

Search misses are negative evidence only; they are not a novelty or openness certificate.

## 2. Input from the cumulative P0029 work

Let `G_n` be the `n x n` square. The previous run proved a positive first-merge decomposition. For a connected component `C`, let

`h_C(r)` = number of successive orderings of `C` rooted at `r`,

`R(C) = sum_{r in C} h_C(r)`,

`mu_C(r) = h_C(r)/R(C)`.

For a two-component pre-merge state `S=A sqcup B`, with no edge between `A` and `B`, let `g_n(S)` be the number of allowed first-merge-plus-birth-free suffixes from `S`. The exact absorption weight is

`Omega_n(S) = binom(|S|,|A|) R(A) R(B) g_n(S)`.

Conditional on `S` under the exactly-two-peak law, the two peak roots are independent with distributions `mu_A` and `mu_B`. This is a positive representation of the actual conditioned pair law, not a surrogate.

The preceding run also defined the component barycenter and variance and reduced the source to a positive dispersion quantity. The present run changes category again: rather than try to bound the zero-field second moment directly, it introduces a spatial field and turns P0029 into a finite-field free-energy question.

## 3. B5 — introduce a parameter and differentiate

Embed the square in coordinates `{1,...,n}^2`. For each connected component `C`, define the rooted spatial partition function

`Z_C(theta) := sum_{r in C} h_C(r) exp(theta dot r)`, `theta in R^2`.

Then, at zero field,

`grad log Z_C(0) = b(C)`,

and

`tr Hess log Z_C(0) = V(C)`.

Thus the barycenter and dispersion found in the previous run are exactly the first two derivatives of a positive rooted partition function.

To remove any arbitrary ordering of the two components, for an unordered first-merge state `{A,B}` define

`K_{A,B}(theta) := (1/2) [ Z_A(theta) Z_B(-theta) + Z_A(-theta) Z_B(theta) ]`.

Define the global tilted absorption partition

`mathcal Z_n(theta) := sum_{ {A,B} } binom(|A|+|B|,|A|) g_n(A sqcup B) K_{A,B}(theta)`,

where the sum ranges over all unordered two-component pre-merge states occurring in the positive first-merge decomposition.

At `theta=0`,

`mathcal Z_n(0) = sum_S Omega_n(S)`.

Now sample the actual pair of peaks under the exactly-two-peak conditioning and orient the pair by an independent fair coin. Write the oriented roots as `(R_1,R_2)` and `D_n=R_1-R_2`. The positive first-merge theorem gives the exact identity

`mathcal Z_n(theta)/mathcal Z_n(0) = E[ exp(theta dot D_n) | exactly two peaks, fair orientation ]`.  (3.1)

This is the key point: the partition function is the moment generating function of the **actual** conditioned peak displacement.

For the first coordinate, put

`Y_n := (D_n)_1 / n`, so `|Y_n| <= (n-1)/n < 1`,

and for real `s` define the scaled log-free-energy

`psi_n(s) := log mathcal Z_n((s/n)e_1) - log mathcal Z_n(0)`.

By (3.1),

`psi_n(s) = log E exp(s Y_n)`.  (3.2)

The field is scaled by `1/n`, which is the source's macroscopic spatial scale. No thermodynamic normalization by `n^2` is inserted: because `Y_n` is bounded, a constant positive limit of `psi_n(s)` is exactly the relevant scale.

## 4. B14 — exploit square symmetry

The fair orientation makes `Y_n` symmetric about zero. The dihedral symmetry `D_4` of the square exchanges the coordinate axes and their signs. Hence

`E Y_n = 0`,

`E (D_n)_1^2 = E (D_n)_2^2`,

and the two-dimensional Hessian at zero is a scalar multiple of the identity.

Let

`V_n := E Y_n^2 = psi_n''(0)`.

If

`m_n := E[rho_n/n | exactly two peaks]`,

then, because Manhattan distance is `rho_n = |(D_n)_1| + |(D_n)_2|` and the two coordinates have equal absolute first moments,

`m_n = 2 E |Y_n|`.  (4.1)

Since `0 <= |Y_n| <= 1`,

`Y_n^2 <= |Y_n|`,

and Cauchy–Schwarz gives `E|Y_n| <= sqrt(EY_n^2)`. Therefore

`2 V_n <= m_n <= 2 sqrt(V_n)`.  (4.2)

Consequences:

1. `m_n -> 0` iff `V_n -> 0`.
2. Because `rho_n/n` is uniformly bounded, the source statement `rho_n/n -> 0` in distribution is equivalent to `m_n -> 0`.
3. Thus Burdzy Problem 9 is YES iff `V_n -> 0`.
4. A subsequence with `V_n >= c>0` gives `D_* >= 2c>0` by the left inequality in (4.2), hence a source-valid NO.

This is stronger and cleaner than the previous Euclidean second-moment lower bound: D4 symmetry converts the one-coordinate variance directly into the source's Manhattan mean.

## 5. Uniform finite-field/zero-field comparison

The main new theorem is that a fixed nonzero scaled field is quantitatively equivalent to the zero-field variance.

### Theorem 5.1 (bounded exponential-tilt comparison)

For every `n` and every `s>=0`, let `P_{n,s}` be the exponential tilt of the law of `Y_n`:

`dP_{n,s}/dP_{n,0} (y) = exp(sy)/E exp(sY_n)`.

Then

`e^{-2s} V_n <= Var_{n,s}(Y_n) <= e^{2s} V_n`.  (5.1)

Consequently,

`a_-(s) V_n <= psi_n(s) <= a_+(s) V_n`,  (5.2)

where

`a_-(s) = (2s - 1 + e^{-2s})/4`,

`a_+(s) = (e^{2s} - 1 - 2s)/4`.

For every fixed `s>0`, both constants are strictly positive. Therefore

`psi_n(s)/a_+(s) <= V_n <= psi_n(s)/a_-(s)`.  (5.3)

#### Proof

Because `|Y_n|<=1`,

`e^{-s} <= exp(sY_n) <= e^s`

and likewise

`e^{-s} <= E exp(sY_n) <= e^s`.

Hence the Radon–Nikodym density obeys the deterministic bounds

`e^{-2s} <= dP_{n,s}/dP_{n,0} <= e^{2s}`.  (5.4)

Variance has the variational representation

`Var_Q(Y) = inf_a E_Q[(Y-a)^2]`.

Applying the lower density bound in (5.4) for every `a` gives

`Var_{n,s}(Y_n) >= e^{-2s} inf_a E_{n,0}[(Y_n-a)^2] = e^{-2s}V_n`.

For the upper bound, evaluate the variational expression at the zero-field mean `a=E_{n,0}Y_n=0` and use the upper density bound:

`Var_{n,s}(Y_n) <= E_{n,s}Y_n^2 <= e^{2s} E_{n,0}Y_n^2 = e^{2s}V_n`.

This proves (5.1).

From (3.2), standard differentiation of the log-mgf gives

`psi_n''(u) = Var_{n,u}(Y_n)`.

Symmetry gives `psi_n(0)=psi_n'(0)=0`, so

`psi_n(s) = integral_0^s (s-u) psi_n''(u) du`.

Use (5.1) with `u` in place of `s`. The lower integral is

`V_n integral_0^s (s-u)e^{-2u}du = V_n (2s-1+e^{-2s})/4`,

and the upper integral is

`V_n integral_0^s (s-u)e^{2u}du = V_n (e^{2s}-1-2s)/4`.

This is (5.2), hence (5.3). QED.

### Corollary 5.2 (source-equivalent finite-field criterion)

Fix **any one** `s>0`. Then the following are equivalent:

1. `rho_n/n -> 0` in distribution under the exactly-two-peak conditioning;
2. `m_n -> 0`;
3. `V_n -> 0`;
4. `psi_n(s) -> 0`;
5. `mathcal Z_n((s/n)e_1)/mathcal Z_n(0) -> 1`.

Thus a source-valid refutation is obtained from the finite-field statement

`limsup_n [ log mathcal Z_n((s/n)e_1) - log mathcal Z_n(0) ] > 0`  (5.5)

for **one fixed** `s>0`.

Conversely, if the source YES statement is true, every fixed scaled field has vanishing free-energy gain.

This is a source-exact equivalence, not merely a sufficient condition.

## 6. B28 — typical rather than worst-case peak pairs

The free-energy criterion can also be expressed as a typical-mass criterion without pointwise control.

For `0<a<1`, splitting according to `|Y_n|<a` and `|Y_n|>=a` gives

`a^2 P(|Y_n|>=a) <= V_n <= a^2 + (1-a^2) P(|Y_n|>=a)`.  (6.1)

Hence if `V_n >= c>a^2`,

`P(|Y_n|>=a) >= (c-a^2)/(1-a^2)`.  (6.2)

Conversely, if along a subsequence

`P(|Y_n|>=a) >= eta`,

then `V_n >= a^2 eta` on that subsequence.

Combining with Theorem 5.1, the following are equivalent as **positive-limsup** statements:

- `D_*>0`;
- `limsup V_n>0`;
- for any fixed `s>0`, `limsup psi_n(s)>0`;
- there exist `a,eta>0` and a subsequence with `P(|(D_n)_1| >= an) >= eta`.

Therefore the next researcher need not compare every root pair, every first-merge state, or even every `n`. It is enough to prove a positive finite-field gain or positive macroscopic coordinate-separation mass along one subsequence.

## 7. Obstruction revealed by B5

The parameter trick does **not** itself prove a positive free-energy gain. The exact remaining obstruction is now:

> prove or disprove that for some fixed `s>0`, the positive ratio `mathcal Z_n((s/n)e_1)/mathcal Z_n(0)` stays bounded away from `1` along a subsequence.

A naive unscaled field `theta=s e_1` is misleading: it rewards `O(n)` displacements by exponentially large factors and can be dominated by an exponentially tiny exceptional set. The `1/n` scaling is essential. Theorem 5.1 is useful precisely because the scaled random variable is uniformly in `[-1,1]`, so finite-field and zero-field behavior are uniformly comparable.

The earlier local-seed-shift approach also remains insufficient: the first-merge weight contains a full suffix partition and can change through an entire growth history. The new criterion avoids needing local ratios, but it does not yet supply the required asymptotic lower bound.

## 8. Relation to previous P0029 reductions

This run strengthens the cumulative chain as follows:

1. exact birth/restart encoding;
2. exact actual-pair inclusion–exclusion kernel;
3. positive first-merge mixture for the actual pair;
4. reversible root conductances inside each component;
5. barycenter/dispersion and absorption-flux reduction;
6. **new:** exact scaled positive partition `mathcal Z_n` whose fixed-field gain is equivalent to the original source statement.

No hypothesis imported from a peer report is used circularly: the only cumulative inputs are the previously proved exact positive first-merge mixture and its conditional root independence, both already checked on all connected graphs through five vertices in the earlier exact certificate.

## 9. Metric and status

Frozen metric before: `D_* = UNKNOWN/UNMEASURED`.

Frozen metric after: `D_* = UNKNOWN/UNMEASURED`.

Movement: **NO MOVEMENT in the frozen source metric**.

The run does produce a stricter equivalent target, (5.5), but it does not establish a positive or zero asymptotic value. Therefore the honest source status remains **OPEN / PARTIAL**.

This is the sixth ordinary unchanged research run on the CLOSABLE target P0029 (with the mandatory STUCK1 diagnosis between ordinary runs 3 and 4). Under Section I of the owner directive, R7-04 must now retire this target from its own active research, preserve an immutable handoff, and rotate to a freshly admitted eligible shard-3 outside source. The retirement is operational for R7-04; it is not a mathematical claim that P0029 is solved or globally abandoned.

## 10. Handoff recommendation

The best next attack is no longer another finite-grid enumeration. It is to lower-bound the **scaled** positive free-energy gain in (5.5). Three plausible future methods, for a successor researcher rather than this retired slot, are:

- identify a positive family of first-merge states whose component root partition functions retain a macroscopic `x`-separation under the `1/n` field;
- prove a comparison principle for the scaled tilted absorption partition under geometric coarse-graining;
- exploit a strip/rectangle decomposition to show that the finite-field gain cannot vanish on all scales.

Any future continuation should preserve the exact `1/n` field scaling. An unscaled tilt is not source-equivalent and can be driven by exponentially rare pairs.
