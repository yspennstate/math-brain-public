Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `22 -> 23` genuinely distinct nonparabolic shape families; Section-B moves tried: #5 ADD A PARAMETER AND DIFFERENTIATE, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall source status remains PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 23: slowly inward critical tubes

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, exclusions, and the fixed metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the convention that trivial Brownian rescaling/reflection and parameter changes inside one structural family do not create new metric points.

The preceding authoritative R07 report is

`runs/R07/20260917T1423Z_i0077_branch_swapping_exterior_22.md`,

which moved the metric `21 -> 22` and used Section-B moves `#6,#12,#27`. This run uses the different second-cycle triple `#5,#18,#24`.

Before new mathematics I reread/recovered current `master` evidence from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0077.md`;
- the complete newest R07 report and targeted searches across the preceding I0077 report chain;
- the newest neighboring R06 evidence (now on a different source after its earlier rotations) and current R15 evidence. R15's old Burdzy--Scheutzow Problem 7.2 / I0076 assignment is preserved as a retired handoff and is not I0077;
- current repository ownership/exclusion searches for I0077 and arXiv:1302.6958.

`INDEX.md` and `RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. The canonical create-only reservation still names R07 and literally says `PENDING_ADMISSION, not READY`; the owner's repeated current prompt assigns exact I0077 to R07, and no competing live claim was found. I do not treat the reservation as proof of worldwide openness.

The large intake JSONL corpus is too large for a literal byte-for-byte connector rendering in one response. I therefore record the limitation honestly: exact I0077 source text, ownership, exclusions, and the prior R07/C29 history were recovered by targeted reads/searches; I do not claim a literal full-file reread of every intake row.

The old R07 KPZ/FPP route remains retired exactly as preserved in the original immutable handoff. Nothing was deleted or reopened.

## 2. Primary-source benchmark rechecked from the PDF

I re-opened the original PDF and visually checked the relevant pages, not merely a text snippet.

For `-infinity <= c_1 < c_2 <= infinity`, Burdzy--Scheutzow write `lambda_0(c_1,c_2)` for the positive principal exponent of killed Ornstein--Uhlenbeck motion with generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right).
\]

Remark 4.1 states continuity and strict domain monotonicity. Remark 4.2 records

\[
\boxed{
\lambda_0(-\infty,-1)
=\lambda_0(-1,1)
=\lambda_0(1,\infty)=1.
}
\tag{2.1}
\]

Theorem 4.3 states:

1. if `lambda_0(c_1,c_2) >= 1`, every FBM has the universal normalized far-past obstruction;
2. if `lambda_0(c_1,c_2) <= 1`, there is a decomposable FBM with normalized far-past liminf/limsup inside the interval;
3. if `c_1 <= 0 <= c_2` and `lambda_0(c_1,c_2) < 1`, there is a decomposable FBM pointwise inside that parabolic strip for every negative time.

The source treats the equality case in (i) by approximating the critical interval from inside. This yields an asymptotic statement at `lambda=1`; it does **not** by itself prohibit a path from staying eventually inside a boundary that approaches the critical walls from the inside.

Problem 7.8 is exactly the one-line request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Lévy text is Problem 7.9 and is not part of this assignment.

## 3. Fresh dated prior-art pass — 2026-09-17

Fresh bounded searches covered:

- `"Forward Brownian Motion" "Problem 7.8"` and exact-title/later-author/citing queries;
- Brownian `sqrt(t)` boundaries with logarithmic corrections;
- slowly moving killed Ornstein--Uhlenbeck boundaries and principal-eigenvalue survival;
- one- and two-sided asymptotically square-root first-passage results.

Nearest literature recovered includes Sato's 1977 square-root-boundary first-passage asymptotics, Denisov--Hinrichs--Sakhanenko--Wachtel (2022), *Crossing an Asymptotically Square-Root Boundary by the Brownian Motion*, and modern OU survival work such as Giorgini--Moon--Wettlaufer. These establish substantial ordinary-Brownian/OU prior art around the ingredients used below.

