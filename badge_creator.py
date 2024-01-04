import requests


def check_badge(badge_url):
    """
    Checks if the badge exists.
    """
    source = requests.get(badge_url)
    return source.status_code == requests.codes.ok


def create_badges(badge_data) -> None:
    """
    ph
    """
    broken_links = []
    with open("templates/badges.md", "w") as f:
        f.write('<p>\n')
        f.write(f'  <!-- Badges Link https://github.com/alexandresanlim/Badges4-README.md-Profile -->\n')
        for badge_section, badges in badge_data.items():
            f.write(f'  <!-- {badge_section} -->\n')
            for badge in badges:
                if check_badge(badge):
                    f.write(f'  <img src="{badge}" />\n')
                else:
                    broken_links.append(badge)
        f.write("<p\>")
    print("\nFinished generating badge template")
    if len(broken_links) > 0:
        print("\nThe following badges's are invalid.")
        print(", ".join(broken_links))


if __name__ == "__main__":
    badges = {
        "Languages": [
            "https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E",
            "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white",
            "https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white",
            "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white",
            "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white",
            "https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white"
        ],
        "Frameworks": [
            "https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white",
            "https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white",
            "https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB",
            "https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white",
            "https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white",
            "https://img.shields.io/badge/Jest-C21325?style=for-the-badge&logo=jest&logoColor=white",
            "https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white",
            "https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white",
        ],
        "Cloud": [
            "https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white",
            "https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white",
        ],
        "OS": [
            "https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white",
            "https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black",
            "https://img.shields.io/badge/GNU%20Bash-4EAA25?style=for-the-badge&logo=GNU%20Bash&logoColor=white"
        ],
        "Misc": [
            "https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white",
            "https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white",
            "https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white",
            "https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white"
            "https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white",
            "https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white",
            "https://img.shields.io/badge/gimp-5C5543?style=for-the-badge&logo=gimp&logoColor=white",
            "https://img.shields.io/badge/Adobe%20Photoshop-31A8FF?style=for-the-badge&logo=Adobe%20Photoshop&logoColor=black",
        ]
    }
    create_badges(badges)
