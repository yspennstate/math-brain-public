# Search budget and measured execution

## Frozen pre-search size

- Four-cube edges: 32.
- Three pairwise-disjoint edge matchings: 2,496.
- Distinct six-vertex unions: 1,984.
- Complement sign laws modulo global negation: `2^9=512` per union.
- Total representatives: `1,984*512=1,015,808`.

The calculation does not scale to five physical bits by replacing `4` with
`5`: all Boolean truth tables would number `2^(2^5)`, and the present
structural reduction would also change.  Any enlargement requires a newly
proved symmetry/domain argument.

## Hard caps

| resource | cap |
|---|---:|
| representatives | 1,100,000 |
| wall time | 60 seconds |
| peak resident memory | 128 MiB |
| random trials | 0 |

## Observed clean rerun

| measurement | value |
|---|---:|
| representatives | 1,015,808 |
| elapsed wall time | 14.165475 seconds |
| peak RSS | 11,264 KiB |
| average rate | approximately 71,700 representatives/second |
| exit status | 0 |
| byte comparison with archived output | identical |

The output contained no interval-ambiguous comparison.  Precision was not
increased after every sign had been certified.
