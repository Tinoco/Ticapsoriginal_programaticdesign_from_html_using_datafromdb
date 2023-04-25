# import sqlite3 lib to acess db
import sqlite3 as sql
# import tqdm to see progress
from tqdm import tqdm
# import html2image to convert html to image
from html2image import Html2Image

programatichtmltopng = Html2Image()


# Class to manage database methods
class Datacenter():
    bd = "programatic.sqlite3"
    conn = None
    cur = None
    connected = False

    def connect(self):
        Datacenter.conn = sql.connect(Datacenter.bd)
        Datacenter.cur = Datacenter.conn.cursor()
        Datacenter.connected = True

    def disconnect(self):
        Datacenter.conn.close()
        Datacenter.connected = False

    def execute(self, sql, parms=None):
        if Datacenter.connected:
            if parms == None:
                Datacenter.cur.execute(sql)
            else:
                Datacenter.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return Datacenter.cur.fetchall()

    def persist(self):
        if Datacenter.connected:
            Datacenter.conn.commit()
            return True
        else:
            return False


# database fetch data from db
def programatic():
    j = Datacenter()
    j.connect()

    j.execute("SELECT * FROM search_manager_search")

    rows = j.fetchall()
    for item in tqdm(rows):
        escope1 = str(item[1])
        escope3 = ("https://ticapsoriginal.com/"+str(item[1]).lower()+"/")
        escope2 = str(item[5]) + " "+str(item[10])

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <link rel="canonical" href="https://ticapsoriginal.com">
  
  <meta property="og:title" content="Ticapsoriginal Professional iT Networking">

  <title> Ticapsoriginal iT Professional Networking </title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
  <link rel="stylesheet" href="https://hidedomain.info/css/ticapsoriginal.css">
  <link rel="image_src" href="https://pbs.twimg.com/profile_images/1544776981245558784/fD1TGn0z_400x400.jpg"/>
  <script type="application/ld+json">

  </script>

</head>
<body style="background:#a5ce89">
  <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
  <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
  <section class="section">     
   <div class="box" style="background:#a5ce89" >
   <div class="tile is-ancestor has-text-centered">
    <div class="tile is-parent has-text-centered">
      <div class="tile is-child box">
        <div alt="Ticapsoriginal Long Description about Ticapsoriginal" class="box">

          <h2 class="title">{escope1}</h2>
          <p alt="Title of Ticapsoriginal on Ticapsoriginal with text   "> </p>
          <p alt="Description about Ticapsoriginal with text  The best learning is free learning, right? 🤓 

Find answers to all your questions here: https://ticapsoriginal.com 💡" style="margin-bottom: 2%"> {escope2}</p>
          <p alt="Description about Ticapsoriginal with text  "> </p>

        </div>
        <div class="box">
          <a target="https://ticapsoriginal.com/ar/" href="https://ticapsoriginal.com/ar/" title="Link to https://ticapsoriginal.com/ar/ ">🇸🇦</a>
          <a target="https://ticapsoriginal.com/en/Ticapsoriginal" href="https://ticapsoriginal.com/en/" title="Link to https://ticapsoriginal.com/ar/ ">🇺🇸</a>
          <a target="https://ticapsoriginal.com/es/" href="https://ticapsoriginal.com/es/" title="Link to https://ticapsoriginal.com/ar/ ">🇪🇸</a>
          <a target="https://ticapsoriginal.com/fr/" href="https://ticapsoriginal.com/fr/" title="Link to https://ticapsoriginal.com/ar/ ">🇫🇷</a>
          <a target="https://ticapsoriginal.com/hi/" href="https://ticapsoriginal.com/hi/" title="Link to https://ticapsoriginal.com/ar/ ">🇮🇳</a>
          <a target="https://ticapsoriginal.com/ja/" href="https://ticapsoriginal.com/ja/" title="Link to https://ticapsoriginal.com/ar/ ">🇯🇵</a>
          <a target="https://ticapsoriginal.com/pt-br/" href="https://ticapsoriginal.com/pt-br/" title="Link to https://ticapsoriginal.com/ar/ ">🇧🇷</a>
          <a target="https://ticapsoriginal.com/zh-hant/" href="https://ticapsoriginal.com/zh-hant/" title="Link to https://ticapsoriginal.com/ar/ ">🇨🇳</a>
        </div>  
        <div class="box">
         <div class="text-center">
        <h1>👇 Acess Now 👇</h1>
        </div>
      </div>
      <div alt="Ticapsoriginal navigator pages control"  class="box">  
        <ul class="pagination">       
            <li class="disabled"><a title="Disabled Button Ticapsoriginal" href="#!"><i class="material-icons"></i></a></li>         
            <div style="margin-right: 3px;margin-left: 3px;"> 
              <a title="Search Button Ticapsoriginal" href=https://ticapsoriginal.com/>{escope3}</a>
            </div>             
            <li  alt="Ticapsoriginal Navigator next page button"  class="waves-effect"><a title="Next page Button Ticapsoriginal" 
              href="?page=2"><i
              class="button" style="background-color: #a5ce89;">➡️</i></a></li>       
            </ul>
          </div>
        </div>
      </div>
    </div> 
  </div>
  <div alt="Ticapsoriginal Contact buttons"  class="columns box is-12">
    <div class="column"> <a title="Link to https://twitter.com/ticapsoriginal/" alt="Ticapsoriginal Twitter Link Button" href="https://twitter.com/ticapsoriginal/"><ion-icon name="logo-twitter" ></ion-icon></a></div>
    <div class="column"><a title="Link to mailto:ticaps@ticapsoriginal.com" alt="Ticapsoriginal Mail Contact Button"  href="mailto:ticaps@ticapsoriginal.com"><ion-icon name="mail-outline"></ion-icon></a></div>
    <div class="column is-four-fifths"><p alt="Ticapsoriginal Legal Advisory Term Respect Laws "  >⚠️ <strong> Legal advisory: All rights reserved </strong> for  all companies displayed. 
      The data used on this site was acquired <strong>respecting laws of public use </strong> in terms of acceptance provided by Twitter. Ticapsoriginal is not responsible for the data contained here and informs that the site may have some typing errors.</p></div>
    </div>
  </div>
</section>
<script src="https://hidedomain.info/js/ticapsoriginal.min.js"></script>
</body>
</html>"""
        programatichtmltopng.screenshot(html_str=html, save_as=str(item[1]).lower()+'.png')
    j.disconnect()
    return rows


# make programatic design html to png from db data    
programatic()
