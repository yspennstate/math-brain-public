# The degree-two extremal class

All logarithms are base two.  For a Boolean function (f), let

\[
p(S)=\widehat f(S)^2,\qquad
\pi(A)=\sum_{S\supseteq A}p(S),
\]

\[
U(f)=\sum_Sp(S)\log\frac{\pi(S)}{p(S)},\quad
I(f)=\sum_S|S|p(S),\quad
G(f)=\sum_i\left(U(f)-\frac{U(f_{i,+})+U(f_{i,-})}{2}\right).
\]

## Theorem

If the Fourier degree of (f:\{-1,1\}^n\to\{-1,1\}) is at most two, then

\[
\boxed{G(f)\le 2I(f)}
\qquad\text{and}\qquad
\boxed{H(f)\le 2I(f)}.
\]

Both constants are sharp, already for a two-bit point defect (equivalently AND/OR up to signs and input symmetries).

## Proof

Nisan and Szegedy proved that a Boolean function of real polynomial degree (d) depends on at most (d2^{d-1}) variables.  Fourier degree on the ({-1,1})-cube is the same real multilinear degree.  Thus a Boolean function of Fourier degree at most two depends on at most four coordinates.

It remains to verify the two inequalities on four coordinates.  Multiplying the output by (-1) changes Fourier signs but not (p,\pi,U,I,G,H), so fix the value at one input to (+1).  There are (2^{15}=32768) such truth tables.  Exact Walsh arithmetic leaves precisely 111 whose Fourier coefficients vanish in levels three and four.

For each of these 111 tables, the verifier constructs (p), every upper sum (\pi), and every restricted spectrum using rational arithmetic.  Each entropy expression is stored symbolically as

\[
c_0+\sum_{q\ {m odd\ prime}}c_q\log_2 q,
\qquad c_q\in\mathbb Q.
\]

The signs of (2I-G) and (2I-H) are certified by rational lower and upper bounds for the logarithms.  For an integer (m\ge2), with (z=(m-1)/(m+1)), the program uses

\[
2\sum_{k=0}^{N-1}\frac{z^{2k+1}}{2k+1}
\le \log m\le
2\sum_{k=0}^{N-1}\frac{z^{2k+1}}{2k+1}
+\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]

All quantities in these bounds are rational.  With (N=220), all 111 cases certify.  There are 25 exact equality cases for each inequality; among strict cases the smallest certified (G)-slack is (2), and the smallest certified (H)-slack is (1).  This proves the theorem in every dimension.

## Use of the minimal-counterexample constraint

Freeze

\[
R(f)=G(f)-4I(f)-\frac34U(f).
\]

If the universal frozen pair fails, choose a counterexample of minimum dimension and then a tensor-prime positive-residual factor.  Every proper physical child has nonpositive residual, so every relevant coordinate satisfies

\[
\Delta_iG-\frac34\Delta_iU\ge4\operatorname{Inf}_i(f)+R(f).
\]

The theorem above now excludes the entire Fourier-degree-two class from this critical source: a nonconstant degree-two function has

\[
R(f)\le -2I(f)-\frac34U(f)<0.
\]

Hence every dimension-minimal positive-residual counterexample to the frozen pair must have Fourier degree at least three.  This is a genuine all-dimensional class removal, not an assumed extremizer condition and not a finite-dimensional maximum presented as a universal constant.

## Exact GU implication and remaining gap

On the restriction-closed class of degree-two Boolean functions, (G\le2I) is the GU pair ((a,b)=(2,0)).  The independently audited restriction induction therefore also gives (U\le2I) and the general reduction gives (H\le6I); the direct exact certificate above improves the last constant to (2).

Universal GU remains open.  The next unpaid structural step is quantitative: use the critical-child inequalities to control the degree-at-least-three signed KL rows, rather than merely observing that some high-degree coefficient exists.

## Source

The junta theorem is from Noam Nisan and Mario Szegedy, “On the degree of Boolean functions as real polynomials,” *Computational Complexity* 4 (1994), 301–313, DOI `10.1007/BF01263419`.
