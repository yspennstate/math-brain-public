# Audit 1 — the finite combinatorial core

**Scope:** Section 3 (Lemma 3.1, eqs (4), (6), (7), both proofs), Section 5 (semigroup argument,
eq (13), Lemma 5.1, eq (14)), Section 10 and the checkers.

**Equation numbers below are the PDF's** (flat, not per-section): (4) = sharp insertion, (5) = the
two side conditions, (6) = coarse insertion, (7) = the weight-ratio identity, (8) = the record
definitions, (13) = the $i_0$ conditions, (14) = the greedy bound. The task brief's
"(3.1)/(3.2)/(3.3)/(5.1)/(5.2)" are (4)/(7)/(6)/(13)/(14).

---

## VERDICT

**HOLDS UNDER ATTACK** — with one genuine statement defect. Lemma 3.1 and its identity (7) are
**false as literally written** (they omit a factor $w_0^{-Q}$; explicit counterexample below), but
the omission is repaired by the standing normalization $w_0=1$ declared in Section 2, so no step
the paper actually performs is wrong; 20.1M exhaustive exact cases, an independent reproduction of
Table 1 to every printed digit, and an exact-rational re-run of the greedy at $a=101/100$ found
nothing else.

---

## FINDINGS

### F1 — MINOR (false as stated; no downstream effect). main.tex lines 237–241, eq (7); lines 204–216, eqs (4) and (6); the hypothesis list at line 198.

**What is wrong.** $\mathcal W(a)=\frac{n!}{\prod_j a_j!}\prod_j w_j^{a_j}$ includes the $j=0$
factor. Under $b_0=a_0-Q$ the weight part of the ratio is
$w_0^{b_0-a_0}\,w_k^{1}\prod_{0<j<k}w_j^{r_j}=w_0^{-Q}\,w_kW_r$, so the true identity is

    W(b)/W(a) = w_0^{-Q} * w_k * W_r * (a_0)_Q / prod_{0<j<k} prod_{l=1..r_j} (a_j + l).

Equation (7) prints it without $w_0^{-Q}$, and (4) and (6) inherit the omission. Lemma 3.1's
hypothesis list ("nonnegative integers $u,k,t,r,n$, with $n\ge1$, $u<k$, $w_k>0$, $m=t+k+r$") does
not contain $w_0=1$, so the lemma reads as a general finite inequality. It is not one.

**Counterexample** (`agent1_scratch/A_w0_attack.py`, exact integers):
$n=5$, $k=3$, $u=1$, $t=0$, $r=1$, representation = one part of size 1 ($R=0$, $C=1$, $Q=2$),
$K=2$, weights $w_0=W$, $w_1=w_3=1$, all others zero. Every hypothesis of Lemma 3.1 holds, and
both conditions of (5) hold ($nK=10\ge2m=8$; $t+1+R+C=2\le n/2$). Then $Z(4,5)=5W+20W^3$, while
(4) claims $Z(4,5)\ge 5W^5$ and (6) claims $Z(4,5)\ge\frac54W^5$:

| $w_0$ | $Z(4,5)$ | RHS of (4) | (4) holds | RHS of (6) | (6) holds |
|---|---|---|---|---|---|
| 1 | 25 | 5 | yes | 5/4 | yes |
| 3 | 555 | 1215 | **no** | 1215/4 | yes |
| 5 | 2525 | 15625 | **no** | 15625/4 | **no** |
| 8 | 10280 | 163840 | **no** | 40960 | **no** |

The corrected identity was then verified on 3,796 random $(a,\text{parts})$ pairs with random
$w_0$: zero failures. The identity as printed held on none of them with $w_0\ne1$.

