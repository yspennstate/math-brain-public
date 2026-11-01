Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — 2026-09-18T08:29:28Z

## 1. Status and metric

Assignment remains **P0456**, Dabirian--Subramanian, *Connectivity of a family of bilateral preference random graphs*, J. Applied Probability 63(2) (June 2026), Section 1.1.

The source-scale metric remains saturated: `c_LK^cert=0`. Recoveries remain `0/2`.

After the fresh source/repository check below I formally admit the finer fleet proof-frontier metric requested by the preceding run. Put

\[
W_n=\sqrt{\log n\,\log\log n}.
\]

Let `a_LK^fine=max(a_-,a_+)`, where `a_-` and `a_+` are the best fixed-coefficient frontiers currently certified by this proof package for disconnection and connection at scale `W_n`. This is a **fleet proof metric**, not a constant asserted by the source and not a claim that the true threshold has such a coefficient.

Claim 278 gives the supported admitted baseline

\[
a_-\le\sqrt3,\qquad a_+\le\sqrt{23},\qquad a_{LK}^{fine}=\sqrt{23}.
\]

This run proves

\[
a_-\le1,\qquad a_+\le\sqrt{11},
\]

so

\[
\boxed{a_{LK}^{fine}:\sqrt{23}\to\sqrt{11}}.
\]

This is genuine movement; fine-window unchanged count is `0`.

Main claim:

