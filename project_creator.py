import requests


def check_repo(username, project):
    """
    Checks if the repo exists before adding it to the file.

    Requires `username` and `projects` to be fiven as arguments.
    """
    url = f"https://github.com/{username}/{project}"
    source = requests.get(url)
    return source.status_code == requests.codes.ok


def create_project_buttons(username, projects, format="Markdown") -> None:
    """
    Creates a text file with your projects set up as markdown or html image links.

    Requires `projects` to be given as arguments.
    """
    print("Starting README Stat Button Maker")
    # checks if the api is still working
    url = f"https://github-readme-stats.vercel.app/api/pin/?username=test_username&repo=test_repo"
    source = requests.get(url)
    if source.status_code != requests.codes.ok:
        print("\nREADME Stat buttons are broken.")
        return
    else:
        print("\nREADME Stat buttons are working.")
    # creates the text file with the selected format
    broken_links = []
    with open("project_buttons.md", "w") as f:
        # sets up the buttons using HTML
        if format == "html":
            f.write('<p align="center">\n')
            for name, username in projects.items():
                if check_repo(username, name):
                    f.write(f'<a href="https://github.com/{username}/{name}">\n')
                    f.write(
                        f'<img src="https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={name}" />\n'
                    )
                    f.write("<a\>\n")
                else:
                    broken_links.append(name)
            f.write("<p\>")
        # sets up the buttons using Markdown
        elif "Markdown":
            for name, username in projects.items():
                if check_repo(username, name):
                    image = f"https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={name}"
                    f.write(
                        f"[![Readme Card]({image})](https://github.com/{username}/{name})\n\n"
                    )
                else:
                    broken_links.append(name)
    print("\nFinished generating template")
    if len(broken_links) > 0:
        print("\nThe following repo's are invalid.")
        print(", ".join(broken_links))


if __name__ == "__main__":
    projects_dict = {
        "Feedly-Clone": "Concrete18",
        # "discord_clone_2": "flow-state-15",
        "Clickr-clone-of-Flickr": "Concrete18",
        "Good-Games-1-week-Group-Project": "Concrete18",
        "easierexcel": "Concrete18",
        "Game-Save-Manager": "Concrete18",
        "Game-Library-Tracker": "Concrete18",
        "Auto-Folder-Cleaner": "Concrete18",
        "Config-Auto-Backup": "Concrete18",
        "Virtual-Assistant": "Concrete18",
        "Home-Control-Interface": "Concrete18",
    }

    create_project_buttons(
        username="Concrete18", projects=projects_dict, format="Markdown"
    )
