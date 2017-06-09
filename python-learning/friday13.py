def killcount(conselors, jason):
	outsmarted = []
	for conselor in conselors:
		if conselor[1] < jason:
			outsmarted.append(conselor)
	return outsmarted

conselors = [
	["Richard", 107],
	["Robert", 500],
	["Igor", 50]
]

killed = killcount(conselors, 120)

for killed_person in killed:
	print(killed_person[0] + " " + str(killed_person[1]))



