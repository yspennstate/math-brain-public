# G0008 coordinate clarification for the critical seven-edge event

This note clarifies coordinates in `2026-09-18T040900Z__G0008_spectral_puncture_critical_certificate.md`; it does not change any formula or bound.

The opening/closing cylinder event used to prove `delta >= 2^{-7}` is written in coordinates **after translating the punctured vertex `y` to the origin**.  In that translated frame,

- `y=(0,0)`,
- `x=(-1,0)`,
- `u=(0,1)`,
- `z=(1,0)`,
- `d=(0,-1)`.

Open

`x--(-1,1)--u--(1,1)--z`

(the four consecutive square-lattice edges on that displayed path), and close the three remaining edges of the punctured graph `K` incident to `d`, namely

`d--(-1,-1)`, `d--(1,-1)`, `d--(0,-2)`.

These seven prescribed edge states are independent at `p=1/2`, have probability `2^{-7}`, connect `x,u,z`, and isolate `d`; hence they force the specified triple-plus-singleton orbit and prove `delta >= 2^{-7}` exactly.

In the untranslated frame of the main target one has `x=0`, `y=e_1`, `z=2e_1`; translating by `-e_1` gives the frame above.  Translation invariance makes the two descriptions identical mathematically.
