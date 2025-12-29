# Automated-TradingView-NY-Session-Capture-Tool



Script gets a picture of every daily NY session in pdf format so I can have a book everyday. I dont want to manually screenshot everyday so was wondering if it's possible to create a python script on tradingview?







&nbsp;				\*\*\*Architecture\*\*\*





------main.py			-entry point (daily run)

|

|

------config/

|	--- settings.py		-time, paths, symbol, timeframe

|	--- constants.py	

|

|

------browser/

|	--- driver.py		- browser setup (Selenium)

|	--- tabs.py		- tab detection \& switching

|	--- cookies.py		- session persistence

|

|

------tradingview/

|	--- navigator.py	- open chart, load layout

|	--- session.py		- NY session logic (time)

|	--- visibility.py	- check chart is visible

|

|

------capture/

|	--- screenshot.py	- take screenshot

|	--- crop.py		- crop chart are

|	--- validate.py		- sanity checks

|
|

------pdf/

|	--- generator.py	- image ---> PDF

|	--- metadata.py		

|
|

------scheduler/

|	--- run\_daily.py	- optional wrapper

|

|

------utils/

|	--- delays.py		- human-like waits

|	--- logger.py	

|	---filesystem.py

|

|

------requirements.txt





Main.py :



1. Load settings
2. Start browser (reuse cookies)
3. Ensure TradingView tab exists
4. Open saved chart layout
5. Wait for NY session end
6. Verify chart visible
7. Capture screenshot
8. Crop chart
9. Generate PDF
10. Close browser
