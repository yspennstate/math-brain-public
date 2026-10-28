# Complete original-reference payment with a growing deleted matching

All logarithms below are base two. Let 2 <= a <= b and 0 <= k <= a. On a+b independent uniform bits, f is +1 exactly when a surviving edge of K_(a,b) has both endpoints one; remove the edges (i,i), 0 <= i < k. Use exactly these surviving positive width-two prime implicants, both endpoint orders, pi_e=1/4, and lambda_e=1/b. Vertex packing holds. Keep the original all-partitions queue reference, including every possible nonempty root set, with D=(1+1/(4b))^(ab-k)-1. Let Q(A) denote its output mass and C=sum_(A nonempty) fhat(A)^2 log(1/Q(A)). Then

    C < (1255/72) I(f) < 18 I(f).

This is an explicit complete-cost upper bound for one admissible representation, hence also an upper bound on a variational infimum containing it. It is not a lower bound on that infimum, an unbounded-ratio family, or a proof of universal FEI. For a,b>=3 the surviving table has no private leaves; boundary cases a=2 are included.

## 1. A generic width-two event, with every queue factor paid

In any graph with no isolated relevant vertices, assign each selected output coordinate to one incident edge; merge assignments to the same edge. The resulting N distinct gates own disjoint nonempty blocks B_i, of sizes s_i in {1,2}, whose union is A. Thus N<=d=|A|. Put an arc i->j if B_i intersects the support of gate j. Select the minimum-index vertex of each source strongly connected component as a root, then take a multi-source breadth-first directed forest. Every gate is reachable. An attaching coordinate is in its parent's owned block and its child's support. Children are ordered by attaching coordinate and gate index; this specifies a legal queue history. Each gate is used once, so the history is compatible with the all-partitions reference.

For c_i children the exact selected-event numerator, with the common D removed, is

    lambda^N 4^(-R) product_i [s_i(s_i+1) binom(2,s_i)
                      (c_i+1)(c_i+2) binom(s_i+c_i-1,c_i)]^(-1).

Root Bernoulli inclusion and all exclusions give lambda^R 4^(-R)/D; each nonroot label contributes lambda. The displayed subset factor includes both endpoint orders. The child-count factor includes c=0. The weak-composition factor specifies the ordered attachment multiset. There is no omitted rarity, ordering, label, or leaf factor.

The subset denominator is at most 6. The composition denominator is at most c+1, and

    (c+1)^2(c+2) <= 2*6^c  (c>=0).

At c=0 there is equality; the successive ratio is (c+2)(c+3)/(c+1)^2<=6, since the difference after cross multiplication is 5c^2+7c. Since sum c_i=N-R, the numerator is at least

    lambda^N 4^(-R) 12^(-N) 6^(-(N-R))
      = (lambda/72)^N (3/2)^R >= (lambda/72)^d.

This argument allows any number of roots; it does not presume a double-star or bounded deletion count. It bounds a selected event from below, so the full reference mass is at least this amount divided by D.

## 2. One-sided labels and the complete-cost decomposition

If A is only on the left, assign each selected vertex any surviving incident gate, give it its singleton block, and take all these gates as roots with zero children. There are no arcs between such blocks and other selected gates. Distinct choices are disjoint valid histories. Summing their exact numerators gives product_(i in A) deg(i)/(32b) >= 64^(-|A|), since deg(i)>=b-1. For a right-only A the same sum is at least (a/(64b))^|A|. For mixed A use section 1. Consequently, writing v_f=sum_(A nonempty) fhat(A)^2, R=sum_(right-only A) |A|fhat(A)^2, and M=sum_(mixed A) |A|fhat(A)^2,

    C <= v_f log D + (log 72) I + R log(b/a) + M log b.       (1)

The one-sided constant log64 was enlarged to log72. The same D is used once for every output; no denominator or weight is reoptimized between outputs.

## 3. Exact Fourier moments; no quadratic loss in k

Write u=2^-a, v=2^-b, n=a+b. The false event is the union of the two empty-side cylinders and the k isolated configurations consisting of precisely the two endpoints of one removed edge. These exceptional configurations are distinct and at mutual distance four. Therefore

    q=Pr(f=-1)=u+v+(k-1)uv,
    I0=2au(1-v)+2bv(1-u),  IL0=2au(1-v),
    I=I0+2k(n-4)uv >= I0.

For each exceptional point its two former boundary edges disappear and its n-2 remaining incident edges become boundary edges; normalization gives the stated influence increment. No overlap of changed edges occurs.

