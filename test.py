from flask import Flask, request, abort, jsonify, render_template
from datetime import datetime
import os
import json
import tempfile
import subprocess
import time
import re
from urllib.parse import urlparse
import base64

import globals
import common
from dbconnector import dbconnector
from dbconnector import dbcursor

# 設定ファイル読み込み・globals初期化
app = Flask(__name__)
app.config.from_envvar('CONFIG_API_TEKTON_PATH')
globals.init(app)
AAA = "xXxxxxxxxxxx"
aaaa = "11"
user = "administrator"
password = "abcdefg1111"