**Second, independent derivation (no arithmetic).** $Z(m,n)$ is homogeneous of degree $n$ in the
weights. The right-hand side of (4) as printed is $w_k\cdot W_r\cdot Z_u(t,n)$ times a purely
combinatorial factor, i.e. degree $1+(R+C)+n=n+Q$. An inequality between a degree-$n$ form and a
degree-$(n+Q)$ form in the same variables cannot hold scale-invariantly, so (4) *must* carry a
normalization or a compensating $w_0^{-Q}$; with $w_0^{-Q}$ inserted both sides are degree $n$ and
the inequality becomes scale-free. This settles the finding without reference to any computation.

**Why no checker caught it.** `check_full_path.insertion_checks` hard-codes
`weights = {j: (1 if j == 0 else (j+1)**2+1)}`; `finite_window` hard-codes `{0:1,...}`;
`audit_stress_checks.randomized_insertion` compares only $\prod a_j!/\prod b_j!$, which is
weight-free; `labelled_double_counting` counts records **unweighted**. The single coordinate where
the paper is wrong is the one coordinate no script touches. (The author's own
`audits/02_finite_inequalities.md` writes the ratio "*after normalization $w_0=1$*" — the
condition was known and was lost in the transfer to the lemma.)

**Minimal fix (A, preferred).** Line 198, replace

```latex
Let $u,k,t,r,n$ be nonnegative integers, with $n\ge1$, $u<k$, $w_k>0$,
```

by

```latex
Let $u,k,t,r,n$ and $K\ge1$ be nonnegative integers, with $n\ge1$, $u<k$, $w_0=1$, $w_k>0$,
```

and after "Repeated sizes ... are allowed." (line 217) add

```latex
The normalization $w_0=1$ of Section~\ref{sec:results} is in force; for a general $w_0>0$ every
right-hand side above carries an extra factor $w_0^{-Q}$.
```

**Minimal fix (B, if the lemma is to stand alone).** Insert $w_0^{-Q}$ in (4), (6), (7):

```latex
 Z(m,n)\ge w_0^{-Q}w_kW_r Z_u(t,n)
 \frac{\fall{n-t}{Q}}
 {\displaystyle\prod_{j:r_j>0}\fall{\min\{n,\lfloor m/j\rfloor\}}{r_j}}
```

```latex
 Z(m,n)\ge\frac{n}{2^{C+1}}\,w_0^{-Q}w_k W_r Z_u(t,n)
```

```latex
 \frac{\mathcal W(b)}{\mathcal W(a)}
 =w_0^{-Q}w_kW_r\frac{\fall{a_0}{Q}}
 {\displaystyle\prod_{0<j<k}\prod_{\ell=1}^{r_j}(a_j+\ell)}
```

---

### F2 — MINOR (definitional). main.tex lines 276–281, eq (8).

**What is wrong.** The `\max` defining $B_i$ carries the range $1\le s\le\lfloor a^i\rfloor$,
$w_s>0$; the `\arg\max` defining $s_i$ carries only "$s$". Read literally, $s_i$ is the smallest
maximizer over **all** $s\ge1$ — which at zero radius does not exist, since
$\sup_s (\log w_s+b\log s)/s=+\infty$ by (1). As printed, $s_i$ (hence $p_i$, $E_J$, $G_J$,
$k=s_J$, and everything in Sections 5–7) is undefined.

**Why this is not pedantry.** $s_i\le\lfloor a^i\rfloor$ is load-bearing three times: it gives
$s_i\le a^i\le x/2$ hence $q\ge1$ in Lemma 5.1; it gives $h_*+s_i\le2a^i$ hence the strict
decrease of the geometric index; and it gives $s_J\le a^J$ in (9).

**Fix.** Lines 278–279, replace

```latex
 s_i=\min\operatorname*{arg\,max}_{s}\frac{\log w_s+b\log s}{s},
```

by

```latex
 s_i=\min\operatorname*{arg\,max}_{\substack{1\le s\le\lfloor a^i\rfloor\\ w_s>0}}
       \frac{\log w_s+b\log s}{s},
```

---

