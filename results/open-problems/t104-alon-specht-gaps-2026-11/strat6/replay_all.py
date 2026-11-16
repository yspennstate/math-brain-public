"""PROVED: replay every certificate used in RESULT.md; no solver required."""
import os
import subprocess
import sys

for key in('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
scripts=['verify_polya_moments.py','verify_new_bounds.py','verify_directional_bounds.py',
         'verify_equal_gap.py','zero_face.py','verify_all_cells.py',
         'verify_rational_witnesses.py','verify_face_boxes.py','verify_equal_gap_rotation.py']
for script in scripts:
    print('PROVED: replaying',script,flush=True)
    subprocess.run([sys.executable,script],check=True)
print('PROVED: all final certificate replays passed.',flush=True)
