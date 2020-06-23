# CGO-Interview-Session
A rich RESTful APIs application named "CGO Interview Session" by Django Framework and
packaged the CGO Interview Session application to Docker's container on port 9999

Using docker compose:
docker-compose up

Parameters input example
http://ec2-13-229-200-227.ap-southeast-1.compute.amazonaws.com:9999/get_earliest_reach_time/?X=5&A=[1,3,1,4,2,3,5,4]
-> return 6

http://ec2-13-229-200-227.ap-southeast-1.compute.amazonaws.com:9999/get_earliest_reach_time/?X=7&A=[1,3,1,4,2,3,5,4]
-> return -1


(Above ec2 will be kept running until 26/06/2020 23:59)
