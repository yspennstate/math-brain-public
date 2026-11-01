# C0133: zero velocity on the non-transient event — complete proof

2026-10-12. Complete argument, accepted after the hostile review recorded in FRESH_HYPERPLANE_REFEREE.md. The only environment assumptions are (IID) and (EL) from the original question. No bounded-stack, moment, uniform-ellipticity, exchangeability, or drift-sign condition is imposed.

## Statement

Let X be the nearest-neighbor excited random walk on Z^d with spatially IID whole cookie stacks, with every cookie transition strictly positive almost surely. Let T be the event ||X_n|| -> infinity. Then X_n/n -> 0 almost surely on T^c, and therefore X_n dot ell/n -> 0 there simultaneously for every ell.

## Published inputs, with their exact scope

These are used as proved literature theorems, not proved anew here.

1. Kosygina--Zerner, arXiv:1204.1895v2, Theorem 2.5, printed/PDF p.7: under (IID), (EL), the range is either almost surely finite or almost surely infinite. Its more detailed criterion using the sets F and numbers b_F is not needed here.
2. Same source, Theorem 3.16, p.14: for every nonzero direction u, P_0[A_u union A_{-u}] belongs to {0,1}, where A_u={X_n dot u -> infinity}. This is the two-sided directional zero-one law; the individual event A_u is NOT assumed to have probability zero or one.
3. Same source, Lemma 3.18, pp.14--16: if the range is almost surely infinite, spatial (IID) holds and every first-cookie direction has positive expectation, then for u<w,
   P_0({X_n dot ell >= u infinitely often} intersect {X_n dot ell <= w for every n})=0.
   (EL) supplies the positive first-cookie expectations.
4. M. P. W. Zerner, Electronic Communications in Probability 7 (2002), 191--197, Lemma 3, p.193: for a fixed nearest-neighbor path starting at zero and a signed coordinate vector e, if limsup X_n dot e/n > 0, then
   sup_{c>=0} inf_{L>=1} limsup_{M->infinity} F_{M,L}(c)>0,
   where T_m=inf{n:X_n dot e=m},
   Tset_{m,L}={n:T_m<=n<T_{m+L}, X_n dot e=m},
   h_{m,L}=diameter(Tset_{m,L}), and
   F_{M,L}(c)=(M+1)^{-1} sum_{m=0}^M 1{h_{m,L}<=c}.
   This is a deterministic path lemma, and does not assume that the walk is Markovian. On the event of positive limsup velocity all the T_m, m>=0, are finite. The published proof is available in zerner_download_reader.txt; a complete self-contained proof with simpler constants is also in DETERMINISTIC_PLANE_LEMMA.md.

All these inputs concern the same nearest-neighbor steps; the first three explicitly allow infinite cookie stacks and merely (EL).

## 1. Infinite range and a lower bound force directional escape

Suppose the original fresh IID walk has almost surely infinite range. Fix a signed coordinate vector e and write h(x)=x dot e. Lemma 3.18, applied with direction -e, u=-a and w=b, gives, for all integers a>=1 and b>=0,

P_0(h(X_n)<=a infinitely often AND h(X_n)>=-b for every n)=0.

Indeed -a<b, so the strict ordering required in that lemma holds. Intersect the full-probability complements of these countably many events. On this common event, if h(X_n) is bounded below, it is bounded below by some -b. For every a>=1 there are then only finitely many n with h(X_n)<=a. This is exactly h(X_n)->infinity. Consequently

{inf_n h(X_n)>-infinity} is a subset of A_e up to a null set.

In particular, when P_0(A_e)=0 and the range is almost surely infinite, the fresh walk is almost surely not bounded below in this coordinate.

This conclusion is used only for the ORIGINAL fresh IID walk. Lemma 3.18 will not be applied to a cookie-depleted environment.

## 2. Any prescribed finite history has vanishing long positive-excursion probability

Continue to assume infinite range almost surely and P_0(A_e)=0. Fix a finite nearest-neighbor path pi=(pi_0,...,pi_j), with pi_0=0 and h(pi_j)=0. Let z=pi_j. For a site y with h(y)>=0, let k_pi(y) be the number of departures from y in pi, that is #{0<=r<j:pi_r=y}. Form the right-half-space cookie field obtained by deleting the first k_pi(y) cookies at each such y. Let Y start at z in this modified field, and kill it at

D=inf{r>=1:h(Y_r)<=0}.

Thus a nonpositive first projected step is killed immediately; after a positive first step the walk is killed on its first return to the plane. Before killing it uses only cookies in h>=0. Define

f_{pi,L}(omega_+) = P_{z, shifted right field}(T_L(Y)<D),
p_{pi,L}=E[f_{pi,L}(omega_+)],