`P03-P0456-JOINT-RACE-FINE-BRACKET-280 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

For every fixed `a<-1`, `k<=log n+aW_n` implies disconnection whp. For every fixed `a>sqrt(11)`, `k>=log n+aW_n` implies connectivity whp. The unresolved certified band is `[-1,sqrt(11)]`; coefficient zero and a limiting law remain open.

## 2. Continuity and source status

Continued from `proofnet24/P03-fei/runs/2026-09-18/2026-09-18T07-43-40Z__p0456-exact-marking-fine-window.md` (creation `1640dc7049fdc9a39cafe9c858c3257bc09e6c9d`, blob `3e811c13270e2bee235e2b8c6c1f8eeb06ca4a72`) and preserved Claims 274, 276, 278.

This invocation recovered/read the root README, hourly protocol, FLEET_RULES, current OWNER_DIRECTIVE, `operations/FLEET_2026-09-16.md`, campaign INDEX/RANKING, POSTED, canonical `operations/claims/P0456.md`, P0456 history/intake references and newest accessible P04/I0101 report. Large connector surfaces can be truncated, so I do not claim byte-for-byte reread of every large ledger.

The canonical P0456 claim still names P03 as exclusive HARD OUTSIDE owner. Fresh 2026-09-18 web searches recovered the current Cambridge primary article (DOI `10.1017/jpr.2025.10051`, online 18 Dec 2025; journal 63(2), June 2026, pp. 552--579) and no later source-matching closure. Section 1.1 still records the `+/-1/2` band at the coarser `sqrt(log n) log log n` scale as unknown and calls for sharper sufficient conditions. A bounded search miss is not proof of worldwide openness or publication novelty.

## 3. New methods

Used **B12 FIND WHAT IS CONSERVED, B19 MAKE IT AN ALGORITHM, B7 TAKE THE LIMIT**.

The previous bad-pair estimate retained only a scalar type-0 occupancy. Actual joint isolation preserves a vector: each preferred neighbor has its own type-0 deadline and its rejection type must accumulate enough earlier symbols. I first give an exact finite gap-count formula/dynamic program, then pass to a common-deadline Gamma race. On the positive side I attack component sizes 7--12 directly, instead of converting all sizes <=12 to `deg<=11`.

## 4. Exact joint rank-profile reduction (B19)

Under one source bad-side conditioning, fix the relevant top-`s` neighbor set. The source leaves a uniformly interleaved type word consisting of one ordered type-0 list and `q=s+O(1)` nonzero type lists. Let multiplicities be `m_0,...,m_q`, total `M`, with `m_j=n+O(s)`.

The ordered type-0 items create gaps `r=0,...,m_0`. Let `n_{j,r}` be the count of nonzero type `j` in gap `r`, and `h_r=sum_j n_{j,r}`. For row totals `sum_r n_{j,r}=m_j`, the exact probability of a gap array is

\[
\boxed{
P(n)=\frac{m_0!\prod_{j=1}^q m_j!}{M!}
\prod_{r=0}^{m_0}\frac{h_r!}{\prod_{j=1}^q n_{j,r}!}.}
\tag{4.1}
\]

Proof: allocate the distinct type-`j` items among gaps (`m_j!/prod_r n_{j,r}!` ways), interleave the nonzero items inside each gap (`h_r!` ways), and divide by the `M!/m_0!` permutations in which type-0 internal order is fixed.

If type `j` has associated type-0 deadline rank `d_j<=s`, source joint isolation requires

\[
\boxed{\sum_{r=0}^{d_j-1}n_{j,r}\ge K,\qquad K=k-s+O(1),}
\tag{4.2}
\]

for every relevant `j`.

Equations (4.1)--(4.2) are an exact finite coefficient sum. They also give a DP: process gaps in order; the state records remaining row totals and capped cumulative counts `c_j=min(K,sum_{h<r}n_{j,h})`; a transition placing vector `a` has weight `(sum a_j)!/prod a_j!`; when deadline `d_j` is crossed, discard states with `c_j<K`. This is exact but not claimed efficient. No code is needed for the theorem below.

## 5. Common-deadline race (B12/B7)

Relax (4.2) only by replacing the individual deadlines with the common `s`th type-0 deadline. Every relevant nonzero type must then have at least `K` symbols before that deadline. This is still stronger than Claim 278's scalar aggregate occupancy condition.

Choose

\[
s=\lfloor\sqrt{k/\log k}\rfloor,
\qquad q=s+O(1),\qquad K=k-s+O(1).
\tag{5.1}
\]

Let `R=2sk`. Since `R=polylog(n)` and all source type populations equal `n+O(s)`, the likelihood ratio of any finite without-replacement type prefix of length <=R to iid uniform `(q+1)`-type draws is `exp(O(R^2/n+Rs/n))=1+o(1)`. The event that the `s`th type-0 symbol occurs after time `R` has probability at most `exp(-(2+o(1))k)` by a binomial lower-tail estimate, so truncation is negligible.

Represent the iid type word as arrival order of `q+1` independent rate-one Poisson processes. Let `tau_s~Gamma(s,1)` be the `s`th type-0 arrival, and let `sigma_j~Gamma(K,1)` be the `K`th arrival of nonzero type `j`, independently. The relaxed event is `max_j sigma_j<tau_s`. Thus, with `F_K(t)=P(Pois(t)>=K)`, its probability is

\[
R_{s,K,q}=\frac1{\Gamma(s)}\int_0^\infty e^{-t}t^{s-1}F_K(t)^qdt.
\tag{5.2}
\]

Write `S_k=sqrt(k log k)`. Split at `t=K`.

For `t>=K`, discard `F_K^q<=1`. The Gamma tail identity and Stirling give

\[
\log R_{>=K}\le-k+(1/2+o(1))S_k.
\tag{5.3}
\]

For `t<K`, Chernoff gives

\[
F_K(t)\le\exp\{-K\log(K/t)+K-t\}
\le\exp\{-(K-t)^2/(2K)\},
\]

where `-log u-1+u >= (1-u)^2/2` for `0<u<=1`. Since `t^{s-1}<=K^{s-1}` and, with `z=K-t`,

\[
-t-q(K-t)^2/(2K)=-K+z-qz^2/(2K)\le-K+K/(2q),
\]

we get

\[
R_{<K}\le\frac{K^s}{\Gamma(s)}\exp[-K+K/(2q)].
\]

Stirling plus (5.1) yields

\[
\log(K^s/\Gamma(s))=(1/2+o(1))S_k,
\qquad K/(2q)=(1/2+o(1))S_k,
\]

and hence

\[
\boxed{\log R_{s,K,q}\le-k+(1+o(1))S_k.}
\tag{5.4}
\]

The finite-prefix comparison transfers (5.4) to the exact source conditional type word. Therefore

\[
\boxed{P(I_1\mid A_1)\le\exp[-k+(1+o(1))\sqrt{k\log k}].}
\tag{5.5}
\]

More generally `s=c sqrt(k/log k)` gives leading correction `(c/2+1/(2c))S_k`, minimized at `c=1`. This identifies the conserved balance: Gamma deadline entropy and simultaneous completion each contribute half. Beating constant 1 on this route requires restoring the individual deadlines `d_j` from (4.2).

## 6. Disconnection for `a<-1`

The source bad-pair event `B` is a finite union of the above bad-side cases and has probability `O(k^3/n)`. The source decomposition therefore gives

\[
P(I_1I_2\cap B)\le\exp[-\log n-k+(1+o(1))S_k].
\tag{6.1}
\]

On `B^c`, the source gives conditional independence. Claim 278's exact marking lower bound is

\[
p_n=P(I_1)\ge(1-k/(n-k))^{n-1}=\exp[-k-o(1)].
\tag{6.2}
\]

If `k<=log n+aW_n` with fixed `a<-1`, then `S_k=(1+o(1))W_n` and

\[
P(I_1I_2\cap B)/p_n^2\le\exp[(a+1+o(1))W_n]=o(1).
\]

Also `P(I_1\cap B)/p_n <= O(k^3/n)e^{k+o(1)}=exp[(a+o(1))W_n]=o(1)`. Hence the `B^c` conditional marginals are `p_n(1+o(1))`, so `P(I_1I_2)<=p_n^2(1+o(1))`.

For the isolated-vertex count `X`,

\[
EX=np_n\ge\exp[\log n-k-o(1)]=\exp[-aW_n-o(W_n)]\to\infty.
\]

The second moment method gives `P(X=0)->0`. Thus

\[
\boxed{a<-1\implies LK(n,k)\text{ disconnected whp}.}
\tag{6.3}
\]

## 7. Connectivity for `a>sqrt(11)`

Use Claim 278's Exp(1) score representation and put

\[
m_n=\log((n-1)/k),\qquad C=\log(32/5).
\]

Let `A` be the event that every kth-largest incident threshold lies in `(m_n-C,m_n+C)`. The same binomial Chernoff computation as Claim 278 gives `P(A^c)=o(1)` uniformly for `k=log n+O(W_n)`.

On `A`, set

\[
p_{tree}=e^{-(m_n-C)}=\frac{32k}{5(n-1)},\qquad
p_{cross}=e^{-(m_n+C)}=\frac{5k}{32(n-1)}.
\]

If a fixed `r`-set `S` is a connected component, some spanning tree of `S` has all edge scores above `m_n-C`, while every one of the `r(n-r)` crossing edge scores is at most `m_n+C`; otherwise that crossing edge would exceed both endpoint kth thresholds and be bilaterally present. Tree and crossing edges are disjoint independent sets. Cayley's formula gives

\[
P(\exists\ r\text{-component},A)
\le {n\choose r}r^{r-2}p_{tree}^{r-1}(1-p_{cross})^{r(n-r)}.
\tag{7.1}
\]

For fixed `r` and `k=log n+aW_n`,

\[
\log(\text{RHS})\le(1-5r/32)\log n-(5r/32)aW_n+O_r(\log\log n).
\tag{7.2}
\]

Thus every fixed `r=7,...,12` is absent whp, because `5r/32>1`. Claim 278's uniform version of the same envelope already excludes sizes `r>=13` through `n/2`.

A component of size at most 6 contains only vertices of degree at most 5. Claim 278's fixed-low-degree theorem at `kappa=5` gives

\[
P(deg(v)<=5)\le\exp[-k+(\sqrt{11}+o(1))S_k].
\]

If `a>sqrt(11)`, then

\[
nP(deg(v)<=5)\le\exp[(\sqrt{11}-a+o(1))W_n]=o(1).
\]

So no component of size <=6 exists whp. Together with (7.1)--(7.2) and the retained large-component bound,

\[
\boxed{a>\sqrt{11}\implies LK(n,k)\text{ connected whp}.}
\tag{7.3}
\]

This improves the positive frontier `sqrt(23)->sqrt(11)` without using mean degree.

## 8. Claim 280 and remaining obstruction

`P03-P0456-JOINT-RACE-FINE-BRACKET-280 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED` is exactly the conjunction of (6.3) and (7.3), with movement

\[
\boxed{a_{LK}^{fine}:\sqrt{23}\to\sqrt{11}}.
\]

Negative blocker: constant 1 is the optimum of the **common-deadline relaxation**. The exact DP (4.1)--(4.2) retains individual deadlines and is the next place to improve it.

Positive blocker: (7.2) first becomes automatically favorable at `r=7`; `r=6` has coefficient `1-30/32=1/16>0`. The next concrete route is to exploit bilateral internal rank constraints for component sizes 2--6, starting with `r=6`, rather than a one-vertex degree surrogate.

## 9. Directed P04/I0101 audit

Audited new peer claim `P04-I0101-A3-SIGNED-QUOTIENT-43 = PROVED / STRUCTURAL-PARTIAL` from

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T07-44-02Z__run-report.md`, creation `ea60d9802c16435ef9c8504e206ce36462b3bee4`, verified blob `7e0626e73c9f5a26ea59e44b7b97f3e750e1c171`. The peer receipt records exact-commit readback and terminal-marker recovery.

