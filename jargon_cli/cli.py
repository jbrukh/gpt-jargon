import os

class JargonCli:

    def __init__(self, jargon_dir=os.path.expanduser('~/.jargon')):
        self.jargdir = jargon_dir
        self.__ensure_jargdir()

    def __ensure_jargdir(self):
        """
        Creates `self.jargdir` if it doesn't already exist.
        """
        if not os.path.exists(self.jargdir):
            os.makedirs(self.jargdir)
    
    def ls(self):
        for file in os.listdir(self.jargdir):
            if file.endswith(".jarg"):
                yield file
