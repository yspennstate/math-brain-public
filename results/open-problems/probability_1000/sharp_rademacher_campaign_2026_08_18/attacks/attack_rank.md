# Rank lane: what the quotient theorem actually bounds, and where the rooted form breaks

Lane: linear-algebraic / rank, iteration 2 (the iteration-1 run died on a session limit; this is the re-run,
with the transfer, entropy, telescope, cluster and referee outputs available). Author: independent attack agent,
2026-08-19. Working under the parent session's claim on the campaign directory; this file is the only file written.

**Honesty header.** Nothing here proves the sharp Rademacher singularity conjecture, the boxed connector-rigidity
theorem, or any weakening of either. Every claim below carries a status label. Dossier citations are to
`rademacher_dossier.txt` by extraction line, with the printed page in brackets. I re-read every dossier statement
I use — I did not rely on STATE.md's digest or on the prompt's summary, and one digest number turns out to be
3x pessimistic (§9.1). Two lanes reading the same dossier is not independence; where I converge with the entropy
or transfer memo I say so and say why the convergence is weak evidence.

---

## 1. What I verified in the source before using it

| object | dossier location | what I checked |
|---|---|---|
| $d_{\rm cb}$ definition (basis from the full dual; every full-dual form gets a signed basis representative; all residuals in one common $R$; minimise $\dim R$ over basis **and** selectors) | lines 141–169 [p.6–7] | read verbatim; my computations in §9 implement exactly this |
| rooted target (41): $\dim\frac{R+R_<}{R_<}\le C L_{Q\mid W}$, $R\cap\operatorname{span}W\subseteq R_<$ | lines 2862–2870 [S1 p.71]; restated lines 184–191 [p.8]; lines 1307–1311 [p.52] | read verbatim, all three copies agree |
| batching: $\psi(u)=\min\{3/4,\,2^{1-u}\binom{u}{\lfloor u/2\rfloor}\}$, $c_s=-\log_2\psi(a_s+1)$, $\kappa=\max_s a_s/c_s$, $\beta=\log_2(4/3)$ | lines 8906–8933 [S9 p.145–146]; lines 1940–1964 [S1 p.60] | read verbatim |
| Theorem 1 proof chain: $\sum_s c_s\le L$ (10); $N=\sum_s a_s\le\kappa L$ (11); $C=$ matching endpoints, $|C|=2N$, $|E_a\setminus C|\le1$ (12); free/never-free $\Rightarrow |N_0|\le L$ (14)–(15); $P_0=\operatorname{span}Q_{C\cup N_0}$, $\dim P_0\le(2\kappa+1)L$ (16) | lines 9000–9169 [S9 pp.147–149] | read the whole proof line by line; **the batching is used only to bound $N$** (see §3) |
| Lemma 2 (connector factorization): $R\cap B\subseteq R_<\iff\ker P\subseteq\ker\overline B\iff\overline B=T\circ P$ | lines 9276–9361 [S9 pp.150–151] | read verbatim including the proof |
| NAE-star counterexample: $W=(x_i,z_i)_{i\le3}$, $Q=(q)$, $Y_i=x_i+z_i+q$, $|A|=54$, $H(q\mid W)=8/27$, $L=19/27$ | lines 9443–9524 [S9 pp.152–153] | read verbatim; **independently recomputed** $|A|=54$, full dual, $L$ (§9) |
| triangular witness basis (28) and $k\le\ell/\beta$ (29) | lines 2346–2390 [S1 p.65] | read verbatim |
| the concrete subproblem ("from the witness basis (28), either find $\kappa=O(1)$ … or extract further dense witnesses") | lines 2892–2909 [S1 p.71]; lines 1312–1314 [p.52] | read verbatim |
| residual class: singleton-layer cyclic SCC, relation corank $\ge5$, $\kappa\gtrsim\log n$ in every useful junction basis **or** common-lift failure | lines 1303–1306 [p.52]; lines 2877–2889 [S1 p.71] | read verbatim; note the horn is a **disjunction** |
| endpoint regime: $4^\ell=o(\ell\log n)$ (26); $\ell\ge\frac12\log_2\log n+\frac12\log_2\log\log n-O(1)$ (27); $O(\kappa\ell k)$ (27a); survivor rows meet $\Omega(\log n\log\log n)$ disjoint pairs | lines 2255–2343 [S1 pp.64–66]; lines 206–217 [p.8] | read verbatim |
| crosspolytope $d_{\rm cb}(A_r)=r-\lfloor\log_2 2r\rfloor$ and its lower-bound argument | lines 2408–2463 [S1 pp.66] | read verbatim; **independently reproduced at $r=4$** (§9.2) |
| $m=1$ interval: $L_{Q\mid W}=3/(2^{k+1}+3)\to0$, exact selector distance 1, "no inequality … with an absolute $C$"; the absorbed alternative (65)–(67) | lines 13196–13308 [S14 pp.198–199] | read verbatim |

Two readings I want on the record because later sections lean on them:

* **[VERIFIED]** S9's Theorem 1 constructs $C$ as *the endpoint set of a maximum matching of $\Gamma$* (line 9064). Everything
  involving $\psi,c_s,\kappa$ exists only to bound $N=|{\rm matching}|$. **Second search, different wording** (grep
  `matching` across all 200 pages, 40 hits read): the dossier *does* use the matching size directly once — S6 §5.1,
  line 6896, "a two-shadow maximum matching has only linear size, whereas $4^\ell=(4^\beta)^t$" — inside its
  counterexample audit, not as a form of the theorem. So §3 is a repackaging the dossier is one step away from, not
  something it contradicts; I state it that way there.
