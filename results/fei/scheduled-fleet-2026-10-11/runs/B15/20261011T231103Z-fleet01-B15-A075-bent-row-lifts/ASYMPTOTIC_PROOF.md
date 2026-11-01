# Asymptotic and scope proof

For the A071 seed define

\[
L=5k_0+k_1+k_2+k_3.
\]

The row-wise lift theorem gives the exact identities

\[
H_L=5+L/4,
\qquad
I_L=(17+L)/8,
\qquad
R_L=H_L/I_L=(40+2L)/(17+L).
\]

There is no remainder term. Direct subtraction gives

\[
\frac{40}{17}-R_L
=\frac{6L}{17(17+L)}.
\]

Thus the inequality is strict for every nontrivial lift, and

\[
R_L=2+\frac6{17+L}\longrightarrow2.
\]

For the diagonal choice `k_0=k_1=k_2=k_3=k`, one has `L=8k` and

\[
H=5+2k,\qquad I=17/8+k,
\qquad H/I=2+\frac6{17+8k}.
\]

This is an actual Boolean family in every even added dimension. Each
conditional row has product squared spectrum. The nonzero physical support of
each row grows by `2^(2K)`, but its normalized row mass is unchanged.

## Exact scope

- The result proves that arbitrary row-wise quadratic-bent tensor lifts of
  the A071 seed cannot improve `40/17`.
- It does not classify every partial sign with product squared spectrum.
- It does not prove a finite constant for all two-address functions (C022).
- It does not establish full FEI.
- It does not invoke overlapping-product entropy subadditivity: the Fourier
  factorization is proved separately inside each orthogonal address row.
- Address labels retain their original Fourier degree and are charged exactly
  once. The additional entropy/influence ratio is exactly two.
- Activation probabilities are unchanged, so the construction neither hides
  nor resolves a rare-event logarithm.

The bridge is therefore a rigorous infinite-family no-go for one natural
extension of the finite maximizer, not an extrapolation from finite data.
