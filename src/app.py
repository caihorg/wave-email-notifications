#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from notifiy.home import Home
from notifiy.proc import Process
from notifiy.proc_phone import PhoneProcess
from notifiy.receive_email import ReceiveEmail


if __name__ == "__main__":
    run_wsgi_app(webapp.WSGIApplication([ ('/', Home),
                                          ('/proc/.*', Process),
                                          ('/phone/.*', PhoneProcess),
                                          ('/_ah/mail/.+', ReceiveEmail) ]))
