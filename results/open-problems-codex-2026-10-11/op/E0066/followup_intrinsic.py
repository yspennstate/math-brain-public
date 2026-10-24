from pathlib import Path
p=Path('.')
with p.joinpath('FOLLOWUP.md').open('a',encoding='utf8') as f:f.write('\nThe projection R is intrinsic to B because its range is span{c}+E. Different positive-weight permutation choices from a Birkhoff decomposition agree on this range. Thus the formula can equivalently be written ||V^n(x)-B^n R x|| to zero for interior x; the decomposition is a proof device, not an ambiguity in the predicted limit.\n')
print('Intrinsic projection clarification saved')
