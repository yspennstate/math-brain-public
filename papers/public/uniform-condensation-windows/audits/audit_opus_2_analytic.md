# Audit 2 (adversarial) — the analytic engine: §4 geometric records, §6 deterministic margins

**VERDICT: HOLDS UNDER ATTACK.** Every load-bearing step of §4 and §6 survived exact re-derivation
and 4,000+ exact-arithmetic adversarial trials; the four defects I found are statement-level
(an unconstrained `arg max`, three asserted-but-unproved one-liners), none of them changes a constant,
a direction, or the truth of any displayed inequality, and the constant dependency graph is acyclic.
The verdict rests on the symbolic re-derivation of every step (each is a one-directional bound on a sum of
nonnegative terms with an explicitly recomputed coefficient); the exact-arithmetic runs corroborate it and
probe tightness, but no finite search could establish it, and I say where my tests cannot reach.

**Equation numbering.** `amsart` numbers straight through, so the PDF numbers are **not** section-relative
and do not match the numbering used in my instructions. Map (extracted from `main.pdf`,
`agent2_scratch/pdf_text.txt`): `eq:records`=(8) L276, `eq:active`=(9) L285, `eq:plateausum`=(10) L295,
`eq:theta`=(11) L327, `eq:kernelsum`=(12) L334, `eq:start`=(13) L370, `eq:greedy`=(14) L390,
`eq:energy`=(15) L424, `eq:margin`=(16) L426, `eq:marginlimsup`=(17) L433, `eq:recurrence`=(18) L442,
`eq:kappa`=(19) L447, `eq:explicitC`=(20) L482, `eq:finiteprefix`=(21) L491, `eq:prefixmax`=(22) L497,
`eq:parameters`=(23) L524. I cite `\label` + `main.tex` line below.

---

## CONSTANT DEPENDENCY GRAPH (item 8d — the highest-value check)

Read "X ← Y" as "X is chosen after Y and may depend on it". **The graph is acyclic**; the paper states
the order explicitly at L529 ("Every parameter is now fixed, before letting $J\to\infty$") and L420,
L369–379, and the statement is accurate.

| constant | chosen after | constraint it must satisfy | where |
|---|---|---|---|
| $w$, span-1 normalization | — | $w_0=1$, $\limsup w_j^{1/j}=\infty$ | L120–124, L182–186 |
| $\varepsilon,\alpha,\beta$ | — | $\varepsilon\in(0,1)$, $0<\alpha<\beta<\infty$ | L521 |
| $a$ | $\varepsilon$ | $a>1$; implicitly $a<\dfrac1{1-\varepsilon}$ (else no $\delta>0$ solves (23)) | L521 |
| $b$ | — | $b=4$ (needs only $b>2$, used for $\sum j^{1-b}<\infty$ at L538) | L522 |
| $B_i,s_i,p_i,d_i,\mathcal A$ | $w,a,b$ | (8); ladder is re-built for each $\varepsilon$ (each $a$) | L276 |
| $D$ | $a$ | $D\ge2$, $\Theta(a,D)<1/4$. **Does not depend on $i_0$** — essential, and true, since $\Theta$ is a function of $(a,D)$ only | L327, L522 |
| $\Theta,C_a$ | $a,D$ | $C_a=2a^2$, $\Theta=2a^{3-D}\!\big(\tfrac{D-1}{a-1}+\tfrac1{(a-1)^2}\big)$ | (11) L327 |
| $\delta$ | $a,D,\beta,\varepsilon$ | $0<\delta<\min\{a^{-D}/100,\ \tfrac1{100(1+\beta)},\ \tfrac1{100}\}$ and $\tfrac1{a(1+5\delta)}>1-\varepsilon$. **All upper bounds** — no lower bound on $\delta$ occurs anywhere ($\delta k\ge1$, $2\delta k\ge h_*$ are conditions on $k$, not on $\delta$) | (23) L524 |
| $K$ | $\beta$ | integer $K\ge4(1+\beta)$; delivers $nK\ge2m$ | L528, L577 |
| $h_*$ | $w$ only | semigroup of a finite gcd-1 supported set contains $[h_*,\infty)$ | L360–367 |
| $i_0$ | $w,a,b,K,h_*$ | $s_i\ge K$ and $B_i\ge0$ for $i\ge i_0$; $a^{i_0}\ge h_*$. Solvable because $s_i\to\infty$, $B_i\to\infty$ | (13) L370 |
| terminal reps, $C_*$, $C_0$ | $i_0,w$ | cover $h_*\le v<2a^{i_0}$; $C_*\ge$ #parts; $C_0\ge0\ge-\log(\text{product weight})$ | L375–379 |
| $M$ | $i_0,a$ | $M=\lceil2a^{i_0}\rceil$ | L377 |
| $\Pi$ | $a,b,i_0$ | $\frac{a}{(a-1)^2}\big(p_{i_0}+ba\log a\cdot U_{i_0+1}/a\big)$ | L477 |
| $J_0$ | $M,a,i_0,D$ ( + $T$ in Lemma 6.1 only) | $J_0\ge i_0+D$ and $\kappa=Ma^{1-J_0}/(a-1)<1/4$; in Lemma 6.1 also beyond the threshold past which $G_J\le T$ | (19) L447, L480 |
| $\kappa$ | $M,a,J_0$ | $<1/4$ | (19) |
| $\mathcal C$ | $\Theta,C_a,\Pi,M,C_0,b,a,B_{i_0},B_{J_0-1},T_{J_0},U_{J_0}$ | finite, $\ge0$, independent of $N$ | (20) L482 |
| $C_2,C_3,C_4$ | $C_0,T$ / $M,B_{J_0-1},a,J_0$ / all of the above | independent of $N$ | L444, L461, L463 |
| $C$ (certificate) | $C_*,\beta,\delta$ | $\max\{1,2^{C_*+3}\beta\delta/(1+3\delta)\}$ | (26) L548 |
| $N$, $J\to\infty$ | everything | last | L529 |

