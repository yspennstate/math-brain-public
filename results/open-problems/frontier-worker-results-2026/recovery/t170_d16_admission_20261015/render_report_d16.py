from pathlib import Path
from datetime import datetime
import json,hashlib
from playwright.sync_api import sync_playwright
H=Path(__file__).resolve().parent
report=Path('~/Downloads/frontier_layer_report_2026-10-15.html')
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True,args=['--disable-gpu'])
 try:
  page=browser.new_page(viewport={'width':1600,'height':1000})
  page.goto(report.as_uri(),wait_until='load')
  row=page.locator('#recovery-t170-d16');assert row.count()==1
  text=row.inner_text();assert all(x in text for x in ['1019722296067/12094627905536','10649701413/125000000000','distinct actual accounts'])
  row.scroll_into_view_if_needed();row.screenshot(path=str(H/'report_review_d16.png'))
  widths=page.evaluate('({scroll:document.documentElement.scrollWidth,viewport:innerWidth})');assert widths['scroll']<=widths['viewport']
  out={'at':datetime.now().astimezone().isoformat(),'report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),'text':text,'widths':widths,'status':'Rendered; visual review pending'}
  (H/'T170_D16_REPORT_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode())
  print(json.dumps(out))
 finally:browser.close()
