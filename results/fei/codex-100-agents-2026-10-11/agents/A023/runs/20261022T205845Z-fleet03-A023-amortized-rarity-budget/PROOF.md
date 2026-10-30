# Three bent cores: a single symmetric reserve pays the complete stopping bill

All logarithms in entropy are base two; ln denotes the natural logarithm. Let m>=4 be even, M=2^m, delta=1/M and e=sqrt(delta). Let b be ANY Boolean bent function on m uniform bits. Flip its value at distinct vertices v,w to obtain b_v,b_w. On one additional independent sign z set g0=zb, g1=zb_v, g2=zb_w. Let A,B be independent fair point indicators, independent of the data, and set f=g0+A[g1+B(g2-g1)-g0]. Original terminal weights are pi=(1/2,1/4,1/4). Write H_T=sum pi_j H(gj), I_T=sum pi_j I(gj), I_C=I(f)-I_T and R=2sum_{j<k}pi_j pi_k I(gj gk). Let eta=1 if v,w are adjacent in the physical cube, zero otherwise.

Then I_C=2delta and R=(3m/2-eta/2)delta. The complete control stopping bill obeys

    H(f)-H_T-R < [9/(4 ln 2)+eta/4] I_C < 4 I_C.

In particular H(f)<=4I(f), with both full terminal costs retained. This is an all-dimensional proper-class theorem, not universal FEI. The asymptotically sharp control rate for this family is 9/(4 ln 2)+eta/4.

## Exact physical accounts

Each outer-control edge differs on a single data vertex, so its influence is delta; the inner bit differs on two vertices only when A=1, giving influence delta. Thus I_C=2delta. Each single-point product gj g0 has influence 2m delta. The two-point product g1g2 has influence 4m delta-4delta eta: adjacency removes the two directed internal edges. Substitution into the ORIGINAL pi weights gives R=(3m/2-eta/2)delta. The z coordinate cancels from all pair products.

For each physical data coordinate, the event that a product gjgk is pivotal is the symmetric difference of the two core pivotal events. Hence I_i(gjgk)<=I_i(gj)+I_i(gk). In R, terminal j owns rate 2(1-pi_j) of its ORIGINAL weighted influence. This gives R<=2I_T, coordinate by coordinate; no terminal bank is recreated at either control descendant.

## Exact coherent spectrum

Translation and multiplication by a constant sign reduce to v=0, b(0)=1 without changing entropy, influence or adjacency. Write b_hat(T)=e s_T, s_T in {+1,-1}. The other edit has sign b(w). The control-zero coefficient, with the obligatory z frequency suppressed, is

    e s_T - (delta/2)[1+b(w)chi_T(w)].

Each of the other three control sectors has coefficient magnitude delta on exactly M/2 data rows and zero on the rest. Their TOTAL raw entropy is 3m delta. These statements follow directly by Fourier expanding the two distinct singleton control cells A(1-B), AB; they retain the coherent cross term.

On the M/2 rows with b(w)chi_T(w)=-1, the zero-control coefficient remains e s_T. On the other M/2 rows it is e s_T-delta. On that latter half, the counts of s_T=+1 and s_T=-1 are M/4+sqrt(M)/2 and M/4-sqrt(M)/2. Indeed sum s_T=sqrt(M)b(0) and sum s_T chi_T(w)=sqrt(M)b(w), by Fourier inversion. This uses w!=0; coincident edits require a different formula.

Let F(x)=(1+x)^2 ln((1+x)^2). Define the point-flip entropy deficit D=m-H(b_v)=m-H(b_w) and the signed root-sector relative entropy J (its root mass is 1-3delta/2, so J may be negative). Exactly,

    D ln 2 = [(1-e)F(2e)+(1+e)F(-2e)]/2,
    J ln 2 = [(1-2e)F(e)+(1+2e)F(-e)]/4,
    H(f)=m+(3m/2)delta-J,
    H_T=m-D/2.

Thus the ACTUAL signed bill, not a bound obtained by dropping a positive grouping surcharge, is

    H(f)-H_T-R = D/2-J+eta delta/2.

## Scalar bounds with a signed remainder

