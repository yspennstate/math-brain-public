Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — full symmetric three-level AP entropy and false-twin dominance

Date: 2026-09-18 UTC.  
Track: `R7-07 Hard Problem New Methods`; native ID `6aabe8413f60819197825dd81ca138ae`.  
Canonical target: `F0003`. Status: **proved restricted theorem / PARTIAL relative to Vu's source question**.  
Captured run-start master: `0dd03c165b10ae27c7dfaf4fcb3285ca773eb7dd`.  
Fresh pre-artifact master: `678e22354f4a1b6515353d4f35af3646d6605ce1`.  
Newest actual own run report recovered: `research7_2026-09-17/R7-07/runs/2026-09-18/2026-09-18T160400Z__report.md` @ creation commit `6885d18dd5934c5a8ac3dea47e7c623f01232e08` (STUCK1).  
Intervening substantive artifact: `research7_2026-09-17/R7-07/artifacts/2026-09-18/2026-09-18T170300Z__F0003_three_level_undirected_contingency_and_balanced_mass.md` @ creation commit `aeca17df86a5b52cb3b36d7ca3da5e52a6983a0b`. No later own run report was recovered after that artifact: **HISTORY_GAP for the corresponding report, not for the mathematics in the artifact**.

This ordinary recovery-cycle iteration uses **B5 / B24 / B30**. The frozen source metric remains

\[
a_3:=\sup\{a:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\},
\qquad a_3\ge \frac14,
\]

so this artifact records **NO SOURCE-METRIC MOVEMENT**. The new result is nevertheless structural: within the entire symmetric three-level arithmetic-progression family, the normalized modular-null mass is asymptotically exhausted by the false-twin configurations that already predict the source's `n^{-1}` cubic scale.

## 1. Starting exact formula from the preceding artifact

Work first in the cubic configuration model on `n` labelled vertices, with `n` even. Let `Q>6` be coprime to `6`, and let `u` be a unit of `Z/QZ`. For

\[
1\le N\le \lfloor n/3\rfloor,
\]

consider modular rows whose coordinates take the three values `-u,0,u`, with exactly `N` coordinates equal to each of `-u` and `u`, and

\[
Z:=n-2N
\]

zero coordinates. Let `S^{AP}_{Q,N}(A)` be the number of **distinct** such surjective rows in the modular kernel of `A`. Scaling by the `phi(Q)` units acts freely, so

\[
U^{AP}_{Q,N}(A):=\frac{S^{AP}_{Q,N}(A)}{\varphi(Q)}
\]

is the number of unit-scaling orbits. Put

\[
U^{AP}_Q(A):=\sum_{N=1}^{\lfloor n/3\rfloor}U^{AP}_{Q,N}(A).
\]

The preceding artifact proved that the symmetric local contingency table has one integer parameter `x`. In the present notation its exact favorable-pairing contribution is

\[
T_{n,N,x}=
\binom Nx^2
\binom Z{N+2x}
6^{3N}
(N+2x)!^2
(N-x)!
((N-x-1)!!)^2
(D-1)!!,
\tag{1.1}
\]

where

\[
D:=3n-8N-4x.
\tag{1.2}
\]

The feasible set is

\[
\mathcal X_{n,N}:=
\left\{x\in\mathbb Z:\ 0\le x\le N,\quad N+2x\le Z,\quad N-x\equiv0\pmod2\right\}.
\tag{1.3}
\]

The number of distinct rows of this shape is

\[
\frac{\varphi(Q)}2\frac{n!}{N!^2Z!};
\]

the factor `1/2` is the exact identification

\[
(u,V_-,V_0,V_+)\leftrightarrow(-u,V_+,V_0,V_-).
\]

Consequently

\[
\boxed{
M_{n,N}:=\mathbb E_{\rm conf}U^{AP}_{Q,N}(A)
=
\frac12\frac{n!}{N!^2Z!}
\frac{1}{(3n-1)!!}
\sum_{x\in\mathcal X_{n,N}}T_{n,N,x}.
}
\tag{1.4}
\]

