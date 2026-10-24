# B12 FEI — a Boolean selector refutes the stop-conditioned TC remainder; hierarchical component conditioning repairs the mechanism

**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. No authenticated brain retrieval or receiver-context use occurred.  
**Route:** spectral-sample compression / martingale coding with exact nonreuse at the joint B/C interface.  
**Mechanism change:** **YES.** The previous B12 run removed common stopping-time dependence by conditioning on `T=|P|`. This run attacks the remaining proposed universal remainder itself and finds a genuine Boolean counterfamily. The replacement exposes a hierarchical component label once before bitwise tensorization.

## 0. Control and named peer result consumed

Fresh owner control and the required FEI files were read before this work, including `TASKS_2026-09-21.md`, then the read-once `REPORT.md`, then `APPROACHES.md`, followed by the joint `ORDER.md` and `RESEARCH_STATE.md`. The live natural-language seven-FEI and joint orders govern this slot. No later account03/B12 pause or stop was observed.

`consumed_peer_artifact`:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260921T212331Z-factorial-trigger-address/REPORT.md`.

The peer proves the exact factorial Palm partition

\[
\mathbb E\log_2(K!)
=\sum_i j_i\,\mathbb E_{\nu_i}\frac{\log_2((1+|B|)!)}{1+|B|},
\tag{0.1}
\]

and, for robust reciprocal trigger components, converts the factorial rebate into a nonreusing logarithmic address payment. Its Corollary 4.2 inserts that payment into B12's previous corrected remainder

\[
R_T:=I\,\operatorname{TC}(P\mid T)-\mathbb E\log_2(K!).
\tag{0.2}
\]

`applied_to_claim`: determine whether (0.2), after the stopping-time correction, is itself universally `O(I)` for Boolean Fourier spectra, and whether the factorial-address payment can by itself make that implication true.

The answer is **NO**. A two-branch Boolean selector produces a component-mixture total-correlation debt of order `m^2`, while the entire factorial bank is only order `m log m`. This identifies a second common-cause variable that must be exposed once rather than tensorized across coordinates.

## 1. Exact universal statement attempted

The previous B12 run left open the statement

> **Candidate `R_T` bound.** There exists a finite universal constant `C` such that for every Boolean function `f`, under the uniform-prefix edge law of its spectral sample,
> \[
> R_T(f)=I(f)\operatorname{TC}(P\mid T)-\mathbb E\log_2(K!)\le C I(f).
> \tag{1.1}
> \]

This would have paid the dependence remainder in the repaired sequential code after the stopping-time artefact had been removed.

**Result of this run:** (1.1) is **REFUTED for every finite `C` by an explicit Boolean family**.

This is not a counterexample to FEI. The counterfamily below has spectral entropy exactly `2` bits.

## 2. The Boolean selector-of-parities family

Fix `m>=2`. Let `A={x_1,...,x_m}` and `B={y_1,...,y_m}` be disjoint coordinate blocks and let `z` be one additional Boolean coordinate, all in `{+1,-1}`. Put

\[
a(x)=\prod_{i=1}^m x_i,\qquad b(y)=\prod_{i=1}^m y_i,
\]

and define the Boolean selector

\[
f_m(z,x,y)=\frac{1+z}{2}a(x)+\frac{1-z}{2}b(y).
\tag{2.1}
\]

Thus `f_m=a` on the `z=+1` half-cube and `f_m=b` on the `z=-1` half-cube.

Expanding (2.1),

\[
f_m=\frac12 a+\frac12 b+\frac12 za-\frac12 zb.
\]

Therefore its only nonzero Fourier coefficients are

\[
\widehat f_m(A)=\widehat f_m(B)=\widehat f_m(A\cup\{z\})=\frac12,
\qquad
\widehat f_m(B\cup\{z\})=-\frac12.
\tag{2.2}
\]

Hence the spectral sample `S` is exactly uniform on four sets:

\[
A,\quad B,\quad A\cup\{z\},\quad B\cup\{z\}.
\tag{2.3}
\]

Consequently

\[
H(S)=2,\qquad
\Pr(K=m)=\Pr(K=m+1)=\frac12,\qquad
I=\mathbb EK=m+\frac12.
\tag{2.4}
\]

So this family satisfies FEI with enormous slack. It is used only to test the proposed compression remainder.

## 3. Uniform-prefix law and exact conditional total correlation

Use the inherited uniform-prefix edge law: terminal sets are size-biased by `K`, a uniformly random insertion edge is chosen, `P` is the unordered predecessor prefix, `L` the inserted label, and `T=|P|`. For every terminal-size law,

\[
\Pr(T=t)=\frac{\Pr(K>t)}I.
\tag{3.1}
\]

For (2.4),

\[
\Pr(T=t)=\frac1I\quad(0\le t\le m-1),
\qquad
\Pr(T=m)=\frac1{2I}.
\tag{3.2}
\]

For `2<=t<=m-1`, conditioning on `T=t` makes the four terminal sets in (2.3) equiprobable. Every coordinate in `A` or `B` therefore has prefix occupancy

\[
q_t=\frac t4\left(\frac1m+\frac1{m+1}\right),
\tag{3.3}
\]

while

\[
r_t:=\Pr(z\in P\mid T=t)=\frac{t}{2(m+1)}.
\tag{3.4}
\]

When `z` is absent, the branch `A/B` is visible from a nonempty prefix and the prefix is uniform over `2 binom(m,t)` possibilities. When `z` is present and `t>=2`, the branch is again visible and the prefix is uniform over `2 binom(m,t-1)` possibilities. Hence

\[
H(P\mid T=t)
=h_2(r_t)
+(1-r_t)\log_2\!\left(2\binom mt\right)
+r_t\log_2\!\left(2\binom m{t-1}\right),
\tag{3.5}
\]

and therefore

\[
\operatorname{TC}(P\mid T=t)
=2m h_2(q_t)+h_2(r_t)-H(P\mid T=t).
\tag{3.6}
\]

The cases `t=0,1,m` have elementary one-line formulas and affect only lower-order terms.

Let `x=t/m` stay in a compact subinterval of `(0,1)`. Stirling's formula in (3.5) gives

\[
\frac1m\operatorname{TC}(P\mid T=t)
\longrightarrow
2h_2(x/2)-h_2(x).
\tag{3.7}
\]

The summands are uniformly bounded by `O(m)` and the endpoint ranges are harmless, so (3.2) and the Riemann-sum limit yield

\[
\begin{aligned}
\frac1m\operatorname{TC}(P\mid T)
&\longrightarrow
\int_0^1\bigl(2h_2(x/2)-h_2(x)\bigr)\,dx\\
&=4\int_0^{1/2}h_2(u)\,du-\int_0^1h_2(x)\,dx\\
&=\frac1{2\ln2}
=0.7213475204444817\ldots .
\end{aligned}
\tag{3.8}
\]

The last equality uses symmetry of binary entropy and
`int_0^1 h_2(x) dx=1/(2 ln 2)`.

Meanwhile

\[
\mathbb E\log_2(K!)
=\frac12\log_2(m!)+\frac12\log_2((m+1)!)
=O(m\log m).
\tag{3.9}
\]

Combining (2.4), (3.8), and (3.9),

\[
\boxed{
\frac{R_T(f_m)}{m^2}\longrightarrow\frac1{2\ln2}>0,
}
\tag{3.10}
\]

so in particular

\[
\boxed{
\frac{R_T(f_m)}{I(f_m)}\longrightarrow\infty.
}
\tag{3.11}
\]

This rigorously refutes (1.1) for every finite universal constant.

## 4. What the peer factorial theorem does and does not pay

The account04/B12 factorial theorem is exact and remains valid. Equation (0.1) shows that the **entire** available factorial rebate in this family is the quantity (3.9), only `Theta(m log m)`. But the stop-conditioned tensorization debt `I TC(P|T)` is `Theta(m^2)` by (3.8).

Therefore no argument that only redistributes the existing factorial bank among row/trigger addresses can universally dominate the whole stop-conditioned total correlation. The missing debt is not an address inside one robust component; it is the repeated rediscovery of the **same branch/component bit** across many coordinate indicators.

This is the concrete implication obtained from the named peer result: its nonreuse principle is correct, but it must be applied one level higher, before coordinatewise tensorization across distinct spectral components.

## 5. PROVED exact replacement: arbitrary component side information

The obstruction suggests exposing a component label once. This admits an exact universal identity.

Let `C` be any finite side variable coupled to the prefix edge law. Since `T` is a deterministic function of `P`, the same entropy algebra as in the previous B12 theorem gives

\[
\boxed{
I_2(L;P\mid C)+\operatorname{TC}(P\mid T,C)
=
I_2(L;T\mid C)
+\sum_k I_2(L;Y_k\mid T,C)
+\operatorname{TC}(P\mid L,T,C),
}
\tag{5.1}
\]

where `Y_k=1_{k in P}` and every information quantity is in bits.

### Proof

Conditioning throughout on `(T,C)`,

\[
\sum_k I_2(L;Y_k\mid T,C)-I_2(L;P\mid T,C)
=\operatorname{TC}(P\mid T,C)-\operatorname{TC}(P\mid L,T,C).
\]

Also, because `T` is determined by `P`,

\[
I_2(L;P\mid C)=I_2(L;T\mid C)+I_2(L;P\mid T,C).
\]

Substitution proves (5.1). QED.

If `C=C(S)` is a deterministic terminal-component label, then at the outer coding level

\[
H(S)=H(C)+H(S\mid C),
\tag{5.2}
\]

so the component is paid **once**, through `H(C)`, rather than once for every prefix coordinate. Applying the prefix code separately inside each conditional law `Law(S|C=c)` is therefore a genuine hierarchical nonreuse code, not an informal bookkeeping change.

Equation (5.1) is universal for random subset laws. It is not FEI closure: one still needs a Boolean-structural rule choosing useful components with a uniformly paid outer entropy and compatible physical flags.

## 6. The same Boolean family validates the repair mechanism

For the selector family, let

\[
C=\begin{cases}
A,&S\in\{A,A\cup\{z\}\},\\
B,&S\in\{B,B\cup\{z\}\}.
\end{cases}
\tag{6.1}
\]

Then `C` is a deterministic function of the terminal spectral set and

\[
H(C)=1.
\tag{6.2}
\]

For `1<=t<m`, conditioned on `(T=t,C)`, every block coordinate has marginal

\[
q'_t=\frac t2\left(\frac1m+\frac1{m+1}\right),
\tag{6.3}
\]

and `z` still has marginal `r_t` from (3.4). The exact prefix entropy is

\[
H(P\mid T=t,C)
=h_2(r_t)
+(1-r_t)\log_2\binom mt
+r_t\log_2\binom m{t-1}.
\tag{6.4}
\]

Thus

\[
\operatorname{TC}(P\mid T=t,C)
=m h_2(q'_t)+h_2(r_t)-H(P\mid T=t,C).
\tag{6.5}
\]

The method-of-types bound

\[
m h_2(k/m)-\log_2(m+1)\le\log_2\binom mk\le m h_2(k/m)
\]

and the fact that `q'_t` is the convex combination

