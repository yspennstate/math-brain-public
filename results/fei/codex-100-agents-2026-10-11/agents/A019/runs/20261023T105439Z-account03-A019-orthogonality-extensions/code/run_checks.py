import sys,runpy,gc
from pathlib import Path
script=str(Path(__file__).with_name('check_events.py'))
for flags in ([],['--review'],['--diagnostic']):
 sys.argv=[script]+flags
 runpy.run_path(script,run_name='__main__')
 gc.collect()
