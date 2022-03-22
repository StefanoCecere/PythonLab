import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read the json file into a dataframe
df = pd.read_json('posts/your_posts_1.json')

df.head()

# rename the timestamp column
df.rename(columns={'timestamp': 'date'}, inplace=True)

#drop some unnecessary columns
df = df.drop(['attachments', 'title', 'tags'], axis=1)

df.info()

# making sure it's datetime format
#pd.to_datetime(df['date'])

#df.head(3)
#print(df.shape)
df.tail(5)

df = df.set_index('date')
#print(df.shape)
post_counts = df['data'].resample('MS').size()
post_counts.tail(50)

# set figure size and font size
sns.set(rc={'figure.figsize':(50,20)})
sns.set(font_scale=3)

# set x labels
x_labels = post_counts.index

#create bar plot
sns.barplot(x_labels, post_counts, color="blue")

# only show x-axis labels for Jan 1 of every other year
tick_positions = np.arange(10, len(x_labels), step=24)

#reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))

# display the plot
plt.show()
