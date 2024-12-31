from flask import Flask, jsonify, render_template, request

import analyzers.cpp_analyzer as cpp_analyzer
import analyzers.css_analyzer as css_analyzer
import analyzers.html_analyzer as html_analyzer
import analyzers.java_analyzer as java_analyzer
import analyzers.js_analyzer as js_analyzer
import analyzers.python_analyzer as python_analyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_code():
    # Handle both form data and JSON input
    if request.is_json:
        data = request.get_json()
        code = data.get('code')
        language = data.get('language')
    else:
        code = request.form['code']
        language = request.form['language']

    # Map language to corresponding analyzer
    analyzers = {
        'Python': python_analyzer.analyze,
        'JavaScript': js_analyzer.analyze,
        'HTML': html_analyzer.analyze,
        'CSS': css_analyzer.analyze,
        'Java': java_analyzer.analyze,
        'C++': cpp_analyzer.analyze
    }

    if language in analyzers:
        results = analyzers[language](code)
        return jsonify({"vulnerabilities": results})
    else:
        return jsonify({"error": "Unsupported language"}), 400

if __name__ == '__main__':
    app.run(debug=True)
