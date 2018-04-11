import logging

from kalliope.core.Utils import Utils
from kalliope.core.HookManager import HookManager
from kalliope.core.ConfigurationManager import SettingLoader

logging.basicConfig()
logger = logging.getLogger("kalliope")


class SettingEditor(object):
    """This class provides methods/functions to update properties from the Settings"""

    @staticmethod
    def set_mute_status(mute=False):
        """
        Define is the mute status
        :param mute: Boolean. If false, Kalliope is voice is stopped
        """
        logger.debug("[SettingEditor] mute. Switch trigger process to mute : %s" % mute)
        settings = SettingLoader().settings
        if mute:
            Utils.print_info("Kalliope now muted, voice has been stopped.")
            HookManager.on_mute()
        else:
            Utils.print_info("Kalliope now speaking.")
            HookManager.on_unmute()
        settings.options["mute"] = mute

    @staticmethod
    def set_deaf_status(trigger_instance, deaf=False):
        """
        Define is the trigger is listening or not.
        :param trigger_instance: the trigger instance coming from the order. It will be paused or unpaused.
        :param deaf: Boolean. If true, kalliope is trigger is paused
        """
        logger.debug("[MainController] deaf . Switch trigger process to deaf : %s" % deaf)
        settings = SettingLoader().settings
        if deaf:
            trigger_instance.pause()
            Utils.print_info("Kalliope now deaf, trigger has been paused")
            HookManager.on_deaf()
        else:
            trigger_instance.unpause()
            Utils.print_info("Kalliope now listening for trigger detection")
            HookManager.on_undeaf()
        settings.options["deaf"] = deaf