* **[VERIFIED]** The residual-class characterisation is a **disjunction** (line 1305: "it *either* has congestion at least
  of order $\log n$ … *or* fails the common-lift condition"). Both delivered iteration-1 lanes and the referee flagged that
  the disjunctive reading is the honest one; my §4 result applies to the first horn only, and I say so each time.

---

## 2. The rooted target splits exactly, and Theorem 1 is exactly one half of it

**[PROVED, elementary]** **Proposition R1 (splitting identity).** Let $B=\operatorname{span}W$, $R_<\subseteq B$, and let
$R$ be any residual space. Then

$$\dim\frac{R+R_<}{R_<}\;=\;\dim\frac{R+B}{B}\;+\;\lambda,\qquad
\lambda:=\dim\frac{(R\cap B)+R_<}{R_<}. \tag{R1}$$

*Proof.* The inclusion-then-quotient map $\varphi:(R+R_<)/R_<\to(R+B)/B$ is surjective, and
$\ker\varphi=\bigl((R+R_<)\cap B\bigr)/R_<$. Since $R_<\subseteq B$, Dedekind's modular law gives
$(R+R_<)\cap B=(R\cap B)+R_<$. $\square$

S9's Lemma 2 uses the same map and kills the kernel by hypothesis (line 9355: "Its kernel is zero by condition 1").
(R1) just computes the kernel unconditionally. Its value is bookkeeping honesty:

**[PROVED]** **Corollary R1a.** For a given block, basis and selectors, target (41) with constant $C$ holds
$\iff$ $\lambda=0$ **and** $\dim\frac{R+B}{B}\le CL$. So, given clause (ii), clause (i) is *exactly* a bound on the
quotient rank — the one object S9's Theorem 1 bounds, by $(2\kappa+1)L$. There is no third ingredient, and the
unproved content of (41) beyond Theorem 1 is precisely **two** things: (a) $\lambda=0$ (or, under a weaker
aggregation, $\lambda$ small), and (b) shrinking Theorem 1's coefficient $2\kappa+1$ to something admissible on the
residual class, where $\kappa\gtrsim\log n$. Item (b) is §4; item (a) is §7. Neither is bookkeeping.

**[PROVED]** **Proposition R2 (the leak is a boundary-trace rank).** With S9's maps $P:F\to P_0$, $e_a\mapsto p_a$ and
$\overline B:F\to B/R_<$, $e_a\mapsto b_a+R_<$ (tags (22)–(23), lines 9284–9306):

$$\lambda=\dim\overline B(\ker P)=\operatorname{rank}\begin{pmatrix}P\\ \overline B\end{pmatrix}-\operatorname{rank}P. \tag{R2}$$

*Proof.* $\sum_a\lambda_ar_a\in B$ iff $\sum_a\lambda_ap_a=0$ (private and boundary parts are independent because
$P_0\cap B=0$: $P_0$ is a private coordinate span and $(W,Q)$ is a basis), i.e. iff $\lambda\in\ker P$; the class of
$\sum\lambda_ab_a$ mod $R_<$ is $\overline B\lambda$. The matrix form is the rank–nullity restatement. $\square$

So the leak is an **excess rank**: the amount by which the residual system's total rank mod $R_<$ exceeds its private
rank. This is the exact quantity the telescope draft's (T1a) filtration needs bounded (it needs only the *total*
$\dim\frac{R_B+R_<^B}{R_<^B}$, never $\lambda=0$ separately). Combining:

**[PROVED, given (T1a) as stated in `telescope_reconstruction_draft1.md` §2 — which is UNREFEREED]**
Filtration bookkeeping needs only the *total*, so under it clause (ii) is replaced by a **leak bound**
$\lambda_B\le\gamma'L_B$ (the exact vanishing $\lambda=0$ is not needed) — while the quotient half still has to be
brought below an admissible coefficient. Under the packet's own ancestor-only bookkeeping (line 192 [p.8]: "the same
boundary direction can be charged at each generation"), clause (ii) is needed as stated, and (R1) says it is exactly
$\lambda=0$.

---

## 3. What Theorem 1 really bounds: the matching number, not the congestion

