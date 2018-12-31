
# Lingo

> An experimental project that seeks to infer the gender of a person
> based on their name.

  

![gif](https://media.giphy.com/media/oFDSFohmyv2c1McGp4/giphy.gif)

  

## Requirements
-  *1 GB* RAM
- Python `3.6` and above

  

## Usage
Make sure you issue these commands while in the directory.

  

### Training
You must first train the model.
```sh
python3 learn.py
```

This will read the file `data/training.txt` and save the trained model as json in `training.json`

> By default, this file contains training data for muslim names
> scraped from the internet. *32,000* names included.

  

### Run
```sh
python3 Lingo.py
```

You will be greeted with a `Name:` prompt as soon as the training data is loaded into memory.

  
  
  
  

## Accuracy

We trained the model on 32 thousand names and checked it against 3,200 names to come to the conclusion that the model is 89% accurate.

  

### Run It

```sh
python3 checker.py
```

Should tell you the accuracy in a few moments.


## License
MIT. Go Crazy.

## Made With ♥ By

|   ||||
|---|---|---|---|
|<img src="https://avatars1.githubusercontent.com/u/30050414?s=460&v=4" width="70">|Samiha Tahsin<br>[mahir.samiha@gmail.com](mailto:mahir.samiha@gmail.com)|<img src="https://avatars1.githubusercontent.com/u/4700757?s=460&v=4" width="70">|Omran Jamal<br>[o.jamal97@gmail.com](mailto:mahir.samiha@gmail.com)|
