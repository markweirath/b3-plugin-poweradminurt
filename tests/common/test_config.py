# -*- encoding: utf-8 -*-
import logging
from mockito import when
from b3.cvar import Cvar

from poweradminurt import PoweradminurtPlugin, __file__ as poweradminurt_file
from b3.config import CfgConfigParser

from tests.iourt41 import Iourt41TestCase
from tests.iourt42 import Iourt42TestCase

class mixin_conf(object):

    def setUp(self):
        super(mixin_conf, self).setUp()
        self.conf = CfgConfigParser()
        self.p = PoweradminurtPlugin(self.console, self.conf)

        # when starting the PoweradminurtPlugin expects the game server to provide a few cvar values
        when(self.console).getCvar('timelimit').thenReturn(Cvar('timelimit', value=20))
        when(self.console).getCvar('g_maxGameClients').thenReturn(Cvar('g_maxGameClients', value=16))
        when(self.console).getCvar('sv_maxclients').thenReturn(Cvar('sv_maxclients', value=16))
        when(self.console).getCvar('sv_privateClients').thenReturn(Cvar('sv_privateClients', value=0))
        when(self.console).getCvar('g_allowvote').thenReturn(Cvar('g_allowvote', value=0))

        logger = logging.getLogger('output')
        logger.setLevel(logging.INFO)



    def test_empty_config(self):
        self.conf.loadFromString("""
[foo]
        """)
        self.p.onLoadConfig()
        # should not raise any error


    ####################################### matchmode #######################################

    def test_matchmode__plugins_disable(self):
        # empty
        self.conf.loadFromString("""
[matchmode]
plugins_disable:
        """)
        self.p.LoadMatchMode()
        self.assertEqual([], self.p.match_plugin_disable)

        # one element
        self.conf.loadFromString("""
[matchmode]
plugins_disable: foo
        """)
        self.p.LoadMatchMode()
        self.assertEqual(['foo'], self.p.match_plugin_disable)

        # many
        self.conf.loadFromString("""
[matchmode]
plugins_disable: foo, bar
        """)
        self.p.LoadMatchMode()
        self.assertEqual(['foo', 'bar'], self.p.match_plugin_disable)






##############################################################################
class Test_41(mixin_conf, Iourt41TestCase):
    """
    call the mixin tests using the Iourt41TestCase parent class
    """

class Test_42(mixin_conf, Iourt42TestCase):
    """
    call the mixin tests using the Iourt42TestCase parent class
    """
