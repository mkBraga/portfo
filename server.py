from flask import Flask ,render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


#Home
@app.route('/')
def my_home():
    return render_template('./index.html')

#MELHOR FORMA
@app.route('/<string:page_name>')
def html_Page(page_name):
    return render_template(page_name)


def write_to_cvs(data):
    #Atenção ao caminho
    with open('database.csv', mode='a', newline='\n') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',  quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            #tem um metodo que passa tudo o que tiver para dicionario .to_dict()
            data = request.form.to_dict()
            write_to_cvs(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Error'
