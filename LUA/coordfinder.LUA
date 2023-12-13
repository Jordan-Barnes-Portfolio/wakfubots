--// This auto attaches to the java application thats open
PROCESS_NAME = 'java.exe'
--------
-------- Auto Attach
--------
local autoAttachTimer = nil ---- variable to hold timer object
local autoAttachTimerInterval = 1000 ---- Timer intervals are in milliseconds
local autoAttachTimerTicks = 0 ---- variable to count number of times the timer has run
local autoAttachTimerTickMax = 5000 ---- Set to zero to disable ticks max
local function autoAttachTimer_tick(timer) ---- Timer tick call back
        ---- Destroy timer if max ticks is reached
	if autoAttachTimerTickMax > 0 and autoAttachTimerTicks >= autoAttachTimerTickMax then
		timer.destroy()
	end
        ---- Check if process is running
	if getProcessIDFromProcessName(PROCESS_NAME) ~= nil then
		timer.destroy() ---- Destroy timer
		openProcess(PROCESS_NAME) ---- Open the process

		wait(2)

		--// Player location memory address
		scan = AOBScan("00 00 00 00 00 00 60 C1 00 00 C0 41 0? 00 00 0? 00 00 00 00 15 00 00 00 00 00 00 00 ??")
		print("Result : "..scan.count) --// The Result

		for i=1,scan.count do
		print(scan[i-1]) --// Prints the address
		address = scan[i-1]
		end

		function saveData(data)
			print("Data: "..tostring(data))
			local file,err = io.open("C:\\Users\\Jordan\\Desktop\\Programming\\GIT\\wakfubots\\LUA\\DATA.txt",'w')
			if file then
				file:write(tostring(data))
				file:close()
			else
				print("error:", err)
			end
		end

		saveData(address)
	end
	autoAttachTimerTicks = autoAttachTimerTicks + 1 ---- Increase ticks
end
autoAttachTimer = createTimer(getMainForm()) ---- Create timer with the main form as it's parent
autoAttachTimer.Interval = autoAttachTimerInterval ---- Set timer interval
autoAttachTimer.OnTimer = autoAttachTimer_tick ---- Set timer tick call back
function wait(seconds)
    local start = os.time()
    repeat until os.time() > start + seconds
end


