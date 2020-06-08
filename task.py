from datetime import date,datetime,timedelta

def solution(D):

    timestamps=[]
    for key in D:
        timestamps.append([key,D[key]])

    timestamps.sort(key=lambda time:time[0])
    new_timestamps={}
    print(timestamps)



    for i in range(0,len(timestamps)-1):
        curr_date=timestamps[i][0].split('-')
        next_date=timestamps[i+1][0].split('-')
        l_date=date(int(next_date[0]),int(next_date[1]),int(next_date[2]))
        f_date=date(int(curr_date[0]),int(curr_date[1]),int(curr_date[2]))
        new_timestamps[timestamps[i][0]]=timestamps[i][1]
        n=(l_date-f_date).days  
        if n<=2:
            incr=(timestamps[i+1][1]+timestamps[i][1])//n
            start=0
        else:
            incr=abs(timestamps[i+1][1]-timestamps[i][1])//n
            start=timestamps[i][1]
        x=1
        while x!=n:
            new_timestamps[str(f_date + timedelta(1))]=start+incr
            f_date=f_date+timedelta(1)
            start +=incr
            x +=1
    new_timestamps[timestamps[len(timestamps)-1][0]]= timestamps[len(timestamps)-1][1]
    return new_timestamps
       
sol=solution({'2019-01-01':100,'2019-01-04':115})  
print(sol)
sol=solution({'2019-01-10':10,'2019-01-11':20,'2019-01-13':10})
print(sol)