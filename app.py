from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model, preprocessor, and label encoder
model = joblib.load('Resources/decision_tree_model.pkl')
preprocessor = joblib.load('Resources/preprocessor.pkl')
label_encoder = joblib.load('Resources/label_encoder.pkl')
final_df = pd.read_csv('Resources/final_df.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.is_json:
        selected_country = request.json.get('country')
        X_country = final_df[final_df['country_origin'] == selected_country]
        X_country_processed = preprocessor.transform(X_country)
        y_pred = model.predict(X_country_processed)
        prediction = label_encoder.inverse_transform([y_pred[0]])[0]
        return jsonify(prediction=prediction)

    countries = final_df['country_origin'].unique()
    return render_template('index.html', countries=countries)


if __name__ == '__main__':
    app.run(debug=True)