**[PROVED, from S9's proof with no new ingredient]** **Theorem R3 ($\nu$-form).** In S9's rooted setup, the selector
certificate of Theorem 1 satisfies

$$\dim\frac{R+B}{B}\;\le\;2\nu(\Gamma)+L, \tag{R3}$$

where $\nu(\Gamma)$ is the **matching number** of the private two-shadow graph $\Gamma$. Moreover, for **any** certified
batching,

$$\nu(\Gamma)\;=\;\sum_s a_s\;\le\;\min\Bigl\{\kappa_{\rm avg}L,\ \kappa L,\ \tfrac92\,4^{L},\ \lfloor q/2\rfloor\Bigr\},
\qquad \kappa_{\rm avg}:=\frac{\sum_s a_s}{\sum_s c_s}\le\kappa. \tag{R3a}$$

*Proof.* S9's proof puts every residual's private projection in $P_0=\operatorname{span}Q_{C\cup N_0}$ with $C$ the
endpoint set of a maximum matching, so $|C|=2\nu$; $|N_0|\le L$ is (15) and is independent of the batching; project
along $B$. For (R3a): the batches partition the matching (line 1906 [S1 p.60]), so $\sum_sa_s=\nu$ exactly; then
$\nu=\kappa_{\rm avg}\sum_sc_s\le\kappa_{\rm avg}L$ by (10), $\kappa_{\rm avg}\le\max_s a_s/c_s=\kappa$ by the mediant
inequality, and $\nu\le\frac92 4^L$ is (17)–(18). $\square$

Three consequences, all [PROVED], none of them deep, all of them changing what one should try:

**(a) $\kappa$ is not the theorem's parameter; $\nu$ is.** The three published forms — $9\cdot4^\ell+\ell$ (19),
$(2\kappa+1)L$ (24c)/(7), and the support form $(1+2(s-1)/\beta)L$ (1) — are three estimates of the same quantity.
Replacing $\kappa$ by $\kappa_{\rm avg}$ is free and never worse; it is a strict improvement whenever congestion is
non-uniform, which is exactly the regime the entropy lane's §4 derives (one dominant dense batch, $O(1)$ remainder).
*Attribution, after a second search:* the dossier already compares the matching size with $4^\ell$ for NAE-circuit
products (S6 §5 item 1, line 6896), so the observation that $\nu$ can be far below $4^\ell$ is theirs; what is not in the
dossier is the estimate written in the $\nu$ form, and $\kappa_{\rm avg}$.

**(b) The crosspolytope's "unbounded $\kappa$" is an artefact of the packaging, not of the theorem.** S9 explains the
crosspolytope by $\kappa\asymp r/\log r$ (line 9271), which makes $(2\kappa+1)L\asymp r^2/\log r$ — vacuous. But
$\nu\le\lfloor r/2\rfloor$ there, so (R3) gives $\le r+\ell\approx2\ell$, coefficient $\approx2$, against the truth
$d_{\rm cb}=r-\lfloor\log_2 2r\rfloor\approx\ell$. The crosspolytope is therefore **not** a counterexample to the
$\nu$-form. (It remains a counterexample to "batching charges alone pay the rows", which is what the dossier actually
claims at lines 2455–2463 — I am not contradicting the dossier, only removing a misleading packaging.) Caveat, stated
plainly: in the unrooted case $\dim\frac{R+B}{B}\le q$ holds trivially, so (R3)'s content in that example is only a
factor 2 better than trivial.

**(c) Nothing in Theorem 1 sees rank.** $P_0$ is a *coordinate span*: the theorem bounds the **support** of the residual
system, and then bounds its rank by its support. Every LO/exposure argument in the packet has this shape
((13), (19), (24c), (7), (16)). The packet's only genuinely rank-level results are the explicit structural certificates
(rooted NAE cycle $\lceil n/3\rceil$ [S10]; interval certificates [S14]) — no LO argument in the packet ever produces
a rank below the support it controls. That is the diagnosis §4 makes quantitative.

---

## 4. The support route is off by exactly $\Theta(\log n)$ on the high-congestion horn — and this is forced

**[PROVED, conditional on the dossier's class characterisation (line 1305) and on the LO inequality
$c_s\ge\frac12\log_2(a_s+1)-1$ (which follows from $\psi(u)\le2/\sqrt u$, tag (16) line 1948)]**

**Theorem R4 (forced deficit).** Let a block admit only batchings with $\kappa\ge c_0\log n$ (the first horn of the
class definition). Then in **every** such batching, in every basis, and for every choice of maximum matching, witness
rows and greedy order,

$$\nu(\Gamma)\;\ge\;a_{s^*}\;\ge\;\Bigl(\tfrac{c_0}{2}-o(1)\Bigr)\,\log n\,\log_2\log n , \tag{R4}$$

so the bound (R3) evaluates to at least that, whatever $L$ is. Consequently the coefficient the support route can
deliver is at least $2\nu/L$, and

* in the **threshold window** — the regime where $\ell$ sits *at* the lower bound (27) forces, i.e.
  $\ell\asymp\log_2\log n$, so that $L\le\ell\asymp\log_2\log n$ — this evaluates to
  $\ge\bigl(2c_0-o(1)\bigr)\log n$: **$\Theta(\log n)$, exactly the factor the endpoint cannot afford**
  (transfer lane W1: any uniform $\gamma_n=o(\log n)$ closes Layer II; $\gamma_n\asymp\log n$ does not).
  Note (27) is only a *lower* bound on $\ell$ (line 2285); "the window" is an extra regime assumption, the same one
  the entropy lane's §4 works in, and outside it the conclusion weakens as follows;
* in general the route can deliver an $o(\log n)$ coefficient **only if** $L=\omega(\log\log n)$ — a statement about
  what the *route* can output, not about the truth of the target. On a block tree this is a strong restriction:
  $\sum_BL_B\le\ell$, so in the threshold window *every* block has $L_B\le\ell=O(\log\log n)$ and the route is dead on
  each of them separately.

*Proof.* $\kappa\ge c_0\log n$ gives a batch with $a_{s^*}\ge c_0\log n\cdot c_{s^*}$; $c_{s^*}\ge\beta$ gives
$a_{s^*}\ge\beta c_0\log n$; feeding that back through $c_{s^*}\ge\frac12\log_2(a_{s^*}+1)-1$ gives
$a_{s^*}\ge c_0\log n\bigl(\frac12\log_2(\beta c_0\log n)-1\bigr)=(\frac{c_0}{2}-o(1))\log n\log_2\log n$. The batches
partition the matching, so $\nu\ge a_{s^*}$. $\square$

(R4) reproduces the dossier's own sentence "such a batching contains a witness meeting $\Omega(\log n\log\log n)$
disjoint matching pairs" (lines 2337–2343) — I re-derived it rather than quoting it, and then used it in the
opposite direction from the dossier: the dossier reads it as *density of the survivor*, I read it as a **lower bound
on the output of the packet's own tool**.

**[PROVED, same conditions] Corollary R4a (no repair by better combinatorics).** On the first horn, no choice of
maximum matching, witness row, greedy order, or congestion estimate — including $\kappa_{\rm avg}$ and the $\nu$-form —
brings S9's Theorem 1 below $\Theta(\log n)\cdot L$ in the threshold window. The deficit is not slack in the estimate;
it is the gap between the *support* $|C|=2\nu\asymp\log n\log\log n$ and the *rank* the target demands,
$O(L)=O(\log\log n)$.

**[VERIFIED, found on the second search — it constrains R4 and survives it]** S6 §6 (lines 6985–7005) lists what the
residual class does *not* have: "no sparse-cyclomatic fundamental graph, no relation-side feedback set of size
$o(\log n)$, **no large disjoint-support matching**, no $o(\log n)$ ordinary star core, no sufficiently low-rank shared
form, and no multiplicative subgroup/coset fibre." I checked whether "no large disjoint-support matching" contradicts
(R4)'s $\nu\ge\Omega(\log n\log\log n)$: it does not — that clause is about a large family of **rows with pairwise
disjoint supports**, whereas $\nu$ is a matching in the two-shadow graph on **private coordinates**, and a *single*
dense row already supplies $\lfloor|E_s|/2\rfloor$ two-shadow matching edges by itself. The two statements are not only
compatible, they compose: many two-shadow edges, no disjoint-support row family, i.e. the edges must come from few
dense rows — the entropy lane's forced "one dominant dense batch" geometry, arrived at here from the class definition
rather than from the threshold window.

**This is the lane's central negative result and it is the honest reason the packet is stuck**: the residual class is
(on this horn) *defined* to be the set of blocks on which every support-type bound is a $\log n$ factor too weak
(compare the dossier's own framing at lines 213–217 [p.8]: the unconditional bridge covers $4^\ell=o(\ell\log n)$, the
congestion theorem covers $\kappa=o(\log n)$, "consequently a surviving nonsummable sequence must have both moderately
large defect and high congestion"). What R4 adds is the *size* of the required repair, stated in the only currency
that matters:

> **Target R-C (rank compression).** For a residual-class block, with $C$ the private core produced by any matching
> cover ($|C|=2\nu\asymp\log n\log\log n$), exhibit selectors whose residual private parts $\{p_a\}\subseteq\operatorname{span}Q_C$
> span a subspace of dimension $O(L)=O(\log\log n)$ — a rank deficiency of factor $\Theta(\log n)$ relative to their
> own support.

Anything less than a factor-$\Theta(\log n)$ rank compression cannot close Layer II on this horn. Anything achieving it
closes the horn, because (R3) then reads $\dim\frac{R+B}{B}\le O(L)$.

---

## 5. One rank-compression mechanism that provably works, and exactly where it stops

The forced geometry (entropy §4: one dominant dense batch plus an $O(1)$ remainder) suggests the compression should
come from the dense row itself. It does, under one hypothesis, and the hypothesis is precisely what
"connector-incoherent" denies.

**Definition.** Let $U\subseteq[r]$ and $h_0\in D(A)$ with $\operatorname{supp}h_0=U$. Say $A$ is **$U$-local through
$h_0$** if every $f\in D(A)$ is either $\pm e_i$ for some $i\in U$, or of the form $f=\alpha_f h_0+g_f$ with
$\operatorname{supp}g_f\cap U=\varnothing$. Let $A'$ be the **contracted fibre** on $([r]\setminus U)\cup\{*\}$,
$A'=\{(x_{[r]\setminus U},\,h_0(x)):x\in A\}$, and let $d_{\rm cb}^{*}(A')$ be the selector distance minimised over
coordinate bases of $A'$ that contain the coordinate $x_*$.

**[PROVED]** **Lemma DRR (dense-row reduction).** If $A$ is $U$-local through $h_0$ then
$$d_{\rm cb}(A)\;\le\;d_{\rm cb}^{*}(A')+1 ,$$
**independently of $|U|$.**

*Proof.* Pull back an optimal $A'$-certificate $(G',\sigma',R')$ along $x_*\mapsto h_0$; the pullback is a bijection
from $D(A')$ onto $\{f\in D(A): f=\alpha h_0+g,\ \operatorname{supp}g\cap U=\varnothing\}$ (surjectivity of
$A\to A'$ gives $\supseteq$; $h_0(A)\subseteq\{\pm1\}$ gives $\subseteq$). Fix a pivot $p\in U$ and set
$G:=\mathrm{pb}(G')\cup\{e_i:i\in U\setminus\{p\}\}$; $|G|=(r-|U|+1)+(|U|-1)=r$, all members lie in $D(A)$, and $G$ is
independent (a nonzero pullback combination lying in $\operatorname{span}\{e_i:i\in U\setminus p\}$ would have to be
$c_*h_0$, whose support contains $p$). Selectors: pulled-back forms take $\mathrm{pb}(\sigma')$, with residuals in
$\mathrm{pb}(R')$; $\pm e_i$ ($i\ne p$) select themselves; $\pm e_p$ selects $\varepsilon h_0\in\pm G$ (available because
$x_*\in G'$), contributing the single new direction $e_p-\varepsilon h_0$. $\square$

**Calibration [all EXACT]:**
* NAE $m$-slice $A=\{x:\sum_ix_i\in\{\pm1\}\}$ ($m$ odd), $U=[m]$, $h_0=\sum x_i$: $U$-local, because
  $D(A)=\{\pm e_i\}\cup\{\pm h_0\}$ exactly. **[PROVED]** *(swapping a $(+,-)$ pair keeps $\sum x_i$ fixed, so
  $a_i-a_j\in\{0,\pm1\}$ for all $i,j$, whence the coefficients take at most two values $t,t+1$, say $k$ of them
  $t+1$; writing $f=t\sum_ix_i+\sum_{i\in S}x_i$, $|S|=k$, on the slice $\sum x_i=1$ the term $\sum_Sx_i$ takes three
  values unless $k\in\{0,1,m-1,m\}$, and those four cases give $\pm h_0$ and $\pm e_i$.)* Hence
  $A'=\{\pm1\}$ and $d_{\rm cb}\le1$ — correct, while $\ell\approx\frac12\log_2m$ and $\nu(\Gamma)=\lfloor m/2\rfloor$.
  **The support route is off by a factor $\asymp m/\log m$ here and the truth is 1.** This is the cleanest existing
  witness that R-C's demanded compression is not absurd.
* **The dossier's own $(3,2)$-star / treewidth-two family** (S6 §5 item 5, lines 6922–6928): "its density tends to $1/2$
  while the number of ears is unbounded … **its actual residual rank remains one**". That is the DRR conclusion for a
  shared dense row, recorded by the packet as a counterexample-audit item rather than as a mechanism. Lemma DRR is the
  general statement behind it, and behind the $m$-slice, in one line each. *(Found on a second, differently-worded
  search of the dossier — I had not read S6 §5 when I proved DRR; the lemma was written from the $m$-slice.)*
* Entropy lane §5a (slice-rooted NAE cycles $A(s,n)$): their enumerated full dual is exactly
  $\{e_i\}\cup\{h_0\}\cup\{h_0+e_{b_j}+e_{b_{j+1}}\}$ — i.e. $U$-local through $h_0=\sum u_i$ — and their basis contains
  $h_0$. Lemma DRR gives $d_{\rm cb}(A(s,n))\le d_{\rm cb}(\text{rooted NAE cycle})+1=\lceil n/3\rceil+1$, **proving in
  general the "+1" they verified by enumeration for seven $(s,n)$ pairs, and proving the $s=1$ control has no $+1$.**
  This is a genuinely different method (algebraic contraction vs exact enumeration), so it is real corroboration of
  that memo's §5a, not lane agreement.

**[PROVED] Where DRR stops.** The hypothesis fails exactly when some full-dual form's restriction to $U$ is neither
zero nor a multiple of $h_0$. Define the **profile space** $\Pi^0_U:=\operatorname{span}\{f|_U:f\in D(A),\,f\ \text{not a
coordinate}\}$; $U$-locality is $\dim\Pi^0_U=1$. The general block-internal question that DRR isolates is:

> **Question R-Q.** For a residual-class block with dominant dense support $U$ ($|U|\asymp4^\ell$), how large can
> $\dim\Pi^0_U$ be? If $\dim\Pi^0_U=O(\ell)$ a DRR-style contraction plausibly gives $O(\ell)$ plus the contracted
> problem; if $\dim\Pi^0_U$ can be $\asymp|U|$, the certificate route dies on that block.

**[PROVED, elementary — and it says the naive attack on R-Q fails]** Every $f\in D(A)$ has
$|\operatorname{supp}f|\le16\cdot4^{\ell}$, and every selector residual $r_a=f-g$ (a difference of two $\pm1$-valued
forms, hence $\{0,\pm2\}$-valued on $A$) has $|\operatorname{supp}r_a|\le36\cdot4^{\ell}$.
*Proof.* Averaging over slices of $A$ above $\operatorname{supp}(f)^c$, some slice has density $\ge2^{-\ell}$ in
$\{\pm1\}^{\operatorname{supp}f}$; on it $f$ takes $\le2$ values (resp. $r_a$ takes $\le3$), so by Erdős's
Littlewood–Offord bound $2^{-\ell}\le2\psi_0(u)\le4/\sqrt u$ (resp. $\le3\psi_0(u)\le6/\sqrt u$) with
$\psi_0(u)=2^{1-u}\binom{u}{\lfloor u/2\rfloor}$. $\square$
So single-form LO controls **support** at the $4^\ell$ scale and says nothing about $\dim\Pi^0_U$: the rank question
is invisible to it. This is §3(c) again, one level down — the problem is **self-similar**, and R-Q is the rank-route's
arrival at the same irreducible core the entropy lane reached as its Gap 2 ("fibres on $m$ coordinates with defect
$\ell\approx\frac12\log_2m$, for which the target demands $d_{\rm cb}=O(\log m)$ while the bridge gives $O(m)$").
Convergence of two lanes on the same dossier is weak evidence; what it does establish is that the core survives a
change of currency (entropy $\to$ rank), which a mere artefact of one lane's framing would not.

---

## 6. The dossier's own concrete subproblem: why iterated witness extraction densifies

Dossier p.52/p.71 (lines 1312–1314, 2892–2909): *"Starting from the witness basis (28), either find a batching with
$\kappa=O(1)$ and verify the common-lift condition (24e), or use the unused part of the conditional defect to extract
further dense witnesses until the remainder has bounded congestion."* This lane's finding on that programme:

**[PROVED] Proposition R5 (exchange densification).** Let $h_s$ be a witness with pivot $p\in E_s=\operatorname{supp}h_s$,
and perform the (28)-exchange replacing the private coordinate $Q_p$ by the witness. For a row $a$ with $h_a(p)\ne0$
put $\alpha=h_a(p)/h_s(p)\ne0$. In the new private coordinates the row reads
$\alpha\cdot(\text{new coordinate})+(h_a-\alpha h_s)$, and
$$\operatorname{supp}(h_a-\alpha h_s)\ \supseteq\ E_a\,\triangle\,E_s \qquad(p\notin E_a\triangle E_s),$$
so the row's new private support has size $\ge|E_a\triangle E_s|+1\ \ge\ |E_s\setminus E_a|+1$. Rows with $h_a(p)=0$ are
unchanged.
*Proof.* For $i\in E_a\setminus E_s$ the value is $h_a(i)\ne0$; for $i\in E_s\setminus E_a$ it is $-\alpha h_s(i)\ne0$. $\square$

**[PROVED] Corollary R5a.** Exchanging a dense witness of support $D$ makes every row meeting its pivot at least
$(D-|E_a\cap E_s|)$-dense. The extraction programme therefore *requires* an **alignment hypothesis** — the rows meeting
the pivot must satisfy $|E_a\triangle E_s|$ small, i.e. the dense rows cluster around the extracted witness. Without
alignment the first extraction strictly densifies the two-shadow graph and $\nu$ can **increase**.

Sanity check against the packet: for the crosspolytope, two full-dual forms $\frac1rHv,\frac1rHv'$ have full supports
and symmetric difference $\asymp r$, so extraction densifies — consistent with the dossier's own audit that the
"unselected rows cost only $O(k)$ after exchange" inference is false (lines 2394–2399).

**[PROVED] Corollary R5b (the concrete subproblem is strictly harder than the theorem it serves).** Achieving
$\kappa=O(1)$ (which forces $\nu\le\kappa L=O(L)$) is *sufficient* for clause (i) but not *necessary*: the NAE $m$-slice has
$\nu=\lfloor m/2\rfloor\asymp4^\ell$ in its own coordinates and $d_{\rm cb}=1$. So a proof strategy that insists on
driving the congestion down is aiming at a strictly stronger statement than the target, and on at least one family the
gap between the two is unbounded. Aligned alternative, which DRR shows is the mechanism actually at work there: a single
exchange of $h_0$ makes $\Gamma$ empty. **The honest summary of the p.52 attack: horn 1 ("find $\kappa=O(1)$") is the
alignment case and is exactly Lemma DRR; horn 2 ("extract dense witnesses") is Proposition R5 and is counterproductive
without alignment. Connector-incoherence is the negation of alignment.**

---

## 7. The minimal extra hypothesis (what the task asked for)

Given (R1)–(R2), the question "what is the minimal extra hypothesis making the rooted form go through" has a precise
and slightly deflationary answer, plus one genuinely new weakening:

1. **For the rooted form as the packet states it, there is no weaker hypothesis than absorption.** Lemma 2 is an
   equivalence, so $\ker P\subseteq\ker\overline B$ is not merely sufficient, it *is* the condition. Any "weaker
   hypothesis" is therefore a statement about a *different aggregation*, not about a weaker rigidity lemma.
2. **[PROVED] The aggregation-level minimal hypothesis is bounded unpaid boundary rank.** Since
   $\lambda\le\operatorname{rank}\overline B$,
   $$\lambda\ \le\ \mu:=\dim\frac{U_B+R_<}{R_<},\qquad U_B:=\operatorname{span}\{b_a\}\subseteq B, \tag{R6}$$
   and therefore, with no absorption hypothesis at all,
   $$\boxed{\ \dim\frac{R+R_<}{R_<}\ \le\ 2\nu(\Gamma)+L+\mu\ }\tag{R7}$$
   **[PROVED, combining R1, R2, R3, R6].** In particular $\mu\le\dim(B/R_<)\le|W|-\dim R_<$: **for a block whose
   unpaid boundary interface has rank $O(L)$, clause (ii) is not needed — the rooted estimate follows from the
   quotient half alone, at the cost of an additive $O(L)$.** Absorption is needed only for blocks with $\mu\gg L$.
   (Caveat, since (R7) has two terms: this removes the *connector* condition, not the coefficient problem of §4 —
   the $2\nu+L$ half must still be admissible. The two halves are independent and both must land.)
   *Checks.* NAE star: $|W|=6$, $L=19/27$, and the true optimal leak is $1$ (§9.1) — $\mu$-bound loose but valid.
   $m=1$ interval (S14 §7): $|W|=3$, $L\to0$, so $\mu/L\to\infty$ — absorption genuinely required, matching S14 §8's
   verdict that this block "must either pass its boundary residuals to an ancestor or be handled by the global
   triangular activation budget" (lines 13335–13339).
3. **Can dense singleton-layer cyclic blocks satisfy $\mu\le\gamma'L$?** **[UNKNOWN]** — and it is a *checkable*
   question, unlike absorption. It asks only for the rank of the block's interface to the not-yet-paid ancestor space,
   which in the endpoint window must be $O(L)=O(\log\log n)$. **Search, with a working detector:** grep over all 200
   pages for `incoming boundary`, `boundary size`, `number of boundary`, `size of the boundary`, `boundary coordinates`,
   `shared coordinate`, `interface` returns 11 hits (lines 181, 1202, 2692, 9573, 9590, 11213, 11588, 11984, 12013,
   12898 and 12485), read individually; the positive control `connector absorption` on the same file returns 12 hits,
   so the detector works. None of the 11 gives the boundary *size* or *rank* for the residual class — the closest,
   line 12485, fixes only the shape of a junction basis ("an incoming junction basis containing $A$ and otherwise
   disjoint from the private coordinate span"), for the *solved* cycle. The inherited flag/layer block-formation
   machinery that would fix it is the same missing layer the telescope reconstruction ran into.
   **This is the cheapest unexplored hypothesis on the board.**

---

## 8. Lower-bound tool (for the counterexample lane), stated generally

**[PROVED, generalising the dossier's own crosspolytope argument, lines 2446–2452]** For any fibre $A$ spanning
$V=\mathbb K^r$, any coordinate basis $G\subseteq D(A)$ and any selectors with residual space $R$, the image
$\pi_R(D(A))\subseteq V^*/R$ has at most $2r$ elements. Hence
$$d_{\rm cb}(A)\ \ge\ \min\{\dim R:\ |\pi_R(D(A))|\le2r\},$$
and if $D(A)$ contains a linear image of a cube of rank $m$ then $2^{m-\dim R}\le2r$, i.e. $\dim R\ge m-\log_22r$.
Its weak corollary $d_{\rm cb}(A)\le|D(A)|-r$ is what makes the census of §9.2 feasible. **Scope warning, from the
dossier itself** (S6 §5 item 6, lines 6931–6937): "crosspolytopes … their full dual has exponentially many forms, so
excess-dual bounds are useless." Agreed — $|D|-r$ is used here **only** as a sound skip-filter inside a finite census,
never as a proof tool, and the lower-bound half above is the part with content.

---

## 9. Exact finite computations (all local, exact rational arithmetic, code in the session scratchpad)

Method: full dual by solving $f\cdot x_i=s_i$ over $\mathbb Q$ on a basis $x_1..x_r\subseteq A$ for all $2^r$ sign
patterns and testing $f(A)\subseteq\{\pm1\}$ (complete, since a form is determined by its values on a spanning set);
$d_{\rm cb}$ by exhaustive search over all $r$-subsets of $D(A)$ that are bases, with branch-and-bound over signed
selectors. Two independent validations of the code before use: $d_{\rm cb}=1$ for the NAE three-circuit (matches the
hand computation) and $d_{\rm cb}(A_4)=1=4-\lfloor\log_22\cdot4\rfloor$ for the $r=4$ crosspolytope (**matches the
dossier's tag (31)**, line 2441).

### 9.1 The S9 NAE star, exactly — and a correction to the campaign digest

**[EXACT FINITE CERTIFICATE]** Recomputed from scratch: $|A|=54$, projective full dual
$=\{x_i,z_i,q\}\cup\{Y_1,Y_2,Y_3\}$ (10 forms — matching S9 tag (32), line 9568), $L=19/27$,
$\ell=7-\log_254=3\beta=1.2451\ldots$

| quantity | value | note |
|---|---|---|
| $d_{\rm cb}$ (unrestricted basis) | **2** | witness below |
| optimal boundary-preserving certificate | $(\dim R,\lambda)=(2,1)$ | 168 of 10976 certificates |
| **min leak over ALL 10976 boundary-preserving certificates** | **1** | exhaustive; **independently confirms S9 pp.153–154's forced-leak proof** by a different method |
| naive certificate (basis $=$ coordinates, every $Y_i\mapsto q$) | $(3,3)$ | occurs in only **4** of 10976 certificates |
| $d_{\rm cb}/\ell$ | $2/1.24511=1.6063$ | below the $1/\beta=2.4094$ floor |
| optimal $\lambda/L$ | $27/19=1.4211$ | |
| optimal $\dim\frac{R+R_<}{R_<}\big/L$ (at $R_<=0$) | $54/19=2.8421$ | |

Explicit optimal witness ($d_{\rm cb}=2$), verified by hand: basis
$\{x_1,z_1,x_2,z_2,x_3,z_3,\,Y_3\}$; selectors $q\mapsto-z_2$, $Y_2\mapsto x_2$, $Y_1\mapsto z_3$; residuals
$z_2+q$ (used twice — $Y_2-x_2=z_2+q$) and $x_1+z_1-z_3+q$. So $R=\operatorname{span}\{z_2+q,\ x_1+z_1-z_3+q\}$,
$\dim R=2$, and $R\cap B=\operatorname{span}\{z_2-x_1-z_1+z_3\}$, $\lambda=1$.

**Correction.** `STATE.md` records the star as giving "constant $\ge81/19\approx4.26$ naive" and leak rank 3. The
naive figure is correct as stated (it is labelled naive) but it is the **worst** of 10976 certificates, realised by 4
of them; the optimum is leak $1$ and total $2$. **Honest floors from the star are $\lambda/L\ge27/19=1.42$ and
$\dim\frac{R+R_<}{R_<}/L\ge54/19=2.84$, not $4.26$.** Any downstream use of $4.26$ as a floor overstates by $3\times$.
(The star's floor $2.84$ does exceed the $2.409$ three-circuit floor, but only for the *rooted* statement at $R_<=0$,
which S14 §7 already kills for absolute constants; the star's *unrooted* ratio $1.61$ does **not** improve the
$2.409$ floor.)

### 9.2 Exhaustive census of $d_{\rm cb}/\ell$ for $r\le5$

**[EXACT, EXHAUSTIVE]** All spanning antipodal fibres $A\subseteq\{\pm1\}^r$:

| $r$ | spanning fibres | exact $d_{\rm cb}$ computed | skipped by the sound filter $d_{\rm cb}\le|D|-r$ | max $d_{\rm cb}/\ell$ |
|---|---|---|---|---|
| 3 | 5 | 5 | 0 | $2.40942=1/\beta$ (NAE three-circuit, $|A|=6$) |
| 4 | 151 | 151 | 0 | $2.40942=1/\beta$ ($|A|=12$) |
| 5 | **60879** | 1092 | 59786 | $\le2.40942$; max among the 1092 computed $=1.6769$ |

The $r=5$ spanning count **60879 exactly matches the dossier's own enumeration line** (`FULL r=5: subsets=65535
spanning=60879 closed=16907 …`, line 2949 [S1 p.73]) — an independent cross-validation that my fibre semantics are
the packet's. The filter is sound ($d_{\rm cb}\le|D|-r$ by §8), so the skipped fibres provably cannot exceed
$1/\beta$; the value $1/\beta$ is attained at $r=5$ by the three-circuit plus two free coordinates ($d_{\rm cb}=1$,
$\ell=\beta$, verified by hand — the census filtered it as "cannot exceed").

**[CONJECTURE, supported by an exhaustive $r\le5$ census, the named families below, and nothing else]**
**Conjecture RC (sharp homogeneous constant).**
$$d_{\rm cb}(A)\ \le\ \frac{\ell(A)}{\log_2(4/3)}\qquad\text{for every spanning full-closed fibre},$$
with equality for products of NAE three-circuits. Equivalently: *every forced residual direction costs at least one
minimal Littlewood–Offord charge $\beta=\log_2(4/3)$ of defect* — the same constant that floors the packet's own
per-batch charge $c_s\ge\beta$ (line 8923). Consistency: rooted NAE cycle $1.0902$; crosspolytope $\to1$;
NAE star $1.6063$; slice-rooted NAE cycles $\to1.0902$; three-circuit products $=2.4094$ — **and this last is the
dossier's own arithmetic**, S6 §5 item 1, line 6890: "for $t$ factors, $\ell=t\log_2(4/3)$ and $d_{\rm cb}=t$", which is an
independent confirmation of my census's maximiser (I found this passage only on the second search, after the census
had already picked out that family). This is a **strengthening** of the dossier's (3) with the constant pinned, hence
strictly more falsifiable — a sharper target for the counterexample lane than "is (3) true".

---

## 10. Ledger: what this lane moved, and what it did not

| item | status |
|---|---|
| (R1) rooted target splits as quotient $+$ leak; (41) $\equiv$ [quotient bound] $+\ \lambda=0$, so two things remain open, not one | PROVED (elementary) |
| (R2) leak $=\dim\overline B(\ker P)$ = excess rank | PROVED |
| (R3) Theorem 1 is $2\nu+L$; $\kappa,\kappa_{\rm avg},4^L$ are estimates of $\nu$; crosspolytope is not a counterexample to the $\nu$-form | PROVED |
| (R4) on the high-$\kappa$ horn the support route is forced to $\Theta(\log n)\cdot L$ in the threshold window | PROVED **conditional on the dossier's class characterisation** |
| Target R-C: what a proof must supply — factor-$\Theta(\log n)$ rank compression inside the core | FORMULATION (not a theorem) |
| Lemma DRR: $U$-locality $\Rightarrow d_{\rm cb}\le d^*_{\rm cb}(\text{contraction})+1$, independent of $|U|$ | PROVED; **proves entropy §5a's "+1" in general** |
| all full-dual forms have support $\le16\cdot4^\ell$; residuals ternary with support $\le36\cdot4^\ell$ | PROVED (elementary LO) |
| (R5) witness exchange densifies unless rows are aligned; the p.52 extraction attack needs alignment | PROVED |
| (R5b) $\kappa=O(1)$ is strictly stronger than the target ($m$-slice: $\nu\asymp4^\ell$, $d_{\rm cb}=1$) | PROVED |
| (R7) $\dim\frac{R+R_<}{R_<}\le2\nu+L+\mu$ with no absorption hypothesis; absorption needed only when $\mu\gg L$ | PROVED |
| whether residual-class blocks have $\mu=O(L)$ | UNKNOWN — cheapest unexplored hypothesis |
| NAE star exact: $d_{\rm cb}=2$, forced leak exactly 1, optimum $(2,1)$; digest's 4.26 is the worst case | EXACT FINITE CERTIFICATE; corrects a campaign number |
| $r\le5$ census: nothing exceeds $1/\beta$; $r{=}5$ spanning count matches the dossier | EXACT, EXHAUSTIVE |
| Conjecture RC ($C=1/\beta$ sharp) | CONJECTURE, small-rank evidence only |
| S6 §6's class-property list ("no large disjoint-support matching") is consistent with, and composes with, (R4) | VERIFIED against the source |
| **the block-internal certificate for dense connector-incoherent cores** | **NOT MOVED.** DRR covers exactly the aligned case, which is what incoherence denies |

**Process note, worth keeping.** Three claims in the first draft of this memo were absence claims ("not packaged
anywhere in the dossier", "'useful junction basis' is nowhere defined", "the dossier does not state the interface
size"). A second, differently-worded search — run only because the campaign's own scar file insists an absence claim
carries the burden of a working detector — overturned the first, weakened the second, and confirmed the third with the
search now documented and a positive control. It also handed me two corroborations I would otherwise have missed
(S6 §5 item 1 confirming the census maximiser; S6 §5 item 5 as a second instance of the DRR mechanism) and one class
property (S6 §6) that composes with R4. **The first-pass draft was wrong about the dossier in exactly the way the
scar predicts.**

---

## 11. Strongest case this is wrong

Written before finishing, against my own chain, in decreasing order of how much it would cost me.

1. **R4 rests entirely on a dossier assertion I cannot verify.** The class characterisation "$\kappa\gtrsim\log n$ in
   every useful junction basis" (line 1305) is an assertion of the packet, not a theorem reproduced in it, and
   the *qualifier* "useful" is undefined. (Second search, `junction`: 5 hits, lines 1305, 2887, 8766, 12485, 12898.
   "Junction basis" itself **is** operationally pinned — line 12485: "an incoming junction basis containing $A$ and
   otherwise disjoint from the private coordinate span" — so my earlier reading that the whole phrase is undefined was
   too strong; what is undefined is which junction bases a proof is entitled to call *useful*, i.e. the quantifier R4
   ranges over. The block-formation layer that would settle it is inherited from the missing earlier tree, the same
   hole the telescope reconstruction hit.) If the class in fact admits bases with $\kappa=o(\log n)$ that the packet's authors
   did not find, R4 evaporates — and so does the open problem's first horn. **Worse for me: the characterisation is a
   disjunction**, and R4 says nothing at all about the second horn (common-lift failure), which is where the star and
   the $m=1$ interval live. So R4 covers at most half the class. The concrete check that would settle it: exhibit one
   explicit member of the residual class and compute $\min_{\text{basis}}\nu$. Three separate passages characterise the
   class by properties (p.52 lines 1303–1306; S1 §9 lines 2877–2889; S6 §6 lines 6985–7005) and none exhibits a member —
   which is what one expects of a *residual* class, but it does mean R4's quantifier has never been tested against a
   concrete object, mine or theirs.
2. **R3 may be a repackaging with no content.** In the unrooted case $\dim\frac{R+B}{B}\le q$ is trivial, so (R3)
   beats the trivial bound only when $\nu\ll q$, and its "improvement" on the crosspolytope is a factor 2 over trivial.
   If the packet's authors always intended $\kappa$ as a *hypothesis class label* rather than as the operative
   parameter, §3 is prose, not mathematics. My defence is only (R4): the $\nu$-form is what makes the deficit
   computable, and the deficit computation is the lane's actual output.
3. **The census could be measuring a slightly different object than the packet's $d_{\rm cb}$.** I enumerate over
   $\mathbb K=\mathbb Q$; the packet also allows $\mathbb F_p$, $p$ odd (line 8860), where the full dual can be larger
   and $d_{\rm cb}$ could differ. I did not check a single $\mathbb F_p$ case. Also $r\le5$ is very small: the ratio
   could grow with $r$ and cross $1/\beta$ only for large $r$ — the NAE cycle family *decreases* to $1.09$, which is
   consistent with a maximum at small $r$, but a family engineered to beat $1/\beta$ would most plausibly be built at
   $r\ge8$ where I have no data. **Conjecture RC is the weakest-supported claim in this memo and I would not build on it.**
4. **Lemma DRR may be a theorem about the solved families only.** $U$-locality holds for the $m$-slice and (by the
   entropy lane's enumeration) for slice-rooted NAE cycles — both *solved*. If no residual-class block is $U$-local,
   DRR contributes calibration and a corroboration of §5a, nothing more. I state this in §5 but it deserves repeating:
   **I did not compress rank on a single block that is actually open.**
5. **(R1)/(R2) may be already-assumed folklore in the packet.** S9's Lemma-2 proof contains the same map; if the
   packet's authors had (R1) in mind, my "clause (i) splits into a quotient bound and a leak" is a restatement. It changes
   what to attack only in combination with the telescope draft's (T1a), which is **UNREFEREED** — if (T1a)'s filtration
   bookkeeping is wrong, §2's conclusion ("clause (ii) is not needed") is wrong with it, and §7's $\mu$-hypothesis
   loses its purpose.
6. **The star correction could be the one thing here that is simply an error.** $d_{\rm cb}=2$ contradicts my own
   first guess of 3 and contradicts the shape of the digest's numbers. I therefore checked it three ways: the
   branch-and-bound search, a separate full-enumeration script, and by hand (the witness in §9.1 — verify it: the seven
   basis forms are independent since $q$ enters only through $Y_3$; $Y_2-x_2=z_2+q$ equals the $q\mapsto-z_2$ residual;
   $Y_1-z_3=x_1+z_1+q-z_3$). If a reader finds a fourth full-dual form of the star I missed, everything in §9.1 moves.
   The forced-leak count (min leak $=1$ over all 10976 certificates) is the claim I am most confident of, because it
   *agrees* with S9's independent argument.
7. **Compute-policy honesty.** The $r=5$ census ran 609 s single-threaded (I planned "a couple of minutes"), at normal
   priority, on the local machine — over budget for polite mode. No research box was touched, nothing was written
   outside the scratchpad and this file, and I did not repeat it.

---

## 12. Next concrete step

**One item, bounded, decides the most.** Compute $\mu$ — the unpaid boundary rank of §7 — and $\dim\Pi^0_U$ of §5 for
the *smallest incoherent dense examples we actually possess*: the dense NAE stars $A(s_1,\ldots,s_k)$ of entropy §5b
(already enumerated there: $(4,4,4)$, $(6,4,2)$, $(4,4,4,4)$) and the S9 star, in each case as a *rooted block inside a
two-level tree* rather than in isolation. Three outcomes, all decisive:

* if $\mu=O(L)$ on these, then (R7) gives the rooted estimate with **no connector hypothesis at all** on the family the
  packet built to force one, and the correct next move is to ask whether the residual class inherits it (§7.3);
* if $\mu\gg L$ but $\dim\Pi^0_U=O(\ell)$, then DRR-style contraction is the live mechanism and the next move is to
  prove a contraction lemma for $\dim\Pi^0_U>1$;
* if both blow up, Target R-C is where the whole programme must be attacked, and the counterexample lane should hunt in
  the $\ell\approx\frac12\log_2m$ regime (entropy Gap 2 = my §5 self-similar core) with the §8 counting bound and
  Conjecture RC as the sharp target — a fibre with $d_{\rm cb}/\ell>1/\beta$ would refute RC, and one with
  $d_{\rm cb}/\ell\to\infty$ would refute (3) and redirect Layer III entirely.

Cost: exact arithmetic on fibres of size $\le2\cdot10^4$ already enumerated by the entropy lane; minutes, local, no
boxes. Do **not** build on Conjecture RC or on (T1a) before their referees.

---
*Honesty footer: the sharp Rademacher singularity conjecture is OPEN and nothing above bears on its truth. The named
gap — the block-internal certificate for dense connector-incoherent cores — was not moved by this lane; the lane's
contribution is a proof that the packet's own main tool cannot move it (§4), an exact statement of what would
(§4, Target R-C), one working compression mechanism with its exact scope (§5), a proved rooted bound that needs no
absorption clause (§7), and two exact corrections/confirmations of campaign numbers (§9).*
