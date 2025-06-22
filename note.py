from datetime import datetime

class Note:
    def __init__(self, title, content, date=None, time=None):
        self.title = title
        self.content = content
        now = datetime.now()
        self.date = date if date else now.strftime("%Y-%m-%d")
        self.time = time if time else now.strftime("%H:%M")

    def __str__(self):
        return f"[{self.date} {self.time}] {self.title}: {self.content}"



    
        