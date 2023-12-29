import os
from flask import Flask, request


#you need to specify your request password
request_password="tangpeng@gitee-inula"


def github_trigger(request):
    try:
        password = request.headers.get("X-Gitee-Token")
        hook_name = request.headers.get("X-Gitee-Event")
        if password != request_password:
            return '401 Unauthorized', 401, {}
        if hook_name != "push_hooks" and hook_name != "Push Hook" and hook_name != "Tag Push Hook":
            return '403 Unauthorized Action', 403, {}
        print("get request from gitee: ", hook_name)
        os.system('./trigger.sh')
        return 'ok'

    except Exception as e:
        print(e)
        return '400 Bad Request', 400, {}
        

app = Flask(__name__)

@app.route('/', methods=["POST"])
def gitee_webhook():
    return github_trigger(request)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
