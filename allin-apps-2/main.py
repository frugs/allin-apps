from leaderboarddata import app as leaderboard_data_app
from leaderboardweb import app as leaderboard_web_app
import werkzeug.wsgi
import werkzeug.serving
import werkzeug.wrappers

app = werkzeug.wsgi.DispatcherMiddleware(
    werkzeug.wrappers.Response("Nothing to see here!", status=404),
    mounts={
        "/leaderboard_data": leaderboard_data_app,
        "/leaderboard": leaderboard_web_app,
    })


def main():
    werkzeug.serving.run_simple("127.0.0.1", 37696, app, use_reloader=True, use_debugger=True, threaded=True)


if __name__ == "__main__":
    main()
