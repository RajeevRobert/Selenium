rem Chrome
pytest -v -s -m "sanity" --html=..\Reports\SanityExecution.html --browser chrome
rem	pytest -v -s -m "regression" --html=..\Reports\SanityExecution.html --browser chrome
rem	pytest -v -s -m "sanity or regression" --html=..\Reports\SanityExecution.html --browser chrome
rem	pytest -v -s -m "sanity and regression" --html=..\Reports\SanityExecution.html --browser chrome

rem Firefox
rem pytest -v -s -m "sanity" --html=..\Reports\SanityExecution.html --browser firefox
rem	pytest -v -s -m "regression" --html=..\Reports\SanityExecution.html --browser firefox
rem	pytest -v -s -m "sanity or regression" --html=..\Reports\SanityExecution.html --browser firefox
rem	pytest -v -s -m "sanity and regression" --html=..\Reports\SanityExecution.html --browser firefox