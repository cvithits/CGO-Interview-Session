from django.http import HttpResponseRedirect
from django.http import HttpResponse

def solution(X, A):
    travelpos_list=[str(i) for i in range(1,X+1)]

    seconds=0
    for leave_fall_pos in A:
        if leave_fall_pos in travelpos_list:
            travelpos_list.remove(leave_fall_pos)
        if len(travelpos_list) == 0:
            break
        seconds+=1

    if len(travelpos_list) == 0:
        return seconds #returns the earliest time when the frog can jump to the other side of the river.
    else:
        return -1 #If the frog is never able to jump to the other side of the river, the function should return −1.

def homeReq(request):
    return HttpResponse("get_earliest_reach_time/position/leavesfalltime")

def solutionReq(request, position, leavesfalltime):

    leavesfalltime_list=list()
    for item in leavesfalltime:
        if item != '-' and item != '_':
            leavesfalltime_list.append(item)

    if len(leavesfalltime_list)>0:
        return HttpResponse(solution(position, leavesfalltime_list))
    else:
        return HttpResponse("Please provide non empty array A")