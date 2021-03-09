from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

news_items = {
    1: {'id': 1,
        'title': 'Covide 19 update',
        'body': 'This is a news on Covid 19'},
    2: {'id': 2,
        'title': 'Python 4',
        'body': 'Python 4 is coming'},
    3: {'id': 3,
        'title': 'Shabu',
        'body': 'Shabu is very delicous'},
}


@ app.route("/")
def hello():
    name = 'Arm'
    time = datetime.now()
    print(news_items.values())
    return render_template('index.html', name=name, time=time, news_items=news_items.values())

@app.route('/news/<id>/')
def show_news_item(id):
        news_item = news_items[int(id)]
        return render_template('news_item.html', 
                                id=news_item['id'],
                                title=news_item['title'],
                                body=news_item['body'])

                               
if __name__ == "__main__":
    app.run(debug=True)


