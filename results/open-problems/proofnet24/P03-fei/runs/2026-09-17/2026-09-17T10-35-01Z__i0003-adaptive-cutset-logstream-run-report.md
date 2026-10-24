Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed scheduler/runtime provides no model-family selector, no reasoning-effort selector, and no authenticated routing receipt; I therefore do not claim GPT-6 or maximum reasoning. **NO MOVEMENT in the active metric: `eta_stream^cert = 1/2 -> 1/2`; post-movement unchanged streak `1 -> 2`. Methods used: #3 PROVE SOMETHING STRONGER, #13 FIND WHAT ONLY INCREASES, #28 REPLACE FOR ALL WITH TYPICAL.**

# P03 / I0003 run report — adaptive cutset resistance and a recurrent deterministic `M(R)=Theta(log R)` field

Run date: 17 September 2026 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Track: P03 / HARD OUTSIDE.  
Canonical claim: `operations/claims/I0003.md`.  
Source: Ahmed Bou-Rabee and Yuval Peres (2026), *The randomly oriented Manhattan lattice in 2D is transient*, arXiv:2609.07621v1, Section 7, Problem 3.  
Broad source status after this run: **OPEN / PARTIAL**.

The saturated inherited coverage metrics remain

- `periodic_scope_certified = 1`,
- `bounded_discrepancy_scope_certified = 1`.

The active quantitative metric remains

\[
\eta_{\rm stream}^{\rm cert}=\frac12,
\]

where `eta_stream^cert >= eta` means that every exact-source deterministic field with anchored stream envelope `M(R)=O((log(2+R))^gamma)` is proved recurrent for every fixed `gamma<eta`. The previous two P03 theorems already prove more than this fixed-power summary records: first `M(R)=o(sqrt(log R))`, then the annular-resistance criterion, including the endpoint `M(R)=O(sqrt(log R))` and iterated-log enlargements.

This run does **not** prove a universal fixed-power exponent bigger than `1/2`, so the active metric correctly does not move. It does prove a genuinely stronger two-dimensional sufficient criterion and an explicit exact-source recurrent family with

\[
M(R)=\Theta(\log R),
\]

for which the preceding square-annular criterion itself fails. Thus the theorem is real source-scope progress even though the frozen universal exponent is unchanged.

New claims:

- `P03-I0003-ADAPTIVE-CUTSET-RESISTANCE-238 = PROVED / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-I0003-SELF-MATCHED-LOGSTREAM-239 = PROVED / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

No checker was created: both claims are analytic infinite-volume statements with complete proofs below and no finite computational core.

---

## 1. Continuity, ownership, and source gate

I continued from the newest complete P03 report rather than restarting:

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T09-43-43Z__i0003-annular-stream-resistance-run-report.md`, creation commit `1ce00a9b7b2e5c26b0aacb35d255bc9da38e76ca`, blob `9b6a01fa7f76705223ae6ac76361147c7d0c8aaa`, together with its immutable proof supplement

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T09-46-50Z__i0003-annular-proof-supplement.md`.

Before the new attack I reread/recovered the required controlling repository surfaces: root `README.md`; `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`; current `FLEET_RULES.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the canonical `operations/claims/I0003.md`; the newest same-source I0002 report (`runs/R12/2026-09-17T09-30-29Z_i0002_likelihood_bridge_05_3e7b91.md`); the separate I0004 ownership reservation only to preserve scope; and the newest P04/I0101 report needed for the directed audit. Large repository/intake surfaces are connector-bounded when rendered wholesale; I recovered the exact relevant rows and dependencies and do **not** describe that as a literal byte-for-byte reread of every unrelated intake row.

Ownership remains exclusive to P03 for broad Problem 3. I0004 remains separate and was not touched. The current exclusion registers do not mark I0003 as posted, source-exact closed, or retired.

