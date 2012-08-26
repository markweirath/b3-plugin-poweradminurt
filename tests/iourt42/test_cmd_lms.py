# -*- encoding: utf-8 -*-
from mock import  call, Mock
from mockito import when
from b3.config import CfgConfigParser
from b3.cvar import Cvar
from poweradminurt import PoweradminurtPlugin
from tests.iourt42 import Iourt42TestCase

class Test_cmd_lms(Iourt42TestCase):
    def setUp(self):
        super(Test_cmd_lms, self).setUp()
        self.conf = CfgConfigParser()
        self.conf.loadFromString("""
[commands]
palms-lms: 20           ; change game type to Last Man Standing
        """)
        self.p = PoweradminurtPlugin(self.console, self.conf)

        when(self.console).getCvar('timelimit').thenReturn(Cvar('timelimit', value=20))
        when(self.console).getCvar('g_maxGameClients').thenReturn(Cvar('g_maxGameClients', value=16))
        when(self.console).getCvar('sv_maxclients').thenReturn(Cvar('sv_maxclients', value=16))
        when(self.console).getCvar('sv_privateClients').thenReturn(Cvar('sv_privateClients', value=0))
        when(self.console).getCvar('g_allowvote').thenReturn(Cvar('g_allowvote', value=0))
        self.p.onLoadConfig()
        self.p.onStartup()

        self.console.say = Mock()
        self.console.write = Mock()

        self.moderator.connects("2")


    def test_nominal(self):
        self.moderator.message_history = []
        self.moderator.says("!lms")
        self.console.write.assert_has_calls([call('g_gametype 1')])
        self.assertEqual(['game type changed to Last Man Standing'], self.moderator.message_history)


