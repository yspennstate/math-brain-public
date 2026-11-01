Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum.** No authenticated runtime model/effort telemetry or binding GPT-6/maximum selector is exposed here.

# R7-01 admission screen — E0084 via the exact moving-window semigroup

**Decision:** `HARD/BROAD OUTSIDE / SUBSTANTIVE ANALYTIC REDUCTION / NOT_ADMITTED`.

**Slot state remains:** `PENDING_ADMISSION`; successor metric `UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`; stagnation `NOT_STARTED`; B2/B24/B11 uncharged because E0084 does not pass the CLOSABLE-source admission gate.

## 1. Candidate, shard, ownership

Canonical intake candidate: **E0084**, “A Dirichlet form for the spacetime shift process on Wiener space.”

Exact case-sensitive shard arithmetic:

```text
sum(ord(c) for c in "E0084") = 69+48+48+56+52 = 273,
273 mod 7 = 0.
```

Thus E0084 belongs to R7-01's initial shard. This is only a partition rule, not ownership.

At the pre-admission master snapshot `9c44bb6e9a3a82242652e025e60669edf7e03b2d`, `operations/claims/E0084.md` does not exist. The exact-ID repository search finds the intake/campaign copies and R7-01's earlier admission cursor, but no canonical E0084 claim. The 91-commit comparison from the preceding R7-01 creation commit `ee87b83e4fa452c9793a3fd4db716979fbb14d75` to that snapshot adds `operations/claims/SHPECTOROV-ZHAO-2026-SRG69.md` but no E0084 claim and no shared QUEUE/RESULTS/POSTED/campaign INDEX/RANKING mutation. Search misses are not treated as proof of global freedom or openness; this is only the repository ownership evidence available here.

## 2. Exact outside source and quantifiers

Primary source:

- Jim Pitman and Wenpin Tang,
- **“Patterns in Random Walks and Brownian Motion,”**
- arXiv:1411.0041 (2014); Springer, *Séminaire de Probabilités XLVII*, LNM 2137, copyright 2015,
- DOI `10.1007/978-3-319-18585-9_4`,
- source PDF `https://www.columbia.edu/~wt2319/Patterns.pdf`,
- Section 4, **Open Problem 2(2)**, printed p. 84 / PDF page 35.

The source defines the spacetime shift

\[
\Theta_t\circ B=(B_{t+u}-B_t;u\ge0)
\]

and the moving-window process

\[
X_t=(B_{t+u}-B_t;0\le u\le1).
\]

It defines

\[
\operatorname{Cap}_{MW}(S_\infty)
=\int_0^\infty e^{-t}
\Pr\{\exists T\in[0,t]:\Theta_T\circ B\in S_\infty\}\,dt,
\]

calls this a Choquet capacity associated with the shift/moving-window process, notes that the process is not time-reversible, and asks literally:

> “Propose a non-symmetric Dirichlet form for the shifted process ... which permits to compute the capacities of the sets of paths E, M, BR^lambda ... etc.”

The source immediately says that this problem is substantial already for one-dimensional Brownian motion. The required endpoint is therefore not merely “write a formal generator”: the form must support actual potential/capacity calculations for the named path families.

Wenpin Tang's 2017 Berkeley dissertation **“Continuous paths in Brownian motion and related problems”** repeats the same question as Open problem 6.0.8(2), with the same warning that the nonsymmetric Dirichlet-form approach is far from obvious. That is positive later-author evidence that the issue was still regarded as open in 2017.

## 3. Prior repository attempt and its correction

The intake attempt `E0084-A001` proposed “OU symmetric part + shift-generator antisymmetric part” and stated that the shift generator is a pure translation with no symmetric part in `L^2(Wiener)`.

The first statement is only a heuristic proposal; the second is false for the actual moving-window semigroup. The window loses old noise through a boundary and receives fresh independent noise through the other boundary. That produces an exact dissipative symmetric component. The calculation below makes it explicit.

## 4. Exact Gaussian representation of the moving-window semigroup

Let

\[
H=L^2(0,1)
\]

be the one-particle Gaussian space and let `mu` be Wiener measure on `C_0[0,1]`. Write

\[
W(h)=\int_0^1h(s)\,dB_s,
\qquad h\in H.
\]

Condition on the present unit Brownian window. For `0<=t<=1`, a first-chaos observable of the future window satisfies

\[
P_t W(h)=W(U_t h),
\]

where

\[
(U_t h)(r)=\mathbf 1_{\{r\ge t\}}h(r-t),\qquad 0\le r\le1.
\]

For `t>=1`, `U_t=0`. The operators `(U_t)_{t>=0}` form the nilpotent right-shift contraction semigroup on `H`:

\[
U_sU_t=U_{s+t},\qquad U_t=0\quad(t\ge1).
\]

The conditional covariance of the fresh part is exactly the missing covariance `I-U_t^*U_t`. Consequently, for the normalized Gaussian exponential vector

