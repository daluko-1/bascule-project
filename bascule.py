from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Main Routes ---
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Handle file upload or form data here
        # Example: file = request.files['file']
        return redirect(url_for("analysis_result"))
    return render_template("upload.html")

@app.route("/claims")
def claims():
    return render_template("flagged-claims.html")

@app.route("/review")
def review():
    return render_template("agent-feedback.html")

@app.route("/edit-claim/<int:claim_id>")
def edit_claim(claim_id):
    # Pass claim_id into the template for context
    return render_template("edit-claim.html", claim_id=claim_id)

@app.route("/manual-review")
def manual_review():
    return render_template("manual-review.html")

@app.route("/search")
def search_filter():
    return render_template("search-filter.html")

@app.route("/analysis-result")
def analysis_result():
    return render_template("analysis-result.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

# --- Run App ---
if __name__ == "__main__":
    app.run(debug=True)
