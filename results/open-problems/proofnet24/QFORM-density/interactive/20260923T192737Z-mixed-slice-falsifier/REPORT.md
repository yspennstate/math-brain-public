# Diffuse orthogonal product projections can have unbounded conditional Fourier-slice norms

**Status:** A rigorous falsifier for a proposed absolute-value shortcut in the near-coloop QFORM endpoint. It is NOT a counterexample to bounded density of the quadratic form. It shows that conditioning on a transverse light projection before taking Fourier absolute values can erase the product-law smoothing, even when all full-frame leaf leverages equal 1/2.

## Statement

For each integer N>=7 there are six independent cap-one real coordinates X_1,...,X_6 and orthonormal linear projections L,V,P of X such that every original-coordinate row of the 6-by-3 projection matrix has squared norm exactly 1/2, while the joint density g(l,v,p) of (L,V,P) has unnormalized Fourier slices
\[
F_p(\eta,\xi)
 :=\int_{\mathbb R^2}e^{i(\eta l+\xi v)}g(l,v,p)\,dl\,dv
\]
satisfying
\[
\int_{\mathbb R}dp\int_{\mathbb R^2}
 |F_p(\eta,\xi)|\,d\eta\,d\xi
 \ge \frac{7N^2}{3072}. \tag{1}
\]
If the left side is infinite for an N, (1) has its usual extended-value meaning. In particular, no constant depending only on orthonormality, the cap-one product hypothesis, and the row-leverage gate 1/2 can bound this mixed conditional Fourier-slice norm.

## Construction and proof

Take pair sums
\[
Y_1=(X_1+X_2)/\sqrt2,\quad
Y_2=(X_3+X_4)/\sqrt2,\quad
Y_3=(X_5+X_6)/\sqrt2,
\]
and the orthogonal rotation
\[
L=(Y_1-Y_2)/\sqrt2,\quad
V=(Y_1+Y_2-2Y_3)/\sqrt6,\quad
P=(Y_1+Y_2+Y_3)/\sqrt3
  =(X_1+\cdots+X_6)/\sqrt6.
\]
Each of L,V,P has coefficient-vector norm one and they are pairwise orthogonal. Every original coordinate belongs to one pair Y_j with coefficient 1/sqrt2, so its three-dimensional squared row leverage is (1/2)||e_j||^2=1/2.

Choose any integer B>N. For i=1,...,6, let X_i have density exactly the indicator of
\[
E_i=\bigcup_{k=0}^{N-1}\left[B^{i-1}k,\ B^{i-1}k+\frac1N\right].
\]
These N intervals are disjoint and their total length is one, so these are admissible independent cap-one probability laws. Let K_i be the chosen interval index. Each six-tuple K=(K_1,...,K_6) has probability N^{-6}. Since B>N, the integers
\[
S(K)=\sum_{i=1}^6 B^{i-1}K_i
\]
are distinct for distinct tuples. Conditional on K, P lies in
\[
\left[S(K)/\sqrt6,\ (S(K)+6/N)/\sqrt6\right].
\]
For N>=7 these P intervals are disjoint. Hence the value of P identifies K almost surely.

Fix a p with marginal density g_P(p)>0. Conditional on P=p, the tuple K is now fixed; all six X_i lie in intervals of width 1/N. The coefficient vectors of L and V each have norm one, so the sum of absolute coefficients of either is at most sqrt6. Relative to tuple-dependent constants l_K,v_K,
\[
|L-l_K|\le\sqrt6/N,\qquad |V-v_K|\le\sqrt6/N
\]
almost surely under this conditional law. If |\eta|,|\xi|<=N/(16 sqrt6), its phase differs from exp(i(\eta l_K+\xi v_K)) by at most
\[
|\eta|\,\sqrt6/N+|\xi|\,\sqrt6/N\le1/8.
\]
The elementary bound |e^{it}-1|<=|t| therefore yields
\[
|F_p(\eta,\xi)|\ge(7/8)g_P(p).
\]
The indicated frequency square has area N^2/384. Integrate this lower bound over that square and over p, using \int g_P=1, to obtain (1).

## Relation to the near-coloop leakage proof attempt

For Q=2HL+V^2+2 epsilon LP with an independent cap-one original hub H, a Fresnel transform in V and conditioning on P=p can turn epsilon P into a translation of the hub integration variable. Taking absolute values at that stage would require a uniform upper bound on the mixed norm in (1). The construction proves that this sufficient estimate is false for arbitrary fragmented cap-one leaf laws even in a perfectly diffuse orthonormal three-frame.

The counterexample concerns the ABSOLUTE-VALUED CONDITIONAL FOURIER-SLICE NORM, not the output density of Q. Oscillatory cancellation across frequency, conditional slabs, and the common original hub has been discarded in (1). It is not an admissible counterexample to the full s_3(A)>=1 density conjecture. Any valid epsilon-stability argument must retain some of that cancellation or use a different product-preserving estimate.
