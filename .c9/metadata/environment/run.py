{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":13,"column":20},"end":{"row":51,"column":23},"action":"remove","lines":["","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        flash(\"Thanks {}, we have received your message\".format(","            request.form[\"name\"]","        ))","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","","            debug=True)"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":13,"column":20},"action":"remove","lines":["import os","import json","from flask import Flask, render_template, request, flash","","app = Flask(__name__)","app.secret_key = 'some_secret'","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":51,"column":23},"action":"insert","lines":["import os","import json","from flask import Flask, render_template, request, flash","","app = Flask(__name__)","app.secret_key = 'some_secret'","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        flash(\"Thanks {}, we have received your message\".format(","            request.form[\"name\"]","        ))","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","","            debug=True)"],"id":4}],[{"start":{"row":51,"column":23},"end":{"row":102,"column":23},"action":"insert","lines":["import os","import json","from flask import Flask, render_template, request, flash","","app = Flask(__name__)","app.secret_key = 'some_secret'","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        flash(\"Thanks {}, we have received your message\".format(","            request.form[\"name\"]","        ))","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","","            debug=True)"],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":102,"column":23},"action":"remove","lines":["import os","import json","from flask import Flask, render_template, request, flash","","app = Flask(__name__)","app.secret_key = 'some_secret'","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        flash(\"Thanks {}, we have received your message\".format(","            request.form[\"name\"]","        ))","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","","            debug=True)import os","import json","from flask import Flask, render_template, request, flash","","app = Flask(__name__)","app.secret_key = 'some_secret'","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        flash(\"Thanks {}, we have received your message\".format(","            request.form[\"name\"]","        ))","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","","            debug=True)"],"id":6}],[{"start":{"row":0,"column":0},"end":{"row":51,"column":23},"action":"insert","lines":["import os","import json","from flask import Flask, render_template, request, flash","","app = Flask(__name__)","app.secret_key = 'some_secret'","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        flash(\"Thanks {}, we have received your message\".format(","            request.form[\"name\"]","        ))","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","","            debug=True)"],"id":7}],[{"start":{"row":50,"column":0},"end":{"row":50,"column":1},"action":"insert","lines":[" "],"id":8},{"start":{"row":50,"column":1},"end":{"row":50,"column":2},"action":"insert","lines":[" "]},{"start":{"row":50,"column":2},"end":{"row":50,"column":3},"action":"insert","lines":[" "]},{"start":{"row":50,"column":3},"end":{"row":50,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":38},"action":"insert","lines":[" port=int(os.environ.get('PORT')),"],"id":9}],[{"start":{"row":51,"column":5},"end":{"row":51,"column":12},"action":"remove","lines":["       "],"id":10}],[{"start":{"row":50,"column":35},"end":{"row":50,"column":36},"action":"remove","lines":[")"],"id":11}],[{"start":{"row":50,"column":35},"end":{"row":50,"column":36},"action":"insert","lines":[")"],"id":12}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":38},"action":"remove","lines":[" port=int(os.environ.get('PORT')),"],"id":13}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":38},"action":"insert","lines":[" port=int(os.environ.get('PORT')),"],"id":14}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":38},"action":"remove","lines":[" port=int(os.environ.get('PORT')),"],"id":15}]]},"ace":{"folds":[],"scrolltop":541,"scrollleft":0,"selection":{"start":{"row":51,"column":16},"end":{"row":51,"column":16},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":27,"state":"start","mode":"ace/mode/python"}},"timestamp":1565730854114,"hash":"4d7d042a6ba98939205ddf24976c4e25de0687df"}