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

 
    counter = 0
    
    #looping thru dictionary
    for start, end in interviews.items():
        #print("start:", start, " end:", end)
        if end >= start:
            counter = counter + 1
            #print(count)
    
    return jsonify({"max_interviews" : counter}), 200

