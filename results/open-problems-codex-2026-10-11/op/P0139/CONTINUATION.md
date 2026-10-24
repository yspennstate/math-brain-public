# P0139: second serious attempt, 12 October 2026

## Two approaches not used in the first attempt

**A. A variation-margin reduction that allows the actual source clocks to move.** Work with 2 < r < p < 3. Combine uniform convergence of enhanced signatures with uniform r-variation bounds to get p-variation convergence by interpolation. Prove enhanced uniform convergence by finite-loop truncation; derive convergence of inverse clocks from the dense set of limiting attached intervals, rather than assume identical attachment schedules. For each finite set, use the source's regular-contact theorem to control root changes. Add explicit enhanced input convergence and uniform tail hypotheses, and see exactly which ones are needed. This differs from the earlier fixed-clock splice estimates and would remove the whole fixed-schedule restriction, at the price of a regularity margin and stronger inputs.

**B. A cusp counterexample with zero signed area.** Insert increasingly many small tree-like loops close to the initial backbone point. Their total added duration can tend to zero, and every loop's enhancement can tend uniformly to the identity, while their total p-variation energy stays nonzero. Placing the loops arbitrarily close to the initial point may defeat a cusp lambda >= C d_R0^beta without needing to suppress lambda itself below an output modulus. This could show that enhanced uniform matching and absolute signed-area tails are still insufficient at the target p exponent. It would not refute a topology that controls aggregate p-energy or has an r<p margin.

Approach A is more promising for a positive result and is pursued first. Approach B is a boundary check on its extra hypotheses.

## Brain query for the actual gap

Read-only query on 2026-10-12:

    python -X utf8 ~/.claude/dreaming/math_recall.py "rough path time change p variation interpolation Friz Victoir rerooting"

The returned cards concerned unrelated displacement interpolation, random path clocks, Kahane interpolation, and unrelated variation estimates. No usable theorem about rough-path time changes or rerooting was returned. Consequently all interpolation and moving-clock steps below must be proved directly; no brain card is treated as authority.

## Working target

Prove a sequential deterministic theorem for source configurations X_n -> X in d_R0, with X in R and lambda_n -> 0, that admits changing first hits, temporal roots, and physical durations. Specify enhancements and stronger uniform tail assumptions entirely on the inputs. Compare outputs on the original physical time axis by constant extension, not modulo reparametrization. Obtain p-variation convergence from a uniform r-variation bound, and state exactly what is still missing for the original open question.

Proofs and referee checks will be appended as they are completed.

## 1. The interpolation step, proved directly

For any two-index array F and 0 < r < p, let u=sup_(s<t)|F_st| and v=||F||_(r-var). Then

    ||F||_(p-var) <= u^(1-r/p) v^(r/p).                  (9)

Indeed every finite partition satisfies sum |F_st|^p <= u^(p-r) sum |F_st|^r. Take its supremum and then its p-th root. If u or v is zero, F is zero and the inequality holds with its continuous zero interpretation. No additive property of F is used.

Apply (9) to first-level increment differences with exponents r,p, and to area increment differences with exponents r/2,p/2. If two rough paths have r-rough norms at most M, and

    d_infty = sup |x_st-x'_st| + (sup |a_st-a'_st|)^(1/2),
    eta = 1-r/p > 0,