The right side no longer depends on `Q`. This exact formula is the input to all three methods below.

## 2. B5 — add the density parameter and derive the exact entropy rate

Set

\[
\alpha:=\frac Nn,\qquad \xi:=\frac xn.
\]

The continuous feasible region is

\[
0<\alpha\le\frac13,\qquad
0\le\xi\le\min\left\{\alpha,\frac{1-3\alpha}{2}\right\}.
\tag{2.1}
\]

Use, uniformly for integers `0<=m<=Cn`,

\[
\log(m!)=m\log m-m+O(\log(n+1)),
\]

with the usual `0 log 0=0`, and derive the corresponding double-factorial estimate from

\[
(2r-1)!!=\frac{(2r)!}{2^rr!}.
\]

Applying these identities to the single summand in (1.4), including the outer multinomial factor, cancels every `n log n` term. The remaining exponential rate is

\[
\begin{aligned}
R(\alpha,\xi)
={}&\alpha\log(\alpha+2\xi)
-4\alpha\log(3-8\alpha-4\xi)
+3\alpha\log(1-3\alpha-2\xi)
+3\alpha\log6\\
&-2\xi\log\xi
+2\xi\log(\alpha+2\xi)
-2\xi\log(3-8\alpha-4\xi)
+2\xi\log(1-3\alpha-2\xi)\\
&+\frac32\log(3-8\alpha-4\xi)
-\log(1-3\alpha-2\xi)
-\frac32\log3.
\end{aligned}
\tag{2.2}
\]

All boundary values below are interpreted by continuous extension.

### Lemma 2.1 — unique entropy maximizer in `x`

For every `0<alpha<1/3`, `R(alpha,xi)` has a unique maximizer on (2.1), namely

\[
\boxed{\xi_*(\alpha)=\alpha(1-3\alpha).}
\tag{2.3}
\]

#### Proof

Direct differentiation gives

\[
\frac{\partial R}{\partial\xi}
=2\log\left(
\frac{(\alpha+2\xi)(1-3\alpha-2\xi)}
{\xi(3-8\alpha-4\xi)}
\right).
\tag{2.4}
\]

The difference between the numerator and denominator inside the logarithm simplifies **exactly**:

\[
(\alpha+2\xi)(1-3\alpha-2\xi)
-\xi(3-8\alpha-4\xi)
=\alpha(1-3\alpha)-\xi.
\tag{2.5}
\]

Therefore the derivative is positive for `xi<alpha(1-3alpha)`, zero there, and negative afterwards. Moreover

\[
\alpha(1-3\alpha)\le\alpha,
\qquad
\alpha(1-3\alpha)\le\frac{1-3\alpha}{2}
\]

because `alpha<=1/3<1/2`. Hence (2.3) lies in the feasible region and is the unique maximizer. ∎

Substituting (2.3) into (2.2) yields a one-variable rate:

\[
\boxed{
R_*(\alpha)
=\alpha\log(8\alpha)
+(2-4\alpha)\log(1-2\alpha)
+(3\alpha-1)\log(1-3\alpha).
}
\tag{2.6}
\]

At `alpha=1/3`, the continuous value is

\[
R_*(1/3)=\log(2/3),
\]

recovering the balanced-profile base from the preceding run.

### Lemma 2.2 — every positive-density AP profile has a strict entropy gap

For every `0<alpha<=1/3`,

\[
\boxed{R_*(\alpha)<0.}
\tag{2.7}
\]

In fact `R_*` is strictly decreasing from `R_*(0+)=0`.

#### Proof

Differentiate (2.6):

\[
R_*'(\alpha)
=
\log\left(
\frac{8\alpha(1-3\alpha)^3}{(1-2\alpha)^4}
\right),
\tag{2.8}
\]

and

\[
R_*''(\alpha)
=-\frac{6\alpha-1}
{\alpha(2\alpha-1)(3\alpha-1)}.
\tag{2.9}
\]

On `(0,1/3)`, the denominator in (2.9) is positive. Thus `R_*'` increases until `alpha=1/6` and decreases afterwards. Its global maximum is therefore

