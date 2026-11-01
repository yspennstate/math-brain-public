Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested, but the available runtime provides no authenticated applied-model/effort telemetry establishing that setting. **NO SOURCE-METRIC MOVEMENT:** Salez Problem 2.3 remains OPEN/PARTIAL and `W_exp=1/2 provisional -> 1/2 provisional`. **MECHANISM MOVEMENT:** proved a multi-block persistence theorem for the invariant heat-kernel localization relation forced by non-cutoff, derived an exact spectral-gap/TV-delay obstruction across integer multiples of the early mixing time, isolated an exact `q^2`-state Markov quotient and mutual-information obstruction for the affine Haiman stress test, and proved that its canonical induced slow direction is an exact L2-heavy/L1-rare spike.

# PROB10-08 — block persistence of transitive localization and the affine mutual-information bottleneck

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL / auxiliary obstruction and reduction theorems proved / no new source-level cutoff class this run / independent validation pending / worldwide novelty UNVERIFIED**.

## 0. Required continuity and consumed state

This run followed the owner PROB10 contract and did not restart an older route. Before research I read/recovered:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`, preserving the exclusion of the already-written Abelian Cayley/product-condition target;
- canonical `operations/claims/I0112.md`, blob `707af6a4ca81d0d6bcf52225c6f69c266ae981e9`;
- preserved pre-refocus R16 successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, blob `fa18fa8669a638c362ad0f90300b733425e808e5`;
- historical I0112 stuck report `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`, blob `048a1dfd9821b0c99cd96c8705e609b3d7ce22da`, preserving the exhausted product-varentropy, synchronous-tensor, moving-weight/local-Poincare, Hecke/information-curvature, curvature, local-limit/AEP and time-zero subcommutation failures;
- newest own predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T06-07-00Z_early-threshold-relation-affine-lre_71c9.md`, blob `a222d5f3f6b9edab589452d66b01aa1bf8164167`;
- the earlier affine two-scale/L2 artifact `artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T03-58-30Z_affine-l2-spectral-barrier_d4c7.md`;
- newest neighboring P26 T08 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_07-58-10__ramanujan-spherical-set-transfer.md`, blob `5f38814781f04ad7c39c1462e4492f6eb268c1fe`; P26 owns shell/spherical-distance transfer;
- newest neighboring NM13 T08 report `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T06-20-00Z__arc-cover-hodge-orbit-drift.md`, blob `a7984c0e662bbca4df7195a9aa2de2350c2407e0`; NM13 owns arc-cover/Hodge, orbit compression and direct product/output-spectrum directions.

Accordingly this run does not duplicate the newer spherical-distance, line/fiber, truncation/replacement-product, arc-cover/Hodge, exact-distance/orbit, old tensor, or old moving-Poincare routes.

The master head observed immediately before persistence of the proof artifact was `1d1b42ef4797562f5324270bf6d838b6504dac45`. The proof artifact was then created at commit `5f9fbad7e45afe9dc5f651ce523f0b048c7f0ae1`, blob `92898f76c47884220fa5e2f6985091dc350c4c70`, and read back at that exact commit. Concurrent authorized work advanced master; immediately before this report write the observed master head was `f6bc6e3055b0f64080e8a9c20617f4c3eb04de22`. All writes here are create-only; no force push or shared-root/peer edit is used.

## 1. Primary-source refresh and exact use of long-range expansion

The source target remains Justin Salez, `https://arxiv.org/abs/2508.21055`, Problem 2.3, with the rate-one continuous-time SRW convention and source graph class frozen exactly as before.

Dylan J. Altschuler, `https://arxiv.org/abs/2609.14945v1`, submitted **14 September 2026**, remains the new primary positive lead. A bounded current search on 20 September 2026 found the arXiv record still at v1 and did not surface a correction/erratum. I reread the proof rather than using only the abstract.

The exact role of LRE is still:

1. Lemma 3.2 transfers graph LRE to maximal-rate volume growth for the oriented-edge NBRW state space;
2. Lemma 3.3 converts that set growth into near-maximal entropy for the NBRW;
3. Proposition 3.1 obtains endpoint Shannon entropy `log n - O(log log n)` at the entropic radius;
4. Lemma 3.4 then uses the ordinary spectral gap only for the short cleanup from near-maximal entropy to TV mixing.

Thus the missing full-source input is still an entropy/Green replacement for maximal long-range growth; ordinary transitive spectral expansion is not known to imply Altschuler's premise.

Haiman--Schildkraut--Zhang--Zhao, `https://arxiv.org/abs/2109.13131v3`, remains the source for the affine high-multiplicity stress family. No theorem from that paper is counted as new fleet progress.

