from zergmacroplot import app as zerg_macro_app
import werkzeug.wsgi
import werkzeug.serving
import werkzeug.wrappers

app = werkzeug.wsgi.DispatcherMiddleware(
    werkzeug.wrappers.Response("Nothing to see here!", status=404),
    mounts={
        "/zergmacro": zerg_macro_app
    })


def main():
    werkzeug.serving.run_simple("127.0.0.1", 37696, app, use_reloader=True, use_debugger=True)


if __name__ == "__main__":
    main()
