# CS335-lyric-compare

### Libraries: 

This python program uses the click, pandas, scikit-learn, and pandas libraries. 
Running "setup.py" (see section below) should install all required libraries- 
however, each one can be installed manually if needed. 

### Set-up: 
Open a command line instance and navigate to the lyric_compare folder. 
Then, run `pip install --editable .` to install all related libraries.
From there, the program can be run by using `python lyric_compare.py`.
If you do not have python installed, refer to the [Beginner's Guide Docs](https://wiki.python.org/moin/BeginnersGuide/Download) to install the appropriate version. 

### Running the program:
Running `python lyric_compare.py` will cause the program to ask the user for a prompt (string) to compare songs against. 

```
>python lyric_compare.py
Give me a song about...: 
```

This step can also be skipped by adding `--prompt` and the prompt you want to compare against the lyrics in quotes. 
```
>python lyric_compare.py --prompt "rising under pressure"
   Score  Song Title      Artist
--------  --------------  -----------
0.144908  Pressure        Lupe Fiasco
0.11038   Reset           Curren$y
0.104296  Can U Get Away  2Pac

Done!
```
Options can also be specified using the short or long notation. 

A user can choose the size of the dataset used by adding `--size` or `--s`, choosing from `mini`, `medium`, or `large`. 
If no option is specified, `medium` will be used by default. 

```
>python lyric_compare.py --size mini
Give me a song about...: the future
    Score  Song Title    Artist 
---------  ------------  ------------
0.053389   Dreams        Domo Genesis
0.0329722  C Section     Canibus
0.0284148  Fly Out       Lil Wayne

Done!
```
```
>python lyric_compare.py --s mini
Give me a song about...: money
   Score  Song Title        Artist
--------  ----------------  -----------------
0.274979  Money On My Mind  Lil Wayne
0.19508   Ski Mask Way      50 Cent
0.166086  Get Money         Junior M.A.F.I.A.

Done!
```

```
>python lyric_compare.py --size large
Give me a song about...: insomnia
   Score  Song Title      Artist
--------  --------------  -----------
0.313875  Insomnia        Shoayb khan
0.26545   Insomnia        Dirty Heads
0.159699  Somnus Nemoris  Detox

Done!
```
```
>python lyric_compare.py --s large
Give me a song about...: becoming someone else
0.530433  Meanwhile     Foreign Legion
   Score  Song Title    Artist
--------  ------------  --------------
0.530433  Meanwhile     Foreign Legion
0.368707  Somedays      Regina Spektor
0.359285  I Want To     Left Boy

Done!
```

A user can dictate the number of results returned by using `--results` or `--r` and entering the number of desired results (as an integer). 
If no option is specified, 3 results/songs will be returned by default.
```
>python lyric_compare.py --results 5
Give me a song about...: rising under pressure
    Score  Song Title       Artist
---------  ---------------  ------------
0.144908   Pressure         Lupe Fiasco
0.11038    Reset            Curren$y
0.104296   Can U Get Away   2Pac
0.0964363  Under Pressure   Thug Life
0.0927655  Lord Have Mercy  Beanie Sigel

Done!
```
```
python lyric_compare.py --r 1
Give me a song about...: rising under pressure
    Score  Song Title       Artist
---------  ---------------  ------------
0.144908   Pressure         Lupe Fiasco

Done!
```

All of these options can be combined into one command. 

```
python lyric_compare.py --prompt "rising under pressure" --r 5 --s mini
    Score  Song Title    Artist
---------  ------------  --------------
0.0386015  Love Is Love  AZ
0.0247058  Evening News  Chamillionaire
0.020491   I Told Yall   Lil Wayne
0.0196262  Illin         Jeezy
0.0164012  Dumb It Down  Lupe Fiasco

Done!
```

A summarized version of this information can be found by running `python lyric_compare.py --help`.
```
Usage: lyric_compare.py [OPTIONS]

  Compares input prompt to various song lyrics.

Options:
  --prompt TEXT           Prompt to compare lyrics against.  [required]
  --size, --s TEXT        Size of song dataset to use: [mini|medium|large]
  --results, --r INTEGER  Number of songs to return.
  --help                  Show this message and exit.
```

###Testing:
Several test prompts have been included in testPrompts.txt along with directions, sample outputs, and the dataset used for each query.
The lyrics used should return their respective songs within the top 3 results.

