# -*- encoding: utf-8 -*-
from mock import patch, Mock
import time
from mockito import when, verify
from b3.config import CfgConfigParser
from b3.cvar import Cvar
from poweradminurt import PoweradminurtPlugin
from tests.iourt41 import Iourt41TestCase
from tests.iourt42 import Iourt42TestCase


class mixin_cmd_pasetnextmap(object):
    def setUp(self):
        super(mixin_cmd_pasetnextmap, self).setUp()
        self.conf = CfgConfigParser()
        self.conf.loadFromString("""
[commands]
pasetnextmap-snmap: 20
        """)
        self.p = PoweradminurtPlugin(self.console, self.conf)

        when(self.console).getCvar('timelimit').thenReturn(Cvar('timelimit', value=20))
        when(self.console).getCvar('g_maxGameClients').thenReturn(Cvar('g_maxGameClients', value=16))
        when(self.console).getCvar('sv_maxclients').thenReturn(Cvar('sv_maxclients', value=16))
        when(self.console).getCvar('sv_privateClients').thenReturn(Cvar('sv_privateClients', value=0))
        when(self.console).getCvar('g_allowvote').thenReturn(Cvar('g_allowvote', value=0))
        self.p.onLoadConfig()
        self.p.onStartup()

        self.sleep_patcher = patch.object(time, 'sleep')
        self.sleep_patcher.start()

        self.console.say = Mock()
        self.console.saybig = Mock()
        self.console.write = Mock()

        self.moderator.connects("2")


    def tearDown(self):
        super(mixin_cmd_pasetnextmap, self).tearDown()
        self.sleep_patcher.stop()


    def test_missing_parameter(self):
        self.moderator.clearMessageHistory()
        self.moderator.says("!snmap")
        self.assertEqual(['Invalid or missing data, try !help setnextmap'], self.moderator.message_history)


    def test_existing_map(self):
        # GIVEN
        when(self.console).getMapsSoundingLike('f00').thenReturn('f00')
        # WHEN
        self.moderator.clearMessageHistory()
        self.moderator.says("!snmap f00")
        # THEN
        verify(self.console).getMapsSoundingLike('f00')
        self.assertEqual(['nextmap set to f00'], self.moderator.message_history)


    def test_suggestions(self):
        # GIVEN
        when(self.console).getMapsSoundingLike('f00').thenReturn(['f001', 'foo2'])
        # WHEN
        self.moderator.clearMessageHistory()
        self.moderator.says("!snmap f00")
        # THEN
        verify(self.console).getMapsSoundingLike('f00')
        self.assertEqual(['do you mean : f001, foo2 ?'], self.moderator.message_history)



class Test_cmd_nuke_41(mixin_cmd_pasetnextmap, Iourt41TestCase):
    """
    call the mixin test using the Iourt41TestCase parent class
    """

class Test_cmd_nuke_42(mixin_cmd_pasetnextmap, Iourt42TestCase):
    """
    call the mixin test using the Iourt42TestCase parent class
    """
