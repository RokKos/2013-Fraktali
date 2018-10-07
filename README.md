# 2013-Fraktali

Fraktali na krožku 2013

## Navodila

Vsak si bo izbral neki fraktal. Vsak program mora imeti dve funkciji:

    def make_fractal(ulx, uly, drx, dry, img_width):
        return "slika_fraktala"
in

    def default_settings():
        return "seznam petih najlepših parametrov za make_fractal"


Uporabljali bomo dve zunanji knjižnjici, NumPy in Pillow, za hitro računanje in
delo s slikami. Dobite jih tukaj, inštalirajte pravo verzijo glede na Python,
ki ga imate na računalniku.

* [Pillow](https://pypi.python.org/pypi/Pillow/2.3.0#downloads) verzija 2.3.0
* [NumPy](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy) verzija 1.8.0

Če nimate admin pravic ne morete instalirati z uporabo .exe datoteke, zato je
treba dobiti Python source (ponavadi .tar.gz ali .rar) in ga instalirati na
roke. To naredite tako, da odpakirate downloadano datoteko (vsebovati mora
datoteko `setup.py`) in nato v komandni vrstici zaženete `python setup.py
install`.

Npr. če ste stvar downloadali na namizje, bi na šolskih računalnikih
instalirali tako, da bi odprli command prompt in izvedli ukaze:

    cd Namizje/Pillow
    python setup.py install

Če ste na šolskih računalnikih, bo namesto `python` verjetno treba vpisati
celotno pot, torej nekaj kot `C:\Python32\python.exe setup.py install`.

Če kdo slučajno uporablja Linux, naj kontaktira
[Natana](mailto:natan.zabkar@gmail.com) za navodila.

Linux navodila za Python 3.6.6, Numpy 1.15.2, Pillow 5.3.0:

```bash
sudo apt-get install python3 (ali sudo dnf install python3)
sudo pip3 install -I --no-cache-dir numpy 
sudo pip3 install -I --no-cache-dir Pillow 
```

Uporabo si poglejte na primeru v datoteki numpy_pillow_example.py

## Seznam:

* Jon Galonja (Jonislav) - [Dragon curve] (http://hollymath.com/2013/06/04/fractal-education-the-dragon-curve/)
* Jure Slak (jureslak) - [Mandelbrot set](http://en.wikipedia.org/wiki/Mandelbrot_set)
* Natan Žabkar (nightmarebadger) - [eden izmed "krožnih"
  fraktalov](https://www.google.si/search?q=circle+fractal&tbm=isch)
* Jaka Grbac (chemlife) -[apollonian gasket](http://en.wikipedia.org/wiki/Apollonian_gasket)
* Miha Černe(MracniPingvin) -[Julia set](http://en.wikipedia.org/wiki/Julia_set)
* Jure Tič (CapitanPirk) - [Zlata / Fibonaccijeva
  spirala](http://en.wikipedia.org/wiki/Golden_spiral)
* Lucija Gruden (lucigruden) - hexaflake
* Aljaž Podgornik (whiterocket) - [Sierpinski trikotnik](http://en.wikipedia.org/wiki/Sierpinski_triangle)
* Rok Kovač (kovarok) - [Pitagorejsko drevo](http://en.wikipedia.org/wiki/Pythagoras_tree_%28fractal%29)


## Primer:
Julia sets - [Rok Kos](https://github.com/RokKos)

![Julia set 01][Julia-set-01]

![Julia set 02][Julia-set-02]

![Julia set 03][Julia-set-03]

![Julia set 04][Julia-set-04]


[Julia-set-01]:		https://github.com/RokKos/2013-Fraktali/blob/master/img/julia_set_0.png
 "Julia set 01"
 [Julia-set-02]:		https://github.com/RokKos/2013-Fraktali/blob/master/img/julia_set_2.png
 "Julia set 02"
[Julia-set-03]:		https://github.com/RokKos/2013-Fraktali/blob/master/img/julia_set_3.png
 "Julia set 03"
 [Julia-set-04]:		https://github.com/RokKos/2013-Fraktali/blob/master/img/julia_set_4.png
 "Julia set 04"
