# [ringcentral-chatbot-server](https://github.com/zxdong262/ringcentral-chatbot-server-python)

CLI tool to run ringcentral bot powered by [ringcentral_bot_framework](https://github.com/zxdong262/ringcentral-chatbot-python).

## Use

```bash
pip3 install ringcentral_chatbot_server
rcs bot.py
```

## Dev

```bash
virtualenv venv --python=python3
source ./venv/bin/activate
pip install -r requirements.txt
pip install pylint ringcentral_bot_framework twine
cp .sample.env .env
# then fill RINGCENTRAL_BOT_CLIENT_ID and RINGCENTRAL_BOT_CLIENT_SECRET at least

# test
pip install .
rcs bot.py
```

## License

MIT
