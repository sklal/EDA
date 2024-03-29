# Metal Music - Metal is the feeling of being an outsider, but still being part of something huge.
# As Sam Dunn, the award winning documentary filmmaker and anthropologist said "If metal doesn't give that overwhelming surge of power that make the hair stand up at the back of your neck, you might never get it, and you know what? That's okay"
# As a fan of the extremely loved/hated genre of music. This is my attempt to make sense of the information I have on the music.
import pandas as pd
import numpy as np
import re
import seaborn as sns
from matplotlib import pyplot as plt
from collections import Counter
import matplotlib._color_data as mcd
# Loading the Dataset
metal = pd.read_csv(
    "D:\\Data Science\\Metal music\\Metal.csv", encoding="ISO-8859-1")
# Shape
metal.shape
# Check for the top few rows of the dataset
metal.head()
# Check for Data types
metal.dtypes
# Data cleaning
# Dropping the unnecessary column
metal.drop(['Unnamed: 0'], axis=1, inplace=True)
# Now that the unnecessary column has been dropped, let's make changes to the column names by standardizing them.
metal.rename({'band_name': 'Band Name', 'fans': 'Fans', 'formed': 'Year Formed',
              'origin': 'Place of origin', 'split': 'Split', 'style': 'Genre'}, axis=1, inplace=True)
metal['Band Name'] = metal['Band Name'].astype('category')
metal['Fans'] = metal['Fans'].astype('int64')
metal['Place of origin'] = metal['Place of origin'].astype('category')
metal['Split'] = metal['Split'].astype('category')
metal['Genre'] = metal['Genre'].astype('category')
metal.head()
metal.dtypes
#
metal['Split'] = metal['Split'].replace(['-'], 'NA')
# Duplicates
metal['Band Name'].duplicated().sum()
# Group the duplicates
pd.concat(dup for _, dup in metal.groupby("Band Name") if len(dup) > 1)
# Drop duplicates
metal.drop_duplicates(subset=None, keep='first', inplace=True)
metal.shape
# Genre - There are a lot of sub genres, let's try to categorize them into fewer genres.
metal['Genre'] = list(map(lambda x: x.lower(), metal['Genre']))


metal.loc[metal['Genre'].str.contains("black"), 'Genre'] = 'Black'
metal.loc[metal['Genre'].str.contains("thrash"), 'Genre'] = 'Thrash'
metal.loc[metal['Genre'].str.contains("progressive"), 'Genre'] = 'Progressive'
metal.loc[metal['Genre'].str.contains("heavy"), 'Genre'] = 'Heavy'
metal.loc[metal['Genre'].str.contains("death"), 'Genre'] = 'Death'
metal.loc[metal['Genre'].str.contains("power"), 'Genre'] = 'Power'
metal.loc[metal['Genre'].str.contains("industrial"), 'Genre'] = 'Industrial'
metal.loc[metal['Genre'].str.contains("folk"), 'Genre'] = 'Folk'
metal.loc[metal['Genre'].str.contains("rock"), 'Genre'] = 'Hard Rock'
metal.loc[metal['Genre'].str.contains("hardcore"), 'Genre'] = 'Hard Rock'
metal.loc[metal['Genre'].str.contains("psychedelic"), 'Genre'] = 'Stoner'
metal.loc[metal['Genre'].str.contains("alternative"), 'Genre'] = 'Alternative'
metal.loc[metal['Genre'].str.contains("punk"), 'Genre'] = 'Alternative'
metal.loc[metal['Genre'].str.contains("doom"), 'Genre'] = 'Doom'
metal.loc[metal['Genre'].str.contains("metalcore"), 'Genre'] = 'Metalcore'
metal.loc[metal['Genre'].str.contains("grindcore"), 'Genre'] = 'Grindcore'
metal.loc[metal['Genre'].str.contains("goregrind"), 'Genre'] = 'Doom'
metal.loc[metal['Genre'].str.contains("gothic"), 'Genre'] = 'Gothic'
metal.loc[metal['Genre'].str.contains("sludge"), 'Genre'] = 'Doom'
metal.loc[metal['Genre'].str.contains("symphonic"), 'Genre'] = 'Symphonic'
metal.loc[metal['Genre'].str.contains("groove"), 'Genre'] = 'Groove'
metal.loc[metal['Genre'].str.contains("extreme"), 'Genre'] = 'Extreme'
metal.loc[metal['Genre'].str.contains("dark"), 'Genre'] = 'Doom'
metal.loc[metal['Genre'].str.contains("avantgarde"), 'Genre'] = 'Avantgarde'
metal.loc[metal['Genre'].str.contains("modern"), 'Genre'] = 'Heavy'
metal.loc[metal['Genre'].str.contains(
    "instrumental"), 'Genre'] = 'Instrumental'