### F3 — EDITORIAL. main.tex lines 236, 242–244 (proof of Lemma 3.1).

"Since the final count $b_j=a_j+r_j$ is at most $\min\{n,\lfloor m/j\rfloor\}$, bounding the
numerator below by $(n-t)_Q$ proves (4)" skips the only non-obvious step: the denominator of (7)
is a *rising* product in $a_j$ and the denominator of (4) is a *falling* factorial of a different
quantity. The bridge is $\prod_{\ell=1}^{r_j}(a_j+\ell)=\fall{b_j}{r_j}$ plus monotonicity of
$x\mapsto\fall{x}{r_j}$ on integers $x\ge r_j$. Separately, "Since $a_0\ge n-t$" (line 236) is
asserted with no reason.

**Fix.** Replace lines 242–244 by

```latex
The $j$th denominator factor in \eqref{eq:typeratio} is
$\prod_{\ell=1}^{r_j}(a_j+\ell)=\fall{b_j}{r_j}$, and $x\mapsto\fall{x}{q}$ is nondecreasing on
integers $x\ge q$. Since $\sum_i b_i=n$ and $\sum_i ib_i=m$, the final count satisfies
$b_j\le\min\{n,\lfloor m/j\rfloor\}$, so that factor is at most
$\fall{\min\{n,\lfloor m/j\rfloor\}}{r_j}$. Bounding the numerator below by $\fall{n-t}{Q}$,
legitimate because $a_0=n-\sum_{j\ge1}a_j\ge n-\sum_{j\ge1}ja_j=n-t\ge Q$, proves
\eqref{eq:sharpinsertion}.
```

---

### F4 — EDITORIAL. main.tex lines 264–271 (the labelled-box remark).

Two defects.

1. "The weight multiplier is always $w_kW_r$" is the same error as F1: the $Q$ overwritten
   coordinates carry weight $w_0$ each in the background, so the multiplier is $w_kW_r/w_0^{Q}$.
   Verified exactly on four fully enumerated specs (`agent1_scratch/E_probes.py`): the assertion
   $\mathcal W(y)/\mathcal W(x)=w_kW_r/w_0^{Q}$ passed on every record at both $w_0=1$ and
   $w_0=3$.
2. "at most $\prod_j\fall{\min\{n,\lfloor m/j\rfloor\}}{r_j}$ preimages" is true but unexplained:
   the preimages are the ordered $r_j$-tuples of distinct coordinates carrying size $j$ in $y$,
   and $\#\{v:y_v=j\}\le\min\{n,\lfloor m/j\rfloor\}$. Measured inverse multiplicities against
   that bound: 12 vs 42, 6 vs 20, 2 vs 18, 12 vs 210.

**Fix.** Line 270: "The weight multiplier is always $w_kW_r$, the $Q$ overwritten coordinates
being empty in the background and $w_0=1$."

---

### F5 — EDITORIAL. main.tex lines 197–203 and 259.

$K$ is used in the hypothesis ("sizes at least $K$") and in (5) but is never declared — add it to
the list of integers (see F1's replacement text).

"Weights of sizes not used in the construction only increase the original denominator" (line 259):
no denominator exists at that point of Lemma 3.1's proof. Delete it, or write "only increase
$Z(m,n)$".

---

### F6 — MINOR (claim accuracy, Section 10). main.tex lines 760–777.

The text says `check_uniform_windows.py` "verifies finite occupation-count bounds and conditional
probabilities on an entire explicit window". What `finite_window()` actually does (line
`k,K,t=17,4,0`):

* **$t=0$.** The background family is the single count vector $a_0=n$, so $Z_u(t,n)=w_0^n=1$
  (my independent recomputation asserts `zu==1` on all 97 pairs). The window check therefore
  exercises *none* of Lemma 3.1's actual content: the small-box partition factor the section
  exists to preserve is the constant 1; the map $a\mapsto b$ is injective because its domain is a
  singleton; every $a_j$ in (7)'s denominator is zero.
