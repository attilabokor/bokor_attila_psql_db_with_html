import select_queries
from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def list_questions():
    return render_template('link_homework.html')


@app.route('/mentors', methods=['GET'])
def sql_list_1():
    questions_table = select_queries.question_1()
    form_action = '/'
    button_caption = 'Back to index'
    return render_template('list_homework.html',
                           form_action=form_action,
                           questions=questions_table,
                           button_caption=button_caption
                           )


@app.route('/all-school', methods=['GET'])
def sql_list_2():
    questions_table = select_queries.question_2()
    form_action = '/'
    button_caption = 'Back to index'
    return render_template('list_homework.html',
                           form_action=form_action,
                           questions=questions_table,
                           button_caption=button_caption
                           )


@app.route('/mentors-by-country', methods=['GET'])
def sql_list_3():
    questions_table = select_queries.question_3()
    form_action = '/'
    button_caption = 'Back to index'
    return render_template('list_homework.html',
                           form_action=form_action,
                           questions=questions_table,
                           button_caption=button_caption
                           )


@app.route('/contacts', methods=['GET'])
def sql_list_4():
    questions_table = select_queries.question_4()
    form_action = '/'
    button_caption = 'Back to index'
    return render_template('list_homework.html',
                           form_action=form_action,
                           questions=questions_table,
                           button_caption=button_caption
                           )


@app.route('/applicants', methods=['GET'])
def sql_list_5():
    questions_table = select_queries.question_5()
    form_action = '/'
    button_caption = 'Back to index'
    return render_template('list_homework.html',
                           form_action=form_action,
                           questions=questions_table,
                           button_caption=button_caption
                           )


@app.route('/applicants-and-mentors', methods=['GET'])
def sql_list_6():
    questions_table = select_queries.question_6()
    form_action = '/'
    button_caption = 'Back to index'
    return render_template('list_homework.html',
                           form_action=form_action,
                           questions=questions_table,
                           button_caption=button_caption
                           )                                                                                                            


if __name__ == '__main__':
    app.run(debug=True)
