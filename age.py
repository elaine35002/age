driving = input('請問您有沒有開過車? ')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('請問您的年齡? ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過開車驗證了')
	else:
		print('奇怪 你怎麼會開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考駕照了，快去考吧')
	else:
		print('很好，再過幾年就可以考駕照了')