I did not locate, in this bounded dated pass, a later paper explicitly resolving exact Burdzy--Scheutzow Problem 7.8 or stating the FBM theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. The Lamperti transform, killed-OU spectral contraction, Brownian modulus bounds, and simple-eigenvalue perturbation are classical tools and are not claimed as new mechanisms by themselves.

## 4. Negation-first target: a critical limiting parabola does not control exact tail confinement

A natural extension rule is:

> If a moving tube converges after Brownian normalization to a source-critical parabolic interval, then its exact eventual-confinement behavior should be the same as the static critical parabola.

The family below falsifies that rule. The defect from the critical walls goes to zero, so every normalized endpoint limit is exactly the source-critical interval `[-1,1]`; nevertheless, the small inward defects accumulate over logarithmic time and can make exact eventual confinement impossible for **every** FBM.

This is a failure of that proposed extension rule, **not** a refutation of Problem 7.8 itself.

## 5. The new family: slowly inward critical tubes

Fix `beta>0` and `p>0`. Choose a deterministic `r_0` large enough that

\[
1-\beta r^{-p}>0\qquad(r\ge r_0).
\]

Let `a_{beta,p}:R->(0,infinity)` be any continuous function whose tail is

\[
\boxed{
a_{\beta,p}(r)=1-\frac{\beta}{r^p}
\qquad(r\ge r_0).
}
\tag{5.1}
\]

Its finite-`r` continuation is irrelevant to the far-past theorem; for a concrete full shape one may take it wide near the seam and interpolate continuously on a compact logarithmic interval.

Define

\[
\boxed{
\mathcal C_{\beta,p}
=
\left\{(-u,x):u>0,
\ |x|\le a_{\beta,p}(\log u)\sqrt u
\right\}\cup\{(0,0)\}.
}
\tag{5.2}
\]

For all sufficiently large `u` the normalized slice is a single bounded interval lying **strictly inside** `[-1,1]`, but

\[
a_{\beta,p}(\log u)\uparrow1.
\tag{5.3}
\]

Thus the limiting frozen exponent is exactly critical:

\[
\lambda_0(-1,1)=1.
\]

This is not run 4's outward `o(sqrt(u))` corrugation: those normalized walls lie outside the limiting strip. It is not run 11's pinched seam: here the new effect occurs in the remote past, not at `u=0`. It is not run 12's widening two-scale aperture class `0<a<=b`, because the present tail approaches its critical aperture **from the inside at every sufficiently large scale**, and its theorem depends on the accumulated vanishing defect rather than only the two endpoint apertures. Brownian rescaling shifts `r=log u` by a constant but preserves the sign and power `p` of the asymptotic inward defect. Reflection changes nothing in the symmetric family.

The entire `(beta,p)` class counts as **one** structural family, not one family per parameter.

## 6. Method #5 + #24: differentiate at the exact critical extremal object

Write

\[
\lambda(a):=\lambda_0(-a,a),\qquad a>0.
\]

The source identity gives `lambda(1)=1`. The exact critical ground state is elementary:

\[
h(x)=1-x^2,
\qquad
\mathcal A h=-h,
\qquad h(\pm1)=0.
\tag{6.1}
\]

The Rayleigh representation in the Gaussian reversible measure is

