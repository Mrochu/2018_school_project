#-*- coding: utf-8 -*-

counter = {'가위': '바위', '바위': '보', '보': '가위'}
def win(me, you):
	try:
		if me == you: return "비겼다"
		elif me == counter[you]: return "졌다"
		elif counter[me] == you: return "이겼다"
	except:
		return "오류"

def main():
	mem = {"가위": {"가위": 0, "바위": 0, "보": 0}, "바위": {"가위": 0, "바위": 0, "보": 0}, "보": {"가위": 0, "바위": 0, "보": 0}}
	then = "가위"
	now = ""

	while 1:
		# 내기
		me = counter[max(mem[then], key=mem[then].__getitem__)]
		now = input()
		res = win(me, now)

		if res == "오류": break

		print(me)
		print(res)

		# 기억
		mem[then][now] += 1
		then = now

main()