\[
q'_t=(1-r_t)\frac tm+r_t\frac{t-1}m
\]

show uniformly that

\[
\operatorname{TC}(P\mid T=t,C)=O(\log m).
\tag{6.6}
\]

For example one may use the binary-entropy continuity estimate over a displacement `1/m` to obtain an explicit `O(log m)` bound. The endpoint `t=m` is also `O(1)`. Hence

\[
\boxed{
\operatorname{TC}(P\mid T,C)=O(\log m),
}
\tag{6.7}
\]

whereas (3.8) gives `TC(P|T)=Theta(m)`. A **single one-bit component label** removes the linear total-correlation inflation.

This is the exact phenomenon the next B/C compiler must reproduce structurally: discover the cluster/component once, then use local flags conditionally inside it.

## 7. Executed numerical stress test

A standard-library evaluator for the exact finite formulas above was executed in this invocation. Representative values are:

| m | I | TC(P\|T) | TC(P\|T,C) | R_T/I | component-conditioned R/I | R_T/m^2 |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10.5 | 7.057108908754 | 1.659367252323 | 4.817034915989 | -0.580706740443 | 0.505788666179 |
| 20 | 20.5 | 14.635787463384 | 2.115888962598 | 11.549273188638 | -0.970625312148 | 0.591900250918 |
| 50 | 50.5 | 36.845637632542 | 2.741462719780 | 32.547729697203 | -1.556445215559 | 0.657464139884 |
| 100 | 100.5 | 73.379020449088 | 3.226165495177 | 68.124352797034 | -2.028502156877 | 0.684649745610 |
| 200 | 200.5 | 145.995420147220 | 3.717043460422 | 139.764966117770 | -2.513410569028 | 0.700571892665 |
| 500 | 500.5 | 363.048751412945 | 4.371545454399 | 355.512611880598 | -3.164594077947 | 0.711736248985 |
| 1000 | 1000.5 | 724.218240676058 | 4.869037931974 | 715.688124117004 | -3.661078627081 | 0.716045968179 |
| 2000 | 2000.5 | 1446.063499143331 | 5.367637673295 | 1436.536645636412 | -4.159215833624 | 0.718447889899 |

