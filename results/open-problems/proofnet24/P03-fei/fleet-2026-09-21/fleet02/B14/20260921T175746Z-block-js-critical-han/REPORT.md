TASK: B14 ACCOUNT: fleet02 RUN: 2026-09-21T17:57:46.647392Z — block recombination tensorization, fractional-Han criticality, and coordinatewise refunded selector

**Status:** PARTIAL / proved universal auxiliary theorems and a stronger localization of any restriction-critical FEI counterexample. **Full uniform-cube Friedgut–Kalai Fourier entropy-influence remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated math_brain or cognitive-memory retrieval/context was used.

**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. Configured reasoning level and provider reasoning-token/time usage: UNKNOWN / not exposed.

**Creative moves used:** FLEET_RULES #3 (prove a stronger all-block statement), #11 (dualize the restriction payment into complementary marginal entropy), and #27 (swap the selector quantifier only after passing to a restriction-critical descendant; do not assert the known-false every-prescribed-coordinate universal payment).

## 0. Fresh frontier and exact scope

Fresh `yspennstate/math-open-problems` master was recovered during the run, initially at `4faf215f342ddef184d58ef68e4e914ad1d6b5b1` and refreshed before writing to `385fa72dde1a1105c9145c9667232c1adf1c515b`. I read the current `FLEET_RULES.md`, `proofnet24/P03-fei/README.md`, the September-21 FEI task packet, the newest B14 centered-refunded selector, fleet04/B14's strong-concavity recombination rebate, fleet01/B18's centered-tangent/Han integration, fleet02/B18's joint phase packing, and the fresh B13 Boolean phase/Palm work.

The current unrestricted FEI lower-bound scale used only for numerical localization is

\[
C_0=6.521845710923046575,
\]

from the externally sourced certified 18-variable monotone construction already recovered in the repository. This is not a new lower-bound claim. The full conjecture has no known finite universal upper bound.

The newest B14 report proved the centered refunded singleton selector. For the spectral sample `X`, with

\[
p_i=\Pr(i\in X),\qquad q_i=\min(p_i,1-p_i),
\]

and after median-character centering, it defined

\[
t_i={\widehat g(\{i\})^2\over q_i}
\]

and proved the coordinate erasure bound

\[
B_i\le q_i F(t_i),
\tag{0.1}
\]

where `F` is the explicit decreasing scalar function in that report. The previous corollary used the linear recombination surcharge `2q_i/ln 2` and obtained only an **average** centered first-shell localization.

The fresh fleet04/B14 result gives the strictly sharper universal singleton recombination envelope

\[
JS_i\le \mathfrak j(q_i),
\qquad
\mathfrak j(s):=1-h_2\!\left({1\over2}+\sqrt{s(1-s)}\right),
\tag{0.2}
\]

where `mathfrak j` is increasing and strongly concave on `[0,1/2]`, with

\[
\mathfrak j(s)\le {2\over\ln2}\left(s-{s^2\over3}\right).
\tag{0.3}
\]

The main new step below is that (0.2) **tensorizes to every physical restriction block** without a block-size factor. That yields a full fractional-Shearer/Han hierarchy for a restriction-critical descendant and upgrades the previous shell statement from an average to a coordinatewise condition.

No novelty or publication-priority claim is made. A bounded current-literature search was performed; failure to locate the exact statements below is not novelty evidence.

## 1. Normalization and block restriction decomposition

Let

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad a_S=\widehat f(S),\qquad \mu(S)=a_S^2,
\]

and let `X~mu`. Write

\[
H=H(X),\qquad p_i=\Pr(i\in X)=\operatorname{Inf}_i(f),\qquad I=\sum_i p_i.
\]

For a physical block `A subseteq [n]`, define

\[
I_A:=\sum_{i\in A}p_i,
\qquad
B_A:=H(X_A\mid X_{A^c}).
\tag{1.1}
\]

For each physical assignment `z in {-1,1}^A`, let `f_{A=z}` be the restriction, and define

\[
\Delta_A H
:=H(f)-2^{-|A|}\sum_z H(f_{A=z}).
\tag{1.2}
\]

Write a Fourier index as `T union U` with `T subseteq A^c`, `U subseteq A`. For a fixed outside label `T`, the restricted child coefficient is

\[
\widehat {f_{A=z}}(T)=\sum_{U\subseteq A} z^U a_{T\cup U}.
\]

Let `nu_z` be the squared Fourier law of this child on `A^c`. Walsh orthogonality in `z` gives