then, by the triangle inequality for each variation norm,

    D_p(X,X') <= C M^(r/p) d_infty^eta.                 (10)

The first-level r-variation difference is <=2M; the area r/2-variation difference is <=2M^2. Substitution in (9), with a square root on the area estimate, proves (10). The constant accounts for the sum of the two powers. For M=0 both paths are constant with zero area. This is the elementary rough-path interpolation reduction, not an appeal to first-level convergence alone.

## 2. Cyclic rerooting of an enhanced loop

A based planar enhanced loop on normalized time [0,1] has global coordinates (g(u),A(u)), with g(0)=g(1)=0, A(0)=0 and c=A(1). Define its extension to all real times by

    g(u+k)=g(u),  A(u+k)=A(u)+k c,   k an integer.

Both extended coordinates are continuous at integers. At a normalized temporal root theta, the rerooted loop has global coordinates

    e_theta(v)=g(theta+v)-g(theta),
    b_theta(v)=A(theta+v)-A(theta)
                 -(1/2)g(theta) wedge g(theta+v),  0<=v<=1.    (11)

This is the increment of the extended group path from theta to theta+v, so its increment arrays satisfy Chen's identity. Its terminal first displacement is zero and its terminal area is exactly c. Formula (11) includes the contribution when the root crosses the old temporal seam; simply shifting A periodically without adding c would be wrong.

**Uniform rerooting lemma.** Suppose (g_n,A_n) converge uniformly on [0,1] to (g,A), and theta_n -> theta in [0,1]. Then their rerooted global coordinates converge uniformly on [0,1]. Proof: c_n=A_n(1) -> c; the extended coordinates converge uniformly on [0,2]. Compose with theta_n+v, using uniform continuity of the limiting extended coordinates, and apply the bilinear wedge formula. This proves the claim, including roots at the seam. The root-closure convention at 1 gives the same rerooted increment path as at 0.

**Variation rerooting lemma.** For r>2 there is C_r such that a cyclic rerooted loop has r-rough norm <=C_r times the original r-rough norm. Proof: cut the rerooted traversal at its one temporal seam into the old suffix and old prefix. In a partition, all but at most one interval lie in one of these pieces. Their sums of first r-powers and area r/2-powers are bounded by twice the original respective variation powers (each piece's norm is at most the original norm). Split the crossing interval at the seam. Chen's formula is x=x_1+x_2 and a=a_1+a_2+(1/2)x_1 wedge x_2. Each |x_j| is at most the original first-level norm; each |a_j| is at most the original area norm. Thus the single crossing first increment is at most twice the original rough norm, and the crossing area at most (5/2) times its square. Adding this single contribution and taking the appropriate roots proves the asserted constant. There is no accumulation over multiple seams since the rerooted loop traverses only one lap. QED.

## 3. Moving inverse clocks from dense limiting loop intervals

Normalize each backbone to time [0,1], retaining its original duration t_gamma. Let X_n=(gamma_n,L_n) converge to X=(gamma,L) in the source distance d_R0, assume X in R, and let lambda_n -> 0 with (X_n,lambda_n) in R'. Choose arbitrary allowed tie breaks B_n. Let T=sum_(ell in L_gamma)t_ell, T_n=sum_(ell in L_n,gamma_n)t_ell+lambda_n t_gamma_n. Fix H>T with T_n<H eventually and extend every output constantly after its terminal time to [0,H]. Let f_n be the source inverse backbone clock sigma_n/t_gamma_n, extended by 1 after T_n; define f=sigma/t_gamma, extended by 1 after T. For all large n the positive backbone durations are bounded above and below, since source path convergence controls duration and t_gamma>0.

**Clock lemma.** Under these assumptions, f_n -> f uniformly on [0,H]. No differentiability, quantitative cusp, or uniform clock Lipschitz constant is assumed.

**Proof of convergence of each fixed attached interval.** Source d_R0 convergence supplies increasingly fine loop isomorphisms and total attached-duration convergence. Each fixed limiting attached loop has positive duration. For large n it is matched to ell_i,n; its duration converges. Theorem 3.2, p.13, applies because every attached limiting pair is regular: intersection persists, the normalized first hit s_i,n converges to s_i, and every selected temporal root converges to the unique limiting root. Every fixed limiting loop disjoint from gamma remains disjoint under small perturbation, by compact separation. The finite first hits in the limit are distinct, so a fixed finite collection of attached matched loops is eventually strictly ordered in the same way, independently of B_n.

For any finite retained collection F that includes loop i, put S_F=sum_(j in F)d_j, S_F,n=sum_(j in F)d_j,n and tau_n=sum of all attached loop durations (excluding lambda_n t_gamma_n). For loop i, its predecessor-duration sum is a sum over predecessors in F plus a nonnegative remainder bounded by tau_n-S_F,n. The limit remainder is bounded by T-S_F. Therefore the difference of predecessor sums is bounded by

    sum_(j in F)|d_j,n-d_j| + (tau_n-S_F,n) + (T-S_F).

For fixed F its limsup is <=2(T-S_F), because tau_n -> T. Finite sets F can exhaust the attached limiting loops, with S_F -> T by finite total duration. Thus the predecessor sums converge. Adding lambda_n times the (bounded) original first hitting time shows physical starts a_i,n -> a_i. Endpoints b_i,n=a_i,n+d_i,n converge to b_i=a_i+d_i. This proof uses nonnegative duration mass and the actual total-duration term in d_R0; a loop isomorphism alone would not suffice.

For t in the interior (a_i,b_i), eventually t in (a_i,n,b_i,n), hence f_n(t)=s_i,n -> s_i=f(t). By source Lemma 2.2, these interiors are dense in [0,T]; after T, f_n(t)=f(t)=1 eventually for each fixed t>T. At 0 the normalized clock equals 0; at H it equals 1. The limiting f is continuous by source Lemma 2.3, including at T.

Here is the monotone convergence argument explicitly. Given epsilon>0, choose finitely many ordered points in the dense convergence set, including 0,H, so that f changes by less than epsilon between successive points; continuity and compactness allow this, by first choosing a sufficiently fine time mesh and then points from the dense set. For large n the differences |f_n-f| at those finitely many points are <epsilon. For a time between two successive chosen points, monotonicity of f_n and f sandwiches its difference between their endpoint errors plus the change of f, hence below 2epsilon. This proves uniform convergence. QED.

Referee point: this proves qualitative uniform clock convergence only. It does not bound its modulus by a power of d_R0 or of lambda.

## 4. A continuity theorem with moving source configurations

Fix 2<r<p<3. Supply the normalized backbone gamma_n and gamma with continuous weak geometric step-two enhancements G_n,G, with fixed initial point zero. Supply each loop with a continuous based enhancement at its original temporal root, normalized to [0,1]. A supplied loop enhancement is rerooted by (11), rather than chosen anew after changing the root. All rough norms in the following hypotheses use exponent r.

Assume:

1. X_n -> X in d_R0, X in R, lambda_n -> 0 and (X_n,lambda_n) in R'.
2. The global first and area coordinates of G_n converge uniformly on [0,1] to those of G. Under loop isomorphisms of scale tending to zero, the normalized global coordinates of each fixed positive-duration limiting loop converge uniformly to its supplied enhancement. This matching includes actual loop durations and absolute first-level spatial locations, as the source isomorphisms do. This is enhanced input convergence, not output convergence.
3. There is a finite M bounding, for n and for the limit,

       V_n + E_n + sqrt(A_n),
       V_n=||G_n||_r,
       E_n=(sum_(ell attached) ||L_ell,n||_r^r)^(1/r),
       A_n=sum_(ell attached)|c_ell,n|.

4. The enhanced tails are uniformly tight by duration:

       e(delta)=sup_(n and limit)
          (sum_(ell attached, duration<=delta)||L_ell,n||_r^r)^(1/r) -> 0,
       h(delta)=sup_(n and limit)
          sum_(ell attached, duration<=delta)|c_ell,n| -> 0.   (12)

Finitely many early n may be discarded or included if each has the stated summability. The supremum could equivalently be an asymptotic limsup with individual summability. The quantities in (12) are input functionals; terminal loop area is invariant under rerooting. These conditions are stronger than the source's d_R0 topology and not consequences of it.

**Theorem 3 (moving clocks and roots, with a variation margin).** The prescribed enhanced chronological attachments exist as the truncation limits of the first attempt, now separately on each configuration's own physical clock. On the common physical horizon [0,H] with constant terminal extension,

       D_p( enhanced Xi(X_n,lambda_n,B_n), enhanced Xi(X,0) ) -> 0.    (13)

This holds for every sequence of permitted tie breaks B_n. In particular, no attachment schedule, duration, or temporal root is held fixed in this theorem. Its first levels are exactly the source outputs. The enhancements are the supplied-concatenation lifts; no claim identifying a stochastic lift is implicit.

**Complete proof.** Apply the variation rerooting lemma to obtain uniform r-energy and tail bounds for the rerooted loops, at a cost C_r. On each configuration compose its backbone enhancement with its actual inverse clock f_n. Ordered clock images of any partition form an ordered backbone partition with repetitions removed, so this composition Y_n has r-rough norm <=V_n and is constant at both levels during every attached interval. Theorem 1 of ATTEMPT.md, used at exponent r, now constructs the full enhanced output and proves its uniform r-rough bound C_r M. Constant extension preserves this bound. The same construction applies to the limit, and the first levels equal the source paths by that theorem's conditional source corollary.

For a finite set F of attached limiting loops of duration >=delta>0, retain its matched loops F_n, keeping all omitted intervals as stationary waits on each configuration's own clock. Denote these enhanced truncations by Z_n^F and Z^F. They are intermediate comparison paths and need not be source outputs for deleted-loop configurations.

The clock lemma proves f_n -> f uniformly. Thus the global coordinates of Y_n converge uniformly to those of Y: they are g_n(f_n(t)) and A_G,n(f_n(t)), and uniform convergence plus uniform continuity of the limiting coordinates proves this composition assertion. For each i in F, the source regular-root result and convergence of durations give normalized theta_i,n -> theta_i. The uniform rerooting lemma proves convergence of the based loop coordinates (e_i,n,b_i,n) on normalized time [0,1]. The clock lemma's preliminary argument gives a_i,n -> a_i and d_i,n -> d_i>0.

Define the local clamped phase on the whole physical horizon by

       u_i,n(t)= min(1,max(0,(t-a_i,n)/d_i,n)).

It converges uniformly to u_i(t): denominators stay bounded away from zero for fixed i, and clamping is 1-Lipschitz. Outside the interval, e_i,n(u_i,n(t))=0; b_i,n(u_i,n(t)) equals 0 before the interval and c_i,n after it. Consequently the finite splice formula is exactly

       z_n^F(t)=y_n(t)+sum_(i in F)e_i,n(u_i,n(t)),
       A_Z,n^F(t)=A_Y,n(t)+sum_(i in F)b_i,n(u_i,n(t))
                    +(1/2)y_n(t) wedge sum_(i in F)e_i,n(u_i,n(t)).   (14)

At a physical time, at most one excursion is nonzero since the retained intervals are disjoint. Formula (14) is the first attempt's verified finite splice formula, written with clamping to include boundaries and changed durations. Every term in the finite sums converges uniformly, so the global coordinates of Z_n^F converge uniformly to those of Z^F. Their increment coordinates converge uniformly too, since an area increment is A(t)-A(s)-(1/2)z(s) wedge z(t) and the globally convergent first levels are bounded.

Take F to be all limiting attached loops of duration >=delta, which is finite. For sufficiently large n, every attached approximating loop of duration >=2delta is matched to a limiting attached loop in F. Indeed an isomorphism error smaller than delta preserves a duration lower bound >=delta; such loops correspond to the finite limiting collection of all soup loops of duration >=delta, and its nonattached members stay nonattached by compact separation. Thus all loops omitted from F_n have duration <2delta. No order assumption about these omitted loops is necessary.

The first attempt's truncation bound at exponent r gives, uniformly in large n,

       D_r(full output_n,Z_n^F) <= C_r Omega(2delta),
       D_r(full output,Z^F) <= C_r Omega(delta),
       Omega(u)=e(u)+[e(u)^2+M e(u)+h(u)]^(1/2),          (15)

where C_r absorbs the rerooting constants. Since variation bounds every single increment, the same estimates hold in d_infty. The finite splice convergence above and the triangle inequality show

       limsup_n d_infty(full output_n,full output)
                   <= C_r[Omega(2delta)+Omega(delta)].   (16)

Let delta decrease to zero and use (12). This proves enhanced uniform convergence, with both levels retained. Finally all full outputs have r-rough norm <=C_r M, so interpolation (10) proves (13). The symmetric tensor level converges in p/2-variation by the product estimate from the first attempt, so this is ordinary step-two rough-path convergence as well. QED.

More explicitly, for any fixed finite retained set, with its finite-splice increment error v_n,F=d_infty(Z_n^F,Z^F), the proof supplies

       D_p(full output_n,full output)
       <= C_(r,p) M^(r/p)
          [Omega(2delta)+Omega(delta)+v_n,F]^(1-r/p).    (17)

The finite-splice error is controlled by input enhanced coordinate errors, normalized temporal-root errors, actual interval-start/duration errors, and the modulus of the limiting backbone and loops. Their qualitative convergence was proved above; no universal power modulus for those first-contact errors is asserted.

## 5. First hostile referee audit of Theorem 3

* **Clock convergence cannot come from small loop-isomorphism error alone.** The proof explicitly uses convergence of total attached duration from d_R0. The finite predecessor-sum remainder is nonnegative and controlled by total minus retained mass.
* **Changing temporal roots could change area at the seam.** Formula (11) uses a central increment c on each complete period. Terminal area is root invariant; the global area coordinate itself is not simply periodic.
* **Small-loop order may change arbitrarily.** Only each fixed finite family must be eventually ordered. All omitted loops are bounded using energy and absolute-area tails on their own clocks. The comparison never aligns their order across configurations.
* **Uniform first-level convergence is not enough.** Finite enhanced inputs and area tails are used to prove uniform second-level convergence before interpolation is invoked.
* **The endpoint exponent r=p is excluded.** The power 1-r/p would vanish. Without an additional compactness condition, (17) yields no endpoint continuity.
* **Physical time is retained.** Every output is constantly extended onto [0,H]; the proof compares increments at the same physical times. Time normalization occurs only for storing backbone/individual loop input data, with all original durations retained.
* **Uniformity over arbitrary tie breaks.** Any selected root is between the source's min and max roots, both converging to the unique regular limiting root. Distinct fixed limiting first hits force strict eventual finite order. This supports the assertion for all sequences B_n.
* **A bare weak geometric lift is insufficient without the hypotheses.** Existence, finite r-variation, finite absolute terminal area, and tight tails are all stated on enhanced inputs. They are not deduced from original source regularity.

At this point the fixed-schedule restriction has been removed under a fully specified stronger set of enhanced hypotheses. Brownian verification of these hypotheses, quantitative cusp moduli, and convergence in a specific lattice coupling still need separate work.

### Theorem 3b: removing the uniform r-energy-tail assumption

The uniform r-energy-tail part of (12) is sufficient but stronger than necessary. Keep hypotheses 1-3 of Theorem 3, and keep its absolute-area tail h(delta)->0. Instead of e(delta)->0, assume only

       m(delta)=sup_(n and limit, attached loops of duration<=delta)
          [diameter(ell)+(sup_(s<t)|a_ell(s,t)|)^(1/2)] -> 0.    (28)

Then the conclusion (13) still holds, with

       Omega_0(delta)=m(delta)
          +[h(delta)+m(delta)^2+M m(delta)]^(1/2)        (29)

in place of Omega in (15)-(17). The diameter and local area increments in (28) are taken at the originally supplied roots. Hypothesis (28) is an enhanced small-loop equicontinuity requirement, not an aggregate variation-tail condition. Its first-level part already follows from the source's equicontinuity and d_R0 convergence; its area part is extra.

**Proof of the sharpening.** Every individual input still has summable r-energy and absolute areas by hypothesis 3, so Theorem 1 constructs its output, and the uniform full-output r-rough bound remains C_r M. In the full-minus-truncated global coordinate formulas, omitted excursions at any one physical time come from at most one loop. For a loop of duration <=delta, its rerooted excursion magnitude is <=m(delta). A rerooted area prefix crosses at most one old temporal seam. Split it there and apply Chen: the two original local area increments are each <=m(delta)^2 and the first-level cross term is <=m(delta)^2/2. Thus its rerooted prefix area is <=(5/2)m(delta)^2. Every completed omitted loop contributes its terminal c, whose total absolute sum is <=h(delta).

Formula (4), valid first for finite truncations and then by the individual summable limit, therefore gives on the entire horizon

       sup |x_full(t)-x_trunc(t)| <= m(delta),
       sup |A_full(t)-A_trunc(t)|
                <=h(delta)+(5/2)m(delta)^2+(1/2)M m(delta).

The first levels of full and truncated outputs are uniformly bounded by C_r M. Passing from global coordinates to increments doubles the displayed global errors and adds at most C_r M m(delta) from the wedge term. Consequently their d_infty distance is <=C_r Omega_0(delta). This is a pointwise estimate, so it does not need uniform tightness of the sum of r-energies. The finite moving-splice convergence proof in Theorem 3 is unchanged. All approximating omitted loops again have duration <2delta. Use this enhanced-uniform tail estimate, let delta decrease to zero, then apply interpolation (10) using the full-output uniform r-bound. This proves Theorem 3b and (29). QED.

Referee check: this sharpening only changes how the enhanced uniform error is estimated. It still requires the aggregate r-energy bound for interpolation and the aggregate absolute-area tail for completed loops. Neither can be dropped on the basis of a vanishing individual-loop diameter.

## 6. Brownian-loop input summability: a proved probabilistic special case

Here D is bounded and Gamma is a fixed compact set with a tubular-volume bound

       |{x: dist(x,Gamma)<=rho}| <= K rho^(2-d),
       0<rho<=1,  d<2.                                  (18)

A compact set of upper Minkowski dimension strictly less than 2 satisfies such a bound for some d<2 above that dimension. The constants may depend on Gamma. Use the usual planar Brownian loop measure with generator (1/2)Delta, whose rooted bridge representation has density dx dt/(2 pi t^2). A change of the intensity convention changes only constants. Give every Brownian loop its canonical geometric Stratonovich enhancement. For r>2 define N_r(ell) as the rough norm at exponent r and c(ell) as its terminal signed area.

**Proposition 4.** For a finite-intensity Brownian loop soup in D and 0<delta<=1,

       E sum_(ell, duration<=delta) N_r(ell)^r
                  <= C_(r,D) delta^(r/2-1),              (19)
       E sum_(ell intersects Gamma, duration<=delta) |c(ell)|
                  <= C_(D,Gamma) delta^((2-d)/2).        (20)

Consequently the small-loop r-energy of the entire soup is summable almost surely, and the absolute terminal area of loops intersecting Gamma is summable almost surely. Their respective duration tails vanish almost surely. The finitely many loops of duration >=1 also have finite norms/areas almost surely. The same assertion holds conditionally for an independent random Gamma satisfying (18) almost surely, without claiming integrability of its random tubular constant.

### Proof of the bridge rough-norm moment used in (19)

Let B be standard planar Brownian motion on [0,1] with its Stratonovich enhancement and signed area a_B(s,t)=(1/2) integral_s^t (B_u-B_s) wedge dB_u. The wedge's antisymmetric cross-variation vanishes, so this is also its Ito expression. For every sufficiently large integer m,

       E|B_t-B_s|^(2m) <= C_m |t-s|^m,
       E|a_B(s,t)|^m <= C_m |t-s|^m.                    (21)

The first is a Gaussian moment calculation. For the second, Brownian scaling reduces to [0,1]; the Burkholder-Davis-Gundy moment inequality bounds the Ito integral by a constant times E(integral_0^1 |B_u|^2 du)^(m/2), which is finite by Gaussian moments and Jensen. This use of BDG is a standard martingale theorem, not a new conjectural input.

Choose alpha with 1/r<alpha<1/2 and an integer m with 2m(1/2-alpha)>1. Sum over all adjacent dyadic intervals I of length 2^-k:

       Q=sum_(k>=0,I level k)
            [ |B_I|^(2m)/|I|^(2m alpha)
               + |a_B(I)|^m/|I|^(2m alpha) ].

By (21), E Q <= C sum_k 2^k 2^-km 2^(2m alpha k)<infinity. With K_B=Q^(1/(2m)), every dyadic increment satisfies |B_I|<=K_B |I|^alpha and |a_B(I)|<=K_B^2 |I|^(2alpha). Any interval [s,t] decomposes, up to its endpoints, into dyadic intervals with at most two of each size and no interval larger than t-s. Their lengths' alpha-powers sum to at most C_alpha |t-s|^alpha, and their 2alpha-powers to at most C_alpha |t-s|^(2alpha). Add first increments and use Chen's identity for area. The area cross terms have absolute sum at most (1/2)(sum_I |B_I|)^2. Continuity lets finite dyadic concatenations converge to the entire interval. Thus

       |B_st|<=C_alpha K_B |t-s|^alpha,
       |a_B(s,t)|<=C_alpha K_B^2 |t-s|^(2alpha).         (22)

Because alpha*r>1, summing |t-s|^(alpha*r) over any partition of [0,1] is <=1. Hence N_r(B)<=C_alpha K_B. Choosing m arbitrarily large in this construction gives finite moments of any prescribed order of N_r(B).

The normalized bridge W_u=B_u-uB_1 has the usual standard Brownian bridge law. Its canonical lift is obtained by translating B's lift by the bounded-variation path -uB_1. This agrees with its Stratonovich lift: polygonal approximations of W are exactly polygonal approximations of B minus uB_1, and the integration-by-parts formulas for this bounded-variation translation pass to their Stratonovich limits. For h=t-s, direct integration by parts gives

       a_W(s,t)=a_B(s,t)
          - integral_s^t B_su wedge B_1 du
          +(h/2) B_st wedge B_1.                        (23)

No anticipative Ito integral is being taken in this formula: the mixed integral displayed is an ordinary time integral. Since |B_1|<=K_B, (22) bounds the added terms by C_alpha K_B^2 h^(1+alpha), which is <=C_alpha K_B^2 h^(2alpha) for h<=1 and alpha<1. The bridge first increments are bounded by C_alpha K_B h^alpha as well. Thus N_r(W) has finite moments of every prescribed finite order. A duration-t bridge scales spatially as sqrt(t) and its area as t, so

       E N_r(bridge of duration t)^r = C_r t^(r/2).     (24)

The norm is invariant under affine increasing time normalization; this is why the physical duration appears only through spatial Brownian scaling.

### Proof of (19)

Poisson integration of a nonnegative mark equals intensity times its loop-measure integral. Root locations for loops contained in D are in D. Dropping the restriction that the bridge stay in D only increases this integral. Formula (24) therefore gives

       E sum_(duration<=delta) N_r(ell)^r
          <= C_r |D| integral_0^delta t^(r/2-2) dt,

which is (19), since r/2-1>0. There is no spatial-intersection conditioning in this estimate.

### Proof of (20), including the intersection selection

Let R=sup_(u<=1)|W_u| and A=a_W(0,1). The bridge maximum satisfies P(R>=z)<=C exp(-c z^2). Indeed sup|W|<=2 sup|B|, and the reflection bound in each coordinate, followed by a union bound, supplies this Gaussian tail. Also E A^2<infinity, by the bridge moment proof above. As an optional check on the normalization, the bridge semimartingale representation dW=d beta-W/(1-u) du gives A=(1/2) integral W wedge d beta: the drift's wedge is zero. Ito isometry gives E A^2=(1/4) integral_0^1 E|W_u|^2 du=1/12. Stopping before 1 and taking the L2 limit justifies the singular endpoint.

A duration-t bridge rooted at x can hit Gamma only if R>=dist(x,Gamma)/sqrt(t). Its terminal area is t A. Cauchy-Schwarz, without asserting independence between A and the hitting event, gives

       E[|t A| 1_(bridge hits Gamma)]
            <= C t exp(-c dist(x,Gamma)^2/t).           (25)

By (18), for 0<t<=1,

       integral_D exp(-c dist(x,Gamma)^2/t) dx
                       <= C_(D,Gamma) t^((2-d)/2).     (26)

To check (26), first handle t>=1/4 by the trivial bound |D|, absorbed into a constant times t^((2-d)/2). For t<1/4 split root locations into shells k sqrt(t)<=dist<(k+1)sqrt(t). For (k+1)sqrt(t)<=1 their volumes are bounded by K (k+1)^(2-d) t^((2-d)/2), and summing the Gaussian factors exp(-c k^2) is finite. The remaining locations have distance >=1-sqrt(t)>1/2; their total contribution is bounded by |D| exp(-c'/t), which is <=C t^((2-d)/2). The portion with dist<=sqrt(t) is covered by the first shell. This proves (26), including the large-shell remainder.

Insert (25),(26) into the loop-measure density dx dt/(2 pi t^2). The result is

       C integral_0^delta t^-1 t^((2-d)/2) dt
                     = C' delta^((2-d)/2),

which proves (20). In particular the spatial selection was handled explicitly, rather than replacing the selected bridge by an unconditional one.

### Almost-sure consequences and their limits

Each nonnegative marked sum below duration 1 has finite expectation by (19),(20), hence is finite almost surely. Its tails tend to zero because all individual durations are positive and the marked series is summable. Loops of duration >=1 have finite loop measure, bounded by |D|/(2 pi) integral_1^infinity t^-2 dt, so there are finitely many such loops almost surely; each has a finite continuous bridge lift. These observations prove all the asserted summability statements. Cyclic rerooting preserves terminal area and changes the rough norm by at most the factor from Section 2, so the assertions survive the source's choice of root.

This validates the one-configuration loop-energy and absolute-area conditions for the Brownian/SLE setting in bounded domains, since the independent SLE range has upper Minkowski dimension <2 as used by the source. It does NOT prove uniform tails over a coupled sequence of distinct soups or varying arbitrary backbones. Nor does it identify the full attached lift with Brownian Stratonovich lift. A supplied backbone lift and the enhanced convergence hypotheses of Theorem 3 still have to be checked.

## 7. Boundary test: a zero-area counterexample along every original-distance cusp

**Proposition 5.** For every p>2, beta>0, and C>0, there is a configuration X in the source's R and a sequence (X_n,lambda_n) in R' such that

       d_R0(X_n,X) -> 0,  lambda_n -> 0,
       lambda_n >= C d_R0(X_n,X)^beta eventually,

but the first levels of the outputs fail to converge in physical-time p-variation. The newly inserted loops have zero area in every increment, uniformly vanishing enhanced coordinates, vanishing total duration, and uniformly bounded total p-energy. Absolute terminal-area tails remain unchanged. Thus a cusp formulated using the **original** source distance cannot by itself yield p-variation continuity, even if finite-loop matching is augmented by uniform signatures. This does not refute a cusp with the source's proposed distance adapted to aggregate stronger norms.

### Full construction of a regular limiting configuration

Take gamma(s)=(s,0), 0<=s<=1. Enumerate distinct rational numbers s_i in (0,1), i>=1, so that the set is dense. Give loop i duration d_i=2^-i and radius R_i=2^-2i, and let its originally rooted parametrization be

       ell_i(u)=(s_i+R_i+R_i cos(2 pi u/d_i),
                              R_i sin(2 pi u/d_i)), 0<=u<=d_i.

Its first intersection with gamma is the leftmost point (s_i,0), at the unique temporal root u=d_i/2. The first hit is interior to the backbone and the loop visits both upper and lower sides of the axis arbitrarily close to this root, so it is regular in Definition 3.1. The first hits are distinct and dense. The sum of durations is 1, and there are finitely many loops above any duration threshold. All loops have speed at most 2 pi R_i/d_i=2 pi 2^-i, so they are equicontinuous. These facts verify all conditions (i)-(v) of R, not just R0.

Put L={ell_i} and X=(gamma,L). The source output W=Xi(X,0) is continuous and starts at (0,0). The deterministic circle lifts also have summable p-energy and absolute areas, although the counterexample only needs first levels. The original temporal roots at the rightmost point are distinct from the source's rerooting point; there is no duplicate limiting temporal root.

### Inserting zero-area loops at the initial end

Let N_n increase to infinity and r_n=N_n^(-1/p), so N_n r_n^p=1. By continuity of W at 0 choose u_n>0, tending to zero, with

       sup_(0<=t<=u_n) |W(t)| <= r_n/10.

Define D(v)=sum_(i:s_i<=v)d_i. Since all s_i>0 and sum d_i<infinity, D(v)->0 as v decreases to zero. Choose a positive rational epsilon_n, tending to zero, so that

       epsilon_n<r_n/10,
       D(epsilon_n)+epsilon_n<u_n/4.

Choose eta_n>0 with eta_n<min(u_n/4,r_n^2). Add N_n loops with equal duration eta_n/N_n, rooted at the distinct irrational positions

       sigma_j,n=(sqrt(2)/2) epsilon_n j/(N_n+1), 1<=j<=N_n.

Each added loop is the piecewise-linear vertical traversal

       (sigma_j,n,0) -> (sigma_j,n,r_n)
       -> (sigma_j,n,0) -> (sigma_j,n,-r_n)
       -> (sigma_j,n,0),

with four equal time segments. It meets the backbone only at its spatial root. Choose the permitted temporal root at its initial time. Its based first-level path is one-dimensional and all its antisymmetric area increments are zero. Its second symmetric tensor level is determined by its displacement and is bounded uniformly by a constant times r_n^2. Its first-level p-variation lies between r_n and 4r_n, so the added total p-energy is bounded above and bounded below independently of n. The first hits of added loops are distinct from all old rational first hits.

Let L_n be L plus these new loops and X_n=(gamma,L_n). Each X_n satisfies R0: finite total duration, local finiteness by duration, and equicontinuity of its original uniformly Lipschitz loops plus a finite set of continuous new loops. The new loops need not be regular; that is allowed because lambda_n will be positive.

An identity matching of all original loops is a delta-isomorphism whenever delta exceeds the new-loop duration. The total attached duration changes by eta_n. The difference between the loop continuity-modulus functions is at most the new-loop diameter 2r_n, uniformly over the modulus parameter. Therefore

       d_R0(X_n,X) <= 2 eta_n/N_n + eta_n + 2r_n <= 5r_n       (n large).

Take lambda_n=(5r_n)^(beta/2). It tends to zero and is <=1 for large n. Because d_R0<=5r_n,

       lambda_n / [C d_R0(X_n,X)^beta]
                          >= (5r_n)^(-beta/2)/C -> infinity.

Thus the stated cusp holds eventually. Since lambda_n>0, (X_n,lambda_n) is in R'. Every newly added loop is completely traversed before physical time

       D(epsilon_n)+lambda_n epsilon_n+eta_n < u_n/2 < u_n.

This bound uses only predecessor durations, the cumulative added duration, and the backbone time cost lambda_n sigma; it remains valid with the infinitely many original loops between new hits. Concentration near the initial point is crucial: lambda_n may be too large relative to an output modulus at a fixed interior root, but lambda_n sigma_j,n is arbitrarily small here.

### The nonvanishing p-variation lower bound

Write W_n=Xi(X_n,lambda_n,B_n) with the specified roots for new loops. For each new loop let a_j,n be its physical start and v_j,n the time of its first upper peak. Both are before u_n. The vertical increment of W_n on [a_j,n,v_j,n] is exactly r_n, while the absolute vertical increment of W is at most 2r_n/10. Thus

       |(W_n-W)(v_j,n)-(W_n-W)(a_j,n)| >= (4/5)r_n.

These intervals are ordered and have disjoint interiors. Include all their endpoints in one finite partition, and include the intervening gaps as additional partition intervals. It follows that

       ||W_n-W||_(p-var) >= [(N_n)((4/5)r_n)^p]^(1/p)=4/5.   (27)

The comparison is on any common physical horizon by constant terminal extension, exactly as in Theorem 3. The source's uniform continuity theorem still gives uniform convergence; (27) concerns the stronger p-variation norm.

The total added terminal area is exactly zero, so absolute-area tails of the original circle family are unchanged, uniformly in n. Every fixed duration-cutoff loop is eventually an unchanged original loop, hence its enhanced matching is exact. The new loops' enhanced coordinate sizes tend to zero. Nevertheless for any r<p their summed r-energy is bounded below by N_n r_n^r=N_n^(1-r/p), which diverges. This explicitly shows why the stronger r-bound in Theorem 3 cannot be replaced merely by a bounded target-p energy plus uniform enhanced convergence. Tight target-p energy tails would also exclude this construction, so it does not show that losing regularity is always necessary. QED.

### Counterexample referee checks

The limiting X really is in R, including bilateral regularity and unique temporal roots. The perturbations only need R0, because lambda_n>0. Source d_R0 includes its total-duration and continuity-modulus terms, both accounted for above. The output discrepancy is proved on actual physical intervals, not on reordered loops or an erased clock. No terminal area is hidden: the added loops are one-dimensional, so even their local signed areas vanish. The cusp constant and exponent are arbitrary but fixed before choosing the sequence, and the lower bound 4/5 is independent of them. This is a counterexample for the original distance and weaker enhanced-uniform variants, not for Theorem 3 or for every possible norm-adapted cusp.

## 8. Completed finite checks and limitations

The numerical code is check_moving.py, with its saved output moving_checks.json. For 4000 circular reroot tests, the maximum local area formula error was 1.5543122344752192e-15 and the maximum terminal-area error was 1.7763568394002505e-15. These tests explicitly cross the temporal seam and include the central area contribution.

The moving-clock sequence uses dyadic dense root locations, varying durations, varying circle radii, moving spatial roots, and lambda tending to zero. It compares actual physical times at 2501 sample points. From 7 to 4095 approximating loops, the sampled clock error relative to an 18-level reference decreased from about 0.07593 to 0.002990; the sampled finite-retained area-increment error decreased from about 0.008641 to 0.0001451. The reference still has a finite cutoff and is not the exact infinite limit. A coarser 12-level reference initially caused an apparent numerical error floor; its data are preserved in moving_checks_coarse_reference.json. Refining the reference resolved that numerical artifact. No monotonicity of every approximation error is used in the proof.

The zero-area numerical boundary check confirms N r_n^p=1 to rounding error while N r_n^r increases for r<p, and each tree polygon has exact zero area. The recorded output p-variation lower bound 0.8 comes from the analytic construction, not an optimized numerical partition search.

`lake env lean ~/brain_workers/TRIO_1011/op/P0139/MovingClockChecks.lean`, from ~/lean_verify, passed with exit code 0 and empty stdout/stderr in 166.2437 seconds, with a 3600-second timeout. It checks a finite even-power interpolation inequality and the terminal central-area identity under rerooting. The first run used unsupported ASCII bounded-quantifier syntax; the second lacked the narrow Finset ring-sum import. Both diagnostic outputs are preserved, and the corrected source imports only the needed Mathlib modules. There is no sorry, admit, native_decide, or extra axiom. This formal verification is finite algebra only; the noninteger variation interpolation and analytic clock/tail arguments are proved in prose above.

The Brownian bridge check in check_bridge.py uses 4000 samples at 512 polygon steps. The bounded-variation translation identity (23) at terminal time agrees to maximum error 4.468647674116255e-15. The empirical bridge-area second moment is 0.0865532, with estimated standard error 0.00256475, consistent with the exact continuum value 1/12=0.0833333. The discretized simulation is only a normalization and finite-identity check; the loop-measure integrals and almost-sure summability are proved analytically. Its output is bridge_checks.json, seed 13906.

## 9. Current remaining gap

The positive result now permits the source's actual attachment times, durations, temporal roots and inverse clocks to move. Theorem 3b gives a concrete rough p-variation estimate for p>r>2 on enhanced inputs with bounded aggregate r-energy, enhanced small-loop equicontinuity, and tight absolute terminal-area tails. Proposition 4 supplies the individual Brownian-loop summability and tail exponents in bounded domains. Proposition 5 shows every power cusp based solely on the original source distance can fail, even without local or terminal loop area.

Still unproved: a quantitative power modulus for regular first-contact/root and inverse-clock stability in a norm-adapted source metric; an endpoint-p theorem without further compactness of variation; enhanced matched-loop/backbone convergence and uniform stochastic tails for a specified random-walk/Brownian coupling; and equality of the prescribed attached enhancement with the canonical Brownian Stratonovich enhancement. One-configuration Brownian summability does not imply those uniform coupling assertions. These are explicit remaining tasks, not implicit consequences of the proved special cases.

The honest verdict remains **PARTIAL**, with substantial additional proved results. Neither the original-cusp counterexample nor the strengthened positive theorem settles all formulations of the open question with an appropriately adapted topology.

This second attempt is finished. All new proofs, the two approaches, the brain query, hostile checks, finite computations and formal diagnostics have been saved. The new positive theorem permits moving schedules under explicit enhanced hypotheses; the unadapted-cusp obstruction supplies a precise negative boundary. The remaining tasks are the ones listed in this section.
