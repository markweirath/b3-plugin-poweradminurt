#
# PowerAdmin Plugin for BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2008 Mark Weirath (xlr8or@xlr8or.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

# Changelog:
#
# 01:49 09/06/2008 by Courgette
#  * add commands pagear (to change allowed weapons)
#  * add commands paffa, patdm, pats, paftl, pacah, pactf, pabomb (to change g_gametype)
#  * now namecheck is disabled during match mode
#  * _smaxplayers is now set taking care of private slots (this is for speccheck)
#  * fixes in Mark's code (I suppose I checkout an unstable version)
#     for LoadRotationManager code, I'm not sure what you meant with all those successives "try:"
#     maybe this is a python 2.5 syntax ? wasn't working for me
# 01:21 09/07/2008 - Courgette
# * add command !paident <player> : show date / ip / guid of player. Useful when moderators make demo of cheaters
# 17/08/2008 - xlr8or
# * added counter for max number of allowed client namechanges per map before being kicked
# 20/10/2008 - xlr8or (v1.4.0b8)
# * fixed a bug where balancing failed and disabled itself on rcon socket failure.
# 10/21/2008 - 1.4.0b9 - mindriot
# * added team_change_force_balance_enable to control force balance on client team change
# 10/22/2008 - 1.4.0b10 - mindriot
# * added autobalance_gametypes to specify which gametypes to autobalance
# 10/22/2008 - 1.4.0b11 - mindriot
# * if client does not have teamtime, provide new one
# 10/23/2008 - 1.4.0b12 - mindriot
# * onTeamChange is disabled during matchmode
# 10/28/2008 - 1.4.0b13 - mindriot
# * fixed teambalance to set newteam if dominance switches due to clients voluntarily switching teams during balance
# 10/28/2008 - 1.4.0b14 - mindriot
# * teambalance verbose typo
# 12/07/2008 - 1.4.0b15 - xlr8or
# * teamswitch-stats-harvest exploit penalty -> non legit switches become suicides
# 2/9/2009 - 1.4.0b16 - xlr8or
# * added locking mechanism to paforce. !paforce <player> <red/blue/s/free> <lock>
# 2/9/2009 - 1.4.0b17 - xlr8or
# * Fixed a default value onLoad for maximum teamdiff setting
# 02:33 3/15/09 by FSK405|Fear
# added more rcon cmds:
#  !waverespawns <on/off> Turn waverespawns on/off
#  !bluewave <seconds> Set the blue team wave respawn delay
#  !redwave <seconds> Set the red team wave respawn delay
#  !setnextmap <mapname> Set the nextmap
#  !respawngod <seconds> Set the respawn protection
#  !respawndelay <seconds> Set the respawn delay
#  !caplimit <caps>
#  !timelimit <mins>
#  !fraglimit <frags>
#  !hotpotato <mins>
# 4/4/2009 - 1.4.0b18 - xlr8or
# * Fixed locked force to stick and not continue with balancing
# * Helmet and Kevlar messages only when connections < 20
# 28/6/2009 - 1.4.0 - xlr8or
# * Time to leave beta
# * Teambalance raises warning instead of error
# 10/8/2009 - 1.4.1 - naixn
# * Improved forceteam locking mechanism and messaging
# 10/8/2009 - 1.4.2 - xlr8or
# * Added TeamLock release command '!paforce all free' and release on gameExit
# 09/07/2009 - 1.4.3 by SGT
# add use of dictionary for private password (papublic)
# 27/10/2009 - 1.5.0 - Courgette
# /!\ REQUIRES B3 v1.2.1 /!\
# * add !pamap which works with partial map names
# * update !pasetnextmap to work with partial map names
# 27/10/2009 - 1.5.1 - Courgette
# * debug !pamap and !pasetnextmap
# * debug dictionnary use for !papublic
# * !papublic can now use randnum even if dictionnary is not used
# 31/01/2010 - 1.5.2 - xlr8or
# * added ignore Set and Check functions for easier implementation in commands
# * added ignoreSet(30) to swapteams and shuffleteams to temp disable auto checking functions
#   Note: this will be overridden by the ignoreSet(60) when the new round starts after swapping/shuffling!
# * Send rcon result to client on !paexec
# 13/03/2010 - 1.5.3 - xlr8or
# * fixed headshotcounter reset. now able to set it to 'no', 'round', or 'map'
# 19/03/2010 - 1.5.4 - xlr8or
# * fixed endless loop in ignoreCheck()
# 30/06/2010 - 1.5.5 - xlr8or
# * no longer set bot_enable var to 0 on startup when botsupport is disabled.
# 20/09/2010 - 1.5.6 - Courgette
# * debug !paslap and !panuke
# * add tests
# 20/09/2010 - 1.5.7 - BlackMamba
# * fix !pamute - http://www.bigbrotherbot.net/forums/xlr-releases/poweradminurt-1-4-0-for-urban-terror!/msg15296/#msg15296
# 25/07/2012 - 1.6 - Courgette
# * prepare separation of poweradmin plugin for UrT4.1 and UrT4.2
# * change default config file from xml to ini format
# * change the way to load from the config the list of plugins to disable in matchmode. See section 'matchmode' in config file
# * gracefully fallback on default value if cannot read publicmode/usedic from config file
# * UrT4.2: implement command !kill <player>
# 25/08/2012 - 1.6.1 - Courgette
# * fix checkunknown feature
# * name checker: provide exact reason for warning in log
# * fix plugin version since UrT 4.1/4.2 split
# 13/09/2012 - 1.6.2 - Courgette
# * UrT42: fix feedback message on missing parameter for the !pakill command
# 05/10/2012 - 1.6.3 - Courgette
# * UrT42: fix the headshot counter by introducing hit location constants
# 06/10/2012 - 1.7 - Courgette
# * UrT42: add the radio spam protection feature
# 21/10/2012 - 1.8 - Courgette
# * UrT42: change: update to new rcon mute command behavior introduced in UrT 4.2.004
#
__version__ = '1.8'
__author__  = 'xlr8or, courgette'


"""

Depending on the B3 parser loaded, this module will either act as the plugin for
UrT4.1 or the plugin for UrT4.2

"""

class PoweradminurtPlugin(object):

    def __new__(cls, *args, **kwargs):
        console, plugin_config = args
        if console.gameName == 'iourt41':
            from poweradminurt.iourt41 import Poweradminurt41Plugin
            return Poweradminurt41Plugin(*args, **kwargs)
        elif console.gameName == 'iourt42':
            from poweradminurt.iourt42 import Poweradminurt42Plugin
            return Poweradminurt42Plugin(*args, **kwargs)
        else:
            raise AssertionError("Poweradminurt plugin can only work with Urban Terror 4.1 or 4.2")