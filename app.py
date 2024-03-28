from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Michael Haramis!'

@app.route('/hello')
def hello_world2():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favorite-course')
def favoritecourse():
   print(f'Favorite Course Subject: {request.args.get("course_subject")}')
   print(f'Favorite Course Number: {request.args.get("course_number")}')


   return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'POST':
       first_name = request.form.get('first_name')
       last_name = request.form.get('last_name')
       email = request.form.get('email')
       additional_info = request.form.get('additional_info')


       return render_template('contact.html', submitted=True, first_name=first_name, last_name=last_name, email=email, additional_info=additional_info)


   return render_template('contact.html', submitted=False)


if __name__ == '__main__':
    app.run(debug=True)
