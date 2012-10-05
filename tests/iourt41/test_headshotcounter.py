# -*- encoding: utf-8 -*-
from mock import  Mock
from mockito import when
from b3.config import CfgConfigParser
from b3.cvar import Cvar
from poweradminurt import PoweradminurtPlugin
from tests.iourt41 import Iourt41TestCase

class Test_headshotcounter(Iourt41TestCase):
    def setUp(self):
        super(Test_headshotcounter, self).setUp()
        self.conf = CfgConfigParser()
        self.conf.loadFromString("""
[headshotcounter]
# enable the headshot counter?
hs_enable: True
# reset counts? Options: no / map / round
reset_vars: no
# set broadcast to True if you want the counter to appear in the upper left, False is in chatarea
broadcast: True
# Announce every single headshot?
announce_all: True
# Announce percentages (after 5 headshots)
announce_percentages: True
# Only show percentages larger than next threshold
percent_min: 10
# Advise victims to wear a helmet?
warn_helmet: True
# After how many headshots?
warn_helmet_nr: 7
# Advise victims to wear kevlar?
warn_kevlar: True
# After how many torso hits?
warn_kevlar_nr: 50
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


    def test_hitlocation(self):

        def joe_hits_simon(hitloc):
            #Hit: 13 10 0 8: Grover hit jacobdk92 in the Head
            #Hit: cid acid hitloc aweap: text
            self.console.parseLine("Hit: 7 6 %s 8: Grover hit jacobdk92 in the Head" % hitloc)

        def assertCounts(head, helmet, torso):
            self.assertEqual(head, self.joe.var(self.p, 'headhits', default=0.0).value)
            self.assertEqual(helmet, self.joe.var(self.p, 'helmethits', default=0.0).value)
            self.assertEqual(torso, self.simon.var(self.p, 'torsohitted', default=0.0).value)


        # GIVEN
        self.joe.connects("6")
        self.simon.connects("7")

        # WHEN
        joe_hits_simon(4)
        # THEN
        assertCounts(head=0.0, helmet=0.0, torso=0.0)

        # WHEN
        joe_hits_simon(0) # 1 is head on 4.1
        # THEN
        assertCounts(head=1.0, helmet=0.0, torso=0.0)

        # WHEN
        joe_hits_simon(1) # 4 is helmet on 4.1
        # THEN
        assertCounts(head=1.0, helmet=1.0, torso=0.0)

        # WHEN
        joe_hits_simon(2) # 5 is torso on 4.1
        # THEN
        assertCounts(head=1.0, helmet=1.0, torso=1.0)