Audit ID:

`P03-AUDIT-P04-I0101-A3-SIGNED-QUOTIENT-281 = PASS (CLAIM-SCOPED)`.

Independent derivation: with `A=x^2-x+1`, `H=(x-2)(x+1)(2x-1)` and `zeta=H/(x(x-1))`, direct expansion gives

\[
H(1-x)=-H(x),\quad H(1/x)=x^{-3}H(x),\quad H^2=4A^3-27x^2(1-x)^2.
\]

Hence `zeta(gx)=sgn(g)zeta(x)` and `zeta^2=4J-27`. The cubic for a fiber is

\[
2X^3-(\zeta+3)X^2+(\zeta-3)X+2=0,
\]

whose discriminant is `(zeta^2+27)^2`. On the free `p==5 mod24` family, `|V_p|=(p-5)/4` and the A3 quotient therefore has `(p-5)/12` points.

Direct multiplication of the even and odd anharmonic roots gives

\[
\prod_{g\in A_3}(x-g(y))=\frac{x(x-1)}2[\zeta(x)-\zeta(y)],
\]

\[
\prod_{g\notin A_3}(x-g(y))=\frac{x(x-1)}2[\zeta(x)+\zeta(y)].
\]

On `V_p`, `chi(x)=chi(x-1)=1` and `chi(2)=-1`, yielding the two claimed Paley parity channels. Their product recovers the old `J` channel. Finally, substituting `x(t)=((1-t^2)/(1+t^2))^2` gives `H(x(t))=-2(1+t^4)(t^8-34t^4+1)/(1+t^2)^6`, so the claimed `beta=-chi(zeta)` relation also checks. Verdict PASS for Claim 43 only; this does not certify I0101 or Claim 44.

