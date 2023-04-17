from flask import Flask, render_template, jsonify

main = Flask(__name__)

COURSES = [{
  'id':1,
  'course': 'Physics 3',
  'Qualification': 'BSc in Physical Sciences',
  'Fees': 'R 14,000',
  'Prerequisite': 'Physics 2 and Mathematics 2',
  'ViewPhysics': 'https://physics-website.karabomohlapo.repl.co'
  'ApplyPhysics':''
}, {
  'id':2,
  'course': 'Computer Science 3',
  'Qualification': 'BSc in Information Technology',
  'Fees': 'R 9,000',
  'Prerequisite': 'Computer Science 2 and Mathematics 1',
  'Hyperlink': 'CSlink'
}, {
  'id':3,
  'course': 'Mathematics 3',
  'Qualification': 'BSc in Mathematical Sciences',
  'Fees': 'R 6,500',
  'Prerequisite': 'Mathematics 2',
  'Hyperlink': 'Mathlink'
}, {
  'id':4,
  'course': 'Biology 3',
  'Qualification': 'BSc in Life Sciences',
  'Fees': 'R 6,000',
  'Prerequisite': 'Biology 2',
  'Hyperlink': 'Biolink'
}, {
  'id':5,
  'course': 'Chemistry 3',
  'Qualification': 'BSc in Physical Sciences',
  'Fees': 'R 11,000',
  'Prerequisite': 'Chemistry 2 and Mathematics 1',
  'Hyperlink': 'Chemlink'
}]


@main.route('/')
def hello_world():
  return render_template("home.html", courses=COURSES)
  
@main.route('/courses')
def course_list():
  return jsonify(COURSES)

if __name__ == "__main__":
  main.run(host='0.0.0.0', debug=True)
