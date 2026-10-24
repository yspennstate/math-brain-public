# B12 — an explicit common bias tube for every five-input composition-prime gate

**Classification:** `ESSENTIAL_STEP_APPLIED / EXPLICIT_ARITY5_PRIME_TUBE / FULL_FEI_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source-bound mathematical artifacts were used directly; no native mathematical-brain receiver/context entered the derivation.  
**Publication priority:** unverified; no novelty claim.

## 0. Live target and exact before/after

The later owner control keeps the FEI fleet on the source-exact all-gate formulation. For a Boolean gate `G` under product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
  [\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The fixed live candidate is

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\qquad
a^\dagger=0.268204856,
\tag{0.2}
\]

where `Gamma_0` is the committed h96 read-once potential. The composition cocycle reduces this candidate to composition-prime gates. Thus the universal unpaid implication remains

\[
D_{\Gamma^\dagger}(P;p)\ge0
\quad\text{for every finite composition-prime Boolean gate }P
\text{ and every }p\in(0,1)^k.
\tag{0.3}
\]

This report does **not** claim (0.3). It makes one finite-arity part quantitative.

### Before this run

The completed other-account report

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T065506Z-prime-central-orbits/REPORT.md`

(report blob `bdbc1c2378da80c6a7d1b1dbb02ceafa2496cc96`) combines the account01/B17 exact five-bit certificate with an independent cube-automorphism orbit enumeration. It proves that every essential composition-prime five-input gate `P` has the uniform-bias reserve

\[
\boxed{
D_{\Gamma^\dagger}(P;1/2,\ldots,1/2)
\ge \delta_5:=0.004906502214.
}
\tag{0.4}
\]

It then obtains only an **existential** common radius `epsilon_5>0` by finite-family continuity. Its explicit replacement obligation is to produce a source-certified numerical radius or an off-center prime falsifier.

The exact finite source underlying (0.4) is account01/B17

`proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T043923Z-arity5-uniform-c001/REPORT.md`

(report blob `daca0767157595c2c2ac7d9da4a58fe86132ffe4`). It certifies all five-bit truth tables at the center and a smallest strict non-equality objective gap `0.004906502214`; account03/B18 proves every central equality case is decomposable, hence the strict gap applies to every essential prime.

### New theorem

Let

\[
\varepsilon:=2^{-18}={1\over262144}.
\tag{0.5}
\]

Then every essential composition-prime five-input Boolean gate `P` satisfies

\[
\boxed{
\max_i|p_i-1/2|\le2^{-18}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(P;p)>2.9\times10^{-4}>0.
}
\tag{0.6}
\]

Thus the previously qualitative common prime tube now has the explicit source-certified radius

\[
\boxed{\varepsilon_5\ge2^{-18}.}
\tag{0.7}
\]

No off-center truth-table enumeration is used. The proof transports the **actual signed biased Fourier coefficient vector of one Boolean source** from the center, then pays the resulting Shannon change. This is not an arbitrary-row relaxation.

## 1. Exact biased-Fourier transport from one Boolean source

Fix one Boolean gate `P:{0,1}^5->{-1,1}` and product bias `p`. Put

\[
\sigma_j=\sqrt{p_j(1-p_j)},
\qquad
\phi_j(x_j)={x_j-p_j\over\sigma_j},
\qquad
\phi_S=\prod_{j\in S}\phi_j,
\]

and write the actual biased Fourier coefficients

\[
a_S(p)=\mathbb E_p[P(X)\phi_S(X)].
\]

Parseval gives `sum_S a_S(p)^2=1`. The squared coefficients

\[
w_S(p)=a_S(p)^2
\tag{1.1}
\]

are therefore the actual 32-atom biased spectral law whose Shannon entropy is `Htilde_P(p)`.

### Lemma 1.1 — exact coefficient derivatives

For every coordinate `j`, at every interior bias,

\[
\boxed{
\partial_{p_j}a_S=
\begin{cases}
 a_{S\cup\{j\}}/\sigma_j,&j\notin S,\\[2mm]
 {1-2p_j\over2p_j(1-p_j)}a_S,&j\in S.
\end{cases}}
\tag{1.2}
\]

**Proof.** If `j notin S`, condition on all variables except `j`. Differentiating the Bernoulli expectation gives the conditional difference `P(1)-P(0)`, while the coefficient with `j` adjoined is exactly `sigma_j` times that conditional difference. If `j in S`, write `S=T union {j}`. Then

\[
a_S=\sigma_j\,\mathbb E_{p_{-j}}[(P(1,X_{-j})-P(0,X_{-j}))\phi_T],
\]

so only `sigma_j` depends on `p_j`, yielding the second line. No absolute-value or sign-free replacement is made. `square`

Pairing `S` not containing `j` with `S union {j}` gives

\[
\|\partial_{p_j}a\|_2^2
=\left({1\over\sigma_j^2}
+{(1-2p_j)^2\over4\sigma_j^4}\right)
\sum_{S\ni j}a_S^2.
\tag{1.3}
\]