\[
2^{-|A|}\sum_z \nu_z(T)
=\sum_{U\subseteq A}a_{T\cup U}^2
=\Pr(X_{A^c}=T).
\tag{1.3}
\]

Therefore, if

\[
JS_A:=H(X_{A^c})-2^{-|A|}\sum_z H(\nu_z),
\tag{1.4}
\]

then `JS_A` is exactly the Jensen–Shannon mutual information between the uniform restriction label `Z_A` and the final child spectral label on `A^c`, so `JS_A>=0`, and

\[
\boxed{\Delta_AH=B_A+JS_A.}
\tag{1.5}
\]

For a singleton this is the inherited identity `Delta_i H=B_i+JS_i`.

The influence identity also tensorizes exactly:

\[
\boxed{
I(f)=I_A+2^{-|A|}\sum_z I(f_{A=z}).
}
\tag{1.6}
\]

This follows either from the cube-edge definition of influence or by averaging the remaining Fourier degrees using (1.3).

## 2. PROVED: block recombination tensorization with the strong-concavity rebate

### Theorem 2.1 — centered block-JS tensorization

For every Boolean `f` and every physical restriction block `A`,

\[
\boxed{
JS_A(f)\le\sum_{i\in A}\mathfrak j(q_i),
\qquad q_i=\min(p_i,1-p_i).
}
\tag{2.1}
\]

Consequently, with `kappa=2/ln 2`,

\[
\boxed{
JS_A(f)
\le \kappa\sum_{i\in A}\left(q_i-{q_i^2\over3}\right)
\le \kappa\sum_{i\in A}q_i.
}
\tag{2.2}
\]

This is a block statement; no factor `|A|` multiplies a worst marginal. Each coordinate's centered recombination budget is paid once.

### Proof

Order the block as `A={i_1,...,i_k}`. Let `Z_1,...,Z_k` be the independent uniform physical restriction signs. Let `T` denote the final child Fourier label on `A^c`, sampled from the child spectral law after all restrictions. By (1.3),

\[
JS_A=I(Z_1,\ldots,Z_k;T).
\]

Apply the mutual-information chain rule:

\[
JS_A=\sum_{t=1}^k I(Z_t;T\mid Z_{<t}).
\tag{2.3}
\]

Fix a previous restriction history `Z_{<t}=z`. Let `f_z` be the resulting Boolean descendant before restricting `i_t`. Conditional on `Z_t=+1` or `-1`, the final law of `T` is obtained by taking the corresponding immediate child's spectral law and projecting its Fourier label onto the still-unrestricted final coordinate set `A^c`: averaging over the later physical restriction signs kills all cross terms by the same Walsh orthogonality as (1.3). Hence data processing for Jensen–Shannon/mutual information gives

\[
I(Z_t;T\mid Z_{<t}=z)
\le JS_{i_t}(f_z).
\tag{2.4}
\]

Let

\[
p_t(z)=\operatorname{Inf}_{i_t}(f_z).
\]

The fresh strong-concavity theorem (0.2) applies to every Boolean descendant:

\[
JS_{i_t}(f_z)
\le \mathfrak j(\min\{p_t(z),1-p_t(z)\}).
\tag{2.5}
\]

The map

\[
p\mapsto \mathfrak j(\min\{p,1-p\})
\]

is concave on `[0,1]`: `min(p,1-p)` is concave, while `mathfrak j` is increasing and concave. Also influence is a martingale under unrelated uniform physical restrictions,

\[
\mathbb E_{Z_{<t}}p_t(Z_{<t})=p_{i_t}(f).
\tag{2.6}
\]

Therefore Jensen gives

\[
\mathbb E_{Z_{<t}}JS_{i_t}(f_{Z_{<t}})
\le \mathfrak j(q_{i_t}).
\tag{2.7}
\]

Sum (2.7) in (2.3) to obtain (2.1). Equation (2.2) is exactly the fresh scalar tangent/strong-concavity rebate (0.3), summed over the block. QED.

### Corollary 2.2 — exact erasure-preserving block payment

Combining (1.5) and Theorem 2.1,

\[
\boxed{
\Delta_AH
\le
B_A+\sum_{i\in A}\mathfrak j(q_i).
}
\tag{2.8}
\]

The erasure `B_A` is kept exact; only the coherent recombination term is bounded.

A useful killed shortcut is now explicit. Since conditional entropy gives

\[
B_A\ge\sum_{i\in A}B_i,
\]