* The non-trivial-background case is tested **only** by `check_full_path.insertion_checks`, whose
  reported `exact_type_identities_checked` is **12** (1+3+2+3+1+2 background count vectors over
  its six specs) — and every spec there asserts `m < 2*k`, i.e. not the regime the paper singles
  out ("No assumption $m<2k$ is required").
* "conditional probabilities" is the wrong term. The quantity computed is the unconditional
  $\Pp_w(Y_{(1)}\le3m/4)=Z_{\{0,2,3,5\}}(m,n)/Z(m,n)$.
* The illustration is $k=17$, $m\in[20,22]$, i.e. $\delta=1/17\approx0.0588$, which violates
  (23)'s $\delta<1/100$. It is not an instance of Theorem 2.1's window, and "an entire explicit
  window" invites that reading.

**Fix.** Replace the first sentence of Section 10's second paragraph by

```latex
The accompanying \texttt{code/check\_uniform\_windows.py} evaluates the exact failure probability
and both insertion bounds on an explicit window of integer pairs with an empty background
($t=0$), the exact finite-prefix inequality with rational geometric data, and the support
obstructions at powers-of-two and factorial sample sizes. The insertion lemma with a non-trivial
background, including totals $m\ge2k$, is tested in \texttt{code/check\_full\_path.py} and
\texttt{code/audit\_stress\_checks.py}. The window parameters are chosen for legibility and do
not satisfy \eqref{eq:parameters}.
```

---

### F7 — no finding, recorded because the brief asked (item 12). Table 1 is exact.

Recomputed from scratch (`agent1_scratch/D_table.py`; no import of the paper's code — own
coefficient recursion, own falling factorial, own $2^{-L}$ search):

* pairs with $20\le m\le22$, $1/2\le m/n\le2$: **97** (31 + 32 + 34), all admissible. Matches.
* max actual failure probability `1.509862200447656899423998e-58` → paper's
  $1.50986220045\cdot10^{-58}$. Matches to all 12 printed digits, at $(m,n)=(20,40)$.
* max sharp insertion bound `9.059173202685941396543987e-58` → $9.05917320269\cdot10^{-58}$, at
  $(20,40)$. Matches.
* max coarse insertion bound `7.581576692191186966115281e-56` → $7.58157669219\cdot10^{-56}$, at
  $(21,42)$. Matches.
* $\sup\Pp_w(Y_{(1)}\le3m/4)\le2^{-189}$: **true**, and the exponent is the best one —
  $2^{-190}$ is false. The coarse row's $\le2^{-183}$: **true**.
* the shipped `code/checks_uniform.json` and `code/checks_stress.json` are byte-equal to a fresh
  run of the scripts on this machine (Python 3.14.3).

---

## WHAT I TRIED THAT DID NOT BREAK IT

All exact integer / `Fraction` arithmetic. No float appears in any assertion.

1. **Injectivity of $a\mapsto b$ (brief item 1).** Holds. Given $b$ and the *fixed* $(Q,(r_j))$,
   invert by $a_0=b_0+Q$, $a_j=b_j-r_j$ for $0<j<k$, $a_j=0$ for $j\ge k$ — the last because
   $a_j=0$ for $j>u$ and $u<k$. The representation is fixed independently of $a$ because the sum
   runs over backgrounds of one fixed total $t$, so $r=m-k-t$ is the same for every summand.
   Enumerated at $m\ge2k$ — the regime `insertion_checks` never reaches (it asserts `m < 2*k`) and
   where `randomized_insertion` tests no injectivity at all: **221,190 image count vectors across
   49,746 $(k,u,t,\text{parts},n)$ specs, zero collisions, $b_k=1$ on every one**
   (`F_inject.py`).
