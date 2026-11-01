"""Core Lean checks the finite P0242 ratio certificate only."""
import os, runpy, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
folder=ROOT/'lean_receipts'
folder.mkdir(exist_ok=True)
os.environ['LEAN_CHECK_DIR']=str(folder)
os.environ['TEMP']=str(folder)
os.environ['TMP']=str(folder)
sys.path.insert(0,'~/.claude/dreaming')
stmt='theorem p0242_ratio_gt_149_percent : 100 * 24076090051009 > 149 * 16078132074513 := by decide\n\ntheorem p0242_ratio_lt_three_halves : 2 * 24076090051009 < 3 * 16078132074513 := by decide'
(ROOT/'P0242_arithmetic.lean').write_text(stmt+'\n',encoding='utf-8')
sys.argv=['lean_check.py','--core','--stmt',stmt,'--target','p0242_ratio_gt_149_percent','--timeout','60','--json']
runpy.run_path('~/.claude/dreaming/lean_check.py',run_name='__main__')
