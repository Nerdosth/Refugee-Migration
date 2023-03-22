import pandas as pd
import joblib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the saved model, preprocessor, and label encoder
best_model = joblib.load("decision_tree_model.pkl")
preprocessor = joblib.load("saved_preprocessor.pkl")
le = joblib.load("saved_label_encoder.pkl")

# Load your DataFrame (assuming it's saved as a CSV file)
final_df = pd.read_csv("Resources/final_df.csv")


@app.route("/")
def index():
    countries = sorted(final_df['country_origin'].unique().tolist())
    return render_template("index.html", countries=countries)


def your_machine_learning_model(country):
    X_country = final_df[final_df['country_origin'] == country]
    X_country_processed = preprocessor.transform(X_country)
    y_pred = best_model.predict(X_country_processed)
    y_pred_country = le.inverse_transform([y_pred[0]])

    return y_pred_country[0]


@app.route("/api/calculate-destination", methods=["POST"])
def calculate_destination():
    data = request.get_json()
    country = data["country"]
    destination_country = your_machine_learning_model(country)
    return jsonify({"country_of_destination": destination_country})


if __name__ == "__main__":
    app.run(debug=True)