For nonempty A=(U,V), let r count deleted indices with exactly one endpoint in A. Direct character summation gives

    fhat(U,V)=-2[u 1_(V empty)+v 1_(U empty)+uv(k-1-2r)].

Summing the squared coefficients weighted by degree yields

    R=2v[b-2u(b+k)+u^2(b(k+1)+2k)],
    M=2uv[(k+1)(a(1-v)+b(1-u))-2k(u+v)].                  (2)

Here is a derivation of the mixed identity valid for all sizes. Under independent uniformly chosen subsets U,V, put Z=sum_(i<k) (-1)^(1_(i in U)+1_(i in V)). Then k-1-2r=Z-1, E(Z-1)^2=k+1, and E[|U|+|V|](Z-1)^2=n(k+1)/2. For an endpoint in a matching edge, this last identity follows by expanding (Z-1)^2 and conditioning that endpoint to be selected: the associated sign still averages to zero against its independent opposite endpoint. The same holds for unmatched endpoints. Multiplication by 4u^2v^2*2^n gives the total weighted contribution 2uv n(k+1). Subtract the empty-U and empty-V rows: their weighted expectations are respectively b(k+1)/2+k and a(k+1)/2+k, giving (2). The empty-empty term has degree zero. The R identity follows by expanding [1-u+u sum_(i<k)(-1)^(1_(i in V))]^2 and using E|V|=b/2, E|V|Z=-k/2, E|V|Z^2=bk/2.

For a right-only coefficient the ratio to its complete-bipartite counterpart in absolute value is at most 1+uk/(1-u)<=5/3, because au<=1/2 and u<=1/4. Hence R <=(25/9)R0, where R0=2bv(1-u)^2. Put h=b-a. For h=0 the label term vanishes. Otherwise log(b/a)<=h, b/a<=h+1, and h(h+1)2^-h<=3/2 (check h=1,2,3 and use successive ratio (h+2)/(2h)<=1 for h>=2). Since 1/(1-v)<=4/3,

    R0 log(b/a) <= 2 IL0,
    R log(b/a) <= (50/9) IL0 <= (50/9)I.                 (3)

Also (2) implies M<=2uv n(k+1). As n<=2b, (k+1)/a<=3/2, log b<=b, and b^2 2^-b<=9/8 (check b=2,3 and successive ratio (b+1)^2/(2b^2)<=1 for b>=3),

    M log b / IL0 <= 3bv log b/(1-v) <=4b^2 2^-b<=9/2.  (4)

## 4. Universal implicant root payment, reconstructed

For any proper nonempty subset of the w-cube, its edge boundary has at least w edges. Induct on w, splitting into two parallel (w-1)-cubes. If both slices are proper nonempty their internal boundaries already give 2(w-1)>=w for w>=2. If exactly one is proper nonempty, its internal boundary gives w-1 and a cross edge gives one more. If both are empty or full but different, the 2^(w-1) cross edges suffice. The base w=1 is immediate.

For a signed implicant fixing w coordinates, each fiber over the other coordinates contains its true corner. Its false subset thus has size at most 2^w-1, and the preceding boundary bound gives boundary >= w times its false size/(2^w-1), including empty false fibers. Average fibers and normalize cube edges:

    sum_(i in supp(e)) Inf_i(f) >= 2q w/(2^w-1).

For width two, multiply by lambda_e and use physical vertex packing. With S=sum_e lambda_e/4 this gives S<=3I/(16q). The root normalizer satisfies ln D<=ln(1+D)<=S, even when ln D is negative. Since v_f=4q(1-q),

    v_f log D <=3(1-q)I/(4 ln2)<9I/8,

where ln2>2/3 follows already from the first term 2/3 of the positive atanh(1/3) series. This is the universal root-payment premise attributed to A008, rederived here, not a private-leaf estimate.

## 5. Conclusion and remaining unsupported universal step

Since 72^4<2^25, log72<25/4. Substituting sections 3 and 4 into (1) gives

    C < [25/4+50/9+9/2+9/8] I = (1255/72)I <18I.

The argument is an ordinary all-parameter proof with rational finite checks supporting its boundary cases and queue interpretation. No Lean proof is claimed. The first unsupported universal line is that the analogous one-sided and mixed spectral label payments remain O(I) when deleted edges overlap in arbitrarily complicated patterns, or for arbitrary Boolean prime tables. Neither coefficientwise domination nor a small optimization gap supplies that line. A generic width-two forest cost is now available; the remaining task is spectral payment, not a growing-root combinatorial repair.
