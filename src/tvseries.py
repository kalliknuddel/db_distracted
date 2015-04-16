from xml.dom import minidom


def getText(nodelist):
    return nodelist[0].firstChild.nodeValue
#    rc = []
#    for node in nodelist:
#        if node.nodeType == node.TEXT_NODE:
#            rc.append(node.data)
#    return ''.join(rc)

def handleEpisode (episodeData):
    print "ID: "                         + getText(episodeData.getElementsByTagName("id"))
    print "SeriesID: "                   + getText(episodeData.getElementsByTagName("seriesid"))
    print "SeasonID: "                   + getText(episodeData.getElementsByTagName("seasonid"))
    print "Compined Episode Number: "    + getText(episodeData.getElementsByTagName("Combined_episodenumber"))
    print "Season Number: "              + getText(episodeData.getElementsByTagName("SeasonNumber"))
    print "Episode Number: "             + getText(episodeData.getElementsByTagName("EpisodeNumber"))
    print "Title: "                     + getText(episodeData.getElementsByTagName("EpisodeName"))
    print "First Aired: "                + getText(episodeData.getElementsByTagName("FirstAired"))
    print ""

def handleEpisodes (episodes):
    for episodeData in episodes:
        handleEpisode (episodeData)

def handleSeries (seriesfile):
    xmldoc = minidom.parse(seriesfile)
    episodes = xmldoc.getElementsByTagName("Episode")
    handleEpisodes (episodes)