## 2. Starting obstruction from the predecessor

The corrected preceding report established that if a source-admissible family fails cutoff, then along a subsequence there exist fixed

`epsilon in (0,1/2)`, `a>0`, `b>0`

and the **early** threshold

`t=t_mix(1-epsilon)`

such that

`R(x)={y:n H_t(x,y)>=n^a}`

forms a symmetric automorphism-invariant regular relation satisfying

`H_t(x,R(x))>=b`,

and

`m:=|R(x)|<=n^(1-a)`.

The predecessor used this once, at time `t`, to force a same-time return spike and a polynomial spectral pile-up. This run asks a different question: **what happens if the Markov chain is required to keep making such relation-sized moves over several independent blocks of length `t`?**

That question produces the retained theorem below.

## 3. New theorem — invariant localization persists through every block

Let `R^{o k}(x)` denote the endpoints of relation paths of length `k` from `x`. For any vertex-transitive regular graph, any invariant symmetric regular relation of degree `m`, any time `t`, and any `b` with

`H_t(x,R(x))>=b` for every `x`,

the Markov property gives, exactly,

\[
\boxed{
H_{kt}(x,R^{\circ k}(x))\ge b^k,
\qquad
|R^{\circ k}(x)|\le m^k.
}
\tag{3.1}
\]

The proof is one line of conditional probabilities but has a nontrivial consequence: at block `j`, conditioned on every earlier block, the chance that the next endpoint lies in `R` of the current state is still at least `b`; multiplying these conditional probabilities gives `b^k`. The endpoint of such a path lies in the `k`-fold relation composition and there are at most `m^k` relation paths.

Testing TV against this endpoint set yields

\[
\boxed{
 d_{TV}(kt)\ge b^k-\frac{m^k}{n}.
}
\tag{3.2}
\]

Because the heat kernel is symmetric,

`H_{2kt}(x,x)=sum_y H_{kt}(x,y)^2`,

and Cauchy--Schwarz on `R^{o k}(x)` gives

\[
\boxed{
 nH_{2kt}(x,x)\ge b^{2k}\frac{n}{m^k}.
}
\tag{3.3}
\]

These are full finite-graph statements, not asymptotic heuristics. The complete proof is in the matching artifact.

### Consequence for the non-cutoff relation

For the predecessor's `m<=n^(1-a)`, whenever a fixed integer `k` satisfies

`k(1-a)<1`,

(3.2) gives

\[
\boxed{
 t_{mix}(b^k/2)\ge k\,t_{mix}(1-\varepsilon)
}
\tag{3.4}
\]

for all large `n`. Thus polynomial likelihood localization cannot be a single-time anomaly: if its support exponent is small enough to survive `k` compositions without becoming macroscopic, it forces an **integer-factor delay at another fixed TV threshold**.

## 4. New spectral restriction across several blocks

Assume the source one-sided gap

`1-lambda_2(P)>=gamma>0`.

Transitivity gives

\[
nH_{2kt}(x,x)=1+\sum_{i=2}^n e^{-2k(1-\lambda_i)t}.
\]

For `k>=2`,

\[
\sum_{i=2}^n e^{-2k(1-\lambda_i)t}
\le
n e^{-2(k-1)\gamma t}.
\]

Combining this with (3.3) gives the exact inequality

\[
\boxed{
 b^{2k}\frac{n}{m^k}
 \le 1+n e^{-2(k-1)\gamma t}.
}
\tag{4.1}
\]

If

`m=n^(theta+o(1))`, `k theta<1`, and `kappa_n=gamma t/log n`,

then exponent comparison yields

\[
\boxed{
 \theta\ge \frac{2(k-1)}{k}\,\kappa_n-o(1).
}
\tag{4.2}
\]

For the non-cutoff relation, `theta<=1-a`, hence every fixed `k>=2` with `k(1-a)<1` must satisfy

\[
\boxed{
\frac{\gamma t_{mix}(1-\varepsilon)}{\log n}
\le
\frac{k(1-a)}{2(k-1)}+o(1).
}
\tag{4.3}
\]

This is a genuine additional constraint beyond the predecessor's one-time spectral-band pile-up.

For completeness the artifact also proves the elementary bounded-degree scale

\[
t_{mix}(1-\varepsilon)
\ge
\left(\frac1{4\log(D-1)}-o(1)\right)\log n
\tag{4.4}
\]

for maximum degree at most `D>=3`, by the Poisson jump count and the size of a radius-`2t` ball. Combining (4.3) and (4.4) gives