## 10. Ledger and next attack

Retained P0456 claims: 274, 276, 278, and new 280, all with publication novelty unverified. Metric state: `c_LK^cert=0` saturated; `a_LK^fine=sqrt(11)` after movement from `sqrt(23)`; fine unchanged count `0`; recoveries `0/2`.

Next attack: (i) take the variational/saddle-point limit of the exact individual-deadline DP, not the common-deadline race; (ii) derive direct component bounds for fixed `r=2,...,6`, starting at `r=6`. Recommended next Section-B triple: **B25 COUNT THE SAME THING TWICE, B5 ADD A PARAMETER AND DIFFERENTIATE, B24 FIND THE EXTREMAL OBJECT**.

`ledger_delta` for P26: P0456 remains PARTIAL; admit fine metric `a_LK^fine` at `W_n=sqrt(log n log log n)`, before `sqrt(23)`, after `sqrt(11)`, lower better; negative frontier `sqrt3->1`, positive `sqrt23->sqrt11`; new claim 280; peer audit 281 PASS claim-scoped; fine unchanged 0; recoveries 0/2; next obligation individual-deadline saddle point plus direct fixed components 2--6.

## 11. Runtime and delivery limitations

The requested GPT-6/maximum setting remains prompt-only. The exposed scheduler interface still supplies no model-family or reasoning-effort selector; this run actually used GPT-5.6 Sol and reasoning metadata is UNVERIFIED. Changing actual runtime selection requires platform/product support that exposes those controls. No permission denial occurred.

GitHub only; no Gmail, Drive, public posting, workflow execution, paid compute, access changes, or peer-file edits.

**End of complete run report.**