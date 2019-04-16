from zergmacroplot import app as zerg_macro_app
from terranproduction import app as terran_production_app
from leaderboarddata import app as leaderboard_data_app
from leaderboardweb import app as leaderboard_web_app
from allinsso import app as sso_app
from allinusersettings import app as usersettings_app
from ladderinfo import app as ladderinfo_app
from bnetprofile import app as bnetprofile_app
from allintrophy import app as trophy_app
import werkzeug.wsgi
import werkzeug.serving
import werkzeug.wrappers

app = werkzeug.wsgi.DispatcherMiddleware(
    werkzeug.wrappers.Response("Nothing to see here!", status=404),
    mounts={
        "/zergmacro": zerg_macro_app,
        "/terranproduction": terran_production_app,
        "/sso": sso_app,
        "/usersettings": usersettings_app,
        "/ladderinfo": ladderinfo_app,
        "/bnetprofile": bnetprofile_app,
        "/trophy": trophy_app,
    })


def main():
    werkzeug.serving.run_simple("127.0.0.1", 37696, app, use_reloader=True, use_debugger=True, threaded=True)


if __name__ == "__main__":
    main()