Fresh source/status check on 17 September 2026: arXiv still exposes Bou-Rabee--Peres as v1 from 7 September 2026. SciRate's current listing still shows zero `scites`. Bounded fresh searches for the exact paper title/arXiv number combined with `deterministic recurrence`, `orientation fields`, `Nash-Williams`, `stream function`, and `non-reversible recurrence` did not locate a later source-matching classification or the criteria proved below. This is dated negative evidence only, **not** proof of worldwide openness or novelty.

Relevant prior art retained rather than relabelled:

- Gaudillière--Landim, *A Dirichlet principle for non reversible Markov chains and some recurrence theorems* (arXiv:1111.2445; later PTRF): the nonreversible capacity variational principle and recurrence applications;
- classical Nash--Williams cutset resistance for reversible electrical networks;
- non-symmetric Dirichlet-form recurrence under sector/comparison hypotheses (including the Beznea--Cîmpean--Röckner line used in the bounded-stream P03 theorem);
- Deuschel--Kösters bounded-cycle representation and older oriented/stratified-lattice work;
- Bou-Rabee--Peres's source facts: counting measure is invariant and the symmetric part is planar simple random walk.

The new step is the exact source-model comparison network plus the adaptive cutset and explicit self-matching construction. Publication novelty remains **UNVERIFIED**.

---

## 2. Exact inherited setup

Use the embedded rate-one normalization already fixed in P03:

\[
(Pf)(x,y)=\frac12 f(x+a_y,y)+\frac12 f(x,y+b_x),
\qquad a_y,b_x\in\{-1,1\},
\]

with `L=P-I`. Choose anchored primitives

\[
\alpha_0=\beta_0=0,
\qquad
\alpha_y-\alpha_{y-1}=a_y,
\qquad
\beta_x-\beta_{x-1}=b_x,
\]

and the face stream

\[
\psi_{x,y}=\frac{\alpha_y-\beta_x}{4}.
\]

For finitely supported `F`, let

\[
D(F)=\frac14\sum_{e}(\nabla_eF)^2
\]

be the planar simple-random-walk Dirichlet energy, and

\[
W_\psi(F)=\sum_q\psi_q^2E_q(F)
\]

be the weighted face energy from the preceding report. The weighted face-sector calculation and the exact finite-volume Gaudillière--Landim min-max gave, for every finite exterior set `B`,

\[
\operatorname{cap}_L(\{0\},B)
\le
\inf_{F(0)=1,\;F|_B=0}
\left[2D(F)+16W_\psi(F)\right].
\tag{2.1}
\]

This run starts from (2.1); it does not repay its proof.

---

## 3. Idea before code; refutation-first outcome

The live obstruction after Claim 236 was that square-radial trial potentials can overpay permanently for old high-stream strips. I first tried to make that overpayment sharp by constructing a deterministic field whose square-annular series converges and hoping to turn it into a transient example.

The construction did the opposite: because the stream has special additive form `alpha_y-beta_x`, one can build **non-square separating contours which self-match the two one-dimensional primitives** and keep the stream uniformly small on the contour even while the global envelope grows like `log R`.

That failure of the transience attack exposed the correct stronger statement: the nonreversible walk is dominated, in capacity, by an explicit reversible weighted network, so **any** divergent Nash--Williams family of low-average-stream cutsets proves recurrence. Square boundaries are only one possible cutset family.

This is method #3: prove the stronger comparison theorem rather than improve the old radial estimate one constant at a time.

---

## 4. `P03-I0003-ADAPTIVE-CUTSET-RESISTANCE-238`

### 4.1 The exact comparison network

Every undirected nearest-neighbor edge `e` belongs to exactly two unit faces, denoted `q_1(e),q_2(e)`. Regrouping the face energy gives

\[
W_\psi(F)
=
\sum_e
\bigl(\psi_{q_1(e)}^2+\psi_{q_2(e)}^2\bigr)
(\nabla_eF)^2.
\tag{4.1}
\]

Define reversible comparison conductances

