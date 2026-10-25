import os,shutil,glob
from PIL import Image, ImageDraw, ImageFont
ACT="#a4b9c6"
P={
"dark":dict(bg="#1e1e1e",side="#2a2a2c",fg="#e6e6e6",mut="#98989d",fa="#636366",sel="#3a3a3c",hov="#2c2c2e",bor="#48484a",g1="#c7c7cc",g2="#9a9a9f"),
"light":dict(bg="#ffffff",side="#ececec",fg="#1d1d1f",mut="#6e6e73",fa="#a1a1a6",sel="#48484a",hov="#e5e5ea",bor="#d2d2d7",g1="#3a3a3c",g2="#6e6e73"),
}
OPEN,CLOSE="\\uE0B6","\\uE0B4"
for m,c in P.items():
    d_=f"macos-{m}.yazi";os.makedirs(d_,exist_ok=True)
    a=ACT
    t=f'''# macOS Finder inspired ({m}) flavor for Yazi
# Grayscale text only; {a} for active text; pill-shaped tabs/status (Nerd Font required)
[mgr]
cwd = {{ fg = "{c['g1']}", bold = true }}
hovered         = {{ fg = "{a}", bg = "{c['sel']}" }}
preview_hovered = {{ fg = "{a}", bg = "{c['sel']}" }}
find_keyword  = {{ fg = "{a}", bold = true, underline = true }}
find_position = {{ fg = "{c['mut']}", bold = true }}
marker_copied   = {{ fg = "{c['g2']}", bg = "{c['g2']}" }}
marker_cut      = {{ fg = "{c['fa']}", bg = "{c['fa']}" }}
marker_marked   = {{ fg = "{a}", bg = "{a}" }}
marker_selected = {{ fg = "{a}", bg = "{a}" }}
count_copied   = {{ fg = "{a}", bg = "{c['sel']}" }}
count_cut      = {{ fg = "{a}", bg = "{c['sel']}" }}
count_selected = {{ fg = "{a}", bg = "{c['sel']}" }}
border_symbol = "│"
border_style  = {{ fg = "{c['bor']}" }}
syntect_theme = "~/.config/yazi/flavors/macos-{m}.yazi/tmtheme.xml"

[tabs]
active   = {{ fg = "{a}", bg = "{c['sel']}", bold = true }}
inactive = {{ fg = "{c['mut']}", bg = "{c['hov']}" }}
sep_inner = {{ open = "{OPEN}", close = "{CLOSE}" }}
sep_outer = {{ open = "", close = "" }}

[mode]
normal_main = {{ fg = "{a}", bg = "{c['sel']}", bold = true }}
normal_alt  = {{ fg = "{c['mut']}", bg = "{c['hov']}" }}
select_main = {{ fg = "{a}", bg = "{c['sel']}", bold = true }}
select_alt  = {{ fg = "{c['mut']}", bg = "{c['hov']}" }}
unset_main  = {{ fg = "{a}", bg = "{c['sel']}", bold = true }}
unset_alt   = {{ fg = "{c['mut']}", bg = "{c['hov']}" }}

[status]
overall   = {{ }}
sep_left  = {{ open = "{OPEN}", close = "{CLOSE}" }}
sep_right = {{ open = "{OPEN}", close = "{CLOSE}" }}
perm_sep   = {{ fg = "{c['fa']}" }}
perm_type  = {{ fg = "{c['g1']}" }}
perm_read  = {{ fg = "{c['g2']}" }}
perm_write = {{ fg = "{c['g2']}" }}
perm_exec  = {{ fg = "{c['g1']}" }}
progress_label  = {{ fg = "{c['fg']}", bold = true }}
progress_normal = {{ fg = "{a}", bg = "{c['hov']}" }}
progress_error  = {{ fg = "{c['mut']}", bg = "{c['hov']}" }}

[which]
cols = 3
mask = {{ bg = "{c['side']}" }}
cand = {{ fg = "{a}" }}
rest = {{ fg = "{c['fa']}" }}
desc = {{ fg = "{c['fg']}" }}
separator = "  "
separator_style = {{ fg = "{c['fa']}" }}

[confirm]
border  = {{ fg = "{c['bor']}" }}
title   = {{ fg = "{c['g1']}", bold = true }}
content = {{ fg = "{c['fg']}" }}
list    = {{ fg = "{c['fg']}" }}
btn_yes = {{ fg = "{a}", bg = "{c['sel']}" }}
btn_no  = {{ fg = "{c['mut']}", bg = "{c['hov']}" }}

[spot]
border   = {{ fg = "{c['bor']}" }}
title    = {{ fg = "{c['g1']}", bold = true }}
tbl_col  = {{ fg = "{c['mut']}", bold = true }}
tbl_cell = {{ fg = "{a}", bg = "{c['sel']}" }}

[notify]
title_info  = {{ fg = "{a}" }}
title_warn  = {{ fg = "{c['g1']}" }}
title_error = {{ fg = "{c['g1']}", bold = true }}

[pick]
border   = {{ fg = "{c['bor']}" }}
active   = {{ fg = "{a}", bg = "{c['sel']}" }}
inactive = {{ fg = "{c['fg']}" }}

[input]
border   = {{ fg = "{c['bor']}" }}
title    = {{ fg = "{c['mut']}" }}
value    = {{ fg = "{c['fg']}" }}
selected = {{ fg = "{a}", bg = "{c['sel']}" }}

[cmp]
border   = {{ fg = "{c['bor']}" }}
active   = {{ fg = "{a}", bg = "{c['sel']}" }}
inactive = {{ fg = "{c['fg']}" }}

[tasks]
border  = {{ fg = "{c['bor']}" }}
title   = {{ fg = "{c['g1']}", bold = true }}
hovered = {{ fg = "{a}", bg = "{c['sel']}" }}

[help]
on      = {{ fg = "{a}" }}
run     = {{ fg = "{c['g1']}" }}
desc    = {{ fg = "{c['mut']}" }}
hovered = {{ fg = "{a}", bg = "{c['sel']}" }}
footer  = {{ fg = "{c['fg']}" }}

[filetype]
rules = [
  {{ mime = "image/*", fg = "{c['g2']}" }},
  {{ mime = "video/*", fg = "{c['g2']}" }},
  {{ mime = "audio/*", fg = "{c['g2']}" }},
  {{ mime = "application/*", fg = "{c['g2']}" }},
  {{ url = "*", is = "orphan", fg = "{c['fa']}" }},
  {{ url = "*", is = "exec", fg = "{c['g1']}" }},
  {{ url = "*/", fg = "{c['g1']}", bold = true }},
  {{ url = "*", fg = "{c['fg']}" }},
]
'''
    open(f"{d_}/flavor.toml","w").write(t)
    def s(n,sc,co,ex=""):
        return f'<dict><key>name</key><string>{n}</string><key>scope</key><string>{sc}</string><key>settings</key><dict><key>foreground</key><string>{co}</string>{ex}</dict></dict>'
    it=[s("Comment","comment",c['fa'],"<key>fontStyle</key><string>italic</string>"),s("String","string",c['g2']),s("Number","constant.numeric",c['g2']),s("Keyword","keyword, storage",a,"<key>fontStyle</key><string>bold</string>"),s("Function","entity.name.function, support.function",a),s("Type","entity.name.type, support.type, support.class",c['g1']),s("Constant","constant, variable.language",c['g1']),s("Tag","entity.name.tag",a),s("Attr","entity.other.attribute-name",c['g2'])]
    open(f"{d_}/tmtheme.xml","w").write(f'''<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0"><dict><key>name</key><string>macOS {m}</string><key>settings</key><array>
<dict><key>settings</key><dict><key>background</key><string>{c['bg']}</string><key>foreground</key><string>{c['fg']}</string><key>caret</key><string>{a}</string><key>selection</key><string>{c['sel']}</string><key>lineHighlight</key><string>{c['hov']}</string></dict></dict>
{chr(10).join(it)}
</array></dict></plist>''')
    open(f"{d_}/LICENSE","w").write("MIT License\n")
    fp=glob.glob('/usr/share/fonts/**/DejaVuSansMono.ttf',recursive=True)[0];fb=glob.glob('/usr/share/fonts/**/DejaVuSansMono-Bold.ttf',recursive=True)[0]
    F=ImageFont.truetype(fp,17);B=ImageFont.truetype(fb,17)
    par=["Applications/","Desktop/","Documents/","Downloads/","Library/","Movies/","Music/","Pictures/","backup.zip","cover.png","demo.mp4","notes.md","report.pdf","setup.sh","track.mp3"]
    files=[("Projects/",1),("Themes/",1),("Icons/",1),("macos.yazi/",1),("README.md",0),("flavor.toml",0),("preview.png",0)]
    W,H,lh=1200,560,28
    im=Image.new("RGB",(W,H),c['bg']);d=ImageDraw.Draw(im)
    d.rounded_rectangle([16,5,170,29],12,fill=c['sel']);d.text((30,7),"1 Documents",font=B,fill=a)
    d.rounded_rectangle([180,5,260,29],12,fill=c['hov']);d.text((194,7),"2 ~",font=F,fill=c['mut'])
    x1,x2=300,760
    for x in (x1,x2): d.line([x,40,x,H-44],fill=c['bor'])
    for i,n in enumerate(par): d.text((14,48+i*lh),n,font=B if n.endswith("/") else F,fill=c['g1'] if n.endswith("/") else c['fg'])
    for i,(n,dr) in enumerate(files):
        y=48+i*lh;hv=i==3
        if hv: d.rounded_rectangle([x1+6,y-3,x2-6,y+lh-5],12,fill=c['sel'])
        d.text((x1+16,y),n,font=B if dr else F,fill=a if hv else (c['g1'] if dr else c['fg']))
        d.text((x2-70,y),str(i+3) if dr else "4K",font=F,fill=a if hv else c['mut'])
    pv=["name: macos-"+m,"version: 1.0","active: "+a,"","[mgr]",'hovered = { fg = "'+a+'" }','border_symbol = "│"']
    for i,l in enumerate(pv): d.text((x2+16,48+i*lh),l,font=F,fill=c['mut'] if l.startswith("[") else c['fg'])
    d.rounded_rectangle([8,H-34,100,H-8],13,fill=c['sel']);d.text((22,H-32),"NORMAL",font=B,fill=a)
    d.rounded_rectangle([110,H-34,200,H-8],13,fill=c['hov']);d.text((126,H-32),"4.0K",font=F,fill=c['mut'])
    d.rounded_rectangle([210,H-34,370,H-8],13,fill=c['hov']);d.text((226,H-32),"drwxr-xr-x",font=F,fill=c['mut'])
    d.rounded_rectangle([W-100,H-34,W-8,H-8],13,fill=c['sel']);d.text((W-84,H-32),"4/15",font=F,fill=a)
    im.save(f"{d_}/preview.png")
    k=m
    open(f"{d_}/README.md","w").write(f"""<div align="center">
  <h1>macOS {m.capitalize()} Flavor for <a href="https://github.com/sxyazi/yazi">Yazi</a></h1>
</div>

A Finder-inspired {m} flavor for Yazi: grayscale text only, `{a}` for active text, and pill-shaped tabs and status bar segments.

## Preview

![preview](preview.png)

## Requirements

A recent Yazi release with flavor support and a [Nerd Font](https://www.nerdfonts.com/) in your terminal, which draws the rounded pill ends.

## Installation

```sh
ya pkg add <your-github-user>/<your-repo>:macos-{m}
```

Or copy this folder to `~/.config/yazi/flavors/macos-{m}.yazi/`.

## Usage

Add this to `~/.config/yazi/theme.toml`:

```toml
[flavor]
{k} = "macos-{m}"
```

To follow the system appearance, use both flavors:

```toml
[flavor]
dark  = "macos-dark"
light = "macos-light"
```

## Palette

| Role | Color |
|------|-------|
| Background | `{c['bg']}` |
| Text | `{c['fg']}` |
| Secondary text | `{c['mut']}` |
| Active text | `{a}` |
| Selection and pills | `{c['sel']}` |
| Borders | `{c['bor']}` |

## License

Released under the MIT License. See [LICENSE](LICENSE).
""")
open("theme.toml","w").write('[flavor]\ndark  = "macos-dark"\nlight = "macos-light"\n')
open("README.md","w").write("""# macOS Yazi Flavors

Finder-inspired dark and light flavors for Yazi. Grayscale text, `#a4b9c6` for active text, pill-shaped tabs and status bar (Nerd Font required).

![dark](macos-dark.yazi/preview.png)
![light](macos-light.yazi/preview.png)

## Install

Copy `macos-dark.yazi` and `macos-light.yazi` to `~/.config/yazi/flavors/`, then add to `~/.config/yazi/theme.toml`:

```toml
[flavor]
dark  = "macos-dark"
light = "macos-light"
```
""")
o=os.path.expanduser('~/output');os.makedirs(o,exist_ok=True)
shutil.make_archive('/tmp/macos-yazi-flavors','zip','.');shutil.move('/tmp/macos-yazi-flavors.zip',o+'/macos-yazi-flavors.zip')
shutil.copy('macos-dark.yazi/preview.png',o+'/preview-dark.png');shutil.copy('macos-light.yazi/preview.png',o+'/preview-light.png')
