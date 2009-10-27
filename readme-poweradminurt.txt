###################################################################################
#
# PowerAdminUrt
# Plugin for B3 (www.bigbrotherbot.com)
# (c) 2006 www.xlr8or.com (mailto:xlr8or@xlr8or.com)
#
# This program is free software and licensed under the terms of
# the GNU General Public License (GPL), version 2.
#
# http://www.gnu.org/copyleft/gpl.html
###################################################################################

PowerAdminUrt (v1.4.0b3) for B3
###################################################################################

This plugin works for 4.1 only! This plugin adds powerfull commands 
and functions to your b3:

Added Commands:
!pamute (!mute) [<seconds>] - mute a player 
!panuke (!nuke) <name/id> [<amount>] - nuke a player (a number of times)
!paslap (!slap) <name/id> [<amount>] - slap a player (a number of times)
!paveto (!veto) - veto the current running vote
!pabigtext (!bigtext) - display a bigtext message center screen
!pashuffleteams (!shuffleteams) - shuffle the teams
!paswapteams (!swapteams) - swap the teams
!paforce (!force) <blue/red/s> - force a player to a team 

!pamaprestart (!maprestart) - restart current map
!pamapreload (!mapreload) - reload current map
!pacyclemap (!cyclemap) - start next map in rotation
!papause - pause the current game
!paset - set a server cvar
!paget - display a server cvar
!paexec <configfile.cfg> - execute a server configfile
!pateams (!teams) - activate teambalancer (read below)
!pavote <on/off/reset> - Switch voting. It remembers your voting settings!

!pamoon (!moon) - Activate Moon Mode... low gravity
!papublic (!public) - Make the server public, or private!
!pamatch (!match) - Switch to MatchMode
!pagear (!gear) - <all/none/reset/[+-](nade|snipe|spas|pistol|auto|negev)> - Set allowed weapons.
    
!paffa (!ffa) - switch to gametype: Free For All
!patdm (!tdm) - switch to gametype: Team Death Match
!pats (!ts) - switch to gametype: Team Survivor
!paftl (!ftl) - switch to gametype: Follow The Leader
!pacah (!cah) - switch to gametype: Capture And Hold
!pactf (!ctf) - switch to gametype: Capture The Flag
!pabomb (!bomb) - switch to gametype: BombMode

!paident (!id) <name/id> - prints a players B3-id, Guid and IP to screen for demo purposes
!paversion (!paver) - spits out the version of PowerAdminUrt

Each command (except !paversion) can be leveled in the config file.

Autobalancer:
When active the autobalancer makes sure the teams will always be balanced. When a 
player joins a team that is already outnumbering the other team B3 will immediately
correct the player to the right team. The balancer also checks on (configurable)
intervals if balancing is needed. In that case it will balance the player with the 
least teamtime, so the player that joined the team last will be force to the other
team.

Namechecker:
When active it can check unwanted playernames. This is a simple function and warns
players using duplicate names, the name 'all' or 'New UrT Player' depending on the 
config. Three warnings without a responding rename action will result in a kick.

Vote Delayer:
You can disable voting during the first minutes of a round. Set the number of
minutes in the config and voting will be disabled for that amount of time. 

Spec Checker:
Controls how long a player may stay in spec before being warned. All parameters
are configurable.

Bot Support:
This will crash your server. I've put it in here as a challenge for you programmers
out there to fix us a stable version.

Headshot counter:
Broadcasts headshots made by players.

RotationManager:
Switches between different mapcycles, based on the playercount.  

Requirements:
###################################################################################

- ioUrT
- B3 version 1.1.3 or higher


Installation of the B3 plugin:
###################################################################################

To install the b3-plugin part:

1. Unzip the contents of this package. Go to the unzipped folder extplugins and
place the .py file in the bots folder b3/extplugins and the config file .xml in
the b3/extplugins/conf folder.

2. Open the .xml file with your favorit editor and modify the
levels if you want them different. Do not edit the command-names
for they will not function under a different name.

3. Open your B3.xml file (in b3/conf) and add the next line in the
<plugins> section of the file:

<plugin name="poweradminurt" priority="13" config="@b3/extplugins/conf/poweradminurt.xml"/>

The numer 13 in this just an example. Make sure it fits your
plugin list.

Important!
###################################################################################
In order to make Spec checker work it is crucial you edit b3/conf/plugin_admin.xml
Open the file with your favorite text editor and look for the next line:
    <set name="spectator">5m, ^7spectator too long on full server</set>
Change it to:
    <set name="spectator">1h, ^7spectator too long on full server</set>

Changelog
###################################################################################
v1.0.0b1       : Beta version 1 for closed beta group testing. 
v1.0.0         : Initial release. 
v1.2.0         : Compatible with UrT v4.1 and a few bugs fixed
                 (thanks to 'Courgette'!)
v1.3.0         : Release
v1.4.0b1       : Added and improved functionality
v1.4.0b3       : Fixed some minor bugs and added multipunish to !slap and !nuke 

###################################################################################
xlr8or - 29 july 2008 - www.bigbrotherbot.com // www.xlr8or.com