On the cube `|p_j-1/2|<=epsilon`, the exact endpoint calculation in the checker gives the coefficient in parentheses below `9`; hence

\[
\boxed{\|\partial_{p_j}a\|_2<3.}
\tag{1.4}
\]

Move from the center `p^0=(1/2)^5` to `p` one coordinate at a time. Integrating (1.4),

\[
\boxed{
\|a(p)-a(p^0)\|_2
\le3\sum_{j=1}^5|p_j-1/2|
\le15\varepsilon.
}
\tag{1.5}
\]

Since both coefficient vectors have Euclidean norm one,

\[
\begin{aligned}
\|w(p)-w(p^0)\|_1
&=\sum_S|a_S(p)^2-a_S(p^0)^2|\\
&\le\|a(p)-a(p^0)\|_2\|a(p)+a(p^0)\|_2\\
&\le30\varepsilon.
\end{aligned}
\tag{1.6}
\]

Thus the total-variation distance between the two **actual Boolean spectral laws** is at most

\[
\boxed{\delta_{\rm TV}\le15\varepsilon.}
\tag{1.7}
\]

This is the marked-spectrum estimate used below. Its crucial input is the common signed coefficient vector `a(p)` belonging to one Boolean gate; arbitrary rows need not satisfy (1.2).

## 2. Spectral Shannon debit

Fannes--Audenaert on the 32-point alphabet gives

\[
|\widetilde H_P(p)-\widetilde H_P(p^0)|
\le h_2(\delta_{\rm TV})+\delta_{\rm TV}\log_2 31.
\tag{2.1}
\]

For `0<x<1`,

\[
h_2(x)\le x\log_2(e/x).
\]

With `delta_TV<=15 epsilon`, `e<3`, and the exact integer check

\[
{31e\over15\varepsilon}<2^{21},
\]

we obtain

\[
\boxed{
|\widetilde H_P(p)-\widetilde H_P(p^0)|<315\varepsilon.
}
\tag{2.2}
\]

Unlike the retired depth-only routes, this payment controls the full 32-atom entropy of the source-valid marked spectrum.

## 3. Input influence-price transport

Under the gate normalization in (0.1),

\[
q_i(p):={\operatorname{It}_i(P;p)\over V_{p_i}}
\tag{3.1}
\]

is exactly the pivotal probability of input `i`, evaluated under the product law of the other four inputs. Therefore `0<=q_i<=1`. Coupling each Bernoulli coordinate optimally gives

\[
\boxed{
|q_i(p)-q_i(p^0)|
\le\operatorname{TV}(\mu_{p_{-i}},\mu_{(1/2)^4})
\le\sum_{j\ne i}|p_j-1/2|
\le4\varepsilon.
}
\tag{3.2}
\]

Set

\[
B(u)=\Gamma^\dagger(u)+h_2(V_u).
\]

At the center, `B(1/2)=C^dagger<7`. The committed source envelope, already used in the current MUX work, gives a valid center Lipschitz bound

\[
|\Gamma^\dagger(u)-C^\dagger|<66|u-1/2|
\tag{3.3}
\]

through this tiny interval. Also

\[
h_2(V_{1/2+x})=h_2(4x^2),
\]

so with `|x|<=epsilon`,

\[
|B(1/2+x)-C^\dagger|
<66\varepsilon+h_2(2^{-34}).
\tag{3.4}
\]

Using (3.2)--(3.4), for each input

\[
|q_i(p)B(p_i)-q_i(p^0)C^\dagger|
<94\varepsilon+h_2(2^{-34}).
\tag{3.5}
\]

Summing the five coordinates,

\[
\boxed{
\left|
\sum_i q_i(p)B(p_i)-C^\dagger\sum_iq_i(p^0)
\right|
<470\varepsilon+5h_2(2^{-34}).
}
\tag{3.6}
\]

All coordinate prices are retained; no pivotal coordinate is discarded.

## 4. Output-potential transport

Let `r(p)=Pr_p[P=-1]`. At the center, a nonconstant five-bit gate has

\[
r(p^0)={m\over32},\qquad 1\le m\le31.
\]

Again by product coupling,

\[
|r(p)-r(p^0)|\le5\varepsilon.
\tag{4.1}
\]

Hence the symmetric representative of every point between the two output biases exceeds

\[
{1\over32}-5\varepsilon>{1\over64}.
\tag{4.2}
\]

For `z<=1/2`, the h96 source representation is

\[
\Gamma_0(z)=zG(\log_2(1/z)),
\qquad
G(x)<4.9096x+8.629,
\qquad |G'(x)|<31.
\tag{4.3}
\]

The candidate is nonnegative, so `G>=0` on the represented source range. With `z>=1/64`, `x<=6`, `1/ln2<3/2`, and `a^dagger<0.269`, every interpolation segment satisfies

\[
|({\Gamma^\dagger})'(z)|
<4.9096\cdot6+8.629+{93\over2}+0.269
=84.8556<85.
\tag{4.4}
\]