\[
R_*'(1/6)
=\log(27/32)<0.
\]

Hence `R_*'<0` throughout `(0,1/3)`. Since `R_*(0+)=0`, (2.7) follows. ∎

The argument can be sharpened to an explicit bound useful at vanishing density.

### Lemma 2.3 — a uniform sparse-to-dense upper envelope

For `0<alpha<=1/3`,

\[
\boxed{
R_*(\alpha)
\le \alpha\log\alpha +(3\log2-1)\alpha
=\alpha\log\left(\frac{8\alpha}{e}\right).
}
\tag{2.10}
\]

#### Proof

Subtract the right side from (2.6) and call the difference `H(alpha)`. Then `H(0+)=0` and

\[
H'(\alpha)
=3\log(1-3\alpha)-4\log(1-2\alpha)
=\log\frac{(1-3\alpha)^3}{(1-2\alpha)^4}.
\tag{2.11}
\]

The ratio inside the last logarithm equals `1` at zero and has logarithmic derivative

\[
-\frac9{1-3\alpha}+\frac8{1-2\alpha}
=\frac{-1-6\alpha}{(1-3\alpha)(1-2\alpha)}<0.
\]

Thus the ratio is `<1` for every positive `alpha`, so `H'<0` and `H<=0`. ∎

Since there are at most `n+1` feasible `x` values and only a fixed number of factorial factors, the uniform Stirling errors in (1.4) can be absorbed into one polynomial. Therefore there is an absolute constant `C` such that

\[
\boxed{
M_{n,N}
\le n^C\exp\{nR_*(N/n)\}
\le n^C\left(\frac{8N}{en}\right)^N.
}
\tag{2.12}
\]

The exact value of `C` is irrelevant for the scale separation below.

## 3. B24 — identify the extremal sparse object exactly

The rate (2.6) tends to zero only when `N/n -> 0`, so the extremal AP configurations must live at the sparse boundary. For fixed `N`, (1.4) can be expanded exactly enough to identify the leading scale.

### Theorem 3.1 — fixed-`N` asymptotic

For every fixed integer `N>=1`,

\[
\boxed{
M_{n,N}=C_Nn^{-N}(1+o(1)),
}
\tag{3.1}
\]

where

\[
\boxed{
C_N=
\frac{6^{3N}}{2(N!)^2}
\sum_{\substack{0\le x\le N\\x\equiv N\ (2)}}
\binom Nx^2
\frac{(N+2x)!(N-x)!((N-x-1)!!)^2}{3^{4N+2x}}.
}
\tag{3.2}
\]

In particular

\[
\boxed{C_1=\frac89.}
\tag{3.3}
\]

#### Proof

Fix `N,x`. Since `Z=n-2N`,

\[
\frac{n!}{Z!}=n^{2N}(1+o(1)),
\qquad
\binom Z{N+2x}
=\frac{n^{N+2x}}{(N+2x)!}(1+o(1)).
\]

Also `D=3n-8N-4x`, so the double-factorial ratio removes exactly `4N+2x` odd factors:

\[
\frac{(D-1)!!}{(3n-1)!!}
=(3n)^{-(4N+2x)}(1+o(1)).
\]

Substitution into (1.4) leaves the power

\[
n^{2N}n^{N+2x}n^{-(4N+2x)}=n^{-N}
\]

and the constant in (3.2). The sum has finitely many terms. For `N=1`, parity forces `x=1`, and (3.2) gives `C_1=8/9`. ∎

The `N=1` object has a direct graph-theoretic meaning.

### Lemma 3.2 — `N=1` is exactly a false-twin pair

Let `A` be the adjacency matrix of a simple cubic graph and `Q>2`. A row in the `N=1` AP family has the form

\[
y=u(e_i-e_j)
\]

up to sign, with `u` a unit. Then

\[
yA=0\pmod Q
\]

if and only if vertices `i,j` are nonadjacent and have the same three neighbours.

#### Proof

