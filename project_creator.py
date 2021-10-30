import requests


def check_repo(username, project):
    '''
    Checks if the repo exists before adding it to the file.
    
    Requires `username` and `projects` to be fiven as arguments.
    '''
    url = f'https://github.com/{username}/{project}'
    source = requests.get(url)
    return source.status_code == requests.codes.ok


def create_project_buttons(username, projects, format='Markdown') -> None:
    '''
    Creates a text file with your projects set up as markdown or html image links.

    Requires `username` and `projects` to be fiven as arguments.
    '''
    # checks
    url = f'https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={projects[0]}'
    source = requests.get(url)
    if source.status_code != requests.codes.ok:
        print('Buttons are broken.')
        return
    # checks
    broken_links = []
    with open('project_buttons.txt', 'w') as f:
        if format == 'html':
            f.write('<p align="center">\n')
            for project in projects:
                if check_repo(username, project):
                    f.write(f'<a href="https://github.com/{username}/{project}">\n')
                    f.write(f'<img src="https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={project}" />\n')
                    f.write('<a\>\n')
                else:
                    broken_links.append(project)
            f.write('<p\>')
        elif 'Markdown':
            for project in projects:
                if check_repo(username, project):
                    image = f'https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={project}'
                    f.write(f'[![Readme Card]({image})](https://github.com/{username}/{project})\n\n')
                else:
                    broken_links.append(project)
    print(broken_links)


if __name__ == '__main__':

    projects_list = [
        "Clickr-clone-of-Flickr",
        "Good-Games-1-week-Group-Project",
        "Game-Save-Manager",
        "Auto-Folder-Cleaner",
        "Config-Auto-Backup",
        "Virtual-Assistant",
        "Home-Control-Interface",
        "Weather-Wallpaper-Changer",
        "Standing-Reminder",
        "Timed-Shutdown-Sleep"
        ]

    create_project_buttons(username='Concrete18', projects=projects_list, format='Markdown')
