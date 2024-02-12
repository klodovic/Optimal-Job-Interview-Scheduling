from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/job', methods=['POST'])
def countJobInteviews():
    
    data = request.get_json() 
    response = ""
    
    #checking if data exists
    if not data:
        response = "Error - Not Acceptable"
        return jsonify(response), 406
    
    #checkin if data have lists
    for d in data:
        if d != "start_times" and d != "end_times":
            response = "Error - Bad Request"
            return jsonify(response), 400
        
    #storing data into lists
    start_times = data.get("start_times")
    end_times = data.get("end_times")
    
    #merging lists into dictionary
    interviews = dict(zip(start_times, end_times))
    print(interviews)
    
    
    counter = 1
    if interviews.__len__() == 0:
        counter = 0
 
    
    #looping through dictionary and counting
    end = list(interviews.values())[0] 
    
    for i in range(1, interviews.__len__()):
        #print(i, "sastanak završava: ", end)
        start = list(interviews.items())[i][0]
        #print(i+1, "sastanak pocinje: ", start)
        if end <= start:
            counter += 1
            end = list(interviews.items())[i][1]
        else:
            end = list(interviews.items())[i][1]
        
    
    return jsonify({"max_interviews" : counter}), 200

