universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def entrollment_stats(unis):
    s=[row[1] for row in unis]
    t=[row[2] for row in unis]
    return s,t
def mean(l):
    return sum(l)/len(l)
def median(l):
    if len(l)%2==1:
        return sorted(l)[len(l)//2]
    else:
        return (sorted(l)[len(l)//2]+sorted(l)[len(l)//2-1])/2
s,t=entrollment_stats(universities)
ts=sum(s)
tt=sum(t)
sm=mean(s)
smd=median(s)
tm=mean(t)
tmd=median(t)
print(f'Total students: {ts}\nTotal tution: $ {tt}\nStudent mean: {sm:.2f}\nStudent median: {smd:.0f}\nTution mean: $ {tm:.2f}\nTution median: $ {tmd:.0f}')


   