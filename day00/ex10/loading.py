import time
import sys

def	ft_progress(listy):
	total = len(listy)
	bar_len = 40
	time_start = time.time()
	for n in listy:
		percents = round(100.0 * (n + 1) / float(total), 1)
		filled_len = int(round(bar_len * n / float(total)))
		bar = '=' * filled_len + ">" + (bar_len - filled_len) * ' '
		time_now = time.time() - time_start
		if n == total -1:
			sys.stdout.write("\033[1;32;40m")
		sys.stdout.write("[{:3.0f}%] [{}] {:3}/{} | elapsed time {:.2f}s \r"\
		.format(percents, bar, n+1, total, time_now))
		sys.stdout.flush()
		yield n

listy = range(456)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)

# time = time - time_start
# p / 100 = time /  time_max
#time_max = time / p / 100 
# time_max = time/p