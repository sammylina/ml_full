#!/usr/bin/env python3
"""
1. From Dictionary
"""
import pandas as pd


dictionary = {
    "First": [0.0, 0.5, 1.0, 1.5],
    "Second": ["one", "two", "three", "four"]
}
df = pd.DataFrame(dictionary, index=list("ABCD"))
