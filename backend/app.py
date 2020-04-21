from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/fcfs',methods=['POST'])
def fcfs():
	p=request.json['processes']
	for i in p:
		i["e"]=False
	current_time=0
	executed=0
	p=sorted(p, key = lambda i: i['at']) 
	while executed<len(p):
		for i in p:
			if not i["e"]:
				if i["at"]>current_time:
					current_time+=1
					break
				else:
					current_time+=i["bt"]
					i["e"]=True
					i["ct"]=current_time
					i["tat"]=i["ct"]-i["at"]
					i["wt"]=i["tat"]-i["bt"]
					executed+=1
	p=sorted(p, key = lambda i: i['id'])
	return json.dumps(p)   