\[
1-a\ge
\frac{\gamma(k-1)}{2k\log(D-1)}-o(1).
\tag{4.5}
\]

This does **not** close the conjecture, because failure of varentropy concentration may produce a small fixed `a`. It does narrow the allowed localization geometry.

## 5. Exact affine stress-test reduction: a q^2-state Markov quotient plus mutual information

I next attacked the concrete affine stress family by a route not used in the old L2/NBRW calculations.

Freeze

`Gamma_q=Pi_q semidirect V_q`, `Pi_q=SL(2,q)`, `V_q=F_q^2`,

with the same 16 subgroup generators and translation pair `(I,+/-e)`. With multiplication

`(M,x)(N,y)=(MN,x+My)`, define the relative coordinate

\[
Y=M^{-1}x.
\]

Then the right Cayley walk has the exact quotient dynamics

- subgroup step `(s,0)`: `Y -> s^{-1}Y`;
- translation step `(I,+/-e)`: `Y -> Y+/-e`.

Thus `Y_t` is itself a Markov chain on exactly `q^2` states, with jump kernel

\[
\boxed{
(Q_Y f)(y)=\frac1{18}
\left(\sum_{s\in S}f(s^{-1}y)+f(y+e)+f(y-e)\right).
}
\tag{5.1}
\]

The subgroup coordinate `M_t` is also Markov, making an `S`-move with total rate `8/9`. The map `(M,x)<->(M,Y)` is bijective and uniform measure on `Gamma_q` becomes `U_Pi tensor U_V`. Therefore the information deficit has the exact chain-rule decomposition

\[
\boxed{
D(\mathcal L(M_t,Y_t)\|U_{\Pi}\otimes U_V)
=
D(\mathcal L(M_t)\|U_{\Pi})
+D(\mathcal L(Y_t)\|U_V)
+I(M_t;Y_t).
}
\tag{5.2}
\]

This is a useful reduction of the explicit non-LRE source-admissible stress test. Marginal mixing of `M` and `Y` is **not** enough: a proof must also make the mutual information `I(M_t;Y_t)` negligible on the mixing scale. The translation kernel alone has no dimension-free entropy contraction, so this is a genuine rotation-plus-noise/hypocoercive problem rather than a one-step refresh.

No cutoff theorem for the affine family is claimed.

## 6. Exact rare-spike calculation — why affine multiplicity alone cannot refute cutoff

A second exact calculation diagnoses the old high-multiplicity route.

Let `H=Pi_q`, `r=[Gamma_q:H]=q^2`, `m=r-1`, and realize

`Ind_H^Gamma(1)=1 direct-sum phi_q`

on the `r` left cosets. Let `u_0` be the normalized mean-zero contrast that equals `sqrt(r-1)` on the distinguished coset `H` and `-1/sqrt(r-1)` on every other coset. Then the permutation matrix coefficient is exactly

\[
\boxed{
\langle u_0,\rho(g)u_0\rangle
=
1\quad(g\in H),
\qquad
=-\frac1{r-1}\quad(g\notin H).
}
\tag{6.1}
\]

Consequently, for uniform `g`,

\[
\boxed{
E|\langle u_0,\rho(g)u_0\rangle|=\frac2r,
\qquad
E|\langle u_0,\rho(g)u_0\rangle|^2=\frac1{r-1}.
}
\tag{6.2}
\]

So this canonical slow representation direction is an **exact rare spike**: its L2 scale is `1/sqrt(m)` but its average absolute size is only order `1/m`. The polynomial second-eigenvalue multiplicity therefore cannot, by itself, imply a broad TV window or a counterexample. The missing datum is the L1 matrix coefficient of the **actual perturbed top vector** after adding the translation generator.

Writing that vector `u=alpha u_0+w`, Schur orthogonality gives only

\[
E|\langle u,\rho(g)u\rangle|
\le
\frac{2|\alpha|^2}{r}
+
\frac{2|\alpha|\|w\|+\|w\|^2}{\sqrt m}.
\tag{6.3}
\]

The existing spectral perturbation bound makes `||w||` only `O(1)`, not `o(1)`, so (6.3) is not enough to prove TV-negligibility. This is a precise obstruction, not a hidden cutoff claim.

The geometry also explains why the new block theorem does not dispose of the affine test automatically. Its natural `Pi_q` coset fibers have size

`|Pi_q|=N_q^(3/5+o(1))`,

and their number is

`q^2=N_q^(2/5+o(1))`.