Continuity transfers the same Lipschitz bound across source breakpoints and symmetry gives the upper half. Therefore

\[
\boxed{
|\Gamma^\dagger(r(p))-\Gamma^\dagger(r(p^0))|
<425\varepsilon.
}
\tag{4.5}
\]

## 5. Combine the three nonreused debits

Equations (2.2), (3.6), and (4.5) concern disjoint terms of the exact gate slack (0.1), so

\[
|D_{\Gamma^\dagger}(P;p)-D_{\Gamma^\dagger}(P;p^0)|
<1210\varepsilon+5h_2(2^{-34}).
\tag{5.1}
\]

Using

\[
h_2(x)\le x\log_2(e/x),\qquad \log_2e<2,
\]

we have

\[
h_2(2^{-34})<36\,2^{-34}.
\]

Thus the exact rational debit used by the checker is

\[
\boxed{
1210\,2^{-18}+180\,2^{-34}
=0.004615794168785214\ldots .
}
\tag{5.2}
\]

Subtract this from the inherited central prime reserve (0.4):

\[
\begin{aligned}
D_{\Gamma^\dagger}(P;p)
&>0.004906502214
 -0.004615794168785214\ldots\\
&={304829479219139\over1048576000000000000}\\
&=0.0002907080452147855\ldots\\
&>{29\over100000}.
\end{aligned}
\tag{5.3}
\]

This proves (0.6).

## 6. Owner-comparable gate margin

The owner requests the base-potential margin rather than raw `D` when comparing gates. Put

\[
M_P(p)={I(P;p)\over4}-r(p)(1-r(p))\ge0.
\tag{6.1}
\]

The quadratic-lift identity is exact:

\[
D_{\Gamma^\dagger}=D_{\Gamma_0}+a^\dagger M_P.
\tag{6.2}
\]

When `M_P>0`, the requested margin is

\[
c_P(p)=-{D_{\Gamma_0}(P;p)\over M_P(p)}
=a^\dagger-{D_{\Gamma^\dagger}(P;p)\over M_P(p)}.
\tag{6.3}
\]

Since each biased influence is at most one, `I(P;p)<=5`, hence `M_P<=5/4`. From (5.3), throughout the tube,

\[
\boxed{
c_P(p)<0.268204856-{4\over5}(0.00029)=0.267972856.}
\tag{6.4}
\]

If `M_P=0`, the quotient is undefined, but (5.3) already supplies strict positive gate slack. The margin estimate is intentionally conservative; the substantive result is the explicit common radius.

## 7. Last-three comparison and honest change fields

The last three **completed substantive** account02/B12 reports before this run were:

1. `20260922T055114Z-zero-credit-mux-collar/REPORT.md`: a source-exact whole-spectrum continuity collar around MUX zero-credit lines;
2. `20260922T045519Z-complementary-mux-fourstep/REPORT.md`: a four-generation descendant-AND bootstrap for the complementary-data MUX line;
3. `20260922T035404Z-balanced-bent-local-obstruction/REPORT.md`: a genuine Boolean bent/two-point selector obstruction to finite pointwise-local restriction payment.

A later operational start record at `20260922T065354Z-fei-gate` had no completed scientific report at this run's fresh read, so it is not counted as substantive predecessor evidence.

**FULL-PROBLEM CHANGE:** **none.** The universal all-arity/all-bias prime-gate implication (0.3), hence full FEI, remains open. This theorem closes only an explicit neighborhood for arity-five primes.

**MECHANISM CHANGE:** **yes.** The previous completed B12 work was MUX-specific (six-atom continuity or descendant AND recursion). This run uses a gate-uniform differential transport identity for the full signed biased Fourier vector of an arbitrary single Boolean source, Parseval to convert it to spectral total variation, and then a nonreused three-part slack budget. It directly executes account03/B18's explicit-radius replacement obligation.

**Quantified remaining implication:** prove `D_{Gamma^dagger}(P;p)>=0` for five-input primes outside the `2^-18` center tube and for every prime of arity at least six, or produce a genuine Boolean falsifier; only then can the composition cocycle/all-gate equivalence close FEI for this candidate.

## 8. Verification and scope

`check_explicit_prime_tube.py` is a standard-library exact-rational checker for every numerical inequality used after the analytic lemmas. It verifies the coefficient-transport endpoint bound, source derivative bound, output-source window, Fannes logarithm simplification, total transport debit, positive residual reserve, and margin translation. Captured output is in `check_output.txt`; it reports `PASS`.

The checker is a sanity check for the arithmetic. The mathematical theorem rests on the proved derivative identities, product coupling, Fannes--Audenaert, the source h96 envelope, and the inherited rigorous central prime reserve. A finite check is not promoted to full FEI.

Scoped privacy/secret review: changed files contain only FEI mathematics, repository-relative source identifiers, nonsecret hashes, and deterministic arithmetic. They contain no credentials, scheduler identifiers, machine paths, raw transcripts, unrelated private material, benchmark gold, email/Drive actions, public-posting actions, paid/remote model calls, workflows, or permission changes.
