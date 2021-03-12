class User:
    def __init__(self,mod_status,username,reputation,banned):
        self.mod_status=mod_status
        self.username=username
        self.reputation=reputation
        self.banned = banned

        def upvote_thread(self,thread,time_voted):
            vote=Vote(up=true,voter= self.username,thread=thread)
            return vote


class Vote:
    def __init__(self,up,time_voted, voter,thread):
        self.up = up
        self.voter = voter
        self.time_voted = time_voted
        self.thread = thread
    def delete(self):
        self.is_deleted=True
class Thread:
    def __init__(self,title,parent_thread,upvote_count,downvote_count, comments):
        self.title = title
        self.parent_thread = parent_thread
        self.upvote_count = 0
        self.downvote_count = 0
        self.comments = []


