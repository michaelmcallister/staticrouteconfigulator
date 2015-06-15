#!/usr/bin/python2

import yaml
from jnpr.junos.factory.factory_loader import FactoryLoader
from jnpr.junos import Device


class route:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        route.device = Device(host=self.host, user=self.user,password=self.password)

    def show(self):
        route.device.open()

        yml = '''
---
staticRouteTable:
 rpc: get-route-information
 args:
  protocol: static
 item: route-table/rt
 key: rt-destination
 view: staticView

staticView:
 fields:
  destination: rt-destination
  via: rt-entry/nh/via
  next-hop:  rt-entry/nh/to
'''
        globals().update(FactoryLoader().load(yaml.load(yml)))
        RouteView = staticRouteTable(route.device)
        RouteView.get()
        return RouteView.values()
        route.device.close()