Because `u` is invertible, `yA=0` is equivalent to equality modulo `Q` of rows `i` and `j` of `A`. Their coordinate differences lie in `{-1,0,1}`, so for `Q>2` modular equality is ordinary equality. Equal rows in a loopless simple graph force `i,j` to be nonadjacent and to have identical neighbourhoods. Conversely identical neighbourhoods make the rows equal. ∎

Every unordered false-twin pair contributes exactly `phi(Q)` scaled modular rows, hence

\[
U^{AP}_{Q,1}(A)=\#\{\text{false-twin vertex pairs of }A\}.
\tag{3.4}
\]

Combining (3.1)--(3.4),

\[
\boxed{
\mathbb E_{\rm conf}[\#\text{ false-twin pairs}]
\sim\frac{8}{9n}.
}
\tag{3.5}
\]

The same leading constant holds in the uniform **simple** cubic model. Indeed, conditioned on a fixed false-twin pair and its three common neighbours, the six twin-neighbour edges are simple and the remaining configuration has degree sequence

- three vertices of residual degree `1`,
- `n-5` vertices of residual degree `3`.

For this residual bounded degree sequence,

\[
\nu_n:=\frac{\sum_vd_v(d_v-1)}{\sum_vd_v}
=\frac{6n-30}{3n-12}\longrightarrow2.
\]

The standard bounded-degree configuration-model simplicity formula gives limiting simplicity probability

\[
\exp(-\nu/2-\nu^2/4)=e^{-2},
\]

the same limit as for the original cubic configuration model. Therefore conditioning on simplicity changes the false-twin probability by a factor `1+o(1)`, and

\[
\boxed{
\mathbb E_{\rm simple}[\#\text{ false-twin pairs}]
\sim\frac{8}{9n}.
}
\tag{3.6}
\]

This use of the standard simplicity theorem is only a transfer from configuration to simple graphs; the new enumeration above is exact before that transfer.

## 4. B30 — localize the AP family by scale and glue the pieces

We now show that the sparse false-twin object is not merely one contribution: it asymptotically exhausts **the entire symmetric three-level AP family** after the natural unit-orbit normalization.

### Theorem 4.1 — false twins dominate all symmetric AP modular null rows

For any sequence of moduli `Q=Q(n)>6` coprime to `6`,

\[
\boxed{
\mathbb E_{\rm conf}U^{AP}_Q(A)
=\frac{8}{9n}+o(n^{-1}).
}
\tag{4.1}
\]

For the uniform simple cubic graph,

\[
\boxed{
\mathbb E_{\rm simple}U^{AP}_Q(A)
=\frac{8}{9n}+o(n^{-1}).
}
\tag{4.2}
\]

In particular, all AP profiles with `N>=2` contribute only `o(n^{-1})` in total.

#### Proof

The `N=1` term is (3.5) in the configuration model and (3.6) in the simple model.

It remains to sum `N>=2`. Fix a large constant `K`, to be chosen after the polynomial exponent `C` in (2.12).

**Fixed sparse range `2<=N<K`.** For each fixed `N`, Theorem 3.1 gives `M_{n,N}=O(n^{-N})`; hence the whole finite range is `O(n^{-2})`.

**Mesoscopic range `K<=N<=sqrt(n)`.** By (2.12),

\[
M_{n,N}
\le n^C\left(\frac{8}{e\sqrt n}\right)^N.
\]

After summing at most `n` values of `N`, choosing `K` sufficiently large in terms of `C` makes this `o(n^{-1})`.

**Macroscopic range `sqrt(n)<N<=n/3`.** Again from (2.12),

\[
M_{n,N}
\le n^C\left(\frac{8}{3e}\right)^N,
\]

and `8/(3e)<1`. Summing at most `n` values gives `n^{C+1}exp(-c sqrt(n))=o(n^{-1})` for some `c>0`.

Thus

\[
\sum_{N=2}^{\lfloor n/3\rfloor}M_{n,N}=o(n^{-1}),
\]

which proves (4.1).

For the simple model, the total `N>=2` contribution is at most the configuration-model expectation divided by `P_conf(simple)`, and `P_conf(simple)->e^{-2}>0`; hence it is still `o(n^{-1})`. Combine with (3.6) to obtain (4.2). ∎

### Corollary 4.2 — the source-predicted cubic obstruction is exact inside this whole three-level family

The source-level primitive-null-vector/cokernel reduction uses the normalized surjection mass `S_Q/phi(Q)`. Theorem 4.1 says that, within the full symmetric AP subfamily,

\[
\boxed{
\mathbb E\frac{S^{AP}_Q(A)}{\varphi(Q)}
\sim\frac{8}{9n},
}
\tag{4.3}
\]

and that the leading term comes **only** from false twins. Thus this entire low-alphabet family reproduces the conjectured cubic `n^{-1}` scale rather than creating a larger obstruction.

This is a restricted theorem. It does **not** prove that every modular null row with support at least three is AP-shaped, and therefore it does not prove the source endpoint `a_3=1` or even the intermediate all-profile `1/3` bound.

## 5. What moved mathematically, and what did not

The frozen source metric does not move:

\[
\boxed{a_3\ge1/4\longrightarrow a_3\ge1/4\qquad\text{NO MOVEMENT}.}
\]

However, the post-STUCK1 recovery did move the structural frontier in two concrete ways:

1. the preceding B22/B18/B9 artifact solved the single balanced three-level profile and produced the exact contingency formula;
2. the present B5/B24/B30 run solves **all symmetric three-level arithmetic-progression profiles simultaneously**, from fixed support through mesoscopic and positive density, and shows the normalized total is asymptotically `8/(9n)`, entirely false-twin dominated.

The remaining `(BLOCK)` from STUCK1 is now narrower in a meaningful sense: any obstruction larger than the source-predicted twin scale must come from **non-AP support-three rows or support at least four**, or from the growing-support regime. The exact global blocker remains

\[
\mathbb E S_Q^{(\ge3)}(A_{n,3})\le n^{o(1)}
\quad\text{for some }Q=n^{1/3-o(1)},
\]

but the symmetric AP component has now been removed at much greater precision than this bound requires.

## 6. Dated source/literature boundary

Checked 2026-09-18 UTC.

- Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020; Probability Surveys 2021), remains the retained outside source and sharp-rate target used by the canonical claim.
- Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461, published in *European Journal of Combinatorics* (2024), obtains the directed `n^{-1/3+o(1)}` scale through modular singularity and inverse characteristic-function/Kneser analysis. Its directed exposure factorization is not silently imported into the undirected model.
- Yukun He and Jiaoyang Huang, *The oriented Kesten--McKay law for random regular digraphs*, arXiv:2609.05297 (submitted 2026-09-04), proves directed hard-edge/small-ball estimates using finite-field anticoncentration. It is again a directed result, not a source-level resolution of Vu's undirected sharp exponent.
- The standard bounded-degree configuration-model simplicity asymptotic used only in (3.6) is classical; Janson's *The Probability That a Random Multigraph is Simple* (CPC 2009) gives a general formulation.

A fresh bounded search found no later theorem settling the **undirected fixed-degree sharp singularity decay exponent**. This is negative evidence only, not a novelty certificate or proof of openness.

## 7. Next nonrepeating attack

The immediately preceding ordinary triple was B22/B18/B9; this run used B5/B24/B30. If the next run remains on F0003, use three different moves:

1. **B15 — BREAK THE SYMMETRY ON PURPOSE.** Replace `{-u,0,u}` by a general three-residue support, normalize one residue by unit scaling, and determine exactly which additive resonances permit local zero-sum degree-three multisets.
2. **B14 — FIND THE GROUP ACTING.** Quotient general support-three rows by the unit action and classify the residual ratio parameter into resonance orbits rather than summing `Q^3` raw triples.
3. **B25 — COUNT THE SAME THING TWICE.** For each resonance class, combine the exact symmetric contingency formula with the row-profile multinomial entropy and decide whether the complete support-three orbit mass is `O(n^{-1})`, `o(1)`, or contains a genuinely new obstruction.

The clean next finite milestone is therefore: **sum all support-exactly-three surjective modular null rows, not only the arithmetic-progression family, at growing squarefree modulus.**
