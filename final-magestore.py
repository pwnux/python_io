#calculate the accuracy of the predicting model using F1-score
results = list()
human = list()
with open('res.txt', 'r') as res:
    lines = res.readline()
    results.append(lines)

with open('human.txt', 'r') as _human:
    lines = _human.readline()
    human.append(lines)

label = [i for i in range(15)]

precision = [0] * len(label)
recall = [0] * len(label)
f1_score = [0] * len(label)
tp = [0] * len(label)   #true positive
fp = [0] * len(label)   #false positive
fn = [0] * len(label)   #false negative

for i in range(len(results)):
    if results[i] == human[i]:
        tp[results[i]] += 1
    else:
        fn[human[i]] += 1
        fp[results[i]] += 1

for i in range(len(label)):
    if tp[i] > 0:
        precision[i] = float(tp[i])/(float(tp[i]) + fp[i])
        recall[i] = float(tp[i])/(float(tp[i]) + fn[i])
    else:
        precision[i] = 0.0
        recall[i] = 0.0

for i in range(len(label)):
    if precision[i] + recall[i] > 0:
        f1_score[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])
    else:
        f1_score[i] = 0.0

print 'Label\tPrecision\tRecall\tF1-Score\n'
for i in range(len(label)):
    print '%i\t\%i\t%i\t%i\n' %(i, precision[i], recall[i], f1_score[i])
