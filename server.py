 # aula_252_253_254_255_256_257_258_259_260


##### Setting Up Flask ######

# 1 - Install Venv
# 2 - Install Flask dentro do venv

#################################################################     Venv     ###################################################################
#                               
#           INSTAL:                 python3 -m venv venv (CMD)
#           Activate:               venv\scripts\activate (CMD)                  
#           DEFINITION:             Não esquecer depois de instalar activar para usar     
#           DOCUMENTATION:          https://docs.python.org/3/library/venv.html
#                                   https://stackoverflow.com/questions/1783146/where-in-a-virtualenv-does-the-custom-code-go
#              
##################################################################################################################################################

#################################################################     Flask    ###################################################################
#                               
#           INSTAL:                 pip install flask (CMD)
#           Define flask            set FLASK_APP=server.py             
#           RUN:                    flask run  (CMD)  
#           Debug On:               set FLASK_ENV=development (CMD)  para atualizar automaticamente                
#           DEFINITION:             uma framework, para criar um server (uma ferramenta)     
#           DOCUMENTATION:          http://flask.palletsprojects.com/en/1.1.x/    
#           Templates:              Temos de criar pasta Templates e inserir os ficheiros .html         http://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
#           static:                 teremos de criar pasta static para inserir os ficheiros .css e .java    
#           Favicon:                Icon: http://flask.palletsprojects.com/en/1.1.x/patterns/favicon/  
#                               
#           ###
#           URL:                    https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for 
#           Jinja: {{ }}            https://en.wikipedia.org/wiki/Jinja_(template_engine)
#           Variable-rules          https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
#           Acess Request Data:     https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
#                      
#   
##################################################################################################################################################

##################################################     Python Virtual Environments     ###########################################################
#                               
#           INSTAL:                                   
#           DEFINITION:              
#           DOCUMENTATION:      https://realpython.com/python-virtual-environments-a-primer/
#              
##################################################################################################################################################


###############################################################     Temas Web     ################################################################ 
#                               
#           INSTAL:                                   
#           DEFINITION:              
#           DOCUMENTATION:      http://www.mashup-template.com/templates.html
#              
##################################################################################################################################################

##################################################################     CSV     ################################################################### 
#                               
#           INSTAL:                                   
#           DEFINITION:              
#           DOCUMENTATION:      https://docs.python.org/3/library/csv.html
#              
##################################################################################################################################################

#############################################################     PythonAnywhere    ############################################################## 
#                               
#           INSTAL:                                   
#           DEFINITION:         para alujar nosso site      
#           DOCUMENTATION:      https://help.pythonanywhere.com/pages/Flask/
#              
##################################################################################################################################################



#Para reutilizar
# 1 - venv\scripts\activate (activar venv)
# 2 - set FLASK_APP=server.py  (identificar flask ao ficheiro python)
# 3 - set FLASK_ENV=development (para atualizar automaticamente)
# 4 - flask run (para executar)



#render_templates = para aceder a ficheiros html, terei de criar uma pasta template porque o metodo só reconhece dentro da pasta template
#request = para captar informação do HTML
#redirect


from flask import Flask ,render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


#Home
#@app.route('/index.html')
#def my_home():
#    return render_template('./index.html')

#Work
#@app.route('/works.html')
#def works():
#    return render_template('./works.html')

#about
#@app.route('/about.html')
#def aboute_me():
#    return render_template('./about.html')

#Contacto
#@app.route('/contact.html')
#def contact():
#    return render_template('./contact.html')

#Components
#@app.route('/components.html')
#def Components():
#    return render_template('./components.html')


#Home
@app.route('/')
def my_home():
    return render_template('./index.html')

#MELHOR FORMA
@app.route('/<string:page_name>')
def html_Page(page_name):
    return render_template(page_name)

def write_to_file(data):
    #Atenção ao caminho
    with open('./venv/database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

#database para ficheiros excell
#delimiter = separado por , (as virgulas são o que criam diferentes colunas)
#
def write_to_cvs(data):
    #Atenção ao caminho
    with open('./venv/database.csv', mode='a', newline='\n') as database2:
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
        
            #write_to_file(data)
            write_to_cvs(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Algo nao está bem'