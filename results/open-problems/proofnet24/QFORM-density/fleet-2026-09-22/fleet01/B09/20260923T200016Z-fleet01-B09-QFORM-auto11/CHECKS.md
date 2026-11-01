# Deterministic checks — fleet01/B09 20260923T200016Z

These checks support `QFORM-RESIDUAL-STABLE-CARRIER-CROSSING-v1` and `QFORM-TOP3-BALANCE-WEAK-FOURTH-v1`. They are not substitutes for the proof in `REPORT.md`.

## 1. Rademacher balance identity

For an n x r orthonormal frame U with rows u_i^T and q=max_i ||u_i||^2,

F=(1/2) sum_i eps_i u_i u_i^T

has

E ||F||_F^2
=(1/4) sum_i ||u_i u_i^T||_F^2
=(1/4) sum_i ||u_i||^4
<=rq/4.

Thus some sign choice has ||F||op<=sqrt(rq)/2 and gives

G_I,G_J >= (1-sqrt(rq))/2 I_r.

## 2. Cross-block stability

For B_0=U_I K U_J^T, restricted-frame factorization gives

s_3(B_0)>=gamma s_3(K).

For any symmetric residual E,

||E[I,J]||op<=||E||op,

so Weyl gives

s_3(B_0+E[I,J])>=gamma s_3(K)-||E||op.

Since e_3(BB^T)>=s_3(B)^6, the physical-D3 no-marginal theorem yields the claimed coefficient C_3/beta.

## 3. Constants

C_3=3*2^(4/3)*exp(1/3)=10.550168831164775.

For r<=4, q<=1/16 gives gamma>=1/4.
If the retained residual satisfies epsilon<=(1-tau)/10 and s_3(S)>=1-tau-epsilon, then

gamma s_3(S)-epsilon
>= (1/4)(9/10)(1-tau)-(1/10)(1-tau)
= (1/8)(1-tau).

Hence

8 C_3=84.4013506493182 <84.402.

For the exact E=0 branch, 4 C_3=42.2006753246591 <42.201.

## 4. High-full-leverage Walsh regression

Take N=64 and three normalized Walsh columns W. Then every row has q_3=3/64 and

gamma_3=(1-sqrt(9/64))/2=5/16.

Define

z=(e_1-WW^T e_1)/sqrt(1-3/64).

Then z is unit and W^T z=0. Because (WW^T)_{11}=3/64,

z_1^2=1-3/64,

so the four-column frame [W,z] has physical row-1 leverage

3/64+(1-3/64)=1.

For

A_epsilon=W diag(1,1,-1)W^T+epsilon zz^T,

spec_nonzero(A_epsilon)={1,1,-1,epsilon}.
For 0<=epsilon<=1/4, the weak rank-one cross tail obeys

||epsilon z_I z_J^T||op<=epsilon/2<=1/8,

hence

s_3(A[I,J])>=5/16-1/8=3/16.

Therefore

(C_3)/(3/16)=(16/3)C_3=56.26756709954547 <56.268.

## 5. Designated partner r19 application

Take N=4096, U the first four normalized Walsh columns, and K=diag(1,1,-1,1/4). Then every row of U has squared norm 4/N=1/1024.

In fleet02/B09 r19, choose eta=1/2. The localization alternative permits at most 64 eta^(-2)=256 physical coordinates. For every unit coefficient u and every such set H,

||(Uu)_H||^2 <=256*(1/1024)=1/4,

so its required mass >1/2 is impossible. The paid alternative therefore applies with gamma=s_3(K)=1:

24 sqrt(2e)/sqrt((1/2)(3/2))
=48 sqrt(2e/3)
=64.61641346061458 <64.617.

The physical spectrum is exactly {1,1,-1,1/4}, so this is a target-valid use of the partner theorem.