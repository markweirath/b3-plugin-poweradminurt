#
# PowerAdmin Plugin for BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2012 Thomas LEVEIL <courgette@bigbrotherbot.net)
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
from poweradminurt.iourt41 import Poweradminurt41Plugin

class Poweradminurt42Plugin(Poweradminurt41Plugin):

    def cmd_pakill(self, data, client, cmd=None):
        """\
        <player> - kill a player.
        (You can safely use the command without the 'pa' at the beginning)
        """
        if not data:
            client.message('^7Invalid data, try !help panuke')
            return
        else:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient:
                # a player matchin the name was not found, a list of closest matches will be displayed
                # we can exit here and the user will retry with a more specific player
                return

        self.console.write('smite %s' % sclient.cid)



    def cmd_palms(self, data, client, cmd=None):
        """\
        Change game type to Last Man Standing
        (You can safely use the command without the 'pa' at the beginning)
        """
        self.console.write('g_gametype 1')
        if client:
            client.message('^7game type changed to ^4Last Man Standing')