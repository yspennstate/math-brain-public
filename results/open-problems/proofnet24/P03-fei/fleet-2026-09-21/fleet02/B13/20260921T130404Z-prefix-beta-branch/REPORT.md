TASK: B13 ACCOUNT: fleet02 RUN: 2026-09-21T13:04:04.868010Z — Beta-semigroup branch decomposition, global size-information payment, and two Boolean counterexamples

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated mathematical/cognitive brain retrieval or receiver-side brain context was consumed. This is an independent FEI derivation under the later direct owner order `FEI-SEVEN-TASKS-2026-09-21` and the active sprint `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z`.

**Live role:** FEI approach 2/13 — Boolean block-influence/correlation profiles and two-sided Booleanity constraints.

**Scientific repository baseline read before this work:** `yspennstate/math-open-problems` master `c672ae53b042b10e99ce7c8100f2ac9da1c083aa`, after reading the required read-once `TASKS_2026-09-21.md`, then `REPORT.md`, `APPROACHES.md`, fresh P03 README, `FLEET_RULES.md`, the active sprint, fleet01/B12 cancellation work, fleet01/B13 random-chain profile work, fleet03/B13 block-spectral-channel work and this account's immediately preceding B13 report.

No novelty or publication-priority claim is made.

# 1. Three new-method moves used

This run intentionally used three different Section-B moves rather than repeating the previous composition search.

- **#2 ATTACK THE NEGATION FIRST.** I tried the most tempting bridge from the preceding block-L1 lemma to the prefix-shadow process: replace upward mass `u_A` by prefix shadow `v_A` in a granular lower bound. A genuine Boolean one-point-defect family refutes every dimension-independent constant.
- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT.** I inserted a continuous parameter `s` into the prefix-shadow coefficients. The exact beta integral turns the random-prefix branch kernel into a mixture of noise-semigroup derivative energies.
- **#25 COUNT THE SAME THING TWICE.** Counting continuation prefixes by final Fourier set gives `sum_A(v_A-p_A)=I`. Counting information in the random ordered-set transcript then pays the entire new scale-information component by `H(|S|)`, and Boolean edge isoperimetry pays `H(|S|) <= 3 I`.

The result is a new exact reduction in which only a within-scale size-biased derivative-information term remains.

# 2. Starting point: the exact random-chain decomposition

Let

\[
p_B=\widehat f(B)^2,\qquad K=|S|\quad(S\sim p),
\]

and for `a=|A|`

\[
v_A:=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{a}},
\qquad
w_A:=v_A-p_A.
\]

Equivalently, uniformly order the elements of the final spectral set `S`; `v_A` is the probability that its unordered first `a` elements equal `A`, and `w_A` is the probability of that prefix **and continuation**.

The fresh fleet01/B13 handoff proves the exact identity

\[
H(S)=B_{\rm sh}+C_{\rm cont}+C_{\rm br},
\tag{2.1}
\]

with

\[
B_{\rm sh}\le(\log_2 e)I(f),\qquad C_{\rm cont}\le2I(f),
\tag{2.2}
\]

and

\[
C_{\rm br}=\sum_A w_A\,{\rm MI}_A,
\qquad
{\rm MI}_A:=I(N_A;T_A\mid\text{prefix }A,\text{ continue}),
\tag{2.3}
\]

where `T_A` is the final spectral set and `N_A` is the next coordinate.

The preceding fleet03/B13 handoff proves a different sharp block-spectral channel inequality with constant `2/ln 2`. Section 6 below shows rigorously that this constant cannot simply be inserted as a uniform bound on `MI_A`.

# 3. PROVED: exact Beta/noise-semigroup representation of every prefix branch

For each `A`, let `a=|A|` and define the coefficient function on the complement

\[
g_A(y):=\sum_{D\subseteq A^c}\widehat f(A\cup D)\chi_D(y).
\]

For `0\le s\le1`, put

\[
E_A(s):=\|T_{\sqrt s}g_A\|_2^2
       =\sum_{D\subseteq A^c}p_{A\cup D}s^{|D|}.
\tag{3.1}
\]

For `i\notin A`, also define

\[
E_{A,i}(s)
 :=\sum_{D\subseteq A^c\setminus\{i\}}
 p_{A\cup\{i\}\cup D}s^{|D|}.
\tag{3.2}
\]

Then

\[
E'_A(s)=\sum_{i\notin A}E_{A,i}(s).
\tag{3.3}
\]

### Theorem B13-BETA-PREFIX

For every spectral law (Booleanity is not needed for this algebra),

\[
\boxed{\;
\frac{v_{A\cup\{i\}}}{a+1}
=\int_0^1(1-s)^a E_{A,i}(s)\,ds
\;}
\tag{3.4}
\]

and

