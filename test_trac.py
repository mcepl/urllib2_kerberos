#!/usr/bin/python
import urllib2
import cookielib
import urllib2_kerberos


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPSHandler(debuglevel=2),
                              urllib2.HTTPRedirectHandler,
                              urllib2.HTTPCookieProcessor(cj),
                              urllib2_kerberos.HTTPKerberosAuthHandler)

response = opener.open(
    'https://trac.dqe.lab.eng.bos.redhat.com/desktopqe-backlog/login')
