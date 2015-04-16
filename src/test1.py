import urllib
import zipfile
from xml.dom import minidom

import tvseries
from tvseries import getText

seriesName = "Arrow"

urllib.urlretrieve ("http://thetvdb.com/api/GetSeries.php?seriesname=" + seriesName, seriesName + "_overview.xml")

xmldoc = minidom.parse(seriesName + "_overview.xml")
seriesid = xmldoc.getElementsByTagName("seriesid")[0].firstChild.nodeValue
seriesname = xmldoc.getElementsByTagName("SeriesName")[0].firstChild.nodeValue

#   URL Pfad bauen mit der SerienID aus der overview.xml
#   Ausgabepfade bauen und zwischenspeichern
dudu = "http://thetvdb.com/api/20EE1583110A3BA2/series/" + seriesid + "/all/en.zip"
filename = seriesid + "_" + seriesname + ".zip"
urllib.urlretrieve (dudu, filename);

#   zipfile pruefen und extrahieren
print zipfile.is_zipfile (filename)
yadaZip = zipfile.ZipFile (filename, "r")
yadaZip.extractall ("extracted")

#   extrahierte daten parsen und ausgeben
tvseries.handleSeries ("extracted/en.xml")