and the surcharge in (2.8) is additive, a search for a *smaller upper-payment coefficient* using only the block envelope `B_A+sum_i mathfrak j(q_i)` cannot outperform the corresponding singleton envelope. Proper blocks are useful here for the **lower/critical structural constraints below**, not as a disguised replacement for the already-refuted every-coordinate upper-payment claim.

## 3. PROVED: every block of a restriction-critical descendant is erasure-heavy

Let `g` be a nonconstant physical restriction descendant maximizing

\[
R={H(g)\over I(g)}
\tag{3.1}
\]

among all nonconstant physical descendants of an original function. Every child of `g` has ratio at most `R`; constants have both entropy and influence zero.

For any block `A`, (1.6) and maximality give

\[
2^{-|A|}\sum_z H(g_{A=z})
\le
R\,2^{-|A|}\sum_z I(g_{A=z})
=R(I-I_A).
\]

Since `H(g)=RI`,

\[
\boxed{
\Delta_AH(g)\ge R I_A
\quad\text{for every physical block }A.
}
\tag{3.2}
\]

This is a lower criticality statement on one specially selected descendant. It is not the false statement that every prescribed coordinate of every Boolean function has a universal upper payment.

Let

\[
s_i:=\mathfrak j(q_i),\qquad S_A:=\sum_{i\in A}s_i,\qquad S:=\sum_i s_i.
\tag{3.3}
\]

Combining (3.2) with (2.8) proves the all-block floor

\[
\boxed{
B_A=H(X_A\mid X_{A^c})
\ge R I_A-S_A
\quad\text{for every }A.
}
\tag{3.4}
\]

Equivalently, putting `B=A^c` and using `H(X_A|X_B)=H-H(X_B)` and `H=RI`,

\[
\boxed{
H(X_B)\le R I_B+S_{B^c}
\quad\text{for every }B\subseteq[n].
}
\tag{3.5}
\]

Thus any local marginal entropy excess above the global slope `R` must be funded by the **recombination capacity of the complementary coordinates**:

\[
\boxed{
H(X_B)-R I_B\le S_{B^c}.
}
\tag{3.6}
\]

This is the new universal-facing implication: a hypothetical FEI counterexample may be localized to a physical descendant for which *every spectral marginal cut* obeys the complement-payment inequality (3.6), not merely the singleton lower floor from the earlier B14 report.

## 4. PROVED: fractional-Shearer/Han hierarchy for the critical core

The block statement yields a compact all-scales entropy-profile constraint.

Let `lambda_A>=0` be any finite family of weights on nonempty physical blocks such that every coordinate is covered exactly once:

\[
\sum_{A\ni i}\lambda_A=1
\quad\text{for every }i.
\tag{4.1}
\]

Put `L=sum_A lambda_A`. Sum the critical lower payment (3.2):

\[
\sum_A\lambda_A(B_A+JS_A)\ge H.
\tag{4.2}
\]

Since

\[
B_A=H-H(X_{A^c}),
\]

we get

\[
\boxed{
G_\lambda(X)
:=\sum_A\lambda_A H(X_{A^c})-(L-1)H(X)
\le\sum_A\lambda_A JS_A.
}
\tag{4.3}
\]

The complements form a fractional cover in which each coordinate is covered with total weight `L-1`; fractional Shearer therefore gives `G_lambda>=0`. Theorem 2.1 and the exact-cover condition (4.1) give

\[
\sum_A\lambda_A JS_A
\le
\sum_A\lambda_A\sum_{i\in A}s_i
=\sum_i s_i=S.
\]

Hence:

### Theorem 4.1 — fractional critical-Han cap

\[
\boxed{
0\le G_\lambda(X)\le S=\sum_i\mathfrak j(q_i)
\quad\text{for every exact fractional physical cover }\lambda.
}
\tag{4.4}
\]

This is independent of the chosen cover. All fractional complementary-entropy gaps of a restriction-critical spectrum must fit inside the same singleton recombination bank.

### Fixed-cardinality form

Let

\[
h_m:=\mathbb E_{|B|=m}H(X_B),\qquad 1\le m\le n-1.
\]

Choose all blocks `A` of size `n-m` with equal weight `1/binom(n-1,n-m-1)`. Then (4.4) becomes

\[
\boxed{
0\le h_m-{m\over n}H
\le {n-m\over n}S.
}
\tag{4.5}
\]

In the `K_m` normalization already used by the compatible B18 Han/KL projection work,

