from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1747534
    API_HASH = "5a2684512006853f2e48aca9652d83ea"
    # the name to display in your alive message
    ALIVE_NAME = "Rizz Store"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://qxouwfwi:c5f9NDngtWs-nQnV2nDUwi2s1FegJ99u@dumbo.db.elephantsql.com/qxouwfwi"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOH0Bu6m65U0UsnIfzLXc2drZ3DmAaU_FyzfDIrcmPln_ee-0G0Hv9pQwunA3rG1BDbIbonLMBel0LQEEmewW1xKQ2X-PK0WIq1A9QwlRuf42TNng1mclTyWsGNBGeCZ4vVFiOq5KfvbSqCpMFpKEzx47di-abctRM6do88fmMEErmbo6qnG8mJcIKVpHpRz8vZACQZMC-P7th7FJIsziR2RFyVFaQ_8DSiiYZSFdEwx-cbH8uqz_umZcYl8aBqn9zZi96bVnikzt8lEDKBu8F8p0kUqh7xay11WvxfphL4ihFk6ZUPDmzKjnJ1cQNDhKspdArjVb2u9p4Q_D84nmaJoOLa0="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5309338630:AAGLzn8Tpo5eiCJSXZeecUfKH3mojhfg8mg"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001977801733
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
