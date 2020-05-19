import mistune

from flask import Blueprint, render_template, render_template_string
from pathlib import Path

blueprint = Blueprint("boids", __name__,
                      static_folder="static",
                      template_folder="templates",
                      static_url_path="/projects/boids")

@blueprint.route("/boids/")
def route():
    markdown = Path(__file__).parent / "static/markdown/boids.md"
    info = mistune.html(markdown.read_text())
    return render_template(f"boids.html", info=info)

from .. import Project
from textwrap import dedent
class Boids(Project):
    def render_html(self):
        center = "position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%)"
        container_style = f"{center}; width: 70%; text-align: center;"
        title_style = "text-decoration: underline"
        image_style = "width: 100px; height: 100px; border-radius: 20px; margin: 2em 0;"
        return render_template_string(dedent(f"""\
            <div style='{container_style}'>
                <p style='{title_style}'>Boids</p>
                <img style='{image_style}', src='{{{{ url_for('static', filename='images/boids.png') }}}}'>
                <p>A flock of boids following 3 simple rules exhibit emergent behaviour.</p>
            </div>
            """))
boids = Boids("boids", href="/boids/", blueprint=blueprint)
