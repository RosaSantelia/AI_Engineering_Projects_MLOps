from datasets import load_dataset
import re

def preprocess(text: str) -> str:
    text = re.sub(r'http\S+', 'http', text)
    text = re.sub(r'@\w+', '@user', text)
    return text

def load_tweet_eval():
    dataset = load_dataset("tweet_eval", "sentiment")
    # Applichiamo preprocess ai testi di train/test
    for split in ['train', 'test', 'validation']:
        if split in dataset:
            dataset[split] = dataset[split].map(lambda x: {'text': preprocess(x['text'])})
    return dataset
