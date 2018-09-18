#!/usr/bin/env python      

from plexapi.server import PlexServer
import xml.etree.ElementTree

baseurl = 'http://127.0.0.1:32400'

prefs = xml.etree.ElementTree.parse('/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Preferences.xml').getroot()
token = prefs.attrib['PlexOnlineToken']

plex = PlexServer(baseurl,token)

# Add Movies library
plex.library.add('Movies','movie','com.plexapp.agents.themoviedb','Plex Movie Scanner','/plex_libraries/movies')

# Add TV Shows library
plex.library.add('TV Shows','show','com.plexapp.agents.thetvdb','Plex Series Scanner','/plex_libraries/tv')
