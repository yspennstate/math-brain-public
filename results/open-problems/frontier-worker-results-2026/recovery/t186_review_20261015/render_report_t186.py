from pathlib import Path
from datetime import datetime
import json
from playwright.sync_api import sync_playwright
HERE=Path(__file__).resolve().parent
report=Path('~/Downloads/frontier_layer_report_2026-10-15.html')
with sync_playwright() as p:
    browser=p.chromium.launch(channel='chrome',headless=True,args=['--disable-gpu'])
    try:
        page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
        page.goto(report.as_uri(),wait_until='load')
        rows=[]
        for side,values in [('upper',['11.415','9.053']),('lower',['9.23414','6.84256'])]:
            row=page.locator('#recovery-t186-'+side)
            assert row.count()==1
            assert all(v in row.inner_text() for v in values)
            row.scroll_into_view_if_needed()
            shot='report_review_t186_'+side+'.png'
            row.screenshot(path=str(HERE/shot))
            rows.append({'side':side,'text':row.inner_text(),'screenshot':shot})
        widths=page.evaluate('({scroll:document.documentElement.scrollWidth,viewport:innerWidth})')
        assert widths['scroll']<=widths['viewport'],widths
        out={'at':datetime.now().astimezone().isoformat(),'rows':rows,
            'widths':widths,'report':str(report),'screenshot':'report_review_t186_lower.png',
            'status':'Chrome render complete; screenshot requires visual review'}
        (HERE/'T186_REPORT_RENDER_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
        print(json.dumps({'at':out['at'],'widths':widths,'screenshots':[r['screenshot'] for r in rows]}))
    finally:browser.close()