Thus the natural complementary exponents are `(theta,a)=(3/5,2/5)`. Since `theta>1/2`, a second relation composition is already potentially macroscopic. A full source proof must therefore handle the moderate-localization regime `a<=1/2`, not only very sparse exceptional sets.

## 7. Three materially different nonexhausted approaches tested

### A. Multi-block invariant-relation concatenation — RETAINED

This is the main success of the run. It proves (3.1)--(4.5), converting one-time heat-kernel localization into a fixed-threshold mixing delay and a new spectral-gap restriction at each admissible integer scale.

### B. Use the Haiman high-multiplicity slow block as a direct TV counterexample mechanism — NAIVE VERSION REFUTED

The exact coefficient formula (6.1)--(6.2) shows that the canonical induced direction is L2-large but L1-tiny. High multiplicity is therefore not enough. A genuine counterexample route must control the actual perturbed eigenvector in L1, not merely its eigenvalue and multiplicity.

### C. Prove affine cutoff by mixing the subgroup and quotient marginals separately — REDUCED, NOT CLOSED

The exact relative-coordinate quotient (5.1) makes both marginals Markov, but the entropy identity (5.2) leaves the mutual information term. This is the precise obstruction to a naive marginal-tensorization proof. The next viable affine route is a rotation-plus-translation information-contraction estimate for `I(M_t;Y_t)`, not another L2 trace estimate.

These are distinct from the immediately preceding one-time Green/spectral-band argument and from the historical product-varentropy, moving-Poincare and synchronous-tensor attempts.

## 8. Tests/checks actually run

No simulation, finite mixing plot, brute-force enumeration, numerical optimization or checker was used. There is no finite computational core in this run.

Analytic self-checks performed:

- multiplied conditional block probabilities to verify the exact `b^k` persistence;
- checked the `m^k` endpoint bound and the resulting TV test-set inequality;
- checked the Green inequality by the continuous-time semigroup identity and Cauchy--Schwarz;
- checked the transitive heat-trace formula and the spectral-gap decay leading to (4.1);
- checked the Poisson-jump support argument behind (4.4);
- checked the semidirect-product generator action on `Y=M^{-1}x`;
- checked the relative-entropy chain rule in (5.2);
- checked both cases of the induced matrix coefficient and its exact first/second absolute moments;
- re-read Altschuler's full entropy step and ran a bounded current correction/erratum search; no later version surfaced.

These are self-checks only. Independent audit count remains **0** for the present claims.

## 9. Source before/after, auxiliary changes, and ledger delta

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  exact_walk: "rate-one continuous-time simple random walk"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  new_graph_class_with_TV_cutoff: false
  mechanism_before:
    - "non-cutoff forces polynomial heat-kernel localization at the early threshold"
    - "same-time Green spike"
    - "O(1/log n) spectral-band pile-up"
    - "affine Haiman family certified source-admissible and outside LRE"
  mechanism_after:
    - "exact b^k multi-block persistence on the invariant relation"
    - "fixed-threshold integer-factor TV delay while m^k=o(n)"
    - "spectral-gap restriction b^(2k) n/m^k <= 1+n exp(-2(k-1) gamma t)"
    - "exact q^2-state relative-coordinate affine quotient"
    - "joint entropy deficit split into two marginal deficits plus mutual information"
    - "exact L2-heavy/L1-rare induced matrix coefficient"
  finite_checker: "not applicable"
  independent_audits: 0
  publication_novelty: "UNVERIFIED"
  status_label: "OPEN/PARTIAL"
```

## 10. Matching artifact and remaining full-scope gap

The complete proof is stored in the matching create-only artifact:

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T06-57-55Z_relation-block-persistence-affine-quotient_b631.md`

created at commit

`5f9fbad7e45afe9dc5f651ce523f0b048c7f0ae1`

with blob

`92898f76c47884220fa5e2f6985091dc350c4c70`,

and read back at that exact commit before this report was written.

The full-source gap is now sharper. The multi-block theorem removes very sparse persistent localization but does **not** eliminate the moderate regime in which the invariant high-likelihood set has size at least about `n^(1/2)`; the affine stress geometry naturally falls on that side. A full solution still needs either:

1. a transitivity-based entropy/Green estimate ruling out fixed heat mass on every polynomially sublinear invariant relation, including the `a<=1/2` regime; or
2. an admissible counterexample family for which such moderate localization actually survives and produces a non-sharp TV profile.

For the explicit affine stress test, the next delimited nonduplicating obligation is now concrete: control the mixing-scale mutual information `I(M_t;Y_t)` and the L1 matrix coefficient of the perturbed slow vector. No source closure, novelty, or independent validation is claimed.