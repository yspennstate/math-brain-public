SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T07:32:05Z.
attacking: the near-null scalar/dependent-pair stability splice by keeping the original independent scalar and proving a weak-L2 definite-Schur kernel bound.

# Substantive checkpoint — scalar + dependent pair, definite Schur side

Status: WORKED PARTIAL DERIVATION / FULL QFORM OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

Start from one genuinely independent original scalar X with density f<=1 and an independent pair Y=(C,D) whose joint density g is allowed to be dependent internally but satisfies ||g||_infinity<=M. Consider

Q = a X^2 + 2 beta X C + alpha C^2 + 2 delta C D + gamma D^2,

with beta*gamma != 0. Let

B = [[a,beta,0],[beta,alpha,delta],[0,delta,gamma]],
h = alpha-delta^2/gamma,
S = [[a,beta],[beta,h]].

The first calculation is the exact root-coordinate reduction. For fixed (c,d), write u=a x+beta c. If the conditional density kernel K_t(c,d) exceeds s, then one of the at-most-two x-roots contributes >s/2, hence |u|<f(x)/s. Completing the d-square and changing c=(u-a x)/beta gives

|{(c,d):K_t(c,d)>s}|
 <= 2/(|beta| sqrt(|gamma|))
    int int_{|u|<f(x)/s} |u| / sqrt(|t-P(x,u)|) du dx,

where

P(x,u) = q0(x,(u-a x)/beta),
q0(x,c)=a x^2+2 beta x c+h c^2,

det(matrix(P)) = det(S)/beta^2 = det(B)/(beta^2 gamma).

Thus if S is definite, P is a definite nondegenerate quadratic form. Its shell kernel is uniformly weak-L2:

|{(x,u): |t-P(x,u)|^(-1/2)>lambda}|
 <= 2 pi |det(P)|^(-1/2) lambda^(-2),

uniformly in t.

For w_s(x,u)=|u| 1_{|u|<f(x)/s}, rearrangement gives

int w_s |t-P|^(-1/2)
 <= sqrt(2 pi)|det(P)|^(-1/4)
    int_0^infinity w_s^*(r) r^(-1/2) dr.

Moreover

|{w_s>tau}| = int 2(f(x)/s-tau)_+ dx <= 2/s

for 0<tau<1/s, because int f=1. Hence

int_0^infinity w_s^*(r) r^(-1/2) dr
 = 2 int_0^infinity |{w_s>tau}|^(1/2) d tau
 <= 2 sqrt(2) s^(-3/2).

Therefore the conditional-kernel superlevel set obeys the explicit bound

|{K_t>s}|
 <= 8 sqrt(pi) |beta|^(-1/2)|gamma|^(-1/4)|det B|^(-1/4) s^(-3/2).

Layer cake against g<=M and int g=1 then gives the candidate theorem

||p_Q||_infinity
 <= 3 (8 sqrt(pi) M)^(2/3)
    |beta|^(-1/3)|gamma|^(-1/6)|det B|^(-1/6).

The remaining work before declaring this proved is to write the area-formula/root multiplicity step carefully at critical roots and check that the conditional density representation is valid by approximation. The singular roots form a null set for each regularized law; the intended final proof will use truncation/regularization and Fatou so no pointwise conditional-density assumption is hidden.

This mechanism is deliberately different from the refuted generic interpolation of a sqrt(epsilon) small-ball bound with an L3 density bound. It attacks the scalar/dependent-pair geometry directly and keeps the one original scalar independent of the whole dependent projected pair.