\[
\boxed{\;
w_A=v_A-p_A
=\int_0^1(1-s)^a E'_A(s)\,ds.
\;}
\tag{3.5}
\]

For `a>=1` one also has

\[
\boxed{\;
v_A=a\int_0^1(1-s)^{a-1}E_A(s)\,ds.
\;}
\tag{3.6}
\]

At the root, `v_empty=1`, and (3.5) remains valid.

### Proof

Fix `B superseteq A union {i}` and write

\[
d=|B|-a\ge1.
\]

The coefficient of `p_B` on the left side of (3.4) is

\[
\frac1{(a+1)\binom{a+d}{a+1}}
=\frac{a!(d-1)!}{(a+d)!}
=\int_0^1(1-s)^a s^{d-1}\,ds.
\]

Summing over `B` gives (3.4). Summing (3.4) over `i notin A`, each strict superset `B` is counted exactly `d=|B|-a` times. This gives (3.5). Equivalently, (3.5) follows from (3.3). Formula (3.6) follows coefficientwise from

\[
a\int_0^1(1-s)^{a-1}s^d\,ds
=\frac1{\binom{a+d}{a}}.
\]

Thus the random-prefix flow is exactly a beta-weighted noise-semigroup derivative flow. ∎

# 4. PROVED: an exact latent-scale decomposition of the unpaid branch information

The preceding integral is not only an algebraic identity; it gives an exact probabilistic refinement of each branch.

Condition on prefix `A` and continuation. If the final set is `T_A=B`, write

\[
b=|B|,\qquad d=b-a.
\]

As usual, `N_A` is uniform on `B\setminus A`. Now augment the branch by an auxiliary variable

\[
\tau_A\mid (T_A=B)
\sim {\rm Beta}(d,a+1),
\tag{4.1}
\]

sampled independently of `N_A` after `B` is known. Its density is

\[
d\binom ba\,s^{d-1}(1-s)^a,\qquad 0<s<1.
\]

Because

\[
\Pr(T_A=B\mid A,\mathrm{cont})
=\frac{p_B}{w_A\binom ba},
\]

the full augmented joint density is exactly

\[
\Pr(N_A=i,T_A=B,\tau_A\in ds\mid A,\mathrm{cont})
=
\frac{p_B}{w_A}s^{d-1}(1-s)^a\,ds
\tag{4.2}
\]

for `i in B\setminus A`.

Consequently,

