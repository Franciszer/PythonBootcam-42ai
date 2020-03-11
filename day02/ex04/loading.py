import time
import sys

def	progressbar(listy):
	total = len(listy)
	bar_len = 40
	time_start = time.time()
	for n in listy:
		percents = round(100.0 * (n + 1) / float(total), 1)
		filled_len = int(round(bar_len * n / float(total)))
		bar = '=' * filled_len + ">" + (bar_len - filled_len) * ' '
		time_now = time.time() - time_start
		time_left = (0.01 * total) - time_now if (0.01 * total) - time_now > 0 else 0.00 
		if n == total -1:
			sys.stdout.write("\033[1;32;40m")
		sys.stdout.write("ETA: {:2f} [{:3.0f}%] [{}] {:3}/{} | elapsed time {:.2f}s \r"\
		.format(time_left, percents, bar, n+1, total, time_now))
		sys.stdout.flush()
		yield n
