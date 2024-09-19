import re

def main():
    print(create_yt_link(parse_html(input("HTML: "))))

def parse_html(html):
    if match := re.search(r"\"(?:https?://)?(?:www\.)?youtube\.com/embed/(.+)\"", html, re.IGNORECASE):
        yt_id = match.group(1)
        return yt_id.replace("\"", "")
    
def create_yt_link(yt_id):
    yt_link = ("https://www.youtu.be/" + yt_id)
    return yt_link

if __name__ == "__main__":
    main()
