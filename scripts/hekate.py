from basemodule import BaseModule


class Hekate(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "eradicatinglove",
                "reponame": "TheOtherSide",
                "assetPatterns": [".*TheOtherSide.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)
