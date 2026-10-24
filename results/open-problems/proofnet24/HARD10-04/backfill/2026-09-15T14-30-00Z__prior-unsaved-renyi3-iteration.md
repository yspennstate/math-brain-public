SOLUTION STATUS: PARTIAL

# HARD10-04 backfill — prior unsaved Rényi-3 / intermittency iteration

Recovery timestamp: 2026-09-15T14:30:00Z
Original authored-run provenance: earlier scheduled HARD10-04 task response on 2026-09-15, after the verified 2026-09-14 capacity-drift checkpoint. The earlier GitHub write attempt did not return a commit receipt, and bounded repository search at the start of the present run found no newer HARD10-04 research report. This file therefore archives genuine prior authored mathematics that was accessible in task history but not verifiably saved. It does not claim that the earlier attempted write succeeded.

Verified predecessor:
`proofnet24/HARD10-04/runs/2026-09-14/2026-09-14T13-30-26Z__report.md`
commit `9e8325a24e5b5793804680abf4c6248858c45d9a`.

## Target

For standard external site DLA on Z^2, prove that log R_n/log n converges almost surely to a deterministic exponent beta and identify beta, or rigorously refute existence/determinism. This backfilled iteration was PARTIAL and did not claim closure.

## Recovered theorem 1: capacity martingale convergence

Let C_n=Cap(overline A_n). If X_{n+1} is selected from harmonic measure p_n on the exterior boundary, define

Delta_{n+1}=C_{n+1}-C_n,

a_n=E[Delta_{n+1}|F_n],

xi_{n+1}=Delta_{n+1}-a_n,

M_n=sum_{k<n} xi_{k+1}.

Losev–Smirnov Lemma 5 gives deterministic constants 0<c0<C0<infinity with

c0 p_n(x)^2 <= d_n(x) <= C0 p_n(x)^2,

where d_n(x) is the capacity increment if x is attached. Hence, writing S_q(n)=sum_x p_n(x)^q,

c0 S_3(n) <= a_n <= C0 S_3(n).

Also

E[Delta_{n+1}^2|F_n] <= C S_5(n) <= C (p_n^*)^2 S_3(n) <= C (p_n^*)^2 a_n.

Discrete Beurling gives p_n^* <= C R_n^{-1/2}. The planar capacity-radius comparison

|C_n-(2/pi)log R_n|<=K

therefore yields, with theta=pi/2,

E[Delta_{n+1}^2|F_n] <= C exp(-theta C_n) a_n.

Set Z_n=exp(-theta C_n). Since one-step capacity increments are uniformly bounded, there exists kappa>0 such that

1-exp(-theta u)>=kappa u

throughout the possible increment range. Consequently

E[Z_n-Z_{n+1}|F_n] >= kappa Z_n a_n.

Taking expectations and telescoping gives

E sum_n Z_n a_n < infinity.

Thus

sum_n E xi_{n+1}^2 < infinity,

so M_n converges almost surely and in L^2 to a finite M_infinity. Therefore

C_n=C_1+sum_{k<n}a_k+M_infinity+o(1)

and

log R_n=(pi/2)sum_{k<n}a_k+O(1) almost surely.

This strengthens the verified predecessor's sublogarithmic martingale error to a bounded error.

## Recovered theorem 2: capacity-biased law and exact intermittency identity

For accessible x define

kappa_n(x)=d_n(x)/p_n(x)^2,

so c0<=kappa_n(x)<=C0 and

a_n=sum_x kappa_n(x)p_n(x)^3.

Define the capacity-biased boundary law

r_n(x)=p_n(x)d_n(x)/a_n=kappa_n(x)p_n(x)^3/a_n.

Let

H_n=-sum_x p_n(x) log p_n(x),

I_n=D_KL(p_n||r_n),

mu_n=sum_x p_n(x) log kappa_n(x).

Then exactly

log a_n=-2H_n+mu_n+I_n.

Proof: log(p_n/r_n)=log a_n-log d_n, average under p_n, and use d_n=kappa_n p_n^2.

Equivalently,

I_n=log E[Delta_{n+1}|F_n]-E[log Delta_{n+1}|F_n].

Thus I_n is exactly the logarithmic arithmetic/geometric mean gap of the one-step capacity increment.

## Recovered theorem 3: Shannon–Rényi-3 gap

Define the order-3 Rényi entropy

H_{3,n}=-(1/2)log S_3(n).

Because a_n/S_3(n) and kappa_n(x) are uniformly bounded above and below,

| I_n - 2(H_n-H_{3,n}) | <= log(C0/c0).

Losev–Smirnov's quoted discrete Makarov entropy estimate gives

H_n=log R_n+O(log log R_n).

Therefore

log a_n=-2 log R_n + I_n + O(log log R_n),

and

-
log S_3(n)/log R_n
=
2-I_n/log R_n+o(1).

The unresolved power-law information is therefore exactly the normalized Shannon–Rényi-3 gap, equivalently normalized capacity intermittency.

## Recovered theorem 4: third harmonic moment exponent implies radial exponent

Define

tau_{3,n}=-log S_3(n)/log R_n,

underline_tau_3=liminf tau_{3,n},

overline_tau_3=limsup tau_{3,n}.

Let s_n=sum_{k<n} a_k. Since log R_n=(pi/2)s_n+O(1) and a_n is uniformly comparable to S_3(n), one has asymptotically

exp(-(pi/2)(overline_tau_3+epsilon)s_n)
<= a_n <=
exp(-(pi/2)(underline_tau_3-epsilon)s_n).

A deterministic comparison lemma for increasing sequences s_{n+1}-s_n=a_n then yields

1/overline_tau_3
<= liminf log R_n/log n
<= limsup log R_n/log n
<= 1/underline_tau_3.

In particular, if tau_{3,n}->tau_3, then

beta=1/tau_3.

This is a rigorous conditional version of the third-harmonic-moment scaling relation: existence of the order-3 harmonic-measure exponent along the actual lattice DLA path forces existence of the radial growth exponent.

## Recovered corollary: normalized intermittency criterion

Let theta_n=I_n/log R_n. Since

tau_{3,n}=2-theta_n+o(1),

if theta_n->theta then

beta=1/(2-theta).

Kesten's rigorous beta<=2/3 bound would then force theta<=1/2 for any stabilized limit.

## Failed/insufficient routes retained from the authored iteration

- Kesten/Beurling alone gives the 2/3 upper radial exponent but not existence/value.
- Discrete Makarov fixes Shannon entropy but not order-3 Rényi entropy; the missing quantity is precisely their gap.
- Assuming S_3=R^{-tau+o(1)} would solve the exponent but is the missing regularity, not a proof.
- Numerical dimensions and off-lattice/Hastings–Levitov amplitude relations are not exact lattice proofs.
- Direct capacity martingale noise is not the main power-law obstruction after the convergence theorem above.

## Verification status

These derivations were adversarially self-checked in the authored run but were not independently/formally verified. Novelty was not assessed. The full DLA exponent problem remained OPEN.
