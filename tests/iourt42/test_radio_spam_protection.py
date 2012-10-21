# -*- encoding: utf-8 -*-
from mock import Mock, call
from mockito import when
import sys
from b3.config import CfgConfigParser
from b3.cvar import Cvar
from poweradminurt import PoweradminurtPlugin
from tests.iourt42 import Iourt42TestCase

class Test_radio_spam_protection(Iourt42TestCase):
    def setUp(self):
        super(Test_radio_spam_protection, self).setUp()
        self.conf = CfgConfigParser()
        self.p = PoweradminurtPlugin(self.console, self.conf)

        when(self.console).getCvar('timelimit').thenReturn(Cvar('timelimit', value=20))
        when(self.console).getCvar('g_maxGameClients').thenReturn(Cvar('g_maxGameClients', value=16))
        when(self.console).getCvar('sv_maxclients').thenReturn(Cvar('sv_maxclients', value=16))
        when(self.console).getCvar('sv_privateClients').thenReturn(Cvar('sv_privateClients', value=0))
        when(self.console).getCvar('g_allowvote').thenReturn(Cvar('g_allowvote', value=0))


    def init(self, config_content=None):
        if config_content:
            self.conf.loadFromString(config_content)
        else:
            self.conf.loadFromString("""
[radio_spam_protection]
enable: True
mute_duration: 2
        """)
        self.p.onLoadConfig()
        self.p.onStartup()



    def test_conf_nominal(self):
        self.init("""
[radio_spam_protection]
enable: True
mute_duration: 2
        """)
        self.assertTrue(self.p._rsp_enable)
        self.assertEqual(2, self.p._rsp_mute_duration)


    def test_conf_nominal_2(self):
        self.init("""
[radio_spam_protection]
enable: no
mute_duration: 1
        """)
        self.assertFalse(self.p._rsp_enable)
        self.assertEqual(1, self.p._rsp_mute_duration)


    def test_conf_broken(self):
        self.init("""
[radio_spam_protection]
enable: f00
mute_duration: 0
        """)
        self.assertFalse(self.p._rsp_enable)
        self.assertEqual(2, self.p._rsp_mute_duration)



    def test_spam(self):
        # GIVEN
        self.init("""
[radio_spam_protection]
enable: True
mute_duration: 2
""")
        self.joe.connects("0")
        self.console.write = Mock(wraps=lambda x: sys.stderr.write("%s\n" % x))
        self.joe.warn = Mock()

        def joe_radio(msg_group, msg_id, location, text):
            self.console.parseLine('''Radio: 0 - %s - %s - "%s" - "%s"''' % (msg_group, msg_id, location, text))

        def assertSpampoints(points):
            self.assertEqual(points, self.joe.var(self.p, 'radio_spamins', 0).value)

        assertSpampoints(0)

        # WHEN
        when(self.p).getTime().thenReturn(0)
        joe_radio(3, 3, "Patio Courtyard", "Requesting medic. Status: healthy")
        # THEN
        assertSpampoints(0)
        self.assertEqual(0, self.joe.warn.call_count)
        self.assertEqual(0, self.console.write.call_count)

        # WHEN
        when(self.p).getTime().thenReturn(0)
        joe_radio(3, 3, "Patio Courtyard", "Requesting medic. Status: healthy")
        # THEN
        assertSpampoints(7)
        self.assertEqual(0, self.joe.warn.call_count)
        self.assertEqual(0, self.console.write.call_count)

        # WHEN
        when(self.p).getTime().thenReturn(1)
        joe_radio(3, 1, "Patio Courtyard", "f00")
        # THEN
        assertSpampoints(9)
        self.assertEqual(0, self.joe.warn.call_count)
        self.assertEqual(0, self.console.write.call_count)

        # WHEN
        when(self.p).getTime().thenReturn(1)
        joe_radio(3, 1, "Patio Courtyard", "f00")
        # THEN
        assertSpampoints(5)
        self.console.write.assert_has_calls([call("mute 0 2")])
