from pathlib import Path
for fn,words,context in [('kenyon.txt',['Height mod','[24]','reference flow'],12),('dubedat.txt',['Theorem','Corollary','electric correlator','small enough','small charges','sufficiently small'],5)]:
 lines=Path(fn).read_text(encoding='utf8').splitlines(); inds=set()
 for i,l in enumerate(lines):
  if any(w.lower() in l.lower() for w in words):inds.update(range(max(0,i-context),min(len(lines),i+context+1)))
 print('\nFILE',fn)
 for i in sorted(inds):print(f'{i+1}: {lines[i]}')
