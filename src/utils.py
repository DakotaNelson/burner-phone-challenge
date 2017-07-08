import random

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

# modified from https://stackoverflow.com/questions/26226801/making-random-phone-number-xxx-xxx-xxxx
def phone_number_generator():
    already_used = []
    while True:
        p=list('0000000000')
        p[0] = str(random.randint(1,9))
        for i in [1,2,6,7,8]:
            p[i] = str(random.randint(0,9))
        for i in [3,4]:
            p[i] = str(random.randint(0,8))
        if p[3]==p[4]==0:
            p[5]=str(random.randint(1,8))
        else:
            p[5]=str(random.randint(0,8))
        n = list(range(10))
        if p[6]==p[7]==p[8]:
            n = (i for i in n if i!=p[6])
        #import pdb; pdb.set_trace()
        p[9] = random.choice(list(n))
        p = ''.join([str(x) for x in p])
        number = p[:3] + '-' + p[3:6] + '-' + p[6:]
        if number not in already_used:
            already_used.append(number)
            yield number

