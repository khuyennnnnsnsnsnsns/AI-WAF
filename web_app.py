from flask import Flask, request, render_template_string, abort
import requests

app = Flask(__name__)
AI_URL = "http://localhost:8000/predict"


HTML_TEMPLATE = """
<h1>Demo AI-WAF Protection</h1>
<form method="GET">
    Nhập nội dung tìm kiếm: <input type="text" name="search">
    <input type="submit" value="Gửi">
</form>
<p>Kết quả: {{ result }}</p>
"""

@app.before_request
def waf_check():
    # Kiểm tra tất cả các tham số trong URL (query string)
    for key, value in request.args.items():
        try:
            res = requests.post(AI_URL, json={"sentence": value}, timeout=1)
            if res.json().get("is_attack") == 1:
                return f"<h1>403 Forbidden</h1><p>AI-WAF đã chặn request chứa mã độc: <b>{value}</b></p>", 403
        except Exception as e:
            print(f"Lỗi kết nối AI Service: {e}")

@app.route('/')
def index():
    search_query = request.args.get('search', 'Trống')
    return render_template_string(HTML_TEMPLATE, result=search_query)

if __name__ == "__main__":
    app.run(port=5000)
