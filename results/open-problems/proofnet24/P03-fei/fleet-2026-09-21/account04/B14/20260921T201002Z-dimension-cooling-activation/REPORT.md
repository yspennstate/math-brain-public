# B14 — dimension-cooling activation reserve for adaptive FEI restriction

**Status:** PARTIAL / PROVED auxiliary selector machinery. **Full uniform-cube Fourier entropy-influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Route:** realizable adaptive restriction / mass-weighted erasure selector.  
**Publication priority:** UNVERIFIED; no novelty claim.

## 1. Fresh dependency and method change

This run consumes the current cross-account FEI coordination state and, substantively, the completed account03/B14 result
`proofnet24/P03-fei/fleet-2026-09-21/account03/B14/20260921T183435Z-linear-activation-telescope/REPORT.md`.
That report proved the exact fixed-noise activation potential
\[
P_z(f)=\frac{1-M_f(z)}{1-z},\qquad M_f(z)=\sum_S\widehat f(S)^2z^{|S|},
\]
with local physical-restriction drop
\[
A_i^{(z)}(f)=\Delta_iP_z(f)=\sum_{S\ni i}\widehat f(S)^2z^{|S|-1},
\]
and it proved a tensor-padding no-go: **every fixed** \(z<1\), and every fixed mixture of such scales without an atom at 1, loses its local rebate under disjoint tensor powers.

The new step here is to let the scale move with the physical restriction state, while preserving a one-use global budget. The allowed motion is monotone: the noise scale may only decrease down the restriction tree. This is enough to evade the fixed-scale tensor-padding disappearance.

The previously proved account04/B14 crossing-amplified corrected-erasure theorem remains compatible and is not weakened: prescribed-coordinate payment is still false in general, and the present result is a reserve for an **adaptive existential selector**, not an every-coordinate FEI theorem.

## 2. Adaptive cooling telescope

For \(0\le z<1\), put
\[
\Phi_z(k)=1+z+\cdots+z^{k-1}=\frac{1-z^k}{1-z},\qquad \Phi_z(0)=0,
\]
and define \(P_z(f)=\sum_S\widehat f(S)^2\Phi_z(|S|)\). Set \(P_1(f)=I(f)\).
For every Boolean \(f\),
\[
0\le P_z(f)\le I(f),
\]
and \(P_z(f)\) is nondecreasing in \(z\).

Consider any finite adaptive physical restriction tree. Let \(w_u\) be the probability of reaching node \(u\), let \(f_u\) be the current Boolean function, and let the node query coordinate \(i(u)\). Assign a scale \(z_u\in[0,1]\) to every node such that each child \(v\) satisfies
\[
z_v\le z_u.
\tag{2.1}
\]

### Theorem 2.1 — adaptive-scale activation budget

\[
\boxed{
\sum_{u\ \mathrm{internal}} w_u A_{i(u)}^{(z_u)}(f_u)
\le P_{z_{\rm root}}(f)
\le I(f).
}
\tag{2.2}
\]

### Proof

At a node \(u\), the fixed-scale identity from the consumed account03 result gives
\[
A_{i(u)}^{(z_u)}(f_u)
=P_{z_u}(f_u)-\mathbb E_{v\mid u}P_{z_u}(f_v).
\tag{2.3}
\]
Since \(P_z(g)\) is nondecreasing in \(z\) and \(z_v\le z_u\),
\[
P_{z_u}(f_v)\ge P_{z_v}(f_v).
\]
Therefore
\[
A_{i(u)}^{(z_u)}(f_u)
\le P_{z_u}(f_u)-\mathbb E_{v\mid u}P_{z_v}(f_v).
\tag{2.4}
\]
Multiplying by \(w_u\) and summing telescopes over the tree. The leaf potentials are nonnegative, leaving at most the root potential. Finally \(P_{z_{\rm root}}\le I\). QED.

