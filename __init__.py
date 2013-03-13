'''
ElophantAPI

A simple API Wrapper class for the Elophant API.

More information about the Elophant Developers API can be found here:
http://elophant.com/developers/docs

You can sign up for an API key here:
http://elophant.com/developers/new

Copyright (C) 2013 Byron Adams <byron.adams54@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

'''

import json
import urllib2

class ElophantException(Exception):
    def __init__(self, message):
        self.message = message
        super(ElophantException, self).__init__(self.message)

class ElophantAPI:

    BASE_URI = 'http://api.elophant.com/v2'

    def __init__(self, key, region = 'NA'):
        self.API_KEY = key
        self.REGION = region

    def call(self, params = []):

        params = '/'. join(map(str, params))

        response = urllib2.urlopen(
            '%s/%s/?key=%s' % (self.BASE_URI, params, self.API_KEY)                           
        ).read()

        data = json.loads(response.decode('UTF-8'))

        if not data['success']:
            raise ElophantException(data['error'])

        return data['data']

    def items (self):
        ''' Returns every items's id and name.'''
        return self.call(['items'])

    def champion(self):
        '''Returns every champion's id and name.'''
        return self.call(['champions'])
   
    def summoner(self, summoner_name):
        '''Returns a summoner's accountId, summonerId, account level, and profile icon id.'''
        return self.call([self.REGION, 'summoner', summoner_name])

    def mastery_pages(self, name):
        '''Returns an array with each mastery book page and subsequent talent point entries for a specific summoner.'''
        return self.call([self.REGION, 'mastery_pages', account_id])

    def rune_pages(self, account_id):
        '''Returns an array with each rune page and subsequent runes for a specific summoner.'''
        return self.call([self.REGION, 'rune_pages', account_id])

    def recent_games(self, account_id):
        '''Returns the statistics for a summoner's 10 most recent games.'''
        return self.call([self.REGION, 'recent_games', account_id])

    def summoner_names(self, names):
        ''' Returns an array of summoner names in the same order as provided in the parameter summonerIds. '''
        return self.call([self.REGION, 'summoner_names', ','.join(names)])

    def leagues(self, account_id):
        '''Returns the current League for the requested summonerId, including all players within the League.'''
        return self.call([self.REGION, 'leagues', account_id])

    def ranked_stats(self, account_id, season = 'current'):
        ''' Returns every statistic for every champion accumulated from all ranked game types for a specified summoner and season. '''
        return self.call([self.REGION, 'ranked_stats', account_id, season])

    def summoner_team_info(self, account_id):
        '''Returns all team info regarding the specified summoner, including team overviews and all of the teams the summoner has created.'''
        return self.call([self.REGION, 'summoner_team_info', account_id])

    def in_progress_game_info(self, summoner_name):
        '''Returns the player information for both teams, bans (if draft or ranked), and observer information.'''
        return self.call([self.REGION, 'in_progress_game_info', summoner_name])

    def team(self, team_id):
        '''Returns a brief overview of a team, including gameType dependent Elos, the current roster, and basic match history statistics.'''
        return self.call([self.REGION, 'team', team_id])

    def find_team(self, search):
        '''Returns a brief overview of a team, including gameType dependent Elos, the current roster, and basic match history statistics.'''
        return self.call([self.REGION, 'find_team', search])

    def team_end_of_game_stats(self, team_id, game_id):
        '''Returns very detailed statistics about the specified match.'''
        return self.call([self.REGION, 'team_end_of_game_stats', team_id, game_id])

    def team_ranked_stats(self, team_id):
        '''Returns each team member's statistics for the specified team. This call provides very similar results to getRankedStats.'''
        return self.call([self.REGION, 'team_ranked_stats', team_id])
                                  
