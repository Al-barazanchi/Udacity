
import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while(break_count<total_breaks):
	time.sleep(2)
	webbrowser.open("https://www.youtube.com/watch?v=u2Yk1CEgc4g")
	break_count += 1

for i in range(3):
	time.sleep(2)
	webbrowser.open("https://www.youtube.com/watch?v=u2Yk1CEgc4g")