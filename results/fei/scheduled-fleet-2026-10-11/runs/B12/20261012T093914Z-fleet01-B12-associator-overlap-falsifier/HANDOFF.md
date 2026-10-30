# Handoff — associator versus overlap refund

For every `n`, with `N=2^n`, take a coordinate character `chi`, a point
`y` with `chi(y)=-1`, and

`g_-=chi`, `g_+=chi+2 1_y`, `h=-chi`.

The full-block source is `b=1_y`.  There is one selector channel and

`Omega_N = Phi(1-2/N)+(N-1)Phi(2/N)-Phi(1-1/N)-(2N-1)Phi(1/N)`.

Exact/asymptotic values:

- selector alpha-log envelope: `0`;
- collision refund `2 Overlap=1/N`;
- `N Omega_N=4 ln N+2-8 ln2+O(ln N/N)`;
- source influence `I(b)=n/(2N)`;
- `Omega_N/I(b) -> 8 ln2`.

Therefore no universal coefficient pays the signed associator from overlap
plus the selector alpha-log envelope.  Source influence has exactly the
right scale.  Use this family as a mandatory control for the next terminal-
reserve inequality.  Route to A058/A059, A085/A091/A090, A094/A097 and B20.
This is not an FEI counterexample.

