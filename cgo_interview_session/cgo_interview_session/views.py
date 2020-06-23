from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseRedirect

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

@api_view(['GET', 'POST'])
def homeReq(request):
    return HttpResponseRedirect("get_earliest_reach_time/?X=5&A=[1,3,1,4,2,3,5,4]")

@api_view(['GET', 'POST'])
def solutionReq(request):
    if request.method == "GET":
        position=int(request.GET['X'])
        leavesfalltime_list=request.GET['A'].replace('[','').replace(']','').split(',')

        if len(leavesfalltime_list)>0:
            return Response(solution(position, leavesfalltime_list), status=status.HTTP_200_OK)
        else:
            return Response("Please provide non empty array A", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)