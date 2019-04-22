name = 'ringcentral_chatbot_server.cmd'
from flask import Flask, request
import pydash as _
from dotenv import load_dotenv
load_dotenv()
import os, sys
sys.path.append(
  os.getcwd()
)
from ringcentral_bot_framework import frameworkInit
from ringcentral_bot_framework.core.common import path_import

def cmd(botPath):
  conf = path_import('ringcentral_bot_framework.localConfig', botPath)
  framework = frameworkInit(conf, _.get(conf, 'extensions'))

  app = Flask('devtest')

  @app.route('/test', methods=['GET'])
  def index():
    return 'RingCentral bot dev server running'
  @app.route('/favicon.ico', methods=['GET'])
  def favicon():
    return ''

  @app.route('/<action>', methods=['GET', 'POST'])
  def act(action):
    event = framework.flaskRequestParser(request, action)
    response = framework.router(event)
    resp = response['body']
    headers = {}
    if 'headers' in response:
        headers = response['headers']
    return resp, response['statusCode'], headers

  port = 9898
  host = 'localhost'
  try:
    port = os.environ['PORT']
    host = os.environ['HOST']
  except:
    pass
  app.run(
    host=host,
    port=port,
    debug=True,
    load_dotenv=True
  )

