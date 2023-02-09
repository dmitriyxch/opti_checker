win_walets = []
my_wallets = []

win_file = open('finished_copy.txt', 'r')
for line in win_file:
    win_walets.append(line[:-1].lower())
win_file.close()

my_file = open('finished.txt', 'r')
for line in my_file:
    my_wallets.append(line[:-1].lower())
my_file.close()

results = list(set(win_walets) & set(my_wallets))
print(results)
print(len(results))
resultsFile = open( 'results.txt', 'w')
for element in results:
     resultsFile.write(element)
     resultsFile.write('\n')
resultsFile.close()