The last column converges toward `1/(2 ln 2)=0.721347520444...`, as proved in (3.10). The executable upload was separately blocked by platform safety and was **not retried or routed around**; the analytic proof above does not depend on that upload.

## 8. Claim ledger

- **REFUTED:** universal `R_T(f)<=C I(f)` for any finite `C`, even after conditioning on prefix size `T`, via the explicit Boolean selector-of-parities family.
- **PROVED:** the exact side-information tensorization identity (5.1) for every prefix random-set law.
- **PROVED:** in the selector family, one deterministic one-bit terminal component label reduces `TC(P|T)` from `Theta(m)` to `O(log m)`.
- **PRESERVED:** account04/B12's exact factorial Palm partition and robust trigger-address payment. This run shows only that those payments cannot, by themselves, pay a component-mixture debt larger than the entire factorial bank.
- **OPEN:** a universal Boolean rule producing a hierarchy of components/flags whose outer component entropy is paid once and whose conditional residuals telescope against influence/factorial/physical credits.
- **OPEN / NOT PROVED:** full uniform-cube FEI.

## 9. Next attack and joint handoff

`remaining_implication`:

> Construct, from the actual mixed-curvature / robust-trigger graph, a measurable hierarchical component label `C=C(S)` such that (i) its outer entropy is paid once by an existing influence/factorial/physical credit, (ii) the level-conditioned signed flags operate inside each component without reuse, and (iii) recursively unresolved exceptional mass strictly decreases under a paid potential.

The most concrete next attempt is to use reciprocal robust trigger components as the first hierarchy level. Account04/B12 already proves their logarithmic trigger addresses are factorial-paid. B12 should now ask whether the **component identity itself**, not every coordinate address, can be encoded by the same partition before applying (5.1) inside each component. The selector family above is the mandatory stress test: a valid theorem must reveal its `A/B` branch once and must not rediscover that bit across `Theta(m)` prefix coordinates.

`next_recipient`: account04/B12 (factorial trigger components) and account03/B18 (joint C-interface integration), with account02/B16/B18 as the authentic signed-parent/flag compiler partners.

`full_problem_change`: full FEI remains OPEN; one previously open universal remainder implication is now rigorously false and replaced by a hierarchical exact-nonreuse identity.

`mechanism_change`: stop-time-only conditioning -> terminal-component hierarchical conditioning.
