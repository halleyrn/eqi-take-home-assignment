from flask import Flask,  request, render_template
from werkzeug.utils import secure_filename
from validation import is_csv, is_10_rows, is_3_columns, is_dataframe_complete
from file_utils import read_csv_into_df


app = Flask(__name__)


@app.route('/')
def upload_file():
    """ Renders index.html on main page
    """
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    """ Saves file that was selected, if file is a CSV, to working 
    directory
    """
    if request.method == 'POST':
        f = request.files['file']
        # print(f)
        filename = secure_filename(f.filename)
        print(filename)
        errors = []
        # check if file is a CSV
        if not is_csv(filename):
            return 'File is not CSV.'
        f.save(filename)
        df = read_csv_into_df(filename)
        # check the contents of the CSV
        if not is_10_rows(df):
            errors += ['There are not 10 rows in the CSV.']
        if not is_3_columns(df):
            errors += ['There are not 3 columns in the CSV.']
        if not is_dataframe_complete(df):
            errors += ['The data is not complete.']
        if len(errors):
            return '\n'.join(errors)
        return 'Success!'


if __name__ == "__main__":
    # run development server
    app.run(host="0.0.0.0", port=8080, debug=True)
