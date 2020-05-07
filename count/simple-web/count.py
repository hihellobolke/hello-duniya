#!/usr/bin/env python
import os
import re
from flask import Flask, request, jsonify, render_template

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length




app = Flask(__name__)
app.config['SECRET_KEY'] = 'HelloWorld'
app.config['WTF_CSRF_ENABLED'] = False


def get_count(fp, search_string, logger=None):
    c = 0
    for line in fp:
        if re.search(search_string, line.decode("utf-8")):
            c += 1
            if logger:
                logger.debug("{} => {}".format(c, line.strip()))
    return c


class UploadForm(FlaskForm):
    search = StringField('String to search', [DataRequired(), Length(max=25)])
    log = FileField("Text file", validators=[FileRequired()])
    submit = SubmitField('Upload')


@app.route('/', methods=['GET', 'POST'])
def search():
    result = {
        "filename": "",
        "count": 0,
        "search": ""
    }
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        file_data = form.log.data
        search_data = form.search.data
        result["filename"] = file_data.filename
        result["search"] = search_data
        result["count"] = get_count(file_data, search_string=search_data)
        return jsonify(result)
    return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run()