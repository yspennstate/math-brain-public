# exact target, quantifiers, hypotheses and units

A001/B01 stage 2, run 20261011T231625Z-fleet05-A001-quantifier-audit. All physical inputs are independent uniform bits, signs are Boolean, logarithms are base two. This stage computes the exact minimum over relevant physical coordinates of B_i/I_i and Delta_i H/I_i for the lead's X009 and B05 families. B_i=H(S_i conditional on S_without_i); Delta_i H=H(f)-[H(f_i^+)+H(f_i^-)]/2. These quantities differ by the nonnegative actual-child Jensen-Shannon term. No function with I_i=0 is divided by I_i.

**Completed mathematical result, pending independent review:** For every even m>=4, both X009 minima occur at every data coordinate. Their limits as m grows are 2 and 4 respectively. For canonical B05 with even k>=4 and r=2k controls, the erasure minimum occurs at data coordinates for k=4 and controls for k>=6 (A089's prior result, independently reconstructed here at r=2k). The entropy-decrement minimum occurs at data coordinates for k=4,6,8,10,12 and controls for every even k>=14. The selector is never minimizing. All minima are given below by closed expressions, not floating comparisons. In particular a bounded-ratio coordinate exists for both families in every dimension: X009 has B/I<2, Delta/I<4; B05 has a selectable decrement bound below 4+41/512. Full FEI is OPEN.

The universal target remains exists one finite C, for every finite dimension n and every Boolean sign f, H_2(f)<=C I(f); constants have H=I=0. This stage does not establish a uniform existential rule for all Boolean f or a hereditary stopping policy.

# sources actually read, revisions and theorem locators

Continuity inputs: BOARD.md, supervisor snapshot 2026-10-11 23:09 UTC; B01 STREAM_NOTES.md v1, 22:40 UTC; this agent's STATUS.md and preceding run; EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2, previously read in full. The lead explicitly assigns the X009/B05 minima and warns against rebuilding the completed gap table. The board records A086's independent acceptance of the previous tensor-admission claim at stated scope.

Original family definitions: source_material/reductions/paper/restrictions.tex, prop:bentsplice, and the original B05 run REPORT.md sections 2-6, 20261011T193057Z-fleet01-B05-rare-restrictions. The B05 every-coordinate no-go is already independently reviewed; it is not re-proved here. The exact split identity is C005 / restrictions.tex prop:splitexact and sources/ERASURE_REDUCTION.md.

New dependency consumed: A089/20261011T224857Z-fleet05-A089-repair-specialist/REPORT.md sections 2-4 and CLAIMS.json, claim A089-EXACT-EXISTENTIAL-ERASURE-REPAIR@1. A089 has already solved B05's erasure minimum and A062's separate balancing-sign minimum. This run audits only the B05 r=2k subclaim, using a directed Walsh-pair implementation and rational intervals, and adds X009 and decrement ordering. It does not independently accept A062 or A089's larger r>=2k scope.

Input hashes and theorem locators are saved in out/SOURCE_MANIFEST.json. Formula checking and source inspection are distinct from external acceptance. No outside literature claim is needed; no web or brain mutation is used.

# complete derivation or exact first unsupported line

## 1. Signed-pair functionals

For nonnegative u,v define

\[
\Phi(u,v)=(u+v)h_2(v/(u+v)),\qquad \Phi(0,0)=0.
\]

For real coefficients a,b define

\[
\mathcal D(a,b)=\eta(a^2)+\eta(b^2)
-\tfrac12\eta((a+b)^2)-\tfrac12\eta((a-b)^2),\qquad
\eta(q)=-q\log_2 q,\quad\eta(0)=0.
\]

For every coordinate i, group the Fourier coefficients into pairs (a,b)=(fhat(T),fhat(T+i)), T not containing i. Then

\[
B_i=\sum_T\Phi(a^2,b^2),\quad
\Delta_iH=\sum_T\mathcal D(a,b),\quad I_i=\sum_T b^2.
\]

Indeed restriction produces coefficients a+b and a-b. The first identity is conditional entropy in the parent law, the second is the exact entropy difference. Both functionals are symmetric in their arguments; D is invariant under either sign change because it interchanges the two restricted squares. Both are homogeneous of degree two in coefficient amplitudes. Directed multiplicities still matter for I_i: the coefficient with i present must remain the second component.

Write c=log2(e)=1/ln2; elementary atanh-series bounds give 7/5<c<3/2. The tools used below are Phi(u,v)<=u+v, Phi(u,v)>=2min(u,v), and, for u>=v>0,

\[
\Phi(u,v)\ge v[\log_2(u/v)+1].\tag{1}
\]

The last inequality follows from u log2(1+v/u)>=v. If u+v<=1, Phi(u,v)<=v log2(e/v). For each pair,

\[
0\le\mathcal D(a,b)-\Phi(a^2,b^2)\le2c\min(a^2,b^2).\tag{2}
\]

The lower counterpart is

\[
\mathcal D(a,b)-\Phi(a^2,b^2)
\ge 2c\frac{a^2b^2}{a^2+b^2},\tag{3}
\]

from 1-h2((1+z)/2)>=c z^2/2 at z=2ab/(a^2+b^2). These inequalities follow by integrating atanh z>=z and atanh z<=z/sqrt(1-z^2); (2) is the exact C005 bound applied to one pair.

## 2. One common core and its multiplicities

Let k>=4 be even, N=2^k, delta=1/N, s=1/sqrt(N), and

\[
b(x)=(-1)^{x_1x_2+\cdots+x_{k-1}x_k},\quad
h(x,y)=b(x)-2\mathbf1_{x=0}\mathbf1_{y=1}.
\]

This h is X009 (put k=m). Its bent coefficients c_T are +/-s with c_empty=c_singleton=s. Let mu=s-delta, a=1-mu. The h coefficients are

\[
\widehat h(T,\varnothing)=c_T-\delta,\qquad
\widehat h(T,\{y\})=\delta.
\]

Put N_+=(N+sqrt(N))/2 and N_-=(N-sqrt(N))/2. For any data coordinate, the directed no-selector coefficient pairs have counts

\[
\begin{array}{c|c}
(\mu,\mu)&N/8+\sqrt N/4\\
(s+\delta,s+\delta)&N/8-\sqrt N/4\\
(\mu,s+\delta)&N/8+\sqrt N/4\\
(s+\delta,\mu)&N/8-\sqrt N/4
\end{array}
\]

where absolute amplitudes suffice for entropy. The selector-containing part adds N/2 pairs (delta,delta). For explanation, toggling data bit j in the Fourier index changes the quadratic phase precisely when its partner bit is one. Fixing that partner to zero or one leaves a bent form on k-2 other coordinates with sign imbalance sqrt(N)/2; hence the directed counts above. In particular the mixed directed counts are not equal even though the two entropy functionals are symmetric. The initial implementation got this direction wrong, was rejected, and is documented in out/FIRST_CHECK_FAILURE.md.

Define the two data costs

\[
\beta=\tfrac12-\tfrac\delta2
+\frac{\Phi((s-\delta)^2,(s+\delta)^2)}{4\delta},\qquad
\gamma=1-\delta+\frac{\mathcal D(s-\delta,s+\delta)}{4\delta}.\tag{4}
\]

Every data coordinate of h has B_x=beta, Delta_x H=gamma, I_x=1/2+delta. Its selector has I_y=delta and

\[
B_y=N_+\Phi(\mu^2,\delta^2)+N_-\Phi((s+\delta)^2,\delta^2),\tag{5}
\]

\[
\Delta_yH=N_+\mathcal D(\mu,\delta)+N_-\mathcal D(s+\delta,\delta).\tag{6}
\]

All expressions are exact finite logarithmic expressions in the integer parameter; no large-cube enumeration is needed to define them.

## 3. X009: exact all-parameter minima

Because a bit has conditional entropy at most one, beta<=1. Thus beta/(1/2+delta)<2. The exact scalar split bound Delta_i H<=2 gives gamma/(1/2+delta)<4.

For every selector pair, (a^2+b^2)/b^2 >=N-2sqrt(N)+2>=N/2, since (sqrt(N)-2)^2/2>=0. Keeping only the b^2 log2((a^2+b^2)/b^2) term in Phi and summing yields B_y/I_y>=k-1. This excludes the selector from the erasure minimum for every k>=4. It also excludes it from the decrement minimum for k>=6, since Delta_y>=B_y. At k=4 the exact rational log certificate gives Delta_y/I_y>8 while gamma/I_x<4. Consequently

\[
\min_i\frac{B_i}{I_i}=\frac\beta{1/2+\delta},\qquad
\min_i\frac{\Delta_iH}{I_i}=\frac\gamma{1/2+\delta},\tag{7}
\]

and all data coordinates, only, attain both minima. As s->0, Phi((1-s)^2,(1+s)^2)->2 and D(1-s,1+s)->4; (4) gives beta->1, gamma->2. Thus the limits of (7) are 2 and 4. These are sharp suprema on X009, without being a lower bound of 4 on the optimal FEI constant.

## 4. B05: exact costs for every coordinate type

Put r=2k, p=2^(-r)=delta^2, t=pa, and let A(z)=1_(z=0) on r fresh controls. The original B05 sign is

\[
F(x,y,z)=1+A(z)(h(x,y)-1).
\]

Its coefficient at the completely empty index is 1-t. At nonempty control indices and empty core index it is -pa; at nonempty core index it is p hhat, for every control fiber. Hence activation changes the empty-core pair in every control fiber, not just the completely empty Fourier index.

The exact data costs and influence are

\[
B_x=p(\beta-2\mu^2)+(p-p^2)\Phi(a^2,\mu^2)
+\Phi((1-t)^2,p^2\mu^2),\quad I_x=p(1/2+\delta),\tag{8}
\]

\[
\Delta_xH=p(\gamma-4\mu^2)+(p-p^2)\mathcal D(a,\mu)
+\mathcal D(1-t,p\mu).\tag{9}
\]

For any control,

\[
B_z=2t-2t^2+\Phi((1-t)^2,t^2),\quad
\Delta_zH=4t-4t^2+\mathcal D(1-t,t),\quad I_z=t.\tag{10}
\]

Finally its selector has I_y=p delta and

\[
B_y=p[(N_+-1)\Phi(\mu^2,\delta^2)+N_-\Phi((s+\delta)^2,\delta^2)]
+(p-p^2)\Phi(a^2,\delta^2)+\Phi((1-t)^2,p^2\delta^2),\tag{11}
\]

\[
\Delta_yH=p[(N_+-1)\mathcal D(\mu,\delta)+N_-\mathcal D(s+\delta,\delta)]
+(p-p^2)\mathcal D(a,\delta)+\mathcal D(1-t,p\delta).\tag{12}
\]

Equations (8)-(12) come from the coefficient-pair multiplicities, not by assuming that Fourier spectra mix incoherently. The terms (p-p^2) retain all nonempty control fibers. Formula (9) is the new decrement counterpart of A089's erasure formula; (10)-(12) similarly retain the actual-child entropy costs.

## 5. B05 erasure: consumed prior theorem, independent subclaim check

A089 already proves that the erasure minimum is data at k=4 and control for even k>=6, for the more general r>=2k domain. Here is an independent reconstruction at the required r=2k.

The core obeys 1-c delta<=beta<=1-c delta/(1+delta), obtained from the two scalar entropy deficit bounds for z=2s/(1+delta). Since a/mu>1/s, (1) gives Phi(a^2,mu^2)>=(k+1)mu^2. Dropping the nonnegative last term in (8),

\[
\frac{B_x}{I_x}\ge2+\frac\delta{1/2+\delta}
 [((k+1)(1-p)-2)(1-s)^2-c-2].\tag{13}
\]

For k>=6 the bracket is greater than 8/25, by substituting k=6,s=1/8,p=1/4096,c<3/2; both positive factors increase afterward. Since 1/2+delta<=33/64, (13) is greater than 2+(3/5)delta.

For controls, (10) and Phi(u,v)<=v log2(e/v), t>=p/2, t<=p imply

\[
\frac{B_z}{I_z}\le2+\delta^2(4+4k)
\le2+(7/16)\delta\qquad(k\ge6).\tag{14}
\]

Also B_z/I_z>=2. The selector's nonempty data fibers have the same q/e>=N/2 lower bound as X009, but carry only 1-delta of the selector influence. Thus B_y/I_y>=(1-delta)(k-1)>=45/16, greater than the uniform control upper bound 2+20/256. At k=4 the interval certificate gives B_x/I_x<2<B_z/I_z and B_y/I_y>5. Therefore the erasure argmin is exactly as claimed by A089. This is acceptance of its B05 r=2k subclaim, not a second discovery and not acceptance of its A062 result.

## 6. B05 decrement: different argmin and an all-parameter tail proof

Let chi(t)=4-4t+D(1-t,t)/t. For t<=p<=1/256, (2) and Phi((1-t)^2,t^2)<=t^2 log2(e/t^2) show

\[
\chi(t)\le4+t[2\log_2(1/t)+3c]
\le4+\delta^2(4k+9/2)\le4+41/512.\tag{15}
\]

The function t[2log2(1/t)+3c] increases on this interval (its derivative is 2log2(1/t)+c>0), and delta^2(4k+9/2) decreases through even k>=4. Moreover chi(t)>4: (1) gives Phi((1-t)^2,t^2)>=t^2[2log2((1-t)/t)+1]>15t^2>4t^2, using (1-t)/t>=255 and log2(255)>7. Therefore every control ratio exceeds 4 but stays uniformly bounded by (15).

The selector lower bound in Section 5 excludes it from the decrement minimum for k>=6, because (1-1/64)*5>4+41/512. At k=4 its certified decrement ratio exceeds 8, while the data ratio is below 4.

For k=4,6,8,10,12 the strict data-versus-control decrement ordering is certified by out/ORDER_CERTIFICATES.json. The data ratio is <4 in these five cases, the control ratio >4. This establishes a genuine finite base, not an assumed pattern.

For all even k>=14 we prove the opposite order. First an exact lower bound for the core is

\[
\gamma\ge2-\delta(k/2+3c/2)>2-\delta(k/2+9/4).\tag{16}
\]

Indeed define G(s)=2[(1+s)^2 ln(1+s)+(1-s)^2 ln(1-s)]. Then G(0)=G'(0)=0 and G''(s)=12+4ln(1-s^2)<=12, so G(s)<=6s^2. Insert this into D(1-s,1+s) and (4) to get (16), retaining the explicit log delta term.

For k>=14, s<=1/128, a>=1-s, mu<=s, so a^2/(a^2+mu^2)>27/28. Combining (1) and (3), using c>7/5 and a/mu>1/s,

\[
\mathcal D(a,\mu)\ge\mu^2[k+1+2c a^2/(a^2+\mu^2)]
>\mu^2(k+37/10).\tag{17}
\]

Drop the nonnegative last term in (9), combine (16)-(17), and subtract 4(1/2+delta). This yields

\[
\frac{\Delta_xH}{p}-4(1/2+\delta)
>\delta\{[(k+37/10)(1-p)-4](1-s)^2-k/2-25/4\}.
\tag{18}
\]

For k>=14 the braced expression is bounded below by

\[
[(k+37/10)(1-2^{-28})-4](127/128)^2-k/2-25/4.
\]

This is linear in k with positive slope. At k=14 it exceeds 1/5 by an exact Fraction comparison saved in out/TAIL_ANCHORS.json. Consequently the data decrement ratio is greater than 4+delta/5 (in fact the stronger excess is delta/[5(1/2+delta)]). On the other hand (15) gives the control ratio less than 4+delta/100 for every k>=14: delta(4k+9/2) decreases and at k=14 equals (121/2)/16384<1/100. Hence controls strictly minimize for every even k>=14, with no finite-to-infinite extrapolation.

The exact minima for B05 are therefore

\[
\min_i B_i/I_i=\begin{cases}B_x/[p(1/2+\delta)]&k=4,\\B_z/t&k\ge6,\end{cases}
\quad
\min_i\Delta_iH/I_i=\begin{cases}\Delta_xH/[p(1/2+\delta)]&4\le k\le12,\\\chi(t)&k\ge14,\end{cases}\tag{19}
\]

where k is even and each numerator is the exact expression above. All coordinates of the minimizing type attain the minimum. The two limits are 2 and 4 by (10), because D(1-t,t)=O(t^2 log(1/t)) and Phi((1-t)^2,t^2)=O(t^2 log(1/t)). The selector's own ratios diverge, so it remains a valid all-coordinate obstruction.

## 7. Certificate summaries and first unsupported universal line

Illustrative rounded numbers (the saved rational intervals, not these decimals, certify the signs):

| Parameter | X009 min B/I | X009 min Delta/I | B05 min B/I, type | B05 min Delta/I, type |
|---|---:|---:|---|---|
| 4 | 1.620778 | 3.093730 | 1.856782, data | 3.381914, data |
| 6 | 1.895903 | 3.722359 | 2.005170, control | 3.870414, data |
| 8 | 1.973327 | 3.921213 | 2.000454, control | 3.978032, data |
| 10 | 1.993290 | 3.978238 | 2.000037, control | 3.997137, data |
| 12 | 1.998320 | 3.994063 | 2.000003, control | 3.999894, data |
| 14 | 1.999580 | 3.998393 | 2.000000205, control | 4.000000208, control |

Neither known every-coordinate falsifier contradicts existential selection. Also minimizing B_i/I_i need not minimize the actual decrement, even on a fully explicit all-weak-coordinate B05 family. At k=6,8,10,12 a C018-based selection would choose a control, whereas minimizing the exact paid decrement chooses a data bit. The JS term changes the argmin. Thus “the cheapest erasure coordinate minimizes entropy price” is false; the C005 bound only supplies a valid upper charge, not that ordering.

The first unsupported universal line is that every reached nonconstant function under such a policy admits a uniformly paid coordinate, or a terminal reserve paid from the same root influence. Fixing a control to zero produces r=2k-1, outside this stage's fixed r=2k statement; fixing data changes the quadratic phase/dummy pattern and the defect's relative position. Root ordering alone is not a hereditary theorem. Choosing a data/control bit cheaply does not erase the descendant seed entropy or imply the aggregate universal C018 bound B(f)<=K I(f).

# executed validation with domain, arithmetic, commands and outputs

Frozen specs out/FROZEN_SPEC.json, out/FROZEN_SPEC_v2.json and out/FROZEN_SPEC_v3.json precede their respective jobs. The first floating pilot accidentally included extra compressed parameters 12,20,40; this scope error is preserved in out/PILOT_SCOPE_CORRECTION.md and its output is discovery only. The certificate domain was explicitly re-frozen to k=4,6,8,10,12,14 after detecting the decrement transition. There was no increase in maximum explicit-table dimension (13), no GPU, no job over 300 MB, and no heavy-job memok trigger. No automatic dimensional escalation was used.

Commands executed from A001:

```text
python -X utf8 runs/20261011T231625Z-fleet05-A001-quantifier-audit/code/pilot.py
python -X utf8 runs/20261011T231625Z-fleet05-A001-quantifier-audit/code/certify.py --mode verify
python -X utf8 runs/20261011T231625Z-fleet05-A001-quantifier-audit/code/certify.py --mode certify
python -X utf8 runs/20261011T231625Z-fleet05-A001-quantifier-audit/code/tail.py
python -X utf8 runs/20261011T231625Z-fleet05-A001-quantifier-audit/code/finalize.py
```

The successful Walsh run checks every data/selector coordinate on cores k=4,6,8,10, constructs all activated pair histograms independently from those cores, and checks every physical coordinate of the full 13-bit B05 truth table k=4,r=8, including independent direct-edge influence. Result: 9 cases, 90 exact assertions, no failures. The final cached run is about 0.5 seconds; an earlier identical verification completed in about 34.1 seconds under concurrent load. No exponential 31-bit B05 table is built at k=10.

The ordering run checks 12 compressed family instances, all coordinate types, both ratios: 66 assertions, no failures, about 0.42 seconds. Every logarithm uses positive atanh series after normalization to [1,2], with z=(q-1)/(q+1)<=1/3, 36 terms and tail <=2 z^73/[73(1-z^2)]. Division by the ln2 interval uses all four quotient corners. The resulting logarithm intervals are rounded **outward** to grid 2^-100 by integer floor/ceiling, so subsequent rational additions remain compact. Saved lower/upper endpoints in out/ORDER_CERTIFICATES.json are exact rationals. No sign relies on a floating log; illustrative midpoint values are display only.

The first histogram error and a separate interval-denominator serialization error are saved in out/FIRST_CHECK_FAILURE.md and out/SERIALIZATION_CORRECTION.md. Both failed before certificate acceptance. Outward rounding repairs representation size, not a mathematical sign. out/TAIL_ANCHORS.json contains the rational base and slope checks that accompany the analytic tail proof.

# proof dependencies and changed downstream conclusions

New theorem dependencies: explicit quadratic Walsh expansion, exact pair entropy/restriction identities, scalar entropy inequalities, the certified finite base, and rational tail anchors. No universal FEI premise, B09 tax, unreviewed posterior payment or floating ordering is used. A089's B05 erasure subclaim is independently reconstructed and accepted only at r=2k; the new X009 and decrement minima have their own full derivations and are pending review.

Consumers A003/A005/A026/A064 should retain the exact distinction between existential B-selection and actual-decrement selection. A089/B18 can use the new decrement formulas alongside its prior B05 repair. These two explicit local falsifiers leave the universal selection route alive even when all influences become small. They do not settle the new lead's erasure-fraction or low-influence localization endpoint.

# one next mathematical action and independent reviewer

NEXT: derive a conditional-row transport identity for one selected data or control restriction, keeping both child deficits and their terminal entropy, then test that identity on activation of an arbitrary tensor core. The missing condition is hereditary payment; testing only another closed root family would not address it. This is a C019/C018 interface for A026/A064 and A003. Independent reviewer: A087 for the exact physical split and tail proof; A094 for the finite certificates and all-parameter argmin. A089 is an appropriate consumer but cannot serve as independent reviewer of its own imported erasure subclaim.

# actual persistence receipts or precise save blocker

The four protocol files, code/ and out/ are saved in this stage's assigned A001 run directory. Required field schemas, statement hashes, PROGRESS/PACKET_DELTA byte identity and file sizes are checked by the finalizer. Local input/output hashes are saved in out/SOURCE_MANIFEST.json and out/ARTIFACT_RECEIPTS.json. STATUS.md, WORKLOG.md and LEARNED.md are updated only inside A001. No shared tree, other agent folder, git state, brain store or external service was modified. Supervisor adoption, mirror verification and independent acceptance of this new claim are not asserted.

**Universal bridge:** This stage moves the B01 lead's exact good-coordinate target supporting C018: it closes both known local-family selection tests, confirms A089's B05 erasure result at the assigned scope, and adds the all-parameter entropy-decrement argmin, with the previously unpaid comparison resolved by a certified k<=12 base and an analytic k>=14 tail. Quantitatively, these all-coordinate counterexamples still admit B-ratios approaching 2 and decrement ratios approaching 4, uniformly bounded independently of dimension. Universal aggregate B<=K I and hereditary transport to descendants remain open. NEXT targets the conditional-row/child-deficit ledger on arbitrary-core activations, because that is the shortest missing edge from a cheap root coordinate to C019's fully paid stopping tree and full FEI, rather than another isolated class entropy bound.
