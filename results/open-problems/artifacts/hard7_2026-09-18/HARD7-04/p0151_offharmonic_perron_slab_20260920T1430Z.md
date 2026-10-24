Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# P0151 analytic artifact — off-harmonic Perron gain and a fixed-buffer slab certificate

This is a self-derived theorem-sized auxiliary result for `HARD7-04` and the exact fixed-outdegree sequential preferential-attachment percolation target frozen in `operations/claims/P0151.md`.

It does **not** prove the finite-graph critical window, `gamma_E=1/2`, the `sqrt(n)/log n` largest-component scale, or a finite-graph coupling. Its purpose is different: it identifies an exact positive Perron margin available at every fixed exponent `beta<1/2`, quantifies how much finite-graph comparison error that exponent can tolerate, and isolates a precise reason a crude minimum-age coupling cannot carry the comparison to `beta` near `1/2`.

The source problem remains **OPEN**.

---

## 1. Frozen constants and the exact critical local operator

Fix integer `m>=2` and `delta>0`. Put

`a:=m+delta`,
`A:=2m+delta`,
`chi:=a/A`,
`alpha:=chi-1/2=delta/(2A)`.

Thus

`1-chi=m/A=1/2-alpha`.

Use the two Pólya-point-tree type constants already established in the killed-PPT spectral artifact:

`c:=m*a/A`,
`d:=m*(a+1)/A`,
`e:=(m-1)*a/A`,
`g:=sqrt(d*e)`,
`lambda0:=c+g`.

The exact critical retention parameter is