Thus scale adaptation in the **cooling direction is free**: it does not create a new root charge.

## 3. Canonical dimension-cooling schedule

At a state with \(d\ge1\) unresolved physical variables choose
\[
\boxed{z_d=1-\frac1d},\qquad z_0=0.
\tag{3.1}
\]
Every proper restriction decreases \(d\), hence the scales satisfy (2.1).
For a relevant coordinate \(i\), every Fourier set containing \(i\) has size at most \(d\), so
\[
z_d^{|S|-1}\ge z_d^{d-1}=\left(1-\frac1d\right)^{d-1}\ge e^{-1}.
\]
Consequently
\[
\boxed{
e^{-1}\operatorname{Inf}_i(f)
\le A_i^{(z_d)}(f)
\le \operatorname{Inf}_i(f).
}
\tag{3.2}
\]
The point is not the crude factor \(e^{-1}\); it is that the scale is allowed to approach 1 in high dimension and automatically cools as restrictions remove variables, while the total activation charge is still at most the original influence by (2.2).

## 4. Decisive tensor-padding calculation

Let a nonconstant seed \(g\) use \(r\) variables and have total influence \(I_g\). Form the disjoint product
\[
F_m=g^{\otimes m}
\]
on \(d=mr\) variables. For a coordinate \(i\) in one copy,
\[
\frac{A_i^{(z)}(F_m)}{\operatorname{Inf}_i(F_m)}
=
\frac{A_i^{(z)}(g)}{\operatorname{Inf}_i(g)}M_g(z)^{m-1}.
\tag{4.1}
\]
The fixed-scale result has \(M_g(z)^{m-1}\to0\) for every fixed \(z<1\). Under dimension cooling, however, take \(z=z_{mr}=1-1/(mr)\). Since
\[
M_g(1-\varepsilon)=1-I_g\varepsilon+O(\varepsilon^2)
\]
and \(A_i^{(z)}(g)\to\operatorname{Inf}_i(g)\) as \(z\uparrow1\),
\[
\boxed{
\lim_{m\to\infty}
\frac{A_i^{(z_{mr})}(F_m)}{\operatorname{Inf}_i(F_m)}
=e^{-I_g/r}>0.
}
\tag{4.2}
\]
So the adaptive schedule **provably escapes the exact tensor-padding mechanism that kills every fixed noise scale**.

For balanced majority on three bits, \(I_g=3/2\), hence the limit is \(e^{-1/2}=0.6065306597\ldots\). Direct values from the checker are
\[
0.7222222,\ 0.6520865,\ 0.6349429,\ 0.6227579,\ 0.6143669,
\]
for \(m=1,2,3,5,10\), and \(0.6066065\) at \(m=1000\). The fixed \(z=1/2\) rebate in the consumed account03 report instead decays to zero.

## 5. Exact block activation and Bernoulli-erasure formula

The construction extends exactly to physical blocks. For \(A\subseteq[d]\), define the fixed-scale block drop
\[
L_A^{(z)}(f)=P_z(f)-\mathbb E_a P_z(f_{A=a}).
\]
Pairing Fourier coefficients under the restriction gives
\[
\boxed{
L_A^{(z)}
=
\sum_S\widehat f(S)^2
z^{|S\setminus A|}\Phi_z(|S\cap A|).
}
\tag{5.1}
\]
In particular \(0\le L_A^{(z)}\le I_A:=\sum_{i\in A}\operatorname{Inf}_i(f)\).
For the dimension-cooling scale \(z_d\), whenever \(S\cap A\ne\varnothing\), the factor in (5.1) is at least \(e^{-1}\); hence
\[
\boxed{
L_A^{(z_d)}
\ge e^{-1}\Pr_{S\sim\widehat f^2}[S\cap A\ne\varnothing].
}
\tag{5.2}
\]

