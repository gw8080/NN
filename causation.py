#:X:Synset('belief.n.01'):A:Synset('volition.n.01'):B:Synset('idea.n.01'):EQUIV:0.16666666666666666:XA:0.16666666666666666:XB:0.3333333333333333  belief -> idea via the method of volition
#:X:Synset('purpose.n.01'):A:Synset('volition.n.01'):B:Synset('percept.n.01'):EQUIV:0.14285714285714285:XA:0.14285714285714285:XB:0.2  purpose -> volition via the method of percept
#:X:Synset('faculty.n.01'):A:Synset('belief.n.01'):B:Synset('memory.n.01'):EQUIV:0.25:XA:0.2:XB:0.16666666666666666 faculty - > memory via the method of belief
from nltk.corpus import wordnet as wn
file_object = open('causation_schematic', 'w')
with open("objects.txt") as file:
    for x in file:
        x = x.rstrip("\n")
        checkA = wn.synsets(x)
        if wn.synsets(x):
            print(checkA[0].name())
            with open("objects.txt") as another_file:
                for y in another_file:
                    y = y.rstrip("\n")
                    checkB = wn.synsets(y)
                    if wn.synsets(y):
                        scanA = checkA[0]
                        scanB = checkB[0]
                        scanEquiv = wn.path_similarity(checkA[0], checkB[0])
                        with open("actions.txt") as another_fileB:
                            for z in another_fileB:
                                z = z.rstrip("\n")
                                checkC = wn.synsets(z)
                                if wn.synsets(z):
                                    scanX = checkC[0]
                                    scanA2 = wn.path_similarity(checkA[0], checkC[0])
                                    scanB2 = wn.path_similarity(checkB[0], checkC[0])
                                    i = 0.2
                                    if checkA != checkB and checkA != checkC and checkB != checkC:  
                                        if scanA2 > scanB2:
                                            if float(scanB2) > i:
                                                file_object.write(str(scanX.name()).split(".")[0])
                                                file_object.write(" -> ")
                                                file_object.write(str(scanB.name()).split(".")[0])
                                                file_object.write(" via ")
                                                file_object.write(str(scanA.name()).split(".")[0])
                                                file_object.write("\n")
                                        if scanB2 > scanA2:
                                            if float(scanA2) > i:
                                                file_object.write(str(scanX.name()).split(".")[0])
                                                file_object.write(" -> ")
                                                file_object.write(str(scanA.name()).split(".")[0])
                                                file_object.write(" via ")
                                                file_object.write(str(scanB.name()).split(".")[0])
                                                file_object.write("\n")                            
file_object.close()