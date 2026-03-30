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
    <h3>Status of Utilization of Grants during the 15th and 16th Finance Commission Cycles</h3>
    <form method="POST" action="/submit">

        State/UT:
        <select name="state">

            <option value="">--Select State--</option>

            <option>Andhra Pradesh</option>
            <option>Arunachal Pradesh</option>
            <option>Assam</option>
            <option>Bihar</option>
            <option>Chhattisgarh</option>
            <option>Goa</option>
            <option>Gujarat</option>
            <option>Haryana</option>
            <option>Himachal Pradesh</option>
            <option>Jharkhand</option>
            <option>Karnataka</option>
            <option>Kerala</option>
            <option>Madhya Pradesh</option>
            <option>Maharashtra</option>
            <option>Manipur</option>
            <option>Meghalaya</option>
            <option>Mizoram</option>
            <option>Nagaland</option>
            <option>Odisha</option>
            <option>Punjab</option>
            <option>Rajasthan</option>
            <option>Sikkim</option>
            <option>Tamil Nadu</option>
            <option>Telangana</option>
            <option>Tripura</option>
            <option>Uttar Pradesh</option>
            <option>Uttarakhand</option>
            <option>West Bengal</option>

            <option>Andaman & Nicobar Islands</option>
            <option>Chandigarh</option>
            <option>Dadra & Nagar Haveli and Daman & Diu</option>
            <option>Delhi</option>
            <option>Jammu & Kashmir</option>
            <option>Ladakh</option>
            <option>Lakshadweep</option>
            <option>Puducherry</option>

        </select>
        <br><br>

        Year:
        <select name="year">
            <option value="">--Select Year--</option>
            <option>2020-21</option>
            <option>2021-22</option>
            <option>2022-23</option>
            <option>2023-24</option>
            <option>2024-25</option>
            <option>2025-26</option>
            <option>2026-27</option>
        </select>
        <br><br>

<h3>Component wise Utilization Details</h3>

<table border="1" cellpadding="6">

<tr>
    <th rowspan="3">S. No.</th>
    <th rowspan="3">Component</th>
    <th colspan="4">Central Share</th>
    <th colspan="4">State Share</th>
    <th colspan="2">Total</th>
    <th rowspan="3">Remarks</th>
</tr>

<tr>
    <th colspan="2">Utilization</th>
    <th colspan="2">Refund</th>
    <th colspan="2">Utilization</th>
    <th colspan="2">Refund</th>
    <th rowspan="2">Utilization</th>
    <th rowspan="2">Refund</th>
</tr>

<tr>
    <th>Recurring</th>
    <th>Non-Recurring</th>
    <th>Recurring</th>
    <th>Non-Recurring</th>

    <th>Recurring</th>
    <th>Non-Recurring</th>
    <th>Recurring</th>
    <th>Non-Recurring</th>
</tr>

<!-- ROW 1 -->
<tr>
<td>1</td>
<td>Ayush Services</td>

<td><input name="c1" type="number"></td>
<td><input name="c2" type="number"></td>
<td><input name="c3" type="number"></td>
<td><input name="c4" type="number"></td>

<td><input name="c5" type="number"></td>
<td><input name="c6" type="number"></td>
<td><input name="c7" type="number"></td>
<td><input name="c8" type="number"></td>

<td><input name="c9" type="number"></td>
<td><input name="c10" type="number"></td>

<td><input name="r1" type="text"></td>
</tr>

<!-- ROW 2 -->
<tr>
<td>2</td>
<td>Ayush Educational Institutions</td>

<td><input name="c11" type="number"></td>
<td><input name="c12" type="number"></td>
<td><input name="c13" type="number"></td>
<td><input name="c14" type="number"></td>

<td><input name="c15" type="number"></td>
<td><input name="c16" type="number"></td>
<td><input name="c17" type="number"></td>
<td><input name="c18" type="number"></td>

<td><input name="c19" type="number"></td>
<td><input name="c20" type="number"></td>

<td><input name="r2" type="text"></td>
</tr>

<!-- ROW 3 -->
<tr>
<td>3</td>
<td>Medicinal Plants</td>

<td><input name="c21" type="number"></td>
<td><input name="c22" type="number"></td>
<td><input name="c23" type="number"></td>
<td><input name="c24" type="number"></td>

<td><input name="c25" type="number"></td>
<td><input name="c26" type="number"></td>
<td><input name="c27" type="number"></td>
<td><input name="c28" type="number"></td>

<td><input name="c29" type="number"></td>
<td><input name="c30" type="number"></td>

<td><input name="r3" type="text"></td>
</tr>

