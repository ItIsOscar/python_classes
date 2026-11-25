key = "No man is an island,    Entire of itself,    Every man is a piece of the continent,    A part of the main.    If a clod be washed away by the sea,    Europe is the less.    As well as if a promontory were.    As well as if a manor of thy friend s    Or of thine own were:    Any mans death diminishes me,    Because I am involved in mankind,    And therefore never send to know for whom the bell tolls;    It tolls for thee."
key = key.replace(' ', '')
plain_message = "Kazakhstan is threatening to bomb us. We are mobilizing immediately everyone to arms! Putin usch a bad guy oh dear, tsk. But that still does not change the fact that we are heading off to war. Hurrah!"
circle_alghabet = 26
alphbet = [chr(x) for x in range(97,123)]

message = [chr((ord(n[0]) + ord(n[1])) % circle_alghabet + ord('a')) for n in zip(plain_message, key * ((len(plain_message) + len(key)) // len(key)))]
print(message)
stat = [[l, message.count(l) / len(message)] for l in alphbet]
variance_stat = sum([(x[1] - sum([y[1] for y in stat]) / len(stat)) * (x[1] - sum([y[1] for y in stat]) / len(stat)) for x in stat]) / len(stat)
print((variance_stat, max([y[1] for y in stat]) - min([y[1] for y in stat])))
print(stat)