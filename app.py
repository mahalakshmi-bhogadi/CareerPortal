from flask import Flask,render_template,jsonify
app=Flask(__name__)
JOBS=[
  {
    'id':1 ,
    'title':'Software Engineer',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'},
  {
    'id':2 ,
    'title':'Software Test Engineer',
    'location':'Hyderabad, India',
    'salary':'Rs. 8,00,000'
  },
  {
    'id':3,
    'title':'Data Analyst',
    'location':'Australia',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':4,
    'title':'Data Scientist',
    'location':'Chennai, India',
    'salary':'Rs. 7,00,000'
  },
  {
    'id':5,
    'title':'Data Engineer',
    'location':'Chennai, India'
  }
]
@app.route("/")
def maha():
  return render_template("home.html",jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)