\[
\mathcal E_h=\exp\{W(h)-\tfrac12\|h\|_2^2\},
\]

one has the exact identity

\[
P_t\mathcal E_h=\mathcal E_{U_t h}.
\]

Thus on Wiener chaos

\[
\boxed{P_t=\Gamma(U_t)},
\]

the Gaussian second quantization of the killed right-shift semigroup. This is the natural Mehler/second-quantized representation of Pitman--Tang's moving window.

The one-particle generator is

\[
Ah=-h',
\qquad
D(A)=\{h\in H^1(0,1):h(0)=0\}.
\]

This already identifies the missing analytic structure much more precisely than the old OU-plus-skew ansatz.

## 5. Dense-core bilinear pre-form

For `h,k in D(A)`, differentiate the semigroup pairing on exponential vectors:

\[
\langle \mathcal E_h,\mathcal E_k\rangle
=e^{\langle h,k\rangle}.
\]

Define the generator pre-form on the exponential core by

\[
\mathfrak E(\mathcal E_h,\mathcal E_k)
:=-\left.\frac d{dt}\right|_{0+}
\langle P_t\mathcal E_h,\mathcal E_k\rangle.
\]

Using `P_t E_h=E_{U_t h}` gives

\[
\boxed{
\mathfrak E(\mathcal E_h,\mathcal E_k)
=-\langle Ah,k\rangle e^{\langle h,k\rangle}
=\left(\int_0^1h'(s)k(s)\,ds\right)e^{\langle h,k\rangle}.
}
\]

This is an exact non-symmetric bilinear pre-form associated with the source process on a dense Gaussian core. It is not yet asserted to be a quasi-regular classical nonsymmetric Dirichlet form; that analytic completion is one of the remaining gates.

## 6. The symmetric part is a boundary trace, not zero

Because every `h,k in D(A)` obeys `h(0)=k(0)=0`, integration by parts yields

\[
\frac12\left[
\mathfrak E(\mathcal E_h,\mathcal E_k)
+\mathfrak E(\mathcal E_k,\mathcal E_h)
\right]
=\frac12 h(1)k(1)e^{\langle h,k\rangle}.
\]

In particular,

\[
\boxed{
\mathfrak E(\mathcal E_h,\mathcal E_h)
=\frac12 h(1)^2 e^{\|h\|_2^2}.
}
\]

So the previous repository statement that the shift has “no symmetric part” is wrong. Infinitesimal dissipation is concentrated at the outgoing edge of the window. The bulk transport is skew; the loss of old noise/fresh-noise replacement appears as boundary energy.

This correction is important: the natural comparison is not with the bulk Malliavin/OU energy `int |Dh|^2`, but with a highly degenerate transport-plus-boundary structure.

## 7. Exact strong-sector obstruction

The classical strong-sector route fails for the natural pre-form. This can be certified by an explicit normalized sequence.

For `n>=1`, set

\[
h_n(s)=\sqrt2\sin(n\pi s),
\qquad
k_n(s)=\sqrt2\sin((n+1)\pi s).
\]

Then

\[
\|h_n\|_2=\|k_n\|_2=1,
\quad
\langle h_n,k_n\rangle=0,
\quad
h_n(0)=h_n(1)=k_n(0)=k_n(1)=0.
\]

Hence the diagonal symmetric energies vanish:

\[
\mathfrak E(\mathcal E_{h_n},\mathcal E_{h_n})
=\mathfrak E(\mathcal E_{k_n},\mathcal E_{k_n})=0,
\]

while the cross transport is

\[
\begin{aligned}
\int_0^1 h_n'(s)k_n(s)\,ds
&=2n\pi\int_0^1\cos(n\pi s)\sin((n+1)\pi s)\,ds\\
&=2n\left(1+\frac1{2n+1}\right).
\end{aligned}
\]

Because `||E_{h_n}||_2^2=||E_{k_n}||_2^2=e`, the usual shifted diagonal quantities

\[
\mathfrak E_1(u,u)=\mathfrak E(u,u)+\|u\|_2^2
\]

stay equal to `e`, but

\[
\mathfrak E_1(\mathcal E_{h_n},\mathcal E_{k_n})
=1+2n\left(1+\frac1{2n+1}\right)\to\infty.
\]

Therefore no uniform classical strong-sector estimate

\[
|\mathfrak E_1(u,v)|\le C
\mathfrak E_1(u,u)^{1/2}\mathfrak E_1(v,v)^{1/2}
\]

can hold on this natural core.

This is an exact analytic obstruction, not a numerical experiment. It points toward the **generalized/non-sectorial Dirichlet-form** framework rather than a standard sectorial Ma--Roeckner form.

## 8. Exact resolvent simplification

The moving window has a finite memory of length one. Once `t>=1`, the future unit window is independent of the present one, so for every `f in L^2(mu)`,

\[
P_t f=\mu(f),\qquad t\ge1.
\]

Hence for every `alpha>0`, its resolvent is exactly

\[
\boxed{
R_\alpha f
=\int_0^1e^{-\alpha t}\Gamma(U_t)f\,dt
+\frac{e^{-\alpha}}{\alpha}\mu(f).
}
\]

For centered `f`, the tail term vanishes and the resolvent is a finite integral over `0<=t<=1`. Thus the potential theory of the process is not obstructed by an infinite-memory semigroup; the hard point is the non-sectorial path-space analytic/capacity theory.

For a Borel target `S` and its first hitting time `tau_S`, the source's exponentially weighted hitting functional satisfies the elementary identity

\[
\int_0^\infty e^{-t}\Pr(\tau_S\le t)\,dt
=\mathbb E[e^{-\tau_S};\tau_S<\infty].
\]

So the source capacity is already a discounted hitting potential for this exact semigroup. What remains is to build the correct generalized form/capacity correspondence and then compute it for the source's named singular path sets.

## 9. Dated literature gate — 2026-09-19

Bounded checks covered the original/current source, later-author work and the nearest analytic literature.

- Tang's 2017 dissertation repeats exactly the same open problem as Open problem 6.0.8, so there is explicit later-author evidence that the problem persisted after the original chapter.
- Schmuland, **“Non-Symmetric Ornstein-Uhlenbeck Processes in Banach Space Via Dirichlet Forms”** (Canadian J. Math. 45 (1993), 1324--1338) develops nonsymmetric Dirichlet forms for Banach-space OU processes, but this is not Pitman--Tang's nilpotent moving-window transport semigroup.
- Stannat's generalized Dirichlet-form framework (Potential Analysis 8 (1998), 21--60) explicitly accommodates a coercive part plus unbounded drift and is structurally closer to the non-sectorial route indicated above.
- Beznea--Trutnau (arXiv:1012.2227) treats quasi-regularity for non-sectorial/generalized forms.
- Applebaum--van Neerven, **“Second quantisation for skew convolution products of measures in Banach spaces”** (EJP; arXiv:1305.5146), shows that Mehler/skew-convolution transition operators lift by second quantization, supporting the general mechanism used above.
- Pitman--Tang's later argmin-process work and Tang's later Brownian-path papers were found, but the bounded search did not recover a paper claiming the requested Dirichlet-form/capacity solution.

No direct 2018--2026 solution matching Open Problem 2(2) was found in the bounded exact-phrase, `CapMW`, moving-window and Dirichlet-form searches. **This search miss is not proof of openness or novelty.** The only safe status is `source-open-looking / later-author restatement / no matching closure found in bounded search`.

## 10. Why E0084 is not admitted to R7-01

The new calculations are substantial: they give the exact one-particle contraction, the second-quantized full semigroup, a dense-core nonsymmetric generator pre-form, the exact boundary symmetric part, an exact failure of the strong-sector inequality, and a finite-memory resolvent formula.

But the source endpoint is broader. To close it one must still, at minimum:

1. choose and prove the correct generalized/non-sectorial Dirichlet-form completion associated with `Gamma(U_t)`;
2. establish the required quasi-regularity/potential-theoretic identification on Wiener path space;
3. connect that analytic capacity rigorously to the source's `Cap_MW` hitting capacity;
4. actually compute capacities for source-listed singular sets such as `E`, `M`, and `BR^lambda` (or a source-acceptable family of them).

Those are theorem-sized obligations. The problem is therefore **HARD/BROAD**, not honestly CLOSABLE by a short counterexample, finite certificate, sharp finite constant, or complete short theorem. R7-01 should not capture it merely because the semigroup representation is clean.

No canonical claim is created.

## 11. Source-matching diagnostic and handoff

A source-matching diagnostic for any future worker is

`N_form-cap = number of source-listed families among {E, M, BR^lambda} for which a rigorous capacity value/criterion is derived from an associated completed form framework.`

Baseline: `UNKNOWN/UNMEASURED`. It is not set to zero by absence of evidence, and because E0084 is not admitted it does not become R7-01's frozen slot metric.

The strongest reusable handoff is:

- **exact semigroup:** `P_t=Gamma(U_t)` with `U_t h(r)=1_{r>=t}h(r-t)`;
- **generator:** `Ah=-h'`, `h(0)=0`;
- **core form:** `E(E_h,E_k)=int h'k * exp(<h,k>)`;
- **symmetric boundary energy:** `(1/2)h(1)k(1)exp(<h,k>)`;
- **strong-sector obstruction:** the sine pair above has bounded diagonal `E_1` but cross energy of order `n`;
- **resolvent:** finite-memory formula above.

These facts should be reused exactly rather than reverting to the incorrect “pure translation/no symmetric part” intake attempt.
