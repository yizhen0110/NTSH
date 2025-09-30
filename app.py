from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store questions and answers in a simple list for demonstration purposes
questions_answers = [
    {"question": "班上什麼時候舉辦運動會？", "answer": "運動會將於下個月舉行。"},
    {"question": "李美芳老師喜歡教什麼科目？", "answer": "李老師喜歡教數學和科學。"}
]

@app.route('/')
def index():
    return render_template('index.html', questions_answers=questions_answers)

@app.route('/ask', methods=['GET', 'POST'])
def quiz_question():
    if request.method == 'POST':
        question = request.form['question']
        
        # Add a placeholder answer for simplicity; you can expand this later
        answer = "回答將稍後提供。"
        questions_answers.append({"question": question, "answer": answer})
        
        return redirect('/')
    
    # Render the ask.html template when the user visits the page
    return render_template('ask.html')

@app.route('/ask', methods=['GET', 'POST'])
def quiz_question():
    if request.method == 'POST':
        question = request.form['question']
        
        # Add a placeholder answer for simplicity; you can expand this later
        answer = "回答將稍後提供。"
        questions_answers.append({"question": question, "answer": answer})
        
        return redirect('/')
    
    # Render the ask.html template when the user visits the page
    return render_template('quiz.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

