# Lingo
> An experimental project that seeks to infer the gender of a person
> based on their name.


![Terminal](https://i.imgur.com/CgOoSIm.gif)


## Requirements
-  *1 GB* RAM
- **Python 3.6** and above



## Usage
Make sure you issue these commands while in the directory.

You must first train the model with the following command. This will read the file `data/training.txt` and save the trained model as json in `training.json`

```sh
python3 learn.py
```

then in order to use, run the file `Lingo.py`. You will be greeted with a `Name:` prompt as soon as the training data is loaded into memory.

```sh
python3 Lingo.py
```
  
  
## How It Works
**TL;DR:** BAYES THEOREM.

At both training and use time, each name is divided into about 300 components
called 'metrics'. A few metrics include:

- Letter pairs. For example: `adnan` is split into `ad`, `dn`, `na` ...
- Letter triplets. For example: `adnan` is split into `adn`, `dna`, `nan` ...
- Pairs and Triplets with offset from the end of the name like: `0:an`, `1:na` or `0:nan`, `1:dna`
- Singular letters with offsets. (`0:n`, `1:a`, `2:n` ...)

Each letter is also represented phonetically in multiple different ways
for example `a` can be `GutturalVowel`, `LongGutturalVowel`, `LongVowel`, `LongGuttural`, `Vowel`, `Guttural`, `Long` (See [phonetics.py](./phonetics.py) a list of representations of each letter).

These phonetic attributes are taken from the [Bengali Alphabet](https://en.wikipedia.org/wiki/Bengali_alphabet) page on [Wikipedia](https://en.wikipedia.org/wiki/Bengali_alphabet) by matching up each english letter
to the fitting phonetic doppleganger in the Bengali language.

![Phonetic Attributes](https://i.imgur.com/35N45hJ.png)


Afterwards all the combinations that can occur between the two(or three) lists of phonetic representations of the two(or three) letters in a pair(or triplet) is found and used as a metric. Examples: `GutturalVowel-LabialConsonant`, `Long-LabialAspiratedGenericConsonant-GutturalUnaspirated`, `Vowel-Consonant-Aspirated`

The combinations mentioned above is combined with the offset from the end of the name again to create yet another set of metrics. Example: `0:GutturalVowel-LabialConsonant`. These two processes account for the meat of the metrics and is what gives the model the high accuracy achieved.

_Note: Internally Lingo uses single letter short hands for traits like `Vowel` is just `v` and etc, making the actual metrics look similar to: `0:xwe-fiu`_


### Training
When learning all the about 300 metrics that each name results in are tallied up and stored in the training file for later use. The count of the number of male or female names found is also tallied for later use in Bayesian Inference.

### Inferencing
When making an inference, Lingo creates two buckets in memory the `female` bucket and `male` bucket. Then all the mtrics for the anme are found out again using the methods above.

![bayes](https://i.imgur.com/ioquSpH.png)

Finally the tally for each metric is run though a bayes probability function
multiplied by a weight based on offset and metric type and added to the bucket.

- metrics that pretain to the ends of names are given higher weights than other metrics
- phonetic trait based metric is given precedence over character based metrics.

If the percentage difference in the levels in each bucket is higher than `15%` an inference is made. Otherwise the name is considered to be Unisex.




## Accuracy
We trained the model on 32 thousand names and checked it against 3,200 names to come to the conclusion that the model is 91% accurate. In order to run this statistic, execute the file `checker.py`. Should tell you the correct and incorrect percentage soon enough.

```sh
python3 checker.py
```


## License
MIT.


## Made With ♥ By

|   ||||
|---|---|---|---|
|<img src="https://avatars1.githubusercontent.com/u/30050414?s=460&v=4" width="70">|Samiha Tahsin<br>[mahir.samiha@gmail.com](mailto:mahir.samiha@gmail.com)|<img src="https://avatars1.githubusercontent.com/u/4700757?s=460&v=4" width="70">|Omran Jamal<br>[o.jamal97@gmail.com](mailto:mahir.samiha@gmail.com)|
