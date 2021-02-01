![Poker PRNG](https://raw.githubusercontent.com/nlo-portfolio/nlo-portfolio.github.io/master/style/images/programs/poker-prng.png "Poker PRNG")

## Description ##

PokerPRNG contains two command-line applications:<br>
&emsp;PokerPRNG uses poker hands to evaluate the distribution of random numbers.<br>
&emsp;PokerCLI evaluates a given poker hand in the form of a string.<br>

## Dependencies ##

Ubuntu<br>
Python v3<br>
\* All required components are included in the provided Docker image.

## Usage ##

Ubuntu:

```
python3 poker_prng.py
python3 poker_cli.py
python3 -m unittest --verbose
```

Docker:

```
docker-compose build
docker-compose run <poker-prng | poker-cli | test>
```