2. **$k\le u$ (brief item 1).** Excluded by hypothesis — and the hypothesis is load-bearing, not
   decorative: relaxing it to $u=k$ produced **117 violations of (4)** in a small sweep, smallest
   at $n=4$, $k=2$, $u=2$, $t=2$, $w_k=10$: $Z=721<920$ (`E_probes.py`). So $u<k$ is correctly
   required and correctly used ($k>u$ forces $a_k=0$, hence $b_k=1$).
3. **The denominator bound and the rising-vs-falling direction (brief item 3).** Correct.
   $\prod_{\ell=1}^{r_j}(a_j+\ell)$ *is* $\fall{b_j}{r_j}$; $b_j\le\min\{n,\lfloor m/j\rfloor\}$
   from $\sum b_i=n$ and $\sum ib_i=m$; $\fall{\cdot}{r_j}$ is nondecreasing for arguments
   $\ge r_j$, and $b_j\ge r_j$. Denominator positivity holds because $r_j\le Q-1<Q\le n$ and
   $jr_j\le r\le m$.
4. **A size in both the R-class and the C-class (brief item 4).** No bookkeeping error, and the
   paper's one-line justification is right. A shared size lies in the R-class, hence is $\ge K$,
   hence *every* one of its $r_j$ factors is at most $\min\{m/K,n\}$ — so assigning some of them
   the bound $m/K$ and the rest the bound $n$ is valid in either order. Tested by taking **all**
   labellings of each multiset of parts into (large, other), since the C-class carries no size
   restriction and so a size $\ge K$ may sit on both sides: **10,260,477 exact cases, 2,552,756 of
   them with a size in both classes; zero failures** of $Z\ge$(4), $Z\ge$(6) or (4)$\ge$(6)
   (`B3_overlap.py`).
5. **Numerator bound $(n-t)_Q\ge(n/2)^Q$ (brief item 5).** Correct. Under $t+Q\le n/2$ the
   smallest factor is $n-t-Q+1\ge n/2+1>n/2$. Checked on **2,666,600** $(n,t,Q)$ triples:
   minimum ratio $(n-t)_Q/(n/2)^Q$ is $200/199=1.005$ at $n=398$, $t=198$, $Q=1$ — tight, never
   violated. Edge cases $Q=1$, $t=0$, $Q=n/2$ all pass (`F_inject.py`).
6. **The exponent arithmetic (brief item 6).** Correct, written out:
   $(n/2)^{1+R+C}/[(m/K)^R n^C] = \frac n2\cdot\frac{n^RK^R}{2^Rm^R}\cdot\frac{n^C}{2^Cn^C}
   = \frac{n}{2^{C+1}}(nK/2m)^R$ — exactly the displayed line. The $R$ factors of $n/2$ are
   consumed by the $R$ factors of $m/K$, the $C$ factors of $n/2$ by the $C$ factors of $n$, and
   the giant's own factor of $n/2$ survives. $nK\ge2m$ then makes the bracket $\ge1$.
7. **The full inequality, broad exhaustive sweep, $w_0=1$.** **9,825,092 exact cases** over six
   weight families (sparse support with gaps; weights above $k$ as large as $2^{100}$; all-ones;
   $w_1=10^6$; $k\le13$, $u<k$, $t\le6$, up to three parts, $K\in\{2,3,4,5\}$, $n\le15$), of which
   **7,791,932 have $t>0$**, **8,376,588 have $m\ge2k$**, and **1,250,231** satisfy (5). All
   satisfy $Z(m,n)\ge$(4), $Z(m,n)\ge$(6) and (4)$\ge$(6). **Zero failures**
   (`B2_insertion_sweep.py`). This widens the paper's own non-trivial-background coverage from 12
   cases to 7.8M.