For |x|<1, the absolutely convergent expansion is

    F(x)=2x+3x^2+sum_{k>=3} 4(-1)^(k-1)x^k/[k(k-1)(k-2)].

It follows by multiplying the power series for ln(1+x), or differentiating three times and integrating with F(0)=0,F'(0)=2,F''(0)=6. Here 2e<=1/2, so all substitutions and regroupings occur strictly inside the radius of absolute convergence. Every term beyond 8delta in D ln2 is NONPOSITIVE: even coefficients are negative, and each positive odd coefficient receives the negative multiplier -e. Therefore

    0<=D<=8delta/ln2.

For J ln2 the quadratic term is -delta/2; every higher term is negative. Bound the even tail using k(k-1)(k-2)>=24 for even k>=4, and the odd tail using that denominator>=6 for odd k>=3. Geometric summation gives

    -delta/2-(3/4)delta^2/(1-delta) <= J ln2 <= -delta/2.

The even tail is at most delta^2/[12(1-delta)] in absolute value; the odd contribution is at most 2delta^2/[3(1-delta)]. Their sum is 3delta^2/[4(1-delta)]. No sign of the earlier A021 remainder is imported.

Since delta<=1/16, (3/4)delta/(1-delta)<=1/20. Consequently

    D/2-J+eta delta/2 <= [(91/20)/ln2+eta/2]delta.

Divide by I_C=2delta>0. The upper rate is at most 91/(40 ln2)+1/4<4. For the final strict inequality, ln2=2 sum_{j>=0}(1/3)^(2j+1)/(2j+1)>2/3>13/20, so 91/(40 ln2)<7/2. No numerical logarithm is a proof premise.

The series also give D/delta ->8/ln2 and J/delta ->-1/(2 ln2), hence the exact rate tends to 9/(4 ln2)+eta/2 as m tends to infinity through even integers, along any adjacent or nonadjacent pair family. This limit follows from the displayed geometric tail estimates, not a numerical fit.

## Full terminal payment and explicit stopping rule

Query A. If A=0 stop at g0; if A=1 query B and stop at g1 or g2. Its expected terminal entropy and influence are exactly H_T,I_T. Open R once at the root, pay the total control bill once, and delete that mark before entering any terminal. The two control entropy drops telescope to H(f)-H_T. A large individual node is allowed; no node is given a fresh copy of R.

Bent b has I(b)=m/2. A single flip changes each physical data influence by at most 2delta, hence I(zb_v)>=1+m/2-2m delta and likewise for w. Since m delta<=1/4 for every integer m>=4, 2I(gj)>=m while H(gj)<=m for all three terminals. Therefore H_T<=2I_T. Combining the control theorem and R<=2I_T proves H(f)<=4I(f). The z balancing coordinate matters to this simple terminal certificate and is not silently removed.

## Exact unresolved line

Neither this root proof nor reserve conservation pays an arbitrary mixed DATA query. At a nonconstant core-data restriction, the original bent profiles become nonflat and unequal, and the signed controller entropy changes. The unpaid step is to bound that actual signed residual using released ORIGINAL R plus unused original terminal surplus, with both complete terminal debts and all past bookings retained. There is no universal terminal admission, arbitrary control-width theorem, or localized odd-face bound here.

## Sharp combined bound

The preceding separate estimates suffice, but retain avoidable slack. For every integer l>=2, set u_l=(2l)(2l-1)(2l-2), v_l=(2l-1)(2l-2)(2l-3), both strictly positive. Directly combining the absolutely convergent expansions gives

    (D/2-J) ln2 = (9/2)delta - sum_{l>=2} [2(4^l-1)/u_l+(4^l-4)/v_l]delta^l.

Every bracket is strictly positive. Therefore the stronger, sharp uniform bound is

    [H(f)-H_T-R]/I_C < 9/(4 ln2)+eta/4 < 4.

The last inequality follows already from ln2>2/3: the largest rate is below 29/8. The tail is O(delta^2) by the earlier geometric estimates, so the upper constant is approached as m tends to infinity. No finite m is asserted to attain it. All-dimensional proof status is author proof pending independent review; the Lean check, if successful, certifies only its stated scalar sign lemma.
