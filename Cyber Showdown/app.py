from flask import Flask,Response,render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/robots.txt")
def robot():
    r = Response(response="User-agent: Googlebot\nDisallow: /nogooglebot/\nUser-agent: *\nAllow: /\n\n\n\n\n\n <!-- aCTF{$1t --> ", status=200, mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r

@app.route("/sitemap.xml")
def sitemap():
    r = Response(response="<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n\t<url>\n\t\t<loc>https://127.0.0.1:5000/</loc>\n\t\t<lastmod>2024-02-06</lastmod>\n\t</url>\n\n\t<url>\n\t\t<loc>https://127.0.0.1:5000/about</loc>\n\t\t<lastmod>2024-02-07</lastmod>\n\t</url>\n</urlset>\n\n\n\n\ne_M@pP3r}", status=200, mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r