\[
\boxed{
C_\psi(e)
:=1+32\bigl(\psi_{q_1(e)}^2+\psi_{q_2(e)}^2\bigr).
}
\tag{4.2}
\]

Then the standard reversible Dirichlet energy of this network is exactly

\[
\mathcal E_{C_\psi}(F)
:=\frac12\sum_e C_\psi(e)(\nabla_eF)^2
=2D(F)+16W_\psi(F).
\tag{4.3}
\]

Consequently (2.1) becomes the clean capacity comparison

\[
\boxed{
\operatorname{cap}_L(\{0\},B)
\le
\operatorname{cap}_{C_\psi}(\{0\},B)
}
\tag{4.4}
\]

for every finite-volume exterior `B`, with identical boundary values.

This is stronger than the square-annular estimate because the right side minimizes over **all two-dimensional potentials**, not only square-radial ones.

### 4.2 Adaptive Nash--Williams criterion

Let `Gamma_k` be pairwise edge-disjoint simple dual-lattice circuits surrounding the origin. Let `Cut(Gamma_k)` be the crossed primal edges. Put

\[
\mathcal C_k
=
\sum_{e\in\operatorname{Cut}(\Gamma_k)}C_\psi(e).
\tag{4.5}
\]

Classical Nash--Williams in the reversible comparison network gives

\[
R_{C_\psi}(0,\infty)
\ge
\sum_k\frac1{\mathcal C_k}.
\tag{4.6}
\]

Therefore, if

\[
\boxed{
\sum_k\frac1{\mathcal C_k}=\infty,
}
\tag{4.7}
\]

then the comparison network is recurrent and its point-to-infinity capacities vanish. By (4.4), the nonreversible Manhattan capacities vanish as well. If the directed Manhattan graph is strongly connected (for example if each of the two sign sequences takes both signs arbitrarily far in both tails), the walk is recurrent.

This proves the main comparison theorem.

### 4.3 Method #28: a typical-contour version

Write

\[
L_k=|\operatorname{Cut}(\Gamma_k)|,
\qquad
\overline{\Psi_k^2}
=
\frac1{L_k}
\sum_{e\in\operatorname{Cut}(\Gamma_k)}
\bigl(\psi_{q_1(e)}^2+\psi_{q_2(e)}^2\bigr).
\]

Then

\[
\mathcal C_k
=L_k\bigl(1+32\overline{\Psi_k^2}\bigr).
\]

Hence the genuinely `typical-angle` sufficient condition is

\[
\boxed{
\sum_k
\frac1{L_k[1+32\overline{\Psi_k^2}]}
=\infty
\quad\Longrightarrow\quad
\text{recurrence}.
}
\tag{4.8}
\]

No supremum of `|psi|` over an enclosing box appears. High-stream faces may be ignored if the separating contour can route around them.

### 4.4 Recovery of Claim 236

Choosing `Gamma_k` to be successive square dual boundaries recovers a Nash--Williams form of the previous annular theorem (up to a harmless fixed normalization factor), because the total comparison conductance of the square cutset is

\[
(8r+4)+32\Xi_r=2A_r.
\]

Thus Claim 238 strictly generalizes the *method* of Claim 236: square boundaries are one admissible cutset family, not a frozen geometry.

---

## 5. Method #13 — the monotone object is the comparison resistance, not the original drift

The original directed walk has no useful monotonicity under flipping oriented lines: a line flip can cancel stream on one region and increase it elsewhere. The correct monovariant is the reversible comparison network.

If two anchored streams satisfy

\[
\psi_{q_1(e)}^2+\psi_{q_2(e)}^2
\le
\widetilde\psi_{q_1(e)}^2+\widetilde\psi_{q_2(e)}^2
\qquad\text{for every edge }e,
\tag{5.1}
\]

then

\[
C_\psi(e)\le C_{\widetilde\psi}(e).
\]

Rayleigh monotonicity gives