If \(A_t\) contains each physical coordinate independently with probability \(t\), then the block reserve has the exact one-dimensional expectation
\[
\boxed{
\mathbb E L_{A_t}^{(z)}
=
\frac{M_f(z+t(1-z))-M_f(z)}{1-z}.
}
\tag{5.3}
\]
Indeed, for a Fourier set of size \(k\), \(|S\setminus A_t|\) is binomial and
\(\mathbb E z^{|S\setminus A_t|}=(z+t(1-z))^k\).

The same adaptive telescope as Theorem 2.1 holds for block-query trees: use (5.1) as the node payment and require only that child scales do not exceed the parent scale.

## 6. A concrete full-FEI compiler target

Fix a median character at the root so that root ordinary influence equals folded influence \(J\); do **not** re-gauge descendants. Character multiplication preserves spectral entropy, and ordinary influence then telescopes under physical restrictions.

Let \(B_i=H(X_i\mid X_{-i})\). The inherited bounded influence potential \(\Phi=\sum_i\mathfrak j(p_i)\) pays the restriction recombination term and satisfies \(\Phi\le(2/\ln2)I\). Therefore the following would be sufficient for full FEI:

> Find finite constants \(K,\lambda\) and an adaptive restriction policy using a nonincreasing scale (for example \(z_d=1-1/d\)) such that at every nonconstant state the selected physical coordinate satisfies
> \[
> \boxed{B_i\le Kp_i+\lambda A_i^{(z_d)}.}
> \tag{6.1}

Then entropy restriction telescoping, the influence telescope, Theorem 2.1, and the existing \(\Phi\)-payment give
\[
\boxed{H(f)\le\left(K+\lambda+\frac2{\ln2}\right)I(f).}
\tag{6.2}
\]
This is a genuine realizable selector compiler. The corresponding Bernoulli-block sufficient condition is controlled by the exact average
\[
tH-D(t)-\lambda\frac{M_f(z+t(1-z))-M_f(z)}{1-z}-KtI.
\tag{6.3}
\]
A negative value selects a physical block with \(B_A<KI_A+\lambda L_A^{(z)}\).

Equation (6.1) is **not proved here**. The crude universal bound (3.2) alone cannot improve a constant after paying the root \(\lambda I\); the missing gain must correlate high conditional-entropy payment with unusually large activation reserve. This is the precise next stopping-policy problem.

## 7. Verification

`check_dimension_cooling.py` directly recomputes Fourier spectra for deterministic Boolean test families through dimension four. It checks:

1. the exact block identity (5.1) on 100 block/function cases;
2. the Bernoulli identity (5.3) at three erasure rates;
3. the adaptive dimension-cooling telescope on complete physical decision trees;
4. the majority-three tensor-power calculation.

Observed maximum absolute errors were \(2.78\times10^{-16}\) for (5.1) and \(3.33\times10^{-16}\) for (5.3); the largest `spent - root potential` value was exactly `0.0` in double arithmetic. The computation is a sanity check only; the proofs above are analytic.

Checker SHA-256: `74a9f2aaef76f1af3368a74c54cadbd97c6009fc92609dbecafa22d4036c20b8`.  
Captured output SHA-256: `894d6564dbb34b3c0792fccc81fd0a63a7fd70e3a3a4d7e035edd58319e73c24`.

## 8. What this changes and what remains open

The account03 fixed-scale no-go is not the end of the activation-reserve route: **state-adaptive monotone cooling retains a one-use influence budget and survives the same tensor-padding test by a positive constant.** This supplies a new candidate resource for the account04 posterior-crossing stopping policy.

It does not prove FEI. The next missing universal implication is to join the existing crossing-amplified selector with (6.1): on a corrected-ratio critical core, show that one physically realizable coordinate or block either spends enough posterior-crossing/instability slack to descend, or has enough dimension-cooled activation to pay its conditional spectral entropy. A proof must exploit Boolean structure; the uniform lower bound (3.2) by itself is too weak.