8. **Lemma 5.1's greedy at $a$ close to one (brief item 7).** The strict decrease survives, and
   not by luck: $x'<h_*+s_i\le2a^i$ forces $\log_a(x'/2)<i$, so the next index is $\le i-1$ for
   **every** $a>1$; and $q\ge1$ because $s_i\le a^i\le x/2$ and $h_*\le a^{i_0}\le a^i\le x/2$
   give $x-h_*\ge x/2\ge s_i$. Tested exactly with $a\in\{2,\,3/2,\,11/10,\,101/100\}$ as
   `Fraction`s, base-2 logarithms (so $B_i$ and $p_i$ are exact rationals), four record patterns,
   $K\in\{2,4\}$, $D\in\{2,3\}$ — 32 lanes, **7,712 values of $r$**. Every one of $i\ge i_0$,
   $q\ge1$, $s_i\ge K$, $h_*\le x'<h_*+s_i\le2a^i$, $qs_i\le x<2a^{i+1}$, strict decrease of the
   index, one stage per index, all parts $\le r$, terminal value in $[h_*,2a^{i_0})$ — **zero
   failures**. At $a=101/100$ this runs with $i_0$ up to 488 and $i_{\max}=697$
   (`C2_greedy.py`).
9. **"Parts at least $K$" and "at most $C_*$ additional parts" (brief item 8).** Correct. Greedy
   parts are copies of $s_i$ with $i\ge i_0$, and (13) makes $s_i\ge K$ for exactly those $i$;
   terminal parts come from the fixed finite list, so their number is $\le C_*$. "All parts are at
   most $r$" is also correct: greedy parts satisfy $s_i\le a^i\le x/2<r$, and terminal parts are
   positive integers summing to $x'\le r$. Asserted on all 7,712 runs.
10. **The active/inactive identity (brief item 9) — where I most expected a silent error.** Safe,
    for a reason the paper does not spell out but does not need to: $B_i$ is *defined* as the
    maximum and $s_i$ as a maximizer, so $\log w_{s_i}=s_iB_i-b\log s_i$ and
    $\log w_{s_i}/s_i=B_i-p_i$ hold at **every** index, active or not. (9) restricts the *window*
    $a^{J-1}<s_J\le a^J$ to active indices, and the greedy never uses that window — it uses only
    $s_i\le\lfloor a^i\rfloor$, which is unconditional. Verified as an exact rational identity at
    **4,464** indices across the 32 lanes, and (9) at **172** active indices; zero failures
    (`C2_greedy.py`).
11. **The $2a^{i+1}$ factor and the summation range (brief item 10).** Correct.
    $qs_i\le x-h_*<x<2a^{i+1}$ because $i=\lfloor\log_a(x/2)\rfloor$ gives $a^{i+1}>x/2$; the
    per-unit deficit $B_{J-1}-B_i+p_i$ is nonnegative because $i\le J-D\le J-1$, $B$ is
    nondecreasing and $p_i\ge0$. Every stage index lies in $[i_0,I(r)]\subseteq[i_0,J-D]$ — the
    first is $I(r)\le J-D$ by hypothesis, they strictly decrease, and they cannot drop below $i_0$
    because the loop stops at $x<2a^{i_0}$ — so the sum covers every stage used and the lower
    limit $i_0$ is right. Inequality (14) itself was checked as an exact rational inequality
    **30,692 times** (every lane, every $r$, several admissible $J$ each); zero failures.
12. **The semigroup / Chicken-McNugget argument (lines 361–367).** Correct as written, if terse. A
    finite subset of the support attains the gcd; in the finite cyclic group $\mathbb Z/s$ the
    sub-*semigroup* generated by a set equals the sub-*group* it generates (every element has
    finite order), and that subgroup is everything because the overall gcd, $s$ included, is one.
    The only thing missing is the clause "since every element of a finite group has finite order,
    the semigroup generated by the residues is a subgroup".
13. **"No assumption $m<2k$ is required."** True. Background sizes are $\le u<k$ and every
    representation size is $<k$, so $r_k=a_k=0$ and $b_k=1$ identically; count vectors of
    $Z(m,n)$ with two size-$k$ boxes simply lie outside the image and contribute nonnegative extra
    mass. Confirmed on 8.4M cases with $m\ge2k$ (item 7) and 221k enumerated images (item 1).