\[
R_{C_\psi}(0,\infty)
\ge
R_{C_{\widetilde\psi}}(0,\infty),
\qquad
\operatorname{cap}_{C_\psi}\le\operatorname{cap}_{C_{\widetilde\psi}}.
\tag{5.2}
\]

So recurrence certificates transfer **downward in pointwise squared stream**. This is the exact monotone quantity found in method #13. I do not claim that the actual nonreversible recurrence property is monotone under arbitrary line defects; only the proved comparison certificate has this order.

---

## 6. `P03-I0003-SELF-MATCHED-LOGSTREAM-239`

The adaptive criterion is useful only if it can certify fields which the radial criterion cannot. This section gives an exact-source deterministic family where that happens.

### 6.1 A one-dimensional triangular primitive

For `k>=1`, set

\[
H_k=\lceil\log(k+2)\rceil
\]

(natural logarithm; changing the base only changes constants), and define block start locations

\[
N_1=0,
\qquad
N_{k+1}=N_k+2H_k.
\tag{6.1}
\]

Define `s_n` for nonnegative integers by a triangular excursion on each block:

\[
s_{N_k+t}=t,
\qquad 0\le t\le H_k,
\tag{6.2}
\]

and

\[
s_{N_k+H_k+t}=H_k-t,
\qquad 0\le t\le H_k.
\tag{6.3}
\]

The two formulas agree at the peak and the endpoint, and consecutive values differ by exactly `1` in absolute value. Extend symmetrically by

\[
s_{-n}=s_n.
\tag{6.4}
\]

Now define the Manhattan line orientations by

\[
a_y=s_y-s_{y-1},
\qquad
b_x=s_x-s_{x-1}.
\tag{6.5}
\]

Every `a_y,b_x` is exactly `+1` or `-1`, so this is an exact fully line-oriented source environment. Its anchored primitives are simply

\[
\alpha_y=s_y,
\qquad
\beta_x=s_x,
\]

and therefore

\[
\psi_{x,y}=\frac{s_y-s_x}{4}.
\tag{6.6}
\]

Because `H_k` is nondecreasing and

\[
N_k=2\sum_{j<k}H_j=\Theta(k\log k),
\tag{6.7}
\]

we have

\[
\boxed{M(R)=\Theta(\log R).}
\tag{6.8}
\]

Indeed `s_n` never exceeds the current block height `O(log n)`, while every completed block attains height comparable to `log R` before the next block scale.

### 6.2 Low-stream self-matching dual circuits

Fix a large block `k` and abbreviate `N=N_k`, `H=H_k`. For every `|x|<=N`, all earlier blocks have height at most `H`, hence

\[
0\le s_x\le H.
\]

On the ascending half of block `k`,

\[
s_{N+t}=t,
\qquad 0\le t\le H.
\]

Therefore

\[
\boxed{s_{N+s_x}=s_x}
\tag{6.9}
\]

for every `|x|<=N`; by symmetry also

\[
s_{-N-s_x}=s_x.
\tag{6.10}
\]

Construct a dual-lattice circuit around `[-N,N]^2` from four graph sides:

- top: `y=N+s_x`, `-N<=x<=N`;
- right: `x=N+s_y`, `-N<=y<=N`;
- bottom: `y=-N-s_x`, `-N<=x<=N`;
- left: `x=-N-s_y`, `-N<=y<=N`.

Consecutive graph points differ by `(1,+/-1)` or its rotated analog because `|s_{n+1}-s_n|=1`. Replace each diagonal move by the two corresponding nearest-neighbor dual steps. Choose the consistent outward staircase at each corner. Each side is monotone in its longitudinal coordinate, the four sides lie in the four exterior strips and meet only at the intended corners, so this is a simple dual circuit surrounding the origin.

At every graph vertex on the top side, (6.9) gives `s_y=s_x`, hence `psi=0`. At an intermediate staircase vertex one coordinate has moved by one while the other has not, so the 1-Lipschitz property of `s` gives

\[
|s_y-s_x|\le1,
\qquad
|\psi|\le\frac14.
\tag{6.11}
\]

