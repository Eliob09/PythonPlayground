while True:
	
	print('wie schlau bist du?')
	antwort =input()
	try:
		
		if int(antwort) >=100:
			print("Extrem schlau")
		elif int(antwort) > 50 :
			print("Normal schlau")
		elif int(antwort) < 10:
			print("Richtig dumm")
		else:
			print("Einbisschen dumm")
	except:
		print("Bitte eine Zahl eingeben#")
	