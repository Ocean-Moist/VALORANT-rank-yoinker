from colr import color

from src.constants import tierDict


class Colors:
    def __init__(self, hide_names, agent_dict, AGENTCOLORLIST):
        self.hide_names = hide_names
        self.agent_dict = agent_dict
        self.tier_dict = tierDict
        self.AGENTCOLORLIST = AGENTCOLORLIST

    @staticmethod
    def get_color_from_team(team, name, playerPuuid, selfPuuid):
        orig_name = name
        if team == 'Red':
            Teamcolor = color(orig_name, fore=(238, 77, 77))
        elif team == 'Blue':
            Teamcolor = color(orig_name, fore=(76, 151, 237))
        else:
            Teamcolor = ''
        if playerPuuid == selfPuuid:
            Teamcolor = color(orig_name, fore=(221, 224, 41))
        return Teamcolor

    def get_rgb_color_from_skin(self, skin_id, valoApiSkins):
        for skin in valoApiSkins.json()["data"]:
            if skin_id == skin["uuid"]:
                return self.tier_dict[skin["contentTierUuid"]]

    @staticmethod
    def level_to_color(level):
        if level >= 400:
            return color(level, fore=(0, 255, 255))
        elif level >= 300:
            return color(level, fore=(255, 255, 0))
        elif level >= 200:
            return color(level, fore=(0, 0, 255))
        elif level >= 100:
            return color(level, fore=(241, 144, 54))
        elif level < 100:
            return color(level, fore=(211, 211, 211))

    def get_agent_from_uuid(self, agentUUID):
        agent = str(self.agent_dict.get(agentUUID))
        if self.AGENTCOLORLIST.get(agent.lower()) is not None:
            agent_color = self.AGENTCOLORLIST.get(agent.lower())
            return color(agent, fore=agent_color)
        else:
            return agent