`pi_c=alpha/lambda0
     =delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The extended mean-offspring kernel on ages `x,y>0` is

`kappa((x,s),(y,t))
 =c_st [1_{x>y,t=O}+1_{x<y,t=Y}]
  /[(x max y)^chi (x min y)^(1-chi)]`,

with coefficient matrix

`M=[[c,d],[e,c]]`.

The actual Pólya-point-tree age interval is `(0,1]`; the extended operator is used only as an exact algebraic device, exactly as in the preceding spectral artifact.

---

## 2. Proposition: every fixed sub-half exponent has an exact positive Perron margin

Fix

`beta in (1-chi,1/2)=(m/A,1/2)`

and set

`epsilon:=1/2-beta in (0,alpha)`.

Define

`u_e:=chi-beta=alpha+epsilon`,
`v_e:=chi+beta-1=alpha-epsilon`.

For a power vector

`h_s^(beta)(x)=r_s x^(-beta)`,

integration of the extended operator reduces exactly to the positive `2x2` matrix

`B_beta
 =[[c/u_e, d/v_e],
   [e/u_e, c/v_e]]`.                                             (2.1)

Let `mu_beta=r(B_beta)` and

`Lambda_beta:=pi_c mu_beta`.                                      (2.2)

Then

`Lambda_beta
 = alpha/(lambda0*(alpha^2-epsilon^2))
   *[c*alpha
     +sqrt(g^2 alpha^2+(c^2-g^2)epsilon^2)]`.                    (2.3)

Moreover

`Lambda_beta>1`                                                   (2.4)

for every `beta in (m/A,1/2)`, and as `beta upward 1/2`, equivalently `epsilon downarrow0`,

`Lambda_beta
 =1+(sigma^2/2)epsilon^2+O(epsilon^4)`,                          (2.5)

where the same variance constant from the killed-PPT Fourier calculation appears:

`sigma^2=lambda0/(alpha^2 g)`.                                   (2.6)

Thus the centered critical operator is exactly neutral at exponent `1/2`, but is **strictly superharmonic in the power-weighted sense at every fixed exponent below `1/2`**, with a quadratic margin.

### Proof

For an `O`-offspring, `0<y<x`, and

`int_0^x y^(-(1-chi)) y^(-beta) dy
 =x^(chi-beta)/(chi-beta)`.

After the parent factor `x^-chi` this contributes

`c_sO r_O x^-beta/(chi-beta)`.

For a `Y`-offspring, `y>x`, and because `beta>1-chi`,

`int_x^infinity y^(-chi-beta)dy
 =x^(1-chi-beta)/(chi+beta-1)`.

After the parent factor `x^(chi-1)` this contributes

`c_sY r_Y x^-beta/(chi+beta-1)`.

This gives (2.1). The Perron eigenvalue of a positive `2x2` matrix is

`mu_beta
 =1/2{ c(1/u_e+1/v_e)
       +sqrt[c^2(1/u_e-1/v_e)^2+4de/(u_e v_e)] }`.

Since

`u_e v_e=alpha^2-epsilon^2`,
`1/u_e+1/v_e=2alpha/(alpha^2-epsilon^2)`,
`1/u_e-1/v_e=-2epsilon/(alpha^2-epsilon^2)`,

and `de=g^2`, this simplifies to

`mu_beta
 =[c alpha+sqrt(g^2 alpha^2+(c^2-g^2)epsilon^2)]
  /(alpha^2-epsilon^2)`.

Multiplying by `pi_c=alpha/lambda0` gives (2.3).

The sign is strict because

`c^2-g^2
 =[m^2 a^2-m(m-1)a(a+1)]/A^2
 =m a(delta+1)/A^2
 >0`.                                                              (2.7)

Hence for `epsilon>0` the square-root numerator is strictly larger than `g alpha`, while the denominator is strictly smaller than `alpha^2`. At `epsilon=0` the expression equals one. Therefore `Lambda_beta>1`.

For the expansion,

`sqrt(g^2 alpha^2+(c^2-g^2)epsilon^2)
 =g alpha+(c^2-g^2)epsilon^2/(2g alpha)+O(epsilon^4)`.

After also expanding `(alpha^2-epsilon^2)^-1`, the coefficient of `epsilon^2` simplifies to

`(c+g)/(2g alpha^2)=sigma^2/2`,

proving (2.5).

---

## 3. B11 duality: the same constant appears on the hyperbolic side

The previous exact full-line Fourier symbol had principal branch

`lambda_+(xi)
 =1-(sigma^2/2)xi^2+O(xi^4)`

for real Fourier frequency `xi`.

The power perturbation above is the real-exponential, or formally `xi=i epsilon`, direction. Equation (2.5) becomes

`Lambda_(1/2-epsilon)
 =1+(sigma^2/2)epsilon^2+O(epsilon^4)`.

So the local critical-window loss and the sub-half exponent gain are two sides of the same quadratic dispersion constant.

This is more than a mnemonic: (2.3) is an exact positive-matrix calculation, so no analytic-continuation assumption is needed.

---

## 4. Exact fixed-buffer slab certificate on the killed age interval

Let `T_L` be the actual PPT mean operator restricted in both age variables to

`e^-L <= x,y <=1`,

or in log-age coordinates

`0<=u=-log x<=L`.

Let `r^(beta)=(r_O,r_Y)>0` be any positive right Perron vector of `B_beta`, so

`B_beta r^(beta)=mu_beta r^(beta)`.

Put

`h_s(u):=r_s exp(beta u)`.

For the extended operator,

`pi_c T_bar h=Lambda_beta h`.                                    (4.1)

The finite interval loses only two tails.

For the `O` direction, the missing ages have `v>L`, and relative to `h_s(u)` their contribution is exactly bounded by the corresponding full-row coefficient times

`exp[-(alpha+epsilon)(L-u)]`.

For the `Y` direction, the missing extended ages have `v<0`, and their relative contribution is bounded by the corresponding full-row coefficient times

`exp[-(alpha-epsilon)u]`.

Because the two positive row coefficients sum, after multiplication by `pi_c`, to `Lambda_beta`, every parent type `s` and every `u in [H,L-H]` satisfy

`0 <= [pi_c(T_bar-T_L)h]_s(u)/h_s(u)
    <= Lambda_beta exp[-(alpha-epsilon)H]`.                       (4.2)

Define the fixed buffer

`H_beta
 :=1/(alpha-epsilon)
   log[2 Lambda_beta/(Lambda_beta-1)]`.                            (4.3)

This depends on `(m,delta,beta)` but **not** on `L` or `n`. For every `L>=2H_beta` and every interior log-age

`H_beta<=u<=L-H_beta`,

(4.1)--(4.3) give the componentwise inequality

`pi_c (T_L h)_s(u)
 >=[(Lambda_beta+1)/2] h_s(u)
 =[1+eta_beta]h_s(u)`,                                            (4.4)

where

`eta_beta:=(Lambda_beta-1)/2>0`.                                 (4.5)

This is the promised **fixed-buffer Perron-weighted slab certificate**.

As `epsilon downarrow0`, (2.5) gives

`H_(1/2-epsilon)
 =(2/alpha)log(1/epsilon)+O(1)`.                                 (4.6)

Thus approaching the half exponent requires only a logarithmically widening deterministic buffer in `1/epsilon`; it does not require a buffer that grows with `n` when `epsilon` is held fixed.

---

## 5. Quantified finite-graph comparison tolerance

The certificate yields a precise target for a future finite-graph transfer.

Set

`G_beta:=(Lambda_beta+1)/2>1`

and

`zeta_beta
 :=(G_beta-1)/(2G_beta)
  =(Lambda_beta-1)/(2(Lambda_beta+1))`.                           (5.1)

Suppose a finite-graph one-generation connected exploration operator `K_n`, on the same Perron weight and on the buffered age/type states, can be proved to satisfy

`K_n h >= (1-zeta_beta) pi_c T_L h`                               (5.2)

componentwise, after all duplicate, fixed-outdegree and without-replacement corrections relevant to that generation are included.

Then (4.4) implies

`K_n h
 >=(1-zeta_beta)G_beta h
 =[(Lambda_beta+3)/4]h
 =[1+(Lambda_beta-1)/4]h`.                                       (5.3)

So for every fixed `beta<1/2`, the finite comparison only has to preserve a **fixed positive relative accuracy**, not an `o((log n)^-2)` spectral accuracy.

Near `1/2`,

`zeta_(1/2-epsilon)
 =(sigma^2/8)epsilon^2+O(epsilon^4)`.                             (5.4)

This sharply separates two goals:

1. proving the full `(log n)^-2` critical window requires window-scale accuracy;
2. proving only the power exponent lower bound `gamma_E>=beta` for a fixed `beta<1/2` could in principle tolerate a fixed `Theta((1/2-beta)^2)` comparison error.

The second route is potentially much easier, but the actual finite-graph domination (5.2) is **not** proved here.

---

## 6. Exact algebraic target matrix: what the scalar shadow is missing

The current finite connected-shadow chain first reached the tangent exponent

`b2=m(1+a pi_c)/A`.

Since `c=ma/A`,

`b2=m/A+pi_c c`.                                                  (6.1)

At criticality

`pi_c(c+g)=alpha=1/2-m/A`.

Therefore the gap of the tangent scalar shadow is exactly

`1/2-b2=pi_c g`.                                                  (6.2)

Equivalently, the positive matrix

`G_target
 :=(m/A)I+pi_c [[c,d],[e,c]]`                                   (6.3)

has Perron eigenvalue exactly

`r(G_target)
 =m/A+pi_c(c+sqrt(de))
 =1/2`.                                                           (6.4)

This does **not** assert that `G_target` is already the drift matrix of a valid finite connected shadow. It identifies the missing structure: the scalar time-forward shadow captures the diagonal contribution `pi_c c`; the exact half exponent also needs the geometric mean of the two directional off-diagonal mechanisms.

This is the natural finite-dimensional target for a genuine two-type age/orientation shadow.

---

## 7. B30 failure test: a hard minimum-age cutoff cannot approach `1/2`

The new fixed-`beta` margin suggested trying a simple finite coupling: discard every vertex born before a deterministic floor `s_n=n^q`, then use only the global square-attractiveness estimate to control collisions.

That route has a rigorous exponent barrier.

For two attachment choices made at a birth time `t`, the probability of a repeated target is bounded by the square-attractiveness ratio. The already established global estimate

`E V_t=E sum_v w_v(t)^2=O(t)`

and total attractiveness `T_t=At+O(1)` give

`P(repeated target at time t)=O(1/t)`.                            (7.1)

If every relevant exposure occurs at time at least `s_n=n^q` and an exploration makes `R_n=O(n^beta)` relevant target exposures, the crude union bound gives expected collision count

`O(R_n^2/s_n)=O(n^(2beta-q))`.                                   (7.2)

Making this `o(1)` by this method requires

`q>2beta`.                                                        (7.3)

On the other hand, the log-age interval left after imposing the floor is

`L_n=log(n/s_n)=(1-q)log n`.

The exact killed-PPT Green calculation from the preceding run has oldest-boundary scale

`exp(L_n/2)/L_n
 =n^((1-q)/2)/[(1-q)log n]`.                                     (7.4)

Even at the level of that idealized operator, a target polynomial scale `n^beta` therefore requires

`beta<=(1-q)/2` at the exponent level, hence

`q<=1-2beta`.                                                     (7.5)

Conditions (7.3) and (7.5) can both hold only if

`beta<1/4`.                                                       (7.6)

Therefore a proof that controls all collisions solely by a single minimum birth time and the uniform estimate `O(1/s_n)` **cannot approach the desired half exponent**. This is a limitation of that proof strategy, not a counterexample to P0151.

The transfer must instead exploit age-sensitive collision accounting or a connected-shadow construction that never creates the full tree-coupling collision burden.

A precise next collision quantity is therefore the age-weighted exposure energy

`E_coll:=sum_t R_t^2/t`,                                          (7.7)

with `R_t` the number of relevant target exposures charged to birth-time scale `t`. A successful slab transfer needs a construction in which the contribution of (7.7), plus fixed-outdegree same-birth corrections, is below the fixed tolerance in (5.1) for every chosen `beta<1/2`.

---

## 8. B7 / B11 / B30 outcomes

### B7 — TAKE THE LIMIT

**Question tested:** does moving the power exponent below `1/2` make the critical local operator subcritical, neutral, or superharmonic?

**Outcome:** exact success. The gain is `Lambda_beta-1>0`, with quadratic law `(sigma^2/2)(1/2-beta)^2+O((1/2-beta)^4)`.

### B11 — DUALIZE

**Question tested:** is the gain unrelated to the earlier killed-window calculation, or is it the dual side of the same dispersion?

**Outcome:** exact success. The same `sigma^2` controls the negative real-Fourier curvature and positive exponential-power curvature. The scalar tangent gap is exactly `pi_c g`, the missing off-diagonal Perron term.

### B30 — ONE SCALE / DIRECTION AT A TIME

**Question tested:** can a crude hard age floor plus `E V_t=O(t)` transfer the local process to the finite graph at polynomial size?

**Outcome:** rejected beyond `beta<1/4`. The exact algebraic incompatibility (7.3)--(7.6) shows why the next proof must use age-sensitive collision energy rather than a single floor.

All B1--B30 had already been used at least once on P0151 before this run, so three never-before-used labels no longer exist. This run therefore follows the latest checkpoint's instruction: it uses a nonconsecutive triple in a genuinely different route rather than fabricating unused labels.

---

## 9. What this changes and what it does not

The frozen finite-graph source metric remains

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)|/log n`.

The preceding run proved

`gamma_E>=b14`.

This artifact does **not** prove a new finite-graph exponent, so the honest value remains

`gamma_E>=b14`.

There is therefore **NO MOVEMENT** in the frozen metric in this iteration.

What has changed is the transfer target. The finite-graph problem no longer needs to be attacked first at the exact `(log n)^-2` window resolution if the immediate goal is only the half power exponent. For every fixed `beta<1/2`, there is now an explicit:

- positive local Perron margin `Lambda_beta-1`;
- buffer width `H_beta` independent of `n`;
- admissible relative comparison loss `zeta_beta`;
- exact two-type target matrix with missing contribution `pi_c g`;
- proof that the simplest minimum-age collision strategy cannot reach the required exponent range.

A next finite-graph run should build a **two-type connected shadow indexed by edge orientation and age slab**, and prove that its one-generation weighted drift loses less than `zeta_beta` while its age-weighted collision energy is summable. That is now a quantified obligation rather than a qualitative “couple to the PPT” instruction.

---

## 10. Closure honesty

This is a theorem-sized analytic self-check only. There is no finite exhaustive claim, so no checker was manufactured. No source-level closure is claimed, and no independent audit is claimed.

Status: **PARTIAL / SOURCE OPEN**.