from flask import Flask, render_template, request, session
from content.explaination import ContentAgent
from content.quizmaker import QuizAgent
from dotenv import load_dotenv
import json, os

load_dotenv()

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.secret_key = os.getenv("SECRET_KEY")
app.debug = True

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/explain', methods=['GET', 'POST'])
def explain():
    if request.method == 'POST':
        topic = request.form.get('topic', None)
        if topic != session.get('topic', None):
            session['topic'] = topic
            session['explaination'] = None
            session['facts'] = None
            session['summary'] = None
            session['links'] = None
            session['content'] = None
            session['quiz'] = None
            session['error'] = False
            session.modified = True

        if session.get('error', False):
            return render_template("error.html")

        agent = ContentAgent(topic)
        try:
            explaination = agent.get_explaination()
            facts = agent.get_facts()
            summary = agent.get_summary()
            links = agent.get_links()
            content = agent.get_content()

            session['explaination'] = explaination
            session['facts'] = facts
            session['summary'] = summary
            session['links'] = links
            session['content'] = content

            quiz_agent = QuizAgent(topic, content)
            quiz = quiz_agent.get_quiz()
            if isinstance(quiz, str):
                try:
                    quiz = json.loads(quiz)
                except json.JSONDecodeError:
                    session['error'] = True
                    session.modified = True
                    return render_template("error.html")
            session['quiz'] = quiz
        except ValueError:
            # session['error'] = True
            # session.modified = True
            return render_template("error.html")

    topic = session.get('topic', None)
    explaination = session.get('explaination', None)
    facts = session.get('facts', None)
    summary = session.get('summary', None)
    links = session.get('links', None)

    if session.get('error', False):
        return render_template("error.html")

    return render_template("explain.html", topic=topic, explaination=explaination, facts=facts, summary=summary, links=links)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    topic = session.get('topic', None)
    quiz = session.get('quiz', None)

    if quiz is None:
        return render_template("error.html")

    if session.get('error', False):
        return render_template("error.html")

    return render_template("quiz.html", topic=topic, quiz=quiz)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))