**No cycle.** The two places a cycle would be fatal, and why neither exists:
* $M=\lceil2a^{i_0}\rceil$ is fixed **before** $J_0$, and $\kappa<1/4$ is achieved by enlarging $J_0$ with $M$ already fixed — not the reverse. ✔
* $D$ is fixed **before** $i_0$ and $\Theta$ contains no $i_0$; $\delta<a^{-D}/100$ is an upper bound on a quantity nothing else bounds below. If $\Theta$ had depended on $i_0$ (e.g. through the truncated lower limit) the choice $D\!\to\!i_0\!\to\!M\!\to\!J_0$ would still be acyclic, but $\delta$ would then depend on $i_0$ and $i_0$ on $K$ only — still acyclic. ✔

One consequence worth stating in the paper: **the whole ladder ($a,D,\delta,K,i_0,M,J_0,k_r$) depends on $\varepsilon$**, so Corollary 2.2's diagonal over $\varepsilon=1/r$ (L631–633) uses a *different* record ladder for each $r$. That is legitimate (sizes are chosen increasing), but it is invisible in the current text.

---

## FINDINGS

### F1 — MINOR (defining display is formally ill-posed) — `eq:records`, main.tex L279, PDF (8)
```latex
 s_i=\min\operatorname*{arg\,max}_{s}\frac{\log w_s+b\log s}{s},
```
The `arg max` carries **no range**. Read literally it is over all $s\ge1$ with $w_s>0$, where under
zero radius $\sup_s(\log w_s+b\log s)/s=+\infty$ is not attained, so the arg max set is empty and
$s_i$ — hence $p_i$, (9), (14), $E_J$, $G_J$ and all of §6 — is undefined. Confirmed present in the
rendered PDF (`agent2_scratch/pdf_text.txt`: `si=minargmaxslogws+blogss`). Every use in the paper is the
constrained one, so this is a typesetting omission in the paper's central definition. Fix:
```latex
 s_i=\min\operatorname*{arg\,max}_{\substack{1\le s\le\lfloor a^i\rfloor\\ w_s>0}}
       \frac{\log w_s+b\log s}{s},
```

### F2 — MINOR (three unproved assertions carrying §4) — main.tex L282 and L289
"Then $B_i$ is nondecreasing and tends to infinity. Also $s_i\to\infty$." and "At inactive indices the
smallest maximizing index remains unchanged." No argument is given for any of the four claims, and the
last one is the engine of Lemma 4.1 (it is what makes $p_i$ constant on plateaus). All are true; each is
one line. Suggested replacement:
```latex
The feasible set in \eqref{eq:records} grows with $i$, so $B_i$ is nondecreasing. If
$w_{j_\ell}^{1/j_\ell}\to\infty$ along a subsequence, then $B_i\ge j_\ell^{-1}\log w_{j_\ell}$ once
$\lfloor a^i\rfloor\ge j_\ell$, because $b\log j_\ell\ge0$; hence $B_i\to\infty$. At a fixed $s$ the
quotient in \eqref{eq:records} is a fixed finite number, so no $s$ can be maximizing for arbitrarily
large $i$, and $s_i\to\infty$. Every index admissible at step $i$ but not at step $i-1$ exceeds
$\lfloor a^{i-1}\rfloor\ge s_{i-1}$; so at an inactive index the least maximizer is unchanged, and
$s_i$, $p_i$ are constant on each plateau of $B_i$.
```