\[
\lambda(a)
=
\inf_{0\ne f\in H_0^1(-a,a)}
\frac{\frac12\int_{-a}^a |f'(x)|^2e^{-x^2/2}\,dx}
{\int_{-a}^a |f(x)|^2e^{-x^2/2}\,dx}.
\tag{6.2}
\]

Scale `x=ay` to the fixed interval `(-1,1)`. The resulting quadratic forms depend smoothly on `a`; the principal Sturm--Liouville eigenvalue is simple, so the standard one-dimensional Feynman--Hellmann differentiation applies. At `a=1`, using the eigenfunction `h(y)=1-y^2`, direct differentiation gives

\[
\boxed{
\lambda'(1)
=-\frac{4e^{-1/2}}
{\displaystyle\int_{-1}^1(1-y^2)^2e^{-y^2/2}\,dy}.
}
\tag{6.3}
\]

For completeness, this does not hide a numerical step. If

\[
I_m=\int_{-1}^1 y^m e^{-y^2/2}\,dy,
\]

then differentiation of the fixed-domain quotient at the stationary minimizer yields

\[
\lambda'(1)
=-2-\frac{I_4}{I_2}
+\frac{I_2-2I_4+I_6}{I_0-2I_2+I_4}.
\]

The eigenvalue identity at `a=1` gives `I_0-2I_2+I_4=2I_2`, while integration by parts gives

\[
I_{m+2}=(m+1)I_m-2e^{-1/2}.
\]

Substitution reduces the derivative exactly to (6.3).

Define

\[
\boxed{
\kappa_*:=-\lambda'(1)
=
\frac{4e^{-1/2}}
{\displaystyle\int_{-1}^1(1-y^2)^2e^{-y^2/2}\,dy}>0.
}
\tag{6.4}
\]

In fact `kappa_*>2` by a purely analytic estimate: the denominator is at most

\[
\int_{-1}^1(1-y^2)^2dy=\frac{16}{15},
\]

so

\[
\kappa_*\ge\frac{15}{4}e^{-1/2}>2.
\tag{6.5}
\]

(The last strict inequality follows, for example, from `e<3`.)

Therefore, for every `kappa<kappa_*`, there is `delta_0>0` such that

\[
\boxed{
\lambda(1-\delta)\ge1+\kappa\delta
\qquad(0<\delta<\delta_0).
}
\tag{6.6}
\]

This first-order excess above the critical exponent is the quantity accumulated below.

## 7. Method #18: say the shape in Lamperti language

Let `B` be standard Brownian motion and define

\[
Y_r=e^{-r/2}B_{e^r}.
\tag{7.1}
\]

Then `Y` is stationary Ornstein--Uhlenbeck motion with invariant standard Gaussian law `gamma` and generator `mathcal A`.

The Brownian event

\[
|B_u|\le a_{\beta,p}(\log u)\sqrt u
\qquad(R\le u\le T)
\]

is exactly

\[
|Y_r|\le a_{\beta,p}(r)
\qquad(\log R\le r\le\log T).
\tag{7.2}
\]

For a static interval `(-a,a)`, let `K_a(t)` be the killed-OU semigroup in `L^2(gamma)`. Self-adjoint spectral theory gives

\[
\|K_a(t)\|_{2\to2}=e^{-\lambda(a)t}.
\tag{7.3}
\]

On a unit log-time block `[j,j+1]`, the function `a_{beta,p}` is increasing for large `j`, so the moving allowed interval is contained in the largest static interval of the block,

\[
(-a_{\beta,p}(r),a_{\beta,p}(r))
\subset
(-a_{\beta,p}(j+1),a_{\beta,p}(j+1)).
\]

Hence the moving survival kernel on that block is pointwise dominated by the corresponding static killed kernel. Composing blocks and applying Cauchy--Schwarz gives, for large `s<t`,

\[
\mathbb P_\gamma\bigl(
|Y_r|\le a_{\beta,p}(r)\ \forall r\in[s,t]
\bigr)
\le
\exp\left\{-\sum_{j=\lceil s\rceil}^{\lfloor t\rfloor-1}
\lambda\bigl(a_{\beta,p}(j+1)\bigr)\right\}.
\tag{7.4}
\]

Choose `kappa<kappa_*`. By (6.6), for all sufficiently large `j`,

\[
\lambda(a_{\beta,p}(j))
\ge1+\kappa\beta j^{-p}.
\tag{7.5}
\]

Thus there is a constant `C` such that

### for `0<p<1`,

\[
\boxed{
\mathbb P_\gamma(\text{survival on }[s,t])
\le
C e^{-(t-s)}
\exp\{-c_{\beta,p}(t^{1-p}-s^{1-p})\},
}
\tag{7.6}
\]

for some `c_{beta,p}>0`;

### for `p=1`,

\[
\boxed{
\mathbb P_\gamma(\text{survival on }[s,t])
\le
C e^{-(t-s)}(t/s)^{-\kappa\beta}.
}
\tag{7.7}
\]

The baseline factor `e^{-(t-s)}` is the source-critical exponent one. The second factor is the cumulative price of the vanishing inward pinch.

## 8. A dependence-safe arbitrary-terminal lemma

The FBM witness time is random, so a deterministic-terminal estimate is not enough. I therefore prove the terminal statement pathwise before using FBM witnesses.

For large `u`, set

\[
f_{\beta,p}(u)
=\left(1-\frac\beta{(\log u)^p}\right)\sqrt u.
\tag{8.1}
\]

For a Brownian path `W`, call a terminal time `T` **good above lag R** if

\[
|W_T-W_{T-u}|\le f_{\beta,p}(u)
\qquad\forall u\in[R,T].
\tag{8.2}
\]

### Lemma 8.1

If either

\[
0<p<1,\quad\beta>0,
\tag{8.3}
\]

or

\[
p=1,\quad\kappa_*\beta>2,
\tag{8.4}
\]

then for every fixed sufficiently large `R`, a standard Brownian path has almost surely only finitely many good terminal times.

Equivalently,

\[
\boxed{
\mathbb P\{\exists\text{ good }T\ge A\}\longrightarrow0
\qquad(A\to\infty).
}
\tag{8.5}
\]

### Proof

First relax the boundary slightly: choose `0<beta'<beta`. In the marginal case `p=1`, because `kappa_* beta>2`, choose also `kappa<kappa_*` and `beta'<beta` so that

\[
\theta:=\kappa\beta'>2.
\tag{8.6}
\]

Choose an exponent `q>1`; in the marginal case choose it more specifically so that

\[
1<q<\theta-1.
\tag{8.7}
\]

Put

\[
R_k=(\log k)^q.
\tag{8.8}
\]

For standard Brownian motion define the unit-scale modulus

\[
M_k
=
\sup\{|W_t-W_s|:
0\le s,t\le k+1,\ |t-s|\le1\}.
\tag{8.9}
\]

A union bound over at most `k+2` intervals of length two and the reflection principle give, for all large `k`,

\[
\boxed{
\mathbb P\{M_k>8\sqrt{\log k}\}
\le12k^{-3}.
}
\tag{8.10}
\]

Suppose `T in [k,k+1]` is good for the original `(beta,p)` boundary and (8.10)'s good modulus event holds. For every `u in [R_k,k]`,

\[
\begin{aligned}
|W_k-W_{k-u}|
&\le |W_T-W_{T-u}|+2M_k\\
&\le f_{\beta,p}(u)+16\sqrt{\log k}.
\end{aligned}
\tag{8.11}
\]

But

\[
f_{\beta',p}(u)-f_{\beta,p}(u)
=(\beta-\beta')\frac{\sqrt u}{(\log u)^p}.
\tag{8.12}
\]

At `u=R_k`, the right side of (8.12) is of order

\[
\frac{(\log k)^{q/2}}{(\log\log k)^p},
\]

which dominates `sqrt(log k)` because `q>1`. The function `sqrt(u)/(log u)^p` is eventually increasing, so for all large `k`, (8.11) implies

\[
|W_k-W_{k-u}|\le f_{\beta',p}(u)
\qquad(R_k\le u\le k).
\tag{8.13}
\]

By Brownian time reversal, the probability of (8.13) equals the probability that a standard Brownian path stays in the relaxed moving tube on `[R_k,k]`. Its Lamperti transform starts at log-time `log R_k` with the invariant Gaussian law, so (7.6)--(7.7) apply.

For `0<p<1`,

\[
\mathbb P\{(8.13)\}
\le
C\frac{R_k}{k}
\exp\{-c(\log k)^{1-p}\}
\tag{8.14}
\]

for all large `k`; the omitted lower-end term is smaller order because `log R_k=q log log k=o(log k)`.
The series of (8.14) over `k` converges for every `q`.

For `p=1`, (7.7) gives

\[
\begin{aligned}
\mathbb P\{(8.13)\}
&\le
C\frac{R_k}{k}
\left(\frac{\log k}{\log R_k}\right)^{-\theta}\\
&\le
\frac{C}{k}
(\log k)^{q-\theta}(\log\log k)^\theta.
\end{aligned}
\tag{8.15}
\]

This series converges because `q<theta-1`.

Therefore

\[
\sum_k
\mathbb P\{\exists\text{ good }T\in[k,k+1]\}
<\infty
\tag{8.16}
\]

by (8.10), (8.14) or (8.15). Borel--Cantelli proves Lemma 8.1. `square`

## 9. Theorem I0077-R07-T24 — critical inward-pinch theorem

Let `C_{beta,p}` be the family (5.2).

### T24(i): the source-critical asymptotic obstruction is unchanged

For **every** `beta>0` and `p>0`, every FBM `X` satisfies

\[
\boxed{
\mathbb P\left(
\limsup_{u\to\infty}\frac{X_{-u}}{\sqrt u}\ge1
\quad\text{or}\quad
\liminf_{u\to\infty}\frac{X_{-u}}{\sqrt u}\le-1
\right)=1.
}
\tag{T24.i}
\]

Equivalently, because `a_{beta,p}(log u)->1`, the same statement holds after subtracting the moving upper/lower walls and dividing by `sqrt(u)`.

**Proof.** This is exactly source Theorem 4.3(i) at the critical interval `[-1,1]`, plus the deterministic limit (5.3). `square`

### T24(ii): the source-critical asymptotic existence phase is also unchanged

For every `beta>0` and `p>0`, there exists a decomposable FBM `X` such that

\[
\boxed{
\limsup_{u\to\infty}\frac{X_{-u}}{\sqrt u}\le1,
\qquad
\liminf_{u\to\infty}\frac{X_{-u}}{\sqrt u}\ge-1
\quad a.s.
}
\tag{T24.ii}
\]

**Proof.** Apply source Theorem 4.3(ii) to `[-1,1]`, whose exponent is exactly one. `square`

The point of the next clause is that (T24.ii) cannot be upgraded to exact eventual membership in the inward-moving tube.

### T24(iii): accumulated inward criticality kills exact eventual confinement

If either

\[
\boxed{0<p<1,\quad\beta>0,}
\tag{9.1}
\]

or

\[
\boxed{p=1,\quad\kappa_*\beta>2,}
\tag{9.2}
\]

then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
|X_{-u}|\le
\left(1-\frac\beta{(\log u)^p}\right)\sqrt u
\quad\forall u\ge R
\right)=0.
}
\tag{T24.iii}
\]

In particular, because (6.5) gives `kappa_*>2`, the explicit marginal tube

\[
\boxed{
|x|\le\left(1-\frac1{\log u}\right)\sqrt u
\qquad(u\text{ sufficiently large})
}
\tag{9.3}
\]

is universally impossible for eventual FBM confinement even though its normalized cross-section converges to the source-critical interval `[-1,1]`.

### Proof of T24(iii)

Assume the event in T24(iii) has positive probability. Since it is a countable union over deterministic integer tail thresholds and bounds on `|X_0|`, there are deterministic `R,M<infinity` and `q_0>0` such that

\[
E:=\left\{
|X_0|\le M,
\ |X_{-u}|\le f_{\beta,p}(u)\quad\forall u\ge R
\right\}
\]

has probability at least `q_0`.

Choose `beta_bar<beta` so close to `beta` that the hypothesis of Lemma 8.1 still holds for `beta_bar`. Since

\[
f_{\beta_{bar},p}(u)-f_{\beta,p}(u)
=(\beta-\beta_{bar})\frac{\sqrt u}{(\log u)^p}\to\infty,
\]

there is `R'>=R` such that on `E`,

\[
|X_0-X_{-u}|
\le f_{\beta_{bar},p}(u)
\qquad(u\ge R').
\tag{9.4}
\]

Let `(S_n)` be FBM witness times, `S_n->-infinity`, and for each fixed index `n` let

\[
W_n(t)=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

which is standard Brownian motion. Put `T_n=-S_n`.
For every sample in `E` with `T_n>=R'`, (9.4) gives

\[
|W_n(T_n)-W_n(T_n-u)|
=|X_0-X_{-u}|
\le f_{\beta_{bar},p}(u)
\quad(R'\le u\le T_n).
\tag{9.5}
\]

By Lemma 8.1, for a standard Brownian motion the probability that there exists any good terminal `T>=A` for this relaxed boundary tends to zero as `A->infinity`. Choose deterministic `A` so large that this probability is below `q_0/2`. Since `S_n->-infinity` almost surely, choose a **deterministic witness index** `n` large enough that

\[
\mathbb P(T_n<A)<q_0/2.
\]

Then (9.5) implies

\[
\mathbb P\{W_n\text{ has some good terminal }T\ge A\}
\ge
\mathbb P(E)-\mathbb P(T_n<A)
>q_0/2,
\]

contradicting the Brownian bound. No conditioning on the random witness time and no independence between the witness and its Brownian path is used. This proves T24(iii). `square`

## 10. What the three Section-B methods actually did

### #5 — ADD A PARAMETER AND DIFFERENTIATE

I parameterized the normalized half-width by `a` and differentiated the principal killed-OU exponent at the exact source-critical point `a=1`. The nonzero derivative (6.3) converts a vanishing geometric defect into a quantitative spectral tax.

### #18 — SAY IT IN ANOTHER LANGUAGE

The physical boundary `sqrt(u)(1-beta/(log u)^p)` becomes a slowly moving Dirichlet interval for stationary OU motion under Lamperti. In that language the obstruction is an operator-product estimate: each log-time block pays the critical `e^{-1}` factor plus a small extra factor, and those small factors accumulate.

### #24 — FIND THE EXTREMAL OBJECT

The source-critical eigenfunction `h(x)=1-x^2` is the extremal object. It makes the shape derivative exact and produces the explicit constant `kappa_*`; no numerical eigenvalue solver is needed.

## 11. Why this earns metric point 23

The preceding twenty-two counted families include outward asymptotically parabolic corrugations, seam pinches, widening two-scale apertures, several pulse/transport classes, disconnected fans/combs, power shears and exterior geometries. None has the defining signature here:

1. every sufficiently remote normalized slice is a **single bounded connected interval strictly inside** the same source-critical interval;
2. the inward defect tends to zero, so the limiting frozen exponent is exactly `1`;
3. there is no fixed supercritical interval that contains all sufficiently late allowed slices;
4. universal obstruction comes from the **cumulative first-order eigenvalue excess** of infinitely many vanishing defects.

Outward corrugations have the opposite sign of defect. The parabolic-tail/pinched-seam family places its singular geometry at `u=0`, not the far past. The earlier two-scale widening family has endpoint aperture data as its classifier; it does not have an every-large-scale inward approach to a critical limit. Brownian rescaling only shifts `log u` by a constant and cannot change the inward sign or exponent `p` of the tail defect.

Accordingly the frozen metric moves

\[
\boxed{22\longrightarrow23},
\qquad
\text{unchanged count}=0.
\]

Different values of `beta` and `p` are not counted separately.

## 12. Validation, limitations, audits, and next obligation

There is no finite combinatorial/arithmetic core in T24. The proof is analytic: the only explicit constant is derived on the page from the exact critical eigenfunction and elementary integrals. Creating a checker would not test the theorem's difficult step and would violate the research-first policy, so no checker was manufactured.

The theorem deliberately leaves open:

- `p>1`, where the integrated first-order spectral excess is finite and the present route no longer gives a summable arbitrary-terminal bound;
- the possible sharp marginal threshold in the `p=1` class. The sufficient FBM threshold `kappa_* beta>2` contains loss from the arbitrary-terminal Brownian modulus compiler and is **not claimed sharp**.

Those are mathematical boundary questions, not gaps in the theorem as stated.

I found no P26 end-to-end audit of T24 and no second independent OTHER-track audit of T24. Therefore:

- T24 is a theorem-sized R07 claim with a complete proof on this page;
- source Problem 7.8 remains **PARTIAL**, not CLOSED;
- publication novelty remains **UNVERIFIED**;
- no `paper_<name>/` closure package is created.

The cleanest next route, if the metric is to move again, is **not** another `beta,p` value. It is either (a) settle the complementary integrable-pinching mechanism `p>1` with a constructive decomposable FBM or a sharper obstruction, or (b) move to a geometrically different class. Parameter changes inside this family do not count.

## 13. Model / reasoning / scheduler-control status

The actual runtime available to this report identifies as GPT-5.6 Sol; reasoning effort is not authenticated by exposed telemetry, so it is reported as **UNVERIFIED**, not as GPT-6 maximum.

The exposed task-control schema still offers title/prompt, schedule/start offset, enabled state and timing mode, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Thus GPT-6/maximum remains prompt text only. Enforcing it would require the product/API or an authorized owning/admin workspace surface to expose those controls.

The historical `You cannot modify this task` P26 event was authorization-context-specific; current repository evidence records a later authorized context in which P26 did update successfully, while another context denied edits to the R-series. The lawful workaround is the owning authorized context or platform support, not a duplicate task, repository-only edit, or permission bypass. This run was explicitly research-only and made no scheduler mutation.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  claim_id: I0077-R07-T24
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 22
  after: 23
  movement: +1
  unchanged_count: 0
  new_family: "slowly inward source-critical tubes"
  methods_this_run: [5, 18, 24]
  negation_test: "convergence to a critical normalized parabola does not preserve exact eventual confinement"
  theorem_scope:
    asymptotic_obstruction: "source-critical [-1,1] Theorem 4.3(i) survives for every beta,p"
    asymptotic_existence: "source-critical Theorem 4.3(ii) survives for every beta,p"
    exact_eventual_obstruction_p_lt_1: "all beta>0"
    exact_eventual_obstruction_p_eq_1: "kappa_* beta > 2"
    p_gt_1: UNCLASSIFIED
    marginal_sharp_threshold: UNCLASSIFIED
  critical_shape_derivative:
    kappa_star: "4 exp(-1/2) / integral_{-1}^1 (1-y^2)^2 exp(-y^2/2) dy"
    certified_bound: "> 2"
  canonical_example: "|x| <= (1 - 1/log u) sqrt(u) for all sufficiently large u"
  finite_core: NONE
  self_check: "analytic derivation only; no finite checker warranted"
  prior_art: "bounded dated search completed; ordinary Brownian/OU moving-boundary literature found; no explicit exact Problem-7.8/T24 resolution located; novelty UNVERIFIED"
  audits:
    new_T24_p26: PENDING_NOT_FOUND
    new_T24_second_other_track: PENDING_NOT_FOUND
  source_status: PARTIAL
  closure: false
  paper_package: false
  remaining_obligation: "integrable inward pinches p>1 or a genuinely different geometry; two external audits required before any closure claim"
```

No email/Gmail, Drive, public posting, purchase, permission change, shared-root edit, peer-file edit, workflow execution, or scheduler change was performed.