where T_L(Y)=inf{r>=0:h(Y_r)=L} and omega_+ is a fresh IID field on h>=0. The events T_L<D decrease with integer L. Their intersection is the event D=infinity and T_L<infinity for every L. Call its conditional probability f_{pi,infinity}. Probability continuity from above gives f_{pi,L} decreasing to f_{pi,infinity}.

To prove its expectation is zero, embed the history pi into a fresh walk on the ENTIRE lattice. Its quenched probability of following pi is

W_pi(omega)=product_{r=0}^{j-1} omega(pi_r, pi_{r+1}-pi_r, 1+#{0<=s<r:pi_s=pi_r}).

Under (EL) every factor is strictly positive, so W_pi>0 almost surely; W_pi=1 for the empty history. The future after pi, while killed as above, uses exactly the shifted right-half-space field defining f. Hence the fresh-walk probability of following pi and subsequently hitting all positive levels without another nonpositive projected position is

E[W_pi f_{pi,infinity}].

Every such full path is bounded below by the minimum projected coordinate of the finite path pi. Section 1 makes it directionally transient almost surely, and P_0(A_e)=0 makes this fresh-walk probability zero. Nonnegativity and W_pi>0 therefore imply f_{pi,infinity}=0 almost surely. Bounded convergence now gives

p_{pi,L}->0 as L->infinity.                                      (1)

No lower bound on W_pi, and no assertion of IID after depletion, was used. Cookie probabilities at different visit indices may have arbitrary dependence.

## 3. A front filtration and a conditional domination

Generate the walk by the complete cookie field and IID uniform variables U_0,U_1,..., independent of it, using one U at each departure to select the direction. For an integer m>=0 let T_m be the first hit of the plane h=m. Until T_m every departure site has h<m. Therefore T_m and the path stopped at T_m are determined by the field on h<m and the driving uniforms up to that hit, with no cookie on h>=m inspected or used.

Let H_m reveal the ENTIRE field on h<m, the value T_m, the stopped path through T_m, and the uniforms U_0,...,U_{T_m-1}. If T_m=infinity it reveals all uniforms and the entire path, which remains in h<m. This is measurable from the below-m field and the full independent uniform sequence, so the h>=m cookie field is independent of H_m. On {T_m<infinity}, the uniforms after T_m are fresh IID uniforms, by the elementary stopped-IID property, applied with the below-m field as independent initial data. First hitting m is a stopping time for this below-m construction.

The sigma-fields H_m are increasing in m: H_{m+L} contains the below-m field and enough of the stopped uniforms/path to recover the first hit of m and all of its stopped data. This remains true when a hitting time is infinite.

Here is a direct justification of the random-time freshness claim. For each finite t, the event T_m=t and any H_m event restricted to T_m=t are measurable with respect to the below-m field and U_0,...,U_{t-1}. These variables are independent of the h>=m field and U_t,U_{t+1},.... Check the claimed conditional product law first on cylinder events for this fresh field and these future uniforms, sum over finite t, and extend to their sigma-algebra. This proves the conditional assertion on T_m<infinity. The current location x can likewise be fixed in this partition; translation invariance of the product field then gives the same fresh law relative to x.

Fix integers c>=0 and L>c. Let P_c be the finite set of all paths pi of length j<=c, starting at zero and ending in h=0. On {T_m<infinity} put x=X_{T_m}. Define B_{m,L}^pi to be the event that the next j steps follow x+pi, and, from its endpoint, the actual walk reaches h=m+L before its first subsequent time with h<=m. Put B=0 if T_m=infinity.

Because L>c, the prefix cannot reach m+L. Consequently B_{m,L}^pi is determined by the walk through T_{m+L}; if T_{m+L}=infinity it is false. Thus

B_{m,L}^pi is H_{m+L}-measurable.                              (2)

Conditional on H_m and T_m<infinity, the entire half-space h>=m is fresh IID. For a fixed realization of this fresh field, the conditional probability of the prescribed prefix is a number W in [0,1]. The prefix may go below m; those departure probabilities can involve arbitrarily depleted stacks, but they still lie in [0,1]. Within h>=m the prefix consumes exactly the counts k_pi, since nothing there was used before T_m. The continuation event then has probability f_{pi,L} of the shifted fresh field. The multiplication rule for the quenched path law therefore gives W f_{pi,L}. Dropping W<=1 and averaging the as-yet-unseen right field proves

E[1_{B_{m,L}^pi} | H_m] <= p_{pi,L}.                         (3)

The translated coordinate x is H_m-measurable and spatial IID makes p_{pi,L} independent of x and m. On T_m=infinity both the indicator and its conditional expectation are zero. Importantly, (3) is conditioned BEFORE the prefix: it does not claim that the field remains unconditioned after observing the prefix.

## 4. Conditional domination gives an almost-sure frequency bound

Fix c,L,pi and a residue i in {0,...,L-1}. Set G_r=H_{i+rL} and Z_r=1_{B_{i+rL,L}^pi}. By (2), Z_r is G_{r+1}-measurable, and by (3), a_r=E[Z_r|G_r]<=p_{pi,L}. The partial sums

M_N=sum_{r=0}^{N-1}(Z_r-a_r)

are a G_N-martingale with increments of absolute value at most one. The conditional exponential-moment argument in ATTEMPT.md Section 1 yields

P(|M_N|>=epsilon N)<=2 exp(-epsilon^2 N/2).

Summation, Borel--Cantelli, and positive rational epsilon show M_N/N->0 almost surely. Therefore limsup_N N^{-1} sum_{r<N}Z_r<=p_{pi,L}. Combining the finitely many residue classes, whose relative sizes each tend to 1/L, gives

limsup_{M->infinity} (M+1)^{-1} sum_{m=0}^M 1_{B_{m,L}^pi}
    <= p_{pi,L} almost surely.                                (4)

Independence of the B events is not claimed or needed. All the parameters c,L,pi,i belong to countable sets; take one common full-probability event for every bound (4).

The limit order matters. The martingale law is applied with c,L,pi fixed and the number of sampled planes tending to infinity. Only after that almost-sure bound is established for all integer L do we let L tend to infinity. No summability in L, no uniform rate in c, and no exponential excursion bound is assumed.

## 5. Positive limsup speed contradicts the frequency bound

Let I_{m,L}(c) indicate that T_m,T_{m+L} are finite and the diameter h_{m,L} in the deterministic input is at most c. If I=1, take the last time s in the plane h=m before T_{m+L}. The first such time is T_m, so s-T_m<=c. The relative path from T_m to s is some pi in P_c. After s the path reaches m+L without another visit to m and hence without a nonpositive coordinate relative to m. Thus B_{m,L}^pi occurs, and pathwise

I_{m,L}(c)<=sum_{pi in P_c}1_{B_{m,L}^pi}.

Equations (4) and (1) imply, for every integer c>=0,

limsup_M (M+1)^{-1} sum_{m=0}^M I_{m,L}(c)
    <=sum_{pi in P_c}p_{pi,L}->0 as L->infinity.                (5)

The family P_c is finite and does NOT grow with L. If limsup h(X_n)/n>0, all nonnegative levels are reached, so I_{m,L}(c)=1{h_{m,L}<=c} for every m,L. On this event (5) contradicts Zerner's deterministic Lemma 3. Real c cause no issue: replacing c by its integer ceiling can only enlarge F. Thus, under infinite range and P_0(A_e)=0,

limsup_n X_n dot e/n<=0 almost surely.                       (6)

The finite-hitting-time indicators in I are essential: no use is made of an empty-plane diameter convention on paths that fail to reach the relevant levels.

## 6. Apply the range and directional zero-one laws

By Theorem 2.5 the original walk either has almost surely finite range or almost surely infinite range. In the finite-range case its positions are bounded on each sample path, so X_n/n->0 everywhere almost surely.

In the infinite-range case apply Theorem 3.16 to each coordinate e_j. If P_0(A_{e_j} union A_{-e_j})=1 for at least one j, then ||X_n||->infinity almost surely, and the required conclusion on T^c is vacuous.

In the remaining case those probabilities are all zero. Therefore P_0(A_e)=0 for every signed coordinate vector e. Apply (6) to e_j and -e_j, and intersect the finitely many full-probability events. This gives limsup X_n dot e_j/n<=0 and liminf X_n dot e_j/n>=0, so every coordinate tends to zero after division by n. Hence X_n/n->0 almost surely, in particular on T^c. Any fixed direction ell follows by taking its linear combination of the coordinates.

This completes the proof under exactly (IID), (EL). All uses of literature results are explicit above; the new part is the bounded-prefix conditional domination and its martingale-frequency argument.

## Verification and scope

The detailed thirteen-point review is FRESH_HYPERPLANE_REFEREE.md. The deterministic path lemma is additionally proved in full in DETERMINISTIC_PLANE_LEMMA.md. The finite covering construction was exhaustively tested on 65,536 planar eight-step paths (108,130 covering cases), and the delicate pre-prefix likelihood bound was tested with exact rational dependent-cookie examples that also refute posterior freshness. FreshHistoryChecks.lean passed with exit code 0 and checks the finite likelihood domination and strictly-positive-weight zero-preservation lemmas. It imports only the indicated specific Mathlib modules, has no sorry or native_decide, and uses ordinary kernel-checked proofs. This is not a Lean formalization of the infinite stochastic argument.

Verdict: SOLVED by the proof in this folder, not SOLVED_IN_LITERATURE. No remaining mathematical gap has been identified after the review. The original survey and Zerner's paper supply the stated inputs, but neither is being reported as a paper that states and proves the target question itself.
