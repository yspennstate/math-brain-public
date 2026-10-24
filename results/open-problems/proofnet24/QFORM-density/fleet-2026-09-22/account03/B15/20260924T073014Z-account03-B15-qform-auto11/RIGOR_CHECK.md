# Rigor check — Fourier-tail regularity compiler

Run: `20260924T073014Z-account03-B15-qform-auto11`.

Status: exact algebra checked; no numerical experiment is used as proof.

## A. beta=2 split

Let `a=sqrt(K)`, `h>0`.

For `ha<=2`,

`J=int_0^infinity min(2,ht)min(1,Kt^-2)dt`

splits as

- `[0,a]`: `h a^2/2`;
- `[a,2/h]`: `hK log(2/(ha))`;
- `[2/h,infinity)`: `hK`.

Thus

`J=hK[3/2+log(2/(ha))]`.

For `ha>=2`,

- `[0,2/h]`: `2/h`;
- `[2/h,a]`: `2a-4/h`;
- `[a,infinity)`: `2a`.

Thus

`J=4a-2/h`.

At `ha=2`, both formulas give `3a`. Since the Fourier inversion modulus has the prefactor `1/pi`, REPORT equations (3.3)-(3.4) are correct.

The height integral is

`(2pi)^-1 * 2[int_0^a 1 dt + int_a^infinity Kt^-2 dt]`
`=(2pi)^-1*4a=2a/pi`.

## B. beta=3/2 split

Now `a=K^(2/3)` and `u=ha<=2`. The same decomposition gives

`J = h a^2/2 + hK * 2[(2/h)^(1/2)-a^(1/2)] + 4K(2/h)^(-1/2)`.

Using `K=a^(3/2)` and `u=ha`, this simplifies exactly to

`J=a[4sqrt(2)sqrt(u)-(3/2)u]`.

Therefore

`J<=4sqrt(2) K sqrt(h)`.

For `u>=2`, the height bound is `||p||inf<=3a/pi`, so

`||tau_h p-p||inf<=6a/pi`.

At `u=2`, the global Hölder right side is

`(4sqrt(2)/pi)K sqrt(2/a)=8a/pi>=6a/pi`.

Hence the global Hölder estimate in REPORT (4.2) is valid for every `h`.

The height integral is

`(2pi)^-1 * 2[a + K * 2 a^-1/2]`
`=3a/pi`.

## C. four-latent substitution

For `Delta=|det H|`, account03/B19 r52 supplies

`K=16pi^2 Delta^-1/2`.

Thus

`sqrt(K)=4pi Delta^-1/4`,

`2sqrt(K)/pi=8Delta^-1/4`.

The small-shift threshold `h sqrt(K)<=2` is

`h<=Delta^(1/4)/(2pi)`.

Also

`K h/pi=16pi h Delta^-1/2`,

and

`2/(h sqrt(K))=Delta^(1/4)/(2pi h)`.

This gives REPORT (5.3). The large-shift formula gives

`pi^-1(4sqrt(K)-2/h)=16Delta^-1/4-2/(pi h)`,

which is REPORT (5.4).

At the gate `Delta>=2^-40`, `Delta^-1/2<=2^20` and `Delta^(1/4)>=2^-10`, so the displayed gated modulus is valid for `h<=2^-10/(2pi)`.

## D. rank-three Theorem-F substitution

The source theorem gives

`K=(4pi)^(3/2) R^-1/2`.

Then

`K^(2/3)=4pi R^-1/3`,

so the height compiler gives

`3/pi * K^(2/3)=12R^-1/3`.

The Hölder coefficient is

`(4sqrt(2)/pi)K`
`=(4sqrt(2)/pi)(4pi)^(3/2)R^-1/2`
`=32sqrt(2pi)R^-1/2`.

Hence REPORT (6.2) is exact.

## E. Scope checks

- No rotation of random coordinates is used in the new proof; only the scalar output characteristic function is analyzed.
- No claim of law-uniform `t^-beta` decay is introduced. The compiler is conditional on a separately proved joint Fourier bound.
- No moment or support estimate is used.
- The account03/B19 receiver permits arbitrary outside blocks and affine terms exactly as cited.
- The account04/B15 partner theorem is applied only after an actual interval-height estimate is available and only in the rank-at-least-three owner-target scope.
- The global conjecture remains open.

## F. Publication/privacy check

Changed-file allowlist for this run is restricted to this worker-owned immutable directory in `math-open-problems` plus the prescribed account03/B15 handoff/memory/status paths in `math-research-brain`. No credentials, tokens, personal archives, scheduler IDs, machine paths, financial/company/client material, or public-release action is present. A repository-native secret-scanner command is not exposed through the available connector, so this is a narrow manual content review rather than a claim of a full repository scan.