<!-- ROW 4 -->
<tr>
<td>4</td>
<td>Quality Control of ASU & H Drugs</td>

<td><input name="c31" type="number"></td>
<td><input name="c32" type="number"></td>
<td><input name="c33" type="number"></td>
<td><input name="c34" type="number"></td>

<td><input name="c35" type="number"></td>
<td><input name="c36" type="number"></td>
<td><input name="c37" type="number"></td>
<td><input name="c38" type="number"></td>

<td><input name="c39" type="number"></td>
<td><input name="c40" type="number"></td>

<td><input name="r4" type="text"></td>
</tr>
<!-- ROW 5 -->
<tr>
<td>5</td>
<td>Flexi Pool</td>

<td><input name="c41" type="number"></td>
<td><input name="c42" type="number"></td>
<td><input name="c43" type="number"></td>
<td><input name="c44" type="number"></td>

<td><input name="c45" type="number"></td>
<td><input name="c46" type="number"></td>
<td><input name="c47" type="number"></td>
<td><input name="c48" type="number"></td>

<td><input name="c49" type="number"></td>
<td><input name="c50" type="number"></td>

<td><input name="r5" type="text"></td>
</tr>
<!-- ROW 6 -->
<tr>
<td>6</td>
<td>Admin Cost</td>

<td><input name="c51" type="number"></td>
<td><input name="c52" type="number"></td>
<td><input name="c53" type="number"></td>
<td><input name="c54" type="number"></td>

<td><input name="c55" type="number"></td>
<td><input name="c56" type="number"></td>
<td><input name="c57" type="number"></td>
<td><input name="c58" type="number"></td>

<td><input name="c59" type="number"></td>
<td><input name="c60" type="number"></td>

<td><input name="r6" type="text"></td>
</tr>
<tr>
<td colspan="2"><b>Total</b></td>
<td colspan="11"></td>
</tr>

</table>

        <br><br>

        Special Remarks:
        <input type="text" name="remarks">

        <br><br>
<br><br>

<h3>Budget head wise Comparison of Utilization Grant</h3>
<h4 style="text-align:right;">Rs. in Lakhs</h4>

<table border="1" cellpadding="6">

<tr>
    <th rowspan="2">S. No.</th>
    <th rowspan="2">Budget Head</th>

    <th colspan="3">Central Share</th>
    <th colspan="3">State Share</th>
    <th colspan="3">Total</th>

    <th rowspan="2">Remaining Unutilized Grant</th>
    <th rowspan="2">Remarks</th>
</tr>

<tr>
    <th>Released</th>
    <th>Utilization</th>
    <th>Refund</th>

    <th>Released</th>
    <th>Utilization</th>
    <th>Refund</th>

    <th>Released</th>
    <th>Utilization</th>
    <th>Refund</th>
</tr>

<!-- ROW 1 -->
<tr>
<td>1</td>
<td>Recurring</td>

<td><input name="b1" type="number"></td>
<td><input name="b2" type="number"></td>
<td><input name="b3" type="number"></td>

<td><input name="b4" type="number"></td>
<td><input name="b5" type="number"></td>
<td><input name="b6" type="number"></td>

<td><input name="b7" type="number"></td>
<td><input name="b8" type="number"></td>
<td><input name="b9" type="number"></td>

<td><input name="b10" type="number"></td>
<td><input name="b11" type="text"></td>
</tr>

<!-- ROW 2 -->
<tr>
<td>2</td>
<td>Non-Recurring</td>

<td><input name="b12" type="number"></td>
<td><input name="b13" type="number"></td>
<td><input name="b14" type="number"></td>

<td><input name="b15" type="number"></td>
<td><input name="b16" type="number"></td>
<td><input name="b17" type="number"></td>

<td><input name="b18" type="number"></td>
<td><input name="b19" type="number"></td>
<td><input name="b20" type="number"></td>

<td><input name="b21" type="number"></td>
<td><input name="b22" type="text"></td>
</tr>

<!-- TOTAL -->
<tr>
<td colspan="2"><b>Total</b></td>
<td colspan="11"></td>
</tr>

</table>

<br>

<p>
• This represents the total grant released during the year, for which States/UTs are required to report the actual utilization. The utilization will be mapped against the approved components, and any unutilized grant should also be reported.
</p>

        <input type="submit" value="Submit">
    </form>

    <br><br>
    <a href="/final_report">📊 View Report</a>
    '''


# ================= SAVE =================
@app.route('/submit', methods=['POST'])
def submit():
    data = list(request.form.values())

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
    # df.columns = [...]

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
    app.run()