14. **Whether the C-class bound "at most $n$" can be evaded.** No: $b_j\le\sum_i b_i=n$ for every
    $j$, with no hypothesis needed.
15. **Reproducibility.** `python code/check_full_path.py`, `python code/check_uniform_windows.py`
    and `python code/audit_stress_checks.py` all exit 0 on Python 3.14.3, printing
    `ALL_EXACT_CHECKS_PASS` / `ALL_STRESS_CHECKS_PASS`; outputs byte-identical to the shipped
    `code/checks_uniform.json` and `code/checks_stress.json`; the predecessor-hash pin in
    `check_uniform_windows.py` matches.

### Bounds on the searches above

The sweeps are bounded, and no absence is asserted from them. Item 7 ran $n\le15$, $k\le13$,
$u<k$, $t\le6$, at most 3 parts, $K\in\{2,3,4,5\}$, six weight families; item 4 ran $n\le18$,
$k\le15$, $t\le4$, 1–4 parts, $K\in\{2,3,4\}$, all labellings, three weight families; item 1 ran
$k\le7$, $t\le8$, $\le3$ parts, six values of $n$ per spec; item 8 ran $r$ up to $2^{13}$ with
$a$ down to $101/100$. Total: 20,085,569 exact cases (9,825,092 + 10,260,477), of which 7,791,932
are counted as having $t>0$ in item 7 alone — against the paper's 12 non-trivial-background cases.
Nothing failed. What rules out a failure outside those bounds is not the search but
the hand derivation reproduced in items 1, 3, 5, 6 and 10–11, each step of which I checked
independently of the code.

### The one thing I could not widen

`prefix_checks` (Section 6's finite-prefix inequality) runs at a single base $a=2$, with $b=4$,
$D=11$, $i_0=4$, $J_0=18$, over four hand-made $B_i$ patterns — while Section 7 needs $a$ close to
one and $D$ large. I re-derived its constants against (18)–(22) by hand and they agree exactly,
including the easily-mis-transcribed $\Pi$ (the code's `tail_l` is
$U_{i_0+1}/a=\sum_{\ell\ge i_0+1}\ell a^{-\ell}$, so `b*a*tail_l` is the paper's
$ba\log a\sum\ell a^{-\ell}$ at $a=2$ in base-2 logs). Section 6 is another auditor's scope and I
did not widen its numerical base.

---

## SUMMARY OF REQUIRED EDITS

| # | Where | Severity | Edit |
|---|---|---|---|
| F1 | line 198 + eqs (4), (6), (7) | MINOR, false as stated | add $w_0=1$ to Lemma 3.1's hypotheses, or insert $w_0^{-Q}$ in three displays |
| F2 | line 278, eq (8) | MINOR, definitional | put $1\le s\le\lfloor a^i\rfloor$, $w_s>0$ under the `\arg\max` |
| F3 | lines 236, 242–244 | EDITORIAL | state $\prod_\ell(a_j+\ell)=\fall{b_j}{r_j}$, falling-factorial monotonicity, and $a_0\ge n-t$ |
| F4 | line 270 | EDITORIAL | labelled multiplier is $w_kW_r/w_0^Q$; say what the preimages are |
| F5 | lines 197, 259 | EDITORIAL | declare $K$; fix "the original denominator" |
| F6 | lines 760–765 | MINOR | disclose $t=0$, the 12 non-trivial-background cases, "unconditional", and $\delta=1/17\not<1/100$ |

Scripts producing every number above:
`agent1_scratch/A_w0_attack.py`,
`B2_insertion_sweep.py`, `B3_overlap.py`, `C2_greedy.py`, `D_table.py`, `E_probes.py`,
`F_inject.py`.
