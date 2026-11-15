"""Sequential suite, one compute thread. Launch alongside at most one other job."""
import study
import sys

if sys.argv[1]=='blocks':
    for L in (8,12,16,24):
        for r in (1,2):
            study.block_run(L,r,16,1024,L*1000+r)
elif sys.argv[1]=='windows':
    for L in (12,16,24):
        study.window_run(L,32,65536,L*1000+7,'original')
