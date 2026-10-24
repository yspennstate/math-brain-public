import unordered as u
import audit as a
import exact as e
from functools import lru_cache
import json,sys
# Memoization only: cached objects are immutable tuples or are read without mutation.
# Every policy's tree telescope, actual leaf and influence check still executes.
original_interval=e.interval
@lru_cache(maxsize=8192)
def interval_tuple(items):return original_interval(dict(items))
def cached_interval(d):return interval_tuple(tuple(sorted(d.items())))
e.interval=cached_interval;a.interval=cached_interval
a.table=lru_cache(maxsize=4096)(a.table)
a.pots=lru_cache(maxsize=4096)(a.pots)
a.local=lru_cache(maxsize=4096)(u.local)
if __name__=='__main__':
    pilot='--pilot' in sys.argv;old=(u.R/'out/UNORDERED_PILOT.json').read_text() if pilot else None
    u.main()
    name='UNORDERED_PILOT.json' if pilot else f'UNORDERED_{sys.argv[sys.argv.index("--start")+1]}_{sys.argv[sys.argv.index("--end")+1]}.json'
    p=u.R/'out'/name;v=json.loads(p.read_text());v['helper_version']='unordered_cached.py v2; exact v1 computations memoized'
    v['cache_info']={k:getattr(a,k).cache_info()._asdict() for k in ['table','pots','local']}
    dest=u.R/'out/UNORDERED_CACHED_PILOT.json' if pilot else p
    dest.write_text(json.dumps(v,indent=2)+'\n')
    if pilot:p.write_text(old)