metal.loc[metal['Genre'].str.contains("nu"), 'Genre'] = 'Nu'
metal.loc[metal['Genre'].str.contains("djent"), 'Genre'] = 'Progressive'
metal.loc[metal['Genre'].str.contains("shoegaze"), 'Genre'] = 'Black'
metal.loc[metal['Genre'].str.contains("suomi"), 'Genre'] = 'Suomi'
metal.loc[metal['Genre'].str.contains("grunge"), 'Genre'] = 'Alternative'
metal.loc[metal['Genre'].str.contains("math"), 'Genre'] = 'Progressive'
metal['Genre'] = list(map(lambda x: x.capitalize(), metal['Genre']))
metal['Genre'].value_counts()

print("There are {} Metal bands with {} attributes in this dataset. \n".format(
    metal.shape[0], metal.shape[1]))

print("There are {} countries producing Metal Music in this dataset such as {}... \n".format(len(metal['Place of origin'].unique()),
                                                                                             ", ".join(metal['Place of origin'].unique()[0:5])))
print("There are {} subgenres of Metal Music in this dataset".format(
    len(metal['Genre'].value_counts())))


plt.figure(figsize=(20, 8))
bands_country = metal['Place of origin'].value_counts()
plt.title('No. of Bands per Country')
sns.barplot(x=bands_country[:15].keys(),
            y=bands_country[:15].values, palette="GnBu_d")
# We can see most number of metal bands are coming out of the USA.


plt.figure(figsize=(20, 8))
bands_genre = metal['Genre'].value_counts()
plt.title('No. of Bands per Genre')
sns.barplot(x=bands_genre[:15].keys(),
            y=bands_genre[:15].values, palette="PuBuGn_d")

# Black metal genre has the most number of bands in this dataset


# Let's see the spread of Genre across the USA
# Subsetting the data for USA
usa = metal[metal['Place of origin'] == 'USA']
plt.figure(figsize=(20, 8))
usa_genre = usa['Genre'].value_counts()
plt.title('No. of Bands per Genre in the USA')
sns.barplot(x=usa_genre[:15].keys(), y=usa_genre[:15].values, palette="Reds")

# We can see that although Black metal genre has the most number of bands throughout the world, No. of Death metal bands exceeds it in the USA

# Popularity of metal over the years in the USA
plt.figure(figsize=(30, 8))
Fans_year = usa.groupby('Year Formed')['Fans'].sum()
plt.title('Counts of Fans per Year')
sns.barplot(x=Fans_year[:46].keys(), y=Fans_year[:46].values, palette="GnBu_d")

# There's a peak in 1981,1983 and 1985!

# On the flip side, the genre has lost popularity in the USA since 2005, witnessing a significant drop!

# Looking at the positive

usa[(usa.Fans >= 700) & (usa['Year Formed'].isin(['1981', '1983', '1985']))]

# The Big 4 of Thrash Metal - Metallica, Megadeth, Anthrax & Slayer were formed in these mentioned years |m/. That's HUGE!

# Spread of Death metal bands over the years
death_usa = usa['Genre'].eq('Death').groupby(usa['Year Formed']).sum()
plt.figure(figsize=(30, 8))
death_usa.plot(kind='bar', color=mcd.CSS4_COLORS)

# After 1993, there is a rise in the no. of bands in 2005,2006,2008 and 2009
usa[(usa.Genre == 'Death') & (usa['Year Formed'].isin(
    ['1993', '2005', '2006', '2008', '2009']))]

# Nile, Dethklok & Six Feet Under. WOW!!!!!!

# Top 5 bands in the US on the basis of no. of fans
top5_usa = usa.nlargest(5, 'Fans')
plt.figure(figsize=(16, 8))
# plot chart
ax1 = plt.subplot(121, aspect='equal')
top5_usa.plot(kind='pie', y='Fans', ax=ax1, autopct='%1.1f%%',
              startangle=90, shadow=False, labels=top5_usa['Band Name'], legend=False, fontsize=14, title="Top 5 Metal bands in the USA")


# Let's have a look at the pioneers of Metal music
metal[(metal.Fans >= 700) & (metal['Year Formed'] < '1980')]

# Iron Maiden, Black Sabbath, AC/DC, Motorhead, Judas Priest. LEGENDS!!!!
