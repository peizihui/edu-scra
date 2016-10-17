#coding=utf-8 
import sys
import json
from tld import get_tld
from urlparse import urlparse
reload(sys) 
sys.setdefaultencoding('utf-8')

f = open("out.json")
out = open("out", "w")
schools = json.load(f)

for school in schools:
    url = school['url']
    tld = get_tld(url, fail_silently=True)
    if not tld:
        tld = urlparse(url).netloc

    if tld == 'baidu.com':
        tld = None

    line = u"{region}/{kind}/{name}|{tld}".format(region=school['region'],
                                                  kind=school['kind'],
                                                  name=school['name'],
                                                  tld=tld)
    out.write(line)
    out.write('\n')
