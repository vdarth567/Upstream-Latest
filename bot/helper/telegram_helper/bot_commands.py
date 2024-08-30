from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand = "pstart"
        self.MirrorCommand = [
            f"pmirror{CMD_SUFFIX}",
            f"pm{CMD_SUFFIX}",
        ]
        self.QbMirrorCommand = [
            f"pqbmirror{CMD_SUFFIX}",
            f"pqbm{CMD_SUFFIX}",
        ]
        self.YtdlCommand = [
            f"pytdlm{CMD_SUFFIX}",
            f"pytm{CMD_SUFFIX}",
        ]
        self.LeechCommand = [
            f"pleech{CMD_SUFFIX}",
            f"pl{CMD_SUFFIX}",
        ]
        self.QbLeechCommand = [
            f"pqbleech{CMD_SUFFIX}",
            f"pqbl{CMD_SUFFIX}",
        ]
        self.YtdlLeechCommand = [
            f"pytdlleech{CMD_SUFFIX}",
            f"pytl{CMD_SUFFIX}",
        ]
        self.CloneCommand = f"clone{CMD_SUFFIX}"
        self.CountCommand = f"count{CMD_SUFFIX}"
        self.DeleteCommand = f"del{CMD_SUFFIX}"
        self.CancelTaskCommand = [
            f"abort{CMD_SUFFIX}",
            f"A{CMD_SUFFIX}",
        ]
        self.CancelAllCommand = f"pcancelall{CMD_SUFFIX}"
        self.ForceStartCommand = [
            f"forcestart{CMD_SUFFIX}",
            f"fs{CMD_SUFFIX}",
        ]
        self.ListCommand = f"plist{CMD_SUFFIX}"
        self.SearchCommand = f"search{CMD_SUFFIX}"
        self.StatusCommand = [
            f"pstatus{CMD_SUFFIX}",
            "sall",
        ]
        self.UsersCommand = f"users{CMD_SUFFIX}"
        self.AuthorizeCommand = f"pauthorize{CMD_SUFFIX}"
        self.UnAuthorizeCommand = f"punauthorize{CMD_SUFFIX}"
        self.AddSudoCommand = f"addsudo{CMD_SUFFIX}"
        self.RmSudoCommand = f"rmsudo{CMD_SUFFIX}"
        self.PingCommand = [
            f"ping{CMD_SUFFIX}",
            "p",
        ]
        self.RestartCommand = f"restart{CMD_SUFFIX}"
        self.StatsCommand = [
            f"pstats{CMD_SUFFIX}",
            "s",
        ]
        self.HelpCommand = f"phelp{CMD_SUFFIX}"
        self.LogCommand = f"plog{CMD_SUFFIX}"
        self.ShellCommand = f"shell{CMD_SUFFIX}"
        self.AExecCommand = f"aexec{CMD_SUFFIX}"
        self.ExecCommand = f"exec{CMD_SUFFIX}"
        self.ClearLocalsCommand = f"clearlocals{CMD_SUFFIX}"
        self.BotSetCommand = [
            f"pbsetting{CMD_SUFFIX}",
            f"pbset{CMD_SUFFIX}",
            f"pbs{CMD_SUFFIX}",
        ]
        self.UserSetCommand = [
            f"pusetting{CMD_SUFFIX}",
            f"puset{CMD_SUFFIX}",
            f"pus{CMD_SUFFIX}",
        ]
        self.SelectCommand = f"sel{CMD_SUFFIX}"
        self.RssCommand = f"rss{CMD_SUFFIX}"
        self.RmdbCommand = f"rmdb{CMD_SUFFIX}"
        self.RmalltokensCommand = f"rmat{CMD_SUFFIX}"


BotCommands = _BotCommands()
