# Deterministic checks — fixed-pair Omega2 compiler

These calculations check algebra and constants only; they are not substitutes for the proof in `ADDENDUM_OMEGA2.md`.

## Random symmetric 7x7 regression

With fixed seed 20260923 and physical pair H={0,1}, the pair core was set to

    B=[[0.3,1.0],[1.0,-0.2]].

It is invertible indefinite, with

    |det B| = 1.06,
    sigma_min(B) = 0.9807764064044151.

For the exact Schur complement S on the other five coordinates, direct summation of squared physical overlap-two 3x3 minors gave

    Omega_(2,H) = 9.907855737430939.

The Schur identity gave independently

    |det B|^2 * sum_(i!=j) S_ij^2
      = 9.907855737430940,

agreeing to floating error.

Enumerating all 2^5 literal bipartitions U|V of the residual coordinates gave

    average ||S[U,V]||_F^2 = 2.2044890836220494,

while the exact expectation formula gives

    Omega_(2,H)/(4 |det B|^2)
      = 2.2044890836220490.

The maximum over the 32 literal cuts was

    max ||S[U,V]||_F^2 = 3.593277886095031,

which is above the required expectation lower bound.

## Constant check

Using the inherited physical-pair constant

    K_pair = 11.4625801249,

the new aggregate fixed-pair constant is

    K_2 = 2^(1/10) K_pair
        = 12.28528919006377 < 12.286.

For the exact target regression with two independent 2x2 hyperbolic blocks, D=kappa=1 and Omega_(2,H)=2, so

    K_2 * 2^(-1/20)
      = 11.866807140030287 < 11.867.

The coefficient is homogeneous of degree -1:

    D^(-3/10) kappa^(-1/10) Omega^(-1/20)

has degrees `-6/10`, `-1/10`, and `-3/10`, respectively.