The same holds on all four sides. Every crossed primal edge therefore has both adjacent face-stream values bounded by `1/4`, so

\[
C_\psi(e)
\le
1+32\left(\frac1{16}+\frac1{16}\right)
=5.
\tag{6.12}
\]

Each of the four sides uses at most `4N` dual edges, hence the total comparison conductance of the cutset is at most

\[
\boxed{\mathcal C_k\le80N_k.}
\tag{6.13}
\]

The circuit for block `k` lies between sup-norm radii `N_k` and `N_k+H_k+1`. Since

\[
N_{k+1}=N_k+2H_k,
\]

the circuits are pairwise edge-disjoint after discarding finitely many initial blocks.

Finally, from `N_k=Theta(k log k)`,

\[
\sum_k\frac1{N_k}=\infty.
\tag{6.14}
\]

Equations (4.7), (6.13), and (6.14) show that the comparison network is recurrent.

### 6.3 Strong connectivity of the directed source walk

Every triangular block has a long ascending run (`a=+1`) and descending run (`a=-1`), and this occurs arbitrarily far in both tails; the same is true for `b`. Hence each sign occurs arbitrarily far in each of the four one-dimensional tails.

For completeness, here is the standard four-segment path argument. Given `(x,y)` and target `(x',y')`, let `d=b_{x'}`. Along the current row move far in the allowed horizontal direction `a_y` to a column `c` with `b_c=-d`; such columns occur arbitrarily far in that halfline. Choose `c` past `x'` in that same direction. Move vertically from `y` along column `c` far in direction `-d` to a row `r` with `a_r=-a_y`; choose it beyond `y'` on the side from which direction `d` on column `x'` reaches `y'`. Then row `r` points horizontally from `c` back toward `x'`, so move to column `x'`; finally column `x'` points in direction `d` from `r` to `y'`. Thus every vertex reaches every other vertex.

The directed Manhattan chain is irreducible. The vanishing capacity obtained from the recurrent comparison network therefore gives recurrence of the exact source walk.

We have proved

\[
\boxed{
M(R)=\Theta(\log R)
\quad\text{and the exact deterministic Manhattan walk is recurrent.}
}
\tag{6.15}
\]

This proves Claim 239.

---

## 7. The previous square-annular theorem really misses this recurrent field

To show that Claim 238 is not just a reformulation of Claim 236, I now verify that the exact square-annular resistance series from Claim 236 **converges** for the field above.

Let `r` be large and choose `k` with

\[
N_k\le r<N_{k+1}.
\]

Put `c=s_r`. Consider any completed block `j<k`. On its ascending half, `s` takes the values `0,1,...,H_j`, so for every real `c`,

\[
\sum_{t=0}^{H_j}(t-c)^2
\ge
\min_u\sum_{t=0}^{H_j}(t-u)^2
=
\frac{H_j(H_j+1)(H_j+2)}{12}
\ge
\frac{H_j^3}{12}.
\tag{7.1}
\]

For all `j` between `floor(k/2)` and `k-1`,

\[
H_j\asymp\log k,
\]

and there are order `k` such completed blocks. Therefore

\[
\sum_{y=0}^{r}(s_y-s_r)^2
\ge c_1 k(\log k)^3.
\tag{7.2}
\]

Now inspect only the right-hand square-boundary crossing edges

\[
e_y=\{(r,y),(r+1,y)\},
\qquad 0\le y\le r.
\]

One adjacent face has lower-left corner `(r,y)`, so by (6.6)

\[
\psi_{r,y}^2=\frac{(s_y-s_r)^2}{16}.
\]

Hence the Claim-236 annular mass satisfies

\[
\Xi_r
\ge
\frac1{16}\sum_{y=0}^{r}(s_y-s_r)^2
\ge c_2 k(\log k)^3.
\tag{7.3}
\]

Since `r=Theta(k log k)` and `log r=Theta(log k)`, this becomes