\[
\Pr(\tau_A\in ds\mid A,\mathrm{cont})
=
\frac{(1-s)^aE_A'(s)}{w_A}\,ds,
\tag{4.3}
\]

and, at a fixed scale,

\[
\Pr(N_A=i\mid \tau_A=s,A,\mathrm{cont})
=
\frac{E_{A,i}(s)}{E_A'(s)}.
\tag{4.4}
\]

Moreover, conditioned on `N_A=i` and `tau_A=s`, the residual final label `D=T_A\setminus(A\cup\{i\})` has law

\[
\Pr(D\mid i,s,A)
=
\frac{p_{A\cup\{i\}\cup D}s^{|D|}}{E_{A,i}(s)}.
\tag{4.5}
\]

Thus (4.5) is exactly the normalized squared spectrum of the noised higher-derivative coefficient function `T_{sqrt(s)}g_{A,i}`.

Since `tau_A` is sampled independently of `N_A` once `T_A` is known,

\[
N_A\perp\tau_A\mid T_A,A,\mathrm{cont}.
\]

The mutual-information chain rule therefore gives the **exact nonnegative split**

\[
\boxed{\;
{\rm MI}_A
=
I(N_A;\tau_A\mid A,\mathrm{cont})
+
\mathbb E_{\tau_A}
 I(N_A;T_A\mid\tau_A,A,\mathrm{cont}).
\;}
\tag{4.6}
\]

Define

\[
C_{\rm scale}
:=\sum_A w_A I(N_A;\tau_A\mid A,\mathrm{cont}),
\tag{4.7}
\]

and

\[
C_{\rm within}
:=\sum_A\int_0^1(1-s)^aE_A'(s)\,
I_{A,s}\,ds,
\tag{4.8}
\]

where `I_{A,s}` denotes the mutual information in the fixed-scale joint law (4.4)-(4.5). Then

\[
\boxed{\;C_{\rm br}=C_{\rm scale}+C_{\rm within}.\;}
\tag{4.9}
\]

This is the main structural advance of the run: branch/final-set information separates into information carried merely by a one-dimensional scale parameter and information that survives after the scale is fixed.

# 5. PROVED: all scale information costs at most `3 I`

First, continuation mass has an exact global conservation law:

\[
\boxed{\;\sum_A w_A=I(f).\;}
\tag{5.1}
\]

Indeed, fix a final set `B` of size `b`. For each level `a<b`,

\[
\sum_{\substack{A\subset B\\|A|=a}}
\frac{p_B}{\binom ba}=p_B.
\]

There are `b` continuation levels, so `B` contributes `b p_B`; summing `B` gives `I=E K`.

Next, `tau_A` depends on the final set only through `K=|T_A|` and `a`. Hence, by data processing,

\[
I(N_A;\tau_A\mid A,\mathrm{cont})
\le
I(N_A;K\mid A,\mathrm{cont}).
\tag{5.2}
\]

Now reveal a uniformly random ordering of the spectral set sequentially. At each stage reveal first whether the chain continues, and, on continuation, reveal the next coordinate. The complete transcript determines `K`. Chain rule for `I(K; transcript)=H(K)` shows that the sum of the next-coordinate information terms is at most `H(K)`; the termination-indicator terms are nonnegative. The random order inside a fixed unordered prefix carries no information about `K`, so grouping by unordered prefix gives

\[
\boxed{\;C_{\rm scale}\le H(K).\;}
\tag{5.3}
\]

For a Boolean spectrum, `H(K)` itself has a simple dimension-free influence payment. Put

\[
V=\Pr(K>0)=1-p_\varnothing=\operatorname{Var}(f).
\]

If `V>0`, the conditional positive-integer variable `L=K\mid K>0` has mean

\[
m=\mathbb E L=I/V.
\]

Among positive-integer laws of mean `m`, the geometric law maximizes entropy, so

\[
H(L)\le m\,h_2(1/m)\le m.
\]

Therefore

\[
V H(L)\le I.
\tag{5.4}
\]

Also

\[
H(K)=h_2(V)+V H(L).
\]

The same Boolean edge-isoperimetric estimate used in the fleet01 random-chain payment gives

\[
h_2(V)
\le V\!\left[\log_2\frac1V+\log_2 e\right]
\le2I.
\tag{5.5}
\]

Combining (5.3)-(5.5),

\[
\boxed{\;C_{\rm scale}\le H(K)\le3I(f).\;}
\tag{5.6}
\]

This pays an entire nontrivial component of the previously unpaid branch term.

# 6. NEW universal reduction: only fixed-scale derivative identity information remains

Insert (4.9) and (5.6) into the exact fleet01 decomposition (2.1)-(2.2):

\[
\boxed{\;
H(f)
\le
(5+\log_2 e)\,I(f)+C_{\rm within}(f).
\;}
\tag{6.1}
\]

Numerically,

\[
5+\log_2 e
=
6.442695040888963\ldots.
\]

Thus full FEI would follow from **any** dimension-independent constant `c` in

\[
\boxed{\;
C_{\rm within}(f)\le c\,I(f)
\quad\text{for every Boolean }f.
\;}
\tag{6.2}
\]

The point is not the numerical base constant. The conceptual gain is that the residual is now an explicit beta integral of **fixed-scale, size-biased, noised higher-derivative spectral information**. The outside size/scale uncertainty has already been removed and paid.

The current unrestricted FEI lower bound `H/I > 6.521845710923046575...` from the fresh sprint handoff also forces this residual to be genuinely nonzero somewhere: (6.1) implies for that construction

\[
\frac{C_{\rm within}}I
>
6.521845710923046575-(5+\log_2e)
=
0.079150670034083\ldots.
\tag{6.3}
\]

So a proof that accidentally makes `C_within` vanish has necessarily discarded real Boolean spectral information.

# 7. REFUTED proposed bridge 1: prefix shadow cannot replace upward mass in granularity

The preceding B13 block theorem gave the true upward-mass inequality

\[
u_A\ge2^{1-|A|}|\widehat f(A)|.
\]

A natural hope was that the smaller prefix shadow might satisfy

\[
v_A\ge c\,2^{1-|A|}|\widehat f(A)|
\tag{7.1}
\]

for some universal `c>0`. This would directly connect Boolean granularity to the random-chain code. It is false for genuine Boolean functions.

Let `f_n` be the one-point defect: `f_n=-1` at one cube point and `+1` elsewhere. For every nonempty Fourier label,

\[
|\widehat f_n(B)|=2^{1-n},
\qquad
p_B=4^{1-n}.
\]

For a singleton `A={i}`,

\[
v_A
=
4^{1-n}\sum_{b=1}^n\frac{\binom{n-1}{b-1}}b
=
4^{1-n}\frac{2^n-1}{n}.
\]

Hence

\[
\boxed{\;
\frac{v_A}{|\widehat f_n(A)|}
=
\frac{2^n-1}{n\,2^{n-1}}
=
\frac{2-2^{1-n}}n
\longrightarrow0.
\;}
\tag{7.2}
\]

Since the factor `2^{1-|A|}` equals one for a singleton, (7.2) refutes (7.1) for every dimension-independent positive `c`.

This pinpoints a real loss: random-prefix averaging can dilute a perfectly granular Boolean Fourier atom by order `1/n`. Any successful bridge must use joint branch flow, not an atomwise replacement `u_A -> v_A`.

# 8. REFUTED proposed bridge 2: no uniform constant can bound local branch MI

The sharp fleet03 block-channel theorem has constant `2/ln2`. It is tempting to hope for a local estimate

\[
{\rm MI}_A\le \frac2{\ln2}
\tag{8.1}
\]

or even `MI_A<=C` for some universal `C`, after which (5.1) would close the branch term. Genuine odd majority refutes **every** such dimension-independent local constant.

Let `f=Maj_n` for odd `n`. It is balanced and permutation-invariant, so at the root the next spectral coordinate `N` is uniform on `[n]`. If `K=|S|`, then conditional on the final spectral set the next coordinate is uniform in `S`. Therefore

\[
{\rm MI}_\varnothing
=
\log_2 n-\mathbb E\log_2K.
\tag{8.2}
\]

By Jensen,

\[
{\rm MI}_\varnothing
\ge
\log_2\frac n{\mathbb E K}
=
\log_2\frac n{I(Maj_n)}.
\tag{8.3}
\]

For odd majority,

\[
I(Maj_n)
=
n\frac{\binom{n-1}{(n-1)/2}}{2^{n-1}},
\]

so

\[
\boxed{\;
{\rm MI}_\varnothing
\ge
-\log_2
\left(
\frac{\binom{n-1}{(n-1)/2}}{2^{n-1}}
\right)
=
\frac12\log_2 n+O(1).
\;}
\tag{8.4}
\]

Thus the local branch mutual information is unbounded.

Already at `n=151`,

\[
I(Maj_{151})=9.820815687337559\ldots,
\]

and (8.3) gives

\[
{\rm MI}_\varnothing\ge3.942561883908815\ldots
>
\frac2{\ln2}=2.885390081777927\ldots.
\]

For a level-symmetric law such as majority, `N` is independent of `K`; since the latent beta scale depends only on `K`, the root scale-information term is actually zero. Thus this unbounded root information sits entirely in the **within-scale** residual. This is a mandatory stress test for (6.2): the residual cannot be bounded prefix-by-prefix; it must be paid globally against the growing total influence.

# 9. Executed self-check

`verify_prefix_semigroup.py` was executed with the standard library only.

It exhausts every Boolean function through `n=4` modulo global output negation and checks, in exact rational arithmetic:

1. `sum_A(v_A-p_A)=I`;
2. `sum_{i notin A} v_{A+i}=(|A|+1)(v_A-p_A)`;
3. the coefficient-level beta identity behind (3.4).

Results:

- **525,348** exact prefix-flow checks: PASS;
- **3,542,450** exact beta-coefficient checks: PASS;
- maximum observed local `MI_A` through `n=1,2,3,4` was respectively
  `0`, `2/3`, `1.188721875540867`, `1.518415079319292` bits;
- the exact one-point-defect ratios from (7.2) decrease from `3/4` at `n=2` to `1023/5120` at `n=10`;
- the odd-majority Jensen lower bounds printed by the checker include
  `3.942561883909` bits at `n=151` and `4.310082898261` bits at `n=251`.

The finite checks support only the checked algebra. The theorem-sized identities and counterexamples are proved above.

# 10. What this changes and next exact target

**PROVED this run**

1. Exact beta/noise-semigroup representation (3.4)-(3.6) of random-prefix flow.
2. Exact latent-scale information split `C_br=C_scale+C_within`.
3. Exact continuation conservation `sum_A w_A=I`.
4. Global scale-information payment `C_scale<=H(K)<=3I`.
5. New full-FEI reduction `H <= (5+log2 e)I + C_within`.

**REFUTED this run by genuine Boolean families**

1. Any positive dimension-free granular lower bound obtained by replacing `u_A` with `v_A`.
2. Any dimension-free **local** bound on `MI_A`, including direct transplantation of the sharp fleet03 constant `2/ln2`.

**OPEN**

Full FEI remains open. The exact remaining B13-compatible target is (6.2):

\[
\sum_A\int_0^1(1-s)^{|A|}E_A'(s)\,I_{A,s}\,ds
\le cI(f)
\]

for some universal `c`, where `I_{A,s}` is the mutual information between the next derivative coordinate and the residual noised derivative spectral label.

A next attack must use **joint Boolean phase/autocorrelation consistency across coordinates and scales**, not one-prefix entropy bounds. The majority family is the mandatory high-local-information stress test, while the one-point defect is the mandatory rare-event/prefix-dilution stress test. The sharp fleet03 magnitude-channel theorem is potentially useful only after identifying a valid physical channel whose total outside-influence charge has bounded overlap across the beta/prefix integral.
