import os
class Commands:
    LEECH = os.environ.get("LEECH_CMD")
    PURGE = os.environ.get("PURGE_CMD")
    PAUSEALL = os.environ.get("PAUSEALL_CMD")
    RESUMEALL = os.environ.get("RESUMEALL_CMD")
    STATUS = os.environ.get("STATUS_CMD")
    SETTINGS = os.environ.get("SETTINGS_CMD")
    EXEC = os.environ.get("EXEC_CMD")
    UPLOAD = os.environ.get("UPLOAD_CMD")
    YTDL = os.environ.get("YTDL_CMD")
    PYTDL = os.environ.get("PYTDL_CMD")
    ABOUT = os.environ.get("ABOUT_CMD")
    GETLOGS = os.environ.get("GETLOGS_CMD")
    SERVER = os.environ.get("SERVER_CMD")
    USERSETTINGS = os.environ.get("USERSETTINGS_CMD")
    INSTADL = "instadl"
    START = "start"
    USTATUS = "ustatus"
    SETTHUMB = "setthumb"
    CLRTHUMB = "clearthumb"
    SPEEDTEST = "speedtest"