@echo off
FOR /L %%M IN (0, 1,7776) DO (
    more ascii%%M.txt
	timeout /t 0.1
	cls
)