\[
K_m:={n\over m}\left(h_m-{m\over n}H\right),
\]

so

\[
\boxed{
0\le K_m\le {n-m\over m}S.
}
\tag{4.6}
\]

The endpoints recover two familiar dependence measures:

\[
\boxed{
\operatorname{DTC}(X)\le S,
}
\tag{4.7}
\]

because `n(h_{n-1}-(n-1)H/n)=DTC`, and

\[
\boxed{
\operatorname{TC}(X)\le(n-1)S,
}
\tag{4.8}
\]

from `m=1`.

Using the strong-concavity tangent bound (0.3),

\[
S\le {2\over\ln2}\sum_i\left(q_i-{q_i^2\over3}\right).
\tag{4.9}
\]

So (4.4)--(4.8) strictly improve the same deductions made with only the older linear `2q_i/ln2` surcharge whenever any `q_i>0`.

## 5. PROVED: high-ratio critical cores are automatically uncentered-low-marginal

The preceding B14 run introduced median-character centering to make the selector immune to deterministic parity padding. For the *restriction-critical hard core* at the current scale, the inherited concave restriction cap shows something stronger: no coordinate needs to be flipped at all.

The inherited sharp cap has

\[
\Delta_iH\le\Psi(q_i),
\qquad
\Psi(t)=h_2(t)+\mathfrak j(t).
\tag{5.1}
\]

If `p_i>=1/2`, then `q_i<=1/2`, `Psi(q_i)<=2`, and therefore

\[
{\Delta_iH\over p_i}\le4.
\]

Hence a restriction-critical descendant with `R>4` has

\[
\boxed{p_i<1/2\quad\text{for every relevant }i.}
\tag{5.2}
\]

Thus `q_i=p_i` and its coordinatewise median character is empty.

Let `tau(R)` be the inherited scalar threshold solving

\[
{\Psi(\tau)\over\tau}=R.
\tag{5.3}
\]

Criticality `Rp_i<=Delta_iH<=Psi(p_i)` then forces

\[
\boxed{p_i\le\tau(R)\quad\text{for every }i.}
\tag{5.4}
\]

At the current certified unrestricted lower-bound scale `C_0`, numerical bisection of the explicit one-variable equation gives

\[
\tau(C_0)=0.1740316570325050166647064\ldots.
\tag{5.5}
\]

Therefore any hypothetical ratio-`>C_0` counterexample has a restriction-critical descendant with **every** spectral marginal strictly below `0.1740316571`.

This explains why deterministic parity padding disappears after critical-descendant selection: a parity coordinate has marginal one and cannot survive in a hard core with ratio above four.

## 6. PROVED: coordinatewise refunded-selector suppression, not merely average shell suppression

On the same critical descendant, write

\[
t_i={\widehat g(\{i\})^2\over p_i}
\quad(p_i>0).
\tag{6.1}
\]

The previous B14 refunded-erasure lemma applies **coordinate by coordinate**, not only to the mass-weighted selected coordinate:

\[
B_i\le p_iF(t_i).
\tag{6.2}
\]

The fresh recombination bound gives

\[
JS_i\le\mathfrak j(p_i).
\tag{6.3}
\]

Criticality then yields

\[
R p_i\le\Delta_iH=B_i+JS_i
\le p_iF(t_i)+\mathfrak j(p_i).
\]

Hence

\[
\boxed{
F(t_i)\ge R- {\mathfrak j(p_i)\over p_i}
\quad\text{for every relevant }i.
}
\tag{6.4}
\]

Since `F` is decreasing, define `rho_R(p)` by

\[
F(\rho_R(p))=R-\frac{\mathfrak j(p)}p.
\tag{6.5}
\]

Then

\[
\boxed{t_i\le\rho_R(p_i)\quad\text{for every relevant coordinate}.}
\tag{6.6}
\]

As `p downarrow0`, `mathfrak j(p)/p -> 2/ln2`, so the old uniform cap is recovered in the rare-coordinate limit. But for every fixed positive marginal the exact recombination profile gives a strictly smaller ceiling.

At `R=C_0`, the old linear-surcharge cap was

\[
\rho_{\rm old}=0.3156061323581678\ldots.
\tag{6.7}
\]

At the largest marginal still allowed by (5.5), the exact profile gives

\[
\boxed{
\rho_{C_0}(\tau(C_0))
=0.2919391325401847\ldots,
}
\tag{6.8}
\]