### F3 — MINOR (two gaps in (9)) — `eq:active`, main.tex L285–288, PDF (9)
**(a) The floor.** The stated lower bound is $a^{J-1}<s_J$, but the argument behind it ("otherwise $s_J$
was already available at step $J-1$") only yields $s_J>\lfloor a^{J-1}\rfloor$, because the range in (8)
is $s\le\lfloor a^i\rfloor$. The clean inequality *is* true — $s_J$ is an integer, so
$s_J\ge\lfloor a^{J-1}\rfloor+1>a^{J-1}$ — but that integer step is never written. I chased the floor
through **every** later use; all five are correct as written:
$1/s_J<a^{1-J}$ (L440, L458, L516) — the one place that genuinely needs the integer step, though even
$1/s_J\le a^{1-J}$ would suffice, since it is only ever summed against $T_{J_0}$;
$u=\lfloor a^{J-1}\rfloor<k=s_J$, the hypothesis $u<k$ of Lemma 3.1 (L530, L198) — needs only
$s_J>\lfloor a^{J-1}\rfloor$; $q_j\le j^{-b}$ for $1\le j\le u$ (L536) — needs $u$ to be exactly the floor,
which is how it is defined at L530; $c=a^\ell/s_\ell\le a$ in the $p_\ell$ bound (F4); and
$u/m\ge(a^{J_r-1}-1)/((1+5\delta)a^{J_r})$ (L605) — uses $\lfloor x\rfloor>x-1$.
Fix: add after (9) — `Indeed $s_J>\lfloor a^{J-1}\rfloor$, since every index at most $\lfloor a^{J-1}\rfloor$ was already available at step $J-1$; as $s_J$ is an integer, $s_J\ge\lfloor a^{J-1}\rfloor+1>a^{J-1}$.`

**(b) The identity is stated only at active $J$ but used at inactive $i$.** (9) records
$\log w_{s_J}=s_JB_J-b\log s_J$ "at an active index $J$". Lemma 5.1's proof uses it at an arbitrary stage
index $i$, which is typically **inactive**: "At stage $i$ the logarithmic weight per unit mass is
$B_i-p_i$" (L412) — and that line is what produces $E_J$, hence $G_J$, hence everything in §6. The
identity holds at *every* $i$ by the definition of $s_i$ as a maximizer; say so, e.g. replace the second
half of (9) by a separate sentence: `By definition of $s_i$, $\log w_{s_i}=s_iB_i-b\log s_i$ at every index $i$, active or not.`

### F4 — MINOR (asserted bound whose obvious proof needs a hypothesis that is not imposed) — Lemma 4.1 proof, main.tex L307–310
"For an active $\ell$, (9) gives $p_\ell\le ba\ell(\log a)a^{-\ell}$."
The natural derivation — monotonicity of $x\mapsto\log x/x$ on $[a^{\ell-1},\infty)$ — requires
$a^{\ell-1}\ge e$, which is **not** among the conditions (13) that $i_0$ must satisfy (L370: only
$s_i\ge K$, $B_i\ge0$, $a^{i_0}\ge h_*$) and which fails for the small $\ell$ that occur when $a$ is close
to one, precisely the regime §7 requires. The inequality is nevertheless **true with no extra hypothesis**;
the two-line proof avoids monotonicity entirely. Fix:
```latex
For an active $\ell$, write $s_\ell=a^\ell/c$ with $c=a^\ell/s_\ell\in[1,a)$ by \eqref{eq:active}. Then
$\log(s_\ell)/s_\ell=c\,(\ell\log a-\log c)\,a^{-\ell}\le a\ell(\log a)a^{-\ell}$, so
$p_\ell\le ba\ell(\log a)a^{-\ell}$, which is summable.
```
Evidence: `agent2_scratch/a2_sec4.py::check_p_bound` — 865 exact cases over
$a\in\{2,\tfrac32,\tfrac54,\tfrac{21}{20},\tfrac{101}{100},3,10\}$, $\ell\le59$, $s$ at both ends and the
midpoint of each window, rigorous rational log brackets: **0 violations, tightest ratio 0.9831**;
`a2_sweep.py` — 0 violations over 4,000 random $(a,D,i_0,N,\text{pattern})$ configurations, tightest 0.9877.

### F5 — EDITORIAL — Lemma 6.2 proof (main.tex L503–518) and Lemma 6.1 proof (L456–464)
* The step $E_J/s_J\le a^{1-J}E_J$ is never written; it is compressed into "the bounds from the preceding
  proof" (L506). It needs $E_J\ge0$ — true, but itself requiring $B_{J-1}\ge0$ from (13), $B_{J-1}\ge B_i$,
  $p_i\ge0$, $C_0\ge0$ — and $s_J>a^{J-1}$ (F3a). One sentence fixes it.
* $C_3$ (L461) and $C_4$ (L463) appear undefined. $C_3=MB_{J_0-1}a^{2-J_0}/(a-1)=MB_{J_0-1}T_{J_0}$;
  $C_4=\Theta(B_{J_0-1}-B_{i_0})+C_a\Pi+MB_{J_0-1}T_{J_0}+b(\log a)U_{J_0}+C_2T_{J_0}$ — i.e. (20) with
  $C_0$ replaced by $C_2$. Worth displaying, since "independent of $N$" is the crux.
* Logically **Lemma 6.1 is a corollary of Lemma 6.2** (which assumes nothing): (22) plus $B_N\to\infty$
  gives it at once. The paper proves 6.1 by contradiction and then derives 6.2 "from the preceding proof",
  which invites the reader to suspect circularity. There is none — the two reused bounds (Lemma 4.2 for the
  memory term, and the Abel bound on $M\sum a^{1-J}B_{J-1}$) contain no occurrence of $T$, and $C_2$ is the
  only $T$-dependent object and does not appear in 6.2. Add one sentence saying so, or reverse the order.

### F6 — EDITORIAL — not a defect, recorded for cross-audit
No section-relative equation numbering (see map above). If the three audits are merged, reconcile citations
by `\label`, not by number.

**Nothing in scope rises to GAP or FATAL.**

---

## WHAT I TRIED THAT DID NOT BREAK IT

Scripts are in `agent2_scratch/`; all arithmetic is `Fraction`/`int`,
logs are rigorous rational brackets from 80–120-digit `Decimal.ln()` padded by $10^{-60}$/$10^{-90}$, and every
inequality is evaluated in the direction that would *break* the paper. Baseline: the paper's own
`check_full_path.py` and `check_uniform_windows.py` both run clean (`ALL_EXACT_CHECKS_PASS`, exit 0;
`paper_full_path_out.json`, `paper_uniform_out.json`); their $\Theta=11/128$, $\kappa=1/4096$ reproduce mine.

1. **$B_i$ nondecreasing, $B_i\to\infty$, $s_i\to\infty$ (item 1, 2).** All three hold; the sparseness of the
   $\limsup$ subsequence is irrelevant because $B_i$ is monotone (sparseness costs rate, not the limit).
   $s_i\to\infty$ is airtight and in fact **stronger than claimed**: $s_i$ is nondecreasing, and at an active
   $J$ strictly increasing, because the candidate set only ever gains indices above $\lfloor a^{J-1}\rfloor$;
   the min-tie-break cannot oscillate downward. $B_i\ge0$ in (13) is reachable since $B_i\to\infty$;
   the "sufficiently large $i$" caveat is respected at every later use (all uses are at indices $\ge i_0$,
   and $J_0-1\ge i_0+D-1$).
2. **The floor chase (item 3).** Done exhaustively — see F3(a). Result: the clean $a^{J-1}<s_J$ is *true*, so
   the five downstream uses are all correct. This was the most likely place for a fatal off-by-one and it is
   not one.
3. **$p_\ell\le ba\ell(\log a)a^{-\ell}$ (item 4).** True with no hypothesis (F4); 865 + 4,000 exact cases,
   0 violations (`a2_sec4.py`, `a2_sweep.py`).
4. **Plateau bookkeeping and the constant $a/(a-1)^2$ (item 5).** Recomputed independently:
   $\sum_{i=\ell}^{v-1}a^i=\frac{a^v-a^\ell}{a-1}<\frac{a^v}{a-1}$ and $\sum_{J\ge v}a^{-J}=\frac{a^{1-v}}{a-1}$,
   product exactly $\frac{a}{(a-1)^2}$ — the paper's constant is right, not merely safe. The "only active
   $J\ge v$ can be charged" step holds for $D\ge1$ (cutoff $\ell-D\le\ell-1<\ell$) and a fortiori $D\ge2$.
   Every $i\ge i_0$ lies in exactly one plateau, so the charge assignment is exhaustive and not double-counted.
   Brute force over long plateaus, singleton plateaus and $D\in\{1,2,3,11\}$, $a\in\{2,\tfrac32,\tfrac54,\tfrac{21}{20}\}$:
   96 exact cases, worst LHS/RHS **0.4708** (`a2_sec4.py::check_plateau`); 4,000 random configurations,
   worst **0.6670**, 0 violations (`a2_sweep.py`).
5. **Kernel coefficient and $\Theta$ (item 6).** Both branches re-derived: for $t\le D-2$ the min is $J-D$ and
   the sum is $a^{1-D}/(a-1)$; for $t\ge D-1$ the min is $\ell-1$ and the sum is $a^{-t}/(a-1)$; **the two
   agree at the boundary $t=D-1$**, so the paper's split $\{1\le t\le D-1\}\cup\{t\ge D\}$ is consistent.
   Summing: $\frac{(D-1)a^{1-D}}{a-1}+\frac{a^{1-D}}{(a-1)^2}$, times $C_a=2a^2$, gives exactly
   $2a^{3-D}(\frac{D-1}{a-1}+\frac1{(a-1)^2})$ — yes, $2a^2\cdot a^{1-D}=2a^{3-D}$, and the whole chain checks.
   Extending $J$ to all integers and $i$ to $-\infty$ is legitimate (every term nonnegative, superset of
   indices); the left side's restriction to active $J$ against the right side's sum over all $\ell$ is also
   fine, since $d_\ell=0$ at inactive $\ell$ and the $\ell$-range $[i_0+1,N-1]\subseteq[i_0+1,N]$.
   Verified per-lag and in total for $a\in\{2,\tfrac32,\tfrac54,\tfrac{21}{20},\tfrac{101}{100}\}$,
   $D\in\{2,3,5,11,40\}$ (`a2_sec4.py::check_kernel_coefficient`). Brute-force inequality (12):
   133 structured exact cases, worst LHS/RHS **0.9375**; 4,000 random exact cases, worst **0.9893**,
   **0 violations**. The bound is essentially tight (ratio $\to1$ as all indices become active,
   $i_0\to-\infty$, $N\to\infty$) — which is why I looked hard for an overshoot; there is none, and the
   proof shows there cannot be, since the extension is a superset of nonnegative terms.
6. **$C_a=2a^2$'s origin and the division by $s_J$ (item 7).** $2a^{i+1}\cdot a^{1-J}=2a^2a^{i-J}=C_aa^{i-J}$ —
   exact. Direction: at an active $J$ the numerator $T+b\log k+E_J$ is bounded above by
   $C_2+b\log k+(E_J-C_0)$, every summand $\ge0$ ($C_2=\max\{0,C_0+T\}$ is exactly the device that absorbs a
   negative $T$; $E_J-C_0\ge0$ needs $B_{J-1}\ge B_i$, $p_i\ge0$, $B_{J-1}\ge0$; $b\log k\ge0$ needs $k\ge1$),
   so replacing $1/k$ by the larger $a^{1-J}$ is the correct direction. $\log k\le J\log a$ from
   $k\le\lfloor a^J\rfloor$.
7. **The self-reference (item 8).** (a) $S_N=B_N-B_{J_0-1}\to\infty$ ✔ ($B$ finite at each index since
   $w_s<\infty$). (b) Every term of $C_4$ traced: $\Theta(B_{J_0-1}-B_{i_0})$ from splitting
   $\sum_{\ell=i_0+1}^Nd_\ell=S_N+(B_{J_0-1}-B_{i_0})$; $C_a\Pi$ from Lemma 4.1; $MB_{J_0-1}T_{J_0}$ and
   $b(\log a)U_{J_0}+C_2T_{J_0}$ from geometric tails — **none depends on $N$ or on $B_N$**.
   The one dangerous step, $M\sum_{J=J_0}^Na^{1-J}B_{J-1}\le C_3+\kappa S_N$, re-derived line by line by Abel:
   $B_{J-1}=B_{J_0-1}+\sum_{\ell=J_0}^{J-1}d_\ell$; first piece $\le MB_{J_0-1}T_{J_0}$; swapping the order in
   the second gives $M\sum_{\ell=J_0}^{N-1}d_\ell\sum_{J\ge\ell+1}a^{1-J}=M\sum_\ell d_\ell\frac{a^{1-\ell}}{a-1}
   \le\frac{Ma^{1-J_0}}{a-1}(B_{N-1}-B_{J_0-1})\le\kappa S_N$. The coefficient is $\kappa<1/4$;
   **there is no hidden coefficient $\ge1$**. (c) index sets agree because $d_\ell=0$ at inactive $\ell$.
   (d) see the graph above.
8. **Lemma 6.2 term by term (item 9).** $d_J=G_J/s_J+b\log(s_J)/s_J+E_J/s_J$ is (16) divided by $k=s_J$ —
   an exact identity, no inequality. Summing over active $J\in[J_0,N]$ gives $\sum d_J=B_N-B_{J_0-1}$, and each
   of the five pieces of $\mathcal C$ in (20) matches the corresponding upper bound exactly, with nothing
   missing and nothing double-counted. $T_L=\frac{a^{2-L}}{a-1}$ and
   $U_L=a^{2-L}(\frac{L}{a-1}+\frac1{(a-1)^2})$ both verified by direct summation with exact tails for
   $a\in\{2,\tfrac32,\tfrac54,\tfrac{21}{20}\}$, $L\in\{0,1,5,18\}$, and the parenthetical
   "the sum in $\Pi$ equals $U_{i_0+1}/a$" is exact (`a2_sec4.py::check_closed_forms`). No power of $a$ is off.
9. **(22) and the negative margins (item 10).** $\sum_{J\ge J_0,\text{active}}1/s_J<\sum_{J\ge J_0}a^{1-J}=T_{J_0}$
   ✔ (needs F3a). The chain $\sum G_J/s_J\le\sum(G_J)_+/s_J\le\max(G_J)_+\cdot T_{J_0}$ is valid with negative
   $G_J$ present, and the paper's wording ("bounding each $G_J$ by the maximum of their positive parts")
   supports it. The empty-active-set convention is consistent, not vacuous: with no active $J$ in $[J_0,N]$ the
   left side is $0$, $B_N=B_{J_0-1}$, and the right side is $-\mathcal C\le0$ because $\mathcal C\ge0$
   (each of its five terms is $\ge0$, using $B_{J_0-1}\ge B_{i_0}$ and $B_{J_0-1}\ge0$).
10. **End-to-end on real weight sequences.** I built genuine zero-radius laws
    $w_s=s^{-b}e^{s\beta_s}$ (so the corrected slope at $s$ is exactly the rational $\beta_s$), computed
    $B_i,s_i,p_i,d_i$, the active set, $E_J$ and $G_J$ *literally from (8),(15),(16)*, and tested (21) and (22)
    for every prefix. Five adversarial families (`a2_sec6.py`, exit 0): $s_J$ at the **bottom** of its window
    $\lfloor a^{J-1}\rfloor+1$ (the paper's own script only ever uses the top, $s_J=a^J$, which is the *easy*
    end for every $1/s_J$ bound), all-indices-active with $d=10^{-3}$ and with $d=10^3$, nine-scale plateaus,
    $a=21/20$ with $D=220$, $a=3/2$ with sparse records. **No violation.** Tightest case: true cost
    $\sum(b\log s_J+E_J)/s_J=4547.4$ against the claimed bound $(\Theta+\kappa)S_N+\mathcal C=5741.5$,
    ratio **0.792**.
11. **Falsification test of Lemma 6.1 (the sharpest attack I have).** Instead of checking the paper's
    inequalities, I let an adversary *saturate* the hypothesis: choose the record increments as large as
    $G_J\le T$ permits, at **every** scale, with $s_J$ at the bottom of its window (which maximises
    $d_J=(T+b\log s_J+E_J)/s_J$), and $\log s_J$ at its upper bracket. If $B_N$ could diverge here, Lemma 6.1
    would be false. It does not: `a2_falsify.py` (exit 0) gives $B_N\to0.0707$ ($a=2,D=11,M=32,T=0$),
    $288.703$ ($a=2,D=10,T=10^6$), $0.2901$ ($a=3/2,D=17$), with the last increment collapsed to
    $10^{-19}$–$10^{-22}$ by $N=140$–$200$. The contradiction in Lemma 6.1 is a real contraction, not a
    hair's-breadth estimate.
12. **Non-vacuity (item 11) — explicit triples, exact rationals** (`a2_feasible.py` /
    the binary-search rerun): for $\beta=2$ (and identically for $\beta=100$, which only moves $K$),

    | $\varepsilon$ | $a$ | $D$ | $\Theta(a,D)$ | $\delta$ | $K$ | $\frac1{a(1+5\delta)}$ vs $1-\varepsilon$ |
    |---|---|---|---|---|---|---|
    | $0.1$ | $19/18$ | 194 | 0.24871 | $1.392\cdot10^{-7}$ | 12 | $0.94737>0.9$ ✔ |
    | $0.1$ | $91/90$ | 1250 | 0.24995 | $5.016\cdot10^{-9}$ | 12 | $0.98901>0.9$ ✔ |
    | $0.01$ | $199/198$ | 3072 | 0.24974 | $9.501\cdot10^{-10}$ | 12 | $0.99497>0.99$ ✔ |
    | $0.01$ | $991/990$ | 18689 | 0.24980 | $3.196\cdot10^{-11}$ | 12 | $0.99899>0.99$ ✔ |

    All of (23), $\Theta<1/4$ and $\delta<a^{-D}/100$ hold **simultaneously**, asserted by `assert` on exact
    `Fraction`s. The failure mode I was told to hunt — $(a-1)^{-2}$ blowing up forces $D$ up, which forces
    $\delta$ down — is real but harmless, because **every constraint on $\delta$ is an upper bound**; I grepped
    the whole argument for a lower bound on $\delta$ and there is none ($\delta k\ge1$, $2\delta k\ge h_*$,
    $\delta k\ge$ one integer in the window, $|I_r|\sim\delta k_r/\lambda$ are all conditions on $k$, satisfied
    since $k=s_J\to\infty$). The price is only that the first usable record is astronomically large
    ($k\gtrsim1/\delta\approx10^9$ at $\varepsilon=0.01$) and $J\ge i_0+3072$ — an asymptotic statement, not a
    vacuous one. **The theorem is not vacuous for any $\varepsilon\in(0,1)$**: any $a\in(1,\frac1{1-\varepsilon})$ works.
13. **Adjacent checks I made because §6 depends on them** (formally outside my scope, reported as clean):
    Lemma 5.1's greedy — $i\ge i_0$, $q\ge1$ (from $s_i\le a^i\le x/2$ and $h_*\le a^{i_0}\le x/2$),
    $h_*\le x'<h_*+s_i\le2a^i$, strict decrease of the scale index, one stage per index, every used index in
    $[i_0,J-D]$, stage deficit $qs_i(B_{J-1}-B_i+p_i)\le2a^{i+1}(\cdot)$, terminal deficit $\le MB_{J-1}+C_0$ —
    all correct, and (14) matches (15) verbatim. And the certificate's exponent: with $h=B_{J-1}$,
    $hk-\log w_k=-kd_J+b\log k$, so $hk-\log w_k+hr-\log W_r\le-G_J$ **exactly** — $G_J$ is precisely the
    right margin, which is the strongest evidence that §6 is estimating the correct quantity.
14. **What I could not break and why:** the only structurally suspicious steps are (i) the extension of
    the summation ranges in Lemma 4.2 and (ii) the conversion of the $B$-dependent terminal term into
    $\kappa S_N$. Both are one-directional bounds on sums of nonnegative terms with explicitly computed
    coefficients, and I reproduced both coefficients independently to the last power of $a$. There is no room
    in either for a coefficient $\ge1$: $\Theta\to0$ geometrically in $D$ and $\kappa\to0$ geometrically in
    $J_0$, and the two are controlled by parameters that are chosen in an order that is genuinely acyclic.

### Scope not covered
Lemma 3.1 (occupation-count insertion) and its labelled-box variant; the §5 semigroup claim; §7's
probabilistic content (Markov/pigeonhole, $A_J^n$ cancellation, dominated convergence for $\mu_J\to0$);
§§8–9 (paths, trees, sampling sharpness); the §10 finite illustrations. Other auditors own these.
