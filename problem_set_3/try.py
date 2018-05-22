import ps3b

# import matplotlib.pylab as plt

# virus1 = ps3b.SimpleVirus(0.5, 0.3)
# virus2 = ps3b.SimpleVirus(0.5, 0.3)
# virus3 = ps3b.SimpleVirus(0.5, 0.3)
# virus4 = ps3b.SimpleVirus(0.5, 0.3)
# virus5 = ps3b.SimpleVirus(0.5, 0.3)
# virus6 = ps3b.SimpleVirus(0.5, 0.3)
# viruses = [virus1, virus2, virus3, virus4, virus5, virus6]

# for virus in viruses:
#     try:
#         print(virus.reproduce(0.1))
#     except ps3b.NoChildException:
#         print('no child')
    

# print("#"*20)
# numViruses = []
# patient = ps3b.Patient(viruses, 50)
# for i in range(100):
#     numViruses.append(patient.getTotalPop())
#     patient.update()
# plt.plot(numViruses)
# plt.show()

# ps3b.simulationWithoutDrug(100, 200, 0.2, 0.8, 1)

# ps3b.simulationWithoutDrug(100,1000,0.1,0.05,100)
# virus1 = ps3b.ResistantVirus(0.1,0.05,{'at':True},0.3)
# print(virus1.getClearProb())
# print('a' if not virus1.isResistantTo('at'))
# virus = ps3b.ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": False}, 0.0)
# child = virus.reproduce(0, ["drug2"])
# child = virus.reproduce(0, ["drug1"])

# virus = ps3b.ResistantVirus(1.0, 0.0, {'drug1': True, 'drug2': True,
#                                   'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
# childs=[]
# for i in range(10):
#     childs.append(virus.reproduce(0, []))

# # Checking the resistances of the children to each of the 6 prescriptions.
# for child in childs:
#     print(child.getResistances())
# print('\n',virus.getResistances())

# virus1 = ps3b.ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# virus2 = ps3b.ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
# virus3 = ps3b.ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": False}, 0.0)
# patient = ps3b.TreatedPatient([virus1, virus2, virus3], 100)

# i = 0
# while i < 10:  
#     print(patient.getResistPop(['drug2']))
#     patient.update()
    
#     i+=1

ps3b.simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)