an auxiliary purity-ceiling improvement of about `0.023667` at the critical marginal frontier. For smaller marginals the ceiling interpolates monotonically back toward (6.7).

Most importantly, (6.6) is **coordinatewise on the specially selected restriction-critical descendant**. The earlier centered-shell statement only asserted

\[
{\sum_i\widehat g(\{i\})^2\over I(g)}\le0.315606\ldots.
\]

Now every individual local purity ratio satisfies its own stronger profile-dependent bound. This does not resurrect the false universal every-coordinate upper-payment proposal: the statement is a necessary condition on the extremal descendant, and the coefficient depends on the coordinate's actual marginal.

## 7. Genuine before/after and remaining universal obligation

### Before this run

1. B14 had an exact singleton decomposition and an existential centered first-shell selector.
2. A high-ratio restriction-critical descendant was known to be singleton-erasure-heavy.
3. The best B14 shell consequence at the current scale was an **average** centered first-shell fraction `<0.3156061324`.
4. fleet04/B14 had a sharper **singleton** recombination profile `JS_i<=mathfrak j(q_i)`, but it had not been propagated through an arbitrary physical restriction block.

### After this run

1. The exact recombination surcharge tensorizes to **every block**: `JS_A<=sum_{i in A} mathfrak j(q_i)`.
2. Every block of a restriction-critical descendant obeys the erasure floor `B_A>=R I_A-S_A` and every complementary marginal obeys `H(X_B)<=R I_B+S_{B^c}`.
3. Every exact fractional physical cover satisfies the same cover-independent Han/Shearer cap `0<=G_lambda<=S`; equivalently the whole fixed-cardinality entropy profile obeys (4.5), with `DTC<=S` as one endpoint.
4. At the current unrestricted lower-bound scale every critical-core marginal is `<0.1740316571`, so the median-character gauge is automatically trivial there.
5. The refunded singleton purity obstruction is now **coordinatewise**. At the largest allowed marginal its explicit ceiling improves from `0.3156061324` to `0.2919391326` using the fresh exact recombination profile.

### Remaining universal obligation

Full FEI remains open. A counterexample above `C_0` is now localized to a Boolean restriction-critical spectral law that simultaneously has:

- all marginals below `0.1740316571`;
- the block erasure floor (3.4) for **every** physical block;
- the complement-funded marginal entropy inequality (3.6) for **every** spectral subset;
- the full fractional-Han cap (4.4) for **every** exact fractional cover;
- the coordinatewise singleton-purity suppression (6.6);
- and, from the compatible B13/B18 work, the genuine Boolean phase/autocorrelation constraints and phase/Hellinger packing laws.

The next B14 target should not return to larger-block *upper* erasure search: Corollary 2.2 shows that the natural additive block envelope cannot beat the singleton envelope. The useful next move is instead to combine the new **all-block lower erasure floor** with Boolean phase/Palm constraints to show that some fractional cover must have a Han gap exceeding the available recombination bank `S`, or equivalently find a complement `B^c` whose `S`-budget cannot fund the marginal excess in (3.6).

## 8. Failed/retired routes preserved

- The stronger claim that every prescribed coordinate of every Boolean function has a universal upper restriction-entropy payment remains false and is not used.
- Bare proper-block erasure search cannot improve the singleton erasure coefficient; the additive recombination envelope does not repair that collapse.
- Deterministic parity padding can kill uncentered singleton mass for a general state, but it cannot survive inside a ratio-`>4` restriction-critical core by (5.2).
- Finite checks or the numerical roots (5.5), (6.8) do not prove FEI. The theorems above are analytic; the decimals merely calibrate their current lower-bound-scale consequences.

## 9. Literature/status check

Current primary/status sources checked during this run still describe full FEI as open. González–MacManus–Pereyra (arXiv:2606.00246, 29 May 2026) use the physical restriction-decrement/stopping-tree framework and explicitly note that a suitable coordinate decrement inequality would imply FEI. Potapov (arXiv:2609.21563, 18 Sep 2026) proves FEI for plateaued and partially bent classes, not universally. Han's published bound and the later Li–Han information-theoretic strengthening control Fourier entropy by influence plus a marginal-log term; they do not by themselves supply the critical all-block selector required here. The current optimization-problem ledger still records the conjecture as open and the certified `>6.521845710923046575` lower bound.

A bounded search did not locate the exact block-JS tensorization/fractional-critical-Han statements above. That is **not** evidence of novelty; publication priority remains UNVERIFIED.
