import os
print("FILES IN FOLDER:", os.listdir())

from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

app = Flask(__name__)

# ================= GOOGLE SHEET SETUP =================
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

SHEET_ID = "1FmXqroQN2IYzGbwEKj2V01oJAFjhilYzvpiXuLODqPU"
sheet = client.open_by_key(SHEET_ID).sheet1


# ================= FORM =================
@app.route('/')
def form():
    return '''
    <h2>Data Entry Form</h2>
    <form method="POST" action="/submit">
        State/UT: <input type="text" name="state"><br><br>
        Year: <input type="text" name="year"><br><br>
        Component: <input type="text" name="component"><br><br>

        Recurring (Central): <input type="number" name="rec_central"><br><br>
        Recurring (State): <input type="number" name="rec_state"><br><br>
        Non-Recurring (Central): <input type="number" name="nonrec_central"><br><br>
        Non-Recurring (State): <input type="number" name="nonrec_state"><br><br>

        Remarks: <input type="text" name="remarks"><br><br>

        <input type="submit" value="Submit">
    </form>

    <br><br>
    <a href="/final_report">📊 View Report</a>
    '''


# ================= SAVE =================
@app.route('/submit', methods=['POST'])
def submit():
    data = [
        request.form.get('state'),
        request.form.get('year'),
        request.form.get('component'),
        request.form.get('rec_central'),
        request.form.get('rec_state'),
        request.form.get('nonrec_central'),
        request.form.get('nonrec_state'),
        request.form.get('remarks')
    ]

    sheet.append_row(data)

    return '''
    <h3>✅ Data Saved Successfully!</h3>
    <a href="/">⬅ Back</a>
    '''


# ================= HEALTH =================
@app.route('/health')
def health():
    return "OK", 200


# ================= REPORT =================
@app.route('/final_report')
def final_report():

    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    if df.empty:
        return "No data found!"

    # Rename columns (IMPORTANT)
    df.columns = [
        'State', 'Year', 'Component',
        'Rec_Central', 'Rec_State',
        'NonRec_Central', 'NonRec_State',
        'Remarks'
    ]

    # Convert numbers
    cols = ['Rec_Central', 'Rec_State', 'NonRec_Central', 'NonRec_State']
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    df['Total'] = df[cols].sum(axis=1)

    # ================= FORMAT 1 =================
    format1 = df.groupby(['Year', 'Component'])['Total'].sum().unstack(fill_value=0)
    format1['Total'] = format1.sum(axis=1)

    grand_total = format1.sum()

    html = "<h1>📊 Reporting Format – I (Rs. in Lakhs)</h1>"
    html += format1.to_html(border=1)

    html += "<h3>Grand Total</h3>"
    html += grand_total.to_frame(name="Total").to_html(border=1)

    # ================= FORMAT 2 =================
    html += "<h1>📊 Reporting Format – II</h1>"

    years = df['Year'].unique()

    for year in years:
        year_df = df[df['Year'] == year]

        grp = year_df.groupby('Component')[cols].sum()
        grp['Total'] = grp.sum(axis=1)

        total_row = grp.sum().to_frame(name="Total").T

        html += f"<h2>{year}</h2>"
        html += grp.to_html(border=1)
        html += "<b>Total</b>"
        html += total_row.to_html(border=1)

    return html


# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)