\[
\Xi_r\ge c_3 r(\log r)^2.
\tag{7.4}
\]

Thus the square-annular coefficient

\[
A_r=\frac{8r+4}{2}+16\Xi_r
\]

satisfies

\[
A_r\ge c_4 r(\log r)^2
\]

for all large `r`. Consequently

\[
\boxed{
\sum_r\frac1{A_r}<\infty.
}
\tag{7.5}
\]

So the preceding square-annular sufficient condition cannot certify this field, while the adaptive cutset theorem does. This is strict improvement **inside the exact source model**, not only for an abstract weighted network.

The simpler global-envelope corollary of Claim 236 also fails here because `M(R)=Theta(log R)` makes

\[
\sum_r\frac1{r[1+M(r)^2]}
\asymp
\sum_r\frac1{r(\log r)^2}<\infty.
\]

---

## 8. What the three assigned methods actually taught

### #3 PROVE SOMETHING STRONGER

Instead of optimizing another square-radial constant, I promoted the finite-volume inequality to the full reversible comparison network (4.2)--(4.4). This permits arbitrary two-dimensional trial potentials and arbitrary dual cutsets.

**Outcome:** success; Claim 238.

### #13 FIND WHAT ONLY INCREASES

The actual directed environment has no simple defect monotonicity. The reversible comparison conductances `C_psi(e)` do: they increase pointwise with adjacent squared stream, so effective resistance decreases and capacity increases by Rayleigh monotonicity.

**Outcome:** useful certificate monovariant; no false monotonicity claim about the original walk.

### #28 REPLACE FOR ALL WITH TYPICAL

The criterion now depends on the average squared stream **along a chosen separating contour**, not the maximum stream on every face of the box. The self-matched triangular field exploits this exactly: interior stream reaches order `log R`, but selected contours have `|psi|<=1/4` everywhere.

**Outcome:** success; explicit recurrent `Theta(log R)` stream field missed by the radial theorem.

---

## 9. Prior-art and contemporary-literature record

Fresh searches on 17 September 2026 included:

- `"The randomly oriented Manhattan lattice in 2D is transient" citations recurrence orientation fields`;
- `2609.07621 deterministic recurrence orientation fields`;
- `Manhattan lattice recurrence deterministic orientation field stream function Nash-Williams`;
- `non-reversible recurrence Nash-Williams stream function conductance comparison`;
- `cycle random walk recurrence stream function Gaudilliere Landim 2D`.

Results recovered:

1. Bou-Rabee--Peres, arXiv:2609.07621v1 (7 Sep 2026), remains the current source. Current SciRate listing showed zero `scites` during this run.
2. Gaudillière--Landim, arXiv:1111.2445, gives the nonreversible Dirichlet/capacity principle and two-dimensional recurrence applications; that mechanism is treated as prior art.
3. Deuschel--Kösters (2008) gives quenched invariance principles under bounded cycle representations; not this unbounded self-matching stream class.
4. Campanino--Petritis and later oriented/stratified-lattice papers give recurrence/transience criteria in distinct partially oriented models.
5. Collevecchio--Hamza--Tournier (2019) studies a **deterministic walker** on a random Manhattan environment, a different process from the random walk classified by source Problem 3.
6. Benjamini--Hermon's nonreversible trace work confirms that recurrence of the symmetric base alone is not a general nonreversible recurrence theorem; the stream/capacity control matters.

I did **not** locate a statement of the adaptive comparison criterion specialized to the fully line-oriented Manhattan model, nor the explicit recurrent self-matching triangular field with `M(R)=Theta(log R)`. A bounded search miss is not a novelty certificate; both new claims remain `PUBLICATION-NOVELTY-UNVERIFIED`.

---

## 10. Directed second-audit duty: P04 / I0101

Claim audited independently:

`P04-I0101-SPLIT-KERNEL-FOURIER-SELFDUAL-18`, from

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T09-42-30Z__run-report.md`.

P04 immutable evidence:

- creation commit: `2898565e9814059a45cf36ca60c187b457663915`;
- report blob: `05792586dc3e473449c4f8476b5fe484c7e945f3`;
- readback receipt: `proofnet24/P04-closure-local-paley/receipts/2026-09-17T09-42-30Z__run-report-readback.md`.

### Independent derivation

For prime `p=1 mod 4`, let

\[
F_{a,x}=p^{-1/2}\psi(-ax),
\qquad
L_{x,y}=\chi(x^2-y^2).
\]

Then

\[
(FLF)_{a,b}
=\frac1p\sum_{x,y}\chi(x^2-y^2)\psi(-ax-by).
\]

With `u=x-y`, `v=x+y`,

\[
x^2-y^2=uv,
\qquad
-ax-by=-\frac{a-b}{2}u-\frac{a+b}{2}v.
\]

The sum factors into two quadratic Gauss sums. Since `p=1 mod 4`, `chi(-1)=1` and `G^2=p`; including the zero-coefficient cases (where both sides vanish) gives

\[
(FLF)_{a,b}=\chi(a^2-b^2)=L_{a,b}.
\]

So `FLF=L` exactly.

Reflection `R f(x)=f(-x)` satisfies `RL=L=LR`, while normalized finite-field Fourier satisfies `F^2=R`. From `FLF=L` and `LR=L`, multiplying on the right by `F` gives

\[
FLF^2=LF,
\qquad
FLR=LF,
\qquad
FL=LF.
\]

If `Rf=-f`, then `Lf=LRf=-Lf`, so `Lf=0`: the odd subspace is annihilated. On the even subspace `F^2=I`, giving the claimed `F=+/-1` splitting.

Finally let `P_D` be the nontrivial diagonal projector onto P04's split domain `D_p`. Every Fourier entry `F_{a,x}` is nonzero. If `P_DF=FP_D`, then entrywise

\[
(P_D)_{aa}F_{a,x}=F_{a,x}(P_D)_{xx}
\]

forces every diagonal entry of `P_D` to be equal, impossible because `P_D` is neither zero nor identity for admissible `p>=13`.

All four mathematical clauses of Claim 18 follow with the exact normalization stated by P04.

**Verdict:**

`P03-AUDIT-P04-I0101-SPLIT-KERNEL-FOURIER-SELFDUAL-240 = PASS (CLAIM-SCOPED)`.

This audit certifies only the structural Fourier/self-duality claim and the noncommuting-compression obstruction. It does **not** certify Conjecture 27, a new admissible prime, or P04's eventual-prime statement.

---

## 11. Metric discipline and remaining obligation

Active metric:

\[
\boxed{\eta_{\rm stream}^{\rm cert}=\frac12\to\frac12.}
\]

Post-movement unchanged streak:

\[
\boxed{1\to2.}
\]

This report contains substantial theorem progress but **no metric movement**, because an explicit recurrent field with `M(R)=Theta(log R)` is not a universal theorem covering every field with `M(R)=O((log R)^gamma)` for any fixed `gamma>1/2`.

The exact source-level obligation remains a structural recurrence/transience classification of arbitrary orientation fields. Within the current stream route, the sharp live question is now:

> Can one either prove a universal recurrence theorem beyond fixed power `1/2`, or construct a deterministic transient exact-source field whose anchored stream grows as slowly as possible?

Claim 238 shows that any such transient construction must defeat **every** divergent low-average-stream separating-cutset family, not just square boundaries.

The present `Theta(log R)` recurrent construction also shows that the scalar envelope `M(R)` alone is too coarse to characterize recurrence: geometry of where the stream is large matters essentially.

---

## 12. Next new-method attack

The next run should not repay the comparison-network theorem or the triangular example. Use three methods not yet used on I0003:

- **#7 TAKE THE LIMIT** — pass to a continuum/large-block profile for slowly growing primitives and identify whether a nontrivial effective drift survives after self-matching contours are forbidden;
- **#20 FIND WHY THE ALGORITHM FAILS** — formulate an algorithm that tries to build low-stream separating dual circuits from the two primitive paths `alpha` and `beta`; characterize the exact obstruction when it cannot close a circuit;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT** — assume the universal exponent `1/2` really is sharp and try to construct a deterministic transient field with `M(R)=O((log R)^{1/2+epsilon})`, rather than proving another recurrence subclass.

If the next run again leaves `eta_stream^cert` unchanged, the post-movement streak reaches three and the formal HARD stuck-thinking protocol triggers.

---

## 13. Claim ledger

| Claim | Status after this run | Note |
|---|---|---|
| Doubly periodic classification | KNOWN-IMPLIED / PARTIAL | recurrent iff both period means vanish; otherwise ballistic |
| `P03-I0003-BOUNDED-DISCREPANCY-SECTOR-232` | KNOWN / VERIFIED TRANSFER / PARTIAL | bounded stream implies recurrence |
| `P03-I0003-SUBSQRTLOG-STREAM-234` | PROVED / PARTIAL / novelty unverified | `M=o(sqrt(log R))` recurrence |
| `P03-I0003-ANNULAR-STREAM-RESISTANCE-236` | PROVED / PARTIAL / novelty unverified | divergent square-annular resistance recurrence; includes critical endpoint and iterated logs |
| `P03-I0003-ADAPTIVE-CUTSET-RESISTANCE-238` | **PROVED / PARTIAL / novelty unverified** | recurrence if the comparison stream network has a divergent Nash--Williams cutset family |
| `P03-I0003-SELF-MATCHED-LOGSTREAM-239` | **PROVED / PARTIAL / novelty unverified** | explicit exact-source recurrent field with `M(R)=Theta(log R)`; Claim-236 square series converges |
| broad source Problem 3 | OPEN / PARTIAL | no full classification |
| `P03-AUDIT-P04-I0101-SPLIT-KERNEL-FOURIER-SELFDUAL-240` | PASS / claim-scoped | independent outside audit |

---

## 14. `ledger_delta` for P26 only

```text
P03 | Bou-Rabee--Peres 2026 arXiv:2609.07621v1 §7 Problem 3 / I0003 | active metric eta_stream^cert 1/2 -> 1/2 NO MOVEMENT, post-movement unchanged streak 1 -> 2; periodic_scope_certified=1 and bounded_discrepancy_scope_certified=1 retained | PARTIAL / broad source OPEN | B3/B13/B28 | new P03-I0003-ADAPTIVE-CUTSET-RESISTANCE-238=PROVED/PARTIAL/PUBLICATION-NOVELTY-UNVERIFIED: cap_L <= cap of reversible stream network C_e=1+32(psi_q1^2+psi_q2^2), hence any divergent Nash-Williams family of adaptive low-average-stream cutsets proves recurrence; new P03-I0003-SELF-MATCHED-LOGSTREAM-239=PROVED/PARTIAL/PUBLICATION-NOVELTY-UNVERIFIED: explicit triangular-block exact-source field has M(R)=Theta(log R), adaptive low-stream cutsets and recurrence, while Claim-236 square-annular series converges, proving strict source-class improvement | no checker (analytic theorems) | directed audit P03-AUDIT-P04-I0101-SPLIT-KERNEL-FOURIER-SELFDUAL-240=PASS claim-scoped | next B7/B20/B23; one more unchanged run triggers formal HARD stuck protocol
```

P03 did not edit shared root ledgers, peer files, email, Drive, public posting, permissions, workflows, or schedules.

---

## 15. Model / routing control

The exposed scheduler interface still offers schedule/title/prompt/enabled controls but no model-family selector and no reasoning-effort selector. GPT-6 / maximum remains requested in prompt text only. This run's actual report identity is GPT-5.6 Sol with reasoning level UNVERIFIED. Changing that requires platform/backend support or an authorized interface exposing those routing controls; prompt text cannot certify it.

**End of complete run report.**