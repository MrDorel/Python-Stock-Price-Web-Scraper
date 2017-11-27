import time
import urllib
import re



def main ():
	
	sec = 20
	timeT = 0

	while timeT < sec:

		oldPrice = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'	
		print "Checking the current price of apple stock. This may take a few a few seconds..."
		time.sleep(5)
		htmlfile = urllib.urlopen("http://www.nasdaq.com/symbol/aapl/real-time")
		htmltext = htmlfile.read()
		regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'	
		pattern = re.compile(regex)
		newPrice = re.findall(pattern,htmltext)
		oldPrice = newPrice
		print " The current price of apple stock is: "
		print newPrice
		
		if newPrice != oldPrice:
			print "Price changed!"
			oldPrice = newPrice
		
		else:
			print "The new Apple stock price is:"
			timeT +=1
			
		print newPrice
		
		if timeT < sec:
			print "Restarting...This may take a few seconds..."
		
		if timeT == sec:
			print "Ending process..."
		
		
	

main()




