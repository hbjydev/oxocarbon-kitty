import yaml
import jinja2


def read_theme(name: str):
    theme = {}

    with open(f"theme/base16-oxocarbon-{name}.yaml", "r") as f:
        theme = yaml.safe_load(f)
        f.close()

    return theme


def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("./templates/"))
    tmp = env.get_template("skin.conf.j2")
    thm = read_theme('dark')

    con = tmp.render(thm)

    open('skin.conf', 'w').close()

    with open('skin.conf', 'w') as f:
        f.write(con)
        f.close()


main()
